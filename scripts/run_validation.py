#!/usr/bin/env python3
"""
Run all 8 validation checks on the model.

Output: data/results/validation/validation_report.md
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from m4_validation_qa import run_all_validation_checks

def main():
    print("=" * 60)
    print("RWF Economic Impact Model - Validation & QA")
    print("=" * 60)
    print()

    output_dir = os.path.join(
        os.path.dirname(__file__),
        '..', 'data', 'results', 'validation'
    )

    # Run all validation checks
    results = run_all_validation_checks(output_dir=output_dir)

    print()
    print("=" * 60)
    print("Validation Checks Summary")
    print("=" * 60)
    print()

    passed = sum(1 for r in results.values() if r['status'] == 'PASS')
    total = len(results)

    for check_name, result in results.items():
        status = "PASS" if result['status'] == 'PASS' else "FAIL"
        print(f"  [{status}] {check_name}")

    print()
    print(f"Overall: {passed}/{total} checks passed")
    print()

    if passed == total:
        print("All validation checks passed!")
    else:
        print("WARNING: Some validation checks failed. Review output.")

    print("=" * 60)

if __name__ == "__main__":
    main()
