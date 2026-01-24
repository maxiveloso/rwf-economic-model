"""
RWF Economic Impact Model - Sensitivity Analysis v2.0
======================================================

A consolidated sensitivity analysis module that performs:
1. One-at-a-time (OAT) Tornado analysis for parameter ranking
2. Break-even analysis to find threshold values
3. Registry update to persist sensitivity metrics

Author: RWF Economic Impact Analysis Team
Version: 2.0 (January 2026)
"""

import numpy as np
import pandas as pd
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional
from datetime import datetime
import os
import sys
import argparse

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.economic_core_v4 import (
    LifetimeNPVCalculator, ParameterRegistry, 
    Gender, Location, Region, Intervention
)
from model.parameter_registry_v3 import Parameter

# ============================================================================
# CONFIGURATION
# ============================================================================

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Parameters to exclude from sensitivity analysis
EXCLUDED_PARAMS = {
    # Deprecated parameters
    'RTE_INITIAL_PREMIUM',
    'VOCATIONAL_PREMIUM', 
    'APPRENTICE_YEAR_0_OPPORTUNITY_COST',
    'WORKING_LIFE_INFORMAL',
    # Fixed structural parameters
    'LABOR_MARKET_ENTRY_AGE',
    'WORKING_LIFE_FORMAL',
}

# Parameter to intervention mapping
RTE_ONLY_PARAMS = {
    'RTE_TEST_SCORE_GAIN',
    'TEST_SCORE_TO_YEARS',
    'P_FORMAL_HIGHER_SECONDARY',
    'P_FORMAL_RTE',  # NEW Jan 2026: RTE-specific formal entry
}

APPRENTICESHIP_ONLY_PARAMS = {
    'APPRENTICE_INITIAL_PREMIUM',
    'APPRENTICE_DECAY_HALFLIFE',
    'APPRENTICE_STIPEND_MONTHLY',
    'P_FORMAL_APPRENTICE',
    'P_FORMAL_NO_TRAINING',
}

BOTH_INTERVENTIONS_PARAMS = {
    'MINCER_RETURN_HS',
    'EXPERIENCE_LINEAR',
    'EXPERIENCE_QUAD',
    'FORMAL_MULTIPLIER',
    'REAL_WAGE_GROWTH',  # DEPRECATED but kept for backward compat
    'REAL_WAGE_GROWTH_FORMAL',  # NEW Jan 2026
    'REAL_WAGE_GROWTH_INFORMAL',  # NEW Jan 2026
    'SOCIAL_DISCOUNT_RATE',
    'P_FORMAL_SECONDARY',
}


# ============================================================================
# PARAMETER INVENTORY
# ============================================================================

def get_active_parameters(registry: ParameterRegistry) -> List[Tuple[str, 'Parameter']]:
    """
    Extract all non-deprecated, numeric parameters with sensitivity ranges.
    
    Returns:
        List of tuples: [(param_name, Parameter object), ...]
    """
    active_params = []
    
    for attr_name in dir(registry):
        if attr_name.startswith('_') or attr_name in EXCLUDED_PARAMS:
            continue
        
        attr = getattr(registry, attr_name)
        
        # Check if it's a Parameter with min/max values
        if hasattr(attr, 'value') and hasattr(attr, 'min_val') and hasattr(attr, 'max_val'):
            # Skip deprecated params based on description
            if hasattr(attr, 'description') and 'DEPRECATED' in str(attr.description).upper():
                continue
            
            active_params.append((attr_name, attr))
    
    return active_params


def affects_intervention(param_name: str, intervention: Intervention) -> bool:
    """Check if a parameter affects a given intervention."""
    if intervention == Intervention.RTE:
        if param_name in APPRENTICESHIP_ONLY_PARAMS:
            return False
        return True
    else:  # Apprenticeship
        if param_name in RTE_ONLY_PARAMS:
            return False
        return True


# ============================================================================
# TORNADO (OAT) ANALYSIS
# ============================================================================

def run_tornado_analysis(
    intervention: Intervention,
    gender: Gender = Gender.MALE,
    location: Location = Location.URBAN,
    region: Region = Region.WEST
) -> pd.DataFrame:
    """
    One-at-a-time sensitivity analysis for tornado diagram.
    
    For each parameter:
    1. Set all params to baseline values
    2. Set param to min_val → calculate NPV_low
    3. Set param to max_val → calculate NPV_high
    4. Record delta_npv = |NPV_high - NPV_low|
    
    Args:
        intervention: RTE or APPRENTICESHIP
        gender: Reference demographic gender
        location: Reference demographic location  
        region: Reference demographic region
        
    Returns:
        DataFrame with columns: parameter_name, tier, baseline_value, min_value,
        max_value, npv_at_min, npv_at_max, delta_npv, pct_swing, direction, rank
    """
    results = []
    
    # Get baseline NPV
    base_registry = ParameterRegistry()
    base_calc = LifetimeNPVCalculator(params=base_registry)
    base_result = base_calc.calculate_lnpv(intervention, gender, location, region)
    baseline_npv = base_result['lnpv']
    
    print(f"\n{'='*60}")
    print(f"Tornado Analysis: {intervention.value.upper()}")
    print(f"Reference: {gender.value} {location.value} {region.value}")
    print(f"Baseline NPV: Rs {baseline_npv:,.0f}")
    print(f"{'='*60}\n")
    
    # Get active parameters
    active_params = get_active_parameters(base_registry)
    
    for param_name, base_param in active_params:
        # Skip if parameter doesn't affect this intervention
        if not affects_intervention(param_name, intervention):
            continue
        
        # Test at min value
        registry_min = ParameterRegistry()
        param_min = getattr(registry_min, param_name)
        param_min.value = base_param.min_val
        calc_min = LifetimeNPVCalculator(params=registry_min)
        result_min = calc_min.calculate_lnpv(intervention, gender, location, region)
        npv_at_min = result_min['lnpv']
        
        # Test at max value  
        registry_max = ParameterRegistry()
        param_max = getattr(registry_max, param_name)
        param_max.value = base_param.max_val
        calc_max = LifetimeNPVCalculator(params=registry_max)
        result_max = calc_max.calculate_lnpv(intervention, gender, location, region)
        npv_at_max = result_max['lnpv']
        
        # Calculate metrics
        delta_npv = abs(npv_at_max - npv_at_min)
        pct_swing = (delta_npv / abs(baseline_npv)) * 100 if baseline_npv != 0 else 0
        direction = "positive" if npv_at_max > npv_at_min else "negative"

        # Calculate NPV elasticity: E = [(NPV_high - NPV_low) / NPV_base] / [(p_high - p_low) / p_base]
        # This measures the relative sensitivity: % change in NPV per % change in parameter
        npv_elasticity = None
        if baseline_npv != 0 and base_param.value != 0:
            npv_pct_change = (npv_at_max - npv_at_min) / abs(baseline_npv)
            param_pct_change = (base_param.max_val - base_param.min_val) / abs(base_param.value)
            if param_pct_change != 0:
                npv_elasticity = npv_pct_change / param_pct_change

        results.append({
            'parameter_name': param_name,
            'tier': base_param.tier,
            'baseline_value': base_param.value,
            'min_value': base_param.min_val,
            'max_value': base_param.max_val,
            'npv_at_min': npv_at_min,
            'npv_at_max': npv_at_max,
            'delta_npv': delta_npv,
            'pct_swing': pct_swing,
            'npv_elasticity': npv_elasticity,
            'direction': direction,
            'affects_intervention': True,
            'intervention': intervention.value,
        })

        elasticity_str = f"{npv_elasticity:.2f}" if npv_elasticity is not None else "N/A"
        print(f"  {param_name}: delta={delta_npv:,.0f} ({pct_swing:.1f}%) elasticity={elasticity_str}")
    
    # Create DataFrame and add ranks
    df = pd.DataFrame(results)
    df = df.sort_values('delta_npv', ascending=False).reset_index(drop=True)
    df['rank'] = range(1, len(df) + 1)
    
    return df


# ============================================================================
# BREAK-EVEN ANALYSIS
# ============================================================================

def run_breakeven_analysis(
    tornado_df: pd.DataFrame,
    intervention: Intervention,
    top_n: int = 10,
    gender: Gender = Gender.MALE,
    location: Location = Location.URBAN,
    region: Region = Region.WEST,
) -> pd.DataFrame:
    """
    Find parameter values where NPV crosses key thresholds.
    
    For each parameter in top_n by delta_npv:
    - Find value where NPV = 0 (break-even point)
    - Calculate margin = (baseline - break_even) / baseline * 100
    
    Args:
        tornado_df: Results from run_tornado_analysis()
        intervention: RTE or APPRENTICESHIP
        top_n: Number of top parameters to analyze
        gender, location, region: Reference demographic
        
    Returns:
        DataFrame with break-even thresholds and margins
    """
    from scipy.optimize import brentq
    
    results = []
    top_params = tornado_df.head(top_n)
    
    print(f"\n{'='*60}")
    print(f"Break-even Analysis: {intervention.value.upper()} (Top {top_n})")
    print(f"{'='*60}\n")
    
    for _, row in top_params.iterrows():
        param_name = row['parameter_name']
        baseline = row['baseline_value']
        min_val = row['min_value']
        max_val = row['max_value']
        
        def npv_for_param_value(val):
            """Helper function to calculate NPV for a given parameter value."""
            registry = ParameterRegistry()
            param = getattr(registry, param_name)
            param.value = val
            calc = LifetimeNPVCalculator(params=registry)
            result = calc.calculate_lnpv(intervention, gender, location, region)
            return result['lnpv']
        
        # Find break-even (NPV = 0)
        npv_zero_threshold = None
        margin_pct = None
        interpretation = ""
        
        try:
            npv_min = npv_for_param_value(min_val)
            npv_max = npv_for_param_value(max_val)
            
            # Check if NPV crosses zero within range
            if npv_min * npv_max < 0:
                # Zero crossing exists
                npv_zero_threshold = brentq(npv_for_param_value, min_val, max_val)
                margin_pct = ((baseline - npv_zero_threshold) / baseline) * 100
                
                if margin_pct > 0:
                    interpretation = f"Parameter can decrease by {abs(margin_pct):.0f}% before NPV < 0"
                else:
                    interpretation = f"Parameter must increase by {abs(margin_pct):.0f}% for NPV > 0"
            elif npv_min > 0 and npv_max > 0:
                interpretation = "NPV always positive within range"
                margin_pct = 100  # Robust
            else:
                interpretation = "NPV always negative within range - check baseline"
                margin_pct = 0
                
        except Exception as e:
            interpretation = f"Could not find break-even: {str(e)}"
        
        results.append({
            'parameter_name': param_name,
            'intervention': intervention.value,
            'baseline_value': baseline,
            'npv_zero_threshold': npv_zero_threshold,
            'margin_pct': margin_pct,
            'interpretation': interpretation,
            'rank': row['rank'],
        })
        
        print(f"  {param_name}: margin={margin_pct:.1f}% - {interpretation[:50]}...")
    
    return pd.DataFrame(results)


# ============================================================================
# REGISTRY UPDATE
# ============================================================================

def update_parameter_sources_csv(
    tornado_rte: pd.DataFrame,
    tornado_app: pd.DataFrame,
    breakeven: pd.DataFrame,
    csv_path: str = "data/param_sources/Parameter_Sources_Master.csv"
) -> None:
    """
    Add/update 4 columns in Parameter_Sources_Master.csv:
    - sensitivity_rank: min(rank_rte, rank_app) - highest impact
    - npv_impact_pct: max(pct_swing_rte, pct_swing_app) - worst case
    - Column 19 (npv_elasticity): NPV elasticity E = (ΔNPV/NPV_base) / (Δp/p_base)
    - breakeven_margin: margin from break-even analysis (or "N/A")

    NPV Elasticity Formula:
    E = [(NPV_high - NPV_low) / NPV_base] / [(p_high - p_low) / p_base]

    Interpretation:
    - |E| > 1: NPV is elastic (more than proportional response)
    - |E| < 1: NPV is inelastic (less than proportional response)
    - E > 0: Higher parameter value → higher NPV (positive relationship)
    - E < 0: Higher parameter value → lower NPV (negative relationship)

    Args:
        tornado_rte: Tornado results for RTE
        tornado_app: Tornado results for Apprenticeship
        breakeven: Break-even results
        csv_path: Path to Parameter_Sources_Master.csv
    """
    print(f"\n{'='*60}")
    print("Updating Parameter_Sources_Master.csv")
    print(f"{'='*60}\n")

    # Read existing CSV
    df = pd.read_csv(csv_path)

    # Create lookup dicts from tornado results (now including elasticity)
    rte_cols = ['rank', 'pct_swing', 'npv_elasticity']
    app_cols = ['rank', 'pct_swing', 'npv_elasticity']

    # Check which columns exist
    rte_available = [c for c in rte_cols if c in tornado_rte.columns]
    app_available = [c for c in app_cols if c in tornado_app.columns]

    rte_lookup = tornado_rte.set_index('parameter_name')[rte_available].to_dict('index')
    app_lookup = tornado_app.set_index('parameter_name')[app_available].to_dict('index')

    # Create break-even lookup (combine both interventions)
    breakeven_lookup = {}
    if breakeven is not None and len(breakeven) > 0:
        for _, row in breakeven.iterrows():
            param = row['parameter_name']
            if param not in breakeven_lookup or row['margin_pct'] is not None:
                breakeven_lookup[param] = row['margin_pct']

    # Initialize new columns
    if 'sensitivity_rank' not in df.columns:
        df['sensitivity_rank'] = None
    if 'npv_impact_pct' not in df.columns:
        df['npv_impact_pct'] = None
    # Column 19 is labeled 'Column 19' in the CSV for elasticity
    if 'Column 19' not in df.columns:
        df['Column 19'] = None
    if 'breakeven_margin' not in df.columns:
        df['breakeven_margin'] = None

    # Update each row
    updated_count = 0
    for idx, row in df.iterrows():
        param_name = row['parameter_name']

        rte_data = rte_lookup.get(param_name, {})
        app_data = app_lookup.get(param_name, {})

        # Calculate sensitivity_rank (min of both, or whichever exists)
        ranks = []
        if 'rank' in rte_data:
            ranks.append(rte_data['rank'])
        if 'rank' in app_data:
            ranks.append(app_data['rank'])

        if ranks:
            df.at[idx, 'sensitivity_rank'] = min(ranks)
            updated_count += 1

        # Calculate npv_impact_pct (max of both)
        swings = []
        if 'pct_swing' in rte_data:
            swings.append(rte_data['pct_swing'])
        if 'pct_swing' in app_data:
            swings.append(app_data['pct_swing'])

        if swings:
            df.at[idx, 'npv_impact_pct'] = round(max(swings), 1)

        # Calculate NPV elasticity (Column 19)
        # Use max absolute elasticity from either intervention
        elasticities = []
        if 'npv_elasticity' in rte_data and rte_data['npv_elasticity'] is not None:
            elasticities.append(rte_data['npv_elasticity'])
        if 'npv_elasticity' in app_data and app_data['npv_elasticity'] is not None:
            elasticities.append(app_data['npv_elasticity'])

        if elasticities:
            # Use the elasticity with the largest absolute value
            max_elasticity = max(elasticities, key=abs)
            df.at[idx, 'Column 19'] = round(max_elasticity, 2)

        # Add breakeven margin
        if param_name in breakeven_lookup:
            margin = breakeven_lookup[param_name]
            df.at[idx, 'breakeven_margin'] = round(margin, 1) if margin is not None else "N/A"
        else:
            df.at[idx, 'breakeven_margin'] = "N/A"

    # Save updated CSV
    df.to_csv(csv_path, index=False)
    print(f"  Updated {updated_count} parameters in {csv_path}")
    print(f"  NPV elasticity values added to 'Column 19'")


# ============================================================================
# MAIN CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="RWF Sensitivity Analysis v2.0",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python sensitivity_analysis_v2.py --tornado --intervention rte
  python sensitivity_analysis_v2.py --tornado --intervention apprenticeship
  python sensitivity_analysis_v2.py --breakeven --top-n 10
  python sensitivity_analysis_v2.py --all
        """
    )
    
    parser.add_argument('--tornado', action='store_true', 
                        help='Run tornado (OAT) analysis')
    parser.add_argument('--breakeven', action='store_true',
                        help='Run break-even analysis')
    parser.add_argument('--update-csv', action='store_true',
                        help='Update Parameter_Sources_Master.csv')
    parser.add_argument('--all', action='store_true',
                        help='Run all analyses')
    parser.add_argument('--intervention', choices=['rte', 'apprenticeship', 'both'],
                        default='both', help='Which intervention to analyze')
    parser.add_argument('--top-n', type=int, default=10,
                        help='Number of top parameters for break-even (default: 10)')
    
    args = parser.parse_args()
    
    # Default to running all if no specific analysis requested
    if not any([args.tornado, args.breakeven, args.update_csv, args.all]):
        args.all = True
    
    tornado_rte = None
    tornado_app = None
    breakeven_results = None
    
    # Run tornado analysis
    if args.tornado or args.all:
        if args.intervention in ['rte', 'both']:
            print("\n" + "="*70)
            print("RUNNING TORNADO ANALYSIS: RTE")
            print("="*70)
            tornado_rte = run_tornado_analysis(Intervention.RTE)
            tornado_rte.to_csv(os.path.join(OUTPUT_DIR, 'sensitivity_tornado_rte.csv'), index=False)
            print(f"\nSaved: {OUTPUT_DIR}/sensitivity_tornado_rte.csv")
        
        if args.intervention in ['apprenticeship', 'both']:
            print("\n" + "="*70)
            print("RUNNING TORNADO ANALYSIS: APPRENTICESHIP")
            print("="*70)
            tornado_app = run_tornado_analysis(Intervention.APPRENTICESHIP)
            tornado_app.to_csv(os.path.join(OUTPUT_DIR, 'sensitivity_tornado_apprenticeship.csv'), index=False)
            print(f"\nSaved: {OUTPUT_DIR}/sensitivity_tornado_apprenticeship.csv")
    
    # Run break-even analysis
    if args.breakeven or args.all:
        # Load tornado results if not already in memory
        if tornado_rte is None:
            tornado_path = os.path.join(OUTPUT_DIR, 'sensitivity_tornado_rte.csv')
            if os.path.exists(tornado_path):
                tornado_rte = pd.read_csv(tornado_path)
        if tornado_app is None:
            tornado_path = os.path.join(OUTPUT_DIR, 'sensitivity_tornado_apprenticeship.csv')
            if os.path.exists(tornado_path):
                tornado_app = pd.read_csv(tornado_path)
        
        breakeven_list = []
        if tornado_rte is not None:
            print("\n" + "="*70)
            print("RUNNING BREAK-EVEN ANALYSIS: RTE")
            print("="*70)
            be_rte = run_breakeven_analysis(tornado_rte, Intervention.RTE, args.top_n)
            breakeven_list.append(be_rte)
        
        if tornado_app is not None:
            print("\n" + "="*70)
            print("RUNNING BREAK-EVEN ANALYSIS: APPRENTICESHIP")
            print("="*70)
            be_app = run_breakeven_analysis(tornado_app, Intervention.APPRENTICESHIP, args.top_n)
            breakeven_list.append(be_app)
        
        if breakeven_list:
            breakeven_results = pd.concat(breakeven_list, ignore_index=True)
            breakeven_results.to_csv(os.path.join(OUTPUT_DIR, 'sensitivity_breakeven.csv'), index=False)
            print(f"\nSaved: {OUTPUT_DIR}/sensitivity_breakeven.csv")
    
    # Update CSV
    if args.update_csv or args.all:
        # Load results if needed
        if tornado_rte is None:
            tornado_path = os.path.join(OUTPUT_DIR, 'sensitivity_tornado_rte.csv')
            if os.path.exists(tornado_path):
                tornado_rte = pd.read_csv(tornado_path)
        if tornado_app is None:
            tornado_path = os.path.join(OUTPUT_DIR, 'sensitivity_tornado_apprenticeship.csv')
            if os.path.exists(tornado_path):
                tornado_app = pd.read_csv(tornado_path)
        if breakeven_results is None:
            breakeven_path = os.path.join(OUTPUT_DIR, 'sensitivity_breakeven.csv')
            if os.path.exists(breakeven_path):
                breakeven_results = pd.read_csv(breakeven_path)
        
        if tornado_rte is not None and tornado_app is not None:
            print("\n" + "="*70)
            print("UPDATING PARAMETER_SOURCES_MASTER.CSV")
            print("="*70)
            update_parameter_sources_csv(
                tornado_rte, 
                tornado_app,
                breakeven_results if breakeven_results is not None else pd.DataFrame()
            )
    
    print("\n" + "="*70)
    print("SENSITIVITY ANALYSIS COMPLETE")
    print("="*70)
    
    # Print summary
    if tornado_rte is not None:
        print(f"\nRTE Top 5 Parameters by NPV Impact:")
        print(tornado_rte[['rank', 'parameter_name', 'pct_swing']].head().to_string(index=False))
    
    if tornado_app is not None:
        print(f"\nApprenticeship Top 5 Parameters by NPV Impact:")
        print(tornado_app[['rank', 'parameter_name', 'pct_swing']].head().to_string(index=False))


if __name__ == "__main__":
    main()
