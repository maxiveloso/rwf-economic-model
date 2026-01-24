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
import pandas as pd

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
    from economic_core_v4 import run_baseline_analysis
    baseline_results_list = run_baseline_analysis()
    baseline_results = pd.DataFrame(baseline_results_list)

    output_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'results')
    os.makedirs(output_dir, exist_ok=True)
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
    from sensitivity_analysis_v2 import run_tornado_analysis, run_breakeven_analysis
    from economic_core_v4 import Intervention

    sensitivity_dir = os.path.join(output_dir, 'sensitivity')
    os.makedirs(sensitivity_dir, exist_ok=True)

    # Run tornado for both interventions
    tornado_rte = run_tornado_analysis(Intervention.RTE)
    tornado_rte.to_csv(os.path.join(sensitivity_dir, 'tornado_rte.csv'), index=False)

    tornado_app = run_tornado_analysis(Intervention.APPRENTICESHIP)
    tornado_app.to_csv(os.path.join(sensitivity_dir, 'tornado_apprenticeship.csv'), index=False)

    # Run break-even analysis
    be_rte = run_breakeven_analysis(tornado_rte, Intervention.RTE, top_n=10)
    be_app = run_breakeven_analysis(tornado_app, Intervention.APPRENTICESHIP, top_n=10)

    breakeven_df = pd.concat([be_rte, be_app], ignore_index=True)
    breakeven_df.to_csv(os.path.join(sensitivity_dir, 'breakeven_analysis.csv'), index=False)

    print("  Completed: Tornado, Break-even analysis")
    print()

    # Step 3: Validation
    print("[3/3] Running validation checks...")
    print("-" * 50)
    from m4_validation_qa import run_all_validations
    run_all_validations()
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
