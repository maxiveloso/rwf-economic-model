#!/usr/bin/env python3
"""
Validate calculated parameters and flag discrepancies
"""
import csv
import math

print("="*80)
print("PARAMETER CALCULATION VALIDATION REPORT")
print("="*80)

csv_path = "/Users/maximvf/Library/CloudStorage/GoogleDrive-maxiveloso@gmail.com/Mi unidad/Worklife/Applications/RWF/RWF_Lifetime_Economic_Benefits_Estimation/rwf_model/parameter_decomposition_enhanced.csv"

# Read the enhanced decomposition file
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"\nTotal parameters: {len(rows)}")
print(f"\n{'='*80}")

# Track issues
critical_issues = []
warnings = []
validated = []

for row in rows:
    param_name = row['Parameter_Name']
    derivation_type = row['Derivation_Type']
    registry_value = row['Registry_Value']
    calculated_value = row['Calculated_Value']
    discrepancy = row['Discrepancy_Pct']
    verified = row['Verified_Manually']

    print(f"\n{param_name}")
    print(f"  Type: {derivation_type}")
    print(f"  Registry: {registry_value}")
    print(f"  Calculated: {calculated_value}")

    # Parse discrepancy if it exists
    try:
        if discrepancy and discrepancy not in ['N/A', 'TBD']:
            disc_val = float(discrepancy.replace('%', ''))
            print(f"  Discrepancy: {disc_val:.1f}%")

            if disc_val > 10:
                print(f"  ⚠️  CRITICAL: >10% discrepancy")
                critical_issues.append({
                    'parameter': param_name,
                    'discrepancy': disc_val,
                    'registry': registry_value,
                    'calculated': calculated_value,
                    'notes': row['Verification_Notes'][:100]
                })
            elif disc_val > 5:
                print(f"  ⚠️  WARNING: >5% discrepancy")
                warnings.append({
                    'parameter': param_name,
                    'discrepancy': disc_val
                })
            else:
                print(f"  ✓ Acceptable variance")
                validated.append(param_name)
        elif calculated_value == 'TBD':
            print(f"  ⏸️  PENDING: Requires manual extraction")
        else:
            print(f"  ✓ No calculation needed (context parameter)")
            validated.append(param_name)

    except (ValueError, AttributeError):
        print(f"  ⏸️  Cannot validate")

# Summary
print(f"\n{'='*80}")
print("VALIDATION SUMMARY")
print(f"{'='*80}")

print(f"\n✅ VALIDATED: {len(validated)} parameters")
for p in validated:
    print(f"   - {p}")

print(f"\n⚠️  WARNINGS ({len(warnings)} parameters with 5-10% discrepancy):")
for w in warnings:
    print(f"   - {w['parameter']}: {w['discrepancy']:.1f}%")

print(f"\n🚨 CRITICAL ISSUES ({len(critical_issues)} parameters with >10% discrepancy):")
for issue in critical_issues:
    print(f"\n   Parameter: {issue['parameter']}")
    print(f"   Discrepancy: {issue['discrepancy']:.1f}%")
    print(f"   Registry: {issue['registry']}")
    print(f"   Calculated: {issue['calculated']}")
    print(f"   Notes: {issue['notes']}...")

# Key Findings
print(f"\n{'='*80}")
print("KEY FINDINGS")
print(f"{'='*80}")

print("""
1. BASELINE WAGE DISCREPANCY (12%):
   All baseline wages show consistent ~12% discrepancy between claimed
   calculation and actual math. This suggests wages are DIRECT QUOTES
   from PLFS Table 21, not calculated values.

   Example: Urban Male HS
   - Registry claims: 26,105 × (1.058)² = 32,800
   - Actual calculation: 26,105 × 1.119364 = 29,218
   - Difference: 12.3%

   ACTION: Update parameter_registry_v3.py to document these as
   "PLFS Table 21 (direct quote)" not "calculated from Mincer return"

2. APPRENTICE_INITIAL_PREMIUM DISCREPANCY (184%):
   This is DOCUMENTED and INTENTIONAL. Model uses conservative ₹84k
   instead of calculated ₹239k. See parameter_registry_v3.py notes
   for full explanation.

   STATUS: No action needed - this is correct.

3. MINCER_RETURN_HS DISCREPANCY (9.4%):
   Registry uses 5.8% (averaged across demographics) vs calculated 6.4%
   from urban male wages alone. This is expected - registry is more
   conservative.

   STATUS: Acceptable - documents averaging methodology.

4. PARAMETERS REQUIRING MANUAL EXTRACTION:
   - P_FORMAL_HIGHER_SECONDARY (PRIORITY 0)
   - P_FORMAL_NO_TRAINING (PRIORITY 1)

   These need PLFS table identification and manual calculation.
""")

print(f"\n{'='*80}")
print("RECOMMENDATIONS")
print(f"{'='*80}")

print("""
IMMEDIATE:
1. Search PLFS Table 21 for direct wage quotes (32,800; 24,928; 22,880; 15,558)
2. Update parameter_registry_v3.py sources from "calculated" to "direct quote"
3. Extract P_FORMAL_HIGHER_SECONDARY from PLFS employment tables

NEXT STEPS:
4. Extract P_FORMAL_NO_TRAINING with proper filters
5. Create automated test suite for all calculated parameters
6. Add data lineage tracking to prevent future discrepancies
""")

print(f"\n{'='*80}")
print("VALIDATION COMPLETE")
print(f"{'='*80}\n")
