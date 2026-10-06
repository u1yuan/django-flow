# Brief — astronomy gap search

Research question or topic:
Which 2022–2026 gaps in night-sky brightness estimation or equatorial geomagnetic disturbance detection are specific enough for a Data Science thesis, and which public dataset could later test each gap?

Requested output:
`docs/activities/litReview/four-field-gaps/2026-10-06/gap-candidates-astronomy.md` with 3 to 5 gap cards and a search log, following `briefs/shared-constraints.md`.

Input locations:
- `docs/activities/litReview/four-field-gaps/2026-10-06/briefs/shared-constraints.md`
- Seeds to test, not findings: (1) estimating sky brightness where observations are sparse, trained on global citizen-science data, with global Globe at Night and EOG VIIRS as dataset leads; (2) detecting geomagnetic disturbances at equatorial stations, with relevance to GNSS positioning and the power grid, and INTERMAGNET and OMNIWeb as dataset leads.
- Historical screen only: Philippine Globe at Night had 323 rows and WDPA had 274 Philippine designations. Those counts retired Philippine-only site catalogs. This search may use global files. Do not treat the old counts as a pass or as a new measurement.
- Skills and CLIs named in the psychology brief's skill paths. OpenAlex and arXiv scripts live under `docs/activities/litReview/.agents/skills/`.

Constraints:
- A sky-brightness gap must not assign a health or legal label from imagery alone.
- A geomagnetic gap must not claim that a detected disturbance caused a grid fault or a positioning failure.
- Pixel expansion of a site catalog is not an independent-record strategy. State the observation unit on the dataset lead.
- Follow every rule in `shared-constraints.md`.

Acceptance criteria:
- 3 to 5 cards meeting the shared card checklist.
- At least one card tests a seed above, and other cards may come from the search if they meet the same checklist.
- Search log shows at least two indexes.
- Indexing that was not opened is marked "indexing not confirmed".

Data handling restrictions:
Do not download bulk imagery or magnetometer archives in this task. Record official URLs and documented sizes only. Earth Engine is excluded. Do not commit.
