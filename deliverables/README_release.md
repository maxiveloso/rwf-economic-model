# RWF Economic Impact Model — Delivery Package v2.0

**February 2026**

---

## Package Contents

### slides/
- **RightWalk_BCR_Baseline_v2.0.pptx** — 25-slide presentation covering model results, deep-dive analyses (gender, trade half-life, policy persistence), evidence audit, tracer study plan, and next steps

### pdfs/
- **donor_onepager_conservative.md** — Wage-only BCR with clear disclaimers (for funder use)
- **donor_onepager_extended.md** — Adds wider social value estimates, clearly labeled as directional

> To export to PDF: open in VS Code, use Cmd+Shift+P > "Markdown: Export to PDF", or use any markdown-to-PDF tool.

### tracer/
- **tracer_onepager_v2.md** — Comprehensive tracer study proposal: 1,200-1,600 sample, 2015-2024 cohorts, Rs 45-55 lakhs, 18 months

### appendices/
| File | Description |
|------|-------------|
| assumptions_methodology_appendix.md | Full parameter table (24 params), formulas, scenarios, limitations |
| parameter_evidence_table.md | 12 parameters ranked by sensitivity with source quality ratings |
| gender_data_assessment.md | Gender funnel analysis, literature benchmarks, 14 priority tracking fields |
| trade_halflife_summary.md | 4-category trade taxonomy with NPV implications by trade mix |
| policy_persistence_scenarios.md | Multi-cohort multiplier analysis (illustrative) |
| microdata_access_checklist.md | 11 datasets with access steps, owners, and compliance notes |
| evidence_gaps_budget_note.md | 8 gaps mapped to cost/timeline; budget summary |
| top5_sources_slide.md | Top 5 evidence sources with sample sizes and confidence |

### data/
- **scenario_chart_data.csv** — Trade half-life scenario data for visualization
- **persistence_chart_data.csv** — Policy persistence year-by-year data for all scenarios

### ops/
- **orchestrator.md** — Task execution flow and dependencies
- **task_dependency_map_v2.xlsx** — Visual dependency map for all workstreams

---

## How to Regenerate the Presentation

```bash
cd github_repo/
python generate_presentation.py
# Output: Presentation_Founders.pptx (25 slides)
```

Requires: `pip install python-pptx`

---

## Reading Order (Recommended)

1. **Slide deck** (slides/) — for the meeting itself
2. **Donor one-pager** (pdfs/) — leave-behind for funders
3. **Tracer proposal** (tracer/) — for approval discussion
4. **Appendices** — for due diligence questions

---

## Key Messages

- Both interventions generate positive returns in ALL 32 scenarios tested
- Conservative headline: wage-only BCR of 13.5:1 (RTE) and 21.7:1 (Apprenticeship)
- Of 12 high-impact parameters, only 1 has HIGH confidence — the tracer study targets the rest
- One investment (Rs 45-55L tracer) closes 7 of 8 evidence gaps simultaneously
- Policy persistence multipliers are illustrative only — single-cohort BCR is the defensible number

---

## Blocking Dependency

**Actual RWF cost data from Shipra** — needed for precise RWF-only BCR. Current figures use estimates (Rs 4,000 RTE, Rs 6,000 Apprenticeship). Annotated in slides as estimates.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | Jan 2026 | Initial PoC: 17-slide deck, core model results |
| v2.0 | Feb 2026 | Added: gender funnel, trade half-life, top-5 sources, tracer plan, policy persistence, assumptions appendix, evidence audit, ask & next steps |
