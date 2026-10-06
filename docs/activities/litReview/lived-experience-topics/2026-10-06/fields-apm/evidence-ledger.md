# Evidence ledger: astronomy, psychology, meteorology

Checked: 6 October 2026. Companion to `../evidence-ledger.md`. Same rules. Stopped titles from `four-field-titles/2026-10-06/opportunity-map.md` are not re-counted here.

## A02. Satellite catalog

Web search returned the body of `https://celestrak.com/satcat` dated "Current as of 2026 Mar 27 18:24:30 UTC." That page's table lists All Objects total 33,054, of which the active-satellite total is 15,265. A different page, `https://celestrak.org/norad/elements/table-geo.php`, returned in the same search and dated 2026 Oct 05, says the official catalog number counter had reached 100953. A catalog number is not a count of objects. The 6 October 2026 object count was not opened. The March page is still a count of objects above 10,000 on the date it prints.

`https://celestrak.org/NORAD/elements/` returned "Last updated: 2026 Oct 06" and a group named "100 (or so) Brightest." That group was not downloaded, so "100" is the page's label, not a row count.

The usage-policy page returned in search describes update intervals (GP data about every 2 hours) and asks users not to re-download large sets. A license that would let a thesis republish the elements was not in the returned text.

No pass was propagated. No sighting log was opened. Satellite-city-nights were not counted. 33,054 objects is not 33,054 passes over a city.

## A01. Clouded observing nights

No public bulk hourly cloud or rainfall archive for Philippine stations was opened.

`https://bagong.pagasa.dost.gov.ph/automated-rain-gauge` returned in search as a latest-hour table, including a Science Garden row time-stamped 6 October 2026. A latest snapshot is not a history.

`https://pagasa.dost.gov.ph/climate/climate-data` describes climatological normals as PDFs and raw Excel by request. No hourly file count was opened.

The opened ClimGridPh abstract (below) is daily rainfall, not night-time cloud.

## M01. Next-day rain

Opened PDF text of DOST-PAGASA (2024), *Combined in situ and satellite-based daily rainfall data of the Philippines in high-resolution grids*, ISBN 978-621-8434-01-1 (PDF), from `https://climgridph.pagasa.dost.gov.ph/climapv2/files/ClimGridPh%20Technical%20Report.pdf`.

The abstract states:

- The product is ClimGridPh-RR, daily gridded rainfall.
- Resolution 0.01°, about 1 km.
- Built from 52 PAGASA synoptic stations merged with GPM/IMERG.
- Period 2001–2020.
- The dataset "has been made available online."

A search extract of the same PDF also described 20 yearly NetCDF files and 55 stations. This ledger uses the abstract's 52, which was read in the saved text. The 55-station sentence was not re-found in the portion read. The NetCDF file count is a search extract, not a number used as a record count.

Cell count was not opened. Calendar arithmetic, not a file count: 2001 through 2020 inclusive is 20 years and 5 leap days (2004, 2008, 2012, 2016, 2020), so 7,305 days. One grid cell at one campus is under 10,000 daily records. The study reaches 10,000 records only if enough cells are used that cell-days exceed 10,000. That product was not downloaded, so that inequality was not checked.

The CliMap page returned in search says the platform was built for daily and sub-daily grids and that the datasets currently include rainfall and temperature at daily timescale. Next-hour rain is not what the opened abstract describes.

The abstract already compares the grid with other products and with 15 independent stations. A thesis that only rebuilds the grid repeats that report. A thesis that forecasts next-day rain for school sites is a different question, and it still needs a counted cell-day file.

## M02. Forecasts as issued

No archive of PAGASA forecasts at issue time was opened. The earlier heat-alert screen's note that iHeatMap and iRISE-UP issue-time archives were not opened is a prior ledger statement, not a new download. `pagasa-pp-cli`'s README, returned in search, says the public forecast pages serve the latest forecast, and that a history exists only if someone stores snapshots. No such store was opened.

## P01. Adult life satisfaction

| Page | Figure | Unit |
| --- | --- | --- |
| IHSN catalog `https://catalog.ihsn.org/catalog/12297/data-dictionary`, text returned by web search | Data file `WVS_Wave_7_Philippines_Stata_v5.0`: 1,200 cases, 434 variables | Philippine respondents, Wave 7, 2019 |
| WVS documentation page returned in the same search | Wave 7 "comprises 64 surveys" and "more than 80,000 respondents" | The page's words. The global file was not downloaded, so 80,000 was not counted. |
| WVS conditions of use, returned in search | Non-profit use, citation required, data files not redistributed, free registration | A use condition, not a record count |
| Fieldwork page | Minimum national sample 1,200, ages 18 and older | Explains why the Philippine file is 1,200. Not a second count. |

Philippine-only analysis fails the 10,000-record rule on the opened case count. A multi-country file might pass if the documentation sentence is accurate, and that file was not opened.

## P05. Taglish sentiment

Same FiReCS card as the other ledger: 10,487 rows stated, split table sums to 10,487, CC-BY-4.0, three human polarity classes, DOI on the card `10.1007/978-981-99-8349-0_11`. The Springer chapter was not opened. The card calls FiReCS a sentiment corpus and describes annotation. It does not describe a test of whether an English model has higher error on Taglish than on English.

The card's update line points to SentiTaglish: Products and Services. A search return for that dataset said 10,510 reviews and four classes. That second card was not fetched directly, so 10,510 is not used.

TagaSenti's card text, returned in search, said 35,686 sentences and said some rows are LLM-labeled or translated. Those rows are a limitation, not a count this pass relies on.

## Benchmark the group named

Opened PDF text, 6 October 2026: STATYX, "Threshold of Urban Biodiversity Collapse: Forecasting Ecological Tipping Points Under Artificial Light at Night and Other Environmental Covariates Using Avian Indicators," The Curiosity Cup 2026, a SAS student-competition manuscript. URL: `https://dam-cdn.sas.orangelogic.com/AssetLink/yl732j015sk7gu383ooy025j4heml5r7/team-statyx-curiosity-cup-winner-2026.pdf.pdf`. This is not a journal article. No figure or table image was remeasured.

The PDF states, and this ledger does not adopt these as our results:

- Philippine eBird logs, reached through GBIF, initially 1,355,677 records and 53 fields, then restricted to a Metro Manila bounding box.
- Covariates from Google Earth Engine: VIIRS monthly nighttime radiance, MODIS vegetation, MODIS land surface temperature, CHIRPS precipitation. Years stated as 2014 to 2024.
- Aggregation to 500 m cells by month, stated as 646,800 rows, split 388,080 / 194,040 / 64,680.
- Models: LightGBM and a multilayer perceptron. The PDF reports LightGBM test R² of 93.53% and a richness decline in light-sensitive birds beginning near 51.96 nW/cm²/sr.
- The PDF's own generalization section says opportunistic sightings carry observer bias, and it names bats, insects, acoustic monitoring, and places beyond Metro Manila as further work.

Those performance numbers and the threshold are the competition manuscript's claims. They are not a result of this screen.

GBIF occurrence count API, direct fetch of `https://api.gbif.org/v1/occurrence/count?country=PH` on 6 October 2026, returned `3901246`. That is a count of indexed occurrence records for the country. It is not a count of 500 m cell-months, not a bird-only count, and not a file this screen downloaded.

## Not reopened

Globe at Night Philippine rows, protected-area catalogs, GSHS ages 13–17, and El Niño-season heat alerts stay on the 6 October opportunity map. They are not given new counts here.
