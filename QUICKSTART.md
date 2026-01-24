# Quick Start Guide

This guide will help you run the RWF Economic Impact Model and reproduce all results.

---

## Prerequisites

### System Requirements
- Python 3.10 or higher
- 4GB RAM minimum
- ~500MB disk space (including source documents)

### Python Dependencies
```
numpy>=1.24.0
pandas>=2.0.0
scipy>=1.10.0
matplotlib>=3.7.0
seaborn>=0.12.0
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/rwf-economic-model.git
cd rwf-economic-model
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Model

### Option 1: Run Everything

```bash
# Full pipeline: baseline + sensitivity + validation
python scripts/run_all.py
```

This will:
1. Generate 32 baseline LNPV scenarios
2. Run complete sensitivity analysis (OAT, two-way, Monte Carlo)
3. Execute all 8 validation checks
4. Generate all visualizations

**Output:** Results saved to `data/results/`

### Option 2: Run Components Separately

#### Generate Baseline Results

```bash
python scripts/run_baseline.py
```

**Output:** `data/results/lnpv_baseline.csv` with 32 scenarios

#### Run Sensitivity Analysis

```bash
python scripts/run_sensitivity.py
```

**Outputs:**
- `data/results/sensitivity/tornado_rte.csv`
- `data/results/sensitivity/tornado_apprenticeship.csv`
- `data/results/sensitivity/monte_carlo_distributions.csv`
- `data/results/sensitivity/breakeven_analysis.csv`
- All visualization PNGs in `data/results/figures/`

#### Run Validation Checks

```bash
python scripts/run_validation.py
```

**Output:** `data/results/validation/validation_report.md` (8/8 checks)

---

## Using the Python Modules Directly

### Import the Core Modules

```python
from src.parameter_registry import ParameterRegistry
from src.economic_core import LNPVModel
from src.sensitivity_analysis import SensitivityAnalyzer
from src.validation import ModelValidator
```

### Example: Calculate LNPV for a Single Scenario

```python
from src.parameter_registry import ParameterRegistry
from src.economic_core import LNPVModel

# Initialize
params = ParameterRegistry()
model = LNPVModel(params)

# Calculate LNPV for RTE, South region, Urban Male
result = model.calculate_lnpv(
    intervention='rte',
    region='south',
    gender='male',
    location='urban'
)

print(f"LNPV: Rs {result.lnpv / 100000:.2f} Lakhs")
print(f"P(Formal): {result.p_formal * 100:.1f}%")
```

### Example: Run Monte Carlo Simulation

```python
from src.sensitivity_analysis import SensitivityAnalyzer

analyzer = SensitivityAnalyzer()

# Run 1000 Monte Carlo iterations for RTE
mc_results = analyzer.run_monte_carlo(
    intervention='rte',
    n_iterations=1000
)

print(f"Mean LNPV: Rs {mc_results.mean / 100000:.2f} Lakhs")
print(f"5th percentile: Rs {mc_results.p5 / 100000:.2f} Lakhs")
print(f"95th percentile: Rs {mc_results.p95 / 100000:.2f} Lakhs")
```

### Example: Access Parameters

```python
from src.parameter_registry import ParameterRegistry

params = ParameterRegistry()

# Get a specific parameter
mincer_return = params.get('MINCER_RETURN_HS')
print(f"Mincer Return: {mincer_return.value}%")
print(f"Range: {mincer_return.low}% - {mincer_return.high}%")
print(f"Source: {mincer_return.source}")

# List all Tier 1 parameters
tier1_params = params.get_by_tier(1)
for p in tier1_params:
    print(f"{p.name}: {p.value}")
```

---

## Understanding the Outputs

### Baseline Results (`lnpv_baseline.csv`)

| Column | Description |
|--------|-------------|
| `scenario_id` | Unique identifier (e.g., `rte_male_urban_south`) |
| `intervention` | `rte` or `apprenticeship` |
| `region` | `north`, `south`, `east`, `west` |
| `gender` | `male` or `female` |
| `location` | `urban` or `rural` |
| `lnpv` | Lifetime NPV in Rupees |
| `p_formal` | Probability of formal employment |

### Monte Carlo Results (`monte_carlo_distributions.csv`)

| Column | Description |
|--------|-------------|
| `scenario_id` | Scenario identifier |
| `mean` | Mean LNPV across iterations |
| `median` | Median LNPV |
| `std` | Standard deviation |
| `p5`, `p10`, `p25`, `p75`, `p90`, `p95` | Percentiles |
| `p_positive` | Probability LNPV > 0 (should be 100%) |

### Sensitivity Results (`tornado_*.csv`)

| Column | Description |
|--------|-------------|
| `parameter` | Parameter name |
| `baseline` | LNPV at baseline value |
| `low` | LNPV at low bound |
| `high` | LNPV at high bound |
| `swing` | Range (high - low) |
| `rank` | Importance ranking (1 = most sensitive) |

---

## Visualizations

All visualizations are saved to `data/results/figures/`:

| File | Description |
|------|-------------|
| `tornado_rte.png` | RTE parameter sensitivity ranking |
| `tornado_apprenticeship.png` | Apprenticeship parameter sensitivity |
| `histogram_monte_carlo_rte.png` | RTE LNPV distribution |
| `histogram_monte_carlo_apprenticeship.png` | Apprenticeship LNPV distribution |
| `boxplot_regional.png` | Regional LNPV comparison |
| `decomposition_stacked_bar.png` | RTE Placement vs Mincer effects |
| `lineplot_halflife.png` | Apprenticeship half-life sensitivity |
| `breakeven_bar_chart.png` | Break-even cost thresholds |
| `heatmap_app_pformal_halflife.png` | Two-way sensitivity |
| `validation_age_wage_profiles.png` | Age-wage trajectory validation |
| `validation_decay_trajectory.png` | Apprenticeship decay validation |

---

## Modifying Parameters

### Via CSV (Recommended)

Edit `data/parameters/Parameter_Sources_Master.csv`:

```csv
parameter_name,value,low,high,unit,source,tier
MINCER_RETURN_HS,7.0,5.0,9.0,percent,Mitra 2019,1
P_FORMAL_RTE,30,20,50,percent,RWF guidance,1
...
```

Then run:
```bash
python scripts/sync_parameters.py
python scripts/run_all.py
```

### Via Python

```python
from src.parameter_registry import ParameterRegistry

params = ParameterRegistry()

# Override a parameter for this session
params.override('P_FORMAL_RTE', value=0.40)  # 40% instead of 30%

# Run model with updated parameter
model = LNPVModel(params)
result = model.calculate_all_scenarios()
```

---

## Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_economic_core.py

# Run with verbose output
python -m pytest tests/ -v
```

---

## Troubleshooting

### Common Issues

**ImportError: No module named 'src'**
```bash
# Make sure you're in the repo root directory
cd rwf-economic-model
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

**FileNotFoundError: Parameter CSV not found**
```bash
# Ensure data files are present
ls data/parameters/
# Should show: Parameter_Sources_Master.csv
```

**Memory Error during Monte Carlo**
```python
# Reduce iterations
mc_results = analyzer.run_monte_carlo(n_iterations=500)  # Instead of 1000
```

### Getting Help

1. Check the [Technical Appendix](docs/TECHNICAL_APPENDIX.md) for methodology details
2. Review [Validation Report](docs/VALIDATION_REPORT.md) for expected outputs
3. Open a GitHub issue for bugs or questions

---

## File Locations Reference

| What | Where |
|------|-------|
| Parameter definitions | `data/parameters/Parameter_Sources_Master.csv` |
| Source documents | `data/sources/` (48 PDFs) |
| Baseline results | `data/results/lnpv_baseline.csv` |
| Sensitivity outputs | `data/results/sensitivity/` |
| Validation outputs | `data/results/validation/` |
| Visualizations | `data/results/figures/` |
| Core Python code | `src/` |
| Run scripts | `scripts/` |
| Documentation | `docs/` |

---

**Model Version:** 4.3 | **Last Updated:** January 2026
