# Source trace

Criteria come only from the two SYNTHETIC abstracts named in the task brief. No full-text body was present, so **no criterion is tagged `full-text`**.

**Constraint:** PLAN is a research plan with no results. Do not call the PLAN framework validated.

## Source inventory

### PLAN — *A Quality-Task Checklist for Model Comparison — A Research Plan*

Abstract (complete):

> This research PLAN will develop quality-assurance guidelines for the model-building phase. Three gaps remain: no QA guidelines, unclear quality-task processes at each phase, and insufficient reporting standards for model performance needed for model comparison. Planned methods are a literature study, expert validation, and a pilot project with two development teams. No results are reported.

### CASE — *A Case Study on Desk-Checking and Variability Coverage*

Abstract (complete):

> This case study evaluates feasibility and acceptance as separate questions for two parts of a QA process: variability-model creation and desk-checking. Desk-checking is a checklist-guided self-review before check-in, not a structured inspection. Variability modeling was feasible, but a different modeling language was needed to represent all important variants. Developers accepted both parts. The study reports that limit.

## Criterion map

| ID | Tag | Source | Verbatim span used | Derivation |
| --- | --- | --- | --- | --- |
| C01 | abstract-only | PLAN | "quality-assurance guidelines for the model-building phase" / "no QA guidelines" | Direct. Presence of model-building QA guidelines, or a stated gap plus a plan to develop them. |
| C02 | abstract-only | PLAN | "unclear quality-task processes at each phase" | Direct. Quality-task processes specified or planned per phase. |
| C03 | abstract-only | PLAN | "insufficient reporting standards for model performance needed for model comparison" | Direct. Performance reporting adequate for comparison. |
| C04 | abstract-only | PLAN | "Planned methods are a literature study" | Direct. Literature study used or planned. |
| C05 | abstract-only | PLAN | "expert validation" | Direct as a **method item**. Planned expert validation is not framework validation. |
| C06 | abstract-only | PLAN | "a pilot project with two development teams" | Direct. Two-team pilot used or planned. |
| C07 | abstract-only | PLAN | "No results are reported." | Direct. Whether empirical results appear. PLAN scores 0 on this row. |
| C08 | abstract-only | CASE | "evaluates feasibility and acceptance as separate questions" | Direct. |
| C09 | abstract-only | CASE | "two parts of a QA process: variability-model creation and desk-checking" | Direct. Variability-model creation treated as its own QA part. |
| C10 | abstract-only | CASE | "Desk-checking is a checklist-guided self-review before check-in, not a structured inspection." | Direct. Wrong if desk-checking is treated as inspection. |
| C11 | abstract-only | CASE | "a different modeling language was needed to represent all important variants" | Direct. Language coverage of important variants, or an explicit shortfall. |
| C12 | abstract-only | CASE | "Developers accepted both parts." | Direct. Acceptance of both QA parts. |
| C13 | abstract-only | CASE | "The study reports that limit." | Direct. Limits disclosed. |
| C14 | adapted | PLAN + CASE | PLAN: guidelines, quality-task processes, reporting standards. CASE: variability-model creation and desk-checking. | Combined: QA process decomposed into identifiable parts. |
| C15 | adapted | PLAN + CASE | PLAN: "This research PLAN" / "No results are reported." CASE: results plus "The study reports that limit." | Combined: claim type matches evidence (plan vs completed study). A plan must not be scored as a validated framework. |

## Tags not used

| Tag | Count | Reason |
| --- | --- | --- |
| full-text | 0 | SYNTHETIC files stop after the abstract. No body text was read. |

## What was not taken as evidence

- Titles were used only to identify papers, not as extra criteria.
- No DOI, venue, or citation chase.
- No other repository files.
- PLAN's phrase "expert validation" was **not** treated as a completed validation of a framework.
