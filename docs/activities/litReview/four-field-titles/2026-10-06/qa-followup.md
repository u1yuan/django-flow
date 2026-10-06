# QA follow-up: four-field title screen, 6 October 2026

Follow-up review of the revision after `qa-review.md`. This note checks the revised sentences. It does not rewrite `opportunity-map.md`. Local files only. No new microdata were downloaded, and no organization was contacted.

The QA status line in `opportunity-map.md` still says a follow-up review is the next pass. That line is the status before this note and is not a failure of the revision.

## Findings from the first review

### M1. Resolved

`opportunity-map.md`, “Prospective organizations,” no longer says that every title has at least three organizations. The sentence checked is: “That is a row count. It is not a count of distinct organizations. Four titles have fewer than three organization names: creative thinking has one (the Department of Education, across three units); the ENSO heat-alert title has two (PAGASA and Quezon City Government); population-weighted heat exposure has those same two; urban green access has two (Quezon City Government and the Philippine Space Agency).”

`client-verification-notes.md`, “Rows per title,” now says: “Every title has at least three rows. Distinct organization names are fewer than three for four titles.”

A fresh count of `client-lists.csv` (38 data rows) matches those four titles:

- Creative Thinking and Digital Leisure Across Southeast Asian PISA Systems Using Multilevel IRT: 1 organization (Department of Education) across 3 units
- Evaluating Philippine Urban Heat Alert Reliability Across ENSO Regimes Using Conformalized XGBoost: 2 organizations
- Estimating Population-Weighted Urban Heat Exposure Across Philippine Cities Using Spatial Random Forests: 2 organizations
- Mapping Philippine Urban Green Access and Surface Heat Using Random Forest and Network Analysis: 2 organizations

The same file still gives the LGU title as “Forecasting Philippine LGU Nighttime-Light Growth Using XGBoost for Dark-Sky Planning” on all four of its rows. `opportunity-map.md` and `client-verification-notes.md` both state that those rows still use that earlier title.

### L1. Resolved

`opportunity-map.md`, population-weighted heat row, says: “The figure of 139 cities is in that field file and was not rechecked from a saved HTML copy in this folder.”

`evidence-ledger.md` row M5 says: “The digit 139 is in that field file and was not rechecked from a saved HTML copy in this folder.” The locator adds: “No saved HTML for that DOI is in `_opened`.” No file for DOI `10.1038/s41467-020-15218-8` is in `_opened`.

### L2. Resolved

`opportunity-map.md`, LGU conditional row, says: “Earth Observation Group monthly VIIRS composites report average radiance in nW/cm²/sr, and the product page points to a Creative Commons Attribution 4.0 license.” The only use of “upward” in that file is the next sentence: “The saved product page does not use the word ‘upward.’”

`evidence-ledger.md` row A1 says: “Monthly VIIRS average radiance is reported in nW/cm²/sr, and the product page points readers to a Creative Commons Attribution 4.0 license.” The saved page `_opened/https-eogdata-mines-edu-products-vnl.html` states average monthly radiance in nW/cm²/sr and a Creative Commons Attribution 4.0 license, and it does not contain the word “upward.”

### L3. Resolved

`opportunity-map.md`, handoff table, does not call these three items a conditional consultation direction. The sentences checked are:

- GAN row: “Backup only, and not one of the two consultation directions.”
- Nighttime-lights row: “The lighting-change wording above is the remainder, and it is not a consultation direction.”
- Multispectral row: “Not activated.”

“Conditional direction” in that file remains the label for the two consultation titles.

### L4. Resolved

`opportunity-map.md`, Decision paragraph, says the study must be “sourced in line with the ethics clause” and cites “sections 2.1, 2.2, 4.1, and 4.4” of `docs/CS-Guideline-as-of-Nov-17-as-430pm-without-signature (1).md`. Section 4.4 of that guideline is: “Datasets must be ethically sourced and compliant with data privacy laws.” `evidence-ledger.md` row G2 still cites sections 4.1 and 4.4.

## New issues

None. The revision did not add a claim that this pass contradicts.

## Verdict

**Pass with limitations.**

M1, L1, L2, L3, and L4 are resolved. No title in the memo is a passed finalist. The two consultation directions stay conditional because the eligible station-hour file and the LGU-month extract were not built. The open items listed in `qa-review.md` under “Unresolved items that stay unresolved” remain open. This follow-up does not close them.
