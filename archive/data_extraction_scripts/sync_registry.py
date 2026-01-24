#!/usr/bin/env python3
"""
Sync Registry Script - Synchronize parameters_unified.csv → parameter_registry_v3.py

This script reads verified parameter values from the unified CSV and generates
updates for parameter_registry_v3.py.

Usage:
    python sync_registry.py --diff                  # Show proposed changes (dry run)
    python sync_registry.py --apply                 # Apply changes to registry
    python sync_registry.py --export registry.json  # Export changes as JSON
    python sync_registry.py --only-verified         # Only sync CONSISTENT parameters

Flow:
    parameters_unified.csv (SSOT for verification)
           ↓
    sync_registry.py (this script)
           ↓
    parameter_registry_v3.py (SSOT for model)
           ↓
    economic_core_v4.py (imports from registry)
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple

import pandas as pd

# =============================================================================
# CONFIGURATION
# =============================================================================

CSV_PATH = Path('parameters_unified.csv')
REGISTRY_PATH = Path('model/parameter_registry_v3.py')

# Mapping from CSV canonical_name to registry variable name
# Most are the same, but some need mapping
CANONICAL_TO_REGISTRY = {
    'MINCER_RETURN_HS': 'MINCER_RETURN_HS',
    'MINCER_RETURN_SECONDARY': 'MINCER_RETURN_SECONDARY',
    'EXPERIENCE_LINEAR': 'EXPERIENCE_LINEAR',
    'EXPERIENCE_QUAD': 'EXPERIENCE_QUAD',
    'BASELINE_WAGE_URBAN_MALE_SECONDARY_10YR': 'BASELINE_WAGE_URBAN_MALE_SECONDARY',
    'BASELINE_WAGE_URBAN_FEMALE_SECONDARY_10YR': 'BASELINE_WAGE_URBAN_FEMALE_SECONDARY',
    'BASELINE_WAGE_RURAL_MALE_SECONDARY_10YR': 'BASELINE_WAGE_RURAL_MALE_SECONDARY',
    'BASELINE_WAGE_RURAL_FEMALE_SECONDARY_10YR': 'BASELINE_WAGE_RURAL_FEMALE_SECONDARY',
    'FORMAL_MULTIPLIER': 'FORMAL_MULTIPLIER',
    'P_FORMAL_HIGHER_SECONDARY': 'P_FORMAL_HIGHER_SECONDARY',
    'P_FORMAL_SECONDARY': 'P_FORMAL_SECONDARY',
    'P_FORMAL_APPRENTICE': 'P_FORMAL_APPRENTICE',
    'SOCIAL_DISCOUNT_RATE': 'SOCIAL_DISCOUNT_RATE',
    'REAL_WAGE_GROWTH': 'REAL_WAGE_GROWTH',
    'WORKING_LIFE_FORMAL': 'WORKING_LIFE_FORMAL',
    'WORKING_LIFE_INFORMAL': 'WORKING_LIFE_INFORMAL',
    'VOCATIONAL_PREMIUM': 'VOCATIONAL_PREMIUM',
    'APPRENTICE_COMPLETION_RATE': 'APPRENTICE_COMPLETION_RATE',
    'APPRENTICE_STIPEND_MONTHLY': 'APPRENTICE_STIPEND',
    'RTE_TEST_SCORE_GAIN': 'RTE_TEST_SCORE_GAIN',
    'RTE_EQUIVALENT_YEARS': 'TEST_SCORE_TO_YEARS',
    'RTE_SEAT_FILL_RATE': 'RTE_SEAT_FILL_RATE',
    'COUNTERFACTUAL_SCHOOLING': 'COUNTERFACTUAL_SCHOOLING',
}


# =============================================================================
# LOAD DATA
# =============================================================================

def load_csv() -> pd.DataFrame:
    """Load parameters_unified.csv."""
    try:
        df = pd.read_csv(CSV_PATH)
        print(f"✓ Loaded {len(df)} parameters from {CSV_PATH}")
        return df
    except FileNotFoundError:
        print(f"❌ CSV not found: {CSV_PATH}")
        sys.exit(1)


def load_registry() -> str:
    """Load registry file content."""
    try:
        with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"✓ Loaded registry from {REGISTRY_PATH}")
        return content
    except FileNotFoundError:
        print(f"❌ Registry not found: {REGISTRY_PATH}")
        sys.exit(1)


def parse_registry_parameters(content: str) -> Dict[str, Dict]:
    """
    Parse Parameter dataclass instances from registry.

    Returns:
        Dict[variable_name] -> {value, tier, sensitivity_range, source, etc.}
    """
    params = {}

    # Pattern to match Parameter(...) blocks
    # This is a simplified parser - handles most common cases
    pattern = r'(\w+)\s*=\s*Parameter\(\s*([^)]+(?:\([^)]*\)[^)]*)*)\)'

    for match in re.finditer(pattern, content, re.MULTILINE | re.DOTALL):
        var_name = match.group(1)
        param_content = match.group(2)

        # Extract value=... using regex
        value_match = re.search(r'value\s*=\s*([\d.eE+-]+)', param_content)
        tier_match = re.search(r'tier\s*=\s*(\d+)', param_content)
        range_match = re.search(r'sensitivity_range\s*=\s*\(([\d.eE+-]+)\s*,\s*([\d.eE+-]+)\)', param_content)

        if value_match:
            params[var_name] = {
                'value': float(value_match.group(1)),
                'tier': int(tier_match.group(1)) if tier_match else None,
                'sensitivity_min': float(range_match.group(1)) if range_match else None,
                'sensitivity_max': float(range_match.group(2)) if range_match else None,
            }

    print(f"  Parsed {len(params)} parameters from registry")
    return params


# =============================================================================
# COMPARE AND GENERATE DIFF
# =============================================================================

def compare_values(csv_value, registry_value, tolerance=0.001) -> Tuple[bool, float]:
    """
    Compare two values with tolerance.

    Returns:
        (is_different, percent_difference)
    """
    if csv_value is None or registry_value is None:
        return False, 0.0

    try:
        csv_val = float(csv_value)
        reg_val = float(registry_value)
    except (ValueError, TypeError):
        return False, 0.0

    if reg_val == 0:
        return csv_val != 0, 100.0 if csv_val != 0 else 0.0

    pct_diff = abs(csv_val - reg_val) / abs(reg_val) * 100
    is_different = pct_diff > tolerance * 100

    return is_different, pct_diff


def generate_diff(df: pd.DataFrame, registry_params: Dict,
                  only_verified: bool = False) -> List[Dict]:
    """
    Generate list of proposed changes.

    Args:
        df: Unified CSV DataFrame
        registry_params: Parsed registry parameters
        only_verified: Only include CONSISTENT parameters

    Returns:
        List of change dicts
    """
    changes = []

    for _, row in df.iterrows():
        canonical_name = row.get('canonical_name')
        if not canonical_name or pd.isna(canonical_name):
            continue

        # Skip non-verified if only_verified flag set
        if only_verified:
            status = row.get('verification_status', '')
            if status != 'CONSISTENT':
                continue

        # Get registry variable name
        registry_var = CANONICAL_TO_REGISTRY.get(canonical_name)
        if not registry_var or registry_var not in registry_params:
            continue

        csv_value = row.get('value')
        registry_data = registry_params[registry_var]
        registry_value = registry_data.get('value')

        is_different, pct_diff = compare_values(csv_value, registry_value)

        if is_different:
            changes.append({
                'canonical_name': canonical_name,
                'registry_var': registry_var,
                'csv_value': csv_value,
                'registry_value': registry_value,
                'pct_diff': round(pct_diff, 2),
                'verification_status': row.get('verification_status', 'UNKNOWN'),
                'confidence_score': row.get('confidence_score', 0),
                'source': row.get('primary_source_doc', ''),
            })

    return changes


def display_diff(changes: List[Dict]):
    """Display proposed changes in human-readable format."""
    if not changes:
        print("\n✓ No changes detected - CSV and registry values match")
        return

    print("\n" + "=" * 80)
    print("PROPOSED CHANGES")
    print("=" * 80)
    print(f"Found {len(changes)} parameter(s) with different values\n")

    for i, change in enumerate(changes, 1):
        status_symbol = '✓' if change['verification_status'] == 'CONSISTENT' else '?'

        print(f"{i}. {change['canonical_name']} ({change['registry_var']})")
        print(f"   CSV Value:      {change['csv_value']}")
        print(f"   Registry Value: {change['registry_value']}")
        print(f"   Difference:     {change['pct_diff']}%")
        print(f"   Status:         {status_symbol} {change['verification_status']} "
              f"(confidence: {change['confidence_score']}%)")
        print(f"   Source:         {change['source']}")
        print()

    print("=" * 80)
    print("To apply these changes: python sync_registry.py --apply")
    print("=" * 80)


# =============================================================================
# APPLY CHANGES
# =============================================================================

def apply_changes(changes: List[Dict], content: str, backup: bool = True) -> str:
    """
    Apply changes to registry content.

    Args:
        changes: List of change dicts
        content: Original registry content
        backup: Create backup before modifying

    Returns:
        Modified content
    """
    if not changes:
        print("No changes to apply")
        return content

    # Create backup
    if backup:
        backup_path = REGISTRY_PATH.with_suffix('.py.backup')
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Created backup: {backup_path}")

    modified_content = content
    applied = 0

    for change in changes:
        registry_var = change['registry_var']
        new_value = change['csv_value']
        old_value = change['registry_value']

        # Find and replace value=X.XXX pattern for this parameter
        # This is a simplified approach - works for most cases

        # Pattern: find the parameter block and update value
        # We look for: PARAM_NAME = Parameter(... value=OLD_VALUE ...
        pattern = rf'({registry_var}\s*=\s*Parameter\([^)]*value\s*=\s*){re.escape(str(old_value))}'

        replacement = rf'\g<1>{new_value}'

        new_content, count = re.subn(pattern, replacement, modified_content, count=1)

        if count > 0:
            modified_content = new_content
            applied += 1
            print(f"  ✓ Updated {registry_var}: {old_value} → {new_value}")
        else:
            print(f"  ⚠ Could not update {registry_var} (pattern not found)")

    # Add update timestamp to header
    today = datetime.now().strftime('%Y-%m-%d')
    modified_content = re.sub(
        r'(VERSION:\s*[\d.]+\s*\n)(UPDATED:)',
        rf'\1UPDATED: {today} (sync_registry.py update)\nPREVIOUS UPDATE: ',
        modified_content
    )

    print(f"\n✓ Applied {applied}/{len(changes)} changes")

    return modified_content


def save_registry(content: str):
    """Save modified registry content."""
    with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Saved updated registry to {REGISTRY_PATH}")


# =============================================================================
# EXPORT
# =============================================================================

def export_changes(changes: List[Dict], output_path: str):
    """Export changes to JSON file."""
    export_data = {
        'generated_at': datetime.now().isoformat(),
        'source_csv': str(CSV_PATH),
        'target_registry': str(REGISTRY_PATH),
        'changes_count': len(changes),
        'changes': changes
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, indent=2)

    print(f"✓ Exported {len(changes)} changes to {output_path}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Sync parameters_unified.csv → parameter_registry_v3.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Show proposed changes (dry run)
  python sync_registry.py --diff

  # Show only verified parameter changes
  python sync_registry.py --diff --only-verified

  # Apply changes to registry
  python sync_registry.py --apply

  # Export changes to JSON
  python sync_registry.py --export changes.json
        """
    )

    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('--diff', action='store_true',
                           help='Show proposed changes (dry run)')
    mode_group.add_argument('--apply', action='store_true',
                           help='Apply changes to registry')
    mode_group.add_argument('--export', type=str, metavar='FILE',
                           help='Export changes to JSON file')

    parser.add_argument('--only-verified', action='store_true',
                       help='Only sync CONSISTENT parameters')
    parser.add_argument('--no-backup', action='store_true',
                       help='Skip creating backup before apply')

    args = parser.parse_args()

    # Load data
    print("\n" + "=" * 60)
    print("SYNC REGISTRY")
    print("=" * 60 + "\n")

    df = load_csv()
    registry_content = load_registry()
    registry_params = parse_registry_parameters(registry_content)

    # Generate diff
    changes = generate_diff(df, registry_params, only_verified=args.only_verified)

    # Execute mode
    if args.diff:
        display_diff(changes)

    elif args.apply:
        if not changes:
            print("\n✓ No changes to apply")
            return

        display_diff(changes)

        # Confirm
        try:
            confirm = input(f"\nApply {len(changes)} changes to registry? [y/N]: ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nCancelled")
            return

        if confirm != 'y':
            print("Cancelled")
            return

        modified_content = apply_changes(changes, registry_content, backup=not args.no_backup)
        save_registry(modified_content)

        print("\n" + "=" * 60)
        print("SYNC COMPLETE")
        print("=" * 60)
        print("\nNext steps:")
        print("  1. Review changes in parameter_registry_v3.py")
        print("  2. Run: python -c \"from model.parameter_registry_v3 import *; print('Import OK')\"")
        print("  3. Run tests if available")

    elif args.export:
        export_changes(changes, args.export)


if __name__ == '__main__':
    main()
