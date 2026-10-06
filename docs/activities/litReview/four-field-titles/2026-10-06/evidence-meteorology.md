# Literature screen: meteorological analytics

Generated: 6 October 2026
Review type: scoping (one bounded title screen, not a systematic review)
Search window: 2021–2026, plus essential earlier studies when a gate required them
Indexes: Crossref REST API and PubMed. Semantic Scholar was attempted and returned HTTP 429. Europe PMC was used only as a supplemental locator after those indexes did not retrieve a Western Luzon heat-index study.
User-Agent: `thesis1-litreview/1.0 (https://github.com/u1yuan/django-flow)`
Track: city heat advisories for a Philippine undergraduate CS Data Science thesis. Hydroponics, diesel, and Native Trees were not searched. Satellite surface temperature is not treated as a pedestrian-comfort result.

## Research question

Can a Philippine undergraduate data-science thesis evaluate next-day urban heat-alert reliability, optionally stratified by finalized ENSO regime, without treating “Super El Niño” as an official class or treating El Niño as a cause of higher heat index in every city and season?

Technical frame:

- Domain: Philippine city heat advisories.
- Technique named in the active titles: conformalized XGBoost, or spatial random forests for the conditional exposure title.
- Comparison: previous-day persistence, seasonal climatology, and simple regression.
- Metrics named in the design, not computed here: error, recall, false alerts, calibration, and interval coverage, on held-out years and cities.

## What WMO and NOAA say about “super” and very strong

These are separate statements from separate opened pages.

**WMO does not use “super,” and this page gives no numeric threshold.** The plan URL `https://public.wmo.int/themes/el-nino-la-nina-phenomena` returned HTTP 200 on 6 October 2026. It did not fail. `https://wmo.int/topics/el-nino-la-nina` redirected to `https://wmo.int/themes/el-nino-la-nina-phenomena`. On the opened page, paragraph text states: “The strength of an ENSO event is highly significant – whether it is classed as weak, moderate, strong or very strong. WMO does not use the term Super El Niño or La Niña.” The same page describes the Oceanic Niño Index and the Relative Oceanic Niño Index, and it does not state a ≥ +2.0°C rule. It also states: “Not all regions of the world are affected, and even within a region, impacts can be different.”

**NOAA names numeric RONI bins and does not use “super” on the pages opened here.** The June 2026 strengths archive, `https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/archives/?month=06&type=strengths&year=2026`, says the color shading shows “weak, moderate, strong, and very strong.” Its table headers for warm bins are `0.5°C ≤ Index < 1.0°C`, `1.0°C ≤ Index < 1.5°C`, `1.5°C ≤ Index < 2.0°C`, and `Index ≥ 2.0°C`. The legend image on that page, `strengths-labeled-example.png`, labels the warm segments, from the lightest to the darkest, as “weak El Niño,” “moderate El Niño,” “strong El Niño,” and “very strong El Niño.” The word “super” does not appear on that archive page. The same page says probabilities are verified with RONI “using incremental -/+ 0.5 degree Celsius thresholds,” and: “The strength of El Niño or La Niña does not necessarily correspond with the strength of the influence or expected impact.”

**Initial RONI values can change.** This sentence is on the historical RONI page, not on the strengths-archive URL. Opened `https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/`: “Because of the high frequency filter applied to the ERSSTv6 data (Huang et al., 2025, Part 1 and Part 2, J. Climate), RONI values may change up to two months after the initial "real time" value is posted. Therefore, the most recent RONI values should be considered an estimate.” Huang et al. 2025 was not opened. Finalized RONI is the appropriate retrospective label. Issue-time archives of the first posted value were not opened, so issue-time stratification is not verified.

**A forecast of a very strong event is not a completed ≥ +2.0°C episode.** The ENSO Diagnostic Discussion issued 10 September 2026 (`ensodisc.shtml`) says: “El Niño is strengthening, with a greater than 90% chance of a very strong event during the Northern Hemisphere fall and winter 2026-27.” It also gives “a 75% chance of a historic event that would exceed the strength of previous El Niño events dating back to 1950 (+2.5°C or more for a 3-month RONI value)” for October–December 2026, and says impacts consistent with El Niño are “larger, though not guaranteed.” That page does not use “super.” The +2.5°C figure is an outlook threshold in that discussion, not the ≥ 2.0°C column header on the strengths archive.

## Search strategy

Inclusion: English or officially bilingual public pages; journal articles, official dataset documentation, and agency pages; 2021–2026, with earlier studies kept when they are the nearest heat-risk map or the RONI episode record; Philippine city heat index, ENSO stratification, or the three handoff DOIs.

Exclusion: wrong hazard or place; book-index records returned by loose Crossref ranking; hydroponics, diesel, and Native Trees; restricted PAGASA climatology and Quezon City station histories; claims that require a station-hour file that was not opened; model scores that this screen did not compute.

Crossref `query.title` and `query.bibliographic` returned very large totals. Only the first result page of each query was screened. Those queries are not exact-phrase filters. PubMed was the second index that returned records. Semantic Scholar search returned HTTP 429 on every call on 6 October 2026, including a later single retry, so it contributed no hits.

No duplicate corpus was merged. Targeted DOI opens were checked against Crossref or the publisher page. One DOI, `10.13203/j.whugis20230013`, is absent from Crossref (HTTP 404) and was resolved through `doi.org` to the China DOI page and then the CNKI overseas abstract page.

## Search log

| Database or page | Date searched | Query or target | Filters | Results screened | Export |
| --- | --- | --- | --- | --- | --- |
| Crossref REST | 2026-10-06 | `query.bibliographic="heat index" "Western Luzon"` | first page, 12 rows | 12 titles; no heat-index/ENSO article | titles and DOIs in session notes |
| Crossref REST | 2026-10-06 | `query.title=heat index Western Luzon` | first page, 8 rows | 8 titles; geology and unrelated heat-index papers | titles and DOIs |
| Crossref REST | 2026-10-06 | `query.title=ENSO heat index Philippines` | first page, 8 rows | 8 titles; nearest heat-index item is a correspondence, not a Western Luzon analysis | titles and DOIs |
| Crossref REST | 2026-10-06 | `query.bibliographic="heat index" Philippines`, `from-pub-date:2015-01-01` | first page, 15 rows | screened; two public-health items kept as leads | titles and DOIs |
| Crossref REST | 2026-10-06 | `query.title=conformal prediction`, `from-pub-date:2021-01-01`, `type:journal-article` | first page, 15 rows | statistical methods; none is a Philippine heat-index alert | titles and DOIs |
| Crossref REST | 2026-10-06 | `query.title=super-resolution downscaling precipitation GAN`, `from-pub-date:2021-01-01` | first page, 8 rows | GAN or super-resolution precipitation papers exist; the handoff DOI was not in this page | titles and DOIs |
| Crossref REST | 2026-10-06 | `query.title=Physics-Informed Deep Learning Convective Storm Initiation` | first page, 5 rows | no matching convective-initiation deep-learning paper | titles |
| Crossref REST | 2026-10-06 | `query.title=Spatiotemporal Graph Neural Networks Atmospheric Dust` | first page, 5 rows | no dust-tracking GNN; unrelated spatiotemporal GNN papers | titles |
| Crossref works | 2026-10-06 | DOI lookup for the handoff and heat-risk DOIs | exact DOI | metadata for five DOIs; `10.13203/j.whugis20230013` returned 404 | JSON metadata |
| PubMed E-utilities | 2026-10-06 | `("heat index"[tiab]) AND (Philippines OR Luzon) AND (ENSO OR "El Nino" OR "El Niño")` | none beyond the query | count 0 | PMID list empty |
| PubMed E-utilities | 2026-10-06 | `("heat index"[tiab]) AND (Philippines OR Luzon)` | none | count 2: PMIDs 38778715 and 42618691 | esummary |
| PubMed E-utilities | 2026-10-06 | `("urban heat" OR "heat vulnerability" OR "heat risk") AND Philippines` | none | count 2: PMIDs 32221303 and 27832866 | esummary |
| PubMed E-utilities | 2026-10-06 | `"Western Luzon"[tiab] AND (heat OR temperature OR ENSO OR "El Nino")` | none | count 0 | empty |
| PubMed E-utilities | 2026-10-06 | `(Philippines OR Luzon) AND (ENSO OR "El Nino") AND (heat OR "heat index" OR heatwave OR "apparent temperature")` | relevance, 30 max | count 2; neither is a Western Luzon heat-index study | esummary |
| PubMed E-utilities | 2026-10-06 | `"conformal prediction"[tiab] AND (weather OR temperature OR heatwave OR precipitation)` | 10 of 12 | one precipitation-forecast paper kept as a distant lead; no heat-index alert paper | esummary |
| Semantic Scholar API | 2026-10-06 | Western Luzon heat index ENSO, plus three related queries, plus one later retry | limit 5–8 | HTTP 429; zero records retrieved | error JSON |
| Europe PMC REST | 2026-10-06 | `TITLE_ABS:"heat index" AND "Western Luzon"` | page size 10 | hitCount 0 | JSON |
| Europe PMC REST | 2026-10-06 | `TITLE:"heat index" AND (Philippines OR Luzon)` | page size 10 | hitCount 2; same two public-health items as PubMed | JSON |
| Official pages | 2026-10-06 | WMO ENSO theme, NOAA RONI history, NOAA June 2026 strengths archive, NOAA 10 September 2026 discussion, PAGASA press release 174, Quezon City heat-index page, Himawari registry, MAIAC catalog, IMERG V07 HTML and PDF | public HTML or PDF | opened; passages quoted below | not a bibliographic export |

## Claim-level ledger

| ID | Claim or question | Source | Locator | Status | Caveat |
| --- | --- | --- | --- | --- | --- |
| C1 | WMO does not use “Super El Niño or La Niña,” and classes strength as weak, moderate, strong, or very strong. | WMO ENSO theme page, HTTP 200 | Paragraph beginning “The strength of an ENSO event is highly significant” | Verified from opened page | No Celsius threshold on this page |
| C2 | ENSO impacts are not uniform across regions or within a region. | Same WMO page | “Not all regions of the world are affected, and even within a region, impacts can be different.” | Verified from opened page | This is not a Philippine heat-index result |
| C3 | NOAA’s opened strengths archive uses 0.5°C RONI bins ending at `Index ≥ 2.0°C`, and the legend names the darkest warm segment “very strong El Niño.” | CPC RONI strengths archive for June 2026, plus `strengths-labeled-example.png` | Table headers and legend image alt text and labels | Verified from opened page and image | The HTML does not put the words “very strong” inside the `Index ≥ 2.0°C` header; the mapping is the ordered bins plus the ordered legend |
| C4 | The word “super” is absent from the opened NOAA RONI history page, the June 2026 strengths archive, and the 10 September 2026 diagnostic discussion. | Those three NOAA URLs | Full-text keyword count on the opened HTML | Verified for those pages | Other NOAA pages were not exhaustively searched |
| C5 | Recently posted RONI values may change for up to two months and should be treated as estimates. | CPC RONI historical page | Notice paragraph citing the ERSSTv6 high-frequency filter | Verified from opened page | Huang et al. 2025 was not opened |
| C6 | A stronger El Niño class does not by itself establish a stronger local impact. | June 2026 strengths archive | “The strength of El Niño or La Niña does not necessarily correspond with the strength of the influence or expected impact.” | Verified from opened page | Supports using ENSO as a stratum, not as a cause |
| C7 | On the RONI table opened 6 October 2026, colored warm episodes with at least one season ≥ 2.0°C are 1965–66 (peak 2.0), 1972–73 (peak 2.0), 1982–83 (peak 2.4), 1991–92 (peak 2.1), 1997–98 (peak 2.3), and 2015–16 (peak 2.3). | CPC RONI historical table, 1950–2026 | Year rows and `roni-warm` cells | Verified by parsing the opened table | Overlapping seasons are one episode. Philippine heat-index pairing was not checked. The page colors a warm episode only after five consecutive overlapping seasons beyond ±0.5°C |
| C8 | The 2023–24 warm episode on that table peaks at 1.4°C (OND and NDJ 2023), not at ≥ 2.0°C. | Same table | 2023 and 2024 rows | Verified from opened table | This contradicts treating 2023–24 as a completed very-strong RONI episode |
| C9 | As opened, 2026 seasons through JAS are not a finalized very-strong episode. JAS 2026 is printed as 1.7 and is not in the warm-episode color class. | Same table, read with C5 | 2026 row | Verified as the table stood when opened | Recent values are estimates under C5. The September 2026 discussion is an outlook, not this table |
| C10 | PAGASA’s iHeatMap is an existing nationwide heat-index service with gridded information, color-coded alerts, and hourly forecasts. | `https://bagong.pagasa.dost.gov.ph/press-release/174?page=6`, dated 4 April 2025 on the page | Launch announcement body | Verified from opened page | The page does not provide an archive of issue-time forecasts. Personal contact details in the release are omitted here |
| C11 | Quezon City’s opened page is a 24-hour maximum heat-index message tied to iRISE-UP, dated 22 April 2024 on the page, not a multi-year forecast archive. | `https://quezoncity.gov.ph/24-hr-maximum-heat-index-forecast/` | Page heading and the iRISE-UP paragraphs | Verified from opened page | Filipino text quoted below. Station history was not requested |
| C12 | Yang and colleagues used physics-augmented random forest and Himawari-8 for convective-initiation nowcasting in South China, April–September 2019. | `10.1029/2024EA003571` | Crossref abstract | Abstract-only | Wiley PDF returned a Cloudflare challenge. Not deep learning, not GOES-R or Meteosat, and not the Philippines |
| C13 | NOAA’s Himawari-8/9 registry covers east Asia and the west and central Pacific, with Full Disk archive data back to July 2015, and NOAA states that it may distribute the data freely. | `https://registry.opendata.aws/noaa-himawari/` | Description and distribution paragraphs | Verified from opened page | The opened paragraphs do not name the Philippines. Coverage of the Philippines is an inference from the stated disk, not a label count |
| C14 | Ramos and colleagues describe Project AiRMoVE as remote sensing, GIS, and numerical modeling for NCR air-quality management, including MODIS MAIAC AOD used to estimate PM with regression and machine learning, plus EMB station PM2.5 and PM10. | `10.5194/isprs-annals-X-5-2024-151-2024` | PDF page 3, section 2.1 | Verified from opened PDF | Not a spatiotemporal graph neural network and not a dust-identity tracker. Torres et al. 2023c, cited there, was not opened |
| C15 | MCD19A2 Version 6.1 is a daily 1 km MAIAC land aerosol optical depth grid. | data.gov catalog page named in the brief | Product description | Verified from opened catalog page | The page describes column AOD layers. It does not define the product as mineral-dust identity or ground-level PM2.5 |
| C16 | Zhang and colleagues trained a twofold GAN super-resolution model on CMPA 5 km precipitation and applied it to daily IMERG and ERA5, then compared it with a multifractal model and random forest using station observations. | `10.13203/j.whugis20230013` | CNKI overseas abstract page; journal line 武汉大学学报(信息科学版), 2025, 50(10), pages 2035–2047+2085 | Abstract-page verified | Crossref has no record. Full PDF was not opened. The abstract does not report a Philippine domain |
| C17 | IMERG combines precipitation estimates into half-hourly 0.1°×0.1° fields and issues Early (~4 h), Late (~14 h), and Final (~3.5 months, after the monthly gauge analysis) runs. | IMERG V07 technical documentation, 13 July 2023, PDF linked from the opened NASA page | PDF pages 5–6 | Verified from opened PDF | A finer grid is not a Philippine gauge-skill result |
| C18 | Estoque and colleagues mapped heat-health risk for 139 Philippine cities with remotely sensed land surface temperature and social-ecological indicators for the hot dry season, because measured air temperature was lacking for a nationwide city analysis. | `10.1038/s41467-020-15218-8` | Abstract and the LST-versus-air-temperature paragraph in the opened HTML | Verified from opened HTML | Not heat index, not ENSO stratification, and not barangay air temperature. “enso” string matches inside “sensor” were ignored |
| C19 | A Western Luzon monthly ENSO and heat-index study was not retrieved. | PubMed, Crossref first pages, Europe PMC | Queries in the search log | Not found | The plan’s novelty caution cannot be tied to an opened paper. The combination is also not established as novel |
| C20 | No NOAA station-hour file was opened, so a count of 10,000 valid station-hours is not available. | This screen | No station file in the opened set | Not established | Do not cite 10,000 as a result |
| C21 | No conformalized XGBoost heat-index forecast for Philippine cities was found in the screened Crossref or PubMed pages. | Search log | First pages and PubMed summaries | Not found in the screened set | Absence from these pages is not a novelty proof |

## Word counts

Counts are whitespace tokens. Hyphenated compounds count as one token. The parenthetical `(GANs)` counts as one token.

| Title | Tokens | Technique named in the title | Length gate |
| --- | ---: | --- | --- |
| Evaluating Urban Heat Alert Reliability Across Philippine Cities Using Conformalized XGBoost | 11 | Conformalized XGBoost | Within 16 |
| Evaluating Philippine Urban Heat Alert Reliability Across ENSO Regimes Using Conformalized XGBoost | 12 | Conformalized XGBoost | Within 16 |
| Estimating Population-Weighted Urban Heat Exposure Across Philippine Cities Using Spatial Random Forests | 12 | Spatial random forests | Within 16 |
| Physics-Informed Deep Learning for Convective Storm Initiation Forecasting Using Geostationary Satellite Imagery | 12 | Physics-informed deep learning | Within 16; park |
| Spatiotemporal Graph Neural Networks for Tracking Atmospheric Dust and Aerosol Dispersion Metrics | 12 | Spatiotemporal graph neural networks | Within 16; park |
| Super-Resolution Downscaling of Satellite-Derived Precipitation Data Using Generative Adversarial Networks (GANs) | 11 | Generative adversarial networks | Within 16; conditional backup only |

## Title cards

### 1. Evaluating Urban Heat Alert Reliability Across Philippine Cities Using Conformalized XGBoost

Gate: **revise**

Question: using only information available at forecast time, how reliably can conformalized XGBoost predict station heat index and threshold exceedance 24 hours ahead in Philippine cities?

Technique: conformalized XGBoost. The title names it. Length is 11 words.

Beneficiary: a prospective user is an agency that already issues heat information. Opened services are PAGASA iHeatMap (4 April 2025 release) and Quezon City iRISE-UP (page dated 22 April 2024). Interest, data sharing, and endorsement are unconfirmed. Other organizations listed in the plan were not re-opened in this screen.

Data source and rights: no station file was opened. The 10,000-record gate is unmet (C20). Restricted PAGASA climatology and Quezon City automated-station histories were not requested. A public NOAA station source remains a candidate only until a codebook and a counted extract exist.

Record-count gate: not passed. Do not state that 10,000 valid station-hours exist.

Baseline and validation design, not results: previous-day persistence at the same hour, seasonal climatology, and a simple regression. Report error, recall, false alerts, calibration, and prediction-interval coverage. Hold out whole years and whole cities. No score was computed here.

Nearest prior art: iHeatMap and iRISE-UP are existing services, not unpublished gaps. Direct comparison requires forecasts saved at issue time and matched observations. Those archives were not opened. Estoque et al. (2020) is a city heat-health risk map from land surface temperature, not a next-day heat-index alert. Screened Crossref and PubMed pages did not yield a conformalized XGBoost heat-index paper for Philippine cities (C21). That absence is not a novelty claim.

Social implication and adoption value: the PAGASA release describes schedule, road-work, and outdoor-work responses that need timely heat-hazard information. A thesis could matter if it measures missed events and false alerts rather than repeating a real-time map. Adoption value is unconfirmed.

Ethical constraints: alerts can change school or work decisions. False alerts and missed exceedances both have costs. Do not infer illness or death from heat index alone. Do not use restricted operational feeds without permission.

Three-trimester feasibility: the modeling design is small enough for three trimesters only after the station-hour audit passes. It is not feasible to promise a comparison with iHeatMap or iRISE-UP until issue-time archives are shown to exist.

Why revise rather than proceed: the wording and the technique pass. The data count, the issue-time comparison, and the nearest-forecast check do not.

### 2. Evaluating Philippine Urban Heat Alert Reliability Across ENSO Regimes Using Conformalized XGBoost

Gate: **revise**

Question: after a next-day heat-index alert model is evaluated, do retrospective forecast error and calibration differ by city, monsoon season, and finalized RONI regime?

Technique: conformalized XGBoost. Length is 12 words. Do not put “Super” in the title. WMO does not use that word (C1). NOAA’s opened pages do not use it either (C4).

Beneficiary: same heat-advisory users as title 1, still unconfirmed. PAGASA’s public ENSO monitoring page was not opened in this screen; the plan lists it, and that listing is not a new verification.

Data source and rights: finalized RONI from the opened CPC table may be used for retrospective stratification. The notice on that page says recent real-time values can change for up to two months (C5). Archived issue-time RONI values were not verified. Station heat index still requires the unmet count in C20.

Record-count gate: not passed for station-hours. For the ≥ +2.0°C bin, the opened table shows six historical warm episodes with at least one season at or above 2.0°C (C7). That is more than one episode on the index. It is not a count of usable Philippine forecast episodes. 2023–24 peaks at 1.4°C on this table (C8). The 10 September 2026 discussion forecasts a possible very strong event; it does not record a finished one (C9).

Baseline and validation design: the alert baselines and metrics of title 1, then stratify retrospective errors by regime. Hold out whole event years. Overlapping three-month seasons inside one episode are not independent replicates. Two episodes would be too few for a broad claim. Six index episodes still do not authorize a general claim about Philippine alert skill, because the heat-index pairs were not audited.

Nearest prior art: the plan says monthly ENSO and heat-index patterns in Western Luzon have already been studied. PubMed, the screened Crossref pages, and Europe PMC did not retrieve that study (C19). The combination of ENSO and heat index is therefore not available as a verified citation, and it is also not available as a novelty claim. NOAA’s own sentence separates event strength from local impact strength (C6). WMO says effects differ by region (C2).

Social implication: a regime-specific false-alert rate could change how a city uses a seasonal outlook. It does not show that El Niño raises the heat index in every city or season.

Ethical constraints: do not present a forecast discussion as if the event had already reached ≥ +2.0°C. Do not use unfinalized 2026 RONI values as if they were stable classes.

Three-trimester feasibility: stratification is inexpensive only after title 1’s station audit exists. A ≥ +2.0°C generalization should not be a primary objective.

Why revise: keep finalized RONI as a retrospective stratum, remove any “super” wording, and do not treat 2023–24 or the 2026 outlook as a completed very-strong sample.

### 3. Estimating Population-Weighted Urban Heat Exposure Across Philippine Cities Using Spatial Random Forests

Gate: **stop**

Question as written: can spatial random forests estimate population-weighted urban heat exposure across Philippine cities?

Technique: spatial random forests. Length is 12 words.

Why stop: Estoque et al. (2020), opened in full HTML, already assessed heat-health risk in 139 Philippine cities, about 40% of the national population in their abstract, using remotely sensed surface temperature and social-ecological indicators for the hot dry season. Manila had the very high heat-health risk index in that paper. They write that they used land surface temperature “in response to a lack of the measured air temperature data needed to support a nationwide city-level analysis.” They also write that the relationship between remotely sensed land surface temperature and measured air temperature is complicated. A new model that combines coarse reanalysis with population pixels would not establish barangay air temperature, and it would sit on top of an existing city heat-risk map. Population density in that paper is an exposure indicator, not a pedestrian-comfort measurement.

Data and rights: no reanalysis extract, population grid, or barangay boundary file was opened. The 10,000-record gate was not counted. Restricted station histories were not requested.

Nearest prior art that was opened: Estoque et al. 2020 is the nearest Philippine urban heat-risk map. The 2017 Southeast Asian megacity surface-temperature paper (DOI `10.1016/j.scitotenv.2016.10.195`) was identified in PubMed and Crossref metadata only; its full text was not opened, so it stays a lead.

Revival condition, not a proceed decision: a later study would need ground-measured air temperature or heat index at the claimed scale, a contribution that Estoque et al. did not already make, and a counted record file. Satellite surface temperature remains a surface-temperature result.

Beneficiary, ethics, and feasibility: city health or environment offices might use a validated exposure layer. No such validation exists in this screen. Three trimesters do not repair the missing air-temperature observations.

## Handoff dispositions

### Physics-Informed Deep Learning for Convective Storm Initiation Forecasting Using Geostationary Satellite Imagery

Disposition: **park**

The title has 12 words and names a technique. The DOI the plan attaches, `10.1029/2024EA003571`, is a different study. Crossref title is “Convective Initiation Nowcasting in South China Using Physics-Augmented Random Forest Models and Geostationary Satellites,” Yang et al., *Earth and Space Science*, volume 11, issue 7, July 2024. The deposited abstract says the Storm Warning System with Physics-Augmentation uses random forest and Himawari-8 Advanced Himawari Imager data from April to September 2019 in South China, adds cloud-top cooling and ancillary fields, and reports higher detection and lower false alarms than the abstract’s conventional comparison, with example lead times of about 30 minutes to 1 hour before radar. Those performance numbers are the paper’s abstract claims, not results computed here. Status: abstract-only, because the publisher PDF was blocked.

The handoff title’s GOES-R/Meteosat mix is not this paper and is not the local default. The opened Himawari registry says Himawari-9 is at 140.7°E, with Himawari-8 as backup, and covers “east Asia, and the west and central Pacific,” with Full Disk archive products back to July 2015. NOAA says it distributes the data freely and openly and requests attribution; modified data must not be presented as unaltered. The opened registry text does not name the Philippines and does not supply labeled convective-initiation events. Imagery volume is not 10,000 independent initiation labels. No Philippine radar or equivalent label archive was opened. A Crossref title search did not place this handoff title on the first result page.

### Spatiotemporal Graph Neural Networks for Tracking Atmospheric Dust and Aerosol Dispersion Metrics

Disposition: **park**

The title has 12 words and names a technique. The DOI the plan attaches, `10.5194/isprs-annals-X-5-2024-151-2024`, is Ramos et al., “Enhancing Government Capacity for Air Quality Management in the Philippines through Geospatial Technologies: A Case of Project AiRMoVE,” ISPRS Annals, volume X-5-2024, pages 151–158, 11 November 2024, Creative Commons Attribution 4.0. The opened PDF is an overview of workshops, training, and stakeholder work by UP TCAGP with NCR airshed partners. On PDF page 3 it says MAIAC AOD from MODIS “were utilized to estimate particulate matter through regression analysis and machine learning algorithms (Torres et al., 2023c)” and that EMB stations supplied PM2.5 and PM10. It does not implement a spatiotemporal graph neural network. The two “dust” string hits in the PDF are inside “industrialization” and “Industry,” not a dust-tracking analysis. Torres et al. 2023c was not opened.

The opened MAIAC catalog page describes MCD19A2 Version 6.1 as daily 1 km land AOD, including 0.47 µm and 0.55 µm AOD, uncertainty, fine-mode fraction over water, column water vapor, and smoke injection height. That is a column aerosol product. It is not mineral-dust identity and not ground-level PM2.5. A Crossref title search did not place the handoff GNN title on the first result page. No file of 10,000 quality-controlled ground observations was opened.

### Super-Resolution Downscaling of Satellite-Derived Precipitation Data Using Generative Adversarial Networks (GANs)

Disposition: **conditional backup, do not promote**

The title has 11 words and names GANs. The DOI `10.13203/j.whugis20230013` is not the English handoff title. Crossref returned HTTP 404. `doi.org` resolved to the China DOI registry, which gives the title 降水融合数据特征驱动下基于GAN的遥感降水产品空间超分辨率重建, authors 张唯, 吉宸佳, 李文凯, 孙晓娜, 梁天欣, 韩松洁, and 卫鸿飞, registered 2024-05-17. The CNKI overseas abstract page places it in 武汉大学学报(信息科学版), 2025, volume 50, issue 10, pages 2035–2047+2085. The abstract says a twofold GAN super-resolution model was built from CMPA precipitation fusion data at 5 km, applied to IMERG daily precipitation and ERA5 daily precipitation, producing 0.05° IMERG and 0.125° ERA5 fields, and evaluated with station observations. It says the GAN fit IMERG better than a multifractal model and a random forest. The abstract does not name the Philippines. Full text beyond that abstract page was not opened. Status: abstract-page verified.

IMERG V07, opened as the 13 July 2023 technical documentation, states that estimates “are combined into half-hourly 0.1°×0.1° fields” and that the runs are Early at about 4 hours, Late at about 14 hours, and Final at about 3.5 months after the monthly gauge analysis. Half-hourly 0.1° fields show that Philippine-covering estimates are frequent in the product design. They do not show that a downscaled pixel is more accurate over the Philippines. No Philippine gauge or radar truth file, and no count of 10,000 eligible space-time units, was opened. Other 2021–2026 GAN or super-resolution precipitation papers appeared on the first Crossref page, which is enough to reject a claim that the method is unsearched. This remains a backup only if an independent Philippine gauge or radar set is later opened and heavy-rain skill is tested on held-out storms.

## Thematic synthesis

The operable heat-advisory question is a 24-hour-ahead station heat index and threshold decision, judged against persistence, climatology, and simple regression, with false alerts and interval coverage on held-out years and cities. PAGASA and Quezon City already publish heat-index products. The thesis would have to add an evaluation those pages do not contain. Those pages do not show that issue-time forecasts were archived.

El Niño belongs in the design as a retrospective stratum from finalized RONI. WMO refuses the word “super” and gives no number. NOAA’s opened archive uses a ≥ 2.0°C bin as the top warm category and warns that strength is not impact. The historical table contains six warm episodes that touch that bin. The recent 2023–24 episode does not, and the 2026 discussion is a probability outlook. None of those episodes has been paired with a counted Philippine heat-index forecast sample.

City heat-risk mapping with surface temperature and population already exists for 139 Philippine cities. The authors of that study say they used surface temperature because city-scale air temperature was lacking, and they treat the surface-to-air relationship as complicated. That is the nearest opened map, and it blocks the population-weighted exposure title as written.

The three handoff DOIs do not match the three handoff titles. Each opened work is a nearby method or a nearby Philippine application, and each one argues for parking or for leaving the precipitation GAN as a backup.

Confidence: high for the WMO wording, the NOAA revision notice, the RONI table values as opened, the iHeatMap and Quezon City page contents, the IMERG run definitions, the AiRMoVE PDF, and the Estoque HTML. Medium for Yang et al., because only the Crossref abstract was opened, and for Zhang et al., because only the CNKI abstract page was opened. Low for any statement about the Western Luzon study, because it was not found.

## Gaps and limitations

- Semantic Scholar contributed no records because of HTTP 429.
- Crossref screens used the first result page only. A relevant paper ranked later would have been missed.
- The Western Luzon ENSO and heat-index study named by the plan was not opened. Do not invent its authors, year, or findings, and do not call the topic new.
- Yang et al. full text was not opened. Zhang et al. full text was not opened. Estoque’s 2017 surface-temperature paper was not opened.
- No station-hour, gauge, radar, or population-grid file was counted.
- The June 2026 strengths page is an outlook archive. Its probability cells were not copied into this ledger.
- Recent RONI numbers, including 2026, can change for up to two months after first posting.
- Himawari coverage of the Philippines is inferred from the stated satellite disk. The registry page did not say “Philippines” in the paragraphs used here.
- This file reports no model performance.

## Open questions

1. Which opened full text is the Western Luzon monthly ENSO and heat-index study, and what period, stations, and ENSO index did it actually use?
2. After quality control, how many Philippine city station-hours have paired temperature and humidity or dew point, in which years and cities, and under what NOAA or PAGASA license?
3. Does any public archive store iHeatMap or iRISE-UP forecasts as they were issued, with the issue time intact?
4. Which finalized RONI episodes can be paired with those station-hours if whole event years are held out, and how many of those pairs fall in a season ≥ +2.0°C?
5. If exposure mapping is revived, what ground air-temperature or heat-index sample would show a result Estoque et al. (2020) did not already report?

## References opened for this screen

WMO. El Niño / La Niña Phenomena. `https://public.wmo.int/themes/el-nino-la-nina-phenomena`. Opened 6 October 2026.

NOAA Climate Prediction Center. Relative Oceanic Niño Index (RONI). `https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/`. Opened 6 October 2026.

NOAA Climate Prediction Center. ENSO strength probabilities archive, June 2026. `https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/archives/?month=06&type=strengths&year=2026`. Opened 6 October 2026.

NOAA Climate Prediction Center. ENSO Diagnostic Discussion, 10 September 2026. `https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml`. Opened 6 October 2026.

DOST-PAGASA. “DOST-PAGASA Launches iHeatMap: An Online Heat Index Monitoring Platform.” Press release dated 4 April 2025 on the page. `https://bagong.pagasa.dost.gov.ph/press-release/174?page=6`. Opened 6 October 2026.

Quezon City Government. “24-HR MAXIMUM HEAT INDEX FORECAST.” Page dated 22 April 2024. `https://quezoncity.gov.ph/24-hr-maximum-heat-index-forecast/`. Opened 6 October 2026.

Yang, C., Yuan, H., Zhang, F., Xie, M., Wang, Y., & Jiang, G.-M. (2024). Convective initiation nowcasting in South China using physics-augmented random forest models and geostationary satellites. *Earth and Space Science, 11*(7). `https://doi.org/10.1029/2024EA003571`. Abstract-only.

NOAA Open Data Dissemination. JMA Himawari-8/9. `https://registry.opendata.aws/noaa-himawari/`. Opened 6 October 2026.

Ramos, R., Tamondong, A., Torres, R. A., Recto, B. A., Panlilio, K., Sta. Ana, R. R., Tinio, M. L., Yumul-Calzado, T., Carcellar, B. III, & Cayetano, M. (2024). Enhancing government capacity for air quality management in the Philippines through geospatial technologies: A case of Project AiRMoVE. *ISPRS Annals, X-5-2024*, 151–158. `https://doi.org/10.5194/isprs-annals-X-5-2024-151-2024`. PDF opened.

NASA. MODIS/Terra+Aqua Land Aerosol Optical Depth Daily L2G Global 1km SIN Grid V061. `https://catalog.data.gov/dataset/modis-terraaqua-land-aerosol-optical-depth-daily-l2g-global-1km-sin-grid-v061`. Opened 6 October 2026.

张唯, 吉宸佳, 李文凯, 孙晓娜, 梁天欣, 韩松洁, 卫鸿飞. (2025). 降水融合数据特征驱动下基于GAN的遥感降水产品空间超分辨率重建. *武汉大学学报(信息科学版), 50*(10), 2035–2047+2085. `https://doi.org/10.13203/j.whugis20230013`. CNKI abstract page opened; Crossref record absent.

Huffman, G. J., Bolvin, D. T., Joyce, R., Kelley, O. A., Nelkin, E. J., Tan, J., Watters, D. C., & West, B. J. (2023, July 13). IMERG technical documentation. NASA GPM. `https://gpm.nasa.gov/sites/default/files/2023-07/IMERG_TechnicalDocumentation_final_230713.pdf`, linked from `https://gpm.nasa.gov/resources/documents/imerg-v07-technical-documentation`. PDF opened.

Estoque, R. C., Ooba, M., Seposo, X. T., Togawa, T., Hijioka, Y., Takahashi, K., & Nakamura, S. (2020). Heat health risk assessment in Philippine cities using remotely sensed data and social-ecological indicators. *Nature Communications, 11*(1). `https://doi.org/10.1038/s41467-020-15218-8`. HTML opened. Crossref did not supply a page range.

Rogayan, D. V. (2024). Addressing the escalating heat index in the Philippines: a call to action. *Journal of Public Health, 46*(3), e580–e581. `https://doi.org/10.1093/pubmed/fdae073`. Crossref abstract only; not a Western Luzon analysis.

Antonio, R. P., Quiatchon, J. C. B., & David, R. A. (2026). Should heat index thresholds trigger public health action? Ethical lessons from rising heat exposure in the Philippines. *Journal of Public Health Policy*. `https://doi.org/10.1057/s41271-026-00661-6`. Crossref record has no abstract. Full text not opened.
