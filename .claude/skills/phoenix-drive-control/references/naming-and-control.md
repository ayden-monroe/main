# Naming and File Control

## The standard

```
YYYY-MM-DD — Project or Case — Document Type — Description — STATUS
```

Example:
`2026-03-14 — IN South Bend 819 Donald — Purchase Agreement — Seller executed — SIGNED`

The date is the document's own date, or the date received if the document carries none.
Not the date it was scanned or uploaded — those are facts about the scanner, not the
document, and they sort the file into the wrong place in time.

Separator is an em dash with spaces (` — `). It survives Drive search, sorts cleanly, and
is visually distinct from hyphens inside the content itself.

## Status ladder

| Status | Use when | Ending |
| --- | --- | --- |
| SOURCE | Original item as received | `— SOURCE` |
| DRAFT | Working document | `— v03 — DRAFT` |
| REVIEW | Awaiting a named reviewer | `— REVIEW` |
| APPROVED | Approved, not necessarily signed or filed | `— APPROVED` |
| SIGNED | Fully executed | `— SIGNED` |
| FILED | Filed with a court or agency | `— FILED` |
| FINAL | Current controlling non-court version | `— FINAL` |
| SUPERSEDED | Replaced; move to folder 99 | `— SUPERSEDED` |

Status is a claim about the document's authority, so it changes only when that authority
actually changes. Promoting a draft to FINAL because it looks finished is the single
easiest way to corrupt the system: FINAL folders are trusted precisely because nothing
enters them casually.

When a document is superseded, rename the old one and move it to `99` in the same action.
A superseded document left in place beside its replacement is worse than a missing one,
because someone will act on it.

## Versioning

Use `v01`, `v02`, `v03`. Never `final`, `final2`, `FINAL-final`, `newest`, `latest`,
`copy`, `(1)`, or a person's initials standing in for a version. Those names encode a
guess about chronology that turns out wrong the moment two people edit on the same day.

Trailing ` (1)`, ` (2)`, `copy of` and duplicated extensions are Drive's duplicate
markers, not versions. Files carrying them go to `00.5 — Possible Duplicates` for a
decision, never silently renamed into the version sequence.

## Standing rules

1. **One home.** One authoritative copy per document. Other departments get shortcuts.
2. **Clean root.** The Drive root holds numbered master folders and essential shortcuts
   only.
3. **Original evidence is never overwritten.** Original and working copy live in separate
   subfolders.
4. **FINAL folders hold only controlling documents.** If it is not controlling, it is not
   in FINAL.
5. **Dates are document dates.** Document date, or received date if none.
6. **Recurring financial records go year → month.**
7. **Permissions are permissions.** A "Restricted" folder name grants no security. Set
   Drive permissions on the folder, and verify them in the weekly audit.
8. **Closed work goes to 90, not 99.** Archive is for superseded material; closed work is
   still live reference.
9. **Email and calendar records are Drive records.** Material attachments and threads get
   filed into the related project or case folder, not left in a mailbox where only one
   person can reach them.

## Renaming safely

When renaming an existing file, preserve any court, agency, or vendor-assigned identifier
somewhere in the new name — case numbers, permit numbers, invoice numbers, parcel IDs.
Those identifiers are how outside parties refer to the document, and a name that drops
them makes the file unfindable from the outside world's reference.

Record the original filename in the Filing Queue row. Until the change has settled, that
row is the only way back.
