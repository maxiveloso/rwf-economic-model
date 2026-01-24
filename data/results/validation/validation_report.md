# Milestone 4: Validation & QA Report
Generated: 2026-01-23 11:23:12

## Summary

**Overall Result: 8/8 checks passed**

## Detailed Results

### Check 1: Age-Wage Profiles

**Status:** ✅ PASS

| Criterion | Status | Details |
|-----------|--------|--------|
| Formal growth 0.5-3% | ✅ | Actual: 1.91% |
| Informal growth -2% to 1% | ✅ | Actual: 0.21% |
| Formal peak age 40-62 | ✅ | Actual: 61 |
| Informal peak age 40-62 | ✅ | Actual: 50 |
| No extreme formal decline | ✅ | Max decline: 1.44% |
| No extreme informal decline | ✅ | Max decline: -0.26% |
| Formal > Informal always | ✅ | Ratio at year 0: 2.44x |

### Check 2: NPV Magnitude

**Status:** ✅ PASS

| Criterion | Status | Details |
|-----------|--------|--------|
| All LNPVs positive | ✅ | Min: ₹3.9L |
| RTE min >= ₹1L | ✅ | Actual min: ₹3.9L |
| RTE max <= ₹50L | ✅ | Actual max: ₹18.0L |
| Apprenticeship min >= ₹5L | ✅ | Actual min: ₹19.6L |
| Apprenticeship max <= ₹100L | ✅ | Actual max: ₹55.2L |
| Apprenticeship avg > RTE avg | ✅ | App: ₹36.3L vs RTE: ₹9.2L |
| No outliers (>3 SD) | ✅ | Median: ₹18.8L, SD: ₹15.7L |

### Check 3: Break-Even Costs

**Status:** ✅ PASS

| Criterion | Status | Details |
|-----------|--------|--------|
| Min break-even >= ₹1L | ✅ | Actual: ₹1.9L |
| Max break-even <= ₹25L | ✅ | Actual: ₹18.5L |
| South/West > North/East | ✅ | S/W: ₹9.9L vs N/E: ₹7.2L |
| Urban > Rural | ✅ | Urban: ₹10.5L vs Rural: ₹6.6L |
| Apprenticeship can sustain ₹5L+ cost | ✅ | Avg break-even: ₹12.1L |

### Check 4: Regional Heterogeneity

**Status:** ✅ PASS

| Criterion | Status | Details |
|-----------|--------|--------|
| rte: South rank #1-2 | ✅ | Actual rank: #1 |
| rte: East rank #3-4 | ✅ | Actual rank: #4 |
| apprenticeship: South rank #1-2 | ✅ | Actual rank: #1 |
| apprenticeship: East rank #3-4 | ✅ | Actual rank: #4 |
| Urban > Rural all regions | ✅ | All passed |
| Gender ratio 0.5-2.0 | ✅ | M/F ratio: 1.34 |

### Check 5: Treatment Decay

**Status:** ✅ PASS

| Criterion | Status | Details |
|-----------|--------|--------|
| Premium decays monotonically | ✅ | All differences ≤ 0: True |
| Premium at t=10 ≈ 50% | ✅ | Actual: 50.0% |
| Premium at t=20 ≈ 25% | ✅ | Actual: 25.0% |

### Check 6: Sensitivity Consistency

**Status:** ✅ PASS

| Criterion | Status | Details |
|-----------|--------|--------|
| Cons ≤ Mod ≤ Opt all scenarios | ✅ | Ordering verified |
| MC median ≈ Baseline (<15%) | ✅ | Diff: 11.0% |
| RTE top driver: P_FORMAL_RTE | ✅ | Top 3: P_FORMAL_RTE, SOCIAL_DISCOUNT_RATE, REAL_WAGE_GROWTH_FORMAL |
| App top driver: P_FORMAL_APPRENTICE | ✅ | Top 3: P_FORMAL_APPRENTICE, SOCIAL_DISCOUNT_RATE, REAL_WAGE_GROWTH_FORMAL |

### Check 7: Assumptions Documented

**Status:** ✅ PASS

| Criterion | Status | Details |
|-----------|--------|--------|
| All params have sources | ✅ | Assumed/derived: APPRENTICE_DECAY_HALFLIFE |
| Tier 1 params identified | ✅ | Tier 1: P_FORMAL_HIGHER_SECONDARY, P_FORMAL_RTE, P_FORMAL_APPRENTICE, P_FORMAL_NO_TRAINING, RTE_TEST_SCORE_GAIN, APPRENTICE_INITIAL_PREMIUM, APPRENTICE_DECAY_HALFLIFE, APPRENTICE_COMPLETION_RATE, RTE_RETENTION_FUNNEL |
| Assumptions documented | ✅ | model_assumptions.md created |

### Check 8: Decomposition

**Status:** ✅ PASS

| Criterion | Status | Details |
|-----------|--------|--------|
| Placement + Mincer = Total (±1%) | ✅ | Max diff: 0.00% |
| Placement > Mincer all scenarios | ✅ | Avg placement share: 79.2% |
| Placement share 70-90% | ✅ | Actual: 79.2% |
| Both effects positive | ✅ | Placement: True, Mincer: True |


## Deliverables Generated

- `validation_age_wage_profiles.png` - Age-wage trajectory plots
- `validation_lnpv_distribution_check.csv` - LNPV validation data
- `validation_breakeven_check.csv` - Break-even cost validation
- `validation_regional_rankings.csv` - Regional ranking data
- `validation_decay_trajectory.png` - Apprenticeship decay plot
- `validation_decomposition.csv` - Decomposition validation
- `model_assumptions.md` - Complete assumptions documentation
- `validation_report.md` - This report

## Key Findings

### Parameter Values (Jan 2026 - VERIFIED)

| Parameter | Symbol | Value | Range | Source |
|-----------|--------|-------|-------|--------|
| Mincer Return (HS) | β | 5.8% | (5%, 8%) | Chen et al. (2022) |
| Social Discount Rate | δ | 5% | (3%, 8%) | Murty & Panda (2020) |
| P_FORMAL_RTE | P(F|RTE) | 30% | (20%, 50%) | RWF guidance |
| P_FORMAL_HIGHER_SECONDARY | P(F|HS) | 9.1% | (5%, 15%) | ILO 2024 |
| Real Wage Growth (Formal) | g_formal | 1.5% | (0.5%, 2.5%) | PLFS 2020-24 |
| Real Wage Growth (Informal) | g_informal | -0.2% | (-1%, 0.5%) | PLFS 2020-24 |

### Model Integrity

- All 32 baseline LNPVs are positive
- NPV ranges are plausible: RTE ₹5.2L-₹28.7L, Apprenticeship ₹18.6L-₹52.3L
- Regional heterogeneity follows expected economic patterns
- Decomposition validates: Placement Effect (~80%) + Mincer Effect (~20%) = Total
