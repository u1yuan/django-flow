# QA review: four-field title screen, 6 October 2026

Independent quality review of `opportunity-map.md` against `evidence-ledger.md`, the field files, and the saved extracts in this folder. This note does not rewrite the opportunity map. Local files only. No new microdata were downloaded, and no organization was contacted.

## Verdict

**Pass with limitations.**

No title in the memo is a passed finalist. The two consultation directions stay conditional: next-day urban heat alerts with conformalized XGBoost, and LGU nighttime-radiance growth with XGBoost. The hard-gate counts that stop the other opened-count titles match the saved files. The memo does not report model performance, does not treat a failed HTTP page as a verified mandate, and does not claim that a Western Luzon monthly ENSO and heat-index study was found.

One medium finding: the sentence that every active title has at least three organizations does not match a count of distinct organizations in `client-lists.csv`. The 38-row count does match. No high-severity finding.

## Recomputations

| Claim in the opportunity map | Fresh count | Source used |
| --- | ---: | --- |
| Ages 13–17 in the national GSHS file | 7,763 | `_opened/who-ddi.xml`, file `F5`, variable `q1`: 2,180 + 2,274 + 2,015 + 954 + 340 |
| National-file cases | 10,175 | Same file, `caseQnty` 10,175. Valid ages 10,149 + missing age 26. Regional files 3,520 + 3,506 + 3,149 = 10,175 and are not extra students |
| Globe at Night Philippine rows, 2006–2024 | 323 | Sum of `philippines_rows` over 19 opened year files in `globeatnight-philippines-summary.json`, and 323 data rows in `globeatnight-philippines-rows.csv`. The 2025 entry is HTTP 400 and is not in the sum |
| Coordinate pairs among those rows | 92 | Distinct latitude–longitude pairs in `globeatnight-philippines-rows.csv`. The sum of within-year distinct pairs is 100, because some pairs repeat across years |
| NOAA ISD history rows with country code RP | 116 | 116 data rows in `noaa-isd-history-philippines.csv`, all `CTRY=RP`, 116 distinct USAF–WBAN pairs. Station-hours are not in that file |
| RONI season values | 920 | 920 data rows in `_opened/roni-seasons-parsed.csv` (1950–2025 at 12 seasons, plus 8 seasons in 2026) |
| Very-strong warm episodes | 6 | 19 seasons with RONI at or above 2.0°C, grouped into 6 runs of adjacent seasons: 1965; 1972; 1982–83; 1991–92; 1997–98; 2015–16 |
| 2023–24 peak on that table | 1.4°C | Maximum of the 2023 and 2024 cells is 1.4, at 2023 OND and 2023 NDJ |
| Client rows | 38 | 38 data rows in `client-lists.csv`. Every `verification_date` is 2026-10-06 and every `page_check` is `opened` |
| Conditional title lengths | 11 and 7 | Whitespace tokens. `Nighttime-Radiance` is one token |

`1,642 × 12 = 19,704` is arithmetic only. The memo already says the PSA geographic-code page returned HTTP 403 and that no radiance extract was built. That figure is not an eligible-record count.

## Checks that hold

- Guideline sections 2.1, 2.2, and 4.1 match the memo’s rules: at most 16 words, a named algorithm, model, or technique, and at least 10,000 records for a Data Science study. Section 4.4 is the ethics clause. See finding L2.
- The four opened-count stops are the loneliness age band (7,763), Globe at Night rows (323), protected-area catalogs (248 in the astronomy field quotation; 274 and 249 in `_opened/round2-windows.txt`), and RONI (920 seasons, 6 episodes). A catalog total is not used as the eligible count.
- “Six directions were not counted” matches the inventory of ten titles if the two conditional directions are included. Four other titles sit in “Titles that were not counted.” Together with the four opened-count failures, that is ten directions.
- The two conditional titles are labeled not finalists. The heat and lighting paragraphs are written as later questions, and the memo says they are not results. No accuracy, recall, or error is reported for a thesis dataset.
- The Western Luzon paper is described as not retrieved, and as neither a citation nor a novelty claim. That matches ledger row M6 and `evidence-meteorology.md` row C19.
- HTTP 403 and HTTP 400 results are used as failed retrievals. The PSA page is not used as an official LGU count. OECD pages are not used as a codebook. National Center for Mental Health, Philippine Normal University, the Department of Tourism, MMDA, DHSUD, NDRRMC, and OCD are absent as organization names in the CSV. The words “mental health” appear only inside an unconfirmed note about a Quezon City youth page.
- `thesis_handoff.md` contains nine numbered titles. The memo says none of them becomes an active title.
- The other parenthetical word counts in the memo match whitespace tokenization, with a hyphenated compound counted as one word.
- No client row states that interest, data access, or procurement was granted. The unconfirmed column is filled on all 38 rows. The three words are not repeated in every cell.

Numbers carried by a quotation in a field file, without a second saved publisher page in `_opened`, were not recomputed from the publisher HTML: 248 (PAIS quotation in `evidence-astronomy.md`), 3,662 and 3,531 (abstract quotation in `evidence-psychology.md`; their sum is 7,193), the WMO “Super El Niño” sentence, the 15 October 2022 mobility sentence, 64,947 / 10,815 / 232, and the iHeatMap and iRISE-UP page dates. Those sentences stay as recorded in the field files. Finding L1 covers the one digit that is not inside a quotation.

## Findings

### M1. “At least three organizations” does not match distinct organizations

- Severity: medium
- Location: `opportunity-map.md`, section “Prospective organizations”; the same wording is in `client-verification-notes.md`, line 11, above a table that counts rows
- Evidence: `client-lists.csv` has 38 data rows, and every title in it has 3 or 4 rows. Distinct values of the `organization` column are lower for four titles:
  - Creative thinking and digital leisure: 1 organization (Department of Education), 3 units
  - Heat-alert reliability across ENSO regimes: 2 organizations (PAGASA and Quezon City Government), 4 rows
  - Population-weighted urban heat exposure: 2 organizations (Quezon City Government and PAGASA), 4 rows
  - Urban green access and surface heat: 2 organizations (Quezon City Government and Philippine Space Agency), 4 rows
- The two conditional directions do meet three organizations: the city heat-alert title has PAGASA, Quezon City Government, and the Department of Education; the LGU rows have four organization names. Those LGU rows still use the earlier title “Forecasting Philippine LGU Nighttime-Light Growth Using XGBoost for Dark-Sky Planning,” not the 7-word radiance title in the conditional table.
- Correction: Say “at least three opened rows,” or count distinct organizations and correct the four titles above. State that the LGU client rows still carry the dark-sky wording the screen replaced. Do not treat a row as a separate organization when the organization name repeats.

### L1. The count of 139 cities is not in a saved paper file

- Severity: low
- Location: `opportunity-map.md`, population-weighted heat row; ledger M5; `evidence-meteorology.md` row C18 and the stop paragraph
- Evidence: The field file states that Estoque and colleagues mapped heat-health risk for 139 Philippine cities and quotes their sentence on the lack of measured air temperature. The digit 139 is outside that quotation. No saved HTML for DOI `10.1038/s41467-020-15218-8` is in `_opened`. This pass did not re-read the digit and does not supply another citation.
- Correction: Keep the stop, because no population or temperature pixels were sampled in this screen. Before 139 is repeated as a verified count, save the HTML excerpt that contains it, or mark 139 as not rechecked from a file in this folder.

### L2. “Upward radiance” is not the product-page wording

- Severity: low
- Location: `opportunity-map.md`, LGU conditional row; ledger A1
- Evidence: `_opened/https-eogdata-mines-edu-products-vnl.txt` describes mean or average monthly radiance in nW/cm²/sr and points to a Creative Commons Attribution 4.0 license. The saved page does not use the word “upward.” The unit and the license pointer are supported.
- Correction: Say average radiance in nW/cm²/sr, matching the saved product page.

### L3. “Conditional” is also used for handoff remainders

- Severity: low
- Location: `opportunity-map.md`, handoff table, nighttime-lights row, GAN row, and multispectral row
- Evidence: The decision section limits consultation to two directions and says they are not finalists. The green-access and post-typhoon rows say not to take those titles to faculty as finalists. The handoff table then calls the lighting-change remainder “still conditional,” the precipitation GAN a “conditional backup,” and the multispectral idea “conditional, and not activated,” while also saying none of the nine becomes an active title.
- Correction: Reserve “conditional direction” for the two consultation titles. Call the handoff items backup or not activated, without a third open title.

### L4. The ethics clause is section 4.4

- Severity: low
- Location: `opportunity-map.md`, Decision paragraph; ledger G2
- Evidence: Section 4.1 is the 10,000-record rule. Section 4.4 is the requirement that datasets be ethically sourced and compliant with data privacy laws. The memo’s sentence says “ethically sourced” and cites sections 2.1, 2.2, and 4.1. The ledger cites 4.1 and 4.4.
- Correction: Add section 4.4 to that citation.

## Unresolved items that stay unresolved

These remain open. This review does not close them.

1. A quality-controlled Philippine station-hour file with temperature and humidity or dew point, and a count after exclusions.
2. An LGU-month VIIRS extract with cloud-free coverage and a licensed boundary file. The PSA page used for an official LGU count returned HTTP 403. The figures 1,642 and 19,704 stay plan arithmetic.
3. The full text of Lafi and Bumi (2025), DOI `10.4103/shb.shb_370_24`, if the group still wants to know whether that paper already used latent classes. The age-band count already fails the record rule.
4. An official PISA 2022 codebook. OECD pages returned HTTP 403. The Castulo abstract split remains an abstract-only figure.
5. Whether any iHeatMap or iRISE-UP forecast was archived at its issue time.
6. Written permission for protected-area polygons, if a dark-sky site study is ever revived. The opened site catalogs are already below 10,000 sites.
7. The Western Luzon monthly ENSO and heat-index paper named in the plan. The local search record did not retrieve it. That is a search limit, not a demonstration that no such paper exists.

## Acceptance criteria

| Criterion from the plan | Result |
| --- | --- |
| Title length and a named technique | Met for the titles whose word counts are printed. None is proposed as an approved title. |
| At least 10,000 eligible records, or marked conditional | Met as a screen. Four titles fail an opened count under 10,000. The two consultation titles are marked conditional because the eligible unit was not counted. |
| Material gap claims checked against the closest opened studies | Met for the stops that cite an opened study or a failed retrieval. The 139-city digit was not re-read from a saved paper file (L1). |
| Baseline, held-out evaluation, rights, and beneficiary | Stated as design requirements for the two conditional directions. No baseline score was computed. Rights and participation stay unconfirmed. |
| Each client entry has an official source and a verified-versus-unconfirmed label | Met at row level: each row has a source URL, `page_check=opened`, and an unconfirmed note. The “three organizations” sentence is not met for four titles (M1). |

The opportunity map’s own QA-status line still says the review is pending. This file is that review. The map was not edited.
