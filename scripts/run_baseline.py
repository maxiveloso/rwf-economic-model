#!/usr/bin/env python3
"""
Run baseline LNPV calculations for all 32 scenarios.

Output: data/results/lnpv_baseline.csv
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from economic_core_v4 import run_baseline_scenarios

def main():
    print("=" * 60)
    print("RWF Economic Impact Model - Baseline LNPV Calculation")
    print("=" * 60)
    print()

    # Run baseline scenarios
    results = run_baseline_scenarios()

    # Save results
    output_path = os.path.join(
        os.path.dirname(__file__),
        '..', 'data', 'results', 'lnpv_baseline.csv'
    )
    results.to_csv(output_path, index=False)

    print(f"\nResults saved to: {output_path}")
    print(f"Total scenarios: {len(results)}")
    print()

    # Summary statistics
    for intervention in ['rte', 'apprenticeship']:
        subset = results[results['intervention'] == intervention]
        mean_lnpv = subset['lnpv'].mean() / 100000
        min_lnpv = subset['lnpv'].min() / 100000
        max_lnpv = subset['lnpv'].max() / 100000
        print(f"{intervention.upper()}:")
        print(f"  Mean LNPV: Rs {mean_lnpv:.1f} Lakhs")
        print(f"  Range: Rs {min_lnpv:.1f}L - Rs {max_lnpv:.1f}L")
        print()

    print("=" * 60)
    print("Baseline calculation complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
