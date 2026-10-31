# Evaluation: A-effendy2025

**Pilot draft by `ai-draft`.** A human must check every score and quote before these scores are used.

## Paper

| Field | Value |
| --- | --- |
| paper_id | A-effendy2025 |
| DOI | 10.1145/3725899.3725909 |
| Citation | Effendy, V., Suyanto, S., Sabariah, M. K., & Utomo, R. G. (2025). A Quality Assurance Framework for Model Building in Machine Learning Workflow – A Research Plan. *ICSIM '25*, pp. 63–67. ACM |
| Metadata source used to verify citation | Crossref API and the ACM landing page (see `source-trace.md`) |
| Reviewer | ai-draft |
| rubric_version | 1.0.0 |
| Evaluation date | 2026-10-31 |
| Copy used and URL | Publisher HTML, https://dl.acm.org/doi/full/10.1145/3725899.3725909 |
| Access date | 2026-10-31 |
| Access level | Full text (HTML) |
| Locator scheme | Section and paragraph. Page numbers within 63–67 are [unverified] |
| Study status | **Research plan.** Stated in the title and by the future tense in §4.2. No results are reported, and the framework is not validated |
| Is this paper a source of the rubric? | **Yes** (C01–C07, C11, C14). These scores test rubric consistency. They are not independent evidence about the rubric |

## Desk-check

| # | Done | Note |
| --- | --- | --- |
| 1 Identity | Yes | Crossref matches on title, four authors, and pp. 63–67. The dates disagree: Crossref print date 2025-01-10, ACM page "Published: 11 July 2025" |
| 2 Copy used | Yes | Publisher HTML with no visible pagination |
| 3 Access level | Yes | Full text |
| 4 Locator scheme | Yes | Section numbers. No page numbers were estimated |
| 5 Full read | Yes | Abstract, §1 Introduction, §2 Related Work, §3 Research Questions and Challenges, §4.1 Research Variable, §4.2 Research Methodology, §5 Implications, Acknowledgments, References |
| 6 Study status | Yes | Plan (title; §4.2 para 1) |
| 7 Rubric version | Yes | 1.0.0 |
| 8 Evidence search | Yes | See locations below. Absence findings name the sections searched |
| 9 Quotes | Yes | Copied from the HTML. All are 25 words or fewer |
| 10 NA decisions | Yes | None used. C03, C04, C08, C09, and C15 are applicable because A plans a comparison, a QA process, an adoption evaluation, a user survey, and study instruments |
| 11 Circularity | Yes | Flagged above |
| 12 Integrity | Yes | Nothing saved. Scores treat A as a plan |

## Scores

| criterion_id | score | evidence location | quote (25 words or fewer) | note |
| --- | --- | --- | --- | --- |
| C01 | 1 | Title; §4.2 para 1; §1 para 4 | "This research will be conducted in three stages to address the research questions." / "Based on initial interviews with developers at five different companies in Indonesia" | Plan status is explicit. The §1 interview finding is reported with no method |
| C02 | 1 | §4.1; §4.2 para 3 | "(3) whether the resulting ML models exhibit higher quality" | Outcomes are named but not operationalized |
| C03 | 1 | §4.2 para 3 | "In the first experiment, the teams will use the typical QA framework." | The baseline is not specified |
| C04 | 0 | §3 RQ2; §5 para 2 | "This QA process will then be formulated in greater detail, such as guidelines or checklists." | The tasks are the planned output, not yet defined |
| C05 | 1 | Abstract; §4.2 paras 1–3 | "The formulated QA model is then presented to experts for validation and feedback." | No expert count, selection, or criteria |
| C06 | 1 | §4.2 para 3 | "The involvement of at least two teams aims to avoid bias." / "There will be a sufficient time gap between the experiments to reduce bias." | Fixed order (typical, then proposed) and an unspecified gap |
| C07 | 2 | §4.1; §4.2 | "research variables are defined for each of the RQs" | Each RQ maps to variables and a stage |
| C08 | 1 | §4.1; §4.2 para 3 | "(2) whether the proposed QA framework can minimize repetition in model training" | Feasibility and effort are not separate questions |
| C09 | 0 | §4.2 para 3; §2 para 4 | "each individual will be asked to complete a survey regarding the use of the framework" | No constructs are named for A's own survey |
| C10 | 1 | §4.2 para 3 | "each comprising individuals with skills appropriate to real project conditions" | No counts or selection criteria |
| C11 | 1 | §4.2 para 1; §4.2 para 3 | "The survey results will be analyzed using ANOVA and correlation analysis" | Stage 3 analysis is unspecified |
| C12 | 1 | Abstract; §4.2 paras 1–3 | "The data collection results will then be combined with the results of the literature study, which will then be validated by experts." | Not framed as a validity safeguard |
| C13 | 0 | §§1–5 searched | (none: absence finding) | No limitations or threats section |
| C14 | 1 | Abstract; §4.2 para 3 | "Each team will conduct two model-building experiments based on predefined model requirements and provided datasets." | Domain is stated; datasets and settings are not |
| C15 | 0 | §§1–5 searched | (none: absence finding) | No pre-use review of instruments |

## Total and open items

- Total from `scripts/score_papers.py`: see `scores/summary.csv` (expected 12/30).
- Items a human must verify:
  - Page numbers for each section, using the ACM PDF.
  - Whether the C01 score of 1 is fair. The §1 interviews may be background, not a claim.
  - All quotes, against the ACM HTML.
  - A second reviewer's independent scores, needed for kappa.
