# Archive

This folder contains historical materials and development artifacts from the RWF Economic Impact Model project.

## Contents

### milestone_prompts/

Contains the original milestone requirement documents (M1-M5) that guided development:

| File | Description |
|------|-------------|
| `M1.md` | Data Extraction & Processing requirements |
| `M2.md` | LNPV Model Construction requirements |
| `M3.md` | Sensitivity Analysis & Break-Even requirements |
| `M4.md` | Validation & QA requirements |
| `M5.md` | Documentation & Reporting requirements |
| `post_milestone.md` | Stakeholder presentation preparation |

These documents serve as a reference for understanding the project's phased development approach.

### data_extraction_scripts/

Utility scripts used during the data extraction phase (M1):

| Script | Purpose |
|--------|---------|
| `extract_parameters.py` | Extract parameters from source documents |
| `merge_parameter_sources.py` | Merge multiple parameter sources |
| `append_parameters.py` | Add parameters to registry |
| `sync_registry.py` | Sync between CSV and Python registry |
| `create_verified_csv.py` | Generate verified parameter CSV |
| `validate_parameter_calculations.py` | Validate parameter math |

### verification_scripts/

Scripts used for parameter verification and source validation (M4):

These scripts were used to verify parameter values against source documents during the QA phase.

### working_documents/

Project evolution documentation, changelogs, and decision logs.

---

## Note

These materials are provided for reference and reproducibility. The production code is in the `src/` folder, and the official documentation is in the `docs/` folder.

For running the model, see the main [README.md](../README.md) and [QUICKSTART.md](../QUICKSTART.md).
