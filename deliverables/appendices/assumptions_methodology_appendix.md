# Assumptions & Methodology Appendix

## RightWalk Foundation -- Lifetime Economic Benefits Estimation Model

---

**Document version**: 1.0
**Date**: February 16, 2026
**Source of truth**: `model/parameter_registry_v3.py` v3.5; `model/economic_core_v4.py` v4.4
**Input dependencies**: Task #9 (`parameter_evidence_table.md`), Task #8 (`policy_persistence_scenarios.md`)

---

## 1. Model Overview

This model estimates the **Lifetime Net Present Value (LNPV)** of two RightWalk Foundation interventions -- RTE 25% quota access (private schooling for EWS children) and National Apprenticeship Training Scheme (NATS) placement -- by comparing discounted lifetime earnings trajectories of beneficiaries against counterfactual scenarios. It produces LNPV estimates for 32 demographic scenarios (2 interventions × 4 regions × 2 genders × 2 locations), 3 scenario configurations (Conservative / Moderate / Optimistic), and dual Benefit-Cost Ratios (RWF-only and Full investment perspectives).

---

## 2. Core Formulas

### 2.1 Lifetime Net Present Value (LNPV)

```
LNPV = Σ[t=0 to T] (E[W_treatment(t)] - E[W_control(t)]) / (1 + δ)^t
```

Where:
- T = 40 years (career horizon, ages ~18-58)
- δ = 5% (social discount rate, real terms)
- E[W_treatment(t)] = expected annual earnings for beneficiary at year t
- E[W_control(t)] = expected annual earnings for counterfactual individual at year t
- All values in constant 2025 INR (real terms, no inflation adjustment needed)

### 2.2 Expected Earnings at Year t

```
E[W(t)] = P_formal × W_formal(t) + (1 - P_formal) × W_informal(t)
```

Where:
- P_formal = probability of formal sector employment (intervention-specific)
- W_formal(t) = formal sector wage at year t
- W_informal(t) = informal sector wage at year t

### 2.3 Wage Trajectory (Formal Sector)

```
W_formal(t) = W₀_formal × exp(β₂_f × t) × (1 + g_formal)^t × (1 + Δ_mincer)
```

Where:
- W₀_formal = PLFS 2023-24 baseline formal wage (demographic-specific)
- β₂_f = 0.027 (2.7%/yr formal experience premium, Chen et al. 2022)
- g_formal = 0.015 (1.5%/yr real wage growth, formal sector)
- Δ_mincer = Mincer wage premium from additional schooling (RTE only)

### 2.4 Wage Trajectory (Informal Sector)

```
W_informal(t) = W₀_informal × exp(β₂_i × t) × (1 + g_informal)^t
```

Where:
- W₀_informal = PLFS 2023-24 baseline informal wage (demographic-specific)
- β₂_i = 0.012 (1.2%/yr informal experience premium, Chen et al. 2022)
- g_informal = -0.002 (-0.2%/yr real wage growth, informal sector)

### 2.5 Mincer Wage Equation (RTE Test Score Chain)

```
Δ_mincer = exp(β₁ × ΔS) - 1

Where:
  ΔS = Δ_RTE × (years/SD)
     = 0.137 SD × 6.8 years/SD
     = 0.93 equivalent years of schooling

  β₁ = 0.058 (5.8% return per year, Chen et al. 2022)

  Δ_mincer = exp(0.058 × 0.93) - 1 = 5.5% wage premium
```

### 2.6 Apprenticeship Premium Decay

```
π(t) = π₀ × exp(-λt)

Where:
  π₀ = Rs 84,000/year (initial annual premium)
  λ = ln(2) / h (decay rate)
  h = 10 years (half-life, baseline)
```

### 2.7 Benefit-Cost Ratio (Dual Framework)

```
BCR_RWF = LNPV / C_RWF        (RWF-only perspective)
BCR_Full = LNPV / C_Total      (Full investment perspective)
```

---

## 3. Full Parameter Table

### 3.1 Tier 1 Parameters (Critical -- Highest Uncertainty, Largest Impact)

| # | Parameter | Symbol | Value | Range | Unit | Source | Confidence | Tracer? |
|:--|:----------|:-------|:------|:------|:-----|:-------|:-----------|:--------|
| 1 | Formal Sector Entry -- RTE | P(F\|RTE) | 0.30 | 0.20--0.50 | probability | RWF/Anand guidance (Dec 2025) | **LOW** | `[PENDING TRACER UPDATE]` |
| 2 | Formal Sector Placement -- Apprenticeship | P(F\|App) | 0.68 | 0.50--0.90 | probability | RWF operational data (Nov 2025) | **HIGH** | `[PENDING TRACER UPDATE]` |
| 3 | Formal Sector Entry -- No Training | P(F\|NoTrain) | 0.10 | 0.05--0.15 | probability | ILO India 2024 / PLFS | **MODERATE** | `[PENDING TRACER UPDATE]` |
| 4 | Formal Sector Entry -- Higher Secondary | P(F\|HS) | 0.091 | 0.05--0.15 | probability | ILO India 2024 | **MODERATE** | -- |
| 5 | Apprentice Decay Half-Life | h | 10 | 5--50 | years | Assumed (no India data) | **LOW** | `[PENDING TRACER UPDATE]` |
| 6 | RTE Test Score Gain | Δ_RTE | 0.137 | 0.10--0.20 | SD (ITT) | Muralidharan & Sundararaman (2013) | **LOW-MODERATE** | -- |
| 7 | RTE Retention Funnel | P_retain | 0.60 | 0.50--0.75 | proportion | UDISE+ proxy (no RTE data) | **LOW** | `[PENDING TRACER UPDATE]` |
| 8 | Apprentice Completion Rate | P_complete | 0.85 | 0.75--0.95 | proportion | MSDE estimate | **LOW** | `[PENDING TRACER UPDATE]` |

### 3.2 Tier 2 Parameters (Moderate Uncertainty)

| # | Parameter | Symbol | Value | Range | Unit | Source | Confidence |
|:--|:----------|:-------|:------|:------|:-----|:-------|:-----------|
| 9 | Social Discount Rate | δ | 5% | 3%--8% | %/year | Murty & Panda (2020) Ramsey | **MODERATE** |
| 10 | Mincer Return (Higher Secondary) | β₁ | 5.8% | 5%--8% | %/year schooling | Chen et al. (2022), PLFS 2018-19 | **MODERATE** |
| 11 | Experience Premium -- Formal | β₂_f | 2.7% | 2.0%--3.5% | %/year experience | Chen et al. (2022), PLFS 2018-19 | **MODERATE** |
| 12 | Experience Premium -- Informal | β₂_i | 1.2% | 0.5%--1.8% | %/year experience | Chen et al. (2022), PLFS 2018-19 | **MODERATE** |
| 13 | Real Wage Growth -- Formal | g_formal | 1.5% | 0.5%--2.5% | %/year | PLFS 2020-24 trends | **MODERATE** |
| 14 | Real Wage Growth -- Informal | g_informal | -0.2% | -1.0%--0.5% | %/year | PLFS 2020-24 trends | **MODERATE** |
| 15 | Test Score to Years Conversion | years/SD | 6.8 | 4.0--8.0 | years/SD | Angrist & Evans (2020) | **LOW** |
| 16 | Apprentice Initial Wage Premium | π₀ | Rs 84,000 | 50k--110k | INR/year | PLFS 2023-24 derived | **MODERATE** |
| 17 | RTE Cost (Full) | C_RTE_Total | Rs 1,04,000 | 90k--120k | INR/beneficiary | RWF + govt reimbursement | **MODERATE** |
| 18 | Apprentice Cost (Full) | C_App_Total | Rs 1,58,460 | 140k--180k | INR/beneficiary | RWF + govt + employer | **MODERATE** |

### 3.3 Tier 3 Parameters (Well-Established, Low Uncertainty)

| # | Parameter | Symbol | Value | Unit | Source |
|:--|:----------|:-------|:------|:-----|:-------|
| 19 | Career Horizon | T | 40 years | years | Standard (ages 18-58) |
| 20 | Labor Market Entry Age | age₀ | 22 | years | Post-HS assumption |
| 21 | RTE Cost (RWF-only) | C_RTE_RWF | Rs 4,000 | INR/beneficiary | RWF operational data |
| 22 | Apprentice Cost (RWF-only) | C_App_RWF | Rs 6,000 | INR/beneficiary | RWF operational data |
| 23 | Apprentice Stipend | S_app | Rs 7,000/mo | INR/month | Gazette 2019 |
| 24 | RTE Seat Fill Rate | P_fill | 29% | proportion | CAG Audit 2014 |

### 3.4 Baseline Wages (PLFS 2023-24 -- Fixed, Not Varied in Monte Carlo)

| Demographic | Formal (HS, monthly) | Informal (casual, monthly) | Embedded Ratio |
|:------------|:---------------------|:---------------------------|:---------------|
| Urban Male | Rs 32,800 | Rs 13,425 | 2.44× |
| Urban Female | Rs 24,928 | Rs 9,129 | 2.73× |
| Rural Male | Rs 22,880 | Rs 11,100 | 2.06× |
| Rural Female | Rs 15,558 | Rs 7,475 | 2.08× |

*Source: PLFS 2023-24 Table 21 (formal wages calculated from secondary wages using 5.8% Mincer return for 2 additional years).*

---

## 4. Scenario Framework

Three scenarios defined in `parameter_registry_v3.py` Section 9B. Moderate scenario uses registry defaults (no overrides).

### 4.1 Parameter Values by Scenario

| Parameter | Conservative | Moderate | Optimistic |
|:----------|:-------------|:---------|:-----------|
| P_FORMAL_APPRENTICE | 50% | 68% (RWF data) | 90% |
| P_FORMAL_HIGHER_SECONDARY (control) | 5% | 9.1% (ILO 2024) | 15% |
| P_FORMAL_RTE | 20% | 30% | 50% |
| FORMAL_MULTIPLIER | 2.24× | 2.25× | 2.48× |
| APPRENTICE_INITIAL_PREMIUM | Rs 50,000 | Rs 84,000 | Rs 120,000 |
| RTE_TEST_SCORE_GAIN | 0.10 SD | 0.137 SD | 0.20 SD |
| APPRENTICE_DECAY_HALFLIFE | 5 years | 10 years | 50 years |
| REAL_WAGE_GROWTH_FORMAL | 0.5% | 1.5% | 2.5% |
| REAL_WAGE_GROWTH_INFORMAL | -1.0% | -0.2% | 0.5% |
| SOCIAL_DISCOUNT_RATE | 8% | 5% | 3% |

### 4.2 Scenario Rationale

- **Conservative**: Worst-case labor markets (Bihar-like formal rates), high discount rate, rapid skill decay, minimal test score gains. Designed to establish a credible floor.
- **Moderate**: Registry defaults calibrated to national averages (PLFS 2023-24, ILO 2024). P_FORMAL_APPRENTICE from RWF's own data (68%). The "best estimate" for decision-making.
- **Optimistic**: Best-case conditions (urban Bangalore-like formal rates), low discount rate, persistent skills, high test score compliance. Upper bound for what the program *could* deliver.

---

## 5. Top 5 Sensitivity Drivers

Ranked by NPV elasticity from one-at-a-time (OAT) tornado analysis (Feb 16, 2026 re-run).

### 5.1 RTE Intervention

| Rank | Parameter | Elasticity | NPV Swing | What Happens at Bounds |
|:-----|:----------|:-----------|:----------|:-----------------------|
| 1 | P_FORMAL_RTE | **1.11** | 111.3% | At 20%: NPV drops ~55%. At 50%: NPV rises ~74%. |
| 2 | SOCIAL_DISCOUNT_RATE | **0.89** | 86.2% | At 3%: NPV nearly doubles. At 8%: NPV drops ~45%. |
| 3 | REAL_WAGE_GROWTH_FORMAL | **0.59** | 40.3% | At 0.5%: NPV drops ~20%. At 2.5%: NPV rises ~20%. |
| 4 | EXPERIENCE_LINEAR_FORMAL | **0.59** | 31.0% | At 2.0%: NPV drops ~15%. At 3.5%: NPV rises ~16%. |
| 5 | MINCER_RETURN_HS | **0.23** | 12.1% | At 5%: NPV drops ~6%. At 8%: NPV rises ~6%. |

**Key insight**: 79% of RTE NPV comes from the Placement Effect (P_FORMAL differential), not the Mincer Effect (test scores). P_FORMAL_RTE is the single parameter on which the RTE business case stands or falls.

### 5.2 Apprenticeship Intervention

| Rank | Parameter | Elasticity | NPV Swing | What Happens at Bounds |
|:-----|:----------|:-----------|:----------|:-----------------------|
| 1 | SOCIAL_DISCOUNT_RATE | **0.89** | 88.7% | At 3%: NPV nearly doubles. At 8%: NPV drops ~45%. |
| 2 | P_FORMAL_APPRENTICE | **1.05** | 58.3% | At 50%: NPV drops ~30%. At 90%: NPV rises ~25%. |
| 3 | REAL_WAGE_GROWTH_FORMAL | **0.59** | 43.0% | At 0.5%: NPV drops ~22%. At 2.5%: NPV rises ~21%. |
| 4 | EXPERIENCE_LINEAR_FORMAL | **0.59** | 33.0% | At 2.0%: NPV drops ~17%. At 3.5%: NPV rises ~16%. |
| 5 | APPRENTICE_DECAY_HALFLIFE | **0.05** | 23.9% | At 5yr: NPV drops ~56%. At 50yr: NPV rises ~175%. |

**Key insight**: The apprenticeship model is more balanced across drivers. The discount rate and P_FORMAL_APPRENTICE together account for ~70% of total NPV variance.

---

## 6. Data Sources

### 6.1 Primary Data

| Source | What It Was Used For |
|:-------|:---------------------|
| PLFS 2023-24 (MOSPI) | Baseline wages (formal/informal), employment distributions, age-earnings profiles |
| ILO India Employment Report 2024 | Formal sector entry rates by education, youth unemployment, sectoral composition |
| RWF Operational Data (Nov 2025) | P_FORMAL_APPRENTICE (68%), program costs, beneficiary counts |
| MSDE Annual Report 2023-24 | Apprentice completion rates, NATS enrollment, trade distributions |
| CAG Audit Report on RTE (2014) | RTE seat fill rate (29%) |

### 6.2 Academic Literature

| Source | What It Was Used For |
|:-------|:---------------------|
| Chen, Kanjilal-Bhaduri & Pastore (2022) | Mincer returns (5.8%), sector-specific experience premiums (formal 2.7%, informal 1.2%) |
| Muralidharan & Sundararaman (2013) | RTE test score gain (0.137 SD ITT, NBER w19441 RCT) |
| Angrist & Evans (2020) | Test score to years conversion (6.8 years/SD, micro-LAYS methodology) |
| Murty & Panda (2020) | Social discount rate (Ramsey formula for India: 5-8.5%) |
| Mitra (2019) | Mincer return range validation (5-9% quantile range) |
| Attanasio, Guarín et al. (2017) | Vocational training premium persistence (Colombia, 15+ year follow-up) |
| Card, Kluve & Weber (2018) | Meta-analysis of ALMP effects (207 studies, treatment persistence) |
| DGT/MSDE National Tracer Study (2024) | ITI graduate employment outcomes (n=11,136) |

---

## 7. Limitations

### 7.1 What the Model Does NOT Capture

| Excluded Effect | Likely Direction | Magnitude Estimate |
|:----------------|:-----------------|:-------------------|
| Health benefits (ESI access for formal workers) | Positive | 5-15% additional value |
| Intergenerational effects (children of beneficiaries) | Positive | Unknown but potentially large |
| Tax revenue from formalized workers | Positive | 10-15% of wage premium |
| Social security (EPF accumulation) | Positive | 8-12% of formal wages |
| Non-market benefits (civic participation, reduced crime) | Positive | Unquantified |
| General equilibrium effects (program scale affects wages) | Negative at scale | 0-5% dampening |
| Selection bias (motivated beneficiaries vs. general population) | Upward bias | 20-40% overstatement |

### 7.2 Key Assumptions Without Empirical Backing

| Assumption | Current Basis | Risk | Tracer Can Address? |
|:-----------|:-------------|:-----|:--------------------|
| P_FORMAL_RTE = 30% | Expert judgment only | **CRITICAL** -- #1 driver, zero data | Yes -- primary tracer target |
| Half-life h = 10 years | International proxy | Moderate -- no India longitudinal data | Partially (cross-cohort design) |
| RTE retention = 60% | Private school proxy | Moderate -- no RTE-specific tracking | Yes -- retrospective education data |
| Constant labor market structure over 40 years | Assumed | Moderate -- structural change likely | No -- inherent limitation |
| No sector transitions (absorbing states) | Simplification | Low-moderate -- some workers do transition | Partially (employment history) |
| Selection on observables only | Assumed | **HIGH** -- 20-40% potential overstatement | Partially (PSM with richer controls) |

### 7.3 Honest Uncertainty Statement

> Of the 12 highest-impact parameters, only **1 has HIGH confidence** (P_FORMAL_APPRENTICE, from RWF's own data). Three parameters rated LOW collectively drive the majority of RTE NPV variance. The model provides a structured framework for thinking about lifetime economic benefits, but the point estimates should be interpreted alongside the wide sensitivity ranges. The recommended tracer study would reduce uncertainty in the top 4 parameters by providing RWF-specific empirical data.

---

*Document created: February 16, 2026*
*Parameter registry version: v3.5 (Feb 16, 2026)*
*Sensitivity analysis: OAT tornado run, Feb 16, 2026*
*Cross-references: parameter_evidence_table.md, policy_persistence_scenarios.md, METHODOLOGY.md*
