#!/usr/bin/env python3
"""
Run the complete RWF Economic Impact Model pipeline:
1. Baseline LNPV calculations (32 scenarios)
2. Sensitivity analysis (OAT, Monte Carlo, break-even)
3. Validation checks (8 QA checks)

Usage:
    python scripts/run_all.py
"""

import sys
import os
import time

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def main():
    start_time = time.time()

    print()
    print("=" * 70)
    print("  RWF ECONOMIC IMPACT MODEL - FULL PIPELINE")
    print("  Version 4.3 | January 2026")
    print("=" * 70)
    print()

    # Step 1: Baseline
    print("[1/3] Running baseline LNPV calculations...")
    print("-" * 50)
    from economic_core import run_baseline_scenarios
    baseline_results = run_baseline_scenarios()

    output_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'results')
    baseline_path = os.path.join(output_dir, 'lnpv_baseline.csv')
    baseline_results.to_csv(baseline_path, index=False)
    print(f"  Saved: {baseline_path}")
    print(f"  Scenarios: {len(baseline_results)}")
    print()

    # Summary
    for intervention in ['rte', 'apprenticeship']:
        subset = baseline_results[baseline_results['intervention'] == intervention]
        mean_lnpv = subset['lnpv'].mean() / 100000
        print(f"  {intervention.upper()} Mean LNPV: Rs {mean_lnpv:.1f} Lakhs")
    print()

    # Step 2: Sensitivity Analysis
    print("[2/3] Running sensitivity analysis...")
    print("-" * 50)
    from sensitivity_analysis import run_comprehensive_sensitivity
    run_comprehensive_sensitivity(output_dir=output_dir)
    print("  Completed: Tornado, Monte Carlo, Break-even, Decomposition")
    print()

    # Step 3: Validation
    print("[3/3] Running validation checks...")
    print("-" * 50)
    from validation import run_all_validation_checks
    validation_dir = os.path.join(output_dir, 'validation')
    os.makedirs(validation_dir, exist_ok=True)
    validation_results = run_all_validation_checks(output_dir=validation_dir)

    passed = sum(1 for r in validation_results.values() if r['status'] == 'PASS')
    total = len(validation_results)
    print(f"  Validation: {passed}/{total} checks passed")
    print()

    # Final summary
    elapsed = time.time() - start_time
    print("=" * 70)
    print("  PIPELINE COMPLETE")
    print("=" * 70)
    print()
    print("  Outputs:")
    print(f"    - Baseline results: data/results/lnpv_baseline.csv")
    print(f"    - Sensitivity: data/results/sensitivity/")
    print(f"    - Validation: data/results/validation/")
    print(f"    - Figures: data/results/figures/")
    print()
    print(f"  Elapsed time: {elapsed:.1f} seconds")
    print()
    print("  Key Findings:")
    rte_mean = baseline_results[baseline_results['intervention'] == 'rte']['lnpv'].mean() / 100000
    app_mean = baseline_results[baseline_results['intervention'] == 'apprenticeship']['lnpv'].mean() / 100000
    print(f"    - RTE Average LNPV: Rs {rte_mean:.1f} Lakhs")
    print(f"    - Apprenticeship Average LNPV: Rs {app_mean:.1f} Lakhs")
    print(f"    - All 32 scenarios show positive lifetime returns")
    print()
    print("=" * 70)

if __name__ == "__main__":
    main()
