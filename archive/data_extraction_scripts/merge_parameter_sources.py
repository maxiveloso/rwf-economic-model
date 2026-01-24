#!/usr/bin/env python3
"""
Merge Parameter Sources Script

Consolidates multiple sources from parameters_verified.csv into
Parameter_Sources_Master.csv with markdown hyperlinks and multi-line cells.

Author: Claude
Date: 2026-01-15
"""

import pandas as pd
import csv
import re
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, List, Tuple, Set


def extract_key_terms(text: str) -> Set[str]:
    """
    Extract key terms from parameter name.

    Args:
        text: Parameter name or description

    Returns:
        Set of meaningful terms (lowercase, no stop words, length > 2)
    """
    if pd.isna(text):
        return set()

    # Stop words to exclude
    stop_words = {
        'the', 'a', 'an', 'in', 'on', 'at', 'for', 'to', 'of',
        'and', 'or', 'by', 'with', 'from', 'vs', 'per'
    }

    # Extract words
    text = str(text).lower()
    words = re.findall(r'\w+', text)

    # Filter: remove stop words and short words
    return set(w for w in words if w not in stop_words and len(w) > 2)


def calculate_similarity(text1: str, text2: str) -> float:
    """
    Calculate string similarity using SequenceMatcher.

    Args:
        text1: First text
        text2: Second text

    Returns:
        Similarity score 0.0-1.0
    """
    if pd.isna(text1) or pd.isna(text2):
        return 0.0
    return SequenceMatcher(None, str(text1).lower(), str(text2).lower()).ratio()


def calculate_match_score(
    master_row: pd.Series,
    verified_name: str,
    verified_value: str
) -> Tuple[float, Dict[str, float]]:
    """
    Calculate match score between Master and Verified parameters.

    Uses weighted scoring:
    - Parameter name similarity (50% weight)
    - Symbol match (30% weight)
    - Value match (20% weight)
    - Key terms overlap (30% weight)

    Args:
        master_row: Row from Master CSV
        verified_name: Parameter name from Verified CSV
        verified_value: Claimed value from Verified CSV

    Returns:
        Tuple of (total_score, component_scores_dict)
    """
    scores = {}

    # 1. Name similarity (50% weight)
    master_name = master_row['name']
    scores['name'] = calculate_similarity(master_name, verified_name)

    # 2. Symbol match (30% weight)
    master_symbol = master_row.get('symbol', '')
    scores['symbol'] = 0.0
    if pd.notna(master_symbol) and str(master_symbol).strip():
        if str(master_symbol) in str(verified_name):
            scores['symbol'] = 0.3

    # 3. Value match (20% weight)
    master_value = master_row.get('value', '')
    scores['value'] = 0.0
    if pd.notna(master_value) and pd.notna(verified_value):
        if str(master_value) in str(verified_value):
            scores['value'] = 0.2

    # 4. Key terms overlap (30% weight)
    master_terms = extract_key_terms(master_name)
    verified_terms = extract_key_terms(verified_name)

    if master_terms and verified_terms:
        intersection = len(master_terms & verified_terms)
        union = len(master_terms | verified_terms)
        scores['terms'] = intersection / union if union > 0 else 0.0
    else:
        scores['terms'] = 0.0

    # Calculate total score
    total_score = (
        scores['name'] * 0.5 +
        scores['symbol'] +
        scores['value'] +
        scores['terms'] * 0.3
    )

    return total_score, scores


def find_best_match(
    master_row: pd.Series,
    verified_df: pd.DataFrame
) -> Tuple[str, float, Dict[str, float]]:
    """
    Find best matching parameter in Verified CSV for a Master parameter.

    Args:
        master_row: Row from Master CSV
        verified_df: Full Verified CSV DataFrame

    Returns:
        Tuple of (best_match_name, best_score, score_components)
    """
    best_match = None
    best_score = 0.0
    best_components = {}

    # Get unique parameter names from verified
    unique_params = verified_df['parameter_name'].unique()

    for verified_name in unique_params:
        # Get a sample row for this parameter to check value
        sample_row = verified_df[verified_df['parameter_name'] == verified_name].iloc[0]
        verified_value = sample_row.get('claimed_value', '')

        # Calculate score
        score, components = calculate_match_score(master_row, verified_name, verified_value)

        if score > best_score:
            best_score = score
            best_match = verified_name
            best_components = components

    return best_match, best_score, best_components


def format_source_entry(
    filename: str,
    url: str,
    citation: str
) -> str:
    """
    Format a single source entry as markdown hyperlink.

    Format: [filename](url) citation
    Falls back to plain text if URL missing.

    Args:
        filename: Source document filename
        url: Source URL
        citation: Source citation text

    Returns:
        Formatted source string
    """
    # Check if we have URL for hyperlink
    has_url = pd.notna(url) and str(url).strip() and str(url).lower() != 'nan'
    has_filename = pd.notna(filename) and str(filename).strip() and str(filename).lower() != 'nan'
    has_citation = pd.notna(citation) and str(citation).strip() and str(citation).lower() != 'nan'

    if has_url and has_filename:
        # Create markdown hyperlink
        result = f"[{filename}]({url})"
        if has_citation:
            result += f" {citation}"
        return result

    elif has_filename and has_citation:
        # Plain text: filename and citation
        return f"{filename} - {citation}"

    elif has_filename:
        # Just filename
        return str(filename)

    elif has_citation:
        # Just citation
        return str(citation)

    else:
        # Nothing useful
        return None


def aggregate_sources(verified_df: pd.DataFrame, parameter_name: str) -> Tuple[str, Dict]:
    """
    Aggregate all sources for a parameter into multi-line string.

    Args:
        verified_df: Verified CSV DataFrame
        parameter_name: Parameter name to aggregate sources for

    Returns:
        Tuple of (multi_line_sources_string, stats_dict)
    """
    # Get all rows for this parameter
    param_rows = verified_df[verified_df['parameter_name'] == parameter_name]

    stats = {
        'total_rows': len(param_rows),
        'with_url': 0,
        'without_url': 0,
        'skipped_empty': 0,
        'duplicates': 0
    }

    sources = []
    seen_urls = set()

    for _, row in param_rows.iterrows():
        filename = row.get('source_document_filename', '')
        url = row.get('source_url', '')
        citation = row.get('source_citation', '')

        # Check for duplicates by URL
        url_str = str(url).strip() if pd.notna(url) else ''
        if url_str and url_str.lower() != 'nan':
            if url_str in seen_urls:
                stats['duplicates'] += 1
                continue
            seen_urls.add(url_str)

        # Format source entry
        formatted = format_source_entry(filename, url, citation)

        if formatted:
            sources.append(formatted)
            if pd.notna(url) and str(url).strip() and str(url).lower() != 'nan':
                stats['with_url'] += 1
            else:
                stats['without_url'] += 1
        else:
            stats['skipped_empty'] += 1

    # Join with actual newlines
    multi_line_sources = '\n'.join(sources)

    return multi_line_sources, stats


def create_backup(file_path: Path) -> Path:
    """
    Create timestamped backup of file.

    Args:
        file_path: Path to file to backup

    Returns:
        Path to backup file
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = file_path.parent / f"{file_path.stem}_backup_{timestamp}{file_path.suffix}"

    import shutil
    shutil.copy2(file_path, backup_path)

    return backup_path


def main():
    """Main execution function."""

    print("=" * 80)
    print("Parameter Sources Merge Script")
    print("=" * 80)
    print()

    # Define paths
    base_dir = Path(__file__).parent
    master_path = base_dir / 'data' / 'param_sources' / 'Parameter_Sources_Master.csv'
    verified_path = base_dir / 'parameters_verified.csv'
    report_path = base_dir / 'merge_sources_report.txt'

    # Validate files exist
    if not master_path.exists():
        print(f"ERROR: Master CSV not found at {master_path}")
        return 1

    if not verified_path.exists():
        print(f"ERROR: Verified CSV not found at {verified_path}")
        return 1

    print(f"Master CSV: {master_path}")
    print(f"Verified CSV: {verified_path}")
    print()

    # Phase 1: Load data
    print("Phase 1: Loading data...")
    try:
        df_master = pd.read_csv(master_path, encoding='utf-8')
    except UnicodeDecodeError:
        df_master = pd.read_csv(master_path, encoding='latin-1')

    try:
        df_verified = pd.read_csv(verified_path, encoding='utf-8')
    except UnicodeDecodeError:
        df_verified = pd.read_csv(verified_path, encoding='latin-1')

    print(f"  Master: {len(df_master)} parameters")
    print(f"  Verified: {len(df_verified)} rows, {df_verified['parameter_name'].nunique()} unique parameters")
    print()

    # Create backup
    print("Creating backup...")
    backup_path = create_backup(master_path)
    print(f"  Backup saved: {backup_path}")
    print()

    # Phase 2-4: Process parameters
    print("Phase 2-4: Matching and merging sources...")
    print()

    report_lines = []
    report_lines.append("=" * 80)
    report_lines.append("PARAMETER SOURCES MERGE REPORT")
    report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("=" * 80)
    report_lines.append("")

    # Stats
    stats = {
        'total_master': len(df_master),
        'matched': 0,
        'unmatched': 0,
        'total_sources_merged': 0,
        'sources_with_url': 0,
        'sources_without_url': 0,
        'duplicates_removed': 0,
        'empty_skipped': 0
    }

    match_details = []
    unmatched_params = []

    # Process each Master parameter
    for idx, master_row in df_master.iterrows():
        master_name = master_row['name']

        # Find best match
        best_match, best_score, score_components = find_best_match(master_row, df_verified)

        print(f"[{idx+1}/{len(df_master)}] {master_name}")
        print(f"  → Best match: {best_match}")
        print(f"  → Score: {best_score:.3f} (name:{score_components['name']:.2f} symbol:{score_components['symbol']:.2f} value:{score_components['value']:.2f} terms:{score_components['terms']:.2f})")

        match_details.append({
            'master_name': master_name,
            'matched_name': best_match,
            'score': best_score,
            'components': score_components
        })

        # Threshold for acceptance
        if best_score > 0.5:
            print(f"  ✓ MATCHED - Updating sources")
            stats['matched'] += 1

            # Aggregate sources
            multi_line_sources, source_stats = aggregate_sources(df_verified, best_match)

            # Update Master CSV
            df_master.at[idx, 'source'] = multi_line_sources

            # Update stats
            stats['total_sources_merged'] += source_stats['total_rows']
            stats['sources_with_url'] += source_stats['with_url']
            stats['sources_without_url'] += source_stats['without_url']
            stats['duplicates_removed'] += source_stats['duplicates']
            stats['empty_skipped'] += source_stats['skipped_empty']

            print(f"    Sources: {source_stats['total_rows']} rows → {source_stats['with_url']} with URL, {source_stats['without_url']} without")
            print(f"    Duplicates removed: {source_stats['duplicates']}, Empty skipped: {source_stats['skipped_empty']}")
        else:
            print(f"  ✗ NOT MATCHED (score < 0.5) - Keeping original source")
            stats['unmatched'] += 1
            unmatched_params.append(master_name)

        print()

    # Phase 5: Save and report
    print("Phase 5: Saving results...")
    print()

    # Save updated Master CSV with proper quoting
    df_master.to_csv(master_path, index=False, encoding='utf-8', quoting=csv.QUOTE_NONNUMERIC)
    print(f"  ✓ Updated Master CSV saved: {master_path}")

    # Generate report
    report_lines.append("SUMMARY STATISTICS")
    report_lines.append("-" * 80)
    report_lines.append(f"Total parameters in Master:    {stats['total_master']}")
    report_lines.append(f"Parameters matched & updated:  {stats['matched']} ({stats['matched']/stats['total_master']*100:.1f}%)")
    report_lines.append(f"Parameters unmatched:          {stats['unmatched']} ({stats['unmatched']/stats['total_master']*100:.1f}%)")
    report_lines.append(f"")
    report_lines.append(f"Total sources merged:          {stats['total_sources_merged']}")
    report_lines.append(f"  - With URL (hyperlinked):    {stats['sources_with_url']}")
    report_lines.append(f"  - Without URL (plain text):  {stats['sources_without_url']}")
    report_lines.append(f"Duplicate sources removed:     {stats['duplicates_removed']}")
    report_lines.append(f"Empty sources skipped:         {stats['empty_skipped']}")
    report_lines.append("")

    # Unmatched parameters
    if unmatched_params:
        report_lines.append("")
        report_lines.append("UNMATCHED PARAMETERS (score < 0.5)")
        report_lines.append("-" * 80)
        for param in unmatched_params:
            report_lines.append(f"  - {param}")
        report_lines.append("")

    # Match details
    report_lines.append("")
    report_lines.append("DETAILED MATCH SCORES")
    report_lines.append("-" * 80)
    for detail in match_details:
        report_lines.append(f"\nMaster: {detail['master_name']}")
        report_lines.append(f"  Matched: {detail['matched_name']}")
        report_lines.append(f"  Score: {detail['score']:.3f}")
        comp = detail['components']
        report_lines.append(f"    name: {comp['name']:.3f}, symbol: {comp['symbol']:.3f}, value: {comp['value']:.3f}, terms: {comp['terms']:.3f}")

    report_lines.append("")
    report_lines.append("=" * 80)
    report_lines.append("END OF REPORT")
    report_lines.append("=" * 80)

    # Save report
    report_text = '\n'.join(report_lines)
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_text)

    print(f"  ✓ Report saved: {report_path}")
    print()

    # Print summary
    print("=" * 80)
    print("MERGE COMPLETE")
    print("=" * 80)
    print(f"Matched: {stats['matched']}/{stats['total_master']} ({stats['matched']/stats['total_master']*100:.1f}%)")
    print(f"Sources merged: {stats['total_sources_merged']}")
    print(f"Duplicates removed: {stats['duplicates_removed']}")
    print()
    print(f"Next steps:")
    print(f"  1. Review report: cat {report_path}")
    print(f"  2. Open in Google Sheets to verify multi-line cells and hyperlinks")
    print(f"  3. Spot-check parameter sources for accuracy")
    print()

    return 0


if __name__ == '__main__':
    exit(main())
