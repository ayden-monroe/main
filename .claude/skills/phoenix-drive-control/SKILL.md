---
name: phoenix-drive-control
description: Implements and maintains the Phoenix Google Drive file-control system for a property, construction and legal operation — creating the numbered master folders, building deal/property/legal-matter workrooms, triaging loose files out of the Drive root, applying the naming and SOURCE→FINAL status standard, and keeping the Filing Queue, Master Document Index and Friday audit current. Use this skill whenever the user mentions Drive organization, filing, the Filing Queue, the Master Document Index, the Control Center, a weekly or Friday file audit, loose files in the Drive root, duplicates, a new deal or property or legal matter folder, document naming or versioning, or asks where a document should live — even if they do not name this system. Also use it before creating, renaming or moving anything in this Drive, so the structure stays consistent. The skill only files documents dated 2020 to the present, sends anything it cannot classify with confidence to a TO BE DETERMINED folder, and stops to ask permission rather than deciding on its own — particularly before undoing folder work from an earlier pass.
---

# Phoenix Drive Control

A file-control system for a business that runs real-estate acquisitions, owned property,
construction, and active litigation out of one Google Drive. The system already exists on
paper (a master directory, folder templates, a naming standard, trackers, a weekly audit).
What it does not yet have is execution. This skill executes and maintains it.

## The one thing that matters

Every operating rule in this system exists to serve a single standard:

> **Any controlling document can be found in 60 seconds, and it is obvious that it is the
> controlling version.**

When a rule and the standard conflict, the standard wins — and the rule should be fixed.

## Before doing anything

1. **Read the current state.** List the Drive root and the relevant folders. Do not assume
   the structure from these references exists yet; most of it does not.
2. **Never delete.** This skill only creates, moves, renames, and links. Deletion,
   trashing, and overwriting are the user's decisions, made one file at a time.
3. **Never touch original legal evidence.** Files that are or may be evidence get copied,
   never edited, never renamed in place. Work happens on a copy in the working-copies
   subfolder. If unsure whether something is evidence, treat it as evidence.
4. **Log every move.** Any file relocated or renamed gets a Filing Queue row recording
   where it came from and where it went. An unlogged move is a lost file.
5. **Ambiguity stops work.** A file you cannot confidently classify goes to
   `00.7 — TO BE DETERMINED` with a queue row naming the question. Do not reason your
   way to a best guess. Guessing is worse than queuing, because a confidently misfiled
   document looks filed and stops being looked for.
6. **Stay inside the date window.** Only files dated 2020-01-01 through today are in
   scope. Anything older, or undated, is left where it is and listed for the user.
7. **Stay inside the provided rules.** The master directory, folder templates, naming
   standard and trackers in `references/` are the whole system. Do not invent folders,
   categories, statuses, naming variants or workflow steps that are not in them.
8. **Ask before undoing prior work.** Earlier passes created folders and files that do
   not match current requirements. Undoing any of it needs explicit permission, item by
   item.

## Permission protocol

The default is to stop and ask, not to proceed and report. Ask — and wait — before:

- Undoing, moving, renaming or restructuring anything created by an earlier pass
- Filing anything whose destination is not unambiguous under the provided rules
- Creating any folder not listed in `references/master-directory.md` or the templates
- Touching a file dated before 2020, or one with no determinable date
- Any judgment call the rules do not already answer

When asking, state the specific decision, the options, and what you would need to know —
one concrete question beats a general request for guidance. Batch related questions into
one list rather than interrupting repeatedly, and keep working on the unambiguous items
while the answer is pending.

A question is never a failure here. Working unsupervised on someone else's live Drive is.

## Date scope

In scope: documents dated **2020-01-01 through the current date**.

Use the document's own date, and the received date only where the document carries none.
Do not use scan dates, upload dates or Drive modified dates to bring a file into scope —
a 2014 deed scanned last week is a 2014 document and stays out of scope.

Out-of-scope and undated files are not moved, not renamed and not deleted. Record them in
a list for the user with the apparent date and why they were skipped, and ask before
doing anything with them.

## Scope boundary

This skill files legal documents. It does not practice law. Do not summarize a filing as
advice, do not characterize deadlines as legal deadlines, do not draft or assess pleadings
under this skill, and do not let a well-formatted output imply that unverified content has
been checked. Filing accuracy and legal accuracy are different things, and this skill only
claims the first.

## The four jobs

Most requests are one of these. Identify which, then read the matching reference.

| Job | What it means | Read |
| --- | --- | --- |
| **Build** | Create master folders or a new workroom (deal, property, legal matter) | `references/master-directory.md`, `references/folder-templates.md` |
| **Triage** | Decide where an existing or incoming file belongs, and name it | `references/triage.md`, `references/naming-and-control.md` |
| **Track** | Write or update Control Center, Filing Queue, Master Document Index rows | `references/trackers.md` |
| **Audit** | Run the Friday review, surface and assign exceptions | `references/weekly-audit.md` |

## Build

Create folders in numeric order, at the root, using the exact names in
`references/master-directory.md`. The numbering is load-bearing: it forces the sort order
that makes the 60-second standard possible, so never renumber, abbreviate, or "clean up"
a folder name.

Two things are genuinely easy to get wrong here:

- **The root is not a workspace.** After a build, the root holds numbered master folders
  and nothing else. Loose files at root are the defining symptom this system exists to cure.
- **Numbering skips are intentional.** 16–89 are deliberately unused so new categories can
  be added without renumbering, and closed work goes to `90`, not `99`. Archive (`99`) is
  for superseded and retired material, not for finished work — finished work still gets
  referenced, so it stays findable in 90.

When building a workroom, create the full template even where subfolders start empty. A
missing subfolder means the next person invents their own location for that document type,
and the structure erodes from there.

## Triage

The full decision procedure is in `references/triage.md`. The short version:

1. What project, property, entity or case does this belong to? If none, it is a company
   function file.
2. What is its document type?
3. Is it current, superseded, or closed?
4. Is it sensitive (personnel, banking, tenant application, legal evidence)?
5. **Route, name, log.** Destination = workroom (or master folder) → subfolder. Name it
   to the standard. Log it.

If any of steps 1–4 cannot be answered from the file itself, the answer is
`00.7 — TO BE DETERMINED` and a question for the user. Do not substitute inference for
evidence.

One authoritative copy, always. When a second department needs the same document, create a
Drive shortcut rather than a copy — two copies means two versions means neither is
controlling. Note that folder names carry no security whatsoever; a folder labelled
"Restricted" that has not had its Drive permissions set is simply a lie, so set actual
permissions whenever the destination is a restricted folder.

## Track

The three trackers are one system, not three: the Filing Queue is intake, the Master
Document Index is the permanent register of controlling documents, and the Control Center
is the roll-up both feed. Column schemas are in `references/trackers.md`.

Write to the Index only for documents that are controlling, signed, filed, sensitive, or
high-value. Indexing everything makes the Index useless — it becomes a second copy of the
file list rather than a shortlist of what governs.

## Audit

Run `references/weekly-audit.md` every Friday. The audit's purpose is not to produce a
clean report; it is to produce a short list of named exceptions with owners and due dates.
An audit that finds nothing in a Drive this active has not looked hard enough — say so
rather than reporting all-clear.

## Batch work

For a large root cleanup, do not propose hundreds of moves in prose. Use
`scripts/propose_filing.py`, which takes a file listing and emits a proposal table
(destination, proposed name, confidence, duplicate flag) for the user to approve in bulk:

```bash
python scripts/propose_filing.py listing.json --out proposals.csv
```

Then execute only the approved rows, in batches, logging each one. Duplicate candidates and
low-confidence rows never execute automatically — they go to the Needs Decision folder.

Work in batches of roughly 20–30 files, reporting after each batch. Long unattended runs on
someone's live Drive are how trust gets destroyed, and a wrong move discovered at file 300
is much more expensive than one caught at file 20.

## Rework of earlier passes

Parts of this Drive were organized before the current requirements were settled, so some
existing folders and files are wrong and need undoing. Treat that work as evidence of
intent, not as a mistake to clean up unilaterally.

Sequence for any rework:

1. List what exists and how it diverges from the provided rules.
2. Present the list with a proposed correction for each item.
3. Wait for approval, item by item or as an approved batch.
4. Execute only what was approved, logging each change with its original location.

Never fold a rework into an unrelated task. If a filing job reveals a structural problem,
finish the filing, then raise the problem separately.

## A note on the two source plans

There are two generations of this plan in the Drive: an earlier generic one ("SRF 11",
00–12 + 99) and the current Phoenix directory (00–15, 90, 99, with owners and access
levels). The Phoenix directory supersedes SRF 11. If a file or instruction references the
old numbering, translate it using the mapping table at the end of
`references/master-directory.md`, and treat the SRF 11 documents themselves as superseded
records belonging in `99 — ARCHIVE`.
