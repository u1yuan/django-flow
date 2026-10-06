# Brief — meteorology gap search

Research question or topic:
Which 2022–2026 gaps in tropical heat alerts, tropical-cyclone rapid intensification, or air-quality sensor anomalies are specific enough for a Data Science thesis, and which public dataset could later test each gap?

Requested output:
`docs/activities/litReview/four-field-gaps/2026-10-06/gap-candidates-meteorology.md` with 3 to 5 gap cards and a search log, following `briefs/shared-constraints.md`.

Input locations:
- `docs/activities/litReview/four-field-gaps/2026-10-06/briefs/shared-constraints.md`
- Seeds to test, not findings: (1) calibrated heat-index exceedance alerts that transfer across tropical cities, with NOAA GSOD or ISD bulk files as leads; (2) predicting rapid intensification of tropical cyclones before landfall, with IBTrACS and SHIPS developmental data as leads; (3) detecting anomalies in air-quality sensors, with OpenAQ as a lead.
- Historical conditional direction, not a finding: urban heat alerts across Philippine cities. It may return only if the new search opens nearest studies and names a dataset lead under these rules.
- Skills and CLIs: OpenAlex `docs/activities/litReview/.agents/skills/literature-search-openalex/scripts/openalex_cli.py`; arXiv `docs/activities/litReview/.agents/skills/literature-search-arxiv/scripts/search_arxiv.py`.

Constraints:
- An alert gap states a target metric to test later, such as false alerts against climatology. It does not report a model result.
- A cyclone gap does not claim the model would have saved lives or prevented damage.
- NOAA GSOD outside the United States is noncommercial; flag that on the lead, do not drop the lead.
- Copernicus accounts and Earth Engine are excluded.
- Follow every rule in `shared-constraints.md`.

Acceptance criteria:
- 3 to 5 cards meeting the shared card checklist.
- Search log shows at least two indexes.
- Each heat, cyclone, or air-quality card names the observation unit (station-hour, storm-time, or sensor-hour) on its dataset lead.

Data handling restrictions:
Do not download bulk GSOD, IBTrACS, or OpenAQ files in this task. Record official URLs, license notes, and documented sizes only. Do not commit.
