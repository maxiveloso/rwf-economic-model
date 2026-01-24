#!/usr/bin/env python3
"""
Append 4 new parameter rows to parameters_verified.csv
"""
import csv
import uuid
from datetime import datetime

# Path to the CSV file
csv_path = "/Users/maximvf/Library/CloudStorage/GoogleDrive-maxiveloso@gmail.com/Mi unidad/Worklife/Applications/RWF/RWF_Lifetime_Economic_Benefits_Estimation/rwf_model/parameters_verified.csv"

# Define the 4 new rows
new_rows = [
    {
        "parameter_id": str(uuid.uuid4()),
        "parameter_name": "Apprenticeship Year 0 Net Opportunity Cost",
        "claimed_value": "-₹49,000/year (sensitivity: -₹80k to -₹20k)",
        "claim_unit": "₹/year",
        "category": "1A-CORE_MODEL",
        "is_derived": "TRUE",
        "year_period": "2025",
        "usage_in_model": "Year 0 adjustment for apprenticeship NPV. Creates negative premium during 1-year training period. Reduces total LNPV by ~₹45-55k in present value terms (4-5% of total apprenticeship NPV). Critical for accurate modeling of apprenticeship pathway vs immediate informal employment.",
        "credibility_limitations": "MODERATE CREDIBILITY: Calculation depends on accurate counterfactual wage estimate. LIMITATIONS: (1) Assumes youth would be employed in informal sector (not accounting for unemployment) (2) Counterfactual wage based on national average - varies significantly by region (urban youth ₹15-16k/mo, rural ₹12-13k/mo) (3) Does not account for non-monetary training benefits (skill development, network) (4) Stipend may cover living costs in rural areas but not urban metros",
        "source_document_filename": "Calculated from APPRENTICE_STIPEND_MONTHLY and PLFS casual wage data",
        "source_url": "",
        "source_citation": "Calculated parameter",
        "source_page_hint": "",
        "verification_status": "Model-Derived",
        "confidence_score": "",
        "verified_snippet": "Stipend ₹120k/year - Counterfactual informal wage ₹168k/year = -₹48k opportunity cost",
        "snippet_page": "",
        "llm_reasoning": "Not Applicable - Model-Derived",
        "llm_thinking_process": "",
        "alternative_value_found": "",
        "needs_human_review": "FALSE",
        "verified_at": "",
        "processing_time_ms": "",
        "llm_model_used": ""
    },
    {
        "parameter_id": str(uuid.uuid4()),
        "parameter_name": "Apprenticeship Wage Persistence Half-Life (h) - CRITICAL UNKNOWN",
        "claimed_value": "10 years (sensitivity: 5-50 years)",
        "claim_unit": "years",
        "category": "0-VETTING",
        "is_derived": "FALSE",
        "year_period": "N/A",
        "usage_in_model": "CRITICAL for apprenticeship LNPV. Determines exponential decay: Premium(t) = π₀ × exp(-ln(2)/h × t). Interaction (π₀, h) requires two-dimensional sensitivity analysis. Conservative: h=5 years. Moderate: h=10 years. Optimistic: h=50 years (effectively no decay).",
        "credibility_limitations": "LOW CREDIBILITY - CRITICAL DATA GAP: No longitudinal studies track apprentices 5-15 years post-completion in India. LIMITATIONS: (1) LARGEST UNCERTAINTY in apprenticeship NPV - varies by factor of 6× (h=5 → ₹3.5L vs h=∞ → ₹22L) (2) Global evidence mixed: OECD countries show persistence 10-20 years, but different labor markets (3) Skill obsolescence may accelerate decay in fast-changing sectors (4) Premium may persist longer in regulated trades vs general skills (5) Interaction effect with π₀ - both parameters uncertain compounds model uncertainty",
        "source_document_filename": "Assumed - no empirical data available",
        "source_url": "",
        "source_citation": "",
        "source_page_hint": "",
        "verification_status": "Data Gap",
        "confidence_score": "",
        "verified_snippet": "",
        "snippet_page": "",
        "llm_reasoning": "",
        "llm_thinking_process": "",
        "alternative_value_found": "",
        "needs_human_review": "FALSE",
        "verified_at": "",
        "processing_time_ms": "",
        "llm_model_used": ""
    },
    {
        "parameter_id": str(uuid.uuid4()),
        "parameter_name": "Formal Sector Entry Probability (Youth Without Vocational Training - Counterfactual)",
        "claimed_value": "10% (sensitivity: 5-15%)",
        "claim_unit": "%",
        "category": "1A-CORE_MODEL",
        "is_derived": "FALSE",
        "year_period": "2023-24",
        "usage_in_model": "COUNTERFACTUAL for apprenticeship intervention. Treatment effect = P(F|Apprentice) - P(F|NoTrain) = 72% - 10% = 62pp. If true baseline is 15% (not 10%), treatment effect overstated by 8%. Critical parameter for defensible apprenticeship NPV.",
        "credibility_limitations": "LOW CREDIBILITY: Derived from aggregate tables without microdata access. LIMITATIONS: (1) PLFS does not directly report P(Formal|NoVocTrain) - requires calculation from employment distribution (2) Definition of \"formal\" unclear - using \"regular salaried\" as proxy (3) Cross-sectional data - not tracking same cohort over time (4) Selection bias: youth who pursue vocational training may differ systematically (5) Regional heterogeneity (5-8% rural North/East vs 12-15% urban South/West) (6) Counterfactual group definition unclear (includes dropouts, unemployed?)",
        "source_document_filename": "PLFS 2023-24 aggregate estimates (derived calculation, not direct quote)",
        "source_url": "https://dge.gov.in/dge/sites/default/files/2024-10/Annual_Report_Periodic_Labour_Force_Survey_23_24.pdf",
        "source_citation": "PLFS 2023-24 (aggregate tables - specific table TBD)",
        "source_page_hint": "",
        "verification_status": "Requires Manual Calculation",
        "confidence_score": "",
        "verified_snippet": "",
        "snippet_page": "",
        "llm_reasoning": "",
        "llm_thinking_process": "",
        "alternative_value_found": "Needs verification via PLFS microdata analysis or Table XX extraction",
        "needs_human_review": "FALSE",
        "verified_at": "",
        "processing_time_ms": "",
        "llm_model_used": ""
    },
    {
        "parameter_id": str(uuid.uuid4()),
        "parameter_name": "Test Score to Years of Schooling Conversion",
        "claimed_value": "4.7 years/SD (sensitivity: 4.0-6.5 years/SD)",
        "claim_unit": "years/SD",
        "category": "1A-CORE_MODEL",
        "is_derived": "FALSE",
        "year_period": "2021 publication",
        "usage_in_model": "Converts RTE test score gain (0.23 SD) to equivalent years: 0.23 × 4.7 = 1.08 years. This increases education from 12 → 13.08 years → 6.2% wage gain via Mincer. If factor is 6.0 (not 4.7), NPV increases 27%. Sensitivity range [4.0, 6.5] captures uncertainty.",
        "credibility_limitations": "MODERATE CREDIBILITY: Based on pooled LMIC data, not India-specific. LIMITATIONS: (1) EXTERNAL VALIDITY: LMIC average may not apply to India's specific context (2) ASSUMPTION: Conversion assumes test scores → degree completion (employers see credentials, not scores) (3) MISSING LINK: No data on whether RTE students have higher completion rates (4) HETEROGENEITY: Varies by subject (math vs language), grade level, and intervention type (5) May double-count if RTE_TEST_SCORE_GAIN already captures credential effects",
        "source_document_filename": "World Bank LMIC meta-analysis (Angrist et al. 2021)",
        "source_url": "",
        "source_citation": "Angrist et al. (2021) - World Bank LMIC Education Returns Meta-Analysis",
        "source_page_hint": "",
        "verification_status": "Approximate Match",
        "confidence_score": "",
        "verified_snippet": "",
        "snippet_page": "",
        "llm_reasoning": "",
        "llm_thinking_process": "",
        "alternative_value_found": "Range 4.0-6.5 years/SD depending on context (confirmed from literature)",
        "needs_human_review": "TRUE",
        "verified_at": "",
        "processing_time_ms": "",
        "llm_model_used": ""
    }
]

# Read the existing CSV
print("Reading existing CSV...")
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    existing_rows = list(reader)

print(f"Found {len(existing_rows)} existing rows")
print(f"Columns: {len(fieldnames)}")

# Append new rows
print(f"\nAppending {len(new_rows)} new rows...")
with open(csv_path, 'a', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    for row in new_rows:
        writer.writerow(row)

print(f"\nSuccessfully appended {len(new_rows)} rows to {csv_path}")
print("New row parameter names:")
for row in new_rows:
    print(f"  - {row['parameter_name']}")
