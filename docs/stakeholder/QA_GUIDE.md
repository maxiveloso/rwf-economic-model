# RWF Economic Impact Assessment
## Stakeholder Q&A Guide

**Purpose:** Anticipated questions from RWF stakeholders, funders, and board members with prepared responses.

---

## Q1: Are these results causal?

**Answer:**
No, these are correlation-based estimates that assume away selection bias. True causal effects could be 20-40% lower if motivated families self-select into private schools or apprenticeships.

A full evaluation with matched control groups and longitudinal data would address this concern. However, even with a 40% haircut, both interventions remain cost-effective.

**Key point:** These are directionally correct order-of-magnitude estimates, not precise causal effects.

---

## Q2: Why are results so different across regions?

**Answer:**
This reflects real labor market differences across India:
- South has approximately 2x the formal sector employment rate compared to East
- Urban areas have higher wage levels and more formal sector opportunities
- Gender gaps in formal employment vary by region

**Implications:**
- Consider focusing expansion on high-return regions (South/West urban)
- For low-return regions, consider complementary interventions (migration support, local formal sector development)
- Regional targeting can improve overall program cost-effectiveness

---

## Q3: What's the single most important thing to improve this analysis?

**Answer:**
A 1-2 year longitudinal tracer study tracking 200-300 beneficiaries to measure actual wage trajectories.

This would:
1. **Validate P_FORMAL assumptions** - Is 30% formal entry for RTE graduates accurate?
2. **Pin down wage persistence (h)** - Does the Apprenticeship premium really last 12+ years?
3. **Measure actual wages** - Are our PLFS-based projections realistic?

**Cost:** Approximately Rs 5-8 lakhs
**Impact:** Would reduce uncertainty by 50%+ and convert PoC to causal evaluation

---

## Q4: Should we use these results to decide between expanding RTE vs. Apprenticeship?

**Answer:**
With appropriate caveats, yes. Key trade-offs to consider:

| Factor | RTE | Apprenticeship |
|--------|-----|----------------|
| Average LNPV | Rs 9L | Rs 36L |
| Upfront cost | Lower | Higher |
| Operational complexity | Lower | Higher |
| Time to impact | Longer (education pathway) | Shorter (direct employment) |
| Scalability | Higher | Lower |
| Uncertainty | Lower (education effects well-studied) | Higher (h parameter uncertain) |

**Decision depends on:** Budget constraints, target population demographics, organizational capacity, and whether you prioritize immediate placement (Apprenticeship) vs. long-term human capital formation (RTE).

---

## Q5: Why is the RTE benefit mostly from 'placement effect' rather than learning?

**Answer:**
Our decomposition analysis shows ~80% of RTE LNPV comes from the formal sector entry differential (30% vs 9.1%), not from test score gains.

Three possible interpretations:
1. **Signaling:** Private school credentials signal quality to employers, regardless of actual learning differences
2. **Network effects:** Private school connections and social capital open formal sector doors
3. **Confounding:** Families choosing private schools may have other unobserved advantages

**Important caveat:** This doesn't mean learning doesn't matter—it means the formal sector pathway is the primary *mechanism* through which RTE generates economic returns.

**Policy implication:** RTE programs should consider adding career guidance and placement support to maximize the formal sector pathway.

---

## Q6: What if our actual costs are higher than your break-even thresholds?

**Answer:**
The break-even analysis provides decision rules for different scenarios:

| Scenario | Break-Even at BCR=3:1 | Interpretation |
|----------|----------------------|----------------|
| RTE Urban South | Rs 6.0L/beneficiary | Can sustain high program costs |
| RTE Rural East | Rs 1.3L/beneficiary | Cost-sensitive, needs efficiency |
| Apprenticeship Urban | Rs 12-18L/beneficiary | Substantial cost tolerance |
| Apprenticeship Rural | Rs 6-8L/beneficiary | Moderate cost tolerance |

**If your costs exceed these thresholds, three options:**
1. **Focus:** Prioritize regions/demographics where you're clearly above threshold
2. **Reduce costs:** Identify operational efficiencies
3. **Accept lower BCR:** Some regions may still be worth serving at BCR=2:1 for equity or strategic reasons

---

## Q7: How confident are you in the 30% formal entry rate for RTE graduates?

**Answer:**
This is our highest-uncertainty parameter (Tier 1). The 30% estimate is based on:
- RWF guidance and program theory
- Literature suggesting private schooling improves formal outcomes 3x over baseline
- ILO 2024 data showing 9.1% baseline for higher secondary graduates

**Sensitivity analysis:**
- If actual rate is 20%: RTE LNPV drops ~30%
- If actual rate is 50%: RTE LNPV increases ~50%
- Even at 20%, RTE remains cost-effective for most scenarios

**Recommendation:** A tracer study following 100 RTE beneficiaries 2 years post-graduation would resolve this. It's the single most valuable data RWF could collect.

---

## Q8: Why do Apprenticeship results vary so much with half-life (h)?

**Answer:**
Because Apprenticeship benefits depend critically on whether vocational skills remain relevant over time:

| Half-Life | Interpretation | LNPV Impact |
|-----------|---------------|-------------|
| h=5 years | Skills become obsolete quickly (e.g., rapidly changing technology) | -40% |
| h=12 years | Moderate skill persistence (baseline assumption) | Baseline |
| h=30 years | Durable skills (e.g., electrical, plumbing, welding) | +30% |

RTE doesn't have this problem because education creates a permanent credential that doesn't depreciate.

**Implications for Apprenticeship program design:**
1. Focus on trades with durable, transferable skills
2. Build in upskilling/reskilling pathways for apprentices
3. Avoid sectors with rapid technological change unless paired with continuous learning

---

## Q9: What about the informal sector? Are we ignoring 90% of the labor market?

**Answer:**
No—we explicitly model informal sector outcomes. Key insight:

- Informal sector wages show **-0.2% real growth** annually
- Formal sector wages show **+1.5% real growth** annually
- Today's 2.44x formal/informal wage gap becomes **3-4x by retirement**

**This means:** Interventions that improve formal sector entry rates have **compounding returns** over a 40-year career. The gap widens, not narrows.

**This is why P_FORMAL is our #1 NPV driver**, not the initial wage premium. Getting someone into formal employment has larger lifetime effects than giving them a higher starting wage in the informal sector.

---

## Q10: Can we trust parameters from 2019-2022 studies in 2026?

**Answer:**
Valid concern. Here's what we used and the risks:

| Parameter | Source Year | Risk |
|-----------|-------------|------|
| Wages | PLFS 2023-24 | Low - current data |
| Mincer returns | Chen et al. 2022 | Low - most recent India estimate |
| Test score effects | NBER RCT 2013 | Medium - no newer RCTs available |
| Formal employment rates | ILO 2024 | Low - current data |

**What could have changed:**
1. Post-COVID labor market recovery - formal employment rates may differ
2. Skill premium evolution - Mincer returns could be higher/lower
3. RWF program maturation - your outcomes may differ from national averages

**Mitigation:** Our sensitivity ranges are deliberately wide enough to capture reasonable shifts. Monte Carlo 5th-95th percentile brackets most plausible scenarios.

---

## Q11: What's the policy implication for government/donors?

**Answer:**
Three key takeaways:

1. **Both interventions pass cost-effectiveness thresholds** even under pessimistic assumptions—continued investment is justified

2. **Formal sector entry is the key mechanism**—policies should focus on employment pathways, not just learning outcomes. Consider linking RTE to career guidance/placement support.

3. **Regional targeting matters**—South/West urban returns are 50%+ higher than North/East rural. Strategic geographic focus improves overall impact.

**For government:** RTE quota enforcement is valuable, but only if it translates to formal employment. Consider policy linkages between education and labor market programs.

**For donors:** Apprenticeship has higher ROI but higher complexity. RTE is simpler to scale but requires longer time horizons to realize returns.

---

## Q12: How does this compare to other education/training interventions globally?

**Answer:**
Our estimates are consistent with global benchmarks:

| Intervention Type | Typical BCR Range | Our Estimates |
|-------------------|-------------------|---------------|
| Primary education (World Bank) | 10:1 - 15:1 | N/A |
| Secondary education | 5:1 - 10:1 | RTE: 3:1 - 8:1 (depending on costs) |
| Vocational training (ILO) | 2:1 - 6:1 | Apprenticeship: 4:1 - 12:1 |
| Job training programs (J-PAL) | 1:1 - 4:1 | Within range |

Our Apprenticeship estimates are on the higher end, which is plausible given RWF's 68% placement rate (well above national average). RTE estimates are conservative, reflecting our honest uncertainty about the causal pathway.

---

## Quick Reference: Key Numbers

| Metric | RTE | Apprenticeship |
|--------|-----|----------------|
| Average LNPV | Rs 14.0L | Rs 34.4L |
| LNPV Range | Rs 5.2L - Rs 28.7L | Rs 18.6L - Rs 52.3L |
| Max Cost at BCR=3:1 (mean) | Rs 4.7L | Rs 11.5L |
| Decomposition | 80% Placement / 20% Mincer | N/A |
| Key Driver | P_FORMAL_RTE | P_FORMAL_APPRENTICE, h |
| Validation Status | 6/8 checks passed | 6/8 checks passed |

---

**Prepared by:** RWF Analytics Team
**Date:** January 2026
**Model Version:** economic_core_v4.py
