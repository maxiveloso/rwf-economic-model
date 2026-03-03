# Gender Data Assessment & Collection Plan

## RightWalk Foundation \-- Economic Impact Model

**Date:** February, 2026 **Purpose:** Assess current gender data availability across RWF programs, identify critical gaps, and recommend practical steps for gender-disaggregated tracking that strengthens both the economic model and funder reporting.

---

## 1\. Funnel Stages and Gender-Disaggregated Indicators

RWF operates two distinct program pathways \-- Apprenticeship and RTE \-- each with its own funnel. Below, each stage is defined alongside the gender-disaggregated indicators that would be most valuable for funders and for refining the economic model.

### 1.1 Apprenticeship Program Funnel

| Stage | Definition | Priority Gender Indicators |
| :---- | :---- | :---- |
| **Mobilized** | Youth identified through outreach (community events, school visits, partner referrals) | Female share of mobilized pool; source channel by gender (which outreach channels reach women?) |
| **Registered** | Completed enrollment form, expressed intent to participate | Female registration rate; conversion rate mobilized-to-registered by gender |
| **Enrolled** | Matched with employer and formally enrolled in NATS/NAPS | Female enrollment rate; trade distribution by gender (are women concentrated in lower-wage trades?) |
| **Completed** | Finished full apprenticeship duration, received certificate | Completion rate by gender; top dropout reasons by gender (stipend adequacy, safety, family pressure, harassment) |
| **Certified** | Received formal trade certificate from MSDE/DGT | Certification rate by gender (conditional on completion) |
| **Placed** | Secured employment (formal or informal) within 6 months of completion | Placement rate by gender; formal vs. informal share by gender; wage at placement by gender (F/M ratio) |
| **Formal sector** | In regular/salaried employment with contract, PF/ESI, or payslip verification | P\_FORMAL\_APPRENTICE by gender (this is the model's \#2 parameter by elasticity); formal sector wage by gender |
| **Retained (6 mo)** | Still employed in same or better job at 6-month follow-up | 6-month retention rate by gender; sector persistence (did she stay formal or slip to informal?) |
| **Retained (12 mo)** | Still employed in same or better job at 12-month follow-up | 12-month retention rate by gender; wage growth since placement by gender; job quality indicators by gender |

### 1.2 RTE Program Funnel

| Stage | Definition | Priority Gender Indicators |
| :---- | :---- | :---- |
| **Mobilized** | EWS/DG families identified as eligible for RTE 25% quota | Female child share in mobilized pool; parent awareness level by child gender |
| **Registered** | Application submitted for RTE seat | Application rate by child gender; documentation barriers by gender |
| **Enrolled** | Admitted to private school under RTE quota | Seat fill rate by gender (overall national: 29%); school quality distribution by gender |
| **Completed (Gr 8\)** | Completed elementary schooling (Grade 1-8) in the assigned private school | Retention rate through Grade 8 by gender; transition to Grade 9 by gender; dropout reasons by gender (early marriage, domestic labor, cost barriers) |
| **Completed (Gr 12\)** | Completed higher secondary (the model's treatment endpoint) | Higher secondary completion rate by gender (model assumes 60% overall \-- is this the same for girls?); exam pass rates by gender |
| **Entered labor market** | Entered workforce (employed, self-employed, or seeking) | Labor force participation by gender \-- critical for female outcomes where LFPR is 37% vs. 78% for men (PLFS 2023-24) |
| **Formal sector** | Secured regular/salaried employment | P\_FORMAL\_RTE by gender (model's \#1 parameter by elasticity at 1.11); wage level by gender |
| **Retained (6 mo)** | Still in formal/quality employment at 6 months | Retention and sector persistence by gender |
| **Retained (12 mo)** | Still in formal/quality employment at 12 months | Wage trajectory by gender; further education enrollment by gender |

### 1.3 Why These Indicators Matter for the Model

The economic model currently computes outcomes for four demographic subgroups: Urban Male (UM), Urban Female (UF), Rural Male (RM), Rural Female (RF). Baseline wages from PLFS 2023-24 already encode significant gender gaps:

| Subgroup | Formal (HS) | Informal (Casual) | Gender Gap (vs. male) |
| :---- | :---- | :---- | :---- |
| Urban Male | Rs 32,800/mo | Rs 13,425/mo | \-- |
| Urban Female | Rs 24,928/mo | Rs 9,129/mo | 24% (formal), 32% (informal) |
| Rural Male | Rs 22,880/mo | Rs 11,100/mo | \-- |
| Rural Female | Rs 15,558/mo | Rs 7,475/mo | 32% (formal), 33% (informal) |

However, the two highest-impact parameters are **not gender-disaggregated**:


- **P\_FORMAL\_RTE \= 30%** (expert assumption, elasticity 1.11) \-- same rate applied to all four subgroups  
- **P\_FORMAL\_APPRENTICE \= 68%** (RWF data, elasticity 1.05) \-- same rate applied to all four subgroups

If the true female formal placement rate for apprenticeships is, say, 55% instead of 68%, the model is overstating female apprenticeship NPV by roughly 24%. Conversely, if female RTE graduates have even lower formal entry than 30% due to India's structural LFPR gap, the model overstates female RTE value too. Neither direction can be assessed without gender-disaggregated placement data.

### 1.4 Literature Benchmarks for Expected Gender Gaps

While RWF lacks its own gender-disaggregated outcome data, the academic literature on India's labor market provides calibration points for what the tracer study should expect to find — and for interpreting any interim data that becomes available.

**A. Gender wage penalties are large and pervasive**

The ILO India Wage Report (2018) documents a raw gender wage gap that declined from 48% in 1993–94 to 34% in 2011–12, but with extreme variation by employment type and location:

| Subgroup (2011–12) | Male daily wage (Rs) | Female daily wage (Rs) | Gap |
| :---- | :---- | :---- | :---- |
| Regular urban | 470 | 365 | 22% |
| Regular rural | 324 | 201 | 38% |
| Casual urban | 184 | 112 | 39% |
| Casual rural | 151 | 104 | 31% |

The gap between the best-off group (regular urban males, Rs 470/day) and the worst-off (casual rural females, Rs 104/day) is a factor of 4.5x. This means the informal-to-formal transition has a compounding gender effect: women gain both the formal premium *and* a reduction in the gender gap (from ~35% in casual to ~22–38% in regular employment).

The ILO India report also identifies a "sticky floor" pattern: the gender wage gap is highest at the first decile (105%) and falls to approximately 10% at the ninth decile. This implies that RWF's beneficiaries — who start near the bottom of the wage distribution — face the *widest* gender gaps, and that program effects on formalisation have proportionally greater value for women at these wage levels.

Occupational segregation compounds the gap. Women are concentrated in low-skilled occupations (67% of the female workforce), where they earn only 69% of men's wages. Even in higher-status occupations, significant gaps persist — professionals: women earn 75% of men's wages; technicians: 62%; service/sales workers: 52% (ILO India Wage Report, 2018).

**B. Returns to education are higher for women — but conditional on labor market entry**

Two Indian studies document that women's returns to each additional level of education consistently exceed men's:

| Education level | Women's return | Men's return | Source |
| :---- | :---- | :---- | :---- |
| Secondary | 38.0% | 28.6% | Chen, Kanjilal-Bhaduri & Pastore (2022), PLFS 2018–19 |
| Higher secondary | 58.7% | 38.2% | Chen et al. (2022) |
| Graduate & diploma | 101.5% | 59.9% | Chen et al. (2022) |
| Postgraduate & above | 119.0% | 71.7% | Chen et al. (2022) |
| Secondary (1993/4) | 25.5% | 12.6% | Duraisamy (2002), NSS 50th Round |

This finding is robust across two decades and two different datasets. It implies that the RTE program's education boost — moving beneficiaries from primary to higher secondary completion — is theoretically *worth more per year of schooling* for women than for men.

However, Chen et al. (2022) also estimate a large gender wage penalty after controlling for education and other covariates: −0.264 log points for regular workers and −0.912 log points for self-employed workers. And crucially, these returns are conditional on being in the labor force — with female LFPR at 37% (PLFS 2023–24), a substantial share of women never reach the labor market stage where education returns are realized.

**C. Employment type matters more for women**

Chen et al. (2022) find that yearly returns to education vary dramatically by employment type: 5.5% per year for regular workers, 2.7% for self-employed, and only 0.6% for casual workers. Since women are disproportionately concentrated in self-employment and casual work (ILO India Employment Report, 2024), the *effective* return to education for women depends heavily on whether programs can move them into regular employment — which maps directly to the P\_FORMAL parameter.

**D. Urban-rural gap widens at higher education levels**

Returns to education are similar across urban and rural areas up to higher secondary (urban 44.5% vs. rural 44.3%), but diverge sharply at graduate level (urban 74.3% vs. rural 62.3%) and postgraduate level (urban 89.4% vs. rural 75.1%) (Chen et al., 2022). This is relevant for the model's 4-subgroup structure: the RTE benefit for rural females combines the steepest gender penalty with the smallest location premium, yielding the lowest expected NPV of the four subgroups — a prediction the tracer study can test.

**E. Implications for the tracer study and model**

These literature benchmarks suggest that the tracer study should expect to find:

- **Large gender gaps in formal placement rates** — the structural LFPR gap and occupational segregation data strongly predict that female P\_FORMAL will be below the blended 68% (apprenticeship) and 30% (RTE) figures
- **Higher per-worker returns for women who do enter formal employment** — because the sticky floor effect means women gain more from moving up the wage distribution
- **The biggest model correction will be for rural females** — where LFPR, formal sector access, and geographic premium all work against realising the education return

These are not reasons to update model parameters today (see Section 7), but they provide the tracer design team with calibration points and the model team with priors for sensitivity analysis.

---

## 2\. Current Data Availability Assessment

### 2.1 What RWF Can Likely Extract from Existing Records

Based on the parameter evidence table and model documentation, the following assessment reflects what RWF can realistically derive from current administrative systems.

| Data Point | Available? | Source | Quality Notes |
| :---- | :---- | :---- | :---- |
| Gender of each participant | **Yes** | Enrollment records | Should be in all intake forms. Basis for any disaggregation. |
| Location (urban/rural) | **Likely yes** | Enrollment records | Mapped from school/employer address. May need manual classification. |
| Program stream (Apprenticeship vs. RTE) | **Yes** | Administrative records | Core tracking dimension. |
| Trade/sector for apprentices | **Likely yes** | NATS enrollment | Available at registration. Critical for understanding gender-segregated trade patterns. |
| Completion status (apprenticeship) | **Partial** | RWF tracking | The 85% completion rate is a national estimate. RWF may have own completion tracking for recent cohorts. Gender breakdown unknown. |
| Formal placement status (apprenticeship) | **Partial** | RWF tracking (Nov 2025\) | The 68% figure comes from RWF operational data, but the evidence table flags that cohort size and method need confirmation. Gender breakdown: **not confirmed to exist**. |
| School assigned (RTE) | **Likely yes** | Enrollment records | School name and location should be recorded. |
| Grade progression / retention (RTE) | **Unlikely** | Would require school-level follow-up | RWF likely does not track individual students through Grade 8-12 after initial placement. The 60% retention figure is a national proxy, not RWF data. |
| Post-program employment (either stream) | **No** | Not currently tracked | This is precisely what the tracer study is designed to fill. |
| Wage data | **No** | Not currently tracked | Requires tracer survey with payslip verification. |

### 2.2 What Requires New Data Collection

| Data Point | Why It's Missing | Collection Method |
| :---- | :---- | :---- |
| **P\_FORMAL\_APPRENTICE by gender** | Nov 2025 RWF data reports 68% aggregate but does not split by gender | Re-query RWF tracking database with gender filter; or include in tracer study |
| **P\_FORMAL\_RTE by gender** | No empirical data exists at all (30% is an expert assumption) | Tracer study is the only path |
| **Completion rate by gender (apprenticeship)** | MSDE does not publish dropout rates; RWF may not track systematically | Retrospective query of RWF records; supplement with tracer |
| **RTE retention by gender through Grade 12** | No longitudinal tracking of RTE students exists anywhere | Tracer study (educational attainment questions for 2018-2020 entry cohorts) |
| **Female labor force participation post-program** | PLFS shows national FLFPR at 37%, but no RWF-specific measure | Tracer study: distinguish "not employed" from "not in labor force" for women |
| **Wage levels by gender post-program** | No post-program economic data collected | Tracer study with payslip/contract verification |
| **Dropout reasons by gender** | Not systematically captured | Exit surveys (prospective) \+ retrospective questions in tracer |
| **Trade/sector distribution of placements by gender** | May exist in NATS records but not analyzed | Query NATS records \+ tracer employment questions |

### 2.3 Honest Summary of Gaps

The gap is substantial. RWF's existing data systems are primarily enrollment-focused (who entered the program) rather than outcome-focused (what happened to them after). This is not unusual for an NGO at RWF's stage \-- most Indian skilling organizations face the same constraint. The specific gaps that matter most for the economic model are:

1. **Critical (model-breaking if wrong):** P\_FORMAL rates by gender. The model's two most elastic parameters have zero gender disaggregation. The entire female NPV calculation rests on the assumption that women achieve the same formal placement rates as men \-- an assumption that contradicts India's structural labor market data (FLFPR 37% vs. 68%).  
     
2. **Important (affects credibility):** Completion and retention rates by gender. The apprenticeship completion rate (85%) and RTE retention rate (60%) are applied uniformly. If female dropout is systematically higher (due to early marriage, safety concerns, or family pressure), the model overstates female-specific BCR.  
     
3. **Valuable but not model-critical:** Dropout reasons, trade distribution, and wage ratios by gender. These matter for program design and funder narratives but do not directly change the NPV calculation (which uses PLFS wage levels by demographic subgroup).

**What the literature tells us about the likely direction of these gaps:** The academic evidence reviewed in Section 1.4 suggests these are not hypothetical concerns. Chen et al. (2022) estimate a gender wage penalty of −0.264 log points for regular workers even after controlling for education and experience, while the ILO India Wage Report (2018) documents that 67% of working women are concentrated in low-skilled occupations earning 69% of male wages. The "sticky floor" pattern — where gender gaps reach 105% at the bottom decile — means RWF's beneficiary population sits precisely where the gender penalty is most severe. Taken together, the literature strongly predicts that gender-disaggregated P\_FORMAL rates will be substantially lower for women, that any uniform assumption overstates female outcomes, and that the magnitude of overstatement is likely largest for rural female beneficiaries.

---

## 3\. Recommended Priority Fields to Track Going Forward

These 14 fields represent the minimum practical set that RWF should begin capturing across both programs. They are organized by when in the funnel they should be recorded.

### 3.1 At Enrollment (Fields 1-5)

| \# | Field | Type | Notes |
| :---- | :---- | :---- | :---- |
| 1 | **Gender** | Categorical (M/F/Other) | Almost certainly already captured. Confirm it is in a queryable database field, not just on paper forms. |
| 2 | **Location classification** | Categorical (Urban/Rural) | Derive from address. Align with Census urban/rural definitions. Enables the 4-subgroup model split. |
| 3 | **Trade/sector** (Apprenticeship) | Categorical | NATS trade codes. Track at enrollment. Enables analysis of gender segregation into lower-wage trades. |
| 4 | **School assigned** (RTE) | Text \+ quality tier | School name and UDISE code. Enables linking to school performance data later. |
| 5 | **Household income bracket** | Ordinal (3-4 bands) | Self-reported at intake. Enables poverty-targeted analysis and PSM matching for tracer. Keep bands simple (below BPL / BPL-to-MIS / above MIS). |

### 3.2 During Program (Fields 6-8)

| \# | Field | Type | Notes |
| :---- | :---- | :---- | :---- |
| 6 | **Attendance/engagement flag** | Binary (active/at-risk) | Monthly or quarterly check. A simple "still active" flag is enough. Enables early warning for gender-specific dropout. |
| 7 | **Dropout date and reason** (if applicable) | Date \+ categorical reason | Standardize reason codes: financial, safety/harassment, family obligation, relocation, employer issue, academic difficulty, other. Gender patterns in reasons are highly informative for program design. |
| 8 | **Completion date and certificate status** | Date \+ Y/N | Record actual completion. For RTE, capture which grade was last completed. |

### 3.3 Post-Program Outcomes (Fields 9-14)

These require either the tracer study or a lightweight post-program follow-up system.

| \# | Field | Type | Notes |
| :---- | :---- | :---- | :---- |
| 9 | **Employment status at 6 months** | Categorical (formal employed / informal employed / self-employed / unemployed seeking / not in labor force) | The "not in labor force" category is critical for women. National FLFPR data says 63% of working-age women are outside the labor force entirely. The model cannot distinguish "unemployed" from "withdrew from labor market" without this field. |
| 10 | **Formal sector verification** | Binary (Y/N) \+ method | PF/ESI enrollment, employment contract, or payslip. Maps directly to P\_FORMAL by gender. |
| 11 | **Monthly take-home wage** | Continuous (INR) | Self-reported \+ verification for 15-20% subsample. Maps to APPRENTICE\_INITIAL\_PREMIUM and gender wage ratio. |
| 12 | **Sector/industry of employment** | Categorical (NSSO NIC codes, simplified) | Manufacturing / services / construction / agriculture / other. Reveals whether women are placed into lower-paying sectors even when "formally" employed. |
| 13 | **Employment status at 12 months** | Same as Field 9 | Repeat measure. Enables retention rate by gender and maps to APPRENTICE\_DECAY\_HALFLIFE estimation. |
| 14 | **Highest education completed** (RTE only) | Grade level | For RTE alumni from 2018-2020 cohorts: what grade did they actually reach? Directly measures RTE\_RETENTION\_FUNNEL by gender. |

### 3.4 What Was Deliberately Left Out

To keep this practical, the following were excluded from the priority list despite being analytically interesting:

- **Health and wellbeing indicators** \-- valuable for extended SROI narrative but not for the economic model's NPV calculation  
- **Hours worked** \-- relevant for job quality analysis but adds survey burden  
- **Savings/asset accumulation** \-- interesting for wealth effects but requires financial literacy questions  
- **Intra-household bargaining power** \-- important for gender research but requires validated instruments (e.g., WEAI) that are too lengthy for a tracer bolt-on  
- **Marriage/fertility status** \-- contextually relevant for understanding female LFPR but sensitive to collect and not directly model-linked

---

## 4\. Tracer Study Integration: Gender Variables and Disaggregation

The tracer study one-pager proposes 300-400 RTE beneficiaries, 300-400 apprenticeship completers, and 600-800 comparison group members (total 1,200-1,600, targeting 70%+ response rate). This section specifies how gender should be embedded throughout.

### 4.1 Gender-Related Variables to Embed in the Tracer Instrument

These variables should be added to (or confirmed present in) the tracer questionnaire, beyond the 14 priority tracking fields above.

**A. Female labor force participation module (3-4 questions)**

This is the single most important gender-specific addition to the tracer. India's female LFPR is 37% nationally (PLFS 2023-24). If the tracer simply asks "Are you employed?" and codes non-employed women as "unemployed," it will conflate two completely different situations: women who want to work but cannot find jobs, and women who have withdrawn from the labor force due to marriage, childcare, family norms, or safety concerns. The economic model treats these differently \-- the first group has unrealized earnings potential, the second may not generate any labor market return regardless of program quality.

Recommended questions:

1. "Are you currently working for pay or profit?" (Y/N)  
2. If no: "Have you looked for work in the past 3 months?" (Y/N \-- distinguishes unemployed from NILF)  
3. If no to both: "What is the main reason you are not working or looking for work?" (Categorical: household responsibilities / childcare / further education / health / family does not allow / no suitable jobs nearby / other)  
4. "If a suitable job were available near your home, would you want to work?" (Y/N \-- reveals latent labor supply)

**B. Workplace safety and discrimination (2-3 questions)**

For female apprenticeship completers and employed RTE alumni:

1. "Have you experienced any harassment or uncomfortable situations at your workplace?" (Frequency scale: never / rarely / sometimes / often)  
2. "Do you feel your gender has affected your job opportunities or pay?" (Y/N \+ open text)  
3. "Were there trade/job options you wanted but could not access due to gender restrictions?" (Y/N \+ specify)

These are not model inputs but are essential for interpreting why female formal placement rates may differ from male rates and for program improvement.

**C. Household decision-making (1-2 questions)**

1. "Who in your household decided that you should join this program?" (Self / parent-father / parent-mother / spouse / other)  
2. "Who decides how your earnings are used?" (Self / shared / other family member)

Relevant for understanding whether female economic gains translate to actual welfare improvements.

**D. Alternative outcomes for women (1-2 questions)**

1. "Have you enrolled in or completed any further education since leaving the program?" (Y/N \+ highest level)  
2. "Have you started any business or self-employment activity?" (Y/N \+ monthly income)

Women may channel program benefits into self-employment or further education rather than formal employment \-- this should be captured rather than treated as a "failure" of the formal placement pathway.

### 4.2 Disaggregation Dimensions for All Tracer Analysis

Every outcome variable in the tracer should be reported along these cross-cutting dimensions:

| Dimension | Categories | Rationale |
| :---- | :---- | :---- |
| **Gender** | Male / Female | Primary disaggregation. Must be reported for every outcome. |
| **Gender x Location** | Urban Female / Urban Male / Rural Female / Rural Male | Maps directly to the model's 4-subgroup structure. This is the minimum disaggregation for updating model parameters. |
| **Gender x Program** | Female Apprentice / Male Apprentice / Female RTE / Male RTE | Reveals whether gender gaps differ by program stream. |
| **Gender x Trade** (Apprenticeship) | Female in manufacturing / Female in services / Male in manufacturing / Male in services | Tests whether trade segregation explains placement gaps. |
| **Gender x Cohort vintage** | Female 2018-20 completers / Female 2021-24 completers / Male equivalents | Enables cross-cohort analysis for APPRENTICE\_DECAY\_HALFLIFE by gender. |

### 4.3 Sample Size Implications for Gender Disaggregation

The parameter evidence table (Task \#9) established that the tracer's 300-400 per program arm is adequate for overall parameter estimation. But gender disaggregation effectively halves the per-cell sample size.

**Critical constraint:** If women are 40% of apprenticeship completers (a plausible estimate given India's skilling gender composition), then from 300-400 completers the tracer would yield:

- Female apprentices: 120-160  
- Male apprentices: 180-240

For detecting P\_FORMAL\_APPRENTICE by gender (e.g., female 60% vs. male 78%):

- Effect size: 18 percentage points  
- N per arm (simple): \~7.84 x \[0.60x0.40 \+ 0.78x0.22\] / 0.18^2 \= 7.84 x \[0.24 \+ 0.17\] / 0.032 \= \~100 per arm  
- With 120-160 females: **adequate** for detecting an 18pp gender gap

For detecting a smaller gender gap (e.g., female 65% vs. male 68%, a 7pp difference):

- N per arm: \~7.84 x \[0.65x0.35 \+ 0.68x0.28\] / 0.07^2 \= 7.84 x \[0.23 \+ 0.20\] / 0.0049 \= \~669 per arm  
- With 120-160 females: **not adequate** \-- would need \~700 per gender

**Implication:** The tracer sample is sufficient to detect large gender gaps (\>15pp) but will not have power to detect moderate gaps (5-10pp) within each program. This is an unavoidable constraint at the proposed budget. The tracer should:

1. Report point estimates with confidence intervals for each gender subgroup, acknowledging wide CIs for female-specific estimates  
2. Pool across programs where appropriate (e.g., overall female formal placement rate across both streams)  
3. Flag gender-disaggregated estimates as "indicative" rather than "statistically confirmed" when per-cell n \< 100

For RTE, the gender composition constraint is different. RTE benefits children admitted to schools, so the male/female split should be closer to 50/50 if admission is equitable. With 300-400 RTE beneficiaries, expect 150-200 per gender \-- adequate for detecting large gaps in educational attainment but marginal for employment outcomes (which require labor market entry, reducing effective n for women given low FLFPR).

### 4.4 Gender-Specific Sampling Considerations

| Issue | Recommendation |
| :---- | :---- |
| **Female response rate** | May be lower than male, especially for married women or those in conservative households. Budget for 2-3 callback attempts. Offer female enumerator option. Response rate target: 65%+ for women (vs. 75%+ for men). |
| **Phone vs. in-person** | Phone surveys reduce safety concerns for female respondents but miss non-verbal cues and document verification. Use phone for initial contact, in-person for verification subsample. |
| **Proxy respondents** | If a female beneficiary is unavailable, the survey may reach a family member. This is common in India but introduces reporting bias (family may overstate employment or understate wages). Code proxy vs. self-report as a data quality flag. |
| **Seasonal employment** | Women in rural areas may have seasonal agricultural employment that does not show up in a point-in-time survey. Ask about employment in the last 12 months, not just current status. |
| **Migration** | Male apprenticeship completers are more likely to have migrated for work. Female completers may stay local due to family constraints. Track current location vs. program location. |

---

## 5\. Immediate Actions: What RWF Can Do Before the Tracer

The tracer study is 18-30 months away from delivering results (design \+ IRB \+ fieldwork \+ analysis). In the interim, RWF can take three concrete steps that cost little and yield gender data quickly.

### 5.1 Action 1: Re-query the 68% Figure by Gender (1-2 weeks)

The November 2025 RWF tracking data that produced P\_FORMAL\_APPRENTICE \= 68% is the model's only HIGH-confidence parameter. If the underlying database records gender (which it almost certainly does since it tracks individual apprentices), a simple filter query could produce:

- P\_FORMAL\_APPRENTICE (Male) \= ?%  
- P\_FORMAL\_APPRENTICE (Female) \= ?%  
- N per gender

This single data point would immediately improve the model. Even a rough split (e.g., "of the N completers tracked, X% were female, and Y% of those females entered formal employment") would be more informative than the current uniform 68% assumption.

**Who:** RWF operations team **Deliverable:** One table with placement rate by gender, with cohort size **Timeline:** 1-2 weeks

### 5.2 Action 2: Add Gender Tabulation to Enrollment Reports (Ongoing)

If RWF produces monthly or quarterly enrollment reports, add a standard gender breakdown row. This costs zero additional data collection \-- it is a reporting format change. Over 2-3 quarters, it will establish the gender composition of each program pipeline, which is necessary for:

- Tracer sampling frames (how many women to expect per cohort)  
- Funder reporting on gender reach  
- Internal benchmarking on gender equity

**Who:** RWF M\&E / reporting team **Deliverable:** Updated report template with gender rows **Timeline:** Next reporting cycle

### 5.3 Action 3: Pilot a Lightweight Exit Survey (3-6 months)

For the next 2-3 cohorts of apprenticeship completers (before the tracer study begins), administer a short (10-question) phone survey at program exit. Include:

1. Gender (confirm from records)  
2. Trade completed  
3. Employment status (employed / seeking / not in labor force)  
4. If employed: formal or informal (contract? PF/ESI?)  
5. If employed: monthly take-home pay  
6. If not employed: main reason  
7. Satisfaction with program (1-5 scale)  
8. Would you recommend to a female friend/relative? (Y/N)  
9. Location (same as during program / migrated)  
10. Contact information for future follow-up

This serves dual purpose: (a) generates immediate gender-disaggregated outcome data, and (b) builds a contact database for the tracer study's retrospective sampling.

**Who:** RWF program team \+ 1 part-time enumerator **Cost:** \~Rs 1-2 lakhs for 200-300 surveys **Timeline:** Begin with next completing cohort

---

## 6\. Summary: Priority Matrix

| Priority | Action | Data Yield | Cost | Timeline |
| :---- | :---- | :---- | :---- | :---- |
| **1 (Immediate)** | Re-query 68% by gender | P\_FORMAL\_APPRENTICE by gender | Near zero | 1-2 weeks |
| **2 (Quick win)** | Gender rows in enrollment reports | Pipeline composition by gender | Near zero | Next report cycle |
| **3 (Short-term)** | Pilot exit survey | Employment, wages, LFPR by gender | Rs 1-2 lakhs | 3-6 months |
| **4 (Medium-term)** | Embed 14 priority fields in MIS | Full funnel tracking by gender | System update cost | 6-12 months |
| **5 (Tracer study)** | Gender module in tracer instrument | Validated P\_FORMAL, wages, retention by gender | Included in tracer budget | 18-30 months |

---

## 7\. What This Means for the Economic Model

### 7.1 Should the Model Be Updated Now?

**No.** The literature data reviewed in Section 1.4 strengthens the *case for collecting* gender-disaggregated data, but it does not provide actionable parameter updates for the model itself. Here is why:

1. **The model's wage inputs already reflect gender gaps.** Baseline wages come from PLFS 2023–24 and are split by the four subgroups (UM/UF/RM/RF). The ILO and Duraisamy/Chen et al. findings on gender wage gaps are *consistent with* these PLFS values but do not supersede them — PLFS is more recent and directly applicable.

2. **The critical missing parameters are RWF-specific transition probabilities.** P\_FORMAL\_APPRENTICE and P\_FORMAL\_RTE are about *what share of RWF's own beneficiaries* enter formal employment. No external literature — however robust — can substitute for this. The ILO "sticky floor" data or Chen et al.'s gender wage penalty tell us what happens in the general labor market, not what happens to RWF program completers specifically.

3. **Returns to education from the literature do not directly map to model parameters.** The model uses a Mincerian return framework calibrated to Indian data. The Chen et al. (2022) and Duraisamy (2002) returns-to-education estimates are informative priors, but the model already has its own values for MINCER\_BETA\_SCHOOLING derived from appropriate sources. Swapping in a different paper's estimate without recalibrating the entire earnings equation would introduce inconsistency.

4. **Using literature data as a proxy for RWF data would create a false sense of precision.** Reporting "female P\_FORMAL\_APPRENTICE = 55% (based on ILO structural data)" sounds empirical but is actually a guess with an academic citation attached. The current model is transparent that it applies 68% uniformly — a known limitation, clearly documented. Replacing this with a literature-derived estimate that has no RWF-specific basis would obscure the real gap in evidence.

**The right use of this literature is for sensitivity analysis and tracer study calibration**, not parameter substitution.

### 7.2 How the Model Should Be Updated — In Stages

Once gender-disaggregated data begins flowing from RWF's own operations and the tracer study, the model can be updated in stages:

**Stage 1 (from Action 1):** Replace uniform P\_FORMAL\_APPRENTICE = 68% with gender-specific values. Recompute apprenticeship NPV for each of the four subgroups. If the female rate is significantly lower (e.g., 55–60%), the blended program NPV will decrease, but the per-female estimate becomes more honest. This is straightforward — a single parameter change in the model's scenario configuration.

**Stage 2 (from tracer Year 1):** Replace expert-assumed P\_FORMAL\_RTE = 30% with a gender-disaggregated empirical estimate. Given that female LFPR in India is 37% and the control group formal rate is ~9%, a realistic female P\_FORMAL\_RTE might be 15–25% rather than 30%. This would substantially change the female RTE NPV — but the current model is likely overstating it by applying the male-calibrated 30% uniformly.

**Stage 3 (from tracer Year 1+):** Introduce gender-specific completion rates, retention rates, and wage trajectories into the model. The wage levels by gender are already built in (PLFS 2023–24 data). The missing pieces are the transition probabilities.

### 7.3 The Picture Is More Complex Than "Female NPV Will Go Down"

The earlier version of this assessment predicted that gender-disaggregated data would likely *lower* female NPV estimates. The literature benchmarks in Section 1.4 reveal a more nuanced picture with two opposing forces:

**Force 1 — Lower formal placement rates will reduce female NPV.** This remains the dominant effect. If female P\_FORMAL is lower than the uniform assumption, fewer women generate the formal wage premium, and female-specific NPV drops. The literature strongly predicts this direction: the ILO India Employment Report (2024) shows women disproportionately in self-employment and informal work, and Chen et al. (2022) document a gender wage penalty of −0.264 log points for regular workers and −0.912 for self-employed workers, even after controlling for education.

**Force 2 — Higher returns to education increase the *per-woman* benefit for those who do enter formal work.** Chen et al. (2022) and Duraisamy (2002) both show that women's returns to each additional level of education consistently exceed men's — at secondary level, 38.0% vs 28.6%; at higher secondary, 58.7% vs 38.2%. The ILO India Wage Report's "sticky floor" finding reinforces this: the gender gap is 105% at the first decile but only 10% at the ninth decile. Moving a woman from informal to formal employment — from the bottom of the wage distribution toward the middle — closes a proportionally larger gap than the equivalent move for a man. This means the *treatment effect* of formal placement may be larger for women, even if fewer women reach that stage.

**Net effect:** For the *average female beneficiary* (including those who never enter the labor force), NPV will likely decrease once gender-specific data is applied. But for the *subgroup of women who do achieve formal placement*, the per-capita NPV may be higher than the male equivalent — because each year of education and each step up the formality ladder closes a wider gap for women.

This distinction matters for funder communication. The narrative is not simply "the program works less well for women." It is: "the program's *potential* return for women is higher, but structural barriers (LFPR, occupational segregation, discrimination) prevent a larger share of women from realising that return. Addressing those barriers — through targeted placement support, safe workplace initiatives, and sector diversification — is where additional investment creates the most value."

### 7.4 What Can Be Done Now Without Changing the Model

While the model parameters should not be updated until RWF-specific data is available, the literature benchmarks support two immediate analytical steps:

1. **Run sensitivity scenarios using literature-informed priors.** The model's existing sensitivity analysis can test: "What happens to female NPV if P\_FORMAL\_APPRENTICE (Female) is 50%, 55%, or 60% instead of 68%?" These are not parameter updates — they are clearly labeled scenario analyses that bracket the plausible range informed by literature. The Chen et al. gender wage penalty (−0.264 for regular workers) and the ILO "sticky floor" data provide empirical grounding for choosing which scenario values to test.

2. **Document the expected direction of bias in current estimates.** The model documentation and any funder-facing materials should note that the uniform P\_FORMAL assumption likely *overstates* female outcomes, cite the literature basis for this expectation, and flag that the tracer study is designed to resolve this. Transparency about known limitations is more credible than silence.

---

*Document prepared: February 16, 2026; updated February 17, 2026* *Inputs: parameter\_evidence\_table.md (Task \#9), tracer\_onepager.md, parameter\_registry\_v3.py (v3.4), economic\_core\_v4.py* *Cross-referenced against: PLFS 2023-24 wage data, ILO India Wage Report (2018), ILO India Employment Report (2024), ILO Global Wage Report (2024-25), Chen, Kanjilal-Bhaduri & Pastore (2022), Duraisamy (2002), Muralidharan & Sundararaman (2013)*