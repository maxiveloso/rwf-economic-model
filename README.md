# RWF Economic Impact Model

**Lifetime Economic Benefits Estimation for RightWalk Foundation Interventions**

[![Validation Status](https://img.shields.io/badge/validation-8%2F8%20passed-brightgreen)]()
[![Model Version](https://img.shields.io/badge/version-4.4-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

---

## Overview

This repository contains a Proof-of-Concept (PoC) economic model that estimates the **Lifetime Net Present Value (LNPV)** of two RightWalk Foundation interventions in India:

1. **Right to Education (RTE)** - Supporting enrollment of economically disadvantaged children in private schools through the 25% reservation quota
2. **National Apprenticeship Training Scheme (NATS)** - Structured apprenticeship programs combining on-the-job training with formal skill certification

The model produces order-of-magnitude benefit estimates across **32 demographic-regional scenarios** (2 interventions × 4 regions × 2 genders × 2 locations) to support cost-effectiveness decision-making.

---

## Key Results

| Intervention | Average LNPV | Range | Key Driver |
|--------------|--------------|-------|------------|
| **RTE** | Rs 14.0 Lakhs | Rs 5.2L - Rs 28.7L | Formal sector entry (30% vs 9.1%) |
| **Apprenticeship** | Rs 34.4 Lakhs | Rs 18.6L - Rs 52.3L | 68% placement rate + wage premium |

### Summary Finding

> Both interventions generate positive lifetime returns across all 32 scenarios analyzed. Apprenticeship yields 4× higher per-beneficiary returns but requires greater operational complexity. RTE is more scalable with lower per-beneficiary costs. **The key driver for both interventions is improved formal sector employment.**

### Dual BCR Analysis (Feb 2026)

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

### BCR Sensitivity to Discount Rate

| Discount Rate | RTE BCR (Full) | Apprenticeship BCR (Full) |
|---------------|----------------|---------------------------|
| 3% (low) | 31.5× | 47.2× |
| 5% (central) | 22.6× | 33.7× |
| 8% (high) | 15.1× | 22.2× |

> Even at 8% discount rate (conservative), both interventions exceed the 3:1 cost-effectiveness threshold.

### Decision Rules

| If your priority is... | Consider... | Because... |
|------------------------|-------------|------------|
| Maximize per-beneficiary impact | Apprenticeship | 4× higher LNPV than RTE |
| Maximize reach with limited budget | RTE | Lower cost, simpler delivery model |
| Serve underserved regions | Targeted Apprenticeship | Higher marginal returns in low-baseline areas |
| Long-term systemic change | RTE | Creates educational pathway shift across generations |
| Quick wins / demonstrable outcomes | Apprenticeship | Shorter time to employment outcomes |

---

## Quick Start

### Prerequisites

- Python 3.10+
- Required packages: `numpy`, `pandas`, `scipy`, `matplotlib`, `seaborn`

### Installation

```bash
# Clone the repository
git clone https://github.com/maxiveloso/rwf-economic-model.git
cd rwf-economic-model

# Install dependencies
pip install -r requirements.txt
```

### Run the Model

```bash
# Generate baseline LNPV results (32 scenarios)
python scripts/run_baseline.py

# Run full sensitivity analysis
python scripts/run_sensitivity.py

# Run validation checks
python scripts/run_validation.py
```

See [QUICKSTART.md](QUICKSTART.md) for detailed usage instructions.

---

## Project Structure

```
rwf-economic-model/
│
├── README.md                    # This file
├── QUICKSTART.md                # Detailed usage guide
├── METHODOLOGY.md               # Causal framework & economic theory
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git exclusions
│
├── src/                         # Core source code
│   ├── __init__.py
│   ├── parameter_registry_v3.py # 77 parameters (SSOT)
│   ├── economic_core_v4.py      # LNPV calculation engine
│   ├── sensitivity_analysis_v2.py # Sensitivity & Monte Carlo
│   └── m4_validation_qa.py      # 8 QA validation checks
│
├── data/
│   ├── parameters/              # Parameter registry CSV
│   ├── sources/                 # 55+ reference documents (PDFs)
│   └── results/                 # Model outputs
│       ├── lnpv_baseline.csv    # 32 scenario results
│       ├── sensitivity/         # Sensitivity CSVs
│       ├── validation/          # Validation outputs
│       └── figures/             # Visualizations (PNGs)
│
├── docs/
│   ├── EXECUTIVE_SUMMARY.md     # 2-page stakeholder summary
│   ├── TECHNICAL_APPENDIX.md    # Full methodology (5-7 pages)
│   ├── VALIDATION_REPORT.md     # 8/8 QA checks
│   ├── stakeholder/             # Q&A guide, talking points
│   └── methodology/             # Detailed technical docs
│
├── scripts/                     # Executable scripts
│   ├── run_baseline.py
│   ├── run_sensitivity.py
│   └── run_validation.py
│
├── deliverables/                # Post-delivery analysis (Feb 2026)
│   ├── appendices/              # 9 technical appendices
│   ├── data/                    # Scenario & persistence CSVs
│   ├── donor_materials/         # 1-pagers for funders
│   ├── ops/                     # Orchestrator & task map
│   └── tracer/                  # Tracer study proposal v2
│
├── tests/                       # Unit tests
│
└── archive/                     # Historical materials
    ├── milestone_prompts/       # M1-M5 requirements
    ├── data_extraction_scripts/ # M1 extraction tools
    └── working_documents/       # Project evolution
```

---

## Documentation

| Document | Description | Audience |
|----------|-------------|----------|
| [PRESENTATION.md](PRESENTATION.md) | **Founders presentation** with embedded figures | Founders, Leadership |
| [EXECUTIVE_SUMMARY.md](docs/EXECUTIVE_SUMMARY.md) | 2-page summary with key findings | Board, Funders |
| [TECHNICAL_APPENDIX.md](docs/TECHNICAL_APPENDIX.md) | Full methodology & parameters | Technical reviewers |
| [METHODOLOGY.md](METHODOLOGY.md) | Causal framework & economic theory | Researchers |
| [Model Chain Diagrams](docs/model_chain_diagrams.md) | Step-by-step parameter flow calculations | Technical deep-dive |
| [VALIDATION_REPORT.md](docs/VALIDATION_REPORT.md) | 8/8 QA checks passed | Quality assurance |
| [Stakeholder Q&A](docs/stakeholder/QA_GUIDE.md) | 12 anticipated questions | Meeting prep |
| [Deliverables Package](deliverables/README_release.md) | Post-delivery deep dives (Feb 2026) | All audiences |

### Post-Delivery Analysis (February 2026)

10 deep-dive workstreams completed after initial PoC delivery. All outputs in [`deliverables/`](deliverables/):

| Deliverable | Description |
|-------------|-------------|
| [Gender Funnel Analysis](deliverables/appendices/gender_data_assessment.md) | 14 priority tracking fields, literature benchmarks for female LFPR/wages |
| [Trade Half-Life Taxonomy](deliverables/appendices/trade_halflife_summary.md) | 4-category trade classification (Rapid/Moderate/Durable/Long-term) with NPV implications |
| [Policy Persistence Scenarios](deliverables/appendices/policy_persistence_scenarios.md) | Illustrative multi-cohort multiplier analysis |
| [Parameter Evidence Table](deliverables/appendices/parameter_evidence_table.md) | 12 high-impact parameters ranked by confidence |
| [Tracer Study Proposal v2](deliverables/tracer/tracer_onepager_v2.md) | 1,200-1,600 sample, Rs 45-55L, 18-month design |
| [Top 5 Evidence Sources](deliverables/appendices/top5_sources_slide.md) | Key citations for presentations |
| [Donor One-Pagers](deliverables/donor_materials/) | Conservative & extended BCR framing |
| [Assumptions Appendix](deliverables/appendices/assumptions_methodology_appendix.md) | Full parameter table with confidence ratings |
| [Evidence Gaps & Budget](deliverables/appendices/evidence_gaps_budget_note.md) | Prioritized research investment plan |
| [Microdata Access Checklist](deliverables/appendices/microdata_access_checklist.md) | PLFS/NSSO unit-level data access steps |

---

## Model Methodology

### LNPV Framework

The model computes Lifetime Net Present Value as:

```
NPV = Σ[t=0 to T] (W_treatment(t) - W_control(t)) / (1 + δ)^t
```

Where:
- `T = 40 years` (career horizon)
- `δ = 5%` (social discount rate)
- `W(t)` = wage at year t, determined by sector and growth rates

### Key Economic Mechanisms

1. **Formal/Informal Sector Split**: Formal wages grow at +1.5%/year; informal at -0.2%/year
2. **Mincer Wage Equation**: Returns to education at 5.8% per year of schooling
3. **Treatment Effects**:
   - RTE: Increased formal sector entry (30% vs 9.1% baseline)
   - Apprenticeship: 68% placement rate + initial wage premium with exponential decay

### RTE Decomposition

For RTE, the total NPV decomposes into:
- **Placement Effect (79%)**: Benefit from higher formal sector entry rate
- **Mincer Effect (21%)**: Benefit from test score gains translating to wages

---

## Key Parameters

The model uses 77 parameters documented in `data/parameters/Parameter_Sources_Master.csv`.

### Tier 1 (Critical - Highest Sensitivity)

| Parameter | Value | Range | Source |
|-----------|-------|-------|--------|
| P_FORMAL_RTE | 30% | 20-50% | RWF guidance |
| P_FORMAL_APPRENTICE | 68% | 50-90% | RWF program data |
| APPRENTICE_DECAY_HALFLIFE | 10 years | 5-30 | Assumed |
| MINCER_RETURN_HS | 5.8% | 5-8% | Chen et al. 2022 |

### Tier 2 (Important)

| Parameter | Value | Range | Source |
|-----------|-------|-------|--------|
| SOCIAL_DISCOUNT_RATE | 5.0% | 3-8% | Murty & Panda 2020 |
| REAL_WAGE_GROWTH_FORMAL | 1.5% | 0.5-2.5% | PLFS 2020-24 |
| REAL_WAGE_GROWTH_INFORMAL | -0.2% | -1% to 0.5% | PLFS 2020-24 |
| FORMAL_WAGE_MULTIPLIER | 2.25× | 2.0-2.5× | ILO 2024 |

---

## Validation

**8/8 QA Checks Passed (January 2026)**

| Check | Status | Notes |
|-------|--------|-------|
| Age-Wage Profile Plausibility | PASS | Formal: 1.91% annual growth |
| NPV Magnitude & Ordering | PASS | All 32 LNPVs positive |
| Break-Even Cost Thresholds | PASS | Range Rs 1.9L - Rs 18.5L |
| Regional Heterogeneity | PASS | South > West > North > East |
| Treatment Effect Decay | PASS | Monotonic, 50% at t=10 |
| Sensitivity Consistency | PASS | MC median within 11% of baseline |
| Assumptions Documented | PASS | All 77 parameters sourced |
| Decomposition Analysis | PASS | 80% + 20% = 100% |

---

## Data Sources

The model draws on 55+ reference documents including:

- **Government**: PLFS 2023-24, MSDE Annual Reports, NITI Aayog, DGT Tracer Studies
- **International**: ILO Global Wage Report 2024, ILO India Employment Report 2024
- **Academic**: Chen et al. 2022, Muralidharan & Sundararaman 2013, Sharma & Sasikumar 2018

All sources are available in `data/sources/` for reproducibility.

---

## Limitations

1. **Causal Identification**: Selection-on-observables assumption may overstate effects by 20-40%
2. **Geographic Granularity**: State/district-level effects require microdata
3. **Wage Persistence**: Apprenticeship half-life (h=10 years) is assumed
4. **External Validity**: Literature parameters may not fully generalize to RWF beneficiaries
5. **No Beneficiary Data**: Population averages used, not RWF-specific outcomes

---

## Recommended Next Steps

### Priority 1: Longitudinal Tracer Study (Fully Designed)
- **Sample:** 1,200-1,600 beneficiaries (RTE + Apprenticeship + matched comparison)
- **Duration:** 18 months core, 24-30 months extended
- **Budget:** Rs 45-55 lakhs
- **Design:** Gender × trade × vintage stratification, PSM matching, cross-cohort decay estimation
- **Impact:** Reduce parameter uncertainty from ±50% to ±15-20% for top 4 parameters
- See full proposal: [`deliverables/tracer/tracer_onepager_v2.md`](deliverables/tracer/tracer_onepager_v2.md)

### Priority 2: Quick Wins (No New Data Collection)
- PLFS unit-level microdata access (Rs 1-2L, 2-3 months) — see [microdata checklist](deliverables/appendices/microdata_access_checklist.md)
- Gender-disaggregated reporting from existing RWF operational data
- Trade-specific outcome tracking in current apprenticeship MIS

### Priority 3: Full Causal Evaluation
- With beneficiary microdata from tracer study
- Propensity score matching and difference-in-differences
- Effort: 150-200 hours post-tracer

---

## Citation

If you use this model, please cite:

```
RightWalk Foundation Economic Impact Model v4.4 (2026)
Lifetime Economic Benefits Estimation for RTE and Apprenticeship Interventions
https://github.com/maxiveloso/rwf-economic-model
```

---

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

## Contact

For questions about this analysis, contact:
- RightWalk Foundation: [contact information]
- Technical inquiries: [email]

---

**Model Version:** 4.4 | **Validation:** 8/8 checks passed | **Last Updated:** February 2026
