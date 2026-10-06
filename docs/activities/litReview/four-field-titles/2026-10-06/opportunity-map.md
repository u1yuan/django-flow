# Opportunity map: four-field Data Science title screen

Compiled: 6 October 2026. This is a screening memo for the next faculty consultation. It is not an approved title, a completed literature review, a finished dataset audit, or evidence that any organization will adopt the work.

Hydroponics, diesel-genset anomalies, and Native Trees were kept out of this screen. Native Trees remains the group’s publishability benchmark and was not re-scored here.

## Decision

No active title passed the hard gates in the CS thesis guideline and in `THESIS_TITLE_RESEARCH_PLAN.md`. The guideline requires a Data Science study to use at least 10,000 records, sourced in line with the ethics clause, and a title of at most 16 words that names the algorithm, model, or technique (`docs/CS-Guideline-as-of-Nov-17-as-430pm-without-signature (1).md`, sections 2.1, 2.2, 4.1, and 4.4). A catalog total was not treated as that eligible count.

Four directions fail because an opened file already puts the stated unit under 10,000. Six directions were not counted, because the codebook, extract, or boundary file was blocked or was never built. The consultation can still discuss two conditional directions. They are the only ones whose proposed record unit was not already shown to fall short. They are not finalists.

| Conditional direction | Why it is still open | What must be counted before it can proceed |
| --- | --- | --- |
| Evaluating Urban Heat Alert Reliability Across Philippine Cities Using Conformalized XGBoost (11 words) | PAGASA iHeatMap and Quezon City iRISE-UP are existing services. The NOAA Integrated Surface Database history file lists 116 Philippine stations. Station-hours with paired temperature and humidity or dew point were not computed. | Eligible station-hours after quality flags, then a split that holds out years and stations. Issue-time archives of iHeatMap or iRISE-UP were not opened, so a direct comparison with those services is not available. |
| Forecasting Philippine LGU Nighttime-Radiance Growth Using XGBoost (7 words) | Earth Observation Group monthly VIIRS composites report average radiance in nW/cm²/sr, and the product page points to a Creative Commons Attribution 4.0 license. The outcome in this wording is radiance growth. The saved product page does not use the word “upward.” | Eligible LGU-months after cloud-free coverage, boundary joins, and missingness. The figure 19,704 is 1,642 local governments times 12 months. The PSA geographic-code page returned HTTP 403, and no radiance extract was built, so that figure stays potential arithmetic from the plan. |

## Titles that fail an opened count

| Working title | Gate | Opened count and unit | Source |
| --- | --- | --- | --- |
| Filipino Adolescent Loneliness Patterns and Protective Factors Using Latent Class Analysis (11 words) | Stop on the record gate | 7,763 national-file respondents in the age categories 13 through 17. The catalog case count is 10,175, including ages outside that band and 26 missing ages. Listwise complete cases on the loneliness and protective-factor items were not computed and cannot exceed 7,763. | `data-feasibility.md` section 1, from the WHO DDI for catalog 944. The psychology screen’s earlier “revise” gate is superseded for the record rule by this upper bound. |
| Estimating Philippine Night-Sky Brightness Using XGBoost and Satellite–Ground Observations (9 words) | Stop | 323 Philippine Globe at Night rows for 2006–2024, in 92 coordinate pairs. The 2025 file returned HTTP 400 and was not added. | `globeatnight-philippines-summary.json` |
| Prioritizing Philippine Dark-Sky Conservation Sites Using NSGA-II and Nighttime-Light Trends (10 words) | Stop | Protected Area Information System: 248 eNIPAS areas. WDPA Philippines profile: 274 designations, 249 national. Both are site catalogs. Pixel expansion would not create independent sites. | Astronomy evidence file; `data-feasibility.md` section 5 |
| Evaluating Philippine Urban Heat Alert Reliability Across ENSO Regimes Using Conformalized XGBoost (12 words) | Stop as a regime study | 920 overlapping RONI seasons and 6 warm episodes at or above +2.0°C. The 2023–24 peak on the opened table is 1.4°C. Overlapping seasons are not independent events. Philippine station-hours inside those episodes were not counted. | `_opened/roni-very-strong-summary.json` |

WMO’s ENSO page says it does not use the term “Super El Niño.” NOAA’s June 2026 strengths archive uses an `Index ≥ 2.0°C` column. Those sentences settle the wording. They do not supply a Philippine forecast sample.

## Titles that were not counted

| Working title | Gate | Why the count is missing |
| --- | --- | --- |
| Creative Thinking and Digital Leisure Across Southeast Asian PISA Systems Using Multilevel IRT (13 words) | Stop | OECD database, Volume III, and codebook hosts returned HTTP 403. The opened Cai, Bi, and Feng (2026) full text uses five East Asian systems and does not include the Philippines. Castulo and colleagues’ abstract gives 3,662 female and 3,531 male Philippine creative-thinking respondents. That abstract split sums to 7,193 and does not mention social media or gaming. |
| Estimating Population-Weighted Urban Heat Exposure Across Philippine Cities Using Spatial Random Forests (12 words) | Stop | Estoque and colleagues (2020), DOI `10.1038/s41467-020-15218-8`, are recorded in the meteorology field file as a Philippine city heat-health map that used land surface temperature because measured air temperature was lacking. The figure of 139 cities is in that field file and was not rechecked from a saved HTML copy in this folder. No population or temperature pixels were sampled in this screen. |
| Mapping Philippine Urban Green Access and Surface Heat Using Random Forest and Network Analysis (14 words) | Revise, and do not take to faculty as a finalist | Sentinel-2 Level-2A has no surface-temperature band. Landsat 9 Level-2 `ST_B10` is surface temperature. Park entrances, routes, population denominators, and cloud-filtered grid-time cells were not counted. Surface temperature is not a pedestrian-comfort measurement. |
| Assessing Post-Typhoon Nighttime Lighting Recovery Using VIIRS and Change-Point Detection (10 words) | Revise the outcome, and do not take to faculty as a finalist | VIIRS `avg_rad` is monthly radiance. No typhoon footprint was joined to it, and no restoration ledger was opened. Google Community Mobility Reports stopped new data on 15 October 2022. The outcome that remains is observed lighting change. |

## Handoff titles

The nine titles in `thesis_handoff.md` were screened in the field files. None becomes an active title.

| Handoff title | Disposition |
| --- | --- |
| Physics-informed deep learning for convective storm initiation | Park. The opened DOI `10.1029/2024EA003571` is a South China Himawari study, abstract only. The Himawari registry does not supply initiation labels. |
| Spatiotemporal graph networks for dust and aerosol metrics | Park. DOI `10.5194/isprs-annals-X-5-2024-151-2024` is Project AiRMoVE. The MAIAC page describes column aerosol optical depth. |
| GAN super-resolution of satellite precipitation | Backup only, and not one of the two consultation directions. IMERG V07 is half-hourly. DOI `10.13203/j.whugis20230013` is a Chinese-data GAN, abstract page only. Philippine gauge truth was not opened. |
| Segment-Anything detection of informal settlement growth | Stop. Planet education access is non-commercial. Imagery appearance does not establish legal tenure. |
| Nighttime lights fused with mobility as economic recovery | Stop. Mobility reports ended new data on 15 October 2022. The lighting-change wording above is the remainder, and it is not a consultation direction. |
| Object detection of green access and thermal comfort from Sentinel-2 | Stop. The official Sentinel-2 pages do not provide a thermal band. |
| Multispectral nighttime imagery as ecological disruption | Not activated. SDGSAT-1 access requires an approved proposal. No paired Philippine ecological outcome was opened. |
| Astronomical source detection transferred to terrestrial features | Park. Wagstaff and colleagues (2018) adapt an Earth-trained network to Mars imagery. |
| Contrastive classification of Martian and terrestrial surfaces | Park. Zenodo 4002935 contains Martian classes. Its 64,947 images come from 10,815 original landmarks and 232 source images. |

## What the two conditional directions would have to show

These paragraphs are scopes for a later consultation. They are not results.

**Heat alerts.** The question is whether a conformalized XGBoost model, using only information available at forecast time, can give a 24-hour-ahead station heat-index exceedance alert whose error, recall, false alerts, calibration, and interval coverage improve on previous-day persistence, seasonal climatology, and a simple regression, in held-out years and cities. El Niño is a possible stratum for a later study. It is not an assumed cause of higher heat index in every city and season. The Western Luzon monthly ENSO and heat-index paper named in the plan was not retrieved, so it is neither a citation nor a novelty claim.

**LGU radiance.** The question is whether XGBoost can forecast next-period average nighttime radiance, in nW/cm²/sr, for Philippine local governments from earlier radiance and public covariates, against persistence and a simple regression, with local governments or months held out. A rise in that series is a change in the satellite product. Visible-star, ecological, and tourism outcomes were stopped in the astronomy screen.

## Prospective organizations

`client-lists.csv` has 38 rows, each marked opened on 6 October 2026. That is a row count. It is not a count of distinct organizations. Four titles have fewer than three organization names: creative thinking has one (the Department of Education, across three units); the ENSO heat-alert title has two (PAGASA and Quezon City Government); population-weighted heat exposure has those same two; urban green access has two (Quezon City Government and the Philippine Space Agency). The city heat-alert title has three organization names. The LGU rows have four, and they still use the earlier title “Forecasting Philippine LGU Nighttime-Light Growth Using XGBoost for Dark-Sky Planning,” which this screen replaced with a radiance-only wording. Interest, data access, and procurement are unconfirmed on every row. National Center for Mental Health, Philippine Normal University, the Department of Tourism, MMDA, DHSUD, NDRRMC, and OCD did not open, so they are absent from the CSV. A client row does not revive a title that failed the record gate.

## Claim map

Material numbers in this memo are tied to `evidence-ledger.md`. Field search logs and quotations remain in:

- `evidence-psychology.md`
- `evidence-astronomy.md`
- `evidence-meteorology.md`
- `evidence-urban.md`
- `data-feasibility.md`

## Unresolved before any title is proposed

1. A quality-controlled Philippine station-hour file with temperature and humidity or dew point, and a count after exclusions.
2. An LGU-month VIIRS extract with cloud-free coverage and a licensed boundary file. The PSA page used for an official LGU count returned HTTP 403.
3. The full text of Lafi and Bumi (2025), DOI `10.4103/shb.shb_370_24`, if the group still wants to know whether that paper already used latent classes. The age-band count already fails the record rule.
4. An official PISA 2022 codebook. OECD pages returned HTTP 403.
5. Whether any iHeatMap or iRISE-UP forecast was archived at its issue time.
6. Written permission for protected-area polygons, if a dark-sky site study is ever revived. The opened counts are already below 10,000 sites.

## QA status

Follow-up review, in `qa-followup.md`: pass with limitations. Findings M1, L1, L2, L3, and L4 from `qa-review.md` are resolved. No title is a passed finalist. The two consultation directions stay conditional because the station-hour file and the LGU-month extract were not built. The unresolved data, codebook, and permission items in `qa-review.md` remain open.
