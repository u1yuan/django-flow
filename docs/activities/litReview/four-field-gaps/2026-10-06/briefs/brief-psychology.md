# Brief — psychology gap search

Research question or topic:
Which 2022–2026 gaps in adolescent belonging, bullying, or wellbeing classification are specific enough for a Data Science thesis, without diagnosing an individual minor, and which public multi-country dataset could later test each gap?

Requested output:
`docs/activities/litReview/four-field-gaps/2026-10-06/gap-candidates-psychology.md` with 3 to 5 gap cards and a search log, following `briefs/shared-constraints.md`.

Input locations:
- `docs/activities/litReview/four-field-gaps/2026-10-06/briefs/shared-constraints.md`
- Seeds to test, not findings: (1) whether models of adolescent belonging or bullying risk transfer across countries, including the Philippines, with PISA 2022 or TIMSS 2019 as dataset leads; (2) subgroup fairness in wellbeing classifiers compared across income levels, with World Values Survey Wave 7 or pooled GSHS as dataset leads.
- Historical screen only, not evidence: `docs/activities/litReview/four-field-titles/2026-10-06/`. The earlier GSHS ages 13–17 file had 7,763 respondents. Do not reuse that count as a pass. A new gap may use a different unit or a multi-country file.
- Skills named in the shared constraints. OpenAlex CLI: `docs/activities/litReview/.agents/skills/literature-search-openalex/scripts/openalex_cli.py`. arXiv CLI: `docs/activities/litReview/.agents/skills/literature-search-arxiv/scripts/search_arxiv.py`.

Constraints:
- Population-level patterns only. No card may propose identifying, diagnosing, or labeling an individual child or adolescent.
- School-survey gaps must name the observation unit (student response, school, country-year) and must not treat a catalog total as an eligible count.
- Philippine relevance may be the beneficiary, a held-out country, or a case study. The dataset does not need to be Philippine-only.
- Follow every rule in `shared-constraints.md`.

Acceptance criteria:
- 3 to 5 cards, each with opened nearest studies, a gap statement, venue notes, social implication, a draft title of at most 16 words that names a technique, one Data Science subdomain, and at least one manual-download dataset lead.
- Search log shows at least two indexes.
- Unopened limitation sentences are not quoted.
- Blocked pages are listed as blocked.

Data handling restrictions:
No raw survey microdata are downloaded in this task. Do not save restricted student-level files. Record only public documentation URLs and documented sizes. Do not commit.
