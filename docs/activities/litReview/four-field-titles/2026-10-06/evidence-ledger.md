# Claim ledger for the four-field title screen

Compiled: 6 October 2026. Each row is a claim used in `opportunity-map.md`. Status labels mean:

- **verified-passage** — a page, codebook, or table opened on 6 October 2026 contains the quoted or counted fact.
- **abstract-only** — the abstract was opened. The full text was not.
- **computed-from-opened-file** — the count was calculated from a file saved in this folder.
- **not-opened** — the search or the page failed. The claim is the failure, not a finding about the topic.

Search strings, inclusion decisions, and longer quotations stay in the field evidence files. This ledger does not add citations beyond those files.

| ID | Claim used in the opportunity map | Status | Locator |
| --- | --- | --- | --- |
| G1 | A Data Science title may contain at most 16 words and must name the algorithm, model, or technique. | verified-passage | `docs/CS-Guideline-as-of-Nov-17-as-430pm-without-signature (1).md`, sections 2.1 and 2.2 |
| G2 | A Data Science study must use a dataset of at least 10,000 records, ethically sourced. | verified-passage | Same guideline, sections 4.1 and 4.4 |
| P1 | The 2019 Philippine GSHS national file lists 10,175 cases. Ages 13–17 account for 7,763 of them. Missing age accounts for 26. | computed-from-opened-file | WHO DDI in `_opened/who-ddi.xml`; arithmetic in `data-feasibility.md` section 1: 2,180 + 2,274 + 2,015 + 954 + 340 = 7,763 |
| P2 | The loneliness item asks, “During the past 12 months, how often have you felt lonely?” Joint complete cases with the protective-factor items were not computed. | verified-passage | DDI variable text saved in `_opened/who-variable-hits.txt`. Complete-case cross-tab was not run because microdata were not downloaded. |
| P3 | Lafi and Bumi (2025) report a multinomial regression of loneliness on four GSHS files, including the Philippines 2019, with a four-country sample of 21,901 in the abstract. | abstract-only | DOI `10.4103/shb.shb_370_24`, Crossref abstract, `evidence-psychology.md` row L6 |
| P4 | Cai, Bi, and Feng (2026) analyze 28,342 students in Singapore, Hong Kong-China, Macao-China, Chinese Taipei, and Korea, with a weekday video-game item and a social-media item. The Philippines does not appear in that opened text. | verified-passage | DOI `10.3389/fpsyg.2025.1655731`, section 4.1, `evidence-psychology.md` row L13 |
| P5 | OECD PISA 2022 database and Volume III URLs returned HTTP 403. Philippine ICT-item coverage was not verified from an official codebook. | not-opened | `evidence-psychology.md` search log; `_opened` error files for the OECD URLs |
| P6 | Castulo and colleagues’ abstract states 3,662 female and 3,531 male Philippine creative-thinking respondents. | abstract-only | DOI `10.11591/edulearn.v20i3.24227`. The sum 7,193 is arithmetic on those two abstract figures. |
| A1 | Monthly VIIRS average radiance is reported in nW/cm²/sr, and the product page points readers to a Creative Commons Attribution 4.0 license. | verified-passage | Saved page `_opened/https-eogdata-mines-edu-products-vnl.html` |
| A2 | 1,642 × 12 = 19,704 is potential LGU-month arithmetic. No LGU-month extract was built. The PSA geographic-code page returned HTTP 403. | computed-from-plan | `data-feasibility.md` section 3. The 1,493 and 149 inputs were not re-counted from PSA. |
| A3 | Globe at Night files that opened contain 323 Philippine rows for 2006–2024. The 2025 file returned HTTP 400. | computed-from-opened-file | `globeatnight-philippines-summary.json`; independent sum of `philippines_rows` is 323 across 19 year files |
| A4 | The PAIS about page says the eNIPAS Act of 2018 brings the protected-area total to 248. | verified-passage | https://pais.bmb.gov.ph/about, re-opened 6 October 2026. The sentence begins “The eNIPAS Act of 2018 brings to 248.” |
| A5 | The WDPA Philippines profile prints 274 protected areas and 249 national designations. | verified-passage | `data-feasibility.md` section 5, from the opened profile |
| A6 | Bará, Rigueiro, and Lima state that SQM-band brightness and VIIRS-DNB radiance may show different, even opposite, behavior. | abstract-only | arXiv:1909.10909, `evidence-astronomy.md` row BARA-2019 |
| A7 | Zenodo 4002935 version 3.2 describes 64,947 images from 10,815 original landmarks and 232 HiRISE source images, with Martian classes. | verified-passage | Zenodo record as opened in `evidence-astronomy.md` |
| M1 | WMO’s ENSO theme page says: “WMO does not use the term Super El Niño or La Niña.” | verified-passage | https://wmo.int/themes/el-nino-la-nina-phenomena, re-opened 6 October 2026 |
| M2 | NOAA’s June 2026 RONI strengths archive has a column `Index ≥ 2.0°C`. The historical table contains 6 independent warm episodes at or above 2.0°C. The 2023 OND and NDJ values are 1.4°C. | computed-from-opened-file | `_opened/roni-very-strong-summary.json` and `roni-seasons-parsed.csv` |
| M3 | The historical RONI page says values may change for up to two months after the initial real-time value is posted, and that the most recent values should be treated as an estimate. The strengths archive says El Niño or La Niña strength does not necessarily correspond to the strength of local influence. | verified-passage | Saved text `_opened/https-www-cpc-ncep-noaa-gov-products-analysis-monitoring-enso-roni.txt`; `evidence-meteorology.md` rows C5 and C6 |
| M4 | PAGASA’s iHeatMap press release is dated 4 April 2025 on the page. Quezon City’s iRISE-UP page is dated 22 April 2024. Neither page was an issue-time forecast archive. | verified-passage | `evidence-meteorology.md` rows C10 and the title card. Personal contact lines in the release were omitted. |
| M5 | The meteorology field file records that Estoque and colleagues mapped Philippine city heat-health risk with land surface temperature because measured air temperature was lacking. The digit 139 is in that field file and was not rechecked from a saved HTML copy in this folder. | field-file | `evidence-meteorology.md` row C18. DOI `10.1038/s41467-020-15218-8`. No saved HTML for that DOI is in `_opened`. |
| M6 | PubMed, the screened Crossref pages, and Europe PMC did not retrieve a Western Luzon monthly ENSO and heat-index study. | not-opened | `evidence-meteorology.md` row C19. This is a search limit, not a demonstration that no such paper exists. |
| M7 | The NOAA ISD history file contains 116 rows with country code RP, and 116 distinct USAF–WBAN pairs. Station-hours were not computed. | computed-from-opened-file | `noaa-isd-history-philippines-summary.json` |
| U1 | Landsat 9 Collection 2 Level-2 includes `ST_B10`, described as Band 10 surface temperature. | verified-passage | Saved catalog text `_opened/https-developers-google-com-earth-engine-datasets-catalog-landsat-lc09-c02-t1-l2.txt` |
| U2 | The VIIRS monthly Earth Engine asset describes `avg_rad` as average DNB radiance. | verified-passage | Saved catalog text for `NOAA/VIIRS/DNB/MONTHLY_V1/VCMSLCFG` |
| U3 | Google’s Community Mobility Reports help page says: “We stopped reporting new data on Oct 15, 2022.” | verified-passage | https://support.google.com/covid19-mobility/?hl=en, re-opened 6 October 2026 |
| U4 | No cloud-filtered Sentinel-2 or Landsat pixel sample, and no typhoon-polygon join, was computed. | not-opened | `data-feasibility.md` sections 9 and 10 |
| C0 | The client CSV has 38 opened rows dated 2026-10-06. Four titles have fewer than three distinct organization names: creative thinking has one; the ENSO heat-alert title and the population-weighted heat title have two; urban green access has two. The LGU rows still use the dark-sky title wording. Interest, data access, and procurement are unconfirmed on every row. | computed-from-opened-file | `client-lists.csv`, organization column grouped by title |

## Counts checked again while compiling this ledger

| Check | Result |
| --- | --- |
| Ages 13–17 | 2,180 + 2,274 + 2,015 + 954 + 340 = 7,763 |
| Valid ages plus missing | 10,149 + 26 = 10,175 |
| Globe at Night `philippines_rows` | 323 across 19 opened year files; 2025 is an HTTP 400 error |
| ISD history | 116 RP rows |
| Very-strong RONI episodes | 6: 1965, 1972, 1982–83, 1991–92, 1997–98, 2015–16 |

## What this ledger does not support

- Any model accuracy, recall, or error for a thesis dataset.
- A claim that children’s creativity has declined because of technology.
- A claim that El Niño raises the heat index in every Philippine city.
- A claim that VIIRS radiance measures visible stars, pedestrian comfort, GDP, or restored infrastructure.
- A claim that any listed organization has agreed to participate.
