# Classifier rulesets actually used (ordered; first match wins)

Titles are lowercased before matching. These encode the owner's real
vocabulary and typos — reuse them rather than writing new ones.

## Financials

```python
RULES=[
 ("MISSIONX", r"steven kollar mission statement"),   # routed OUT to Personal
 ("CASHAPP",  r"cash_app_report|cash app"),
 ("CHASE",    r"^chase|statements-1602"),
 ("RENTLED",  r"rent_ledger|rent ledger"),
 ("DONNY",    r"donny"),
 ("PL",       r"profit and loss|^p&l"),
 ("BUDGET",   r"budget|rehab_scan|rehab-budget|deercreek"),
 ("NOTES",    r"note_purchase|^purchase |^option purchase"),
 ("RECEIPT",  r"receipt|invoice|payment_history"),
 ("TAXW9",    r"tax lein|^w9"),
 ("ACCT",     r"asset and loan details|bank balances|titan bank|one main cc"),
 ("TXN",      r"^transactions|individual-transaction"),
 ("FUND",     r"non-repayable funds"),
]
```
Bucket -> folder: CASHAPP `19NxBPljZsQ3pmQeWBvj8gx_T-FVuCGoM` · TXN
`18PouIpbiHtQYgL-OvrWZcVOXZW8aUJWV` · CHASE `1Len52CYX6jZ2gHtkxootZ5gOidqa524c` ·
BUDGET `1b9zWVNz3dWXQNqB1Nj3UVrPvP3CH3-hf` · NOTES `1oD8EMgelhSFtUItkp-_IclQRM2ew4y1s` ·
RENTLED `1pY9JUjZhhPzxYq0bZctQXIWyljv78GLY` · ACCT `1ccv1GowZ67DARbqeGfSRua-chPCIqrw7` ·
PL `1RhA3bPyvkZSsCwg8cfEDTosgsSEX59fL` · DONNY `1Caz1IzrDemw0PQmDrfgpfP8xcTYVUTyi` ·
TAXW9 `1m4jG_17vVCvQHuhOfmPw4KWL7rONXOJJ` · FUND `1dIpyyi3ci_0ZeNnnqPcP2nxG1kiZ3vx7` ·
RECEIPT `1IXIOzgKF61IQ6Ym6GZKhi4tC9cAP0jy_`

## Legal & company documents

```python
RULES=[
 ("TODD",      r"^0[1-8]_|todd_paid_work|residential_payment_reset|property_upkeep_lawn|option_[abc]_|no_agreement_reservation|account_status_statement"),
 ("REOTHER",   r"shadow creek|receivership sale"),
 ("ATTYASST",  r"attorney-assistant|client-intake-sop|intake-systems"),
 ("PHXMGMT",   r"phoenix_legal_war|phoenix legal war|phoenix_legal_case|legal_case_control|collections_loc|phoenix_legal_collections"),
 ("AGCASE",    r"_ag_judgment|indiana_attorney_general_complaint|disciplinary_commission_grievance|attorney general|attorney geeneral|attorney misconduct|kollar v|511 ag|appeal 511|steven_kollar_revised_complaint|proposed_agreed_amended_judgment|rokita|griner|511 35th"),
 ("SANCOME",   r"sancome|sancomne"),
 ("BIGGS",     r"biggs|sfr.?11|sfr fund 11|sfr_11|tri state furs|tri sate furs|lewis response|lewis transcripts"),
 ("MASSA",     r"massa|\bm60\b|kodax|koidax|dan case|meeting: dan"),
 ("BANKRUPT",  r"chapter 11|26-50689|tower capital group"),
 ("TAXNOTICE", r"noticesandletters|^1801\d+"),
 ("PPM",       r"\bppm\b|ppm_|fund2_ppm|private debt fund|fractionalized|investor due diligence|residential_income_fund"),
 ("TITLE",     r"title commitment|title product package|commitment a\.|fatc commitment|velocity-title|quitclaim|balloon fixed rate note|note endorsed|note 1243|\balta\b"),
 ("TAXSALE",   r"tax sale|surplus funds|excess proceeds|koerber"),
 ("ENTITY",    r"operating agreement|opertaing agreement|certificate of (assumed|compliance)|filinghistory|cp_575|\bein\b|clarification log|arkham blue|gpre mw|nah\.png|north america hold|filingservices|\bw 9\b|trust paperwork|1129 +trust|^sfr 11 llc|welcome! overview"),
 ("RESEARCH",  r"^i reviewed|^i've reviewed|^i’ve reviewed|^i’ll|^i'll|^i want to|^yes\.|^this document outlines|^an analysis|^indiana’s|^indiana's|^phoenix, i reviewed|^latest legal cases"),
 ("LEASE",     r"\blease\b|land contract|rental affidavit|section 8|cottage grove"),
 ("CONTRACT",  r"agreement|contract(?!or|ing)|_nda|\bnda\b|transaction fee|receivables_purchase|buyout|services contract|term sheet"),
 ("COURT",     r"order |^order|motion|complaint|exhibit|appendix|judgment|judgement|stipulation|answer to|interrogator|plaintiffs notice|proposed order|brief -|consent to withdraw|doc_3\d|l4kjz|request for interpreter|intervenor|filed|court|\sv\.?\s|\sv\.?$"),
]
```
COURT was too big (105) and got a second pass:
```python
if b=="COURT":
    if   re.search(r'exhibit|appendix', t):                       b='EXHIBIT'
    elif re.search(r'^order|order |judgment \(entered\)|judgement', t): b='ORDER'
    elif re.search(r'motion|withdraw|intervenor|stipulation', t):  b='MOTION'
    elif re.search(r'complaint|answer|interrogator|pleading', t):  b='PLEADING'
    else:                                                          b='COURTMISC'
```

## Templates

```python
RULES=[
 ("REUW",     r"168_unit|underwriting"),
 ("RC",       r"relevant_communities"),
 ("SKBRAND",  r"steven_kollar_"),
 ("PHXOS",    r"phoenix operating system|phoenix war room|phoenix master dashboard|phoenix_operating_system|phoenix_weekly_executive_dashboard|phoenix_one_page_dashboard|phoenix_executive_os|your operating system"),
 ("PHXPLAY",  r"phoenix_implementation_playbook|phoenix_logon|project_logon|phoenix_executive_manager|phoenix_top_10|phoenix_project_inventory|phoenix_risk_and_resistance|phoenix_ragnar"),
 ("PHXBIO",   r"phoenix_bio|phoenix_personal_blueprint|phoenix knowledge base|^phoenix,|built a blueprint|ground this in your actual workspace"),
 ("DLP",      r"dlp-elite|elite-compass|personal compass|family compass|quarterly-clarity|rrek-template|24-practices|2021-life-assessment"),
 ("HEALTH",   r"health matrix|rise dash board"),
 ("QUEST",    r"questionnaire"),
 ("REHAB",    r"rehab guild|decommissioning|entity-checklist"),
 ("BIZ",      r"business blueprints|business-scaling-blueprint|playbooks-hvco|hiring playbook|retirement playbook|buy back your time"),
 ("PROJ",     r"project_conversation_log|strategic_project_thinking|weekly_production_template|mistakes_lessons_learned"),
]
```

## Personal documents

```python
RULES=[
 ("SKIPMED", r"hernia|surgery|recovery_log"),   # EXCLUDED from the queue entirely
 ("ICLOUD",  r"icloud photos"),
 ("SHOT",    r"^screenshot"),
 ("PHOTO",   r"^chatgpt image|^img_|^copy of img_"),
 ("PHXSYS",  r"^daily phoenix|phoenix_form_command|phoenix_hard_core|phoenix_open_loops|phoenix_operator_doctrine|phoenix_personal_operating|phoenix_project_conversation|phoenix_systems_thinking|^phoenix, you have"),
 ("MISSION", r"mission statement|founder profile|life timeline|price of principles|demartini"),
]
```
SKIPMED must be filtered out before the queue is built:
```bash
grep -v $'\tSKIPMED\t' per_plan.tsv | awk -F'\t' 'NR==FNR{m[$1]=$2;next}{print $1"\t"m[$2]}' pmap.txt - > pq.tsv
```
