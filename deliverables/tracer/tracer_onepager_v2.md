# Tracer Study Proposal (v2)
## RightWalk Foundation -- Economic Impact Validation

> **Updated February 16, 2026** with inputs from Tasks #9 (Evidence Table), #6 (Gender Assessment), #7 (Trade Half-Life Taxonomy), #4 (Private Schooling Validation Plan)

---

### Objective

Validate key model parameters (formal sector placement rates, wage uplift, retention, skill decay) and generate defensible BCR inputs. Currently, 3 of 12 high-impact parameters have LOW confidence and zero empirical grounding. The tracer study is the single most cost-effective intervention to close these evidence gaps.

### Priority Research Questions

1. **P_FORMAL_RTE validation** (Priority #1, elasticity 1.11): What proportion of RTE 25% quota beneficiaries enter formal employment? Current assumption: 30%. No empirical data exists anywhere.
2. **External validation of P_FORMAL_APPRENTICE** (Priority #2): Is the 68% placement rate (from RWF internal data) replicated with external measurement and broader sampling?
3. **Trade-specific decay estimation** (Priority #3): Do skill premiums persist differently across trade categories (IT vs. electrician vs. health)?
4. **Gender-disaggregated outcomes** (Priority #4): Do formal placement rates, wages, and retention differ significantly by gender?

### Who to Sample

| Group | N | Source | Stratification |
|-------|---|--------|----------------|
| **RTE beneficiaries** | 300-400 | 2018-2024 cohorts, 3-4 states | Gender × urban/rural × school type |
| **Apprenticeship completers** | 300-400 | 2015-2024 cohorts (expanded) | Gender × trade category (A/B/C/D) × vintage year |
| **Comparison group** | 600-800 | Matched non-beneficiaries via PSM (1:1) | Same demographics, no program exposure |
| **Total** | **1,200-1,600** | Targeting 70%+ response rate | |

**Changes from v1**:
- Apprenticeship vintage expanded to include **2015-2018 cohorts** (needed for cross-cohort decay estimation; minimum 75-100 per vintage for survival analysis)
- Stratification now includes **trade category** (4-category taxonomy: rapid/moderate/durable/long-term) and **gender** as primary strata
- RTE group adds **school type** (government/private aided/private unaided) and **RTE enrollment flag** variables

### Outcomes Measured

| Category | Measures | Model Parameter | New Variables (v2) |
|----------|----------|-----------------|-------------------|
| **Employment status** | Employed/unemployed/self-employed | P_FORMAL_RTE, P_FORMAL_APPRENTICE | -- |
| **Formal sector indicators** | Written contract, PF/EPF, ESI, regular salary | P_FORMAL (all) | **Employer sector** (govt/large private/small private/self) |
| **Wages** | Monthly gross, starting salary | APPRENTICE_INITIAL_PREMIUM | -- |
| **Retention/decay** | Job tenure, sector persistence | APPRENTICE_DECAY_HALFLIFE | **Job start/end dates (all jobs since completion)**, trade relevance (1-5) |
| **Education history** | Highest grade, school type, RTE flag | RTE_RETENTION_FUNNEL | **RTE enrollment flag**, years under RTE, board exam scores |
| **Gender-specific** | LFPR, reasons for non-participation | Gender-disaggregated P_FORMAL | **Household decision-making** (2 questions), **workplace safety** (3 questions) |
| **Mechanism** | How found job, school name effect, placement support | Qualitative pathway | **Job search method**, school signaling (Likert 1-5) |
| **Taxes/contributions** *(optional)* | PF/ESI enrollment, income tax | Government revenue estimate | -- |

### SES Controls for Matching

- Household income at enrollment (recalled), parental education, caste, religion, urban/rural at age 6, number of siblings, current location

### Verification

- **Payslips:** 15-20% of respondents for wage validation
- **Contracts:** Employment contract review for formal sector classification
- **Employer confirmation:** Phone verification for 10-15% subset

### Timeline

| Phase | Duration | Notes |
|-------|----------|-------|
| Design & ethics approval | 2-3 months | IRB submission; questionnaire finalization |
| Sampling frame construction | 1-2 months | **CRITICAL PATH**: RWF beneficiary contact records |
| Baseline data collection | 2-3 months | Exit survey for recent cohorts |
| Follow-up 1 | Month 8-9 | 6 months post-baseline |
| Follow-up 2 | Month 14-15 | 12 months post-baseline |
| Follow-up 3 *(optional)* | Month 26-27 | 24 months post-baseline |

**Core duration:** 18 months | **Extended:** 24-30 months

### Budget Estimate

| Activity | % of Budget | Est. Cost (1,200+ sample) |
|----------|-------------|---------------------------|
| **Fieldwork** (surveys, travel, enumerators) | 45% | Rs 20-25 lakhs |
| **Sampling frame & tracking** (older cohorts) | 10% | Rs 5-6 lakhs |
| **Data entry & cleaning** | 12% | Rs 5-6 lakhs |
| **Verification** (payslips, employer calls) | 13% | Rs 6-7 lakhs |
| **Analysis & reporting** | 20% | Rs 9-11 lakhs |
| **Total** | 100% | **Rs 45-55 lakhs** |

**Budget impact of v2 changes**: Expanded vintage range (+Rs 5-8 lakhs for locating 2015-2018 completers) and additional gender/mechanism modules (+Rs 2-3 lakhs for longer surveys). Total increase: ~Rs 7-11 lakhs vs. v1 estimate (Rs 30-35 lakhs for 800 sample).

### How It Feeds the Model

| Parameter | Current Source | Confidence | After Year 1 |
|-----------|----------------|------------|--------------|
| P_FORMAL_RTE | Assumption (30%) | **LOW** | **Validated from tracer data** |
| P_FORMAL_APPRENTICE | RWF internal (68%) | **HIGH** | **Externally validated** |
| APPRENTICE_INITIAL_PREMIUM | Literature (Rs 84k) | **MODERATE** | **RWF-specific wage gap** |
| APPRENTICE_DECAY_HALFLIFE | Assumed (10 years) | **LOW** | **Cross-cohort + trade-stratified estimate** |
| RTE_RETENTION_FUNNEL | Assumed (60%) | **LOW** | **Retrospective grade completion data** |
| Gender-disaggregated P_FORMAL | Not available | **N/A** | **Gender-specific placement rates** |

**Year 1 results replace current assumptions.** Expected: reduce parameter uncertainty from ±50% to ±15-20% for top 4 parameters.

### Power Analysis Summary (from Task #9)

| Parameter | Effect Size | N per arm (simple) | N per arm (stratified) | Tracer Target | Adequate? |
|-----------|-------------|-------------------|----------------------|---------------|-----------|
| P_FORMAL_RTE (30% vs 9.1%) | 20.9 pp | ~53 | ~320 | 300-400 | Yes |
| P_FORMAL_APPRENTICE (68% vs 9%) | 59 pp | ~7 | ~60-80 | 300-400 | Yes (oversized) |
| APPRENTICE_DECAY (cross-cohort) | N/A | ~100/vintage | ~400-600 total | 300-400 | Marginal -- needs older cohorts |

---

**Contact:** [TBD]
**Detailed crosswalk:** See Annex D (Parameter-Question Mapping)
**Supporting documents:** parameter_evidence_table.md, validation_plan.md, gender_data_assessment.md, trade_halflife_summary.md
