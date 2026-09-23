# Trackers

Three sheets, one system. The Filing Queue is intake, the Master Document Index is the
permanent register of what governs, the Control Center is the roll-up both feed. They live
in `00.9 — Filing Queue & Master Index`.

## Drive Filing Queue

Everything entering Drive gets a destination, an owner and a next action.

| Column | Contents |
| --- | --- |
| Intake ID | `Q-YYYYMMDD-NNN` |
| Date Received | Date the item arrived in Drive |
| Current File Name | Name as received — record before renaming |
| Project / Case | Subject, or blank if unidentified |
| Document Type | |
| Destination Folder | Full path, or the `00` subfolder if unresolved |
| Status | `QUEUED` · `FILED` · `NEEDS DECISION` · `TO BE DETERMINED` · `DUPLICATE REVIEW` · `OUT OF SCOPE` · `ESCALATED` |
| Owner | Named person, never a role alone |
| Due Date | |
| Next Action | The specific next step |
| Exception | The blocking question, stated concretely |

A row closes when the file is in its authoritative home under its standard name. Items
still open after seven days escalate — that threshold is the whole point of the queue, and
a queue with month-old rows has quietly become a second inbox.

## Master Document Index

Not every file. Only documents that are controlling, signed, filed, sensitive, or
high-value. An index of everything is a file list, and nobody consults a file list to find
out what governs.

| Column | Contents |
| --- | --- |
| Document ID | `DOC-NNNN` |
| Date | Document date |
| Project / Case | |
| Document Type | |
| Description | |
| Status | From the status ladder |
| Version | `v01`, `v02`, … |
| Owner | |
| Drive Folder / Link | Link to the authoritative copy |
| Source / Sender | Where it came from |
| Access | Who can see it |
| Retention | How long it is kept, and why |
| Notes | |

When a document is superseded, update its row to `SUPERSEDED` rather than deleting it, and
add a row for the replacement. The chain of what replaced what is often the thing someone
needs years later.

## Control Center

Roll-up, refreshed at least weekly:

| Control | Source |
| --- | --- |
| Open filing items | Filing Queue rows not `FILED` |
| Needs decision | Filing Queue rows `NEEDS DECISION` |
| To be determined | Filing Queue rows `TO BE DETERMINED` — awaiting an answer |
| Out of date scope | Files dated pre-2020 or undated, awaiting instruction |
| Possible duplicates | Filing Queue rows `DUPLICATE REVIEW` |
| Overdue items | Queue rows past due date |
| Open weekly audit exceptions | Audit rows `OPEN` |

Alongside the counts, keep the six operating rules visible:

1. The Drive root contains only numbered master folders and essential shortcuts.
2. Every file has one authoritative home; shortcuts instead of duplicate copies.
3. Original legal evidence is never overwritten.
4. FINAL folders contain only controlling documents.
5. Inbox items older than seven days require escalation.
6. If a controlling document cannot be found in 60 seconds, fix the filing system.

## Writing rows

Append; do not rewrite history. When correcting a row, edit the specific cells and note
the correction rather than replacing the row, so the audit trail survives.

Counts on the Control Center are derived, never typed from memory — recount from the
source sheets each refresh. A hand-typed count that drifts from reality makes the whole
dashboard untrustworthy, and a dashboard nobody trusts gets ignored within a month.
