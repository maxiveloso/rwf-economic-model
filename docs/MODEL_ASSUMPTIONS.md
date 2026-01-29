# Model Assumptions Documentation
Generated: 2026-01-23 11:23

## Parameter Sources and Assumptions

| Parameter | Value | Tier | Source | Assumption/Limitation |
|-----------|-------|------|--------|----------------------|
| MINCER_RETURN_HS | 0.058 | 2 | Mitra (2019) via Chen et al. (2022) - quantile ret... | Direct empirical |
| EXPERIENCE_LINEAR | 0.00885 | 3 | PLFS 2023-24 cross-sectional age-wage profiles... | Direct empirical |
| EXPERIENCE_QUAD | -0.000123 | 3 | PLFS 2023-24 cross-sectional age-wage profiles... | Direct empirical |
| P_FORMAL_HIGHER_SECONDARY | 0.091 | 1 | ILO India Employment Report 2024 - 9.1% formal emp... | Direct empirical |
| P_FORMAL_RTE | 0.3 | 1 | RWF assumption: 3.3× national baseline (Anand guid... | Direct empirical |
| P_FORMAL_APPRENTICE | 0.68 | 1 | RWF placement data (validated Nov 2025)... | Direct empirical |
| P_FORMAL_NO_TRAINING | 0.09 | 1 | PLFS aggregate estimates (derived, not directly qu... | Direct empirical |
| REAL_WAGE_GROWTH_FORMAL | 0.015 | 2 | PLFS 2020-24 formal sector trends; India inequalit... | Direct empirical |
| REAL_WAGE_GROWTH_INFORMAL | -0.002 | 2 | PLFS 2020-24 informal stagnation; India inequality... | Direct empirical |
| SOCIAL_DISCOUNT_RATE | 0.05 | 2 | Murty & Panda (2020) - Ramsey formula p + vg = 8.5... | Direct empirical |
| RTE_TEST_SCORE_GAIN | 0.137 | 1 | Muralidharan & Sundararaman (2013) NBER RCT w19441... | Direct empirical |
| TEST_SCORE_TO_YEARS | 6.8 | 2 | Angrist & Evans (2020) micro-LAYS rescaling method... | Direct empirical |
| APPRENTICE_INITIAL_PREMIUM | 78000 | 1 | Calculated: [(W_formal × P(F\App)) + (W_informal ×... | Direct empirical |
| APPRENTICE_DECAY_HALFLIFE | 12 | 1 | Assumed - no India-specific data available... | Model assumption |
| APPRENTICE_COMPLETION_RATE | 0.85 | 1 | MSDE funnel analysis; independent of placement rat... | Direct empirical |
| RTE_RETENTION_FUNNEL | 0.6 | 1 | UDISE+ EWS completion rates as proxy (no RTE-speci... | Direct empirical |

## Key Assumptions

1. **Sector-Specific Wage Growth**: Formal sector workers see 1.5%/year career progression while informal stagnates (-0.2%/year). This captures growing inequality.

2. **P_FORMAL_RTE = 30%**: RTE graduates have 3.3× the national baseline (9.1%) for formal sector entry due to selection effects, urban concentration, and private school networks.

3. **Apprenticeship Decay Half-life = 12 years**: No India-specific data exists; this is a model assumption. Sensitivity range [5, 30] years tested.

4. **PLFS Wages as SSOT**: Baseline wages from PLFS 2023-24 are used directly without additional adjustments. This eliminates the over-specification issue.

5. **ITT vs ToT**: RTE test score gain uses Intent-to-Treat (0.137 SD) rather than Treatment-on-Treated (0.23 SD) per Anand guidance.

## Tier 1 (Critical) Parameters - Highest Uncertainty

These parameters have the largest impact on NPV and highest uncertainty:

- **P_FORMAL_HIGHER_SECONDARY**: 0.091 (range: (0.05, 0.15))
- **P_FORMAL_RTE**: 0.3 (range: (0.2, 0.5))
- **P_FORMAL_APPRENTICE**: 0.68 (range: (0.5, 0.9))
- **P_FORMAL_NO_TRAINING**: 0.09 (range: (0.05, 0.15))
- **RTE_TEST_SCORE_GAIN**: 0.137 (range: (0.1, 0.2))
- **APPRENTICE_INITIAL_PREMIUM**: 78000 (range: (69000, 85000))
- **APPRENTICE_DECAY_HALFLIFE**: 12 (range: (5, 30))
- **APPRENTICE_COMPLETION_RATE**: 0.85 (range: (0.75, 0.95))
- **RTE_RETENTION_FUNNEL**: 0.6 (range: (0.5, 0.75))

## Limitations

1. No longitudinal tracking of RTE beneficiaries exists (RTE_RETENTION_FUNNEL is estimated)
2. Apprenticeship wage premium decay rate has no India-specific empirical basis
3. Sector-specific wage growth rates are derived from inequality trends, not individual-level panel data
4. Control group P(Formal) may be understated if selection effects are strong
