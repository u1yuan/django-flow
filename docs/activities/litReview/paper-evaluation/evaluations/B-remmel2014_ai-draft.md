# Evaluation: B-remmel2014

**Pilot draft by `ai-draft`.** A human must check every score and quote before these scores are used.

## Paper

| Field | Value |
| --- | --- |
| paper_id | B-remmel2014 |
| DOI | 10.1109/MCSE.2014.57 |
| Citation | Remmel, H., Paech, B., Engwer, C., & Bastian, P. (2014). A Case Study on a Quality Assurance Process for a Scientific Framework. *Computing in Science & Engineering, 16*(3), 58–66 |
| Metadata source used to verify citation | Crossref, DBLP, and the reprint's title page (see `source-trace.md`) |
| Reviewer | ai-draft |
| rubric_version | 1.0.0 |
| Evaluation date | 2026-10-31 |
| Copy used and URL | Author-posted IEEE reprint, https://se-paech.ifi.uni-heidelberg.de/fileadmin/pdf/2014_Remmel__Paech__Engwer__Bastian_A_Case.pdf |
| Access date | 2026-10-31 |
| Access level | Full text (author reprint). Page 58 body after the standfirst was read in this session |
| Locator scheme | Printed journal pages (58–66) plus section headings. Not checked against IEEE Xplore |
| Study status | Completed case study (pp. 60–66) |
| Is this paper a source of the rubric? | **Yes** (C05, C06, C07, C08–C15). These scores test rubric consistency. They are not independent evidence about the rubric |

## Desk-check

| # | Done | Note |
| --- | --- | --- |
| 1 Identity | Yes | The reprint's title page matches Crossref on title, four authors, 16(3), and pp. 58–66 |
| 2 Copy used | Yes | Author reprint with journal pagination. The server's TLS certificate had expired, so it was fetched with verification off (SHA-256 in `source-trace.md`) |
| 3 Access level | Yes | Full text of the reprint, including the p. 58 body |
| 4 Locator scheme | Yes | Printed pages |
| 5 Full read | Yes | Standfirst; Case Study Background (Planning, Review); Related Work sidebar; Case Study Design; Research Questions; Research Methods; Results; Proposed Desk-Checking Checklist sidebar; Support for Stated Goals; Threats to Validity; future work; References |
| 6 Study status | Yes | Completed (p. 61 "Results") |
| 7 Rubric version | Yes | 1.0.0 |
| 8 Evidence search | Yes | See locations below |
| 9 Quotes | Yes | Ligatures (fi, fl, ff, Th) were restored by hand after text extraction. Check them against the PDF |
| 10 NA decisions | Yes | None used. C03 is a candidate for NA; see note |
| 11 Circularity | Yes | Flagged above |
| 12 Integrity | Yes | Nothing saved |

## Scores

| criterion_id | score | evidence location | quote (25 words or fewer) | note |
| --- | --- | --- | --- | --- |
| C01 | 2 | p. 61 Results; p. 66 final para | "In our current and future work, we plan to adjust the design of the quality assurance process" | Future work is labelled |
| C02 | 1 | p. 61; pp. 63–64 | "For the closed questionnaire questions, we used a Likert scale and aggregated the answers with a median." | Medians are reported only as verbal labels |
| C03 | 0 | p. 65 Goal 2 | "The case study convinced the developers that desk-checking helps to develop higher quality source code." | No comparator. NA is arguable because this is a perception claim |
| C04 | 2 | pp. 59–60 | "developers should review all artifacts they created or changed: source code, unit tests, variability models, and system test applications." | Two in-scope phases are fully specified |
| C05 | 1 | p. 61; p. 65 Goal 2 | "The developers didn't try out desk-checking directly because it wasn't possible to simulate a realistic application of desk-checking." | Yet p. 65 concludes desk-checking is feasible |
| C06 | 1 | p. 65; p. 61 | "The moderator didn't mention any advantages or disadvantages of the methods." | Group influence is not addressed |
| C07 | 2 | p. 62 Table 1 | "F = feasibility, E = effort, A = acceptance" | RQ, code, hypothesis, and data source table |
| C08 | 2 | p. 60; p. 62 | "Goal 2: Assess the feasibility of desk-checking." / "Goal 4: Assess the acceptance of desk-checking." | Effort is coded separately (E_RQ) |
| C09 | 2 | pp. 60–61; p. 64 | "The acceptance part of our case study is based on the technology acceptance model (TAM)." | Results are reported per construct |
| C10 | 2 | p. 60 | "The case study was executed with a group of six Dune developers." | Experience and discipline are given |
| C11 | 2 | p. 61 | "For the data aggregation, we counted how many times similar answers were given." | Median with tie rule for Likert items |
| C12 | 2 | p. 65; p. 66 | "To achieve a methodological triangulation, we combined different types of data collection methods: observation, questionnaire, and discussion." | Also member checking and peer review |
| C13 | 1 | pp. 65–66; p. 61 | "Some problems with this specific variability modeling language might have negatively influenced the results" | The desk-checking limit is not carried into the conclusion |
| C14 | 2 | p. 61; p. 64 | "Task 1 was to model different possibilities of how a grid can be defined." / "the items in the checklist are rather suitable for the development in the Dune base classes" | Coverage and one exclusion are named |
| C15 | 2 | p. 65; p. 66 | "Several researchers checked the questions in the questionnaire for understandability." / "A second researcher peer reviewed each step." | |

## Total and open items

- Total from `scripts/score_papers.py`: see `scores/summary.csv` (expected 24/30).
- Items a human must verify:
  - Page numbers and quotes, against the IEEE Xplore version.
  - The p. 58 body was re-read in this session; confirm against IEEE Xplore.
  - Whether C03 should be NA.
  - Whether the overlap between C05 and C13 (both penalize the desk-checking feasibility conclusion) counts the same issue twice.
  - A second reviewer's independent scores, needed for kappa.
