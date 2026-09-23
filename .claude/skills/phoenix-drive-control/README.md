# phoenix-drive-control

A Claude Code skill that executes and maintains the Phoenix Drive file-control system.

## Install

Drop the folder into either location:

```bash
# this project only
cp -r phoenix-drive-control .claude/skills/

# all projects on this machine
cp -r phoenix-drive-control ~/.claude/skills/
```

Then `/skills` in Claude Code to confirm it loaded.

## Contents

```
phoenix-drive-control/
├── SKILL.md                        workflow, guardrails, job routing
├── references/
│   ├── master-directory.md         the 00–15 / 90 / 99 root structure + SRF 11 mapping
│   ├── folder-templates.md         deal, owned property, legal matter, vendor, entity
│   ├── naming-and-control.md       naming standard, SOURCE→FINAL ladder, versioning
│   ├── triage.md                   where a file goes, and what to do when unclear
│   ├── trackers.md                 Filing Queue / Master Index / Control Center schemas
│   └── weekly-audit.md             Friday review
└── scripts/
    └── propose_filing.py           batch filing proposals from a Drive listing
```

## Drive access

The skill assumes Claude Code can reach the Drive — a Google Drive MCP connector, `rclone`,
or the Drive API. It is written to be tool-agnostic: it decides *what* should happen, and
whatever Drive tool is configured carries it out. With no Drive access it still works as a
planner, emitting the folder list and filing proposals for someone to apply by hand.

## Batch proposals

```bash
python scripts/propose_filing.py listing.json --out proposals.csv
```

`listing.json` is a JSON array of Drive records (`name` required; `id`, `mimeType`,
`modifiedTime` used when present). Output is a review table — nothing is moved. Files
dated outside 2020-to-present, or with no determinable date, are marked "leave in place"
and never proposed for filing. Anything the rules don't clearly place goes to
`00.7 — TO BE DETERMINED` with the question attached. Confidence below 0.50 is
deliberately routed to a human; the script is conservative by design, since a wrong
confident move in a litigation folder costs far more than a queued file.

## Suggested first run

```
Read the Drive root and tell me what's actually there versus what the plan says
should be there. Don't move anything yet.
```

Then build `00` and the master folders, then do the root cleanup in batches.
