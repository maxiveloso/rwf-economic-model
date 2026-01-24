#!/usr/bin/env python3
"""
Run comprehensive sensitivity analysis.

Outputs:
- data/results/sensitivity/tornado_rte.csv
- data/results/sensitivity/tornado_apprenticeship.csv
- data/results/sensitivity/monte_carlo_distributions.csv
- data/results/sensitivity/breakeven_analysis.csv
- data/results/figures/*.png
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from sensitivity_analysis_v2 import run_comprehensive_sensitivity

def main():
    print("=" * 60)
    print("RWF Economic Impact Model - Sensitivity Analysis")
    print("=" * 60)
    print()

    output_dir = os.path.join(
        os.path.dirname(__file__),
        '..', 'data', 'results'
    )

    # Run comprehensive sensitivity analysis
    results = run_comprehensive_sensitivity(output_dir=output_dir)

    print()
    print("=" * 60)
    print("Sensitivity analysis complete!")
    print("=" * 60)
    print()
    print("Outputs generated:")
    print("  - Tornado diagrams (one-way sensitivity)")
    print("  - Monte Carlo distributions (10,000 iterations)")
    print("  - Break-even cost thresholds")
    print("  - Two-way heatmaps")
    print("  - Decomposition analysis (RTE)")
    print()

if __name__ == "__main__":
    main()
