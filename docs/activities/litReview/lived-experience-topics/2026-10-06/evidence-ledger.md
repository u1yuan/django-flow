# Evidence ledger: lived-experience check round

Checked: 6 October 2026. This ledger covers the ten ideas in `scorecard.md` plus the trade replacement named after T01 and T02 failed the opened period. Counts below are either a figure printed on an opened page, a line count from a downloaded public file, or arithmetic from those figures. Arithmetic is labeled. A file size is not a record count.

OpenAlex CLI was started for five queries and stopped after several minutes with an empty `l01.json`. No OpenAlex work is cited. An arXiv CLI batch was started the same day and is recorded in `qa-review.md` if it returned. Papers below were opened as the files named here, not through that CLI.

## L01. PhilGEPS awards

| Item | What was opened | What it supports | What it does not support |
| --- | --- | --- | --- |
| BetterGov mirror | Direct fetch of `https://data.bettergov.ph/datasets/5` | Title "Open PhilGEPS Data." License line: CC0 1.0 Universal. Total size 500.37 MB. Last updated Nov 13, 2025. Attribution points at `https://philgeps.gov.ph/CmsHomePages/open-data`. The page says the content is public domain unless noted, and that users should verify it. | The resource table did not load (extracted text said Resources: 0). No row count. The 500.37 MB figure is a size, not a number of awards. |
| Search snippet of the same URL | Web search result, not a second successful table load | Listed a parquet "PhilGEPS Complete Dataset" at 492.93 MB, plus smaller files for awardees and organizations. | The parquet was not downloaded. The snippet and the direct fetch do not agree on whether the file list was visible. Neither is a row count. |
| Open Contracting comparison | Direct fetch of `https://open-contracting.github.io/opendatacomparison/datasets/p/philgeps-award-notices/` | The page says that as of February 28, 2014 there were 183,619 award notices, and that the public site displayed only the 100 most recent unless the user registered. | This is a 2014 statement on a comparison site. It is not a 2026 count and not a count of the BetterGov file. |
| PhilGEPS notices UI | Search result for the recent-awards page | The live UI shows recent awards with amounts and supplier context in the page text. | A page of recent rows is not a population count. |

Gate: row count not opened. The 2014 figure is above 10,000 but is twelve years old. A flag on an award is not a finding of corruption.

## C02. GTFS

Downloaded from `https://github.com/sakayph/gtfs` raw files on master, 6 October 2026. Line counts are non-blank lines from `Measure-Object -Line`, then the files were deleted. They were not committed.

| File | Lines | Bytes on disk |
| --- | ---: | ---: |
| stop_times.txt | 79,415 | 4,014,151 |
| stops.txt | 4,859 | 406,553 |
| trips.txt | 1,865 | 65,631 |
| routes.txt | 1,718 | 279,480 |

If each file has one header row and no other non-data lines, data rows are 79,414 stop-times, 4,858 stops, 1,864 trips, and 1,717 routes. That header assumption was not checked by reading the first line into this ledger. Routes, trips, and stops are under 10,000. Stop-times are over 10,000 only under the header assumption.

`LICENSE.md` on the same repository is a DOTC developer license. It grants a limited, revocable license to use the data to assist mass-transportation riders or to promote public transportation. It says DOTC owns the data, and it forbids selling the data apart from an application. It is not a Creative Commons license. The README says the feed was released for a concluded transit-app challenge and was modified for Sakay. Transitland's page for this feed, returned in search, shows service dates in 2013–2014 on an older fetch. This pass did not re-open a modernization-era "after" feed.

A stop-time row is one scheduled stop on one trip. It is not a barangay that lost service, and it is not a before-and-after of jeepney modernization.

## O01. Reviews, revised

The fake-review version has no opened fraud labels.

| Source | Opened how | Stated size | Labels | License and limit |
| --- | --- | --- | --- | --- |
| `https://huggingface.co/datasets/scaredmeow/shopee-reviews-tl-stars` | Direct fetch | Card says 2,100 training and 450 validation and 450 test samples for each of 5 stars, and states 10,500 training and 2,250 validation and 2,250 test. Arithmetic from those stated pieces: 10,500 + 2,250 + 2,250 = 15,000. The file was not row-counted. | Stars 1–5, not fake or genuine | The SEACrowd card for the same corpus, fetched directly, says Mozilla Public License 2.0. Viewer examples are Tagalog or Taglish product reviews. |
| `https://huggingface.co/datasets/ccosme/FiReCS` | Direct fetch | Page says "Number of rows: 10,487." Split table: train 2,410 / 2,549 / 2,381 = 7,340; test 1,033 / 1,087 / 1,027 = 3,147; 7,340 + 3,147 = 10,487. | Negative, neutral, positive | CC-BY-4.0. Card says no personal information was stored. Text came from Google Maps and Shopee Philippines reviews. Card cites Cosme and De Leon (2024), DOI `10.1007/978-981-99-8349-0_11`. That paper's PDF was not opened. |
| `https://huggingface.co/datasets/letijo03/sentiment-analysis-taglish-shopee-comment` | Page text saved from search | "Number of rows: 50,290." "No dataset card yet." | Not read | No license was on the opened portion. Not used as a primary source. |
| Shopee seller data-protection page | Search result `https://seller.shopee.ph/edu/article/26985` | None | None | The returned text forbids bots, crawlers, and automated collection. That is a terms lead, not a reading of the full legal agreement. |

FiReCS is the corpus used in the concept brief. Scraping Shopee again is not part of the proposal.

## S01. Class suspensions

PDF text opened: HabagatPlus, Salvilla and Fabregas, ICAIIC-style manuscript at `https://www.manuscriptlink.com/society/kics/media?key=kics%2Fconference%2Ficaiic2024%2F1570978277.pdf`.

The PDF states a Naive Bayes recommender using rainfall, wind, and temperature, coverage 1 January 2012 through 31 December 2021, and 17 of 116 PAGASA stations. Table II states total records of 87,011 preschool, 48,584 elementary, 64,205 high school, and 65,054 tertiary. Those four figures were not added into a unique locality-day count, because the paper treats them as separate school-level datasets. Table III states an average accuracy of 82.05%. The acknowledgment says the weather file was provided by PAGASA's Climatology and Agrometeorology Division. The PDF does not give a public download link for the suspension file.

A Twitter NLP paper titled along the lines of "#Walangpasok on Twitter" appeared only as a secondary summary page. Its full text was not opened, so it is not cited for a tweet count.

Gate: a prior model exists. The training file is not a public dataset this pass could count.

## S04. Thesis titles

HERDIN homepage fetch returned HTTP 504. A search hit on a filtered HERDIN URL displayed "Thesis/Dissertations 10647" beside a keyword search. That number is not used. A filtered page is not a population count. No thesis file was downloaded.

## C01. Rail complaints

No public complaint corpus was opened. No tweet count.

## O03. Match drafts

OpenDota docs returned in search: `GET /publicMatches` returns a sample of public matches, with a free-tier description of 50,000 calls per month and 60 requests per minute on one docs page. A 2018 blog says the API was built for public developers and refers to millions of matches. "Millions" was not opened as a current total. No match file was downloaded. The documented filters that were read do not include a Philippines flag.

## L05. Audit observations

`https://www.coa.gov.ph/reports/annual-audit-reports/` timed out. No observation count. A news page distinguished preliminary audit observation memoranda from published annual audit reports. That is a definition lead, not a corpus.

## T01 and T02. Retail prices

| Source | What the returned page says | Gate |
| --- | --- | --- |
| `https://openstat.psa.gov.ph/Database/Prices/Retail-Prices` | Old series is the Retail Price Survey of Selected Agricultural Commodities, discontinued effective February 2021. New series is monthly CPI retail collection. A direct fetch of the PX-Web table list timed out. A search return of that list showed dimension labels such as 100 geolocations and multi-year monthly periods for cereals. | Dimension labels are not a count of non-missing prices. The old series ends before the 2023 onion spike. |
| Metadata page in the same search return, table 2M4ARP05 | Frequency monthly. Latest available January 2021. | Confirms the end of the old fruit-vegetable table. Not a row count. |
| `https://www.da.gov.ph/price-monitoring/` | Weekly average-price files are listed for 2023 through early October 2026. | No spreadsheet was opened. National weekly averages of a short commodity list would not reach 10,000. Geography inside the files is unknown. |

The 2023 onion-crisis framing is not supported by the opened PSA old series.

## T07. Comtrade, replacement lead only

Search return of `https://comtradeplus.un.org/Subscriptions` describes a free data API of up to 100,000 records per call and says bulk files are not in the free tier. That 100,000 is a cap, not a count of Philippine rows. No Philippine extract was downloaded. Reporter code 608 was not confirmed on an opened code list in this pass.

## Terms and ethics

Court, procurement, review, and forum texts name firms or people. Briefs keep flags and sentiment labels, and they do not convert a score into a finding of fraud or corruption. No personal file was stored.
