# QA review: lived-experience and three-field ideation

Date: 6 October 2026. Reviewer role: research QA. Artifacts: `idea-pool.md`, `scorecard.md`, `evidence-ledger.md`, `concept-briefs.md`, and `fields-apm/` (`idea-pool.md`, `scorecard.md`, `caliber.md`, `evidence-ledger.md`, `concept-briefs.md`).

Brief: fun, publishable, marketable Data Science topics from lived experience, then the same workflow for astronomy, psychology, and meteorology, then the same caliber as an association between biodiversity and light. Gates: at least 10,000 records, ethical sourcing, titles of at most 16 words that name a technique. No invented counts. Association is not causation. Procurement flags are not findings of corruption.

## Checks

| Check | Result |
| --- | --- |
| Title length | B1 is 12 words. B2, B3, B5, and B6 are 10. All name a technique. See finding Q1. |
| STATYX split | 388,080 + 194,040 + 64,680 = 646,800, matching the total the PDF states. This does not audit the grid. |
| GBIF API | Ledger figure 3,901,246 matches the fetch body `3901246`. The brief calls these occurrences, not cell-months. |
| FiReCS splits | 2,410 + 2,549 + 2,381 = 7,340. 1,033 + 1,087 + 1,027 = 3,147. Sum 10,487, matching the card. |
| One ClimGridPh cell | 20 × 365 + 5 leap days = 7,305. Labeled as calendar arithmetic. Under 10,000 for one cell. |
| WVS Philippines | 1,200 cases. Philippine-only title is stopped. |
| GTFS | 79,415 non-blank lines stated, with the header assumption kept in the ledger. Not used as a proposed title. |
| Causation and blame | Briefs forbid cause claims, wildlife blame, and corruption findings. |
| Literature CLIs | OpenAlex batch was stopped with an empty `l01.json`. arXiv batch was stopped with no usable JSON. No paper is cited from either CLI. |

## Findings

| ID | Severity | Location | Evidence | Correction |
| --- | --- | --- | --- | --- |
| Q1 | Medium | `fields-apm/concept-briefs.md` titles B2, B5, B6 as first written | The parenthetical word counts were 11, 11, and 12. Recount: B2 is 10, the revised B5 wording is 10, B6 is 10. | Writer changed the labels and the B5 wording before this review closed. Follow-up must confirm the file on disk. |
| Q2 | Low | Baldres, Principe, and Soriano (2023) | Support is the proceedings abstract returned by web search, not a fetched PDF. | Brief already says the PDF was not opened. Do not add their statistics. |
| Q3 | Low | Unopened analysis units | Outside-Manila cell-months, insect subsets, temperature grids, and province-month rice prices were not counted. | Already written as kill risks. No change. |

## Status

Pass with limitations, pending the follow-up confirmation of Q1 on the saved file. No title is ready for faculty as a finalist. B1 is the closest discussion piece, and only with an effort control and a city the STATYX manuscript did not fit. B3 is stopped. B4 is below the caliber. B2, B5, and B6 stay conditional on counts.
