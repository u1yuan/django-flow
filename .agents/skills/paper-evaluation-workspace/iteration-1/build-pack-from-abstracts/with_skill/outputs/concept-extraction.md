# QA concept extraction

Sources and access levels are in `source-trace.md`. Both papers are SYNTHETIC invented abstracts. Locators are Title or Abstract. Quotes are 25 words or fewer. SYN-PLAN is a research plan. None of its concepts is a completed finding, and its planned guidelines are not a validated framework.

## SYN-PLAN: A Quality-Task Checklist for Model Comparison — A Research Plan

| ID | Concept | Location | Short quote |
| --- | --- | --- | --- |
| P-1 | The file labels the work a research plan and reports no results | Title; Abstract | "This research PLAN will develop quality-assurance guidelines for the model-building phase." |
| P-2 | Intended output is QA guidelines for the model-building phase | Abstract | "quality-assurance guidelines for the model-building phase" |
| P-3 | Gap: no QA guidelines | Abstract | "Three gaps remain: no QA guidelines" |
| P-4 | Gap: quality-task processes at each phase are unclear | Abstract | "unclear quality-task processes at each phase" |
| P-5 | Gap: reporting standards for model performance are insufficient for model comparison | Abstract | "insufficient reporting standards for model performance needed for model comparison" |
| P-6 | Planned methods: literature study, expert validation, and a two-team pilot | Abstract | "a literature study, expert validation, and a pilot project with two development teams" |
| P-7 | No results are reported | Abstract | "No results are reported." |

## SYN-CASE: A Case Study on Desk-Checking and Variability Coverage

| ID | Concept | Location | Short quote |
| --- | --- | --- | --- |
| C-1 | The file labels the work a completed case study | Title; Abstract | "This case study evaluates feasibility and acceptance as separate questions" |
| C-2 | Feasibility and acceptance are separate questions | Abstract | "evaluates feasibility and acceptance as separate questions" |
| C-3 | The QA process has two parts: variability-model creation and desk-checking | Abstract | "two parts of a QA process: variability-model creation and desk-checking" |
| C-4 | Desk-checking is a checklist-guided self-review before check-in, not a structured inspection | Abstract | "Desk-checking is a checklist-guided self-review before check-in, not a structured inspection." |
| C-5 | Variability modeling was feasible | Abstract | "Variability modeling was feasible" |
| C-6 | A different modeling language was needed to represent all important variants | Abstract | "a different modeling language was needed to represent all important variants" |
| C-7 | Developers accepted both parts | Abstract | "Developers accepted both parts." |
| C-8 | The study reports that coverage limit | Abstract | "The study reports that limit." |

## Candidate seeds from the brief: confirmed or discarded

| Seed | Decision | Basis |
| --- | --- | --- |
| PLAN: no QA guidelines | **Confirmed** as a stated gap, not as a result | P-3 |
| PLAN: unclear quality-task processes at each phase | **Confirmed** as a stated gap | P-4 |
| PLAN: insufficient performance-reporting standards for model comparison | **Confirmed** as a stated gap | P-5 |
| PLAN: literature study, expert validation, two-team pilot | **Confirmed** as planned methods. Not treated as completed validation | P-6, P-7 |
| PLAN framework is validated | **Discarded.** The abstract reports no results. The planned guidelines are not described as validated | P-1, P-7 |
| CASE: feasibility and acceptance as separate questions | **Confirmed** | C-2, C-5, C-7 |
| CASE: desk-checking is a structured inspection | **Discarded.** The abstract states the opposite | C-4 |
| CASE: desk-checking is a checklist-guided self-review before check-in | **Confirmed** | C-4 |
| CASE: variability modeling was feasible but needed another language for important variants | **Confirmed** | C-5, C-6 |
| CASE: developers accepted both parts | **Confirmed** | C-7 |
| CASE: the study reports that limit | **Confirmed** | C-8 |

## Design principle taken from SYN-CASE

C-4 defines desk-checking as a checklist-guided self-review. `desk-check-checklist.md` uses that idea as a pre-scoring self-review. That use is an adaptation: the source sentence describes a QA process part, not a paper-evaluation workflow.

Score anchors (0/1/2) are operational wording written for this pack. They are not quoted from either abstract.
