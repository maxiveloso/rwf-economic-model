# Evidence Gaps, Budget Note & SROI Roadmap

## RightWalk Foundation -- Economic Impact Model

---

**Date**: February 16, 2026
**Purpose**: Synthesis for funders -- what evidence is missing, what it costs to close each gap, and the path from current wage-only BCR to credible SROI.

---

## 1. Gap Inventory

### 1.1 Evidence Gap Table

| # | Gap | Parameter Affected | Current Basis | What's Needed | Est. Cost | Timeline | Tracer Covers? |
|:--|:----|:-------------------|:-------------|:--------------|:----------|:---------|:---------------|
| 1 | **No data on RTE graduate employment** | P_FORMAL_RTE (elasticity 1.11) | Expert assumption (30%) | Employment survey of RTE beneficiaries | Rs 0 (desk) + Rs 20-25L (tracer) | 3 weeks (desk) / 18 months (tracer) | **Yes -- primary target** |
| 2 | **No India longitudinal data on skill decay** | APPRENTICE_DECAY_HALFLIFE | International proxy (10 yr) | Cross-cohort wage/employment survey of multiple vintage years | Rs 5-8L (incremental) | 18 months (tracer) | **Yes -- cross-cohort design** |
| 3 | **External validation of 68% placement** | P_FORMAL_APPRENTICE | RWF internal data only | Independent verification with employment contracts/payslips | Rs 4-5L (verification) | 6-12 months | **Yes -- verification module** |
| 4 | **No RTE-specific retention data** | RTE_RETENTION_FUNNEL (60%) | Private school proxy | Retrospective education history from RTE cohorts | Rs 0 (embedded in tracer) | 18 months | **Yes -- education module** |
| 5 | **Single-state RCT for test score gain** | RTE_TEST_SCORE_GAIN (0.137 SD) | AP School Choice RCT | Young Lives secondary analysis + tracer education data | Rs 0 (desk research) | 3 weeks | **Partially -- education attainment data** |
| 6 | **No India-specific score-to-years factor** | TEST_SCORE_TO_YEARS (6.8) | Global LMIC meta-analysis | Desk research linking Indian test scores to labor market | Rs 0 (desk) | 2-4 weeks | **No** |
| 7 | **No gender-disaggregated placement rates** | P_FORMAL by gender | Not available | Gender-stratified employment outcomes | Rs 2-3L (longer surveys) | 18 months | **Yes -- gender module** |
| 8 | **RWF cost data not independently verified** | BCR denominator | RWF self-reported | Financial audit or independent cost verification | Rs 1-2L | 1-2 months | **No** |

### 1.2 Gap Severity Summary

| Severity | Count | Parameters |
|:---------|:------|:-----------|
| **Critical** (model depends on it, zero data) | 2 | P_FORMAL_RTE, APPRENTICE_DECAY_HALFLIFE |
| **High** (data exists but needs validation) | 3 | P_FORMAL_APPRENTICE, RTE_RETENTION_FUNNEL, gender disaggregation |
| **Moderate** (desk research can address) | 3 | RTE_TEST_SCORE_GAIN, TEST_SCORE_TO_YEARS, cost verification |

---

## 2. Budget Summary

### 2.1 What's Free (Desk Research)

| Activity | Cost | Timeline | Gaps Addressed |
|:---------|:-----|:---------|:---------------|
| Young Lives secondary analysis (Track A) | Rs 0 (existing staff + free data) | 3 weeks | #1 (partial), #5 |
| IHDS-II secondary analysis | Rs 0 | 3 weeks (concurrent) | #1 (partial) |
| PLFS microdata analysis (regional P_FORMAL) | Rs 0 | 1-2 weeks | #1 (baseline validation) |
| Test-score-to-years literature review | Rs 0 | 2 weeks | #6 |
| **Subtotal** | **Rs 0** | **3-4 weeks** | **4 of 8 gaps (partially)** |

### 2.2 What Needs Internal Action (Near-Zero Cost)

| Activity | Cost | Timeline | Gaps Addressed |
|:---------|:-----|:---------|:---------------|
| Re-query 68% placement by gender from RWF data | Rs 0 | 1-2 weeks | #3 (partial), #7 (partial) |
| Confirm RWF beneficiary records quality | Rs 0 | 1 week | Tracer GO/NO-GO |
| Independent cost data review | Rs 1-2L | 1-2 months | #8 |
| **Subtotal** | **Rs 1-2L** | **1-2 months** | **3 of 8 gaps** |

### 2.3 What Needs Funded Research (Tracer Study)

| Component | Cost | Gaps Addressed |
|:----------|:-----|:---------------|
| Core tracer fieldwork (1,200+ sample) | Rs 20-25L | #1, #3, #4, #7 |
| Older cohort tracking (2015-2018) | Rs 5-8L | #2 |
| Verification module (payslips, employer) | Rs 6-7L | #3 |
| Gender & mechanism modules | Rs 2-3L | #7 |
| Data entry, cleaning, analysis | Rs 14-17L | All |
| **Subtotal** | **Rs 45-55L** | **7 of 8 gaps** |

### 2.4 Total Investment Required

| Tier | Cost | Timeline | Gaps Closed |
|:-----|:-----|:---------|:------------|
| **Tier 1: Desk research** | **Rs 0** | 3-4 weeks | Partial on 4 gaps |
| **Tier 2: Internal data actions** | **Rs 1-2 lakhs** | 1-2 months | Partial on 3 gaps |
| **Tier 3: Tracer study** | **Rs 45-55 lakhs** | 18 months | Full on 7 of 8 gaps |
| **TOTAL** | **Rs 46-57 lakhs** | 18 months | **All 8 gaps addressed** |

**Key message for funders**: One investment (the tracer study at Rs 45-55L) closes 7 of 8 evidence gaps simultaneously. The remaining gap (TEST_SCORE_TO_YEARS) is addressable through zero-cost desk research.

---

## 3. Priority Order

Execute cheapest and fastest first:

1. **Week 1-3**: Desk research (Rs 0) -- Young Lives + IHDS-II secondary analysis for P_FORMAL_RTE directional evidence
2. **Week 1-2**: Internal data actions (Rs 0) -- Confirm RWF tracking data, re-query by gender
3. **Month 1-2**: Cost verification (Rs 1-2L) -- Independent review of BCR cost denominators
4. **Month 2-18**: Tracer study (Rs 45-55L) -- Comprehensive primary data collection

**Decision gate**: After Week 3 desk research, decide whether P_FORMAL_RTE assumption needs revision *before* investing in the tracer. If desk evidence suggests P_FORMAL_RTE < 12%, the RTE value proposition may need fundamental reframing (see validation_plan.md Section 4.4).

---

## 4. SROI Roadmap

### 4.1 What RWF Can Credibly Claim Today

**Wage-only BCR** -- the current model estimates lifetime earnings differentials discounted to present value. This is the most conservative and defensible metric:

| Intervention | BCR (RWF-only) | BCR (Full) | Basis |
|:-------------|:----------------|:-----------|:------|
| **RTE (Moderate scenario)** | ~82:1 | ~3.2:1 | Wage differential from formal sector entry + Mincer premium |
| **Apprenticeship (Moderate scenario)** | ~133:1 | ~5.1:1 | Wage differential from formal placement + decaying skill premium |

**What this INCLUDES**: Lifetime earnings differences, experience premiums, formal/informal wage gap, discounting, opportunity costs.

**What this does NOT include**: Tax revenue, health benefits (ESI access), intergenerational effects, reduced welfare dependency, social mobility, civic participation. These are real but not yet quantified.

### 4.2 What Phase 2 Enables (Post-Tracer)

With tracer data, RWF can credibly add:

| Outcome Domain | Data Source | Monetization Approach | Estimated BCR Uplift |
|:---------------|:-----------|:---------------------|:---------------------|
| **Tax revenue** | Formal employment → income tax + PF/ESI contributions | Direct calculation from wage data | +10-15% of BCR |
| **Health outcomes** | ESI enrollment status from tracer | DALY-based valuation or healthcare cost savings | +5-10% of BCR |
| **Intergenerational** | Education aspirations for beneficiaries' children | Reduced intergenerational poverty trap valuation | Directional only |
| **Reduced welfare dependency** | Formal employment reduces dependence on government schemes | Fiscal savings calculation | +3-5% of BCR |

### 4.3 What It Takes to Publish a Credible SROI

A full SROI requires:

1. **Stakeholder consultation** (2-3 months): Map all stakeholder groups, identify material outcomes, agree on scope. This is methodologically required by SROI standards (Social Value International).

2. **Primary data collection via tracer** (12-18 months): Employment, wages, health, education, social participation outcomes for beneficiaries and comparison group.

3. **Monetization of non-wage outcomes** (2-3 months): Assign financial proxies to health improvements, civic participation, intergenerational effects. Requires India-specific willingness-to-pay or cost-of-illness data.

4. **Sensitivity testing and assurance** (1-2 months): Independent review of methodology and assumptions. SROI Network assurance process if pursuing accreditation.

**Total timeline**: 18-24 months from tracer launch to publishable SROI.
**Total cost**: Tracer (Rs 45-55L) + stakeholder consultation (Rs 3-5L) + SROI analysis (Rs 5-8L) = **Rs 53-68 lakhs**.

### 4.4 Conservative vs. Full SROI Framing

| Frame | What It Measures | Credibility | Use Case |
|:------|:-----------------|:------------|:---------|
| **Conservative BCR** (current) | Wages only, individual earnings | **Highest** -- hardest to argue with | Funder due diligence, academic peer review |
| **Extended BCR** (post-tracer) | Wages + tax + ESI | **High** -- all measurable and verifiable | Government advocacy, policy briefs |
| **Full SROI** (future) | Wages + tax + health + intergenerational + social | **Moderate** -- requires assumptions for non-market outcomes | Impact reports, social investor pitches |

**Honest note**: The 1.25-1.45× BCR-to-SROI conversion factor sometimes cited in impact evaluation literature has **no empirical backing** for Indian education/employment programs. Do not use this multiplier. Instead, build the SROI bottom-up from measured outcomes.

---

*Document created: February 16, 2026*
*Inputs: parameter_evidence_table.md (Task #9), validation_plan.md (Task #4), gender_data_assessment.md (Task #6), trade_halflife_summary.md (Task #7), microdata_access_checklist.md (Task #11), tracer_onepager_v2.md*
