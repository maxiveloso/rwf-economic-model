# RightWalk Foundation Economic Impact Assessment
## Executive Summary | Proof-of-Concept Results

**Date:** February 2026
**Prepared by:** RWF Analytics Team

---

## 1. Introduction

This analysis estimates the lifetime economic benefits of RightWalk Foundation's interventions in Right to Education (RTE) and Apprenticeship programs. Using a Lifetime Net Present Value (LNPV) model calibrated with publicly available wage data and education literature, we provide order-of-magnitude benefit estimates across four macro-regions of India. This Proof-of-Concept delivers decision-useful ranges to assess program cost-effectiveness while explicitly acknowledging methodological limitations.

---

## What We Found

> **Summary Finding:**
> Both RTE and Apprenticeship interventions generate positive lifetime returns across all 32 demographic-regional scenarios analyzed. Apprenticeship yields higher per-beneficiary returns (Rs 36L average) but requires greater upfront investment and operational complexity. RTE yields lower returns (Rs 9L average) but is more scalable and has lower per-beneficiary costs. The key driver for both interventions is improved formal sector employment—accounting for ~80% of RTE benefits and being the primary differentiator for Apprenticeship outcomes.

---

## Decision Rules

| If your priority is... | Consider... | Because... |
|------------------------|-------------|------------|
| Maximize per-beneficiary impact | Apprenticeship | 4x higher LNPV than RTE |
| Maximize reach with limited budget | RTE | Lower cost, simpler delivery model |
| Serve underserved regions | Targeted Apprenticeship | Higher marginal returns in low-baseline areas |
| Long-term systemic change | RTE | Creates educational pathway shift across generations |
| Quick wins / demonstrable outcomes | Apprenticeship | Shorter time to employment outcomes |

---

## 2. Key Findings

### RTE Intervention
- **LNPV Range:** Rs 5.2L - Rs 28.7L per beneficiary
  - Highest: Urban South (Rs 28.7L male, Rs 22.1L female)
  - Lowest: Rural East (Rs 7.7L male, Rs 5.2L female)
- **Average LNPV:** Rs 14.0L
- **Decomposition:** ~79% from Placement Effect (30% vs 9.1% formal entry), ~21% from Mincer Effect

### Apprenticeship Intervention
- **LNPV Range:** Rs 18.6L - Rs 52.3L per beneficiary
  - Highest: Urban South (Rs 52.3L male, Rs 41.2L female)
  - Lowest: Rural East (Rs 26.9L male, Rs 18.6L female)
- **Average LNPV:** Rs 34.4L
- **Key Driver:** 68% formal sector placement rate

### Break-Even Cost Thresholds

| Intervention | Max Cost at BCR=3:1 (Range) | Mean Max Cost |
|--------------|----------------------------|---------------|
| RTE | Rs 1.89L - Rs 10.06L | Rs 4.96L |
| Apprenticeship | Rs 6.58L - Rs 18.48L | Rs 12.13L |

**Interpretation:** If actual program cost per beneficiary is below these thresholds, the intervention achieves a 3:1 benefit-cost ratio.

### Dual BCR Analysis (February 2026)

Two perspectives on Return on Investment:

| Metric | RTE | Apprenticeship |
|--------|-----|----------------|
| **Average LNPV** | Rs 14.9 Lakhs | Rs 36.4 Lakhs |
| **Full BCR** (Total Investment) | 14.3× (range 5.4-29.0) | 23.0× (range 12.5-35.0) |
| **RWF-only BCR** (Direct Spend) | 372× (range 141-755) | 606× (range 329-924) |
| **RWF Direct Cost** | Rs 4,000 | Rs 6,000 |
| **Total Investment** | Rs 1.04 Lakhs | Rs 1.58 Lakhs |
| **Unlock Multiplier** | 26× | 39.6× |

> **Full BCR**: Total benefits / total costs (RWF + government + private co-finance)
> **RWF-only BCR**: Total benefits / RWF direct spend only (funder ROI perspective)
> **Unlock Multiplier**: Total investment unlocked per rupee of RWF direct spend

### Sensitivity Results
- Monte Carlo median within 11% of baseline (high consistency)
- Critical uncertainty: P_FORMAL parameters and Apprentice decay half-life drive 50-70% of LNPV variation
- Even under pessimistic assumptions, both interventions remain positive

---

## 3. Methodology

We apply a Lifetime Net Present Value (LNPV) framework that computes:

**NPV = Sum[t=0 to T] (W_treatment(t) - W_control(t)) / (1+d)^t**

- Treatment effects estimated via Mincer wage equations calibrated to PLFS 2023-24 data
- Formal/informal sector wage trajectories modeled separately (+1.5%/year formal, -0.2%/year informal)
- 40-year career horizon with 5% social discount rate
- Treatment/control groups constructed synthetically based on formal sector entry probabilities

---

## 4. Regional & Demographic Insights

| Region | RTE Average LNPV | Apprenticeship Average LNPV |
|--------|------------------|----------------------------|
| South | Rs 13.3L | Rs 40.1L |
| West | Rs 10.6L | Rs 38.7L |
| North | Rs 7.4L | Rs 35.5L |
| East | Rs 5.6L | Rs 31.4L |

**Key Patterns:**
- Urban beneficiaries: LNPV 30-50% higher than rural
- South/West regions: LNPV 20-40% higher than North/East
- Gender: Similar LNPVs within scenarios (male ~45% higher due to baseline wage gaps)

---

## 5. Limitations

1. **Causal Identification:** Selection-on-observables assumption may overstate effects by 20-40% if motivated families self-select into programs
2. **Geographic Granularity:** State/district-level effects require microdata not available in this PoC
3. **Wage Persistence (h):** Apprenticeship premium decay rate (10-year half-life) is assumed; could be faster or slower
4. **External Validity:** Literature-based parameters may not generalize to RWF-specific beneficiaries
5. **No Beneficiary Data:** Estimates use population averages, not actual RWF participant outcomes
6. **P_FORMAL Split:** 30% RTE vs 9.1% control based on RWF guidance, not observed longitudinal data

---

## 6. Recommendations

### Program-Level
- Both interventions likely cost-effective; evidence supports continued investment
- Apprenticeship provides higher per-beneficiary impact but requires more operational capacity

### Geographic Focus
- Prioritize expansion in South/West urban areas (highest returns)
- For North/East rural, consider complementary interventions or accept lower BCR for equity

### Data Investment (Priority — Fully Designed)
- **Longitudinal tracer study** (18 months) tracking 1,200-1,600 beneficiaries across RTE, Apprenticeship, and matched comparison groups
- **Design:** Gender × trade × vintage stratification, propensity score matching, cross-cohort decay estimation
- **Budget:** Rs 45-55 lakhs
- **Impact:** Reduce parameter uncertainty from ±50% to ±15-20% for top 4 parameters
- See full proposal: [`deliverables/tracer/tracer_onepager_v2.md`](../deliverables/tracer/tracer_onepager_v2.md)

### Quick Wins (No New Data Collection)
- PLFS unit-level microdata access (Rs 1-2L, 2-3 months)
- Gender-disaggregated reporting from existing RWF operational data
- Trade-specific outcome tracking in current apprenticeship MIS

### Full Causal Evaluation
- 150-200 hour project with beneficiary microdata from tracer study would enable propensity score matching and difference-in-differences

---

## Closing Statement

> This Proof-of-Concept provides sufficient evidence to justify continued investment in RWF's interventions, with clear pathways to reduce uncertainty through targeted data collection. Both programs generate positive lifetime returns across all scenarios tested. The key question isn't whether these interventions work—it's how to optimize their delivery for maximum impact.

---

### Post-Delivery Deep Dives (February 2026)

Following the initial PoC delivery, 10 additional analytical workstreams were completed. Key outputs include gender funnel analysis, trade half-life taxonomy, policy persistence scenarios, evidence quality audit, and a fully designed tracer study. All deliverables are available in [`deliverables/`](../deliverables/README_release.md).

---

**Appendix:** Technical Appendix (5-7 pages) provides detailed methodology, complete parameter specifications, sensitivity analyses, and validation results. See also [`deliverables/appendices/`](../deliverables/appendices/) for assumptions methodology, evidence gaps, and parameter evidence table.

**Model Version:** economic_core_v4.py | parameter_registry_v3.py | v4.4
**Validation Status:** 8/8 QA checks passed (February 2026)
