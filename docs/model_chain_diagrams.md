# PART 1: MODEL CHAIN DIAGRAMS (Updated Jan 20, 2026)

## 1A. RTE Intervention Parameter Flow

**Key Parameter Values (Updated Jan 20, 2026):**
- RTE_TEST_SCORE_GAIN = **0.137 SD (ITT)** [was 0.23 ToT]
- TEST_SCORE_TO_YEARS = 6.8 years/SD
- MINCER_RETURN_HS = 5.8%
- P_FORMAL_HIGHER_SECONDARY = 9.1% (national baseline for CONTROL)
- **P_FORMAL_RTE = 30%** (NEW - for RTE treatment group)
- FORMAL_MULTIPLIER: **REMOVED** (benefits_adjustment ELIMINATED). PLFS wages ARE the baseline:
  - Urban Male: Formal ₹32,800 / Informal ₹13,425 = 2.44× (embedded ratio)
  - No additional adjustment needed - PLFS already differentiates by sector
- REAL_WAGE_GROWTH_FORMAL = **1.5%/year** (NEW - sector-specific)
- REAL_WAGE_GROWTH_INFORMAL = **-0.2%/year** (NEW - sector-specific)
- SOCIAL_DISCOUNT_RATE = 8.5%
- Urban Male HS wage = ₹32,800/month (formal), ₹13,425/month (informal)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RTE INTERVENTION MODEL CHAIN (Updated Jan 2026)          │
└─────────────────────────────────────────────────────────────────────────────┘

STEP 1: Test Score → Equivalent Years (UPDATED: Using ITT)
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│ RTE_TEST_SCORE_GAIN │  ×  │ TEST_SCORE_TO_YEARS │  =  │   Equivalent Years  │
│   0.137 SD (ITT)    │     │    6.8 years/SD     │     │    0.93 years       │
└─────────────────────┘     └─────────────────────┘     └─────────────────────┘
NOTE: Changed from ToT (0.23) to ITT (0.137) as
we should think of per child allocated, not per completer.

STEP 2: Equivalent Years → Effective Schooling (UPDATED)
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│   Baseline Years    │  +  │   Equivalent Years  │  =  │ years_schooling     │
│      12 years       │     │    0.93 years       │     │    12.93 years      │
└─────────────────────┘     └─────────────────────┘     └─────────────────────┘

STEP 3: Effective Schooling → Education Premium (Mincer Equation) (UPDATED)
┌─────────────────────────────────────────────────────────────────────────────┐
│  education_premium = exp(MINCER_RETURN_HS × (years_schooling - 12))         │
│                    = exp(0.058 × (12.93 - 12))                              │
│                    = exp(0.058 × 0.93)                                      │
│                    = exp(0.054)                                             │
│                    = 1.055  → 5.5% higher wages (was 11.5% with ToT)        │
└─────────────────────────────────────────────────────────────────────────────┘

STEP 4: Benefits Adjustment - ELIMINATED (Jan 20, 2026)
┌─────────────────────────────────────────────────────────────────────────────┐
│  ELIMINATED per RWF guidance to avoid over-specifiying the model.           │
│                                                                             │
│  OLD: benefits_adjustment = 2.25 / 1.86 = 1.21×                             │
│  NEW: No additional adjustment - PLFS wages are Single Source of Truth      │
│                                                                             │
│  PLFS wages ALREADY differentiate by sector:                                │
│  - Formal: ₹32,800 (urban male HS)                                          │
│  - Informal: ₹13,425 (urban male casual)                                    │
│  - Ratio: 2.44× (already exceeds ILO 2.25× target!)                         │
└─────────────────────────────────────────────────────────────────────────────┘

STEP 5: 4-Pathway Model
┌─────────────────────────────────────────────────────────────────────────────┐
│ CONTROL GROUP (9.1% formal, NO Mincer premium):                             │
│ ┌───────────────────────────────────────────────────────────────────────┐   │
│ │ Control Formal (9.1%): ₹32,800/mo (no education premium)              │   │
│ │ Control Informal (90.9%): ₹13,425/mo (no education premium)           │   │
│ └───────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│ TREATMENT GROUP (30% formal, WITH Mincer 5.5% premium):                     │
│ ┌───────────────────────────────────────────────────────────────────────┐   │
│ │ RTE Formal (30%): ₹32,800 × 1.055 = ₹34,604/mo                        │   │
│ │ RTE Informal (70%): ₹13,425 × 1.055 = ₹14,163/mo                      │   │
│ └───────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│ KEY: P_FORMAL_RTE (30%) > P_FORMAL_HIGHER_SECONDARY (9.1%)                  │
│      This captures PLACEMENT EFFECT (private school networks, selection)    │
│      Mincer premium (6.7%) captures QUALITY EFFECT (better learning)        │
└─────────────────────────────────────────────────────────────────────────────┘

STEP 5B: Wage Growth Now Sector-Specific (NEW Jan 2026)
┌─────────────────────────────────────────────────────────────────────────────┐
│ Formal sector: REAL_WAGE_GROWTH_FORMAL = 1.5%/year                          │
│   - Career progression: promotions, seniority increments                    │
│   - Year 40 wage = Year 0 × 1.015^40 = Year 0 × 1.81 (81% growth)           │
│                                                                             │
│ Informal sector: REAL_WAGE_GROWTH_INFORMAL = -0.2%/year                     │
│   - No progression, competition from younger workers                        │
│   - Year 40 wage = Year 0 × 0.998^40 = Year 0 × 0.92 (8% DECLINE)           │
│                                                                             │
│ This captures growing inequality: formal pulls away from informal           │
└─────────────────────────────────────────────────────────────────────────────┘

STEP 6: Expected Wage = Weighted Average (UPDATED with new P_FORMAL_RTE)
┌─────────────────────────────────────────────────────────────────────────────┐
│  TREATMENT (RTE graduates with P_FORMAL_RTE = 30%):                         │
│  E[Wage_treatment] = 0.30 × ₹34,604 + 0.70 × ₹14,163                        │
│                    = ₹10,381 + ₹9,914                                       │
│                    = ₹20,295/month                                          │
│                                                                             │
│  CONTROL (national baseline with P_FORMAL_HS = 9.1%, NO Mincer):            │
│  E[Wage_control] = 0.091 × ₹32,800 + 0.909 × ₹13,425                        │
│                  = ₹2,985 + ₹12,203                                         │
│                  = ₹15,188/month                                            │
└─────────────────────────────────────────────────────────────────────────────┘

STEP 7: Compare Treatment vs Control (SIMPLIFIED)
┌─────────────────────────────────────────────────────────────────────────────┐
│  Treatment (RTE): ₹20,295/month                                             │
│  Control: ₹15,188/month                                                     │
│                                                                             │
│  Monthly differential = ₹20,295 - ₹15,188 = ₹5,107/month                    │
│  Annual differential = ₹5,107 × 12 = ₹61,284/year (Year 1)                  │
│                                                                             │
│  SIGNIFICANTLY HIGHER than previous estimate (₹29,232) due to:              │
│  - P_FORMAL_RTE (30%) >> P_FORMAL_HS (9.1%) - placement advantage           │
│  - Education premium (6.7%) applies to ALL RTE graduates                    │
│  - BUT: benefits_adjustment (1.21×) was REMOVED - partially offsets         │
└─────────────────────────────────────────────────────────────────────────────┘

STEP 8: Decomposition of Treatment Effect
┌─────────────────────────────────────────────────────────────────────────────┐
│  PLACEMENT EFFECT (30% vs 9.1% formal access):                              │
│  - Additional 21% of RTE graduates get formal wages (₹32,800 vs ₹13,425)    │
│  - Contribution: 0.21 × (₹32,800 - ₹13,425) = ₹4,069/month                  │
│                                                                             │
│  QUALITY EFFECT (5.5% Mincer premium):                                      │
│  - Applies to ALL RTE graduates (formal and informal)                       │
│  - Contribution: E[wage_base] × 0.055 ≈ ₹800-1,200/month                    │
│                                                                             │
│  PRIMARY DRIVER: Placement effect > Quality effect                          │
│  This validates the intuition that P_FORMAL_RTE is critical                 │
└─────────────────────────────────────────────────────────────────────────────┘

STEP 9: NPV Calculation (40-year horizon) - UPDATED Jan 2026
┌─────────────────────────────────────────────────────────────────────────────┐
│  NPV = Σ(differential_t × wage_growth_t × employment_prob_t)                │
│        / (1 + SOCIAL_DISCOUNT_RATE)^t                                       │
│                                                                             │
│  KEY CHANGES in Jan 2026:                                                   │
│  - P_FORMAL_RTE = 30% (was P_FORMAL_HS = 9.1%)  →  ↑ NPV                     │
│  - ITT 0.137 (was ToT 0.23)                     →  ↓ NPV                    │
│  - benefits_adjustment REMOVED (was 1.21×)     →  ↓ NPV                    │
│  - Sector-specific wage growth                  →  ↑ NPV (more formal)     │
│                                                                             │
│  With 8.5% discount rate:                                                   │
│  - Present value factor at Year 20: 1/(1.085)^20 = 0.195                    │
│  - Present value factor at Year 40: 1/(1.085)^40 = 0.038                    │
│                                                                             │
│  ESTIMATED LNPV ≈ ₹6-10 Lakhs (Urban Male baseline)                         │
│  - Higher than previous ₹3-5L due to P_FORMAL_RTE = 30%                     │
│  - Lower than original ₹22.8L due to other corrections                      │
└─────────────────────────────────────────────────────────────────────────────┘

KEY INSIGHT (Jan 2026): With P_FORMAL_RTE = 30% (vs control 9.1%), RTE
graduates have SIGNIFICANT placement advantage. The education quality
premium (5.5%) applies to ALL graduates but the placement effect (21pp
more formal access) is the PRIMARY NPV driver.
```

---

## 1B. Apprenticeship Intervention Parameter Flow

**Key Parameter Values (Updated Jan 24, 2026):**
- P_FORMAL_APPRENTICE = 68%
- P_FORMAL_NO_TRAINING = 9%
- FORMAL_MULTIPLIER: **REMOVED** (benefits_adjustment ELIMINATED Jan 2026)
  - PLFS wages are baseline: Formal ₹32,800, Informal ₹13,425 (ratio 2.44×)
- APPRENTICE_INITIAL_PREMIUM = ₹78,000/year
- APPRENTICE_DECAY_HALFLIFE = 12 years
- APPRENTICE_STIPEND_MONTHLY = ₹7,000
- REAL_WAGE_GROWTH_FORMAL = 1.5%/year (NEW)
- REAL_WAGE_GROWTH_INFORMAL = -0.2%/year (NEW)
- SOCIAL_DISCOUNT_RATE = 8.5%

```
┌─────────────────────────────────────────────────────────────────────────────┐
│               APPRENTICESHIP INTERVENTION MODEL CHAIN (Updated Jan 2026)    │
└─────────────────────────────────────────────────────────────────────────────┘

YEAR 0: Training Period (Opportunity Cost)
┌─────────────────────────────────────────────────────────────────────────────┐
│  Treatment: APPRENTICE_STIPEND_MONTHLY × 12 = ₹7,000 × 12 = ₹84,000/yr      │
│  Control:   Informal wage = ₹13,425 × 12 = ₹161,100/yr                      │
│  Year 0 differential = ₹84k - ₹161k = -₹77,100 (NEGATIVE)                   │
│                                                                             │
│  NOTE: Updated stipend (₹7k vs ₹10k) INCREASES opportunity cost             │
└─────────────────────────────────────────────────────────────────────────────┘

YEARS 1-40: Working Life with Premium
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  STEP 1: Initial Premium Calculation                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ initial_premium_pct = APPRENTICE_INITIAL_PREMIUM / base_annual      │   │
│  │                     = ₹78,000 / (₹13,425 × 12)                       │   │
│  │                     = ₹78,000 / ₹161,100 = 0.48 (48% wage boost)     │   │
│  │                                                                     │   │
│  │ Or equivalently: Applied to formal wage as multiplier               │   │
│  │ formal_premium_factor = 1 + (₹78,000 / (₹32,800 × 12))               │   │
│  │                       = 1 + 0.198 = 1.198 (19.8% on formal wages)    │   │
│  │ NOTE: benefits_adjustment (1.21×) ELIMINATED Jan 2026               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  STEP 2: Premium Decay Over Time                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ premium_t = initial_premium × exp(-ln(2) × t / DECAY_HALFLIFE)      │   │
│  │                                                                     │   │
│  │ With halflife = 12 years:                                           │   │
│  │   Year 1:  premium = 48.0% (or 18.5% on formal)                     │   │
│  │   Year 12: premium = 24.0% (half of initial)                        │   │
│  │   Year 24: premium = 12.0% (quarter of initial)                     │   │
│  │   Year 36: premium = 6.0%                                           │   │
│  │   Year 40: premium = 4.8%                                           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

DUAL PATHWAY - Formal vs Informal
                                    ┌─────────────────────────────────────────┐
                           ┌───────▶│ FORMAL PATHWAY (P = 68%)                │
                           │        │ Year 1: ₹32,800 × 1.198 = ₹39,294/mo    │
┌──────────────────────┐   │        │ (benefits_adjustment ELIMINATED)        │
│ P_FORMAL_APPRENTICE  │───┤        │ (wages decay toward base over career)   │
│      = 0.68          │   │        └─────────────────────────────────────────┘
└──────────────────────┘   │
                           │        ┌─────────────────────────────────────────┐
                           └───────▶│ INFORMAL PATHWAY (P = 32%)              │
                                    │ wage = ₹13,425/month (no premium)       │
                                    └─────────────────────────────────────────┘

TREATMENT EXPECTED WAGE (Year 1) - UPDATED Jan 2026
┌─────────────────────────────────────────────────────────────────────────────┐
│  E[Wage_treatment_Y1] = 0.68 × ₹39,294 + 0.32 × ₹13,425                     │
│                       = ₹26,720 + ₹4,296                                    │
│                       = ₹31,016/month (was ₹37,372 with 1.21× adjustment)   │
└─────────────────────────────────────────────────────────────────────────────┘

CONTROL GROUP (No Apprenticeship) - UPDATED Jan 2026
┌─────────────────────────────────────────────────────────────────────────────┐
│  P_FORMAL_NO_TRAINING = 9%                                                  │
│  Formal wage (no premium) = ₹32,800/month (benefits_adjustment ELIMINATED)  │
│  E[Wage_control] = 0.09 × ₹32,800 + 0.91 × ₹13,425                          │
│                  = ₹2,952 + ₹12,217                                         │
│                  = ₹15,169/month                                            │
└─────────────────────────────────────────────────────────────────────────────┘

YEAR 1 DIFFERENTIAL - UPDATED Jan 2026
┌─────────────────────────────────────────────────────────────────────────────┐
│  Monthly differential = ₹31,016 - ₹15,169 = ₹15,847/month                   │
│  Annual differential = ₹15,847 × 12 = ₹190,164/year                         │
│  (was ₹255,840/year with benefits_adjustment - now ~26% lower)              │
│                                                                             │
│  This is the PRIMARY VALUE DRIVER:                                          │
│  68% vs 9% formal access = 59 percentage point improvement                  │
└─────────────────────────────────────────────────────────────────────────────┘

NPV CALCULATION
┌─────────────────────────────────────────────────────────────────────────────┐
│  Year 0: -₹77,100 (opportunity cost - larger with ₹7k stipend)              │
│                                                                             │
│  Years 1-40: Σ[(E[Wage_treatment_t] - E[Wage_control]) × 12                 │
│               / (1 + 0.085)^t]                                              │
│                                                                             │
│  With 8.5% discount rate and premium decay:                                 │
│  - Early years heavily weighted (Year 1 at full value)                      │
│  - Year 20 contribution: ₹255k × 0.5 × 0.195 = ₹24.9k                       │
│  - Year 40 contribution: ₹255k × 0.125 × 0.038 = ₹1.2k                      │
│                                                                             │
│  Approximate LNPV ≈ ₹15-25 Lakhs (urban male, moderate scenario)            │
│                                                                             │
│  Still positive because:                                                    │
│  - 72% vs 10% formal access is massive (7.2× improvement)                   │
│  - Formal/informal gap (2.25×) applies to majority of treatment group       │
└─────────────────────────────────────────────────────────────────────────────┘

KEY INSIGHT: Apprenticeship NPV remains strongly positive because the
68% formal placement rate (vs 9% counterfactual) overcomes the higher
discount rate. The formal access differential is the dominant driver.
```

---

## 1C. Why RTE NPV Dropped More Than Apprenticeship

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COMPARATIVE IMPACT OF PARAMETER UPDATES                  │
└─────────────────────────────────────────────────────────────────────────────┘

                        RTE INTERVENTION          APPRENTICESHIP
                        ───────────────           ──────────────
Formal Access:          9.1% (treatment)          68% (treatment)
                        vs 9.1% (control)         vs 9% (control)
                        ─────────────────         ─────────────────
Differential:           ~0% improvement           +59pp improvement
                        (same P_FORMAL)           (7.6× higher access)

Treatment Effect:       Better QUALITY            Better ACCESS
                        (5.5% wage premium)       (formal sector entry)
                        applied to BOTH sectors   + wage premium

Who Benefits:           91% informal workers      68% get formal jobs
                        get small premium         with 2.25× multiplier

Old P_FORMAL_HS:        40% assumed for RTE       N/A
New P_FORMAL_HS:        9.1% (ILO data)           N/A
Impact:                 Treatment loses its       No change to
                        formal sector advantage   apprenticeship logic

CONCLUSION: RTE's value proposition relied on ASSUMED higher formal
sector access (40%). With realistic 9.1%, the education quality premium
mostly benefits informal workers where wage gains are smaller.

Apprenticeship's value proposition is OBSERVED formal access (68% RWF data),
which creates a real 59pp advantage over counterfactual.
```

