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

### 115 Lafayette Building — 5 filed
All five are the City of South Bend `Request for Proposals — Rehabilitation and
Adaptive Reuse of The Lafayette Building`, release date **22 September 2022**,
submission deadline 26 January 2023. One Doc plus four identical PDFs.
→ `115 Lafayette Building - Purchase & Closing Documents`. All copies kept.

### 520 27th Street — 2 filed, 2 OUT OF SCOPE
| File | Date read from text | Destination |
|---|---|---|
| 520 27th street .pdf | Tax deed petition notice 8 Sep 2026 | Property Taxes |
| LTIPrint 520 29th street | Tax sale record, tax year 2019 / pay year 2020, printed Apr 2020 | Property Taxes |
| my properties 520 s 27th ... AFFIRMED DEMO ORDER ... UPDATED 10/2/19 | Hearing dates 2018–2019 | `00.8 — Out of Date Scope` |
| bbbc 520 27th street ... eviction lace cutler case summary | Case filed 31 Jul 2018 | `00.8 — Out of Date Scope` |

### 919 Portage Ave — 7 filed
`919 Portage Ave - A Regenerative Case Study` — four copies in root, three more
already sitting in the property folder. Reading it settled an earlier question:
it is not marketing. It is a deconstruction record by reGen South Bend LLC dated
**5 June 2026**, covering asbestos removal, material salvage and waste hauls.
→ `919 Portage Ave - Maintenance & Repairs`. This clears the "no matching
category" hold recorded in Part 1 section F item 4.

### Found while searching, filed elsewhere
| File | Date read from text | Destination |
|---|---|---|
| PSA_Plymouth Plaza_FINAL.pdf | Purchase and sale agreement, Plymouth Plaza, 2024 | `02 ACTIVE DEALS - Offers` |
| S Kollar Property Data Form (rev 11 11 22) (5) | Borrower property data form 16 Jun 2023, SFR Fund 11 LLC | `02 ACTIVE DEALS - Financing Applications` |

### Not records — left in root
`ILtinleypark_Redacted.pdf` ×2 (Tinley Park IL land listing, matched on "park"),
`CheapOair - CrossSell` (travel site capture), `Phoenix, for the Lincoln Tower
Apartments at 520 S` (Springfield IL analysis, matched on "520 S"), and a
business-coaching email that merely mentions Parkmore in a list.


### Mini Mountain RV Resort — 1 filed, 3 to Needs Review
| File | What reading revealed | Destination |
|---|---|---|
| c1656679-b3aa-40fa-851b-21f2bbdd8164.pdf | **CBRE Offering Memorandum, Mini Mountain RV Resort, New Carlisle IN**, 2026 | Purchase & Closing Documents |
| Vault - Mini Mountain RV Resort (Unzipped Files) | Folder — the archive was already extracted | Needs Review |
| Vault - Mini Mountain RV Resort (1) (Unzipped Files) | Folder — second extraction | Needs Review |
| Vault - Mini Mountain RV Resort.zip | Fourth copy of the archive, found at root | Needs Review |

The offering memorandum had a meaningless UUID filename. Nothing but reading it
would have found it. **Also significant:** two "(Unzipped Files)" folders exist
at root, so the Mini Mountain archives have already been extracted once. The
same may be true for Northgate, Chiafos and Value Add Retail — worth checking
before anyone extracts them again.

### Found while searching, filed elsewhere
| File | Date read from text | Destination |
|---|---|---|
| Sierra_Condos_Investment_Summary.pdf | Texas multifamily offering, 2026 | `02 ACTIVE DEALS - Leads & Opportunities` |
| Sierra_Condos_PPM_Final.pdf | Private placement memorandum, Dec 2025 | `02 ACTIVE DEALS - Leads & Opportunities` |

### Search queries that were too loose
Three of four queries this round matched on a fragment rather than the property:
`Indiana Beach` matched every document containing "Indiana", `Country View`
matched "View", and `Northgate` matched a trust name inside an unrelated
Attorney General complaint. Future rounds need the full distinctive phrase.

### Held for a decision — third-party litigation at root
Court filings in cases Mr Kollar is not a party to, all 2024–2025 and so in
scope by date, but none belongs to a property or to one of his own matters:
`Reply in Support of Motion to Ap.pdf` (KeyBank v Matthews, Jun 2025),
`Exhibit 1 - Declaration of K. Co (3).pdf` (Li v Longview, Feb 2024),
`Lei Zhao_Complaint (Final to Fil.pdf` (State of Indiana v Lei Zhao, Dec 2024).

These read as research — other operators' cases kept for reference. There is no
category for that. `15 — RESEARCH & REFERENCE LIBRARY` exists but is empty and
has no category list, so nothing was invented. Needs a decision.

### Held — templates
Four copies of `Crystal View Capital Fund IV LP - Private Placement
Memorandum`, dated November 2022. One is titled "master template to duplicate
for our fund phoniex", so these are another firm's PPM kept as a model. In
scope by date; no obvious home between `14 SYSTEMS, SOPs & TEMPLATES` and the
empty `09 — INVESTORS, LENDERS & CAPITAL`.

### Not records — left in root
A Continental Properties job board capture, a ChatGPT interface capture, an
American Express status page, and a 2024 news article on the Indiana Attorney
General's office. Also a personal health and age chat, left untouched.


### ⚠ Park More Plaza and Value Add Retail - 2024 Roof are the same building

Four documents read this round all describe **1104 West Bristol Street,
Elkhart, Indiana 46514** under three different names:

| Document | Name it uses | Date |
|---|---|---|
| Carlisle roofing warranty (filed earlier) | PARKMOR PLAZA | Apr 2024 |
| AEI Property Condition Report | Value Add Multi-Tenant Retail | 5 Jun 2026 |
| EBI Phase I Environmental Site Assessment | Shops on Bristol | 9 Dec 2024 |
| rx_Comm_Lease_Deposit.pdf | Parkmor Plaza (1104) | 2 Dec 2024 |

`Park More Plaza` and `Value Add Retail - 2024 Roof` are therefore two folders
for one asset, each with its own 14 categories, and its records are being split
between them.

**No folders were merged.** Each document went to the folder matching the name
in its own text. Merging is the operator's call.

### Value Add Retail - 2024 Roof — 2 filed, 2 folders to Needs Review
| File | Date read from text | Destination |
|---|---|---|
| 529097-LPCA Elkhart, Indiana (1104 West Bristol Street) - Final.pdf | AEI Property Condition Report, 5 Jun 2026 | Inspections |
| Environmental_1130-1220_W_Bristol_St_Elkhart_IN_465142100.pdf | EBI Phase I ESA, 9 Dec 2024 | Inspections |
| `Value Add Multi-Tenant Retail - New 2024 Roof` ×2 | Duplicate property folders sitting at root | Needs Review |

### Park More Plaza — 1 filed
`rx_Comm_Lease_Deposit.pdf` — commercial lease deposit schedule for Parkmor
Plaza (1104), four tenants, as of 2 Dec 2024 → Lease & Tenant Documents.

### Chiafos / Indiana Beach — 2 folders to Needs Review
Two more `Vault - Chiafos Rental Resort (Unzipped Files)` folders found at root.
As with Mini Mountain, those archives were already extracted.

### Kollar v Massa and Mackowiak — 3 filed
| File | Date read from text | Destination |
|---|---|---|
| Massa_Mackowiak_9_Complaint_Worklist.xlsm | Worklist, Sep 2026 | `06 LEGAL / Kollar v Massa and Mackowiak — Matter Records` |
| Massa_Mackowiak_9_Complaint_Worklist (1).xlsm | Same worklist, Sep 2026 | same |
| Find state court dockets mentioning Frank D. Massa.pdf | Docket research, Oct 2025 | same |

### Left untouched — could not place them
Per the operator's instruction, anything without a clear destination stays
where it is and is not listed for a decision: a shortcut to a 2023 Chiafos
proforma (a shortcut, not a file), a Diplomat Plaza analysis for a Michigan
property with no folder, a receivership multifamily archive, two near-empty
sheets titled "massa 2026" and "Massa 2025" whose contents do not match their
titles, and a negotiation email that does not name its property.


---

## Running totals

| | Count |
|---|---|
| Root files read and decided | 85 |
| Filed into the structure | 35 |
| Moved to a `Needs Review` subfolder | 7 |
| Moved to `00.8 — Out of Date Scope` | 5 |
| Left untouched — no clear destination | 22 |
| Not records (web-page captures, false matches) | 16 |
| **Root files remaining** | **~5,830** |

Separately, 3 files already sitting loose in `919 Portage Ave` were filed once
reading established what they were.
