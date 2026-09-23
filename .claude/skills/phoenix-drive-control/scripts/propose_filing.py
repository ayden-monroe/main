#!/usr/bin/env python3
"""Propose filing destinations and standard names for a batch of Drive files.

Input: a JSON array (or JSON object with a "files" key) of Drive file records.
Only "name" is required; "id", "mimeType", "modifiedTime", "size" are used when present.

    [{"id": "1abc", "name": "Scan2026-09-20 po1 dayton.pdf",
      "mimeType": "application/pdf", "modifiedTime": "2026-09-20T19:32:54Z"}]

Output: a CSV of proposals (destination, proposed name, confidence, flags) for a human to
approve before anything is moved. This script never touches Drive. It is a triage aid,
not a decision — low-confidence rows are meant to be routed to 00.6 Needs Decision.

    python propose_filing.py listing.json --out proposals.csv
"""

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from datetime import date

INBOX = "00 — INBOX & FILE CONTROL"
TBD = f"{INBOX} / 00.7 — TO BE DETERMINED"
OUT_OF_SCOPE = "LEAVE IN PLACE — out of date scope"
SCOPE_START = "2020-01-01"

# (regex, destination, document type, confidence) — first match wins within each pass.
TYPE_RULES = [
    (r"\b(complaint|answer|counterclaim|motion|pleading|summons|affidavit)\b",
     "06 — LEGAL — RESTRICTED", "Pleading", 0.55),
    (r"\b(order|docket|notice of hearing|judgment)\b",
     "06 — LEGAL — RESTRICTED", "Court order or notice", 0.5),
    (r"\b(discovery|interrogator|request for production|subpoena|deposition)\b",
     "06 — LEGAL — RESTRICTED", "Discovery", 0.55),
    (r"\b(deed|title|closing|settlement statement|hud|alta)\b",
     "03 — OWNED REAL ESTATE PORTFOLIO", "Acquisition or closing", 0.5),
    (r"\b(purchase agreement|psa|loi|letter of intent|offer)\b",
     "02 — ACTIVE DEALS & ACQUISITIONS", "Offer or agreement", 0.5),
    (r"\b(lease|tenant|rent roll|eviction|move[- ]?in|move[- ]?out)\b",
     "05 — PROPERTY MANAGEMENT & TENANTS", "Leasing", 0.5),
    (r"\b(invoice|receipt|statement|payable|receivable|draw request|payoff)\b",
     "07 — FINANCE, BANKING & TAX — RESTRICTED", "Financial record", 0.45),
    (r"\b(tax|1099|w-?2|k-?1|return)\b",
     "07 — FINANCE, BANKING & TAX — RESTRICTED", "Tax record", 0.5),
    (r"\bw-?9\b|\bcertificate of insurance\b|\bcoi\b",
     "11 — VENDORS, CONTRACTORS & PROFESSIONALS", "Vendor qualification", 0.55),
    (r"\b(estimate|bid|scope of work|change order|punch list|permit|inspection)\b",
     "04 — CONSTRUCTION & REHAB", "Construction record", 0.45),
    (r"\b(operating agreement|articles|formation|resolution|registration|llc)\b",
     "08 — COMPANIES & ENTITY RECORDS", "Entity record", 0.5),
    (r"\b(investor|lender|loan|promissory|term sheet|capital)\b",
     "09 — INVESTORS, LENDERS & CAPITAL", "Capital record", 0.45),
    (r"\b(payroll|personnel|onboarding|job description|performance review)\b",
     "10 — TEAM, HR & ACCOUNTABILITY — RESTRICTED", "HR record", 0.55),
    (r"\b(logo|brand|website|listing|flyer|signage|campaign|content brief)\b",
     "13 — MARKETING, BRAND & SALES", "Marketing material", 0.45),
    (r"\b(sop|procedure|template|checklist|organization plan|file control)\b",
     "14 — SYSTEMS, SOPs & TEMPLATES", "Procedure or template", 0.45),
    (r"\b(research|market study|seminar|report|reference)\b",
     "15 — RESEARCH & REFERENCE LIBRARY", "Research", 0.35),
]

# Patterns that override any type match and force a human decision.
HOLD_RULES = [
    (r"\bdel[ei]te\b|\bdelete me\b|\bold\b(?!\w)", f"{INBOX} / 00.6 — Needs Decision",
     "informal disposal marker — never act on it"),
    (r"\buntitled\b", f"{INBOX} / 00.4 — Needs Identification",
     "unnamed document"),
    (r"\bcopy of\b|\(\d+\)\s*(\.\w+)?$|\bfinal[ _-]?final\b|\bnewest\b|\blatest\b",
     f"{INBOX} / 00.5 — Possible Duplicates", "duplicate or ambiguous-version marker"),
]

SCAN_RE = re.compile(r"^scan\s*\d{4}-?\d{2}-?\d{2}[_ ]?\d*", re.I)
DATE_RE = re.compile(r"(20\d{2})[-_]?(\d{2})[-_]?(\d{2})")
DUP_STRIP = re.compile(r"\s*\((\d+)\)|\bcopy of\b|\.(md|pdf|docx|xlsx|csv|png|jpg|jpeg)$",
                       re.I)


def norm_key(name):
    """Normalized key for grouping likely duplicates."""
    k = name.lower()
    for _ in range(4):
        k = DUP_STRIP.sub("", k).strip()
    return re.sub(r"[^a-z0-9]+", "", k)


def extract_date(rec):
    m = DATE_RE.search(rec.get("name", ""))
    if m:
        y, mo, d = m.groups()
        scanned = bool(SCAN_RE.match(rec["name"].strip()))
        return f"{y}-{mo}-{d}", scanned
    mt = rec.get("modifiedTime", "")
    if len(mt) >= 10:
        return mt[:10], True
    return "YYYY-MM-DD", True


def classify(rec):
    name = rec.get("name", "")
    # Underscores and dots are word characters, so \b never fires inside
    # Phoenix_901_Dayton_Counterclaim. Flatten separators before matching.
    low = re.sub(r"[_.\-]+", " ", name.lower())

    for pattern, dest, reason in HOLD_RULES:
        if re.search(pattern, low):
            return dest, "Needs review", 0.2, reason

    for pattern, dest, doctype, conf in TYPE_RULES:
        if re.search(pattern, low):
            return dest, doctype, conf, ""

    return TBD, "Unknown", 0.1, "no type signal in filename — needs a human answer"


def propose_name(rec, doctype):
    date, uncertain = extract_date(rec)
    stem = re.sub(r"\.\w{1,5}$", "", rec.get("name", "")).strip()
    stem = re.sub(r"\s*\(\d+\)", "", stem).strip()
    if SCAN_RE.match(stem):
        stem = SCAN_RE.sub("", stem).strip(" -_") or "Scanned document"
    desc = re.sub(r"[_]+", " ", stem)
    desc = re.sub(r"\s{2,}", " ", desc)[:60].strip()
    subject = "SUBJECT"
    return f"{date} — {subject} — {doctype} — {desc} — SOURCE", uncertain


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("listing", help="JSON file listing (array, or object with 'files')")
    ap.add_argument("--out", default="proposals.csv", help="output CSV path")
    ap.add_argument("--min-confidence", type=float, default=0.0,
                    help="omit proposals below this confidence")
    ap.add_argument("--through", default=date.today().isoformat(),
                    help=f"end of the date window (default today); start is {SCOPE_START}")
    args = ap.parse_args()

    with open(args.listing) as fh:
        data = json.load(fh)
    files = data.get("files", data) if isinstance(data, dict) else data
    if not isinstance(files, list):
        sys.exit("Expected a JSON array of file records, or an object with a 'files' key.")

    groups = defaultdict(list)
    for rec in files:
        groups[norm_key(rec.get("name", ""))].append(rec)

    rows = []
    for rec in files:
        name = rec.get("name", "")
        doc_date, date_uncertain = extract_date(rec)

        # Date gate comes first: out-of-window files are never proposed for filing.
        in_window = doc_date != "YYYY-MM-DD" and SCOPE_START <= doc_date <= args.through
        if not in_window:
            why = ("no determinable date" if doc_date == "YYYY-MM-DD"
                   else f"document date {doc_date} outside {SCOPE_START}..{args.through}")
            rows.append({
                "id": rec.get("id", ""),
                "current_name": name,
                "proposed_destination": OUT_OF_SCOPE,
                "document_type": "Out of scope",
                "proposed_name": "(unchanged — do not rename)",
                "confidence": "0.00",
                "auto_file": "no",
                "flags": f"{why}; leave in place and ask before moving",
            })
            continue

        dest, doctype, conf, reason = classify(rec)
        proposed, _ = propose_name(rec, doctype)

        flags = []
        if len(groups[norm_key(name)]) > 1:
            flags.append("possible duplicate")
            dest = f"{INBOX} / 00.5 — Possible Duplicates"
            conf = min(conf, 0.2)
        if date_uncertain:
            flags.append("date unverified — open the file")
        if "RESTRICTED" in dest or "Sensitive" in dest:
            flags.append("set Drive permissions before filing")
        if reason:
            flags.append(reason)

        if conf < args.min_confidence:
            continue

        rows.append({
            "id": rec.get("id", ""),
            "current_name": name,
            "proposed_destination": dest,
            "document_type": doctype,
            "proposed_name": proposed,
            "confidence": f"{conf:.2f}",
            "auto_file": "no" if conf < 0.5 else "review",
            "flags": "; ".join(flags),
        })

    with open(args.out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) if rows else
                           ["id", "current_name", "proposed_destination", "document_type",
                            "proposed_name", "confidence", "auto_file", "flags"])
        w.writeheader()
        w.writerows(rows)

    low = sum(1 for r in rows if float(r["confidence"]) < 0.5)
    dups = sum(1 for r in rows if "possible duplicate" in r["flags"])
    oos = sum(1 for r in rows if r["proposed_destination"] == OUT_OF_SCOPE)
    tbd = sum(1 for r in rows if r["proposed_destination"] == TBD)
    print(f"{len(rows)} rows written to {args.out}")
    print(f"  {oos} out of date scope — leave in place, ask before moving")
    print(f"  {tbd} to be determined — no destination under the rules")
    print(f"  {low} below 0.50 confidence — route to 00 for a human decision")
    print(f"  {dups} flagged as possible duplicates")
    print("Subject fields read SUBJECT and must be filled in before any rename.")
    print("No file has been moved. Approve rows before executing.")


if __name__ == "__main__":
    main()
