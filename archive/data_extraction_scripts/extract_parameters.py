"""
PARAMETER EXTRACTION & CLASSIFICATION SCRIPT
=============================================

Extracts all 77 parameters from parameter_registry_v3.py into:
1. parameters_master.csv - Single source of truth for all parameter values
2. parameters_derived.csv - Formulas and dependencies for calculated parameters
3. Validation report - Issues and ambiguities for human review

Author: RWF Economic Impact Analysis Team
Date: 2026-01-12
"""

import re
import json
import csv
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from pathlib import Path

# Import the parameter registry
import sys
sys.path.insert(0, str(Path(__file__).parent / 'model'))
from parameter_registry_v3 import *


class ParameterExtractor:
    """Extracts and classifies parameters from parameter_registry_v3.py"""

    def __init__(self):
        self.parameters_extracted = []
        self.formulas_extracted = []
        self.validation_issues = {
            'unclear_classification': [],
            'missing_inputs': [],
            'circular_dependencies': [],
            'registry_only': [],
            'verified_only': []
        }

    def extract_parameter(self, canonical_name: str, param_obj: Parameter) -> Dict:
        """Extract all metadata from a Parameter object"""

        # Basic extraction
        extracted = {
            'canonical_name': canonical_name,
            'display_name': param_obj.name,
            'value': param_obj.value,
            'unit': param_obj.unit,
            'tier': param_obj.tier,
            'sensitivity_min': param_obj.sensitivity_range[0] if param_obj.sensitivity_range else None,
            'sensitivity_max': param_obj.sensitivity_range[1] if param_obj.sensitivity_range else None,
            'sampling_method': param_obj.sampling_method,
            'source_field': param_obj.source,
            'notes_field': param_obj.notes,
            'last_updated': param_obj.last_updated
        }

        # Classify parameter type
        param_type, derivation_type = self.classify_parameter(
            param_obj.source, param_obj.notes
        )
        extracted['parameter_type'] = param_type
        extracted['derivation_type'] = derivation_type

        # Extract source summary (first 200 chars)
        source_summary = param_obj.source[:200] if param_obj.source else ""
        extracted['source_summary'] = source_summary

        # Extract important comments
        registry_notes = self.extract_important_comments(param_obj.notes)
        extracted['registry_notes'] = registry_notes

        return extracted

    def classify_parameter(self, source: str, notes: str) -> Tuple[str, Optional[str]]:
        """
        Classify parameter as direct_quote or derived.

        Rules:
        1. If source contains "Calculated:" → derived
        2. If notes contains formulas (=, ×, ÷, -, +) → derived
        3. Otherwise → direct_quote
        """
        source_lower = source.lower()
        notes_lower = notes.lower()

        # Check for explicit "Calculated" marker
        if 'calculated' in source_lower or 'calculation' in source_lower:
            # Determine complexity
            formula_complexity = self.assess_formula_complexity(source + " " + notes)
            if formula_complexity >= 3:
                return 'derived', 'complex_derived'
            else:
                return 'derived', 'simple_calc'

        # Check for mathematical expressions in notes
        math_patterns = [r'=', r'×', r'÷', r'\*', r'/', r'\+', r'-']
        has_math = any(re.search(pattern, notes) for pattern in math_patterns)

        if has_math and ('formula' in notes_lower or 'calculation' in notes_lower):
            formula_complexity = self.assess_formula_complexity(notes)
            if formula_complexity >= 3:
                return 'derived', 'complex_derived'
            else:
                return 'derived', 'simple_calc'

        # Default: direct quote
        return 'direct_quote', None

    def assess_formula_complexity(self, text: str) -> int:
        """Count number of parameter references in formula"""
        # Look for patterns like: P(Formal), ₹26,105, MINCER_RETURN, etc.
        param_patterns = [
            r'P\([^)]+\)',  # P(Formal), P(App)
            r'₹[\d,]+',      # Currency values
            r'[A-Z_]{3,}',   # UPPERCASE_NAMES
            r'\d+\.\d+%',    # Percentages
        ]

        total_refs = 0
        for pattern in param_patterns:
            matches = re.findall(pattern, text)
            total_refs += len(matches)

        return total_refs

    def extract_important_comments(self, notes: str, max_length: int = 700) -> str:
        """
        Extract key information from notes field.

        Looks for:
        - TIER 1 WEAKNESS / CRITICAL
        - MAJOR FINDING
        - VALIDATED WITH
        - UPDATED / CHANGED FROM
        - Mathematical explanations
        """
        if not notes:
            return ""

        # Keywords indicating important content
        important_markers = [
            'TIER 1',
            'CRITICAL',
            'MAJOR FINDING',
            'VALIDATED',
            'UPDATED',
            'CHANGED FROM',
            'IMPLICATION',
            'WEAKNESS',
            'GAP',
            'RECONCILIATION'
        ]

        # Split into lines
        lines = notes.strip().split('\n')
        important_lines = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Check if line contains important markers
            is_important = any(marker in line.upper() for marker in important_markers)

            if is_important:
                # Clean the line (remove excessive whitespace)
                cleaned = re.sub(r'\s+', ' ', line)
                important_lines.append(cleaned)

        # Join and truncate
        combined = " ".join(important_lines)
        if len(combined) > max_length:
            combined = combined[:max_length-3] + "..."

        return combined if combined else notes[:max_length]

    def extract_formula(self, canonical_name: str, source: str, notes: str) -> Optional[Dict]:
        """
        Extract calculation formula and identify inputs.

        Returns dictionary with:
        - formula: The calculation expression
        - inputs: List of input parameter names
        - input_types: Type of each input (direct/derived)
        """
        combined_text = source + "\n" + notes

        # Look for calculation formulas
        # Pattern 1: "Calculated: X × Y = Z"
        calc_pattern = r'Calculated[:\s]+(.+?)(?:\n|$)'
        match = re.search(calc_pattern, combined_text, re.IGNORECASE)

        if match:
            formula = match.group(1).strip()
        else:
            # Pattern 2: Look for explicit formula in notes
            formula_pattern = r'(?:Formula|Calculation)[:\s]+(.+?)(?:\n|$)'
            match = re.search(formula_pattern, combined_text, re.IGNORECASE)
            if match:
                formula = match.group(1).strip()
            else:
                return None

        # Extract input parameters
        inputs = self.extract_formula_inputs(formula, combined_text)

        if not inputs:
            # Couldn't identify inputs - flag for review
            self.validation_issues['missing_inputs'].append(canonical_name)

        return {
            'parameter_name': canonical_name,
            'formula': formula,
            'inputs': inputs
        }

    def extract_formula_inputs(self, formula: str, context: str) -> List[Dict]:
        """Identify parameter references in formula"""
        inputs = []

        # Common parameter name patterns
        patterns = [
            r'P\(Formal\|[^)]+\)',  # P(Formal|HS), P(Formal|App)
            r'baseline_wage_\w+',    # baseline_wage_urban_male_hs
            r'[A-Z_]{5,}',           # UPPERCASE_PARAMETER_NAMES
        ]

        seen = set()
        for pattern in patterns:
            matches = re.findall(pattern, formula + " " + context)
            for match in matches:
                if match not in seen:
                    seen.add(match)
                    inputs.append({
                        'name': match,
                        'type': 'unknown',  # Will be resolved later
                        'source': ''
                    })

        return inputs

    def extract_all_parameters(self):
        """Extract all parameters from the registry"""

        # Main parameters (individual Parameter objects)
        param_objects = [
            ('MINCER_RETURN_HS', MINCER_RETURN_HS),
            ('EXPERIENCE_LINEAR', EXPERIENCE_LINEAR),
            ('EXPERIENCE_QUAD', EXPERIENCE_QUAD),
            ('FORMAL_MULTIPLIER', FORMAL_MULTIPLIER),
            ('P_FORMAL_HIGHER_SECONDARY', P_FORMAL_HIGHER_SECONDARY),
            ('P_FORMAL_SECONDARY', P_FORMAL_SECONDARY),
            ('P_FORMAL_APPRENTICE', P_FORMAL_APPRENTICE),
            ('REAL_WAGE_GROWTH', REAL_WAGE_GROWTH),
            ('SOCIAL_DISCOUNT_RATE', SOCIAL_DISCOUNT_RATE),
            ('INFLATION_RATE', INFLATION_RATE),
            ('RTE_TEST_SCORE_GAIN', RTE_TEST_SCORE_GAIN),
            ('RTE_EQUIVALENT_YEARS', RTE_EQUIVALENT_YEARS),
            ('RTE_INITIAL_PREMIUM', RTE_INITIAL_PREMIUM),
            ('VOCATIONAL_PREMIUM', VOCATIONAL_PREMIUM),
            ('RTE_SEAT_FILL_RATE', RTE_SEAT_FILL_RATE),
            ('RTE_RETENTION_FUNNEL', RTE_RETENTION_FUNNEL),
            ('APPRENTICE_COMPLETION_RATE', APPRENTICE_COMPLETION_RATE),
            ('APPRENTICE_STIPEND_MONTHLY', APPRENTICE_STIPEND_MONTHLY),
            ('APPRENTICE_YEAR_0_OPPORTUNITY_COST', APPRENTICE_YEAR_0_OPPORTUNITY_COST),
            ('APPRENTICE_INITIAL_PREMIUM', APPRENTICE_INITIAL_PREMIUM),
            ('WORKING_LIFE_FORMAL', WORKING_LIFE_FORMAL),
            ('WORKING_LIFE_INFORMAL', WORKING_LIFE_INFORMAL),
        ]

        # Extract individual parameters
        for canonical_name, param_obj in param_objects:
            extracted = self.extract_parameter(canonical_name, param_obj)
            self.parameters_extracted.append(extracted)

            # If derived, extract formula
            if extracted['parameter_type'] == 'derived':
                formula_data = self.extract_formula(
                    canonical_name,
                    param_obj.source,
                    param_obj.notes
                )
                if formula_data:
                    self.formulas_extracted.append(formula_data)

        # Extract baseline wages (nested dictionary)
        for location in ['urban', 'rural']:
            for gender in ['male', 'female']:
                for edu_level in ['secondary_10yr', 'higher_secondary_12yr', 'casual_informal']:
                    key = f'{location}_{gender}'
                    if key in BASELINE_WAGES and edu_level in BASELINE_WAGES[key]:
                        param_obj = BASELINE_WAGES[key][edu_level]
                        canonical_name = f"BASELINE_WAGE_{location.upper()}_{gender.upper()}_{edu_level.upper()}"

                        extracted = self.extract_parameter(canonical_name, param_obj)
                        self.parameters_extracted.append(extracted)

                        if extracted['parameter_type'] == 'derived':
                            formula_data = self.extract_formula(
                                canonical_name,
                                param_obj.source,
                                param_obj.notes
                            )
                            if formula_data:
                                self.formulas_extracted.append(formula_data)

        # Counterfactual distribution (special case - tuple value)
        counterfactual = {
            'canonical_name': 'COUNTERFACTUAL_SCHOOLING',
            'display_name': COUNTERFACTUAL_SCHOOLING.name,
            'value': str(COUNTERFACTUAL_SCHOOLING.value),  # Convert tuple to string
            'unit': COUNTERFACTUAL_SCHOOLING.unit,
            'tier': COUNTERFACTUAL_SCHOOLING.tier,
            'sensitivity_min': None,
            'sensitivity_max': None,
            'sampling_method': COUNTERFACTUAL_SCHOOLING.sampling_method,
            'source_field': COUNTERFACTUAL_SCHOOLING.source,
            'notes_field': COUNTERFACTUAL_SCHOOLING.notes,
            'last_updated': COUNTERFACTUAL_SCHOOLING.last_updated,
            'parameter_type': 'direct_quote',
            'derivation_type': None,
            'source_summary': COUNTERFACTUAL_SCHOOLING.source[:200],
            'registry_notes': self.extract_important_comments(COUNTERFACTUAL_SCHOOLING.notes)
        }
        self.parameters_extracted.append(counterfactual)

        print(f"✓ Extracted {len(self.parameters_extracted)} parameters")
        print(f"✓ Identified {len(self.formulas_extracted)} derived parameters")

    def generate_master_csv(self, output_path: str):
        """Generate parameters_master.csv"""

        fieldnames = [
            'canonical_name',
            'display_name',
            'value',
            'unit',
            'parameter_type',
            'tier',
            'sensitivity_min',
            'sensitivity_max',
            'sampling_method',
            'source_summary',
            'registry_notes',
            'last_updated'
        ]

        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for param in self.parameters_extracted:
                row = {k: param.get(k, '') for k in fieldnames}
                writer.writerow(row)

        print(f"✓ Generated {output_path} ({len(self.parameters_extracted)} rows)")

    def generate_derived_csv(self, output_path: str):
        """Generate parameters_derived.csv"""

        if not self.formulas_extracted:
            print("⚠ No derived parameters found - skipping parameters_derived.csv")
            return

        # Build fieldnames dynamically (up to 6 inputs)
        fieldnames = [
            'parameter_name',
            'derivation_type',
            'calculation_formula'
        ]

        max_inputs = 6
        for i in range(1, max_inputs + 1):
            fieldnames.extend([
                f'input_{i}',
                f'input_{i}_type',
                f'input_{i}_source'
            ])

        fieldnames.extend(['verified_manually', 'verification_notes'])

        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for formula_data in self.formulas_extracted:
                # Find parameter type
                param_name = formula_data['parameter_name']
                param_obj = next(
                    (p for p in self.parameters_extracted if p['canonical_name'] == param_name),
                    None
                )

                row = {
                    'parameter_name': param_name,
                    'derivation_type': param_obj.get('derivation_type', '') if param_obj else '',
                    'calculation_formula': formula_data['formula'],
                    'verified_manually': 'FALSE',
                    'verification_notes': ''
                }

                # Add inputs
                for i, input_data in enumerate(formula_data['inputs'][:max_inputs], 1):
                    row[f'input_{i}'] = input_data['name']
                    row[f'input_{i}_type'] = input_data['type']
                    row[f'input_{i}_source'] = input_data['source']

                writer.writerow(row)

        print(f"✓ Generated {output_path} ({len(self.formulas_extracted)} rows)")

    def generate_validation_report(self, output_path: str):
        """Generate EXTRACTION_VALIDATION_REPORT.md"""

        report = f"""# PARAMETER EXTRACTION VALIDATION REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary

- **Total parameters extracted:** {len(self.parameters_extracted)}
- **Derived parameters:** {len(self.formulas_extracted)}
- **Direct quote parameters:** {len(self.parameters_extracted) - len(self.formulas_extracted)}

## Validation Issues

### 1. Parameters with Unclear Classification
"""
        if self.validation_issues['unclear_classification']:
            for param in self.validation_issues['unclear_classification']:
                report += f"- {param}\n"
        else:
            report += "*None found*\n"

        report += f"""
### 2. Derived Parameters with Missing Inputs
"""
        if self.validation_issues['missing_inputs']:
            for param in self.validation_issues['missing_inputs']:
                report += f"- {param} (could not identify formula inputs)\n"
        else:
            report += "*None found*\n"

        report += f"""
### 3. Circular Dependencies
*Not yet implemented - requires dependency graph analysis*

### 4. Parameters in Registry Only (not in verified.csv)
*Requires cross-reference with parameters_verified.csv*

### 5. Parameters in verified.csv Only (not in registry)
*Requires cross-reference with parameters_verified.csv*

## Parameter Type Distribution

"""
        type_counts = {}
        for param in self.parameters_extracted:
            ptype = param['parameter_type']
            type_counts[ptype] = type_counts.get(ptype, 0) + 1

        for ptype, count in sorted(type_counts.items()):
            report += f"- **{ptype}**: {count} parameters\n"

        report += f"""
## Tier Distribution

"""
        tier_counts = {}
        for param in self.parameters_extracted:
            tier = param['tier']
            tier_counts[tier] = tier_counts.get(tier, 0) + 1

        for tier in sorted(tier_counts.keys()):
            report += f"- **Tier {tier}**: {tier_counts[tier]} parameters\n"

        report += f"""
## Next Steps

1. **Human review of derived parameters**: Verify formulas in `parameters_derived.csv`
2. **Cross-reference with verified.csv**: Identify discrepancies
3. **Circular dependency check**: Build dependency graph
4. **Complete input resolution**: For derived parameters, identify input types and sources

## Notes

- Parameters with `parameter_type='derived'` should have entries in `parameters_derived.csv`
- All parameter values are from `parameter_registry_v3.py` (canonical source)
- Registry notes field has been truncated to 700 characters max
- Formulas extracted from `source` and `notes` fields may require manual cleanup
"""

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)

        print(f"✓ Generated {output_path}")

    def save_intermediate_json(self, params_path: str, formulas_path: str):
        """Save intermediate JSON files for debugging"""

        with open(params_path, 'w', encoding='utf-8') as f:
            json.dump(self.parameters_extracted, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved {params_path}")

        with open(formulas_path, 'w', encoding='utf-8') as f:
            json.dump(self.formulas_extracted, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved {formulas_path}")


def main():
    """Main execution"""
    print("="*70)
    print("PARAMETER EXTRACTION & CLASSIFICATION - PHASE 1")
    print("="*70)
    print()

    extractor = ParameterExtractor()

    # Task 1-4: Extract and classify
    print("TASK 1-4: Extracting parameters from registry...")
    extractor.extract_all_parameters()
    print()

    # Save intermediate JSON
    print("Saving intermediate JSON files...")
    extractor.save_intermediate_json(
        'parameters_extracted.json',
        'formulas_extracted.json'
    )
    print()

    # Task 5: Generate master CSV
    print("TASK 5: Generating parameters_master.csv...")
    extractor.generate_master_csv('parameters_master.csv')
    print()

    # Task 6: Generate derived CSV
    print("TASK 6: Generating parameters_derived.csv...")
    extractor.generate_derived_csv('parameters_derived.csv')
    print()

    # Task 7: Generate validation report
    print("TASK 7: Generating validation report...")
    extractor.generate_validation_report('EXTRACTION_VALIDATION_REPORT.md')
    print()

    print("="*70)
    print("EXTRACTION COMPLETE")
    print("="*70)
    print()
    print("Deliverables:")
    print("  1. parameters_master.csv - SSOT for all parameter values")
    print("  2. parameters_derived.csv - Formulas for calculated parameters")
    print("  3. EXTRACTION_VALIDATION_REPORT.md - Issues for human review")
    print("  4. parameters_extracted.json - Intermediate data (debugging)")
    print("  5. formulas_extracted.json - Intermediate data (debugging)")
    print()
    print("Next steps:")
    print("  - Review validation report for issues")
    print("  - Manually verify formulas in parameters_derived.csv")
    print("  - Cross-reference with parameters_verified.csv")


if __name__ == '__main__':
    main()
