# Phoenix Drive Control — current state of the Drive

Read-only survey, 21 September 2026. **Nothing was created, moved, renamed or
deleted.** This is step 1 of the skill's "Before doing anything" and step 1 of
its "Rework of earlier passes" sequence.

Blocked at step 2 (divergence + proposed corrections): the skill's `references/`
files were not supplied, so there is no authoritative folder list to measure
divergence against.

## Headline numbers

| Measure | Count |
|---|---|
| Folders at Drive root | ~201 |
| Loose FILES at Drive root | **6,000+** (pagination not exhausted; 5,943 captured) |
| Captured loose files sharing a name with another file | **2,939 (49%)** across 874 repeated names |

The skill calls loose files at root "the defining symptom this system exists to
cure" and mandates batches of 20–30 with a report after each. At that rate the
root cleanup alone is **200–300 batches**.

## Four competing numbered systems at root

All four exist simultaneously. None is complete.

**1. SRF 11 — built 2026-09-17 (14 folders + 86 subfolders).** Per the skill
this generation is superseded and its own planning documents belong in
`99 — ARCHIVE`.
`00 — INBOX & TO SORT` · `01 — COMPANY & ADMINISTRATION` ·
`02 — FINANCE & ACCOUNTING` · `03 — PROPERTY PORTFOLIO` ·
`04 — ACQUISITIONS & SALES` · `05 — CONSTRUCTION & RENOVATION` ·
`06 — RENTAL & PROPERTY MANAGEMENT` · `07 — VENDORS & CONTRACTORS` ·
`08 — EMPLOYEES & TEAM` · `09 — LEGAL & COMPLIANCE` ·
`10 — MARKETING & BRANDING` · `11 — SYSTEMS & OPERATIONS` ·
`12 — TEMPLATES & FORMS` · `99 — ARCHIVE`

**2. `Phoenix_Google_Drive_Directory` `1dWKcVWk_SZBJWZsuqCkd663XDQK_UnRA`** —
16 folders, nested one level below root rather than at root:
`00_COMMAND_CENTER` `01_911_ACQUISITIONS` `02_REAL_ESTATE_PORTFOLIO`
`03_ACTIVE_DEALS` `04_LEGAL_AND_COLLECTIONS` `05_FINANCE_AND_CAPITAL`
`06_OPERATIONS_AND_TEAM` `07_COMPANIES_AND_BRANDS`
`08_INVESTORS_LENDERS_PARTNERS` `09_MARKETING_AND_BRAND` `10_AI_WORKBENCH`
`11_PERSONAL_PHOENIX` `12_FAMILY_LEGACY` `90_REFERENCE_LIBRARY`
`98_INBOX_TO_FILE` `99_ARCHIVE`

**This does not match the skill's description of Phoenix** ("00–15, 90, 99").
It has no 13, 14 or 15; it has a 98 the skill never mentions; and it is not at
root. Cannot be assumed to be the target without confirmation.

**3. An August 9 series at root** — `00 — PHOENIX COMMAND CENTER chat downloads` ·
`10 — REAL ESTATE & ACQUISITIONS` · `30 — FINANCE, BANKING & CREDIT` ·
`40 — OPERATIONS & TEAM` · `50 — BRAND, MARKETING & MEDIA` ·
`60 — HEALTH & PERFORMANCE` · `70 — PERSONAL & FAMILY` · `90 — INBOX — TO FILE`

**4. A March 22 series at root** — `03_FINANCIAL_CONTROL` · `04_LEGAL` ·
`05_REPORTS_DATA` · `06_BUSINESS_OPERATIONS` · `07_ARCHIVE`

## Duplicate concentration

Roughly half of all loose root files share a filename with at least one other
file. Largest clusters in the captured sample:

| Name | Copies |
|---|---|
| `Statement` | 36 |
| `Untitled document` | 33 |
| `Order Issued` | 26 |
| `Order Granting` | 25 |
| `Pre_Deal_Gatekeeper_OnePage` | 17 |
| `Phoenix_Strategic_Financial_System` | 17 |
| `Transactions-9020-2026-09-17` | 16 |
| `Rent Roll Commercial` | 15 |
| `Phoenix_Two_Brand_Pawn_Marketing_Plan` | 15 |
| a restricted personal-legal document | 15 |
| `Betrayal_to_Leverage_Workbook` | 15 |
| `Untitled spreadsheet` | 13 |
| `Proposed Order (No Motion)` | 13 |

Same name does not prove same content. Under the skill these are duplicate
candidates for the Needs Decision folder, never automatic merges or deletions.

## Date-scope warning

Upload year of the captured files (`createdTime`):

| Year | Files |
|---|---|
| 2016–2019 | 6 |
| 2020 | 58 |
| 2021 | 31 |
| 2022 | 45 |
| 2023 | 92 |
| 2024 | 351 |
| 2025 | 558 |
| 2026 | 4,802 |

**This table cannot be used for scoping.** The skill is explicit: scope on the
document's own date, and "do not use scan dates, upload dates or Drive modified
dates to bring a file into scope." The 4,802 files uploaded in 2026 include
scans of much older documents. Determining true document dates requires opening
files, which is a separate decision given the restricted material.

## Full listing

`root-files-inventory.tsv` — id, upload time, MIME type, title for the 5,943
captured loose root files. Pagination was not exhausted; more remain.
