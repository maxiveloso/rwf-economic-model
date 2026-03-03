# Microdata Access Checklist

## RightWalk Foundation -- Data Coordination Artifact

---

**Date**: February 16, 2026
**Purpose**: Consolidate all datasets needed for model validation, secondary analysis, and tracer study into one actionable checklist with owners, timelines, and access steps.

---

## 1. Dataset Inventory

### 1.1 External Datasets (Secondary Analysis)

| # | Dataset | Needed For | Key Variables | Owner/Source | Access Method | Approval Needed | Status | Priority |
|:--|:--------|:-----------|:--------------|:-------------|:--------------|:----------------|:-------|:---------|
| 1 | **Young Lives India (Round 1-5)** | Track A: P_FORMAL_RTE validation | School type, employment at age 19-20, wealth index, test scores | UK Data Service | Online registration + data use agreement | Academic DUA (free) | **NOT STARTED** | **CRITICAL** |
| 2 | **IHDS-II (2011-12)** | Track A: PSM analysis of private school → employment | School type (ED6), contract (WS4), PF/ESI (WS7), COPC, caste | ICPSR (U of Michigan) | Online download after registration | Standard ICPSR DUA | **NOT STARTED** | **HIGH** |
| 3 | **PLFS 2023-24 (Unit-Level)** | Validate P_FORMAL_HS = 9.1%, regional breakdowns | Employment type, education, wages, state, age, gender | MOSPI | Online application | MOSPI approval (~1 week) | **NOT STARTED** | **MODERATE** |
| 4 | **NSSO 75th Round (2017-18)** | Selection into private schooling analysis | School type, household MPCE, caste, education expenditure | MOSPI | Online application | MOSPI approval (~1 week) | **NOT STARTED** | **LOW** |
| 5 | **UDISE+ (School-Level)** | Update RTE seat fill rate, tracer sampling frame | EWS enrollment, seats reserved/filled, school characteristics | UDISE+ dashboard | Public (dashboard); bulk download needs request | None for dashboard | **NOT STARTED** | **MODERATE** |

### 1.2 Internal Data (RWF Program Records)

| # | Dataset | Needed For | Key Variables | Owner | Access Method | Status | Priority |
|:--|:--------|:-----------|:--------------|:------|:--------------|:-------|:---------|
| 6 | **RWF Apprenticeship Tracking Database** | Confirm 68% placement rate, sample size, gender breakdown | Beneficiary name, trade, completion status, placement status, employer, gender | RWF Operations (Akash/Shipra) | Internal request | **NEEDS CONFIRMATION** | **CRITICAL** |
| 7 | **RWF RTE Beneficiary Records** | Tracer sampling frame + contact info | Name, school, enrollment year, contact info, location, gender | RWF Program Team | Internal request | **NEEDS CONFIRMATION** | **CRITICAL** |
| 8 | **RWF Cost Data (Detailed)** | BCR cost denominator validation | Per-beneficiary costs by intervention, overhead allocation | RWF Finance | Internal request | **NOT STARTED** | **HIGH** |

### 1.3 Tracer Study Data (To Be Collected)

| # | Dataset | Needed For | Status | Dependency |
|:--|:--------|:-----------|:-------|:-----------|
| 9 | Tracer baseline survey | All priority parameters | **PLANNING** | Depends on #6, #7 (sampling frame) |
| 10 | Tracer follow-up 1 (6 months) | Retention, wage trajectory | **FUTURE** | Depends on #9 |
| 11 | Tracer follow-up 2 (12 months) | Decay estimation, panel | **FUTURE** | Depends on #9 |

---

## 2. Critical Path Items

### ⚠ CRITICAL: RWF Beneficiary Records (#6, #7)

**These are the tracer study sampling frame. If contact information is incomplete or inaccessible, the entire tracer plan is at risk.**

Questions to resolve immediately:

1. **Does a structured database exist?** (vs. scattered spreadsheets, paper records)
2. **What fields are available?** (Name, phone, address, school/employer, enrollment year)
3. **How complete is the contact information?** (If <60% have valid phone/address, budget for tracking costs increases significantly)
4. **Are 2015-2018 cohort records available?** (Needed for cross-cohort decay estimation; older records may be less complete)
5. **Can records be disaggregated by gender?** (Gender field present in enrollment data?)

**GO / NO-GO**: If RWF cannot produce a usable sampling frame with ≥500 contactable beneficiaries per intervention, the tracer design must be revised (e.g., snowball sampling from a smaller seed, or geographic clustering around known program sites).

### ⚠ HIGH: Young Lives Data Access (#1)

Young Lives is the single most feasible dataset for Track A (P_FORMAL_RTE desk validation). Registration takes 1-3 days, but data cleaning and variable construction add 1-2 weeks. Starting access now means Track A results could be available within 3 weeks.

---

## 3. Immediate Actions (This Week)

| # | Action | Owner | Timeline | Notes |
|:--|:-------|:------|:---------|:------|
| 1 | **Confirm RWF apprenticeship tracking database** -- request structured export with: beneficiary ID, trade, completion date, placement status, employer name, gender | Akash / Shipra | This week | Needed to confirm 68% rate sample size and enable gender breakdown |
| 2 | **Confirm RWF RTE beneficiary records** -- request structured export with: beneficiary ID, school name, enrollment year, last known contact info, gender, location | Program Team | This week | Tracer sampling frame GO/NO-GO depends on this |
| 3 | **Register for Young Lives data** -- UK Data Service account creation and data download request | Analyst (TBD) | This week (1-3 days) | Free; academic DUA; Round 1-5 linked dataset |
| 4 | **Register for IHDS-II data** -- ICPSR account creation and download | Analyst (TBD) | This week (1-2 days) | Free; standard DUA; linked IHDS-I + IHDS-II |
| 5 | **Request PLFS 2023-24 unit-level data** -- MOSPI microdata portal application | Analyst (TBD) | Submit this week (approval ~1 week) | Needed for regional P_FORMAL breakdowns |

---

## 4. Compliance Notes

### 4.1 External Data

- **Young Lives / IHDS-II**: Standard academic data use agreements. No personal data -- all anonymized. Can be used for model validation without additional IRB.
- **PLFS / NSSO**: Government survey microdata. MOSPI requires brief justification of use. No restrictions on academic analysis.
- **UDISE+**: Public administrative data. No restrictions.

### 4.2 Internal Data (RWF Records)

- **Data sharing agreement**: If an external analyst accesses RWF beneficiary records, a data sharing agreement should be executed specifying: purpose limitation, data retention period, destruction protocol, and prohibition on re-identification.
- **Consent**: Tracer study will require informed consent from all respondents. Consent protocol to be developed during tracer design phase (not needed for this checklist).
- **IRB**: If the tracer study is intended for academic publication, IRB/ethics committee approval is required. If for internal decision-making only, a lighter review may suffice. Flag with RWF leadership early.

### 4.3 GDPR / Indian Data Protection

- The Digital Personal Data Protection Act, 2023 (DPDPA) applies to collection of personal data from beneficiaries. Ensure: (a) lawful purpose, (b) informed consent, (c) data minimization, (d) secure storage. These become binding during tracer implementation, not during secondary analysis of anonymized survey data.

---

## 5. Timeline Summary

| Week | Access Goal | Dependent Tasks |
|:-----|:-----------|:----------------|
| Week 1 | Confirm RWF internal data access (#6, #7) | Tracer sampling frame |
| Week 1 | Register for Young Lives + IHDS-II (#1, #2) | Track A desk analysis |
| Week 1-2 | Submit PLFS application (#3) | Regional P_FORMAL validation |
| Week 2-3 | Download and clean Young Lives data | Track A analysis |
| Week 3-4 | Complete Track A primary analysis | P_FORMAL_RTE validation memo |
| Week 4-6 | Assess RWF records quality; determine tracer feasibility | Tracer GO/NO-GO decision |

---

*Document created: February 16, 2026*
*Inputs: validation_plan.md (Task #4), gender_data_assessment.md (Task #6), trade_halflife_summary.md (Task #7), tracer_onepager_v2.md*
