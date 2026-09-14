---
name: drive-organizer
description: Inventory, classify, and file a large Google Drive into master folders and content-based subfolders. Resumable across sessions and usage-limit resets. Use when asked to sort, organize, clean up, or de-duplicate Google Drive, or to continue/resume Drive organizing work.
---

# Drive Organizer

Sorts a large Google Drive into master folders, then into content-based
subfolders inside them. Built to run unattended, cheaply, and to survive
session death, MCP disconnects, and usage-limit resets.

**On every invocation, read `STATE.md` in this same directory first.** It is the
authoritative record of what is done and what is next. Do the next unfinished
step, update `STATE.md`, commit, push. Never re-derive progress from Drive alone.

---

## 0. Hard safety rules (never override)

These were set by the Drive owner. They do not expire.

1. **Criminal case material about the Drive owner, and medical / health
   records: leave in place, untouched.** Do not move, rename, trash, open, or
   summarize them. Report a count only — never describe contents. The
   conversation may be shared.
2. **Credentials and credit reports** (`Chrome Passwords`, Experian /
   TransUnion / myFICO exports, password or subscription trackers): leave in
   root, untouched. Flag them to the user once.
3. **Never delete anything.** `trash_file` is only for folders you have just
   emptied yourself and verified empty. Duplicate *files* are grouped so they
   sit together and reported as a proposed delete list — the owner decides.
4. **`.exe` and other executables**: flag, never trash.
5. **Skip files created or modified in the last few hours** — the owner may be
   working in them right now.
6. Anything you cannot confidently classify goes to
   `Unidentified — needs review`. Guessing is worse than parking.

---

## 1. Environment assumptions

- Google Drive MCP tools: `search_files`, `update_file`, `create_file`,
  `trash_file`, `get_file_metadata`.
- If a call returns `MCP server "Google_Drive" session expired`, re-load the
  tools with `ToolSearch` (`select:mcp__Google_Drive__search_files,...`) and
  retry. This happens often. It is not a failure; nothing is lost.
- **The container is ephemeral.** `/tmp` scratchpad state does NOT survive.
  Only this git repo survives. Checkpoint meaningful progress into `STATE.md`
  and push.

---

## 2. The cheap-inventory trick (most important technique)

A naive `search_files` listing of a large folder dumps ~20k tokens into
context. When a tool result is oversized, the harness instead **saves it to
disk** and puts a ~300 token pointer in context — roughly 60x cheaper.

So *deliberately* inflate the payload to force that overflow:

```
search_files(
  query: "parentId = 'FOLDER_ID' and mimeType != 'application/vnd.google-apps.folder'",
  snippetVerbosity: "MAX_ALLOWED",
  pageSize: 100
)
```

Then parse from disk, never from context:

```bash
jq -r '.files[] | [.id,.mimeType,.title] | @tsv' \
  /root/.claude/projects/*/tool-results/mcp-Google_Drive-search_files-*.txt \
  > folder_all.tsv
jq -r '.nextPageToken // "none"' <same file>
```

Rules:
- **Always check `nextPageToken`** and page until it is absent.
- **Always dedupe by ID**: `sort -u -t$'\t' -k1,1` — Drive paging can repeat
  IDs across pages.
- If a page comes back inline instead of overflowing (smaller pages sometimes
  do), transcribe it to TSV by hand via heredoc rather than re-querying.
- `createdTime` is upload/sync date, **not** content date. A date filter does
  not select by content era. Say so if the user asks for "only 2024 files".

---

## 3. Classify with a script, not with the model

Per-file model reasoning is the expensive failure mode. Instead write an
ordered-regex classifier over the on-disk manifest. First match wins, so order
encodes precedence.

```python
# cls.py
import re, sys
RULES = [
  ("BUCKET_KEY", r"regex|alternatives"),
  # ... most specific first, generic catch-alls last
]
for line in open(sys.argv[1]):
    fid, mime, title = line.rstrip("\n").split("\t")
    t = title.lower()
    b = "OTHER"
    for key, pat in RULES:
        if re.search(pat, t):
            b = key
            break
    print(f"{fid}\t{b}\t{title}")
```

Then:
1. `cut -f2 plan.tsv | sort | uniq -c | sort -rn` to see bucket sizes.
2. Any bucket over ~80 files is too coarse — split it with a second pass.
3. `OTHER` is your review queue. Read those titles and add rules until OTHER
   is small; what's left goes to `Unidentified — needs review`.

Regex gotchas learned the hard way:
- `\b` does **not** match against `_`. `\bnda\b` fails on `One_Way_NDA`. Use
  `_nda|nda\b` or match the underscore explicitly.
- Titles contain typos from the owner (`opertaing`, `geeneral`, `sancomne`).
  Add the misspelling to the pattern rather than "fixing" the file.

---

## 4. Batch the moves

Create each subfolder once:

```
create_file(title: "Court orders and judgments",
            mimeType: "application/vnd.google-apps.folder",
            parentId: "<master folder id>")
```

Build an id -> destination queue, then issue **30 `update_file` calls in a
single assistant message**. `update_file(fileId, parentId)` moves;
`update_file(fileId, title)` renames. Parallel batching is what makes an
800-file sort affordable.

### Checkpoint pattern (survives disconnects)

```bash
# n.sh — print the next N unprocessed as "id dest"
grep -vFf done.txt q.tsv | head -${1:-30} | awk -F"\t" '{print $1" "$2}'
# m.sh — mark the next N as done
grep -vFf done.txt q.tsv | head -${1:-30} | cut -f1 >> done.txt
```

Call `n.sh`, fire the batch, call `m.sh`. If the session dies mid-run you lose
at most one batch, and re-moving a file to the folder it is already in is a
harmless no-op.

---

## 5. Verify before declaring a folder done

```
search_files(query: "parentId = 'MASTER_ID' and mimeType != 'application/vnd.google-apps.folder'")
```

Must return `{}` (or only deliberately-skipped files). Do this for every master
folder. A folder with loose files at its top level is **not** done — the owner
was explicit about that.

---

## 6. Merging duplicate folders

Same-named folders in root are common. For each pair:
1. Pick the KEEP folder (the one with subfolders already built, else the older).
2. Inventory the duplicate (section 2).
3. If the KEEP folder has subfolders: classify the duplicate's files
   (section 3) and move them into the *subfolders*, not the top level.
4. If not: move everything straight into KEEP.
5. Re-query the duplicate. Only when it returns `{}` — files **and** folders —
   `trash_file` it.
6. Identical names do not guarantee identical content. For folders that are
   not obvious master-folder duplicates, list both and report to the user
   before touching them.

---

## 7. Auto-resume across a usage-limit reset

The mechanism is a Routine (server-side, survives everything):

```
create_trigger(
  name: "Drive organizer — auto-resume",
  create_new_session_on_fire: true,
  notifications: { push: true, email: true },
  initiation: "human_request",
  cron_expression: "<hourly or the reset time, UTC>",
  prompt: "<standalone instructions: read .claude/skills/drive-organizer/STATE.md,
            do the next unfinished step, update STATE.md, commit, push,
            notify when the whole checklist is done>"
)
```

The fired session starts with **no memory of this conversation**, so the prompt
must be fully self-contained and must point at `STATE.md`.

When the entire checklist in `STATE.md` is complete:
- Send a `PushNotification` summarizing what was done.
- `delete_trigger` the Routine so it stops firing.

Use `send_later` for a mid-run self-check-in inside one session.
