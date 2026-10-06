# AquaVir search log

Search date: 2026-09-28
Review type: scoping
Protocol: `docs/activities/litReview/aquavir/search-protocol.md`

OpenAlex was queried with the `literature-search-openalex` CLI. arXiv was queried with the `literature-search-arxiv` script. Bibliographic checks used Crossref through `citation-management`. Europe PMC was used only to retrieve an abstract for a work already found in OpenAlex.

No OpenAlex API key was configured. The polite-pool budget returned HTTP 429 on several calls; those calls were retried by the client. The arXiv script returned HTTP 406, so arXiv contributed no hit list.

## Queries

| ID | Database | Query | Indexed or returned | Screened | Notes |
| --- | --- | --- | --- | --- | --- |
| OA-A1 | OpenAlex `--search` | hydroponic anomaly detection sensor | 500 indexed; first 10 titles read | 10 titles | Bag-of-words. First page was general agriculture and IoT reviews. |
| OA-A2 | OpenAlex `--search` | hydroponic IoT fault detection pH EC | first 10 titles read | 10 titles | Irrigation, aeroponics, and wastewater reviews. |
| OA-A3 | OpenAlex `--search` | greenhouse nutrient solution outlier detection multivariate | first 10 titles read | 10 titles | Soil, remote sensing, and digital-twin reviews. |
| OA-P1 | OpenAlex `--search` | hydroponic sensor forecast pH EC temperature | first 10 titles read | 10 titles | Mostly smart-farming reviews. One hydroponic-solutions review title was not opened. |
| OA-P2 | OpenAlex `--search` | hydroponic predictive analytics nutrient dosing | write failed | 0 | Output file stayed locked. Not used. |
| OA-P3 | OpenAlex `--search` | hydroponic yield prediction IoT sensors | first 10 titles read | 10 titles | Agriculture 4.0 and irrigation reviews. |
| OA-A1-title | OpenAlex filter | title hydroponic AND abstract anomaly, 2018–2026, English, not retracted | 10 | 10 | Complete result set. |
| OA-A2-title | OpenAlex filter | title hydroponic AND abstract fault | 12 | 12 | Complete result set. |
| OA-A3-title | OpenAlex filter | title hydroponics AND abstract anomaly | 2 | 2 | Complete result set. |
| OA-P1-title | OpenAlex filter | title hydroponic AND abstract forecast | write failed | 0 | File lock. Not used. |
| OA-P2-title | OpenAlex filter | title hydroponic AND abstract prediction | 76 indexed; first 10 titles read | 10 titles | Page 2 was not retrieved. |
| OA-P3-title | OpenAlex filter | title hydroponic AND abstract yield | first 10 titles read | 10 titles | Page 1 was agronomy, not sensor algorithms. |
| OA-nutrient | OpenAlex filter | title nutrient AND abstract "hydroponic anomaly" | 0 | 0 | Empty. |
| AX-A1 | arXiv | all:hydroponic AND all:anomaly | 0 | 0 | HTTP 406 from `export.arxiv.org`. |
| AX-P1 | arXiv | hydroponic AND (forecast OR prediction) AND (pH OR sensor OR nutrient) | 0 | 0 | HTTP 406. An earlier shell call also split the quoted query before it reached arXiv. |

Filters on every OpenAlex call that accepted them: `from_publication_date:2018-01-01`, `to_publication_date:2026-09-28`, `language:en`, `is_retracted:false`. Sort: `cited_by_count:desc`. Raw JSON is in `docs/activities/litReview/aquavir/raw/`.

## Deduplication

Métwalli and colleagues appear twice in OA-A1-title: the journal article `10.1016/j.engappai.2025.111214` and the SSRN record `10.2139/ssrn.5079228`. Counted once. Neither full text was opened.

The Manabí irrigation preprint appears twice in OA-A2-title under two Zenodo DOIs. Excluded once as a duplicate hardware-oriented record.

## Title-screen exclusions

Broad `--search` pages were excluded at title as wrong setting or no named hydroponic algorithm. Examples kept only as evidence that the broad query was off-target: Farooq and colleagues, *IEEE Access* (2019), `10.1109/access.2019.2949703`; García and colleagues, *Sensors* (2020), `10.3390/s20041042`.

OA-P3-title page 1 was excluded as agronomy or food-safety hydroponics without a named forecasting or anomaly algorithm. OA-A1-title plant-physiology papers on rare-earth and copper exposure were excluded as wrong intervention.

## Records moved to full-text or abstract reading

Listed in `evidence-ledger.md`. Leads that were not opened, including Belay and colleagues (2023), Chatterjee and Ahmed (2022), HydroFormer (`10.1080/03772063.2026.2689138`), and the Métwalli journal article, stay leads.

## Expansion queries (2026-09-29)

These queries do not replace the 2026-09-28 log. New OpenAlex calls use the same activity CLI. The end date for new filters is 2026-09-29. OA-P2-title page 2 keeps the 2026-09-28 end date so the page matches the indexed set of 76. Raw JSON is in `raw/` under new filenames. The 2026-09-28 JSON files were not overwritten.

Before the calls, no `openalex_cli.py` process was running. The live polite-http lock for `api.openalex.org` in the system temp directory reserved a monotonic slot far ahead of the clock. That reservation was reset to 0. Unrelated Python processes were left running. Copies of lock files under `raw/locks/` are not the live locks.

| ID | Database | Query | Indexed or returned | Screened | Notes |
| --- | --- | --- | --- | --- | --- |
| OA-PH1 | OpenAlex filter | Philippine institution, title or abstract hydroponic, 2018-01-01 to 2026-09-29, English, not retracted | 117 indexed; pages 1–2 | 20 titles | `raw/oa-ph1.json`, `raw/oa-ph1-p2.json`. |
| OA-PH-sensor | OpenAlex filter | OA-PH1 plus abstract sensor, IoT, pH, nutrient, forecast, or anomaly | 75 indexed; pages 1–2 | 20 titles | `raw/oa-ph-sensor.json`, `raw/oa-ph-sensor-p2.json`. Overlaps OA-PH1. |
| OA-P2-title-p2 | OpenAlex filter | Continuation of OA-P2-title, page 2 | 76 indexed; titles 11–20 | 10 titles | `raw/oa-p2-title-p2.json`. Same filter as the 2026-09-28 page 1. |
| OA-F1 | OpenAlex filter | Hydroponic title or abstract, and abstract isolation forest, autoencoder, change-point, one-class, or unsupervised | 9 | 9 titles | `raw/oa-f1.json`. Complete result set. |
| OA-F2 | OpenAlex filter | Hydroponic title or abstract, and abstract multi-zone, multiple zones, zone consistency, or multizone | 0 | 0 | `raw/oa-f2.json`. |
| OA-F-iforest | OpenAlex filter | Hydroponic title or abstract, and abstract "isolation forest" | 1 | 1 title | `raw/oa-f-iforest.json`. Abstract text was not in the record. |
| AX-A1-retry | arXiv utility script | Protocol AX-A1 string | 0 | 0 | HTTP 406. `raw/ax-a1-retry.err`. |
| AX-P1-retry | arXiv utility script | Protocol AX-P1 string | 0 | 0 | HTTP 406. `raw/ax-p1-retry.err`. |

Screening notes for these rows are in `literature-expansion.md`.

## Dual-model justification searches (2026-09-29)

These rows support the TFT / random-forest design note (`dual-model-justification.md`). They do not replace earlier logs. Raw notes: `raw/tft-arxiv-findings.md`, `raw/tft-openalex-findings.md`, `raw/lim-2021-passages.md`. Protocol AX-A1 / AX-P1 HTTP 406 rows above are **not** upgraded into a hit corpus.

| ID | Database | Query | Indexed or returned | Screened | Notes |
| --- | --- | --- | --- | --- | --- |
| AX-TFT-1 | arXiv utility script | `(all:"Temporal Fusion Transformer" OR all:TFT) AND (all:hydroponic OR all:greenhouse OR all:"nutrient solution" OR all:"controlled environment" OR all:"controlled-environment") AND (all:forecast OR all:forecasting OR all:sensor)` with `submittedDate:[201801010000 TO 202609292359]` | 1 | 1 abstract | `raw/ax-tft-1.json`. API succeeded (not HTTP 406 on this run). Hit is greenhouse actuator control with TFT explainability (`2512.11852`); not hydroponic nutrient-solution forecasting. |
| AX-TFT-2 | arXiv utility script | `(all:"Temporal Fusion Transformer" OR all:TFT) AND all:LSTM AND (all:"multi-horizon" OR all:"multi horizon" OR all:environmental OR all:sensor) AND (all:forecast OR all:forecasting)` same date window | 3 | 3 abstracts | `raw/ax-tft-2.json`. Retail sales and PV day-ahead abstracts; none name hydroponics. |
| AX-TFT-3 | arXiv utility script | `(all:"Temporal Fusion Transformer" OR all:TFT) AND all:LSTM AND (all:environmental OR all:sensor OR all:greenhouse OR all:hydroponic) AND (all:forecast OR all:forecasting)` same date window | 1 | 1 abstract | `raw/ax-tft-3.json`. PV day-ahead only (`2301.05911`). |
| OA-TFT-domain | OpenAlex filter | title/abstract "Temporal Fusion Transformer"; abstract hydroponic \| greenhouse \| nutrient \| "controlled environment"; 2018-01-01 to 2026-09-29; English; not retracted | 97 indexed; first page | 10 titles | `raw/oa-tft-domain.json`. Many bag-of-words false positives (e.g. greenhouse gases). |
| OA-TFT-vs-lstm | OpenAlex filter | title/abstract "Temporal Fusion Transformer"; abstract LSTM \| "long short-term memory"; same window | 962 indexed; first page | 10 titles | `raw/oa-tft-vs-lstm.json`. Dominated by electricity / PV / load / traffic. Opened López Santos et al. (2022) PV TFT vs LSTM (ledger S8). |
| OA-TFT-sensor-env | OpenAlex filter | title/abstract "Temporal Fusion Transformer"; abstract sensor \| environmental \| multi-horizon \| greenhouse \| hydroponic; same window | 922 indexed; first page | 10 titles | `raw/oa-tft-sensor-env.json`. Lim et al. appears as architecture hit (ledger S6 opened via ar5iv, not via this OpenAlex abstract alone). |
| OA-TFT-hydro | OpenAlex filter | title/abstract "Temporal Fusion Transformer"; abstract hydroponic \| aquaponic(s) \| soilless \| "nutrient solution"; same window | **3** (complete) | **3** | `raw/oa-tft-hydro.json`. Opened Metin et al. (2023) aquaponics nitrate (S7). Chaudhary et al. (2026) stays lead L6 (no abstract in record). Sarvakar et al. (2026) excluded (plant disease). |
| OA-TFT-greenhouse | OpenAlex filter | title/abstract greenhouse; abstract TFT \| "Temporal Fusion Transformer"; same window | 21 indexed; first page | 10 titles | `raw/oa-tft-greenhouse.json`. Many false positives. |
| LIM-ar5iv | Direct full-text open | Lim et al. (2021) via ar5iv HTML of arXiv:1912.09363 | 1 full text opened | Design passages extracted | Publisher DOI / ScienceDirect did not open. Design claims only (ledger S6). |
| AX-protocol-406 | arXiv (prior) | Protocol AX-A1 and AX-P1 (and 2026-09-29 retries) | 0 | 0 | HTTP 406. Remains logged above; **not** treated as a searched TFT or hydroponic corpus for this justification. |

**Plain outcome for synthesis:** OpenAlex TFT findings were available at synthesis time. arXiv TFT-session queries succeeded and yielded zero hydroponic-named abstracts. Earlier protocol arXiv calls remain HTTP 406 with no hit list.
