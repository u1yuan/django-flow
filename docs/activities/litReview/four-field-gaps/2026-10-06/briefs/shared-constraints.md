# Shared constraints — gap search, 6 October 2026

These constraints bind every field brief. They are screening rules, not findings.

## Question

Which gaps in this field, visible in indexed literature from 2022 through 2026, are specific enough for an undergraduate Data Science thesis, and which manually downloadable dataset could later test each gap?

## What a gap card must contain

Return 3 to 5 cards. Each card has all of the following:

1. **Gap statement.** One paragraph. Say what the nearest studies do, what they leave open, and why that opening is a study rather than a restatement of their limitation.
2. **Nearest studies.** Three to five studies, 2022–2026 preferred. For each: authors, year, title, DOI, venue, what was opened (full text, HTML, or abstract only), and a short locator for any limitation or future-work sentence. Quote at most one sentence, and only from text that was actually opened. An abstract supports only what it states. A citation inside another paper is a lead until that paper is opened.
3. **Candidate venues.** At least two Scopus- or IEEE-indexed venues from 2022–2026 that published comparable-scale studies. Record how indexing was checked. If the index page was not opened, write "indexing not confirmed" and do not treat the venue as passing.
4. **Social implication.** Named affected population, one Sustainable Development Goal, the decision the result would inform, and a harm note covering privacy, stigma, and misuse.
5. **Draft title.** At most 16 words, form "[action] [outcome] for [context or user] Using [named technique]". The technique must be named. Count words and show the count.
6. **Subdomain.** One of: data mining, big data analytics, predictive analytics, feature engineering, recommendation systems, data visualization, anomaly detection, statistical modeling, data governance and ethics, edge and IoT data analytics.
7. **Dataset lead.** At least one Philippine, multi-country, or global dataset a person could download in a browser, including free registration. Record the official URL if opened, the documented unit, and whether Philippine rows are known. A lead is not a counted dataset. Earth Engine, Copernicus accounts, scraping, primary collection, and partner requests are out.
8. **Claim boundary.** Associations are not causes. Do not propose an individual diagnosis of a minor. Do not propose a legal or health label from imagery alone.

## Search

- Read and follow `.agents/skills/evidence-research/SKILL.md`, `.agents/skills/literature-review/SKILL.md`, and `.agents/skills/citation-management/SKILL.md`.
- Use both activity skills: `docs/activities/litReview/.agents/skills/literature-search-openalex/SKILL.md` and `docs/activities/litReview/.agents/skills/literature-search-arxiv/SKILL.md`. License notices already exist at the repository root `.licenses/`. Use the CLIs in those skills. Do not call the APIs with curl or urllib.
- Search at least two indexes. Start with review papers, then limitation and future-work sections of recent studies.
- Date window for the gap literature: 2022-01-01 through 2026-10-06. Older work may be named as background, not as a nearest study, unless no 2022–2026 study exists; if so, say that the window was empty for that seed.
- Do not claim a gap is novel. Call it a candidate gap.
- If a page is blocked (403, login wall, timeout), record the failure and do not bypass it.
- Do not fit a model. Do not contact an organization or search for a competition.
- Keep hydroponics and diesel out of this search.
- Do not commit, push, or edit files outside your field output.
- Do not save full-text PDFs into the repository.

## Output

Write only:

`docs/activities/litReview/four-field-gaps/2026-10-06/gap-candidates-<field>.md`

Include, in this order: search log table (database, date, query, filters, result count), inclusion and exclusion notes, then the cards, then unverified leads and blocked pages. Every DOI in a card must have been resolved through OpenAlex, Crossref, the publisher page, or the paper itself during this run. If resolution failed, move that study to unverified leads.
