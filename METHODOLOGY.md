# Methodology: Estimating Lifetime Economic Benefits

This document describes the economic framework, causal mechanisms, and modeling approach used to estimate lifetime earnings benefits of RightWalk Foundation interventions.

---

## 1. Model Framework

### Lifetime Net Present Value (LNPV)

We employ a **Difference-in-Differences Net Present Value** framework that compares the discounted lifetime earnings of beneficiaries against a counterfactual scenario:

```
LNPV = Σ[t=0 to T] (W_treatment(t) - W_control(t)) / (1 + δ)^t
```

Where:
- `T = 40 years` - Career horizon (ages 18-58)
- `δ = 5%` - Social discount rate
- `W_treatment(t)` - Expected wage for intervention beneficiary at year t
- `W_control(t)` - Expected wage for counterfactual individual at year t

### Wage Trajectory Components

Wage at time t is determined by:

1. **Base wage** - Entry-level wage based on education and sector
2. **Sector** - Formal (Rs 30,000/month) vs. Informal (Rs 13,333/month)
3. **Sector growth rates** - Formal: +1.5%/year real; Informal: -0.2%/year real
4. **Experience returns** - Mincer equation with experience premium
5. **Treatment effects** - Intervention-specific wage premiums (decaying for Apprenticeship)

---

## 2. Intervention-Specific Mechanisms

### 2.1 RTE Intervention (Private School Access)

**Target Population:** Economically Weaker Section (EWS) children enrolled in private schools via RTE 25% reservation quota.

**Causal Pathway:**

```
Private School → Test Score Gains → Educational Credentials → Formal Sector Entry → Wage Premium
     (1)              (2)                   (3)                    (4)              (5)
```

| Stage | Mechanism | Evidence |
|-------|-----------|----------|
| (1) Private School Attendance | RTE 25% quota provides access | Policy mechanism |
| (2) Test Score Gains | +0.137 SD (ITT estimate) | Muralidharan & Sundararaman 2013 |
| (3) Educational Credentials | Higher completion rates | UDISE+ data |
| (4) Formal Sector Entry | 30% vs. 9.1% baseline | RWF guidance + ILO 2024 |
| (5) Wage Premium | Mincer returns (7%/year) | Mitra 2019 |

**Key Parameters:**

| Parameter | Value | Source |
|-----------|-------|--------|
| Test score gain | 0.137 SD | NBER RCT (ITT estimate) |
| SD to years conversion | 6.8 | Angrist & Evans 2020 |
| Mincer return | 7.0% | Mitra 2019 via Chen et al. 2022 |
| P(Formal | RTE) | 30% | RWF guidance |
| P(Formal | Control) | 9.1% | ILO India 2024 |

**Counterfactual (Control Group):**

Without RTE intervention, EWS children would face:
- 70%+ enrollment in government schools
- 9.1% probability of formal sector employment
- Baseline education returns in informal sector

**RTE Decomposition:**

Total LNPV decomposes into two effects:

```
Total NPV = Placement Effect + Mincer Effect

Placement Effect (~79%): NPV(P_FORMAL=30%) - NPV(P_FORMAL=9.1%) | test_gain=0
Mincer Effect (~21%): NPV(test_gain=0.137) - NPV(test_gain=0) | same P_FORMAL
```

**Interpretation:** The primary value of RTE is as a **pathway to formal employment** (79%), not just improved learning outcomes (21%). This suggests RTE programs should consider career guidance and placement support.

---

### 2.2 Apprenticeship Intervention (NATS)

**Target Population:** Youth enrolled in National Apprenticeship Training Scheme, receiving structured on-the-job training with National Apprenticeship Certificate (NAC).

**Causal Pathway:**

```
Apprenticeship → Skill Certification → Employer Absorption → Formal Wages → Sustained Premium
      (1)              (2)                   (3)               (4)              (5)
```

| Stage | Mechanism | Evidence |
|-------|-----------|----------|
| (1) Program Enrollment | Application and selection | MSDE data |
| (2) NAC Certification | 85% completion rate | MSDE Annual Report |
| (3) Employer Absorption | 72% placement rate | RWF program data |
| (4) Formal Wages | 2.25× informal wage | ILO 2024 |
| (5) Premium Persistence | Half-life 10 years | Assumed (sensitivity tested) |

**Key Parameters:**

| Parameter | Value | Source |
|-----------|-------|--------|
| Completion rate | 85% | MSDE Annual Report 2023-24 |
| Placement rate (formal) | 72% | RWF program data |
| Initial wage premium | Rs 84,000/year | Calculated |
| Premium half-life | 10 years | Assumed (range: 5-50) |
| P(Formal | No Training) | 10% | PLFS derived |

**Counterfactual (Control Group):**

Without apprenticeship, youth entering labor market directly face:
- 10-17% unemployment rate
- 90%+ informal sector employment
- Low, stagnant wages (Rs 400-500/day casual)
- No social security benefits

**Treatment Effect Decay:**

The apprenticeship wage premium decays exponentially:

```
π(t) = π₀ × exp(-λt)

Where:
- π₀ = Rs 84,000 (initial annual premium)
- λ = ln(2) / h (decay rate)
- h = 10 years (half-life)
```

At t=10 years, premium has declined to 50% of initial value.
At t=20 years, premium has declined to 25% of initial value.

---

## 3. Mincer Wage Equation

Wages follow the standard Mincerian specification:

```
ln(W) = β₀ + β₁×S + β₂×Exp + β₃×Exp²
```

| Parameter | Value | Interpretation |
|-----------|-------|---------------|
| β₁ | 7.0% | Return per year of schooling |
| β₂ | 0.885% | Linear experience return |
| β₃ | -0.0123% | Experience squared (diminishing returns) |

**Important:** Returns to education are **concentrated in formal sector employment**. In the informal sector (90%+ of workforce), returns to education are near-zero. This creates a stark bifurcation:

- **Formal sector:** Education → Higher wages (8.6%/year)
- **Informal sector:** Education → Minimal wage gains

This is why **P(Formal)** is the critical mediating variable for both interventions.

---

## 4. Formal vs. Informal Sector Dynamics

### Sector Characteristics

| Characteristic | Formal Sector | Informal Sector |
|----------------|---------------|-----------------|
| Share of workforce | ~10% | ~90% |
| Entry wage | Rs 30,000/month | Rs 13,333/month |
| Wage multiplier | 2.25× | 1.0× (baseline) |
| Real wage growth | +1.5%/year | -0.2%/year |
| Social security | Yes | No |
| Job stability | Higher | Lower |

### Compounding Effect

The divergent growth rates create **compounding lifetime effects**:

```
Year 0:  Formal = 2.25× Informal
Year 20: Formal = 3.0× Informal
Year 40: Formal = 4.0× Informal
```

This explains why **formal sector entry** is the #1 driver of LNPV, more important than initial wage levels.

---

## 5. Regional Adjustments

The model accounts for regional labor market heterogeneity across four macro-regions:

| Region | States | Formal Sector Share | Wage Multiplier |
|--------|--------|--------------------:|----------------:|
| **South** | TN, KA, AP, TG, KL | Highest | 1.15× |
| **West** | MH, GJ, MP, CG, GA | High | 1.10× |
| **North** | DL, HR, PB, UP, RJ | Medium | 1.00× |
| **East** | WB, BR, JH, OD, NE | Lowest | 0.90× |

Regional P_FORMAL multipliers for RTE:

| Region | P_FORMAL_RTE |
|--------|-------------:|
| South | 41.7% |
| West | 33.3% |
| North | 25.0% |
| East | 20.0% |

---

## 6. Demographic Subgroups

Each scenario is computed for four demographic subgroups:

| Subgroup | Code | Notes |
|----------|------|-------|
| Urban Male | UM | Highest baseline wages |
| Urban Female | UF | Lower LFPR, similar wage levels |
| Rural Male | RM | Lower wages, less formal sector access |
| Rural Female | RF | Lowest wages, lowest formal sector access |

---

## 7. Sensitivity Analysis Framework

### One-Way (Tornado) Analysis

Each parameter varied from low to high bound while holding others at baseline:

```
ΔLNPV = LNPV(param=high) - LNPV(param=low)
```

Parameters ranked by |ΔLNPV| to identify key drivers.

### Two-Way Analysis

Selected parameter pairs varied jointly to identify interactions:
- P_FORMAL × Test Score Gain (RTE)
- P_FORMAL × Half-Life (Apprenticeship)
- Discount Rate × Mincer Return

### Monte Carlo Simulation

10,000 iterations with parameters drawn from distributions:

- **Tier 1 parameters:** Uniform distribution over [low, high]
- **Tier 2 parameters:** Triangular distribution (mode = baseline)

Outputs: Mean, median, 5th/95th percentiles, P(positive)

### Break-Even Analysis

Maximum allowable cost per beneficiary at target BCR:

```
Max_Cost = LNPV / Target_BCR
```

Computed for BCR = 1:1, 2:1, 3:1 across all 32 scenarios.

---

## 8. Key Assumptions & Limitations

### Maintained Assumptions

1. **Selection-on-observables:** Treatment and control groups differ only in program participation. Selection effects could inflate estimates by 20-40%.

2. **Stable labor markets:** Wage trajectories based on 2023-24 PLFS data persist over 40-year horizon.

3. **No general equilibrium effects:** Programs don't affect overall wage levels or formal sector employment rates.

4. **Linear Mincer returns:** Returns to schooling constant across education levels and time.

### Key Limitations

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| No causal identification | May overstate effects | Wide sensitivity ranges |
| Macro-regional aggregation | Misses state/district variation | Regional multipliers |
| Assumed half-life (h) | Uncertain for apprenticeship | Sensitivity from 5-50 years |
| Population averages | Not RWF-specific | Recommend tracer study |
| Cross-sectional wage data | No longitudinal validation | PLFS trend analysis |

---

## 9. Data Sources

### Primary Sources

| Category | Sources |
|----------|---------|
| **Wages & Employment** | PLFS 2023-24, ILO India Employment Report 2024 |
| **Education Outcomes** | ASER Centre, NAS, UDISE+, NFHS-5 |
| **Apprenticeship** | MSDE Annual Reports, DGT Tracer Studies, NAPS data |
| **Macroeconomic** | RBI CPI, World Bank Discount Rate studies |

### Academic Literature

| Topic | Key References |
|-------|----------------|
| Private school effects | Muralidharan & Sundararaman 2013 (NBER RCT) |
| Mincer returns (India) | Mitra 2019, Chen et al. 2022, Duraisamy 2002 |
| Formal/informal wage gap | Sharma & Sasikumar 2018, ILO 2024 |
| Test-to-years conversion | Angrist & Evans 2020 |

---

## 10. Model Validation

### Internal Consistency Checks

1. **Age-wage profiles:** Match empirical PLFS patterns (formal: peak ~60; informal: peak ~50)
2. **NPV ordering:** South > West > North > East (matches economic development)
3. **Decomposition:** Placement + Mincer = Total (verified to 0.00% error)

### External Benchmarks

| Benchmark | Literature | Our Model |
|-----------|------------|-----------|
| Secondary education BCR | 5:1 - 10:1 | RTE: 3:1 - 8:1 |
| Vocational training BCR | 2:1 - 6:1 | Apprenticeship: 4:1 - 12:1 |
| Formal/informal gap | 2-3× | 2.25× baseline |

---

## 11. Recommended Extensions

### Priority 1: Longitudinal Tracer Study

Track 200-300 beneficiaries for 1-2 years to:
- Validate P_FORMAL assumptions
- Measure actual wage trajectories
- Estimate treatment persistence (h)

**Impact:** Reduce uncertainty by 50%+, convert PoC to causal evaluation

### Priority 2: Propensity Score Matching

With beneficiary microdata, construct rigorous control groups to:
- Control for selection bias
- Estimate causal treatment effects
- Enable subgroup analysis

### Priority 3: State-Level Disaggregation

With state-specific data, produce:
- State-level LNPV estimates
- District-level targeting recommendations
- Policy-relevant geographic insights

---

**Framework:** Difference-in-Differences Net Present Value Model
**Timeline:** 40-year lifetime earnings horizon, discounted at 5%
**Validation:** 8/8 QA checks passed (January 2026)
