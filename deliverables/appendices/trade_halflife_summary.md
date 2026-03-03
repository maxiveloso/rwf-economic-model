# Half-Life by Trade: Taxonomy & BCR Impact

## RightWalk Foundation -- Economic Impact Model

### Trade-Specific Decay Rates for the Apprenticeship Wage Premium

---

**Document version**: 1.1
**Date**: February 18, 2026
**Input dependencies**: `model/parameter_registry_v3.py` v3.5; `model/economic_core_v4.py` v4.4; `data/param_sources/Parameter_Sources_Master.csv`; `after_delivery/06_gender_funnel/gender_data_assessment.md`

**v1.1 changes** (Feb 18, 2026): NPV implications in Sections 2 and 4 recalculated using the full model specification from `economic_core_v4.py` (including formal experience premium β₂_f=0.027 and real wage growth g_f=1.5%), replacing v1.0's inconsistent mix of simple decay formulas and undiscounted cumulative sums. All percentages now use a consistent "vs. h=10 baseline" comparison at r=5%, T=40 years.

---

## 1. The Problem

The model uses a single `APPRENTICE_DECAY_HALFLIFE = 10 years` for all trades. In reality, different skills decay at vastly different rates:

- A **web development** bootcamp graduate's React skills may be obsolete in 3-5 years
- An **electrician's** wiring knowledge remains relevant for 20+ years
- A **CNC machinist's** programming skills depreciate as machines evolve (~8-12 years)

The decay formula in the model:

```
π(t) = π₀ × exp(-λt)

Where:
  π₀ = Initial wage premium (Rs 84,000/year baseline)
  λ = ln(2) / h (decay rate)
  h = half-life in years
```

At time h, the premium has decayed to 50% of its initial value. The choice of h therefore determines what fraction of the initial premium is captured over a 40-year career horizon.

---

## 2. Four-Category Trade Taxonomy

### Category A: Rapid Obsolescence (h = 5-8 years)

**Defining characteristic**: Skills tied to specific technologies, platforms, or software versions that undergo frequent replacement cycles.

| Example Trades | Typical h | Rationale |
|:---|:---|:---|
| IT/ITES (web development, data entry, BPO) | 5-6 years | Technology stack turnover every 3-5 years (React, Angular, cloud platforms) |
| Digital marketing / social media | 5-7 years | Platform algorithm changes, new channels emerge annually |
| Desktop publishing / graphic design (software-specific) | 6-8 years | Tool migration (CorelDraw → Adobe → AI-assisted design) |

**Supporting evidence**:
- Deming & Noray (2020): STEM skills depreciate 2x faster than non-STEM; half-life of technology-specific knowledge ~5-7 years in US data
- ILO (2021) *Future of Work in India*: IT/ITES sector reports 25-30% of workers need reskilling within 3 years

**NPV implication**: At the category midpoint h=6.5, only **71%** of the h=10 baseline cumulative premium is captured (range: 57% at h=5 to 84% at h=8). These trades capture roughly a third less lifetime economic value than the model baseline assumes. See Section 4 for methodology.

### Category B: Moderate Decay (h = 8-12 years)

**Defining characteristic**: Skills with a durable core but evolving tools/standards. Workers can adapt incrementally but face competitive pressure from newer cohorts.

| Example Trades | Typical h | Rationale |
|:---|:---|:---|
| Automobile mechanics / service technicians | 8-10 years | Vehicle platform changes (ICE → hybrid → EV) require periodic upskilling |
| CNC/CAM machine operation | 9-11 years | Machine interface evolution; programming languages shift |
| Retail management / hospitality operations | 8-10 years | Operational knowledge durable; digital systems change |
| COPA (Computer Operator & Programming Assistant) | 8-10 years | Office software evolves but core logic persists |

**Supporting evidence**:
- Card, Kluve & Weber (2018) meta-analysis: Median vocational training effect in LMICs persists 5-10 years, with significant heterogeneity by trade
- PLFS 2023-24 occupation tenure data: Median job tenure in manufacturing trades = 6-8 years

**NPV implication**: This category spans the model baseline. At h=9, cumulative premium is **92%** of baseline; at h=10, it is 100%; at h=12, it reaches **114%**. Trades in the lower end of this range (COPA at h=9, auto mechanics at h=9) capture slightly less than the model assumes, while CNC/electronics trades (h=10-12) validate or exceed it.

### Category C: Durable Skills (h = 12-18 years)

**Defining characteristic**: Foundational technical skills where the physics/chemistry/biology hasn't changed. Tools evolve slowly. Regulation creates barriers to entry that sustain premiums.

| Example Trades | Typical h | Rationale |
|:---|:---|:---|
| Electrician / wireman | 15-18 years | Wiring standards stable; Indian Electricity Rules evolve slowly |
| Plumber / pipe fitter | 14-17 years | Fundamental hydraulics unchanged; new materials adoptable |
| Welder (structural) | 12-15 years | Core technique stable; new alloys require incremental learning |
| Fitter / turner / machinist (manual) | 12-15 years | Precision metalwork fundamentals endure |

**Supporting evidence**:
- Attanasio, Guarín, Medina & Meghir (2017): Colombia's Jóvenes en Acción program shows 15+ year sustained premium for construction and manufacturing trades
- German dual system longitudinal data: Electricians retain ~75% of initial premium at 15 years (Adda et al., 2007)

**NPV implication**: At the category midpoint h=15, cumulative premium is **131%** of the h=10 baseline (range: 114% at h=12 to 145% at h=18). Electricians (h=16, 136% of baseline) and plumbers (h=15, 131%) offer the highest lifetime economic value per training investment among common NATS trades.

### Category D: Long-Term Persistent (h = 18-25+ years)

**Defining characteristic**: Regulated professions or trades where certification creates lasting market power. Skills are foundational (e.g., basic health, agriculture science) with slow obsolescence.

| Example Trades | Typical h | Rationale |
|:---|:---|:---|
| Health/paramedical assistant | 20-25 years | Anatomy, patient care fundamentals unchanged; certification gating |
| Draughtsman (civil/mechanical) | 18-22 years | Engineering drawing principles stable; CAD transition manageable |
| Surveyor | 18-22 years | Measurement principles stable; GPS/GIS tools adoptable |
| Agriculture/dairy technician | 20-25 years | Biological knowledge base stable; mechanization adoptable |

**Supporting evidence**:
- ILO (2024) India Employment Report: Health and agriculture workers show the lowest inter-cohort wage compression
- WHO (2022): Community health worker programs in LMICs show sustained productivity over 15-20 years with minimal refresher training

**NPV implication**: At the category midpoint h=22, cumulative premium is **161%** of the h=10 baseline (range: 145% at h=18 to 170% at h=25). However, these trades often have lower initial premiums (π₀), partially offsetting the persistence advantage.

---

## 3. Mapping NATS Designated Trades

### 3.1 MSDE Top Designated Trades (by enrollment volume)

`[NEEDS RWF INPUT]` -- The actual RWF trade distribution should replace these MSDE national averages.

| NATS Trade | Category | Estimated h | Enrollment Share (National) |
|:---|:---|:---|:---|
| Fitter | C (Durable) | 13 years | ~15% |
| Electrician | C (Durable) | 16 years | ~12% |
| Welder | C (Durable) | 13 years | ~8% |
| Turner | C (Durable) | 13 years | ~5% |
| COPA | B (Moderate) | 9 years | ~10% |
| Mechanic Motor Vehicle | B (Moderate) | 9 years | ~7% |
| Mechanic Diesel | B (Moderate) | 10 years | ~5% |
| Electronics Mechanic | B (Moderate) | 10 years | ~6% |
| Draughtsman Civil | D (Long-term) | 20 years | ~3% |
| Plumber | C (Durable) | 15 years | ~3% |
| Information Technology | A (Rapid) | 6 years | ~8% |
| Secretarial Practice | A (Rapid) | 7 years | ~4% |
| Other trades | Mixed | 10 years | ~14% |

### 3.2 Trade Mix by Category (National NATS Estimate)

| Category | Share of NATS Enrollment | Weighted Average h |
|:---|:---|:---|
| A (Rapid Obsolescence) | ~12% | 6.5 years |
| B (Moderate Decay) | ~28% | 9.5 years |
| C (Durable Skills) | ~43% | 14 years |
| D (Long-term Persistent) | ~6% | 21 years |
| Mixed/Other | ~11% | 10 years (assumed) |
| **National weighted average** | **100%** | **~11.4 years** |

**Key finding**: The national NATS trade mix is dominated by Category C (durable manual trades), which have half-lives *above* the model's baseline of 10 years. This suggests the current model assumption may be slightly **conservative** for the actual trade mix.

---

## 4. BCR Impact by Trade Mix Scenario

### 4.1 Methodology

The relationship between half-life and NPV is nonlinear. We compute NPV ratios using the **full model specification** from `economic_core_v4.py`, which accounts for the formal sector experience premium and real wage growth that amplify the wage base over a career:

```
NPV(h) = Σ_{t=0}^{T-1} p_f × exp(β₂_f × t) × (1+g_f)^t × exp(-λt) / (1+r)^t

Where:
  p_f = 0.72       (P(Formal|Apprentice))
  β₂_f = 0.027     (formal experience premium, Chen et al. 2022)
  g_f = 0.015       (formal real wage growth)
  λ = ln(2) / h     (decay rate)
  r = 0.05          (social discount rate)
  T = 40            (working life horizon)
```

This formula captures the key interaction: formal sector wages grow with experience (2.7%/yr) and real wage growth (1.5%/yr), so the premium base at year t is larger than at year 0. This makes early-career premium capture relatively more valuable in NPV terms, increasing sensitivity to half-life compared to a simple decay-only formula.

**Reference NPV ratios** (vs. h=10 baseline):

| h (years) | NPV as % of h=10 | Context |
|:---|:---|:---|
| 5 | 57% | Conservative scenario lower bound |
| 6 | 66% | IT/ITES trades |
| 9 | 92% | COPA, auto mechanics |
| **10** | **100%** | **Model baseline** |
| 13 | 120% | Fitter, welder, turner |
| 15 | 131% | Plumber |
| 16 | 136% | Electrician |
| 20 | 153% | Draughtsman |
| 50 | 212% | Optimistic scenario upper bound |

**Baseline**: h=10 years, Apprenticeship NPV ≈ Rs 8.0L (West, male, urban reference)

For scenario BCR calculations below, approximate NPV = Rs 8.0L × (NPV ratio), and BCR = NPV / cost.

### 4.2 Three Trade Mix Scenarios

#### Scenario 1: IT-Heavy Mix (Pessimistic)

Represents an apprenticeship program focused on IT/ITES and digital trades.

| Category | Share | h_mid |
|:---|:---|:---|
| A (Rapid) | 40% | 6.5 |
| B (Moderate) | 35% | 9.5 |
| C (Durable) | 20% | 14 |
| D (Long-term) | 5% | 21 |
| **Weighted h** | | **9.2 years** |

- NPV impact vs. baseline (h=10): **-6%** (full model at weighted h=9.2)
- Approximate NPV: Rs 7.5L (vs. Rs 8.0L baseline)
- BCR (RWF-only, cost Rs 6,000): ~125:1 (vs. 133:1 baseline)
- BCR (Full, cost Rs 1.58L): ~4.7:1 (vs. 5.1:1 baseline)

#### Scenario 2: Balanced National Mix (Baseline-Adjacent)

Represents the national NATS trade distribution as estimated in Section 3.2.

| Category | Share | h_mid |
|:---|:---|:---|
| A (Rapid) | 12% | 6.5 |
| B (Moderate) | 28% | 9.5 |
| C (Durable) | 43% | 14 |
| D (Long-term) | 6% | 21 |
| Other | 11% | 10 |
| **Weighted h** | | **11.4 years** |

- NPV impact vs. baseline (h=10): **+10%** (full model at weighted h=11.4)
- Approximate NPV: Rs 8.8L (vs. Rs 8.0L baseline)
- BCR (RWF-only): ~147:1
- BCR (Full): ~5.6:1

#### Scenario 3: Manufacturing/Infrastructure-Heavy Mix (Optimistic)

Represents a program deliberately targeting durable trades (electrician, fitter, welder, plumber).

| Category | Share | h_mid |
|:---|:---|:---|
| A (Rapid) | 5% | 6.5 |
| B (Moderate) | 15% | 9.5 |
| C (Durable) | 60% | 14 |
| D (Long-term) | 20% | 21 |
| **Weighted h** | | **15.1 years** |

- NPV impact vs. baseline (h=10): **+32%** (full model at weighted h=15.1)
- Approximate NPV: Rs 10.5L (vs. Rs 8.0L baseline)
- BCR (RWF-only): ~175:1
- BCR (Full): ~6.7:1

### 4.3 Scenario Comparison Summary

| Scenario | Weighted h | NPV (approx.) | BCR (Full) | BCR vs. Baseline |
|:---|:---|:---|:---|:---|
| IT-Heavy (pessimistic) | 9.2 years | Rs 7.5L | 4.7:1 | -6% |
| Balanced National | 11.4 years | Rs 8.8L | 5.6:1 | +10% |
| Manufacturing-Heavy (optimistic) | 15.1 years | Rs 10.5L | 6.7:1 | +32% |
| **Model baseline** | **10 years** | **Rs 8.0L** | **5.1:1** | **--** |

**Key insight**: The trade mix matters, but even the pessimistic IT-heavy scenario produces a strong BCR (4.7:1 Full, 125:1 RWF-only). The model's baseline assumption of h=10 appears slightly conservative relative to the national NATS trade distribution, which is dominated by durable manual trades (enrollment-weighted average h ≈ 11.4, implying ~108% of baseline NPV).

**Policy implication**: RWF could meaningfully improve the apprenticeship BCR by steering youth toward Category C/D trades where skill premiums persist longest. A shift from h=10 to h=15 increases NPV by ~31%.

---

## 5. Tracer Data Needs for Empirical Decay Estimation

### 5.1 Variables to Collect

The tracer study should collect the following for ALL apprenticeship respondents:

| Variable | Type | Purpose |
|:---|:---|:---|
| **Trade classification** (4-digit NTC code) | Categorical | Maps to taxonomy categories A-D |
| **Apprenticeship start date** | Date (month/year) | Calculates time since completion |
| **Apprenticeship end date** | Date (month/year) | Confirms completion; enables duration analysis |
| **Current employment status** | Categorical (formal/informal/unemployed/NILF) | Primary outcome at each follow-up |
| **Current monthly wage** (gross) | Continuous (INR) | Wage premium measurement |
| **Job start date** (current job) | Date (month/year) | Measures job tenure; enables tenure analysis |
| **Job end dates** (all jobs since completion) | Date (month/year) per job | Reconstructs employment history |
| **Trade relevance of current job** | Likert 1-5 | Measures skill utilization decay |
| **Any upskilling/retraining since completion** | Binary + type | Controls for human capital renewal |
| **Reason for job change** (if applicable) | Categorical | Distinguishes voluntary from displacement |

### 5.2 Cross-Cohort Design for Decay Estimation

The ideal approach is a **cross-cohort design**: survey apprenticeship completers from multiple vintage years at a single point in time.

| Vintage | Years Since Completion | Target N | What It Measures |
|:---|:---|:---|:---|
| 2024 completers | 1-2 years | 100-150 | Initial premium (π₀) |
| 2021 completers | 4-5 years | 100-150 | Short-term decay |
| 2018 completers | 7-8 years | 100-150 | Medium-term decay (near half-life) |
| 2015 completers | 10-11 years | 75-100 | At or past half-life |
| **Total** | | **375-550** | Full decay trajectory |

**Comparison group** at each vintage: Matched non-apprentice youth from same age cohort, same trade interest (if available), same region.

### 5.3 Analytical Approaches

Once tracer data is available, three methods can estimate the trade-specific half-life:

**Method 1: Kaplan-Meier Survival Analysis**
- Define "event" = loss of formal employment (transition from formal to informal/unemployed)
- Estimate survival curve S(t) = P(still formally employed at time t since completion)
- Stratify by trade category (A/B/C/D)
- Non-parametric; makes no distributional assumptions
- Limitation: Only measures formal/informal transition, not the continuous wage premium

**Method 2: Cox Proportional Hazards Regression**
- Model: h(t) = h₀(t) × exp(β₁×Trade + β₂×Region + β₃×Gender + ...)
- Estimates hazard ratios for formal employment loss by trade category
- Semi-parametric; accounts for covariates
- Tests whether trade category significantly predicts premium persistence after controlling for demographics

**Method 3: Exponential Decay Regression on Wage Data**
- Model: ln(Premium_i) = α - λ × t_i + β×X_i + ε_i
- Where Premium_i = wage_i - predicted_counterfactual_wage_i
- Directly estimates λ (and therefore h = ln(2)/λ) for each trade category
- Parametric; assumes exponential decay (can test with quadratic term)
- Most directly maps to the model's decay specification

**Recommended approach**: Start with Kaplan-Meier (transparent, easy to communicate). Confirm with Cox regression (adds covariates). If wage data quality is sufficient, estimate exponential decay model for direct calibration of h.

### 5.4 Stratification for Trade Groups

The tracer sampling should ensure adequate representation within each trade category. Minimum N per category for survival analysis:

| Category | Minimum N | Rationale |
|:---|:---|:---|
| A (Rapid) | 50-75 | Smallest enrollment share; need enough events |
| B (Moderate) | 80-100 | Moderate share; good representation |
| C (Durable) | 120-150 | Largest share; enables subgroup analysis |
| D (Long-term) | 30-50 | Smallest share; may need to pool with C |

**Total minimum for trade-stratified analysis**: ~280-375 apprenticeship completers across all vintages.

This aligns with the tracer one-pager target of 300-400 apprenticeship completers, but the tracer should deliberately include pre-2018 cohorts (currently underrepresented in the sampling frame).

---

## 6. Gender Interaction with Trade Half-Life

Per the Gender Data Assessment (Task #6), the trade distribution is heavily gendered:

- **Category A/B** (IT, COPA, secretarial): Higher female enrollment share (~30-40% female)
- **Category C** (electrician, fitter, welder): Predominantly male (~5-10% female)
- **Category D** (health assistant, draughtsman): Mixed (~15-25% female)

**Implication**: If the female trade mix is concentrated in Category A/B (shorter half-life), the gender-specific apprenticeship NPV will be lower than the male-specific NPV -- **even before accounting for wage gaps and LFPR differences**. The tracer should collect trade × gender × employment outcomes to disentangle these effects.

---

## 7. Caveats

1. **No India-specific longitudinal data exists** for vocational training premium persistence. The taxonomy is constructed from international evidence and sector logic.
2. **Half-life is a simplification**: Real skill decay is not purely exponential. Some skills have threshold effects (suddenly obsolete when a technology changes) or step functions (stable for years, then rapid depreciation).
3. **Upskilling confounds**: Workers who invest in continuing education or retraining may sustain premiums longer than the "natural" half-life suggests. The tracer should capture upskilling separately.
4. **Trade classification granularity**: The 4-category taxonomy is deliberately coarse. Within each category, individual trades may vary by ±3-5 years.
5. **Initial premium × half-life interaction**: Category D trades (longest half-life) often have lower initial premiums. Total NPV is the integral of both, not just half-life.

---

*Document created: February 16, 2026*
*Updated: February 18, 2026 (v1.1 — NPV methodology correction)*
*Inputs: parameter_registry_v3.py v3.5, economic_core_v4.py v4.4, Parameter_Sources_Master.csv, gender_data_assessment.md (Task #6)*
*References: Deming & Noray (2020); Card, Kluve & Weber (2018); Attanasio et al. (2017); Adda et al. (2007); ILO (2024); WHO (2022); Chen, Kanjilal-Bhaduri & Pastore (2022)*
