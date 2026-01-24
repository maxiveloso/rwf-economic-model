#!/usr/bin/env python3
"""
Create parameters_verified.csv from existing sources.

This script migrates data from:
1. Parameters sources - Latest.csv (main parameter data)
2. Parameters sources - param2URL2sourcename.csv (URL to filename mapping)
3. Supabase claim_verification_log (9 successful verifications)

Output: parameters_verified.csv with new schema
"""

import pandas as pd
import re
import uuid
from datetime import datetime
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

# Supabase connection
SUPABASE_URL = os.getenv('SUPABASE_URL', 'https://msytuetfqdchbehzichh.supabase.co')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def extract_urls_from_text(text: str) -> list:
    """Extract all URLs from a text field."""
    if pd.isna(text):
        return []

    # Find all HTTP(S) URLs
    urls = re.findall(r'https?://[^\s<>\"\'\)]+', str(text))

    # Clean URLs (remove trailing punctuation)
    cleaned = []
    for url in urls:
        # Remove trailing punctuation and special chars
        url = re.sub(r'[;,\.\)]+$', '', url)
        cleaned.append(url)

    return cleaned


def get_filename_for_url(url: str, url_mapping: pd.DataFrame) -> str:
    """
    Get source_document_filename for a URL from param2URL2sourcename.csv

    Returns filename WITHOUT .pdf extension.
    """
    # Exact match first
    match = url_mapping[url_mapping['url'] == url]
    if len(match) > 0:
        return match.iloc[0]['/sources']

    # Partial match (sometimes URLs have slight differences)
    for idx, row in url_mapping.iterrows():
        mapped_url = row['url']
        # Check if core domain and path match
        if mapped_url in url or url in mapped_url:
            return row['/sources']

    # No match found
    return None


def load_supabase_verifications():
    """Load the 9 successful verifications from Supabase."""
    result = supabase.table('claim_verification_log').select('*').eq('needs_human_review', False).execute()

    verifications = {}
    for row in result.data:
        # Key: (parameter_name, source_url or filename)
        param_name = row['claim_text']

        # Try to get source info
        source_key = None
        if row.get('source_document_id'):
            # Get source document details
            source = supabase.table('source_documents').select('*').eq('id', row['source_document_id']).execute()
            if source.data:
                source_key = source.data[0].get('filename', '')

        if not source_key:
            source_key = 'unknown'

        key = (param_name, source_key)

        verifications[key] = {
            'verification_status': row['match_type'],  # exact, approximate, etc
            'confidence_score': row['confidence_score'] * 100,  # Convert 0-1 to 0-100
            'verified_snippet': row.get('extracted_snippet', ''),
            'snippet_page': row.get('snippet_page_number', ''),
            'llm_reasoning': row.get('llm_interpretation', ''),
            'llm_thinking_process': row.get('llm_raw_response', ''),
            'verified_at': row.get('verified_at', ''),
            'processing_time_ms': row.get('processing_time_ms', 0),
            'llm_model_used': row.get('llm_model', 'moonshotai/kimi-k2-thinking')
        }

    print(f"Loaded {len(verifications)} successful verifications from Supabase")
    return verifications


def create_verified_csv():
    """Main function to create parameters_verified.csv"""

    print("=" * 80)
    print("CREATING parameters_verified.csv")
    print("=" * 80)
    print()

    # 1. Load source CSVs
    print("1. Loading source CSVs...")
    df_latest = pd.read_csv('data/param_sources/Parameters sources - Latest.csv', encoding='utf-8')
    df_url_mapping = pd.read_csv('data/param_sources/Parameters sources - param2URL2sourcename.csv', encoding='utf-8')

    print(f"   Loaded {len(df_latest)} parameters from Latest.csv")
    print(f"   Loaded {len(df_url_mapping)} URL mappings from param2URL2sourcename.csv")
    print()

    # 2. Load Supabase verifications
    print("2. Loading Supabase verifications...")
    supabase_verifications = load_supabase_verifications()
    print()

    # 3. Build verified CSV rows
    print("3. Building verified CSV rows...")
    print("   (One row per parameter-source pair)")
    print()

    verified_rows = []

    for idx, row in df_latest.iterrows():
        param_name = row['Parameter/Variable Name']

        # Skip if parameter name is empty
        if pd.isna(param_name):
            continue

        print(f"   [{idx+1}/{len(df_latest)}] {param_name[:60]}")

        # Extract all URLs from columns D (URL) and N (External Sources)
        urls_col_d = extract_urls_from_text(row['URL'])
        urls_col_n = extract_urls_from_text(row['External Sources'])
        all_urls = urls_col_d + urls_col_n

        # Remove duplicates while preserving order
        seen = set()
        unique_urls = []
        for url in all_urls:
            if url not in seen:
                seen.add(url)
                unique_urls.append(url)

        print(f"       Found {len(unique_urls)} unique URLs")

        # If no URLs found, create one row with empty source
        if len(unique_urls) == 0:
            print(f"       WARNING: No URLs found, creating row with empty source")
            verified_rows.append(create_row_from_latest(row, None, None, supabase_verifications))
            continue

        # Create one row per URL
        for url_idx, url in enumerate(unique_urls, 1):
            # Get filename from mapping
            filename = get_filename_for_url(url, df_url_mapping)

            if filename:
                print(f"       [{url_idx}] {filename[:50]}")
            else:
                print(f"       [{url_idx}] NO MATCH for {url[:60]}...")

            # Create row
            verified_row = create_row_from_latest(row, url, filename, supabase_verifications)
            verified_rows.append(verified_row)

        print()

    # 4. Create DataFrame
    print("4. Creating final DataFrame...")
    df_verified = pd.DataFrame(verified_rows)

    print(f"   Total rows: {len(df_verified)}")
    print(f"   Parameters: {df_verified['parameter_name'].nunique()}")
    print(f"   With source_document_filename: {df_verified['source_document_filename'].notna().sum()}")
    print()

    # 5. Save to CSV
    output_path = 'parameters_verified.csv'
    df_verified.to_csv(output_path, index=False, encoding='utf-8')
    print(f"✓ Saved to: {output_path}")
    print()

    # 6. Summary statistics
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total rows: {len(df_verified)}")
    print(f"Unique parameters: {df_verified['parameter_name'].nunique()}")
    print(f"\nBy category:")
    print(df_verified['category'].value_counts())
    print(f"\nVerification status:")
    print(df_verified['verification_status'].value_counts())
    print()

    return df_verified


def create_row_from_latest(row, url, filename, supabase_verifications):
    """
    Create a verified CSV row from a Latest.csv row.

    Args:
        row: Row from Latest.csv
        url: Source URL (or None)
        filename: Source document filename (or None)
        supabase_verifications: Dict of existing verifications
    """
    param_name = row['Parameter/Variable Name']

    # Generate parameter_id (deterministic based on name + url)
    if url:
        id_seed = f"{param_name}_{url}"
    else:
        id_seed = f"{param_name}_no_source"
    param_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, id_seed))

    # Extract claim unit from claimed_value if possible
    claimed_value = row.get('Original Claim', row.get('Value/Range', ''))
    claim_unit = extract_unit(claimed_value)

    # Detect if derived
    is_derived = 'Model-Derived' in param_name or 'derived' in str(row.get('Usage in Model', '')).lower()

    # Check if we have verification from Supabase
    verification_key = (param_name, filename if filename else 'unknown')
    existing_verification = supabase_verifications.get(verification_key, {})

    # Map old verification status to new
    old_status = existing_verification.get('verification_status', '')
    if old_status == 'exact':
        new_status = 'CONSISTENT'
    elif old_status == 'approximate':
        new_status = 'PARTIAL'
    elif old_status == 'contradictory':
        new_status = 'CONTRADICTORY'
    elif old_status == 'not_found':
        new_status = 'NO_EVIDENCE'
    else:
        new_status = 'NOT_VERIFIED'

    # Build row
    verified_row = {
        # A. Parameter Definition
        'parameter_id': param_id,
        'parameter_name': param_name,
        'claimed_value': claimed_value,
        'claim_unit': claim_unit,
        'category': row.get('Category', ''),
        'is_derived': is_derived,
        'year_period': row.get('Year/Period', ''),
        'usage_in_model': row.get('Usage in Model', ''),
        'credibility_limitations': row.get('Credibility & Limitations', ''),

        # B. Source Document
        'source_document_filename': filename if filename else '',
        'source_url': url if url else '',
        'source_citation': row.get('Source Citation', ''),
        'source_page_hint': '',  # Empty for now

        # C. Verification Results (from Supabase if available)
        'verification_status': new_status,
        'confidence_score': existing_verification.get('confidence_score', 0),
        'verified_snippet': existing_verification.get('verified_snippet', ''),
        'snippet_page': existing_verification.get('snippet_page', ''),
        'llm_reasoning': existing_verification.get('llm_reasoning', ''),
        'llm_thinking_process': existing_verification.get('llm_thinking_process', ''),
        'alternative_value_found': '',
        'needs_human_review': existing_verification.get('confidence_score', 0) < 60 or new_status in ['CONTRADICTORY', 'NO_EVIDENCE'],
        'verified_at': existing_verification.get('verified_at', ''),
        'processing_time_ms': existing_verification.get('processing_time_ms', 0),
        'llm_model_used': existing_verification.get('llm_model_used', '')
    }

    return verified_row


def extract_unit(value_str):
    """Extract unit from a value string (e.g., '0.23 SD' -> 'SD')"""
    if pd.isna(value_str):
        return ''

    # Common units
    units = ['SD', '%', '₹', 'years', 'months', 'days', 'percentage', 'percent']

    value_str = str(value_str)

    for unit in units:
        if unit in value_str:
            return unit

    # Try to extract unit after number
    match = re.search(r'\d+\.?\d*\s*([A-Za-z₹%]+)', value_str)
    if match:
        return match.group(1)

    return ''


if __name__ == '__main__':
    df = create_verified_csv()

    print("\n" + "=" * 80)
    print("SAMPLE ROWS:")
    print("=" * 80)
    print(df[['parameter_name', 'source_document_filename', 'verification_status', 'confidence_score']].head(10))
    print()

    print("✓ Done! Review parameters_verified.csv and run verify_claims_simple.py when ready.")
