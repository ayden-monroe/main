# Triage

How to decide where a file belongs. Used for incoming items and for cleaning loose files
out of the Drive root.

## Procedure

**0. Check the date window.**
Documents dated 2020-01-01 through today are in scope. Older or undated files are left
alone and listed for the user — do not rename, move or file them. The document's own date
governs; a scan date or Drive modified date does not bring an old document into scope.

**1. Identify the subject.**
Which deal, property, entity, vendor or case does this concern? Look at the filename, then
the content, then the surrounding files uploaded at the same time. If it concerns no
specific subject, it is a company-function file and routes to a master folder directly.

**2. Identify the document type.**
Purchase agreement, invoice, court order, W-9, photo, scan, spreadsheet, correspondence.
Type determines the subfolder within the workroom.

**3. Identify its state.**
Current, superseded, or closed. Superseded → `99` of its workroom. Closed matter → `90`.

**4. Identify sensitivity.**
Personnel, banking, tenant application, legal evidence, investor material. Sensitive
destinations need their Drive permissions checked before the file lands there.

**5. Route, name, log.**
Destination = workroom → subfolder. Rename to the standard. Write the Filing Queue row.

## When you cannot complete step 1 or 2

Route to `00 — INBOX & FILE CONTROL`:

| Situation | Destination |
| --- | --- |
| Cannot tell what it is | `00.4 — Needs Identification` |
| Know what it is, cannot tell which subject it belongs to | `00.4 — Needs Identification` |
| Appears to duplicate something already filed | `00.5 — Possible Duplicates` |
| Classification is clear but the call is a judgment one person must make | `00.6 — Needs Decision` |
| Legal document whose matter is unclear | `00.6 — Needs Decision`, flagged |
| Classifiable, but the rules do not clearly establish a destination | `00.7 — TO BE DETERMINED` |
| Dated before 2020, or no determinable date | Leave in place; list for the user (`00.8` only with permission) |

Every one of these gets a queue row stating the specific question blocking the filing. A
row that says "unclear" wastes the reviewer's time; a row that says "invoice from Summers
Construction, no property named, matches draw schedule for two active rehabs" gets
answered in seconds.

## Filename signals

Common patterns and what they usually mean:

| Pattern | Reading |
| --- | --- |
| `Scan2026-09-20_152253 po1 dayton.pdf` | Scanner output. Date is scan date, not document date — open it to find the real date. Shorthand ("po1 dayton") is a property or case reference. |
| `..._Packet (1)` | Drive duplicate marker → `00.5`. Compare against the original before anything else. |
| `Untitled document` | Unnamed working doc → `00.4`; check content and recency before assuming it is disposable. |
| `..._Plan (1) (2).md` | An export of an export. Almost certainly superseded; find the authoritative version first. |
| `... delite`, `... delete`, `... old` | Someone's informal disposal marker. Never act on it — it is not a decision, it is a note to self. Route to `00.6`. |
| `.md` exports of AI output | Working material. Belongs with drafts, not FINAL, until a person has verified the content. |
| Long descriptive titles that read like commentary | Usually AI-generated summaries rather than source documents. File as analysis, never as evidence or source. |

## Duplicate handling

Two files are duplicates only if their content is the same. Same name and size is a strong
hint, not proof; a scan and a re-scan of the same page are different files with the same
content, and two invoices from the same vendor in the same month may be different bills.

When duplicates are confirmed: keep the copy with the best provenance — the original
received file, the signed version, the filed-stamped version — and keep it in its
authoritative location. The other becomes a shortcut, or goes to `99` if it has historical
value, or is queued for the user's deletion decision. This skill does not delete.

## The root-cleanup pass

The realistic first job for this system is a root full of loose files. Sequence:

1. Build `00` and the master folders first. There must be somewhere to put things.
2. Inventory the root: name, type, size, apparent document date, modified date, owner.
3. Split the inventory by date window first. Everything outside 2020-to-present, or
   undated, comes out of the working set and goes on a list for the user.
4. Group by apparent subject before filing anything. Groups reveal which workrooms are
   actually needed, and filing one at a time creates workrooms that turn out to be wrong.
5. Build the workrooms the groups call for.
6. File in batches of 20–30, highest-confidence groups first, reporting after each batch.
7. Everything unresolved lands in `00`, never left at root.

Build only the folders the provided rules define. If a group of files has no home in the
master directory or the templates, that is a question for the user, not a licence to
create a new category — the structure's value comes from being the same everywhere, and
a folder invented mid-cleanup is one nobody else knows to look in.

Confidence matters more than throughput here. A file placed wrongly but confidently is
harder to recover than a file sitting honestly in `Needs Identification`.
