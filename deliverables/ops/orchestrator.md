# Orchestrator — Post-Delivery Tasks
## RightWalk Foundation Economic Impact Model

---

## How to Use
Execute tasks in order (01 → 09). Each prompt is in `after_delivery/_prompts/`. Read the prompt, execute it, then move to the next. The dependency map (`task_dependency_map_v2.xlsx`) is the structural source of truth.

After Task 04: run the checkpoint to update the tracer proposal before continuing.

---

## Execution Flow

### Phase 1: Foundations

| Order | Prompt File | Output Location | Depends On |
|-------|------------|-----------------|------------|
| 01 | `01_sample_sizes_evidence_table.md` | `09_sample_sizes_evidence_table/parameter_evidence_table.md` | Nothing |
| 02 | `02_gender_funnel_template.md` | `06_gender_funnel/gender_data_assessment.md` | Task 01 |
| 03 | `03_halflife_by_trade.md` | `07_halflife_by_trade/trade_halflife_summary.md` + `scenario_chart_data.csv` | Task 02 |
| 04 | `04_private_schooling_validation.md` | `04_private_schooling_validation/validation_plan.md` | Task 01 |

### Checkpoint
| — | `checkpoint_update_tracer_proposal.md` | `tracer_study/deliverables/tracer_onepager.md` (updated) | Tasks 01-04 |

### Phase 2: Synthesis

| Order | Prompt File | Output Location | Depends On |
|-------|------------|-----------------|------------|
| 05 | `05_microdata_access_checklist.md` | `11_microdata_access/microdata_access_checklist.md` | Tasks 02, 03, 04 |
| 06 | `06_evidence_gaps_budget_note.md` | `13_evidence_gaps/evidence_gaps_budget_note.md` | All previous |

### Phase 3: Model & Documentation

| Order | Prompt File | Output Location | Depends On |
|-------|------------|-----------------|------------|
| 07 | `07_policy_persistence.md` | `08_policy_persistence/policy_persistence_scenarios.md` + `persistence_chart_data.csv` | Nothing |
| 08 | `08_assumptions_appendix.md` | `03_assumptions_appendix/assumptions_methodology_appendix.md` | Tasks 01, 07 |

### Phase 4: Final Deliverables

| Order | Prompt File | Output Location | Depends On |
|-------|------------|-----------------|------------|
| 09 | `09_donor_materials.md` | `10_donor_materials/` (3 files) | Tasks 03, 01, 06 |

---

## Key Model Inputs (shared across tasks)
- `src/parameter_registry_v3.py` — parameter source of truth
- `data/Parameter_Sources_Master.csv` — sensitivity ranks, ranges, sources
- `src/economic_core_v4.py` — model calculation logic
- `METHODOLOGY.md` — existing documentation
- `after_delivery/tracer_study/deliverables/tracer_onepager.md` — tracer concept

## Total Deliverables
- 12 output files across 9 folders
- 1 updated tracer proposal
- 1 dependency map (xlsx — already exists)
