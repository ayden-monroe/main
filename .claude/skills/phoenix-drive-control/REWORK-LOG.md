# Rework log — SRF 11 → Phoenix

**2026-09-24.** Executed with the owner's approval (whole-folder moves).
Nothing deleted, nothing renamed, nothing overwritten.

## The 14 moves

Each SRF 11 master folder was moved intact into its Phoenix counterpart, using
the mapping table at the end of `references/master-directory.md`. Contents rode
along untouched.

| From (SRF 11) | To (Phoenix) |
|---|---|
| 00 — INBOX & TO SORT | 00 — INBOX & FILE CONTROL |
| 01 — COMPANY & ADMINISTRATION | 08 — COMPANIES & ENTITY RECORDS |
| 02 — FINANCE & ACCOUNTING | 07 — FINANCE, BANKING & TAX — RESTRICTED |
| 03 — PROPERTY PORTFOLIO | 03 — OWNED REAL ESTATE PORTFOLIO |
| 04 — ACQUISITIONS & SALES | 02 — ACTIVE DEALS & ACQUISITIONS |
| 05 — CONSTRUCTION & RENOVATION | 04 — CONSTRUCTION & REHAB |
| 06 — RENTAL & PROPERTY MANAGEMENT | 05 — PROPERTY MANAGEMENT & TENANTS |
| 07 — VENDORS & CONTRACTORS | 11 — VENDORS, CONTRACTORS & PROFESSIONALS |
| 08 — EMPLOYEES & TEAM | 10 — TEAM, HR & ACCOUNTABILITY — RESTRICTED |
| 09 — LEGAL & COMPLIANCE | 06 — LEGAL — RESTRICTED |
| 10 — MARKETING & BRANDING | 13 — MARKETING, BRAND & SALES |
| 11 — SYSTEMS & OPERATIONS | 14 — SYSTEMS, SOPs & TEMPLATES |
| 12 — TEMPLATES & FORMS | 14 — SYSTEMS, SOPs & TEMPLATES |
| 99 — ARCHIVE | 99 — ARCHIVE — NOT ACTIVE WORK |

Verified: root now returns none of the 13 SRF 11 master folder names.
Queue rows: `filing-queue-rows-20260924.csv` (Q-20260924-001 … -014).

## Dead scaffolds — inspected, not touched

The owner asked for contents to be reported before anything moves.

### August 9 series (8 folders at root) — 108 files, no subfolders

| Folder | Files |
|---|---|
| 00 — PHOENIX COMMAND CENTER chat downloads | 25 |
| 10 — REAL ESTATE & ACQUISITIONS | 19 |
| 30 — FINANCE, BANKING & CREDIT | 24 |
| 40 — OPERATIONS & TEAM | 2 |
| 50 — BRAND, MARKETING & MEDIA | 0 — empty |
| 60 — HEALTH & PERFORMANCE | 3 |
| 70 — PERSONAL & FAMILY | 0 — empty |
| 90 — INBOX — TO FILE | 35 |

**`60 — HEALTH & PERFORMANCE` holds medical records** (Labcorp patient
documents). Standing rule: medical material is left untouched. Do not fold this
folder into a bulk move.

### March 22 series (5 folders at root) — nearly empty

| Folder | Contents |
|---|---|
| 03_FINANCIAL_CONTROL | empty |
| 04_LEGAL | 2 files + 1 subfolder (`20 — LEGAL & ASSET RECOVERY`) |
| 05_REPORTS_DATA | empty |
| 06_BUSINESS_OPERATIONS | empty |
| 07_ARCHIVE | empty |

### Phoenix_Google_Drive_Directory — scaffold only

Its 16 numbered folders contain only further empty numbered subfolders created
by the original PowerShell script, plus the 8 personal folders still sitting in
`11_PERSONAL_PHOENIX` (health dashboards, bio, photos, screenshots, iCloud
archives, personal system, mission statement, personal reports).

No business files remain anywhere in this scaffold — they were migrated out on
17 September.

## Two findings that need the owner

1. **The master directory names roles, not people, for eight folders**
   (02, 03, 05, 06, 08, 11, 13, 99 → "Assigned deal owner", "PM owner",
   "Administration owner", "Legal coordinator / paralegal", "Marketing owner",
   "Operations owner"). `trackers.md` requires "Named person, never a role
   alone." Every queue row for those folders carries an owner exception until
   real names are supplied.

2. **No RESTRICTED folder has had its Drive permissions set.**
   `naming-and-control.md` rule 7: "A 'Restricted' folder name grants no
   security." Folders 06, 07 and 10 are named RESTRICTED but are currently
   as open as everything else. This is a weekly-audit item and it is open now.

## Rule check

| Rule | Status |
|---|---|
| 1. Read current state first | Done before every action |
| 2. Never delete | Nothing deleted or trashed |
| 3. Never touch original legal evidence | Legal folder moved as a sealed container; nothing inside opened, renamed or edited |
| 4. Log every move | 14 rows written, validated against the 11-column schema |
| 5. Ambiguity stops work | Dead scaffolds inspected and reported, not moved |
| 6. Date window | No individual document was filed, so no date scoping applied yet |
| 7. Stay inside provided rules | Every destination came from the mapping table; no folder invented |
| 8. Ask before undoing prior work | Rework was proposed and approved before execution |
