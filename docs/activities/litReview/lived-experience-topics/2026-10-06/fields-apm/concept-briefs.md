# Concept briefs at the biodiversity–light caliber

Compiled: 6 October 2026. Screening briefs for a faculty conversation. None is an approved title, a fitted model, or a completed count. Evidence is in `evidence-ledger.md` and `../evidence-ledger.md`. The cut is in `caliber.md`.

STATYX, Curiosity Cup 2026, already associated Metro Manila bird richness with nighttime radiance on a 500 m monthly grid and reported a threshold near 51.96 nW/cm²/sr. That number is their manuscript's claim. These briefs do not repeat the Metro Manila bird study and do not treat the threshold as established.

Association language is required in every brief. A partial-dependence curve is not a cause.

## B1. Birds and light outside Metro Manila

**Title (12 words):** Associating Avian Richness Outside Metro Manila with Night Radiance Using Gradient Boosting

**Hook.** People notice fewer birds in the brightest districts. A 2026 student manuscript already modeled that pattern inside Metro Manila. The open question is whether the same association appears in other Philippine cities once observer effort is held constant.

**Question.** After grid cell, month, vegetation, rainfall, and an effort measure, is nighttime radiance still associated with bird species richness outside Metro Manila?

**Objectives.**

1. Build city-month grids outside Metro Manila from public bird logs and VIIRS radiance.
2. Compare gradient boosting with a linear model that uses the same covariates, including effort.
3. Report the radiance association with a partial-dependence curve and a held-out city, and state what the curve does not prove.

**Data.** Exposure: VIIRS nighttime radiance. Outcome: species richness from eBird logs distributed through GBIF. STATYX states a Philippine eBird extract of 1,355,677 records before a Metro Manila box, and 646,800 Metro Manila cell-months after gridding. Those are the manuscript's figures. This screen did not download eBird or VIIRS. GBIF's count API returned 3,901,246 Philippine occurrence records on 6 October 2026, all taxa, not cell-months. The outside-Manila cell-month count was not opened.

**Baselines and metrics.** Linear regression with the same covariates. Persistence of last year's richness in that cell-month. Metrics: held-out error, and the change in the radiance association when effort is added. A high R² alone is not the result.

**Novelty.** Not claimed as a gap. The opened manuscript already did Metro Manila birds, LightGBM, and VIIRS, and it says opportunistic sightings are biased toward where people walk. The only reason to proceed is the effort control plus a city that manuscript did not fit. A paper that skips the effort control is a weaker copy.

**Users.** City environment offices and bird groups. No office has been asked.

**Venue type.** An ecology or environmental-data journal that publishes observational associations. No journal was checked for indexing in this pass.

**Ethics.** Public species observations. Drop observer names. Do not rank a barangay as hostile to wildlife.

**Kill risk.** If effort fully accounts for the radiance association, the light result goes away. If the outside-Manila cell-months fall under 10,000 after empty cells are dropped, the record gate fails.

## B2. A second taxon and light

**Title (10 words):** Associating Insect Occurrence with Philippine Night Radiance Using Gradient Boosting

**Hook.** The same manuscript says bats and insects are the next light-sensitive groups. Fireflies and night insects are the lived version of that sentence.

**Question.** In grid cell-months with at least one recorded insect survey, is nighttime radiance associated with occurrence after habitat and effort covariates?

**Objectives.**

1. Count a named insect group from GBIF, not all animals.
2. Fit the same association design as B1.
3. Stop if the surveyed cell-months are under 10,000.

**Data.** No insect-only count was opened. The 3,901,246 figure is all Philippine occurrences. It cannot be used as the insect sample.

**Baselines.** A habitat-only model, without radiance.

**Novelty.** The manuscript names this as future work. That is a lead, not proof the study is unoccupied.

**Users.** Local conservation groups. Unconfirmed.

**Ethics.** Species records only.

**Kill risk.** Insect records may be too sparse, or too tied to collector locations, to support a grid.

## B3. Psychology, same shape, opened file fails

**Title (10 words):** Associating Adult Life Satisfaction with Local Night Radiance Using Regression

**Hook.** Bright, hot streets and how tired people say they are. This is the psychological version of B1: a place exposure and a person outcome.

**Question.** Among adults, is life satisfaction associated with the nighttime radiance or night heat of the place, after income and age?

**Data.** IHSN catalog text for World Values Survey Wave 7 Philippines, 2019: 1,200 cases and 434 variables. Ages 18 and older on the WVS fieldwork page. The documentation page says Wave 7 has more than 80,000 respondents in 64 surveys. The global file was not downloaded. Philippine-only analysis fails the 10,000-record rule on the opened 1,200.

**Decision.** Do not propose the Philippine-only title. A multi-country version could be discussed only after the global file is counted and a radiance join is possible. Many respondents will not have coordinates fine enough for a neighborhood exposure. That join was not tried.

**Ethics.** Adults. No diagnosis. The stopped adolescent loneliness title stays stopped.

**Kill risk.** Already met for a Philippine-only respondent file.

## B4. Explicitly below the bar

**Not a proposed title.** Classifying Taglish review sentiment.

FiReCS states 10,487 human-labeled reviews, CC-BY-4.0, and cites Cosme and De Leon (2024), DOI `10.1007/978-981-99-8349-0_11`. The chapter PDF was not opened. The corpus can support a sentiment classifier. It has no exposure, no health outcome, and no place-time grid. It does not match the biodiversity–light design. Shopee's seller page, as returned in search, forbids new automated collection. The brief does not propose scraping.

## B5. Night heat and night light

**Title (10 words):** Associating Nighttime Land Surface Temperature with Radiance Using Gradient Boosting

**Hook.** The districts that stay bright also stay hot after sunset, which is the walk home.

**Question.** Across Philippine grid cell-months, is nighttime land surface temperature associated with VIIRS radiance after vegetation and a seasonal baseline?

**Objectives.**

1. Pair MODIS night land-surface temperature with VIIRS radiance on one grid.
2. Compare gradient boosting with a seasonal climatology and a linear model.
3. Interpret radiance as a co-occurring urban marker, not as the sole source of the heat.

**Data.** Both products are named in the STATYX methods as Earth Engine datasets. This screen did not download them and did not count cell-months. ClimGridPh-RR, opened as the PAGASA 2024 abstract, is daily rainfall for 2001–2020 at 0.01°, from 52 synoptic stations merged with IMERG. It is not a temperature product. One rainfall cell for that period is 7,305 days by calendar arithmetic (20 years and 5 leap days) and would fail the record gate alone.

**Prior work, abstract only.** The proceedings abstract of Baldres, Principe, and Soriano (2023), SPP-2023-1D-04, says VIIRS composites for 2015 and 2020 were correlated with PSA urbanization at regional and provincial levels. The paper PDF was not opened. B5 is not that provincial correlation.

**Baselines.** Month-of-year climatology. A model with vegetation and no radiance.

**Novelty.** Not claimed. Night lights and surface temperature are a crowded pair.

**Users.** City heat planning. Unconfirmed. This is not the conditional heat-alert title in the 6 October opportunity map, which is a forecast verification problem and was not counted.

**Ethics.** No personal data.

**Kill risk.** Radiance and temperature may move together only because both track built-up land. If a built-up covariate removes the association, the light sentence should be dropped. Cell-months under 10,000 after cloud filters would also stop it.

## B6. Rain and the rice price

**Title (10 words):** Associating Provincial Rice Prices with Gridded Rainfall Using Panel Regression

**Hook.** A dry spell shows up later as the price of rice.

**Question.** Are provincial retail rice prices associated with prior rainfall in that province, after a seasonal baseline and a national price factor?

**Data.** ClimGridPh-RR covers 2001–2020 daily rainfall. Province-months were not counted. PSA OpenSTAT's old agricultural retail series was discontinued effective February 2021, and the opened metadata example lists January 2021 as the latest month. A province-by-month rice file was not opened. The 2023 onion spike is outside that old series. National monthly prices cannot reach 10,000 records.

**Decision.** Discuss only if a province-month price panel is counted and overlaps 2001–2020. Do not propose it on a national series.

**Ethics.** Public prices.

**Kill risk.** The price panel is missing. Rainfall will also be collinear with season.

## Claim map

| Claim in these briefs | Source |
| --- | --- |
| STATYX used eBird/GBIF, VIIRS, MODIS, CHIRPS, LightGBM, a 500 m monthly grid, and stated 1,355,677 then 646,800 | Opened competition PDF |
| 51.96 nW/cm²/sr and the R² figures are theirs | Same PDF, not remeasured |
| GBIF country count 3,901,246 | API fetch, 6 October 2026, all occurrences |
| WVS Philippines Wave 7 has 1,200 cases | IHSN catalog text |
| FiReCS states 10,487 reviews | Hugging Face dataset card |
| ClimGridPh-RR is daily, 2001–2020, 0.01°, 52 stations | Opened PAGASA 2024 abstract |
| One cell, 2001–2020, is 7,305 days | Calendar arithmetic, not a file count |
| Baldres and colleagues correlated VIIRS with provincial urbanization | Proceedings abstract only |

## Unresolved

1. Outside-Manila bird cell-months after an effort filter.
2. An insect or bat subset count.
3. A radiance join that does not depend on the 1,200-person Philippine WVS file.
4. Philippine grid cell-months of paired night temperature and radiance after clouds.
5. A province-month rice price file overlapping 2001–2020.
6. Whether any journal will take an observational association of this size. Not checked.
