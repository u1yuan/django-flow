# Data-feasibility audit

**Search date:** 6 October 2026  
**Role:** statistical analyst. No model was fit. No predictive performance is reported.  
**Question:** For each active provisional direction, can a Philippine undergraduate Data Science study reach at least 10,000 usable records from ethically sourced public data, under a stated observation unit, after missingness and exclusions, with a defensible validation design?

Catalog totals are not treated as eligible complete cases. A failed download is a failed result and is not entered as a count. Potential arithmetic is labeled potential. Counts below are from pages or files opened on this date.

Calculations used Python 3.14.7 and the standard library, plus `pypdf` to read two short PDFs. Category frequencies were checked by adding them back to the file’s case total.

## Gate summary

| # | Direction | Record-count gate |
| --- | --- | --- |
| 1 | Filipino adolescent loneliness and protective factors | **fail** |
| 2 | Creative thinking and digital leisure, PISA 2022 | **not counted** |
| 3 | LGU nighttime-light growth | **not counted** |
| 4 | Night-sky brightness | **fail** |
| 5 | Dark-sky conservation sites | **fail** |
| 6 | Urban heat alerts | **not counted** |
| 7 | Heat alerts across ENSO regimes | **fail** |
| 8 | Population-weighted urban heat | **not counted** |
| 9 | Green access and surface heat | **not counted** |
| 10 | Post-typhoon nighttime lighting | **not counted** |

## Access failures

These requests did not yield a usable table. Cloudflare challenge pages are recorded as HTTP 403. They were not bypassed.

| URL | Result |
| --- | --- |
| https://www.oecd.org/en/data/datasets/pisa-2022-database.html | HTTP 403 |
| https://webfs.oecd.org/pisa2022/ | HTTP 403 |
| https://www.oecd-ilibrary.org/education/pisa-2022-results-volume-i_53f23881-en | HTTP 403 |
| https://doi.org/10.1787/53f23881-en | HTTP 403 |
| https://psa.gov.ph/classification/psgc | HTTP 403 |
| https://openstat.psa.gov.ph/ | HTTP 403 |
| https://bmb.gov.ph/ and https://www.bmb.gov.ph/ | HTTP 403 |
| https://elibrary.bmb.gov.ph/ | HTTP 403 |
| https://www.denr.gov.ph/ | HTTP 403 |
| https://www.ncei.noaa.gov/products/land-based-station/global-summary-of-the-day | HTTP 503 |
| https://eogdata.mines.edu/nighttime_light/monthly/v10/ | TLS failure: unable to get local issuer certificate. Directory not read. |
| https://www.lightpollutionmap.info/ | TLS failure: certificate has expired. Page not read. |
| https://www.globeatnight.org/documents/1190/GaN2025.csv | HTTP 400. Philippine rows for 2025 were not counted. |

The GSOD product page failed. The GSOD readme at https://www.ncei.noaa.gov/data/global-summary-of-the-day/doc/readme.txt opened (file date 28 October 2020).

## 1. Adolescent loneliness and protective factors

**Working direction:** Filipino Adolescent Loneliness Patterns and Protective Factors Using Latent Class Analysis.

**Observation unit:** one school-going respondent in the national file. The catalog unit of analysis is “Individuals.”

**Independent unit:** the file contains `psu`, `stratum`, and `weight`. The study description says stage 1 selects schools with probability proportional to enrollment and stage 2 selects classes. A separate class identifier was not among the variable names inspected. Students who share a PSU are repeated measures on that sampling unit. A defensible split holds out PSUs. This catalog entry is one survey year, so it has no second year to hold out.

**Opened on 6 October 2026:**

- Catalog: https://extranet.who.int/ncdsmicrodata/index.php/catalog/944 (study description, data dictionary, related materials, get-microdata terms). Reference `PHL_2019_GSHS_v01`. Metadata last modified 14 December 2023.
- DDI: https://extranet.who.int/ncdsmicrodata/index.php/metadata/export/944/ddi saved as `_opened/who-ddi.xml`.
- National codebook PDF and 2019 fact sheet PDF, linked from the catalog’s related-materials tab, saved as `_opened/who-codebook-national.pdf` and `_opened/who-factsheet.pdf`.
- Microdata were not downloaded and are not stored.

**What the opened material says about N:**

The national file `PHL2019` has `caseQnty` 10,175 and 104 variables. The fact sheet says: “A total of 10,175 students participated in the Philippines GSHS.” That participant total includes ages outside 13–17. It is not an eligible complete-case count.

Regional files are a partition of the national file, not extra students:

3520 (Luzon) + 3506 (Mindanao) = 7026; 7026 + 3149 (Visayas) = 10,175.

Stacking the national file with any regional file would duplicate respondents.

National age item `q1` (“How old are you?”), DDI category frequencies:

| Code | Label | Frequency |
| --- | --- | ---: |
| 1 | 11 years old or younger | 313 |
| 2 | 12 years old | 1,886 |
| 3 | 13 years old | 2,180 |
| 4 | 14 years old | 2,274 |
| 5 | 15 years old | 2,015 |
| 6 | 16 years old | 954 |
| 7 | 17 years old | 340 |
| 8 | 18 years old or older | 187 |
| Sysmiss | missing | 26 |

Ages 13–17: 2180 + 2274 = 4454; 4454 + 2015 = 6469; 6469 + 954 = 7423; 7423 + 340 = **7,763**.

Check: valid age responses 313 + 1886 + 2180 + 2274 + 2015 + 954 + 340 + 187 = 10,149; 10,149 + 26 missing = 10,175. Ages outside 13–17 among valid answers: 313 + 1886 + 187 = 2,386; 10,149 − 2,386 = 7,763.

**Eligible count:** 7,763 is the unweighted count of national-file respondents in the age categories 13, 14, 15, 16, and 17. Listwise complete cases on loneliness plus protective-factor items inside that age band were **not computed** (that cross-tab needs the microdata). Any such complete-case count cannot exceed 7,763.

All-age univariate valid counts in the national DDI, for description only: `q22` loneliness 10,121 valid (54 invalid); `q27` close friends 10,064; `q55` parents check homework 9,941; `q56` parents understand problems 10,044; `q57` parents know free time 10,015; `q58` parents go through things 10,023. These are not age-restricted and are not a joint N. The smallest of them, 9,941, is already below 10,000 before the age restriction.

**Time span:** data-collection start year 2019. The study description does not give an end date. One cross-section.

**Geographic coverage:** Philippines. The catalog says “National plus Luzon, Mindanao and Visayas.”

**Labels present in the opened DDI:** `q22`, “During the past 12 months, how often have you felt lonely?” Protective-factor items include `q27` close friends and `q55`–`q58` (homework checks, understanding problems, knowing free time, going through things). The fact sheet’s age columns are weighted prevalence displays, not headcounts.

**Usage rights, from the study-description access conditions:** the user undertakes “(4) to use the data for non-commercial, not-for-profit public health purposes only,” to acknowledge the source, to share planned publications with WHO before publication, and to offer co-authorship to the survey coordinator. The get-microdata page adds that the materials “will not be redistributed or sold” without written agreement of the repository.

**Leakage and correlation:** students are clustered in PSUs and classes. Regional files duplicate the national file if combined. Survey weights do not create additional records. A random student split would put classmates on both sides of a split.

**Record-count gate: fail.** The age-eligible upper bound from the opened codebook is 7,763, below 10,000. Joint complete cases were not computed.

**Extract required before model work:** the public-use microdata under the WHO terms, restricted to ages 13–17, with a listwise or explicitly declared missing-data rule for `q22` and the protective-factor items, a count of distinct PSUs, and a PSU-held-out validation plan. Do not stack regional files onto the national file.

## 2. Creative thinking and digital leisure

**Working direction:** Creative Thinking and Digital Leisure Across Southeast Asian PISA Systems Using Multilevel IRT.

**Observation unit:** one student with the creative-thinking outcome and the digital-leisure items the title needs. **Independent unit:** school, then country, if the official design variables are present. Neither was counted.

**Opened:** the OECD PISA 2022 database URL returned HTTP 403 (Cloudflare challenge). The same result occurred for the OECD iLibrary Volume I page, `webfs.oecd.org/pisa2022/`, and `doi.org/10.1787/53f23881-en`. No official sample-size table, creative-thinking country list, or ICT codebook was read.

**Eligible count:** not counted. No Philippine student count is stated here, because no official table was opened. Optional social-media and gaming items for the Philippines were not verified.

**Time span, geography, labels:** not read from an official PISA table on this date.

**Usage rights:** not quoted, because the dataset page did not open.

**Leakage:** not assessable from an unread file. PISA students are clustered in schools; a student-level random split would leak school context. That is a design warning, not a result from opened microdata.

**Record-count gate: not counted.**

**Extract required before model work:** an official PISA 2022 table or student codebook that states the Philippine sample and whether the Philippines has the optional ICT social-media and gaming items; then a count of distinct students with non-missing creative-thinking and those ICT responses. If the items are absent for the Philippines, a Philippine digital-leisure claim is not supported by this file. A multi-country count would have to add country samples from an opened table, with school-level holdout. That sum was not made.

## 3. LGU nighttime lights

**Working direction:** Forecasting Philippine LGU Nighttime-Light Growth Using XGBoost for Dark-Sky Planning.

**Observation unit intended:** one city or municipality in one month. **Independent site unit:** the LGU. Monthly rows for the same LGU are repeated measures.

**Opened:** https://eogdata.mines.edu/products/vnl/ and the license PDF https://eogdata.mines.edu/files/EOG_products_CC_License.pdf. Rasters were not downloaded. The monthly directory https://eogdata.mines.edu/nighttime_light/monthly/v10/ failed TLS verification, so month files were not listed.

The product page describes monthly cloud-free DNB composites and says the version-1 monthly series uses annual masks “for each of the months from 2012–2020.” It also describes annual VNL V2 from monthly averages, with 2012 beginning in April 2012. Resolution on the page is 15 arc seconds. Bands named on the page include `avg_rade9h` and cloud-free coverage `cf_cvg`. The page says a zero in the average-radiance image must not be read as “no lights” without the cloud-free coverage file, and that tropical cloud cover leaves many places without good monthly coverage.

**PSA LGU count:** https://psa.gov.ph/classification/psgc and https://openstat.psa.gov.ph/ returned HTTP 403. No official city or municipality count was opened. **Potential LGU-month arithmetic was not computed.**

**Eligible count:** not counted. No LGU-month radiance file was built. Cloud-free coverage was not measured.

**Time span on the opened product page:** monthly discussion covers 2012–2020; annual V2 is described as a series derived from monthly averages beginning in 2012. A complete month index was not read.

**Geographic coverage:** the page states global grids from 180W, 75N to 180E, 65S. Philippine coverage was not extracted from a raster.

**Labels:** radiance in nW/cm²/sr and coverage counts. These are lighting measurements, not sky-brightness or a development outcome.

**Usage rights, from the license PDF opened with the product page:** “The Earth Observation Group (EOG), Payne Institute for Public Policy, Colorado School of Mines, makes many of their datasets publicly available under the Creative Commons Attribution 4.0 International license (CC-BY 4.0). These include the DMSP nighttime lights, VIIRS nighttime lights (VNL).” Users “are allowed to copy, modify, and distribute data in any format for any purpose, including commercial use,” with credit and a note of changes.

**Leakage:** months within an LGU are serially dependent. A random row split leaks the place’s level into both sides. Adjacent LGUs share light and weather. Cloud-free coverage is a missingness field, not a zero.

**Record-count gate: not counted.**

**Extract required before model work:** an official PSA or equivalent list of cities and municipalities; a spatial join to monthly VIIRS radiance and `cf_cvg`; an explicit rule for months with poor cloud-free coverage; then a count of LGU-months left after that rule. Validation has to hold out whole LGUs or whole years. The forecast target on this product is radiance, not visual sky brightness.

## 4. Night-sky brightness

**Working direction:** Estimating Philippine Night-Sky Brightness Using XGBoost and Satellite–Ground Observations.

**Observation unit:** one Globe at Night data row. **Independent site proxy:** one distinct latitude-longitude pair in those rows. Pairs are not a cleaned site registry; a single place can appear as more than one coordinate.

**Opened:**

- https://www.globeatnight.org/ (homepage states 330,453 total observations and 10,113 observations in 2026). Those figures are global. They are not Philippine counts.
- https://www.globeatnight.org/maps-data/ and the yearly CSV links on that page.
- https://www.globeatnight.org/gan-mn/ and http://globeatnight-network.org/. Neither page contained the string “Philippines.” The GaN-MN page describes SQM-LE meters and gives Salt Lake City and Dead Horse Point, Utah, as examples.
- https://www.lightpollutionmap.info/ did not open (expired TLS certificate).

**Philippine rows counted from the opened CSVs** (`Country` equal to Philippines, PH, PHL, or Republic of the Philippines after trimming):

| Year | Philippine rows | File result |
| --- | ---: | --- |
| 2006 | 0 | opened |
| 2007 | 2 | opened |
| 2008 | 7 | opened |
| 2009 | 1 | opened |
| 2010 | 8 | opened |
| 2011 | 13 | opened |
| 2012 | 7 | opened |
| 2013 | 7 | opened |
| 2014 | 6 | opened |
| 2015 | 7 | opened |
| 2016 | 8 | opened |
| 2017 | 4 | opened |
| 2018 | 0 | opened |
| 2019 | 0 | opened |
| 2020 | 198 | opened |
| 2021 | 37 | opened |
| 2022 | 10 | opened |
| 2023 | 4 | opened |
| 2024 | 4 | opened |
| 2025 | not counted | HTTP 400 on `GaN2025.csv` |

Sum for opened years 2006–2024: years 2006–2019 contribute 70 rows (2+7+1+8+13+7+7+6+7+8+4); years 2020–2024 contribute 198+37+10+4+4 = 253; 70 + 253 = **323** Philippine rows. Distinct latitude-longitude pairs among those 323 rows: **92**. The page’s 2025 global total of 13,421 observations was not used as a Philippine count.

Quality filters (cloud, moonlight, limiting-magnitude completeness) were not applied. Eligible rows after those exclusions were not computed and cannot exceed 323 in the opened years.

**Time span counted:** 2006–2024 CSV releases. The page says collection started in 2006. 2025 was not read. 2026 is described on the maps page as a campaign still in progress; its Philippine rows were not in the CSV set that was counted.

**Geographic coverage:** rows whose country field is the Philippines. Global totals were not treated as Philippine coverage.

**Labels:** citizen-science night-sky submissions in the Globe at Night files. The opened GaN-MN pages did not provide a Philippine SQM site inventory or a Philippine SQM reading count.

**Usage rights, from the maps-data page:** “Globe at Night data is made available under a Creative Commons Attribution 4.0 International License.”

**Leakage:** repeated rows at the same coordinates are one place, not independent skies. A random row split leaks the site. Satellite pixels matched to these points would share calibration if the same nights are on both sides of a split. Hold out sites, not rows.

**Record-count gate: fail.** Opened Philippine observations are 323 and distinct coordinate pairs are 92. The 2025 file was a failed download, not a count.

**Extract required before model work:** a Philippine SQM or other instrument series with site identifiers, timestamps, cloud conditions, and a held-out site set large enough for the claim. Globe at Night’s opened Philippine rows do not supply 10,000 ground records.

## 5. Dark-sky conservation sites

**Working direction:** Prioritizing Philippine Dark-Sky Conservation Sites Using NSGA-II and Nighttime-Light Trends.

**Observation unit on the opened WDPA page:** one protected-area designation. **Independent place:** a geographic location. The page says the same location can be counted more than once when it has more than one designation.

**Opened:**

- https://www.protectedplanet.net/country/PHL on 6 October 2026. The page citation line reads: “UNEP-WCMC (2026). Protected Area Profile for Philippines from the World Database on Protected Areas, October 2026.”
- https://www.protectedplanet.net/en/legal for WDPA terms.
- NIPAS/BMB boundary pages did not open: `bmb.gov.ph`, `www.bmb.gov.ph`, `elibrary.bmb.gov.ph`, and `www.denr.gov.ph` returned HTTP 403. Polygons were not downloaded.

**Counts printed on the Philippines WDPA profile:** 274 total protected areas; “Number of national designations only = 249”; 18 with management effectiveness evaluations. The page also prints 178 other effective area-based conservation measures, of which “Number of national designations only = 5.” These are catalog designation counts. They are not eligible sites after a boundary, expert, or sky-brightness filter. Eligible-N after those exclusions was **not computed**. Exclusions cannot raise 274 or 249 to 10,000.

Polygons/points ratio on the page: polygons 68%, points 32%. That is a composition statement, not a downloaded geometry count.

**Time span:** the profile is the October 2026 WDPA release named on the page. Trend years were not computed.

**Geographic coverage:** Philippines profile on Protected Planet. This is not a confirmed NIPAS boundary extract.

**Labels:** designation counts and a management-effectiveness count. No sky-brightness outcome is on this page.

**Usage rights, from the legal page:** “Neither (a) the WDPCA Materials and the GD-PAME Materials nor (b) any work derived from or based upon the WDPCA Materials and the GD-PAME Materials (‘Derivative Works’) may be put to Commercial Use without the prior written permission of UNEP-WCMC.” Commercial use includes use by a for-profit entity or revenue generation. Redistribution of the data, including through downloads and web services, requires permission. Publication is allowed when the data are not downloadable and attribution is visible.

**Leakage:** overlapping designations of one place are not independent sites. Nighttime-light months attached later to the same polygon would be repeated measures. Pixels inside a polygon are not independent sites.

**Record-count gate: fail.** The opened designation totals are 274 and 249 national designations.

**Extract required before model work:** an official NIPAS or BMB boundary source with its download terms actually opened; a rule for overlapping designations; field or instrument labels for sky quality; and a site-level table. A pixel or month expansion was not counted and would not turn designations into independent sites.

## 6. Urban heat alerts

**Working direction:** Evaluating Urban Heat Alert Reliability Across Philippine Cities Using Conformalized XGBoost.

**Observation unit intended:** one station-hour with temperature and humidity or dew point, from which a heat index can be formed. **Independent site unit:** the station. Hours at the same station are repeated measures. Nearby stations are spatially correlated.

**Opened:**

- ISD product page: https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database
- Access Data Service API documentation: https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation
- Country list: https://www.ncei.noaa.gov/pub/data/noaa/country-list.txt (`RP` = PHILIPPINES)
- ISD history: https://www.ncei.noaa.gov/pub/data/noaa/isd-history.csv (29,661 data rows scanned). Philippine rows saved as `noaa-isd-history-philippines.csv`. The global file was not kept.
- GSOD readme: https://www.ncei.noaa.gov/data/global-summary-of-the-day/doc/readme.txt (28 October 2020). The GSOD product HTML page returned HTTP 503.

**Station inventory, not station-hours:** 116 history rows have `CTRY` = `RP`, and 116 distinct USAF–WBAN pairs. All 116 have latitude and longitude. Coordinate range in those rows: latitude 5.047 to 20.8, longitude 115.82 to 126.333. `BEGIN` runs from 19440914 to 20221006. `END` runs from 19450809 to 20250824. Rows with `END` on or after 20240101: 52. Rows with `END` on or after 20250101: 51. These end stamps are not proof of continuous reporting, and they do not show which stations observed temperature and dew point.

The history file’s latest Philippine `END` is 24 August 2025, earlier than this 6 October 2026 download. The file does not document hours through the search date.

The ISD page says the database includes temperature and dew point “as observed by each station.” Global figures on that page (more than 20,000 stations in the hourly product, over 35,000 in the database, more than 14,000 active) are not Philippine counts. The GSOD readme defines `TEMP` and `DEWP` among daily elements and says a daily summary needs at least four observations that day. It does not list Philippine stations.

**Eligible station-hours:** not counted. No hourly or daily climate archive was downloaded. Ten thousand station-hours is not claimed.

**Labels in the opened docs:** temperature and dew point exist as ISD/GSOD elements when a station reports them. A heat-index threshold label was not in the files. It would have to be calculated later from temperature and humidity or dew point.

**Usage rights, from the GSOD readme:** summaries “are intended for free and unrestricted use in research, education, and other non-commercial activities.” For non-U.S. locations, “the data or any derived product shall not be provided to other users or be used for the re-export of commercial services.” The readme ties this to WMO Resolution 40.

**Leakage:** hours within a station, and stations in the same weather regime, are correlated. A random hour split leaks persistence into the test set. A 24-hour-ahead alert has to use only fields available at forecast time. Same-hour persistence and seasonal climatology are baselines, not results of this audit.

**Record-count gate: not counted.**

**Extract required before model work:** an hourly ISD or daily GSOD extract for the Philippine station IDs, restricted to hours or days with both temperature and humidity or dew point after the published quality flags; a count of those records; and a split that holds out years and stations. The 116-row history file is the station list, not that extract.

## 7. Heat alerts across ENSO regimes

**Working direction:** Evaluating Philippine Urban Heat Alert Reliability Across ENSO Regimes Using Conformalized XGBoost.

**Observation unit for the index:** one overlapping 3-month RONI season. **Independent event unit:** one warm episode that reaches the very-strong bin, after the seasonal series has fallen below +0.5°C. Overlapping seasons share two months with the next season, so season-rows are not independent events. Station-hours that would be stratified by these episodes were **not counted** (see direction 6).

**Opened:**

- Strengths archive, issued June 2026: https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/archives/?month=06&type=strengths&year=2026. This page is an outlook probability table for upcoming seasons. It is not a historical episode list. It defines bins in 0.5°C steps and includes the column “Index ≥ 2.0°C.” It says probabilities “are verified using the Relative Oceanic Niño Index (RONI).”
- Historical table: https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/ (ERSSTv6, 1991–2020 base period). Parsed seasons saved as `_opened/roni-seasons-parsed.csv`.

**Revision language, from the historical page:** “RONI values may change up to two months after the initial ‘real time’ value is posted. Therefore, the most recent RONI values should be considered an estimate.” The reason given on the page is the high-frequency filter applied to ERSSTv6.

**Table actually parsed:** 1950 DJF through 2025 NDJ is 76 × 12 = 912 season values. The 2026 row has eight seasons, DJF through JAS. 912 + 8 = **920** season values. The page header says data availability 1950–2026. The 2026 JAS value is 1.7°C. No 2026 season is ≥ +2.0°C.

**Seasons ≥ +2.0°C in the opened table (19 overlapping seasons):**

| Episode | Seasons ≥ +2.0°C | Peak |
| --- | --- | ---: |
| 1965–66 | 1965 OND 2.0 | 2.0 |
| 1972–73 | 1972 OND 2.0 | 2.0 |
| 1982–83 | 1982 SON 2.0, OND 2.2, NDJ 2.4; 1983 DJF 2.4, JFM 2.2 | 2.4 |
| 1991–92 | 1991 NDJ 2.0; 1992 DJF 2.1, JFM 2.1 | 2.1 |
| 1997–98 | 1997 ASO 2.1, SON 2.2, OND 2.3, NDJ 2.3; 1998 DJF 2.1 | 2.3 |
| 2015–16 | 2015 SON 2.0, OND 2.2, NDJ 2.3; 2016 DJF 2.1 | 2.3 |

**Independent episodes: 6.** A new episode was started only after the ordered series had fallen below +0.5°C. The 2023–24 peak in this table is 1.4°C (2023 OND and NDJ). That peak is not in the ≥ +2.0°C list.

**Eligible count:** 920 season values and 6 very-strong episodes. Both are below 10,000. Philippine station-hours inside those episodes were not counted.

**Time span:** 1950 DJF–2026 JAS in the saved table. **Geography:** the page defines Niño-3.4 as 5°N–5°S, 120°–170°W, relative to a tropical-mean SST. This is not a Philippine station series.

**Labels:** RONI in °C. The page colors warm and cold episodes when ±0.5°C lasts at least five consecutive overlapping seasons. The very-strong cut used here is the strengths page’s “Index ≥ 2.0°C.”

**Usage rights:** the pages are NOAA CPC public web products. No separate license paragraph was printed on the two opened HTML pages beyond standard NOAA footer links (disclaimer, information quality, privacy).

**Leakage:** overlapping seasons double-count months. The newest seasons can still change for up to two months, so using them as if they were final leaks a revision that was not available at first posting. Joining the latest revised RONI to a past forecast, as if the revised value had been known at issue time, would use future information. Holding out one episode leaves five others; six episodes are a small event sample.

**Record-count gate: fail.**

**Extract required before model work:** the station-hour extract from direction 6, labeled with the season’s RONI from a dated vintage if the study claims issue-time information; otherwise a retrospective label with the revision window stated. Event-level uncertainty has to be reported at the episode, not at the overlapping season. This index alone cannot supply 10,000 records.

## 8. Population-weighted urban heat

**Working direction:** Estimating Population-Weighted Urban Heat Exposure Across Philippine Cities Using Spatial Random Forests.

**Observation unit that would be required:** one population cell paired with a temperature field, then checked against a ground air-temperature station. **Independent unit:** a ground station or a held-out city. Neither join was made.

**Opened, documentation only:**

- Population grid: https://developers.google.com/earth-engine/datasets/catalog/JRC_GHSL_P2023A_GHS_POP. Band `population_count`, pixel size 100 m, availability field 1975-01-01 through 2030-12-31. Epochs through 2030 are part of the catalog span; they were not sampled, and future epochs are not observations.
- Reanalysis: https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_HOURLY. `temperature_2m` is “Temperature of air at 2m above the surface of land, sea or in-land waters,” “calculated by interpolating between the lowest model level and the Earth’s surface.” Pixel size on the page: 11,132 m. Availability field 1950-01-01T01:00:00Z through 2026-09-29T21:00:00Z. `skin_temperature` is a separate surface-energy variable, not 2 m air temperature.
- Satellite surface temperature: https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD11A1, Terra land surface temperature and emissivity, daily, about 1 km, availability field 2000-02-24 through 2026-09-30. Day and night bands are surface temperature under clear-sky rules. Above 30° latitude the page says some pixels average multiple clear-sky observations. The Philippines sits below 30°N; that sentence is not a Philippine clear-sky count.

Earth Engine was not initialized. No population or temperature pixels were sampled. **Eligible grid-cell count: not counted.**

**Why this cannot validate barangay air temperature without ground stations:** GHSL is a population grid, not a thermometer. ERA5-Land `temperature_2m` is a reanalysis value on an 11,132 m grid, produced by interpolating a model level to 2 m. MODIS MOD11A1 is satellite land-surface (skin) temperature at about 1 km under clear-sky compositing rules, not screen-level air temperature in a barangay. Population weighting changes the spatial average. It does not create an air-temperature observation. No ground stations were paired with these grids in this audit, so there is no barangay air-temperature residual to compute.

**Usage rights, quoted from the opened catalog pages:**

- GHSL: “The GHSL has been produced by the European Commission Joint Research Centre as open and free data. Reuse is authorised, provided the source is acknowledged.”
- ERA5-Land: the page points to Copernicus C3S/CAMS License agreement section 5.1.1, which requires recipients to be told the source, with the notice beginning “Generated using Copernicus Climate Change Service information.”
- MODIS: “MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.”

**Leakage:** neighboring 100 m population cells inside one 11 km reanalysis cell share one temperature value. Treating those cells as independent weather observations overstates the sample. A spatial random split that scatters adjacent cells into train and test leaks the same weather into both.

**Record-count gate: not counted.**

**Extract required before model work:** a stated grid and epoch, a count after any water or built-up mask, and a held-out set of ground stations with air temperature. Without those stations the product can be described as a population-weighted reanalysis or surface-temperature field. It cannot be reported as validated barangay air temperature.

## 9. Green access and surface heat

**Working direction:** Mapping Philippine Urban Green Access and Surface Heat Using Random Forest and Network Analysis.

**Observation unit intended:** one cloud-filtered grid cell at one time, plus a separately mapped park or entrance if the claim is access rather than vegetation. **Independent unit:** a neighborhood or city held out whole. Pixels inside one park are not independent places.

**Opened:**

- https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED
- https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_L2
- https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC09_C02_T1_L2

Earth Engine was not initialized. **No pixels were sampled. Cloud-free coverage was not counted.**

**Sentinel-2:** the Harmonized MSI Level-2A page says the assets contain “12 UINT16 spectral bands representing SR scaled by 10000 (unlike in L1 data, there is no B10).” The band table opened on that page lists B1 through B9, B8A, B11, and B12, plus AOT, WVP, SCL, QA60, and mask bands. B12 is described at 2202.4 nm (S2A) / 2185.7 nm (S2B), shortwave infrared. There is no surface-temperature band and no thermal-infrared wavelength in that table. Availability field: 2017-03-28 through 2026-10-05. Revisit interval on the page: 5 days.

**Landsat Collection 2 Level-2:** both LC08 and LC09 pages include `ST_B10`, “Band 10 surface temperature,” units K, wavelength 10.60–11.19 μm, scale 0.00341802, offset 149, 30 m. The LC09 description says the images contain “one thermal infrared (TIR) band processed to orthorectified surface temperature.” LC08 availability field: 2013-03-18 through 2026-09-27. LC09 availability field: 2021-10-31 through 2026-10-03. A sentence on the LC09 page also says “October 2021 through October 2025”; the availability field is the later date range printed on the same page. If `PROCESSING_LEVEL` is `L2SR`, the page says `ST_B10` is fully masked out.

**Labels:** Sentinel-2 can supply reflectance for a vegetation index. It does not supply the thermal outcome. Landsat `ST_B10` is land surface temperature, not pedestrian air temperature or a health outcome. Park entrances and walkable routes were not in these catalog pages.

**Usage rights, from the opened pages:**

- Sentinel-2: “Usage of this Sentinel data is subject to the Copernicus Sentinel Data Terms and Conditions.” The legal-notice PDF linked from the page was not opened.
- Landsat: “Landsat datasets are federally created data and therefore reside in the public domain and may be used, transferred, or reproduced without copyright restriction,” with USGS acknowledgement.

**Leakage:** adjacent pixels and repeat visits of the same block are correlated. A random pixel split leaks the neighborhood. Surface temperature from Landsat cannot be trained against Sentinel-2 as if Sentinel-2 measured heat.

**Record-count gate: not counted.**

**Extract required before model work:** a defined city set and grid; a cloud filter with the fraction removed; a count of remaining cell-times; Landsat `ST_B10` where the processing level actually contains surface temperature; and an independent park or entrance layer for any access ranking. Sentinel-2 reflectance can be the vegetation feature. It cannot be the thermal band.

## 10. Post-typhoon nighttime lighting

**Working direction:** Assessing Post-Typhoon Nighttime Lighting Recovery Using VIIRS and Change-Point Detection.

**Observation unit intended:** one nighttime-light pixel at one month, inside a dated impact area, with a pre-event baseline. **Independent event unit:** the typhoon. Months and neighboring pixels are repeated measures.

**Opened:** the EOG VNL product page in direction 3, and the Earth Engine monthly collection page https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMSLCFG. That catalog entry is `NOAA/VIIRS/DNB/MONTHLY_V1/VCMSLCFG`, cadence 1 month, availability field 2014-01-01 through 2026-08-01, pixel size 463.83 m, bands including `avg_rad` and `cf_cvg`. The page repeats the tropical cloud-cover warning. Earth Engine was not initialized. The EOG monthly directory itself did not open (TLS failure in direction 3).

**Pixel-time counts were not computed. Typhoon impact polygons were not opened and were not joined to the lights.** No control areas, seasonal baselines, or restoration records were counted.

**Labels on the opened pages:** monthly average nighttime radiance and cloud-free coverage. The product is a lighting measurement. It is not a label for GDP, infrastructure repair, or household recovery.

**Usage rights:** the Earth Engine page says “Colorado School of Mines data, information, and products, regardless of the method of delivery, are not subject to copyright and carry no restrictions on their subsequent use by the public.” The EOG license PDF opened for direction 3 places VIIRS nighttime lights under CC-BY 4.0, including commercial use with attribution. Both statements are on pages opened today. They are not the same sentence. A later extract needs to follow the terms of the copy actually downloaded.

**Leakage:** pixels in the same storm footprint move together. A random pixel split leaks the event. Holding out whole typhoons is the split that matches the independent unit. Cloud-covered months are missing, not true dark.

**Record-count gate: not counted.**

**Extract required before model work:** dated impact polygons for more than one typhoon, a pre-event month baseline, `cf_cvg` thresholds, a count of pixel-months left after that filter across the held-out events, and any external restoration series kept separate from the radiance outcome. If restoration records are absent, the outcome that can be stated is lighting change.

## Saved extracts

| Path | What it is |
| --- | --- |
| `docs/activities/litReview/four-field-titles/2026-10-06/data-feasibility.md` | this audit |
| `docs/activities/litReview/four-field-titles/2026-10-06/noaa-isd-history-philippines.csv` | 116 ISD history rows with country code RP |
| `docs/activities/litReview/four-field-titles/2026-10-06/noaa-isd-history-philippines-summary.json` | scan count 29,661 and the RP filter |
| `docs/activities/litReview/four-field-titles/2026-10-06/globeatnight-philippines-rows.csv` | 323 Philippine Globe at Night rows, 2006–2024 |
| `docs/activities/litReview/four-field-titles/2026-10-06/globeatnight-philippines-summary.json` | per-year row counts and the 2025 HTTP 400 |
| `docs/activities/litReview/four-field-titles/2026-10-06/_opened/roni-seasons-parsed.csv` | 920 RONI season values parsed from the saved CPC HTML |
| `docs/activities/litReview/four-field-titles/2026-10-06/_opened/roni-very-strong-summary.json` | 19 seasons ≥ +2.0°C and 6 episodes |
| `docs/activities/litReview/four-field-titles/2026-10-06/_opened/who-ddi.xml` | GSHS 2019 variable metadata, not respondent microdata |
| `docs/activities/litReview/four-field-titles/2026-10-06/_opened/who-codebook-national.pdf` | national codebook PDF |
| `docs/activities/litReview/four-field-titles/2026-10-06/_opened/who-factsheet.pdf` | 2019 fact sheet |

Raw HTML of pages that opened is under `_opened/` with `fetch-log.json` and `fetch-log-round2.json`. The global ISD history file was deleted after the Philippine subset was saved.

## Limitations

- Eligible complete cases were not computed for any direction that would require microdata, rasters, or a climate archive.
- PISA sample size and Philippine ICT item coverage were not read.
- No official LGU count was opened, so no LGU-month potential was calculated.
- Globe at Night 2025 was a failed download. SQM network pages that opened did not give a Philippine site count.
- NIPAS boundary-download terms were not opened. The dark-sky gate uses the WDPA country profile that did open.
- NOAA station-hours with paired temperature and dew point were not counted. The history file does not flag those elements.
- The June 2026 RONI strengths page is an outlook, not the historical episode list. Very-strong seasons come from the historical RONI table. The most recent RONI values are estimates for up to two months.
- Population grids, ERA5-Land, MODIS, Sentinel-2, and Landsat were read as catalog pages only. No pixel sample and no Earth Engine session.
- Typhoon polygons were not joined to monthly lights.
- GSHS microdata, WDPA polygons, VIIRS rasters, Planet imagery, and PAGASA restricted data were not downloaded.
