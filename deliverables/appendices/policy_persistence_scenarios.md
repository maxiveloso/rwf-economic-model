# Policy Persistence Multiplier: Multi-Cohort Impact Analysis

**Version:** 1.0
**Date:** February 16, 2026
**Status:** Illustrative scenario analysis (not empirically validated)
**Dependencies:** `model/economic_core_v4.py` (v4.4), `model/parameter_registry_v3.py` (v3.4)

---

## 1. Motivation

The RWF economic impact model calculates the Lifetime Net Present Value (LNPV) and Benefit-Cost Ratio (BCR) for **one cohort** of beneficiaries over a 40-year working life. This is the standard unit of analysis.

However, if the policy reforms that RWF helped establish -- the RTE 25% quota implementation and the NATS apprenticeship pipeline -- continue to operate **after RWF exits**, then each subsequent year produces a new cohort of beneficiaries. The cumulative program impact is therefore a multiple of the single-cohort BCR.

This document explores three illustrative scenarios for how much "credit" RWF can claim for post-exit policy persistence, and how that scales the program's effective BCR.

**Critical caveat:** The attribution fractions used below are illustrative and have no empirical basis. They are included to show the *structure* of how persistence affects program valuation, not to make specific claims about RWF's lasting influence. Empirical validation would require tracer studies and institutional analysis.

---

## 2. Parameter Definitions

### 2.1 Policy Persistence Length (T)

The number of years after RWF exits that the policy intervention continues to generate new beneficiary cohorts.

| Scenario     | T (years) | Rationale |
|-------------|-----------|-----------|
| Conservative | 5         | Institutional memory fades quickly without direct support; government programs often lose momentum within one election cycle |
| Moderate     | 10        | Established partnerships and trained government staff sustain delivery for a medium-term period |
| Optimistic   | 15        | Policy is fully institutionalized; RWF's contribution created self-sustaining systems |

### 2.2 Annual Beneficiary Volume (N)

| Intervention    | N (per year) | Source |
|----------------|-------------|--------|
| RTE 25% quota  | 5,000       | [ASSUMED] -- needs RWF confirmation of actual annual intake |
| Apprenticeship (NATS) | 3,000 | [ASSUMED] -- needs RWF confirmation of actual annual placement |

**Note:** These are assumed to be constant across years. In practice, volumes may grow (as government scales) or shrink (as RWF support fades). Constant volume is the simplest assumption and should be updated with actual data.

### 2.3 Attribution Fraction (alpha)

The share of ongoing policy impact that can be reasonably attributed to RWF's original work (capacity building, partnership development, system design). This is the most judgmental parameter.

| Scenario     | alpha | Rationale |
|-------------|-------|-----------|
| Conservative | 0.20 (20%) | RWF was one of several organizations contributing; government would have eventually reached similar capacity independently; only early-mover advantage is attributable |
| Moderate     | 0.40 (40%) | RWF played a catalytic role in establishing the specific delivery model and partnerships; without RWF, the program would operate at reduced effectiveness |
| Optimistic   | 0.60 (60%) | RWF designed the core systems and trained the personnel that continue to operate; the program would not exist in its current form without RWF's foundational work |

### 2.4 Program Intensity Decay (delta)

Annual reduction in program effectiveness as RWF's institutional knowledge, partnerships, and quality oversight fade.

| Scenario     | delta (per year) | Rationale |
|-------------|-----------------|-----------|
| Conservative | 0.05 (5%/yr) | Rapid quality deterioration without active external support; consistent with literature on NGO program fade-out (Bold et al. 2018) |
| Moderate     | 0.03 (3%/yr) | Moderate institutional capacity built; trained government staff retain core competencies for several years |
| Optimistic   | 0.01 (1%/yr) | Near-complete institutionalization; program operates on established systems with minimal quality loss |

---

## 3. Formula

### 3.1 Per-Cohort BCR (baseline)

From the existing model:

```
BCR_cohort = LNPV / Cost_per_beneficiary
```

Where LNPV is the discounted incremental lifetime earnings for one beneficiary, and Cost is the program cost per beneficiary.

### 3.2 Cumulative Program Multiplier

For T years of post-exit persistence, the cumulative multiplier accounts for additional cohorts, weighted by attribution and decayed by intensity loss:

```
M(T) = 1 + SUM_{t=1}^{T} [ alpha * (1 - delta)^t ]
```

Where:
- `M(T)` = cumulative multiplier at year T
- `alpha` = attribution fraction (how much of each new cohort's benefit is credited to RWF)
- `delta` = annual decay rate in program intensity
- `t` = years after RWF exit (t=0 is the final RWF-supported cohort)
- The leading `1` represents the original RWF-supported cohort (t=0)

The geometric sum has a closed form:

```
M(T) = 1 + alpha * (1 - delta) * [ 1 - (1 - delta)^T ] / delta
```

### 3.3 Effective BCR

```
BCR_effective = BCR_cohort * M(T)
```

This represents the total program BCR when accounting for all cohorts (original + post-exit).

### 3.4 Incremental Contribution per Year

For a given year t after exit, the incremental BCR contribution from that year's new cohort is:

```
Incremental_BCR(t) = BCR_cohort * alpha * (1 - delta)^t
```

---

## 4. Reference Per-Cohort BCR Values

From the model (cross-demographic average of 16 demographic cells per scenario):

### 4.1 Moderate Scenario (primary reference)

| Metric | RTE | Apprenticeship |
|--------|-----|----------------|
| Average LNPV (INR) | 14,89,011 | 36,38,550 |
| Average LNPV (lakhs) | 14.89 | 36.39 |
| Cost: RWF-only (INR) | 4,000 | 6,000 |
| Cost: Total investment (INR) | 1,04,000 | 1,58,460 |
| **BCR (RWF-only)** | **372.3x** | **606.4x** |
| **BCR (Full/Total)** | **14.3x** | **23.0x** |

### 4.2 All Scenarios (Full/Total cost BCR)

| Scenario     | RTE BCR (Full) | Apprenticeship BCR (Full) |
|-------------|----------------|--------------------------|
| Conservative | 5.5x           | 8.0x                     |
| Moderate     | 14.3x          | 23.0x                    |
| Optimistic   | 42.4x          | 65.0x                    |

For the persistence analysis, we use the **Full/Total BCR** as the per-cohort baseline, because this represents the full societal cost-effectiveness. The RWF-only BCR (funder ROI metric) scales by the same multiplier.

---

## 5. Worked Example: Moderate Scenario, RTE Intervention

**Parameters:**
- T = 10 years post-exit
- alpha = 0.40 (40% attribution)
- delta = 0.03 (3% annual decay)
- BCR_cohort (RTE, Full, Moderate) = 14.3x

**Step 1: Calculate cumulative multiplier M(10)**

Using the closed-form formula:

```
M(10) = 1 + 0.40 * (1 - 0.03) * [1 - (1 - 0.03)^10] / 0.03
       = 1 + 0.40 * 0.97 * [1 - 0.97^10] / 0.03
       = 1 + 0.388 * [1 - 0.7374] / 0.03
       = 1 + 0.388 * 0.2626 / 0.03
       = 1 + 0.388 * 8.7536
       = 1 + 3.3964
       = 4.40
```

**Verification by explicit summation:**

| Year (t) | (1-delta)^t | alpha * (1-delta)^t | Cumulative M(t) |
|-----------|------------|---------------------|-----------------|
| 0 (original cohort) | -- | 1.000 (baseline) | 1.000 |
| 1 | 0.9700 | 0.3880 | 1.388 |
| 2 | 0.9409 | 0.3764 | 1.764 |
| 3 | 0.9127 | 0.3651 | 2.129 |
| 4 | 0.8853 | 0.3541 | 2.484 |
| 5 | 0.8587 | 0.3435 | 2.827 |
| 6 | 0.8330 | 0.3332 | 3.160 |
| 7 | 0.8080 | 0.3232 | 3.484 |
| 8 | 0.7837 | 0.3135 | 3.797 |
| 9 | 0.7602 | 0.3041 | 4.101 |
| 10 | 0.7374 | 0.2950 | 4.396 |

**M(10) = 4.40** (matches closed-form result)

**Step 2: Calculate effective BCR**

```
BCR_effective = 14.3 * 4.40 = 62.9x
```

**Interpretation:** If RTE policy persists for 10 years after RWF exits, and RWF can claim 40% attribution for the continuing program (with 3% annual quality decay), the effective program BCR is approximately 63x -- roughly 4.4 times the single-cohort BCR of 14.3x.

**Step 3: Total beneficiary impact (illustrative)**

Over 10 years post-exit at [ASSUMED] 5,000 RTE beneficiaries/year:
- Additional beneficiaries reached: 50,000
- Attribution-weighted equivalent beneficiaries: SUM_{t=1}^{10} [5,000 * 0.40 * 0.97^t] = 16,982
- Combined with original cohort (5,000): approximately 21,982 full-equivalent beneficiaries

---

## 6. Scenario Matrix

### 6.1 Cumulative Multipliers

| Scenario     | T (years) | alpha | delta | **M(T)** |
|-------------|-----------|-------|-------|----------|
| Conservative | 5         | 0.20  | 0.05  | **1.86** |
| Moderate     | 10        | 0.40  | 0.03  | **4.40** |
| Optimistic   | 15        | 0.60  | 0.01  | **9.31** |

### 6.2 Effective BCR: RTE Intervention (Full/Total Cost)

| Scenario     | Per-Cohort BCR | Multiplier M(T) | **Effective BCR** |
|-------------|---------------|-----------------|-------------------|
| Conservative | 5.5x          | 1.86            | **10.2x**         |
| Moderate     | 14.3x         | 4.40            | **62.9x**         |
| Optimistic   | 42.4x         | 9.31            | **395.0x**        |

### 6.3 Effective BCR: Apprenticeship Intervention (Full/Total Cost)

| Scenario     | Per-Cohort BCR | Multiplier M(T) | **Effective BCR** |
|-------------|---------------|-----------------|-------------------|
| Conservative | 8.0x          | 1.86            | **14.8x**         |
| Moderate     | 23.0x         | 4.40            | **100.9x**        |
| Optimistic   | 65.0x         | 9.31            | **605.5x**        |

### 6.4 Effective BCR: RWF-Only Cost Perspective

For the funder ROI perspective (RWF direct costs only):

**RTE (RWF cost = INR 4,000/beneficiary):**

| Scenario     | Per-Cohort BCR | Multiplier | **Effective BCR** |
|-------------|---------------|------------|-------------------|
| Conservative | 143.3x        | 1.86       | **266.4x**        |
| Moderate     | 372.3x        | 4.40       | **1,637.5x**      |
| Optimistic   | 1,102.9x      | 9.31       | **10,268.0x**     |

**Apprenticeship (RWF cost = INR 6,000/beneficiary):**

| Scenario     | Per-Cohort BCR | Multiplier | **Effective BCR** |
|-------------|---------------|------------|-------------------|
| Conservative | 210.8x        | 1.86       | **391.7x**        |
| Moderate     | 606.4x        | 4.40       | **2,668.3x**      |
| Optimistic   | 1,717.1x      | 9.31       | **15,986.3x**     |

---

## 7. Interpreting the Multipliers

### 7.1 What the multiplier means

A multiplier of M(T) = 4.40 means that if the policy persists for 10 years post-exit with moderate attribution and decay assumptions, the **total program value is 4.4 times the single-cohort value**. The original cohort accounts for only 23% of the total impact; the remaining 77% comes from continuing policy effects.

### 7.2 Sensitivity of the multiplier

The multiplier is most sensitive to:

1. **Attribution fraction (alpha):** This is the most subjective parameter. Doubling alpha from 0.20 to 0.40 roughly doubles the persistence contribution (the non-baseline portion of M).

2. **Persistence length (T):** Longer persistence increases the multiplier, but with diminishing returns due to decay. The marginal value of an additional year declines as (1-delta)^t shrinks.

3. **Decay rate (delta):** Higher decay reduces the multiplier more aggressively. At 5%/yr decay, intensity drops to 77% by year 5. At 1%/yr decay, intensity is still 86% at year 15.

### 7.3 Combined beneficiary impact

Using [ASSUMED] annual volumes (RTE: 5,000; Apprenticeship: 3,000):

| Scenario     | RTE Post-Exit Cohorts | App Post-Exit Cohorts | RTE Equiv. Beneficiaries | App Equiv. Beneficiaries |
|-------------|----------------------|----------------------|--------------------------|--------------------------|
| Conservative | 25,000 over 5 yrs    | 15,000 over 5 yrs   | 4,335                    | 2,601                    |
| Moderate     | 50,000 over 10 yrs   | 30,000 over 10 yrs  | 16,982                   | 10,189                   |
| Optimistic   | 75,000 over 15 yrs   | 45,000 over 15 yrs  | 49,920                   | 29,952                   |

*Attribution-weighted equivalent = N * SUM_{t=1}^{T} [alpha * (1-delta)^t], representing the effective number of full-benefit-equivalent beneficiaries from post-exit cohorts.*

---

## 8. Caveats and Limitations

### 8.1 Attribution fractions are illustrative

The 20% / 40% / 60% attribution fractions have **no empirical basis**. They are round numbers chosen to bracket a plausible range. Rigorous attribution would require:

- Counterfactual analysis: what would have happened without RWF?
- Process tracing: which specific institutional capacities did RWF build?
- Comparable case studies: how do similar programs evolve post-funder-exit?

### 8.2 Constant beneficiary volume assumption

The model assumes the same number of beneficiaries each year. In practice:
- Volume may **increase** if government scales up the program
- Volume may **decrease** if program quality or targeting deteriorates without RWF support
- Volume and quality may be correlated (worse targeting = more beneficiaries but lower per-capita impact)

### 8.3 Decay function is assumed exponential

The 5%/3%/1% decay rates are illustrative. Real program decay may be:
- **Non-linear:** quality could be stable for years then drop sharply (cliff decay)
- **Domain-specific:** policy advocacy effects may decay differently from service delivery effects
- **Context-dependent:** state-level governance quality affects decay rates

### 8.4 BCR compounding assumption

The analysis assumes each post-exit cohort generates the same per-capita LNPV as the original (reduced only by the intensity decay factor). This ignores:
- Changes in economic conditions (wage levels, formality rates) over time
- Policy environment changes (new regulations, competing programs)
- Selection effects (later cohorts may differ systematically from early cohorts)

### 8.5 Data needs for improvement

To move from illustrative to evidence-based multipliers, RWF would need:

| Data Point | Purpose | Priority |
|-----------|---------|----------|
| Actual annual beneficiary volumes | Replace [ASSUMED] values | High |
| Tracer study retention rates | Calibrate decay parameter | High |
| Government budget commitments | Assess persistence likelihood | Medium |
| Comparable program exit evaluations | Benchmark attribution fractions | Medium |
| Longitudinal quality metrics | Validate decay function shape | Low |

---

## 9. Chart Data Reference

The companion file `persistence_chart_data.csv` contains year-by-year data points for all three scenarios, suitable for visualization:

- **Line chart:** Cumulative multiplier M(t) vs. year, one line per scenario
- **Area chart:** Incremental BCR contribution per year, stacked by scenario
- **Bar chart:** Final effective BCR by scenario and intervention

Columns in CSV:
- `year`: Years after RWF exit (0 = original cohort, 1..15 = post-exit years)
- `scenario`: conservative / moderate / optimistic
- `attribution_fraction`: alpha for that scenario
- `intensity_factor`: (1 - delta)^t for that year and scenario
- `cumulative_multiplier`: M(t) up to and including that year
- `effective_bcr_rte`: BCR_cohort_rte * M(t) using Full/Total cost
- `effective_bcr_apprenticeship`: BCR_cohort_app * M(t) using Full/Total cost

---

## 10. Summary

Policy persistence is a powerful lever for program valuation. Even under the conservative scenario (5 years, 20% attribution, 5% decay), the cumulative multiplier is 1.86x -- nearly doubling the single-cohort BCR. Under moderate assumptions, the multiplier reaches 4.40x, and under optimistic assumptions, 9.31x.

However, these multipliers rest on illustrative attribution fractions that have no empirical grounding. The analysis demonstrates the *structure* of how persistence compounds program value, not the *magnitude*. Rigorous attribution analysis and tracer study data would be needed to move from illustrative to evidence-based multipliers.

**Key takeaway:** The single-cohort BCR is a conservative floor. If RWF's policy work creates lasting institutional change, the true program value is substantially higher. The challenge is credibly estimating *how much* higher.
