# Workroom Folder Templates

Create the complete template every time, including subfolders that start empty. An absent
subfolder is an invitation for someone to invent a location, which is how the structure
comes apart.

Every template has the same spine: `00` is the dashboard, `13` is FINAL (current
controlling documents only), `99` is superseded. Anyone who learns one template can
navigate all three.

---

## Active Deal — goes in `02`

Folder name: `STATE — CITY — PROJECT OR ADDRESS — DEAL STAGE`
Example: `IN — South Bend — 819 Donald Street — UNDER CONTRACT`

| No. | Subfolder | Holds |
| --- | --- | --- |
| 00 | Deal Dashboard & Next Decisions | Owner, status, money at risk, deadline, next decision, controlling docs |
| 01 | Source Documents & Seller Information | Original received materials, unedited |
| 02 | Contacts, Parties & Authority | People, roles, who can bind whom |
| 03 | Offers, LOIs & Purchase Agreements | Drafts, signed versions, amendments |
| 04 | Due Diligence | Physical, legal, financial, environmental |
| 05 | Market Study & Business Plan | Demand, competition, operating plan |
| 06 | Underwriting, Pro Forma & Valuation | Models, assumptions, value cases |
| 07 | Rehab, CapEx & Construction | Scopes, estimates, schedules |
| 08 | Financing, Investors & Capital Stack | Debt, equity, incentives |
| 09 | Municipality, Incentives & Public Support | TIF, grants, approvals, correspondence |
| 10 | Legal, Title & Closing | Title, survey, legal, closing |
| 11 | Meetings, Calendar & Correspondence | Agendas, notes, decisions, commitments |
| 12 | Photos, Video & Site Inspections | Dated evidence |
| 13 | FINAL — Approved Decision Documents | Current controlling documents only |
| 99 | Superseded Drafts & Archive | Replaced versions |

Deal stage values: `LEAD` · `UNDERWRITING` · `OFFER OUT` · `UNDER CONTRACT` · `DILIGENCE`
· `CLOSING` · `DEAD`. Update the folder name when the stage changes; a stale stage in the
name is a false signal to everyone scanning the folder list.

On close: move to `03` as an owned property (rebuild under the property template, carrying
`13 FINAL` across), or to `90` if it died or sold on.

---

## Owned Property — goes in `03`

Folder name: `STATE — CITY — STREET ADDRESS — ASSET NAME`

| No. | Subfolder | Holds |
| --- | --- | --- |
| 00 | Property Dashboard & Critical Dates | Owner, asset status, risks, dates |
| 01 | Overview, Parcel & Contacts | Summary, tax and parcel records |
| 02 | Acquisition, Deed, Title & Closing | Ownership documents |
| 03 | Financing, Insurance & Appraisals | Debt and risk records |
| 04 | Plans, Surveys, Permits & Approvals | Technical and government approvals |
| 05 | Construction, Rehab & Capital Projects | Scopes, bids, contracts, change orders |
| 06 | Accounting, Budget, Invoices & Draws | Property financial records, year → month |
| 07 | Photos, Video & Inspection Evidence | Dated property evidence |
| 08 | Leasing, Tenants & Occupancy — Restricted | Applications, leases, notices |
| 09 | Maintenance, Work Orders & Warranties | Operations records |
| 10 | Municipality, Utilities & Taxes | Government and utility records |
| 11 | Correspondence & Meeting Notes | Material communications |
| 12 | Sale, Refinance or Disposition | Exit materials |
| 13 | FINAL — Current Controlling Documents | Current documents only |
| 99 | Superseded & Historical Records | Replaced and historical material |

`08` requires real Drive permissions — tenant applications carry identity and financial
data belonging to third parties.

---

## Legal Matter — goes in `06`

Folder name: `COURT OR AGENCY — CASE NUMBER — SHORT CASE NAME`

| No. | Subfolder | Holds |
| --- | --- | --- |
| 00 | Case Dashboard, Deadlines & Next Actions | Court, judge, parties, counsel, deadlines, strategy |
| 01 | Pleadings Filed by Our Side | Filed-stamped copies |
| 02 | Opposing Pleadings & Claims | Opposing filings |
| 03 | Court Orders, Notices & Docket | Court-issued material |
| 04 | Evidence — Original, Unaltered | **Never overwrite, edit, or rename in place** |
| 05 | Evidence — Working Copies & Analysis | Annotations and analysis |
| 06 | Discovery Sent | Requests, service records, responses sent |
| 07 | Discovery Received | Responses and productions received |
| 08 | Correspondence & Email Threads | Material communications |
| 09 | Research & Verified Authorities | Statutes and case law that have been checked |
| 10 | Drafts for Attorney Review | Working legal drafts |
| 11 | Attorney-Approved or Filed FINAL | Approved and filed material |
| 12 | Damages, Costs & Settlement Analysis | Economic analysis |
| 13 | Hearing, Mediation & Trial Preparation | Preparation materials |
| 99 | Superseded Drafts & Closed Archive | Replaced or closed matter records |

Three rules specific to legal matters, each of which has cost people cases:

- **04 is write-once.** Original evidence is copied into `05` before anyone marks it up.
  Chain of custody is a property of the file's history, and a rename destroys it.
- **`09` means verified.** Anything in Research that has not been confirmed against the
  actual statute or reporter does not belong there. AI-generated or unchecked authority
  goes in `10` with the drafts, clearly marked as unverified, because polished output that
  has not been verified is the most dangerous kind of document in the folder.
- **`11` is attorney-approved only.** Not "looks final". Approved.

On resolution: move to `90 — CLOSED, SOLD & COMPLETED / <year>`, retaining `04` intact.

---

## Vendor (in `11`) and Entity (in `08`)

Lighter templates, one folder per vendor or entity, named for it:

**Vendor:** `01 Qualification & W-9` · `02 Insurance Certificates` · `03 Agreements &
Rates` · `04 Work History & Performance` · `05 Invoices & Payments` · `99 Superseded`

**Entity:** `01 Formation & Ownership` · `02 Operating Agreements & Resolutions` ·
`03 Licenses & Registrations` · `04 Insurance` · `05 Annual Filings & Compliance` ·
`13 FINAL — Current Governing Documents` · `99 Superseded`
