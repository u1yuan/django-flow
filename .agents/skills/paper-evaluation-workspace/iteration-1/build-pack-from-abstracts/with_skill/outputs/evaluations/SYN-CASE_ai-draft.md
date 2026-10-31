# Evaluation: SYN-CASE

**Pilot draft by `ai-draft`.** A human must check every score and quote before these scores are used.

## Paper

| Field | Value |
| --- | --- |
| paper_id | SYN-CASE |
| DOI | unavailable |
| Citation | Title only: A Case Study on Desk-Checking and Variability Coverage. Authors, year, venue, and pages unavailable |
| Metadata source used to verify citation | Local SYNTHETIC file header. No Crossref or publisher record was retrieved |
| Reviewer | ai-draft |
| rubric_version | 1.0.0 |
| Evaluation date | 2026-10-31 |
| Copy used and path | Local SYNTHETIC file `.agents/skills/paper-evaluation/evals/files/SYNTHETIC_paper_casestudy.txt` |
| Access date | 2026-10-31 |
| Access level | Abstract only |
| Locator scheme | Title; Abstract. No pages |
| Study status | **Completed case study.** Title and opening sentence. Past-tense findings on feasibility, acceptance, and a limit |
| Is this paper a source of the rubric? | **Yes** (C01, C04–C08). These scores test rubric consistency. They are not independent evidence about the rubric |

## Desk-check (`desk-check-checklist.md`)

| # | Done | Note |
| --- | --- | --- |
| 1 Identity | Yes | Title matches the file. Authors, venue, pages, and DOI marked unavailable |
| 2 Copy used | Yes | Local SYNTHETIC file listed above. Access date 2026-10-31 |
| 3 Access level | Yes | Abstract only |
| 4 Locator scheme | Yes | Title; Abstract. No page numbers estimated |
| 5 Full read | Yes | SYNTHETIC header, Title, Abstract |
| 6 Study status | Yes | Completed case study (Title; Abstract) |
| 7 Rubric version | Yes | 1.0.0 |
| 8 Evidence search | Yes | See locations below. Absences say "searched Abstract: none" |
| 9 Quotes | Yes | Verbatim from the file. Each is 25 words or fewer |
| 10 NA decisions | Yes | None used. C03 and C05–C08 apply because the abstract evaluates a QA process, names desk-checking, reports variants, and reports a limit |
| 11 Circularity | Yes | Flagged above |
| 12 Integrity | Yes | No PDF saved. No second reviewer. SYN-PLAN is not described as validated in this file |

## Scores

| criterion_id | score | evidence location | quote (25 words or fewer) | note |
| --- | --- | --- | --- | --- |
| C01 | 2 | Title; Abstract | "This case study evaluates feasibility and acceptance as separate questions" | Completed case study. Findings are in the past tense and match that status |
| C02 | 0 | Abstract | searched Abstract: none | No model-performance metric, unit, or comparison report is named |
| C03 | 1 | Abstract | "two parts of a QA process: variability-model creation and desk-checking" | Two process parts are named. Task, timing, role, and output are incomplete |
| C04 | 1 | Abstract | "Developers accepted both parts." | Case study and developer role are named. Count, selection, and procedure are missing |
| C05 | 2 | Abstract | "evaluates feasibility and acceptance as separate questions" | Separate evidence: "Variability modeling was feasible" and "Developers accepted both parts." |
| C06 | 2 | Abstract | "Desk-checking is a checklist-guided self-review before check-in, not a structured inspection." | Definition matches the score-2 minimum |
| C07 | 1 | Abstract | "a different modeling language was needed to represent all important variants" | A coverage limit is named. Covered variants are not enumerated |
| C08 | 1 | Abstract | "The study reports that limit." | Limit is reported and qualifies feasibility. "Developers accepted both parts" is not qualified by it |

## Total and open items

- Total from `scripts/score_papers.py`: see `scores/summary.csv` (expected 10/16, scored=8, NA=0).
- Items a human must verify:
  - Every quote against `SYNTHETIC_paper_casestudy.txt`.
  - Whether C08 should stay 1 (acceptance not qualified) or return to 2.
  - A second reviewer's independent scores, needed for kappa.
