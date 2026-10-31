# Evaluation: SYN-PLAN

**Pilot draft by `ai-draft`.** A human must check every score and quote before these scores are used.

## Paper

| Field | Value |
| --- | --- |
| paper_id | SYN-PLAN |
| DOI | unavailable |
| Citation | Title only: A Quality-Task Checklist for Model Comparison — A Research Plan. Authors, year, venue, and pages unavailable |
| Metadata source used to verify citation | Local SYNTHETIC file header. No Crossref or publisher record was retrieved |
| Reviewer | ai-draft |
| rubric_version | 1.0.0 |
| Evaluation date | 2026-10-31 |
| Copy used and path | Local SYNTHETIC file `.agents/skills/paper-evaluation/evals/files/SYNTHETIC_paper_plan.txt` |
| Access date | 2026-10-31 |
| Access level | Abstract only |
| Locator scheme | Title; Abstract. No pages |
| Study status | **Research plan.** Title contains "A Research Plan". Abstract: future tense and "No results are reported." The planned guidelines are not a validated framework |
| Is this paper a source of the rubric? | **Yes** (C01–C04). These scores test rubric consistency. They are not independent evidence about the rubric |

## Desk-check (`desk-check-checklist.md`)

| # | Done | Note |
| --- | --- | --- |
| 1 Identity | Yes | Title matches the file. Authors, venue, pages, and DOI marked unavailable |
| 2 Copy used | Yes | Local SYNTHETIC file listed above. Access date 2026-10-31 |
| 3 Access level | Yes | Abstract only. Criteria the abstract does not address use NA where allowed |
| 4 Locator scheme | Yes | Title; Abstract. No page numbers estimated |
| 5 Full read | Yes | SYNTHETIC header, Title, Abstract |
| 6 Study status | Yes | Plan (Title; Abstract). Not treated as validated |
| 7 Rubric version | Yes | 1.0.0 |
| 8 Evidence search | Yes | See locations below. Absences say "searched Abstract: none" |
| 9 Quotes | Yes | Verbatim from the file. Each is 25 words or fewer |
| 10 NA decisions | Yes | C05, C06, C07, C08. Each guiding question contains `NA allowed if`. Notes restate the condition |
| 11 Circularity | Yes | Flagged above |
| 12 Integrity | Yes | No PDF saved. No second reviewer. Plan not described as validated |

## Scores

| criterion_id | score | evidence location | quote (25 words or fewer) | note |
| --- | --- | --- | --- | --- |
| C01 | 2 | Title; Abstract | "This research PLAN will develop quality-assurance guidelines for the model-building phase." | Status is labelled a plan. "No results are reported." Claims stay in future tense |
| C02 | 0 | Abstract | "insufficient reporting standards for model performance needed for model comparison" | The gap is named. No metric, unit, or planned report format is specified |
| C03 | 0 | Abstract | "unclear quality-task processes at each phase" | Model-building is named as the intended phase. Tasks are a planned goal, not defined |
| C04 | 1 | Abstract | "a literature study, expert validation, and a pilot project with two development teams" | Methods and a two-team pilot are named. Procedure and selection are missing |
| C05 | NA | Abstract | searched Abstract: none | NA allowed if the paper does not evaluate a method or process intended for adoption. This file is a plan with no results |
| C06 | NA | Abstract | searched Abstract: none | NA allowed if the paper does not discuss desk-checking or a review process |
| C07 | NA | Abstract | searched Abstract: none | NA allowed if the paper claims no results and names no variants or configurations |
| C08 | NA | Abstract | searched Abstract: none | NA allowed if the paper reports no executed method. Gaps listed here are research gaps, not limits of an executed method |

## Total and open items

- Total from `scripts/score_papers.py`: see `scores/summary.csv` (expected 3/8, scored=4, NA=4).
- Items a human must verify:
  - Every quote against `SYNTHETIC_paper_plan.txt`.
  - Whether C03 should stay 0 (goal only) or move to 1 because "model-building phase" names a phase.
  - A second reviewer's independent scores, needed for kappa.
