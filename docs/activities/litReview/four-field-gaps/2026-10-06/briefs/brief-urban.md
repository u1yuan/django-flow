# Brief — urban gap search

Research question or topic:
Which 2022–2026 gaps in digital-divide mapping, health-facility access, or road-crash hotspot detection are specific enough for a Data Science thesis, and which public dataset could later test each gap?

Requested output:
`docs/activities/litReview/four-field-gaps/2026-10-06/gap-candidates-urban.md` with 3 to 5 gap cards and a search log, following `briefs/shared-constraints.md`.

Input locations:
- `docs/activities/litReview/four-field-gaps/2026-10-06/briefs/shared-constraints.md`
- Seeds to test, not findings: (1) digital-divide mapping from speed-test and building data, with Ookla open tiles, Google Open Buildings, and Meta Relative Wealth Index as leads; (2) gaps in access to health facilities, with OpenStreetMap and HDX layers as leads; (3) hotspots in road-crash records, using global open crash data, with a Philippine case only if an MMDA file is publicly downloadable without a partner request.
- Historical conditional direction, not a finding: forecasting Philippine LGU nighttime-radiance growth. It may return only if nearest studies are opened and a manually downloadable radiance product is named. Earth Engine is excluded.
- Skills and CLIs: OpenAlex `docs/activities/litReview/.agents/skills/literature-search-openalex/scripts/openalex_cli.py`; arXiv `docs/activities/litReview/.agents/skills/literature-search-arxiv/scripts/search_arxiv.py`.

Constraints:
- Ookla open data is CC BY-NC-SA; flag noncommercial use on the lead.
- Do not propose a legal finding of negligence, a clinical shortage diagnosis, or a health label from imagery alone.
- A facility-access gap uses published facility locations. It does not infer who is sick.
- Follow every rule in `shared-constraints.md`.

Acceptance criteria:
- 3 to 5 cards meeting the shared card checklist.
- Search log shows at least two indexes.
- Each card names the observation unit on its dataset lead (tile, building, facility, crash record, or LGU-month).

Data handling restrictions:
Do not download Ookla, Google, Meta, OSM, HDX, or crash files in this task. Record official URLs and license notes only. Do not commit. Do not contact MMDA or any other organization.
