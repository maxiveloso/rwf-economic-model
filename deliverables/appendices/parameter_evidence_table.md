# Parameter Evidence Table

## RightWalk Foundation — Economic Impact Model

### Sample Sizes & Evidence Table

---

## 1\. Methodology

### 1.1 Ranking Criterion

Parameters are ranked by the **absolute value of NPV impact elasticity** from the model's sensitivity analysis. Elasticity measures the percentage change in NPV for a 1% change in the parameter value, isolating each parameter's structural leverage on the model independently of how wide or narrow the uncertainty range is.

This is preferred over `npv_impact_pct` (which measures the total NPV swing when varying across the full sensitivity range), because `npv_impact_pct` conflates parameter sensitivity with range width. A parameter with a narrow, well-established range can still have high elasticity if the model is structurally dependent on it.

### 1.2 Confidence Rating Rubric

| Rating | Criteria |
| :---- | :---- |
| **HIGH** | Direct RWF operational data or large-N Indian study (nationally representative survey, n \> 10,000) |
| **MODERATE** | Indian study with relevant design but not RWF-specific; or well-established international methodology applied to Indian data |
| **LOW** | Expert assumption, outdated study (\> 10 years), non-India proxy, or no empirical backing |

### 1.3 Source Data

- Primary input: `data/param_sources/Parameter_Sources_Master.csv` (Jan 2026 update)
- Sensitivity results: `model/outputs/sensitivity_tornado_rte.csv`, `sensitivity_tornado_apprenticeship.csv` (Feb 16, 2026 re-run)
- Cross-checked against: `model/parameter_registry_v3.py` (v3.4, parameter definitions, tiers, sampling methods)
- Model documentation: `github_repo/METHODOLOGY.md`

### 1.4 Sample Size Sourcing

Where available, sample sizes are extracted from original study documentation or survey metadata. Where unavailable or not applicable (calibration models, expert assumptions), the cell is marked accordingly. Parameters marked "TBD" require a review of the source document to extract the study sample size.

---

## 2\. Parameter Evidence Table

Parameters ranked by |elasticity| from sensitivity analysis (Feb 16, 2026 re-run). Top 12 active (non-deprecated) parameters. EXPERIENCE\_LINEAR, EXPERIENCE\_QUAD, FORMAL\_MULTIPLIER, and REAL\_WAGE\_GROWTH deprecated and replaced by sector-specific parameters.

### Table 2.1: Evidence Summary

| Rank | Parameter | Central Estimate | Range | Elasticity | Source | Sample Size | Study Design | Applicability | Confidence |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | **Formal Sector Entry \-- RTE** (`P_FORMAL_RTE`) | 0.30 (30%) | 0.20--0.50 | **1.11** | RWF/Anand guidance (Dec 2025); selection effects literature | N/A \-- expert assumption | Expert elicitation based on selection effects reasoning; no empirical measurement of RTE graduate employment outcomes exists | Expert assumption \-- no empirical basis | **LOW** |
| 2 | **Formal Sector Placement \-- Apprenticeship** (`P_FORMAL_APPRENTICE`) | 0.68 (68%) | 0.50--0.90 | **1.05** | RWF internal tracking data (Nov 2025); DGT/MSDE Tracer Study 2024; ILO 2022 | TBD \-- RWF internal^2^ | Administrative/operational data (RWF program tracking); cross-referenced with MSDE national tracer (n \= 11,136 ITI graduates) | Direct RWF data \-- highest applicability | **HIGH** |
| 3 | **Social Discount Rate** (`SOCIAL_DISCOUNT_RATE`) | 5%^1^ | 3%--8% | **0.89** | Murty & Panda (2020) | N/A \-- calibration model (Ramsey formula) | Calibration: Ramsey equation (p \+ vg) applied to Indian macroeconomic parameters | India-specific calibration using Indian growth, elasticity, and pure time preference | **MODERATE** |
| 4 | **Experience Premium \-- Formal Sector** (`EXPERIENCE_LINEAR_FORMAL`) | **2.7%/yr** | 2.0%--3.5% | **0.59** | Chen, Kanjilal-Bhaduri & Pastore (2022), PLFS 2018-19 | \~100,000 households (PLFS 2018-19); individual-level Mincer regressions for regular/salaried workers | Cross-sectional Mincer regression on nationally representative survey, stratified by employment type | India-specific, PLFS-based, sector-stratified methodology | **MODERATE** |
| 5 | **Real Wage Growth (Formal)** (`REAL_WAGE_GROWTH_FORMAL`) | 1.5%/yr | 0.5%--2.5% | **0.32** | PLFS 2020-24 trends; India inequality literature; Anand guidance (Dec 2025\) | PLFS 2023: \~433,339 individuals across India | Nationally representative repeated cross-sections; supplemented by expert judgment on career progression | India-specific survey data \+ expert judgment | **MODERATE** |
| 6 | **Mincer Return (Higher Secondary)** (`MINCER_RETURN_HS`) | 5.8% per year | 5%--8% | **0.23** | Chen et al. 2022 (PLFS 2018-19); Mitra 2019; Duraisamy 2002 | Conservatively: 25,000-30,000 observations | Cross-sectional Mincer regression on nationally representative survey; quantile regression (Mitra) | India-specific, PLFS-consistent methodology | **MODERATE** |
| 7 | **Apprentice Initial Wage Premium** (`APPRENTICE_INITIAL_PREMIUM`) | Rs 84,000/yr | Rs 50,000--110,000 | **0.15** | PLFS 2023-24; MSDE Annual Report; ILO India Employment Report 2024 | PLFS 2023: \~433,339 individuals across India | Calculated from nationally representative wage data: E\[W\_treatment\] \- E\[W\_control\] using differential formal sector entry rates | India-specific, derived from PLFS wage levels | **MODERATE** |
| 8 | **RTE Test Score Gain** (`RTE_TEST_SCORE_GAIN`) | 0.137 SD (ITT) | 0.10--0.20 | **0.12** | Muralidharan & Sundararaman (2013), NBER w19441 | 18,926 observations (7,451 treatment, 11,475 control) | Randomized Controlled Trial (lottery assignment to private schools under AP School Choice program) | India-specific RCT, but single state (AP); external validity to other states uncertain | **LOW-MODERATE** |
| 9 | **Test Score to Years Conversion** (`TEST_SCORE_TO_YEARS`) | 6.8 years/SD | 4.0--8.0 | **0.12** | Angrist & Evans (2020); Evans & Yuan (2019); Angrist et al. (2021) | 12,500-15,000 individuals total | Meta-analysis / rescaling methodology (micro-LAYS framework) | Global LMIC average; no India-specific conversion factor available | **LOW** |
| 10 | **Formal Sector Entry \-- No Training** (`P_FORMAL_NO_TRAINING`) | 10% | 5%--15% | **0.08** | ILO India Employment Report 2024 (PLFS-based) | PLFS-based tabulations | Nationally representative survey tabulation (youth 18-25 without vocational certification) | India-specific aggregate; not validated for RWF target population specifically | **MODERATE** |
| 11 | **Apprentice Decay Half-Life** (`APPRENTICE_DECAY_HALFLIFE`) | 10 years | 5--50 years | **0.05** | ILO 2024; Attanasio & Guarin (2017, Colombia); Card & Kluve (2017, meta-analysis) | 141 long-term estimates in meta-analysis | International longitudinal studies and meta-analysis; conservative calibration for India | Non-India proxy; no Indian longitudinal vocational training data exists | **LOW** |
| 12 | **Experience Premium \-- Informal Sector** (`EXPERIENCE_LINEAR_INFORMAL`) | **1.2%/yr** | 0.5%--1.8% | **0.04** | Chen, Kanjilal-Bhaduri & Pastore (2022), PLFS 2018-19 | \~100,000 households (PLFS 2018-19); individual-level Mincer regressions for casual workers | Cross-sectional Mincer regression on nationally representative survey, stratified by employment type | India-specific, PLFS-based, sector-stratified methodology | **MODERATE** |

### Table 2.2: Confidence Summary

| Confidence | Count | Parameters |
| :---- | :---- | :---- |
| **HIGH** | 1 | P\_FORMAL\_APPRENTICE |
| **MODERATE** | 7 | SOCIAL\_DISCOUNT\_RATE, EXPERIENCE\_LINEAR\_FORMAL, REAL\_WAGE\_GROWTH\_FORMAL, MINCER\_RETURN\_HS, APPRENTICE\_INITIAL\_PREMIUM, P\_FORMAL\_NO\_TRAINING, EXPERIENCE\_LINEAR\_INFORMAL |
| **LOW-MODERATE** | 1 | RTE\_TEST\_SCORE\_GAIN |
| **LOW** | 3 | P\_FORMAL\_RTE, TEST\_SCORE\_TO\_YEARS, APPRENTICE\_DECAY\_HALFLIFE |

^1^ **Note on Social Discount Rate**: Murty & Panda (2020) derive 8.5% using the original Ramsey formula and 6% using an extended formula with precautionary effects. The model uses 5% as a conservative central estimate within the 3-8% sensitivity range.

^2^ **ACTION REQUIRED \-- P\_FORMAL\_APPRENTICE sample size**: The RWF internal tracking data (Nov 2025\) that produced the 68% formal placement estimate needs its cohort size confirmed. Follow up with the RWF operations team to obtain: (a) total number of apprenticeship completers tracked, (b) time period covered, (c) method of employment status verification (self-report vs. employer confirmation). This is the model's only HIGH-confidence parameter and anchoring its sample size strengthens the entire evidence table.

**Interpretation**: Only 1 of 12 high-impact parameters has HIGH confidence (direct RWF data). Three parameters rated LOW have no India-specific empirical basis and collectively drive the majority of RTE NPV variance and a significant share of apprenticeship NPV uncertainty. These are priority targets for the tracer study.

---

## 3\. Evidence Gaps & Tracer Study Targets

### 3.1 Critical Evidence Gaps (LOW Confidence Parameters)

#### Gap 1: P\_FORMAL\_RTE (30%) \-- Elasticity: 1.11

**Current basis**: Expert assumption (Anand/Shipra guidance, Dec 2025). No empirical measurement of RTE graduate formal sector employment outcomes exists anywhere in the literature.

**Why it matters**: This is the single most impactful parameter for the RTE intervention (111.3% NPV swing). Moving from 20% to 50% changes the RTE NPV by a factor of \~2.8x.

**Tracer study target**: Directly measure formal sector employment status (contract type, PF/ESI enrollment, regular salary) of RTE beneficiaries from 2018-2024 cohorts. Compare against matched non-RTE peers from similar socioeconomic backgrounds.

**Validation approach**: Employment status survey \+ payslip/contract verification for 15-20% of respondents.

---

#### Gap 2: APPRENTICE\_DECAY\_HALFLIFE (10 years) \-- Elasticity: 0.05

**Current basis**: No India-specific longitudinal data. Conservative calibration based on international programs: Colombia Jovenes en Accion (15+ years sustained premium), Germany dual system (15-20 years). The 10-year estimate is deliberately conservative for India given unknown labor market dynamics.

**Why it matters**: Despite modest elasticity (0.05), the NPV impact over the full range is 23.9% because the range is very wide (5-50 years). A 5-year half-life would reduce apprenticeship NPV by \~40% vs. a 50-year half-life.

**Tracer study target**: Cross-cohort design \-- survey apprenticeship completers from multiple vintage years (e.g., 2015, 2018, 2021, 2024\) at a single point in time to estimate the decay trajectory. Track: current employment status, sector (formal/informal), wage level, job tenure persistence.

**Limitation**: Retrospective cross-cohort design introduces cohort effects and survivorship bias. True longitudinal panel would be gold standard but requires 10+ years of follow-up.

---

#### Gap 3: RTE\_TEST\_SCORE\_GAIN (0.137 SD ITT) \-- Elasticity: 0.12

**Current basis**: Single RCT in Andhra Pradesh (Muralidharan & Sundararaman, 2013). The study used lottery-based assignment to private schools under the AP School Choice program. Sample \~1,000 students. Subject heterogeneity is substantial: Hindi 0.55 SD, English 0.12 SD, Math 0 SD.

**Why it matters**: External validity is the core concern. AP private schools may differ systematically from private schools in other states where RWF operates. The aggregate 0.23 SD (used in the model chain) vs. ITT 0.137 SD creates additional ambiguity.

**Tracer study target**: While replicating the RCT is not feasible, the tracer can collect educational attainment data (highest grade completed, exam scores if available) from RTE beneficiaries and comparison group to estimate the realized education quality differential.

---

#### Gap 4: TEST\_SCORE\_TO\_YEARS (6.8 years/SD) \-- Elasticity: 0.12

**Current basis**: Global LMIC meta-analysis (Angrist & Evans 2020, Angrist et al. 2021). The micro-LAYS framework converts test score improvements to equivalent years of schooling based on 150+ interventions. No India-specific conversion factor exists.

**Why it matters**: This parameter bridges the RTE test score gain to the Mincer wage equation. If the true India-specific conversion is 4.0 rather than 6.8, the RTE wage premium drops from 11.5% to 6.7%.

**Tracer study target**: Not directly measurable in a tracer study. Requires secondary analysis of Indian datasets linking test scores to labor market outcomes (e.g., IHDS panel, Young Lives India). Flagged as a desk research priority.

---

### 3.2 Additional Gaps Outside Top 12 (Flagged for Completeness)

#### Gap 5: P\_FORMAL\_NO\_TRAINING (10%) \-- Elasticity: \-0.08

**Current basis**: Derived from ILO India Employment Report 2024 / PLFS tabulations. The 9% figure is a national aggregate for youth 18-25 without vocational training. Regional variation is substantial: South 12.3%, West 12.7%, Central 9.4%, East 8.6%, North 6.0%.

**Tracer study target**: The comparison group (matched non-beneficiaries) in the tracer directly provides a RWF-specific estimate of this counterfactual rate.

---

#### Gap 6: RTE\_RETENTION\_FUNNEL (60%) \-- Not in Sensitivity Top 12

**Current basis**: Assumed same as private school average retention through Grade 12\. No RTE-specific longitudinal tracking exists. May OVERESTIMATE if RTE students face discrimination, hidden costs, or social isolation in private schools.

**Why it matters**: Combined with the 29% seat fill rate (CAG Audit 2014), effective program reach \= 29% x 60% \= 17.4%. If retention is actually 40%, effective reach drops to 11.6%.

**Tracer study target**: Track educational attainment (highest grade completed) of RTE beneficiaries from earlier cohorts (2018-2020 entry) who should have completed Grade 12 by survey date.

---

### 3.3 Gap Prioritization Matrix

| Priority | Parameter | Evidence Gap | Tracer Can Measure? | Alternative |
| :---- | :---- | :---- | :---- | :---- |
| **1 (Critical)** | P\_FORMAL\_RTE | No empirical data at all | Yes \-- employment status survey | None |
| **2 (Critical)** | APPRENTICE\_DECAY\_HALFLIFE | No India longitudinal data | Partially \-- cross-cohort design | International proxy (current approach) |
| **3 (High)** | RTE\_TEST\_SCORE\_GAIN | Single-state RCT, external validity unknown | Partially \-- educational attainment data | Secondary analysis of IHDS/Young Lives |
| **4 (High)** | RTE\_RETENTION\_FUNNEL | No RTE-specific tracking | Yes \-- grade completion from cohort records | UDISE analysis (limited) |
| **5 (Moderate)** | TEST\_SCORE\_TO\_YEARS | No India-specific conversion | No | Desk research (IHDS panel linking test scores to wages) |
| **6 (Moderate)** | P\_FORMAL\_NO\_TRAINING | National aggregate, not RWF-specific | Yes \-- comparison group provides this | Current PLFS-based estimate is reasonable |

---

## 4\. Directional Sample Size Estimates

### 4.1 Methodology

Power calculations use standard two-sample tests with the following assumptions:

- **Power**: 80% (1 \- beta \= 0.80)  
- **Significance**: Two-tailed alpha \= 0.05  
- **Proportions**: Two-sample proportions test (normal approximation to binomial)  
  - Formula: N per arm \= (Z\_alpha/2 \+ Z\_beta)^2 \* \[p1(1-p1) \+ p2(1-p2)\] / (p1 \- p2)^2  
- **Means**: Two-sample t-test assuming equal variances  
  - Formula: N per arm \= 2 \* (Z\_alpha/2 \+ Z\_beta)^2 \* sigma^2 / delta^2

Where Z\_0.025 \= 1.96, Z\_0.20 \= 0.84, so (Z\_alpha/2 \+ Z\_beta)^2 \= (1.96 \+ 0.84)^2 \= 7.84.

These are **directional estimates** \-- order-of-magnitude N per arm for planning purposes, not a full statistical protocol. Actual study design would need to account for clustering, stratification, attrition, and design effects.

### 4.2 Sample Size Estimates by Parameter

#### 4.2.1 P\_FORMAL\_RTE: 30% vs. 9.1% baseline

| Item | Value |
| :---- | :---- |
| Test | Two-sample proportions |
| p\_treatment | 0.30 (RTE graduates) |
| p\_control | 0.091 (national baseline, HS graduates) |
| Effect size | 20.9 percentage points |
| N per arm (simple) | 7.84 \* \[0.30*0.70 \+ 0.091*0.909\] / 0.209^2 \= 7.84 \* \[0.210 \+ 0.083\] / 0.0437 \= 7.84 \* 6.70 \= **\~53 per arm** |
| N per arm (with stratification) | With gender (2) x region (2) subgroups and design effect \~1.5: **\~320 per arm** |
| Tracer one-pager target | 300-400 RTE beneficiaries \-- **adequate** |

**Note**: The large effect size (20.9 pp) means even a simple comparison needs modest samples. The larger 300-400 target in the tracer one-pager accounts for stratification by gender and region, attrition (\~30%), and subgroup analyses.

---

#### 4.2.2 P\_FORMAL\_APPRENTICE: 68% vs. 9% baseline

| Item | Value |
| :---- | :---- |
| Test | Two-sample proportions |
| p\_treatment | 0.68 (apprenticeship completers) |
| p\_control | 0.09 (untrained youth) |
| Effect size | 59 percentage points |
| N per arm (simple) | 7.84 \* \[0.68*0.32 \+ 0.09*0.91\] / 0.59^2 \= 7.84 \* \[0.218 \+ 0.082\] / 0.348 \= 7.84 \* 0.861 \= **\~7 per arm** |
| N per arm (with stratification) | With trade (3) x region (2) subgroups and design effect \~1.5: **\~60-80 per arm** |
| Tracer one-pager target | 300-400 apprenticeship completers \-- **more than adequate** |

**Note**: The effect size is so large that statistical detection is trivial. The tracer's larger sample serves a different purpose: estimating subgroup variation (by trade, region, gender) and validating the rate externally with sufficient precision (95% CI width \~5 pp at n=300).

---

#### 4.2.3 APPRENTICE\_INITIAL\_PREMIUM: Rs 78,000/yr wage difference

| Item | Value |
| :---- | :---- |
| Test | Two-sample t-test (unequal variances) |
| delta (effect) | Rs 78,000/yr |
| sigma (assumed SD) | \~Rs 60,000/yr (based on PLFS wage dispersion for secondary-educated workers) |
| Cohen's d | 78,000 / 60,000 \= 1.30 (very large) |
| N per arm (simple) | 2 \* 7.84 \* 60,000^2 / 78,000^2 \= 2 \* 7.84 \* 0.592 \= **\~10 per arm** |
| N per arm (with stratification) | With trade x region x gender and design effect \~1.5: **\~80-120 per arm** |
| Tracer one-pager target | 300-400 \-- **more than adequate** for overall estimate; enables subgroup breakdowns |

**Note**: The assumed SD of Rs 60,000 should be verified against PLFS microdata. If wage dispersion is higher (e.g., Rs 100,000), N per arm increases to \~25 simple or \~160-200 stratified.

---

#### 4.2.4 APPRENTICE\_DECAY\_HALFLIFE: Cross-Cohort Estimation

| Item | Value |
| :---- | :---- |
| Design | Cross-sectional survey of multiple vintage cohorts (not a simple two-sample test) |
| Approach | Survey completers from 3-4 vintage years (e.g., 2015, 2018, 2021, 2024\) and compare current formal employment rates / wage levels across cohorts |
| Minimum N per vintage | \~100-150 (to estimate cohort-specific formal rate with 95% CI width \< 10 pp) |
| Total N across vintages | **\~400-600** (4 vintages x 100-150 each) |
| Tracer one-pager target | 300-400 apprenticeship completers (primarily recent cohorts) \-- **may need to oversample earlier cohorts** |

**Note**: This is the hardest parameter to validate because it requires retrospective data from older cohorts (2015-2018) who may be harder to locate. The tracer one-pager focuses on 2018-2024 cohorts. To estimate the decay trajectory with any precision, the study would need to deliberately include pre-2018 completers, which increases cost and reduces response rates. An alternative is to collect retrospective employment histories from recent cohorts (cheaper but more recall bias).

### 4.3 Summary: Tracer Sample Adequacy

| Parameter | Minimum N (simple) | N with Stratification | Tracer Target | Adequate? |
| :---- | :---- | :---- | :---- | :---- |
| P\_FORMAL\_RTE | \~53/arm | \~320/arm | 300-400 | Yes |
| P\_FORMAL\_APPRENTICE | \~7/arm | \~60-80/arm | 300-400 | Yes (oversized) |
| APPRENTICE\_INITIAL\_PREMIUM | \~10/arm | \~80-120/arm | 300-400 | Yes (oversized) |
| APPRENTICE\_DECAY\_HALFLIFE | \~100-150/vintage | \~400-600 total | 300-400 | Marginal \-- needs older cohorts |
| Comparison group | \-- | \-- | 600-800 | Yes (PSM matching) |

**Bottom line**: The tracer one-pager's sample targets (1,200-1,600 total) are adequate for all priority parameters except APPRENTICE\_DECAY\_HALFLIFE, which may require deliberate oversampling of pre-2018 cohorts or a supplementary retrospective module.

---

## Appendix A: Data Sources Quick Reference

| Source | Type | Coverage | Approximate N | Notes |
| :---- | :---- | :---- | :---- | :---- |
| PLFS 2023-24 | Nationally representative household survey | All India, quarterly rotation | \~100,000 households (\~400,000 individuals) | Published by MOSPI; gold standard for Indian labor market data |
| ILO India Employment Report 2024 | Secondary analysis | PLFS-based tabulations | Same as PLFS | Published by ILO Geneva; uses PLFS microdata |
| Muralidharan & Sundararaman (2013) | RCT | Andhra Pradesh | \~1,000 students (lottery-assigned) | NBER Working Paper w19441; AP School Choice program |
| Chen et al. (2022) | Cross-sectional regression | All India | \~100,000 households (PLFS 2018-19) | Published returns to education estimates |
| Murty & Panda (2020) | Calibration study | India macroeconomic parameters | N/A (Ramsey formula) | Social discount rate derivation |
| Angrist & Evans (2020) | Meta-analysis | 150+ LMIC interventions | Varies by study | World Bank; LAYS methodology |
| Attanasio & Guarin (2017) | Longitudinal study | Colombia | \~3,000+ (Jovenes en Accion program) | 15+ year follow-up |
| Card & Kluve (2017) | Meta-analysis | 207 studies globally | Varies | Active labor market programs |
| RWF Internal Data (Nov 2025\) | Administrative/operational | RWF program participants | TBD (needs confirmation) | Direct program tracking data |
| DGT/MSDE National Tracer Study (2024) | National tracer survey | ITI graduates across 33 states | n \= 11,136 | STRIVE-funded national study |

---

## 5\. Source Verification Checklist

The sample sizes and study details in Table 2.1 are based on metadata available in the codebase (CSV notes, parameter registry comments, source file names). **The following items should be verified against the original source documents** to confirm accuracy before this table is used in donor-facing materials or the tracer study proposal.

| \# | Parameter | Claim to Verify | Source Document | Status |
| :---- | :---- | :---- | :---- | :---- |
| 1 | P\_FORMAL\_APPRENTICE | RWF internal cohort size (currently TBD) | RWF operations team \-- request apprentice tracking database summary | \[ \] Pending |
| 2 | P\_FORMAL\_APPRENTICE | MSDE national tracer n \= 11,136 | `sources/dgt_msde_2024_tracer_study_iti_employment_outcomes.pdf` | \[ \] Verify |
| 3 | MINCER\_RETURN\_HS | Chen et al. 2022 uses PLFS 2018-19, confirm sample size \~100k HH | Chen et al. 2022 paper (full text) | \[ \] Verify |
| 4 | RTE\_TEST\_SCORE\_GAIN | Muralidharan & Sundararaman 2013 RCT sample \~1,000 students | NBER w19441 (full text) | \[ \] Verify |
| 5 | TEST\_SCORE\_TO\_YEARS | Angrist & Evans 2020 meta-analysis covers 150+ interventions | World Bank working paper (full text) | \[ \] Verify |
| 6 | APPRENTICE\_DECAY\_HALFLIFE | Attanasio & Guarin 2017 Colombia JeA n \~ 3,000+ | Attanasio & Guarin 2017 paper | \[ \] Verify |
| 7 | SOCIAL\_DISCOUNT\_RATE | Murty & Panda 2020 Ramsey derivation (calibration, no sample) | `murty_panda_2020_social_time_preference_rate_climate` | \[ \] Verify methodology |
| 8 | APPRENTICE\_INITIAL\_PREMIUM | PLFS 2023-24 wage data (\~100k HH) used to derive Rs 78k premium | PLFS Annual Report 2023-24 | \[ \] Verify |
| 9 | EXPERIENCE\_LINEAR\_FORMAL / INFORMAL | Chen et al. 2022 Mincer regression: formal 2.7%/yr, informal 1.2%/yr (PLFS 2018-19) | Chen, Kanjilal-Bhaduri & Pastore (2022) full text | \[ \] Verify |
| 10 | REAL\_WAGE\_GROWTH\_FORMAL | 1.5%/yr based on PLFS 2020-24 \+ Anand guidance | PLFS trend tables \+ guidance notes | \[ \] Verify |
| 11 | P\_FORMAL\_NO\_TRAINING | 9% from ILO India Employment Report 2024 | ILO India Employment Report 2024 (Chapter 3\) | \[ \] Verify |
| 12 | Power calc SD assumption | Assumed SD \~Rs 60,000 for wage premium power calculation | PLFS microdata wage distribution tables | \[ \] Verify |

**Recommended workflow**: Check items 1-6 first (most impactful parameters with least certain sample sizes). Items 7-12 are lower priority since the PLFS sample frame is well-documented (\~100k HH is a known figure for PLFS rounds).

---

*Document updated: Feb 16, 2026* *Source data: Parameter\_Sources\_Master.csv (Jan 2026 update); sensitivity\_tornado\_rte.csv, sensitivity\_tornado\_apprenticeship.csv (Feb 16, 2026 re-run)* *Cross-checked: parameter\_registry\_v3.py (v3.4), sensitivity\_analysis\_v2.py, METHODOLOGY.md*