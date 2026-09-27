# Root sweep — running log

Method: search root by destination (`parentId = 'root' and fullText contains
'<property>'`) with content snippets on. Each result's document date is read
from the text, never from the title or the upload date. In scope 2020–2026;
anything earlier goes to `00.8 — Out of Date Scope`.

Measured constraint: the connector returns **5 files per call** with snippets
enabled, regardless of pageSize. Tested at 50 and 200.

---

## 2026-09-27

### 1129 Huey — 2 filed
| File | Date read from text | Destination |
|---|---|---|
| 1129 Huey st signed lease.pdf | Lease term begins 4 Apr 2022 | Lease & Tenant Documents |
| 1129 huey trust (6).pdf | Trust agreement 5 Sep 2022 | Deeds & Ownership |

Also seen: 3 × `don lewis 1129 huey` — not property records. They are saved
OneDrive "On this day" web pages captured as Docs. Left in root.

### 512 West Edison — 3 filed, 2 held
| File | Date read from text | Destination |
|---|---|---|
| Assignment and Notice-Martin Heinemann (512 W. Edison Ave).docx | Assignment 5 Jun 2026, 1031 exchange | Purchase & Closing Documents |
| 512_W_Edison_Four_Store_Concept.png | 2026 concept | Photos |
| massa:kodax 512 west Edison ... settlement funding | Email thread 5 Jun 2026 | Legal |

Held — no matching category. Both are 2026 marketing collateral, and the 14
categories have no marketing bucket:
`512_W_Edison_Pawn_Operator_Opportunity.pptx`,
`512_W_Edison_Mishawaka_Sale_Lease_Flyer.pdf`

### 1919 Marquette — 4 filed, 1 held
| File | Date read from text | Destination |
|---|---|---|
| 1919 Marquette larrys rehab list 2025 dec | Dec 2025 | Maintenance & Repairs |
| 1919 marquette construction-proposal-template-24 | Proposal 31 May 2023 | Maintenance & Repairs |
| quit claim deed griner form template 1919 marquette | Quitclaim, notary block 2024 | Deeds & Ownership |
| adam grayson 1919 marquette | Messenger thread 2025 | Property Management & Correspondence |

Held: `1919 marquette blank deed to american consulting in llc.pdf` — snippet
empty, date not readable, and it is a blank form rather than an executed record.

### 24255 Huron — 1 filed, 3 OUT OF SCOPE, 1 held
| File | Date read from text | Destination |
|---|---|---|
| 24255 huron (7).pdf | Trust agreement 8 Sep 2022 | Deeds & Ownership |
| new creation 24255 huron ... lease from phoniex with church ×3 | **Lease dated 26 May 2012** | `00.8 — Out of Date Scope` |

Those three would have been filed as current leases on the title alone. Reading
them caught it. Held: `St.Joseph Indiana, Assessor 24255 huron st` — empty file.

### 1937 Johnson — 4 filed, 1 held
| File | Date read from text | Destination |
|---|---|---|
| 1937 johnson | Inspection corrections, Mar 2026 | Inspections |
| Inspection Repairs 1937 Johnson 03_2026 | Mar 2026 | Inspections |
| Quit Claim 1937 johnson april 2025 | Quitclaim deed 2025 | Deeds & Ownership |
| 1937 johnson water application.pdf | Utility authorisation, lease dated 25 Oct 2024 | Utilities |

Held: `_document1937 johnson` — 23 MB, snippet empty, date not readable.

Note: the water application form carries a social security number field. Filed
as a utility record; contents not reproduced anywhere.

---

## Running totals

| | Count |
|---|---|
| Root files read and decided | 25 |
| Filed into the structure | 14 |
| Moved to `00.8 — Out of Date Scope` | 3 |
| Held — no category, unreadable, or empty | 5 |
| Not records (web-page captures) | 3 |
| **Root files remaining** | **~5,890** |
