# Concept briefs at the biodiversity–light caliber

Compiled: 6 October 2026. Screening briefs, not a proposed title and not a fitted model. Evidence is in `evidence-ledger.md` and `caliber.md`. The STATYX manuscript's threshold and R² are that paper's claims.

No brief uses collapse, causation, or corruption language. An association that disappears after an effort or habitat control is a successful negative result.

## B1. Birds and nighttime light outside the already modeled city

**Title (12 words):** Associating Avian Richness Outside Metro Manila with Night Radiance Using Gradient Boosting

**Hook:** In a bright district the evening is loud with traffic and thin with birds. A 2026 student manuscript already modeled that pattern inside Metro Manila.

**Question:** Outside that Metro Manila box, is monthly nighttime radiance still associated with bird species richness after vegetation, land surface temperature, rainfall, and observer effort?

**Objectives:**

1. Define a grid and a month, exclude the bounding box used in the opened STATYX manuscript, and count cell-months after empty-cell rules.
2. Fit gradient boosting of richness on radiance plus those covariates, against a vegetation-only model and a same-month-last-year baseline.
3. Report whether the radiance association remains after an effort measure. If it does not, say so.

**Data:** eBird observations are the outcome lead. The STATYX PDF states a Philippine eBird extract of 1,355,677 records before its Metro Manila filter, then 646,800 Metro Manila cell-months. Those are that PDF's figures. This screen's GBIF API count for the Philippines was 3,901,246 occurrence records on 6 October 2026, all taxa, not cell-months. VIIRS monthly radiance is the exposure lead. The cell-month file for a second city or a national mask was not built.

**Metrics:** Held-out error against the two baselines, and a partial-dependence or accumulated-local-effects curve for radiance. A curve is not a tipping point unless a pre-registered change in slope is defined.

**Novelty:** The opened manuscript already does Metro Manila birds, LightGBM, VIIRS, vegetation, temperature, and rain. It says opportunistic sightings are biased. The open question is the association outside that city, with effort in the model. That question is not a result.

**Users:** City environment offices and bird groups. No adoption is confirmed.

**Venue type:** An ecology or environmental-data journal that publishes observational associations. No journal was checked for indexing in this pass.

**Ethics:** Public observations and satellite grids. Do not publish observer names. eBird and GBIF licenses have to be read before a download. Google Earth Engine terms apply if that is the extractor. The STATYX PDF used Earth Engine.

**Kill risk:** The second grid is still Metro Manila under another name, or effort is unavailable and the association is only "people count birds where people and lights already are."

## B2. The taxon the bird manuscript left open

**Title (11 words):** Associating Insect Occurrence with Philippine Night Radiance Using Gradient Boosting

**Hook:** The same manuscript says bats and insects are the next light-sensitive groups. Insects are the lived version: the swarm at a streetlight, and the dark farm with fewer of them.

**Question:** Are insect occurrence rates associated with nighttime radiance after habitat and sampling effort?

**Objectives:**

1. Choose one insect order from a public occurrence store and state the grid.
2. Count non-missing cell-months. A national occurrence total is not that count.
3. Fit the same association design as B1. Do not borrow the bird threshold.

**Data:** GBIF's Philippines occurrence count of 3,901,246 is all taxa. An insect-only count was not opened. Effort for insects is often worse than for birds.

**Metrics:** Same as B1.

**Novelty:** The STATYX generalization section names insects and bats as further work. Naming is not a demonstration that the association is unstudied. No insect-and-radiance paper was opened in this pass.

**Users:** DENR regional offices and farms near city edges. Unconfirmed.

**Venue type:** Same family as B1.

**Ethics:** No collector names. Do not infer a disease risk from insect or bat occurrence. The search hit on Mindanao bats and light mentioned disease in a secondary summary; that paper was not opened and is not a basis for a health claim.

**Kill risk:** Too few identified insect records per cell, or no usable effort variable.

## B3. Psychology, same shape, opened file too small

**Title (10 words):** Associating Adult Life Satisfaction with Local Night Radiance Using Regression

**Hook:** Sleep and mood in a bright, hot neighborhood. That is the psychological version of the light association.

**Question:** Among adults, is life satisfaction associated with the radiance or night temperature of the place, after income?

**Status:** Do not take this to faculty as a Philippine-only study. The IHSN page for World Values Survey Wave 7 Philippines states 1,200 cases. That is under 10,000. The documentation page's "more than 80,000 respondents" is the multi-country wave, and that file was not downloaded.

**What would reopen it:** A geocoded adult file whose respondent count, after the age rule and the join to a place, is at least 10,000, with a license that allows the join. Adolescent GSHS rows are not a substitute. The loneliness title already failed at 7,763 respondents ages 13–17.

**Ethics:** Adults only. No diagnosis. Association only.

## B4. Explicitly below the bar

FiReCS states 10,487 human-labeled Taglish reviews, CC-BY-4.0, and the card cites a 2024 transformer sentiment chapter. That can support a sentiment course project. It has no exposure, no place, and no outcome of the biodiversity–light kind. It is not briefed further.

## B5. Meteorology twin: heat measured in air, not another satellite of the same city

**Title (12 words):** Associating Philippine Night Air Temperature with Nearby Radiance Using Gradient Boosting

**Hook:** The bright blocks are also the ones that stay hot after sunset. Land surface temperature from the same family of satellites is not that feeling. Station air temperature is.

**Question:** Is nighttime air temperature, or a heat index if humidity is in the same record, associated with nearby nighttime radiance after vegetation and elevation?

**Objectives:**

1. Count station-nights with temperature, and humidity if the index is used.
2. Attach a radiance summary around each station without using future nights.
3. Compare gradient boosting with a vegetation-only model. Do not call radiance the cause of the heat.

**Data:** Not counted in this pass. The four-field heat screen did not produce a Philippine station-hour file. PAGASA's public rain-gauge page, as returned in search, is a latest snapshot. ClimGridPh-RR, opened as the 2024 abstract, is daily rainfall for 2001–2020, not night air temperature. One rainfall cell for that period is 7,305 days by calendar arithmetic and would fail the record rule alone.

**Novelty:** Baldres, Principe, and Soriano (2023), abstract only at `https://proceedings.spp-online.org/article/view/SPP-2023-1D-04`, report a correlation between VIIRS and PSA urbanization at regional and provincial scale. They do not report a station-night air-temperature model. Full text was not opened.

**Users:** PAGASA and city heat planners. Unconfirmed. This is not the conditional heat-alert title, which is a forecast verification problem.

**Ethics:** No household data.

**Kill risk:** The station-night file is below 10,000 after quality flags, or humidity is missing and a heat index cannot be formed. Surface temperature must not be substituted and then described as pedestrian heat.

## B6. Trade rebuilt as an association

**Title (11 words):** Associating Provincial Rice Prices with Gridded Rainfall Using Panel Regression

**Hook:** The sack of rice costs more after a bad rain year. The 2023 onion spike is a story. It is not the opened price file.

**Question:** Are provincial retail rice prices associated with prior gridded rainfall after a month-of-year control?

**Objectives:**

1. Count province-months with a price and a rainfall summary.
2. Fit a panel model against last month's price.
3. Keep the 2023 onion year out unless a price file that contains it is opened.

**Data:** PSA's old retail series, opened as the database notes, was discontinued effective February 2021. Latest month on the fruit-vegetable metadata page was January 2021. A province-month rice extract was not counted. ClimGridPh-RR covers 2001–2020 daily grids. The overlap is real on the calendar and uncounted in rows.

**Novelty:** Not checked against a paper. No arXiv result is cited. The OpenAlex and arXiv command-line searches for this track did not return usable JSON.

**Users:** A provincial agriculture office. Unconfirmed.

**Ethics:** Public prices and public rainfall. No farm names.

**Kill risk:** Province-months under 10,000, or the only long price series stops before the years people remember.

## Rank for a faculty conversation

| Order | Brief | Take? |
| --- | --- | --- |
| 1 | B1 Birds outside Metro Manila | Yes, as a conditional association study. The Metro Manila bird model already exists. |
| 2 | B5 Night air temperature and radiance | Yes, only after a station-night count. Do not swap in land surface temperature and call it the walk. |
| 3 | B2 Insects | Only after an insect cell-month count. |
| 4 | B6 Rice and rainfall | Only after a province-month count that survives January 2021. |
| 5 | B3 Life satisfaction | No, on the opened 1,200 Philippine cases. |
| 6 | B4 Review sentiment | No. Below this caliber. |

## Claim map

| Claim | Source |
| --- | --- |
| STATYX used eBird/GBIF, VIIRS, MODIS, CHIRPS, LightGBM, a Metro Manila grid, and stated 1,355,677 then 646,800 | Opened competition PDF |
| GBIF indexed 3,901,246 Philippine occurrence records on 6 October 2026 | Direct API fetch |
| WVS Wave 7 Philippines has 1,200 cases | IHSN catalog text |
| FiReCS states 10,487 reviews | Hugging Face dataset card |
| ClimGridPh-RR is daily rainfall, 2001–2020, 52 stations in the abstract, 0.01° | Opened PDF abstract |
| One cell over that period is 7,305 days | Calendar arithmetic, not a file count |
| Baldres and colleagues correlate VIIRS with urbanization at province and region | Abstract returned in search; full text not opened |
| PSA old agricultural retail prices stop effective February 2021 | Opened OpenSTAT notes |
