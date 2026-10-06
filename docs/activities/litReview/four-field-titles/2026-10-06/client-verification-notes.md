# Client verification notes

Checked on 6 October 2026. Each row is a prospective public organization whose opened official page states a mandate that could fit one decision. Listing an organization does not mean it is a buyer, partner, data provider, or endorser, and it does not mean interest, data access, or procurement.

No personal names, direct lines, or outreach are included. Contact values are organizational page URLs. Native Trees, hydroponics, diesel, and parked handoff titles are out of scope.

The plan table in `THESIS_TITLE_RESEARCH_PLAN.md` was treated as a same-day lead checklist. Mandate sentences in the CSV are taken from pages retrieved on this date. Where the first client rejected a certificate, a later HTTPS GET that returned the page text is marked opened. HTTP 403, HTTP 404, timeouts, and connection failures are failed and are not used as verified mandates.

## Rows per title

All 38 CSV rows are `page_check=opened`. Every title has at least three rows. Distinct organization names are fewer than three for four titles: creative thinking has one organization across three Department of Education units; the ENSO heat-alert title has two (PAGASA and Quezon City Government); population-weighted heat exposure has those same two; urban green access has two (Quezon City Government and the Philippine Space Agency). The LGU rows still carry the title “Forecasting Philippine LGU Nighttime-Light Growth Using XGBoost for Dark-Sky Planning.”

| Title | Opened rows |
| --- | ---: |
| Filipino Adolescent Loneliness Patterns and Protective Factors Using Latent Class Analysis | 3 |
| Creative Thinking and Digital Leisure Across Southeast Asian PISA Systems Using Multilevel IRT | 3 |
| Forecasting Philippine LGU Nighttime-Light Growth Using XGBoost for Dark-Sky Planning | 4 |
| Estimating Philippine Night-Sky Brightness Using XGBoost and Satellite–Ground Observations | 4 |
| Prioritizing Philippine Dark-Sky Conservation Sites Using NSGA-II and Nighttime-Light Trends | 4 |
| Evaluating Urban Heat Alert Reliability Across Philippine Cities Using Conformalized XGBoost | 4 |
| Evaluating Philippine Urban Heat Alert Reliability Across ENSO Regimes Using Conformalized XGBoost | 4 |
| Estimating Population-Weighted Urban Heat Exposure Across Philippine Cities Using Spatial Random Forests | 4 |
| Mapping Philippine Urban Green Access and Surface Heat Using Random Forest and Network Analysis | 4 |
| Assessing Post-Typhoon Nighttime Lighting Recovery Using VIIRS and Change-Point Detection | 4 |

## What stayed unconfirmed

Every row still has unconfirmed interest. Data access, procurement, and program fit are unconfirmed wherever the opened page does not itself provide the file, threshold, or lighting, heat, or youth use the title needs. Nighttime lighting is not treated as economic recovery. Satellite surface temperature is not treated as pedestrian comfort.

An organization can appear under more than one title only for a different decision, as written in `decision_or_contribution`.

## Plan leads that were not kept

- DepEd Schools Division Office of Valenzuela City. The TeleSafe release is a national helpline rollout held in Valenzuela. The regional directory lists a division office. The citizen's charter PDF does not name Valenzuela. None of those opened pages states a division learner-support mandate.
- National Center for Mental Health. The citizen's charter PDF and the agency home pages returned HTTP 403.
- Philippine Normal University Research Institute for Teacher Quality. The plan URLs and the university home page timed out.
- Puerto Princesa City Environment and Natural Resources Office. The page opened. Its functions cover forests, protected areas, tree parks, and environmental management. It does not state a lighting or dark-sky mandate, so it is not listed.
- Department of Tourism. The plan URLs returned HTTP 403. The public destination site opened, but not as a product-development mandate. `https://www.tourism.gov.ph/about` returned HTTP 404.
- MMDA and DHSUD. Home and about URLs returned HTTP 403, so they are not listed for urban green access.
- NDRRMC and OCD. Home URLs returned HTTP 403, or the certificate check failed and a later request still returned HTTP 403. The Metro Manila disaster row is the Quezon City DRRMO. PAGASA is listed only to date typhoon events, not to treat lighting change as recovery of the economy.

## URLs that failed

- `https://www.ncmh.gov.ph/images/pdf/iso/2025-7TH-EDITION-04072025.pdf` — HTTP 403
- `https://ncmh.gov.ph/` — HTTP 403
- `https://www.ncmh.gov.ph/index.php` — HTTP 403
- `https://www.pnu.edu.ph/tec-designates-pnu-other-heis-as-teacher-education-excellence-centers/` — timeout
- `https://www.pnu.edu.ph/directory/` — timeout
- `https://www.pnu.edu.ph/` — timeout
- `https://remote.tourism.gov.ph/tourism/about-dot/` — HTTP 403
- `https://remote.tourism.gov.ph/contact-us/central-offices/` — HTTP 403
- `https://www.tourism.gov.ph/dot/` — HTTP 403
- `https://www.tourism.gov.ph/about` — HTTP 404
- `https://beta.tourism.gov.ph/` — timeout
- `https://mmda.gov.ph/` — HTTP 403
- `https://www.mmda.gov.ph/` — HTTP 403
- `https://mmda.gov.ph/index.php` — HTTP 403
- `https://dhsud.gov.ph/` — HTTP 403
- `https://www.dhsud.gov.ph/` — HTTP 403
- `https://dhsud.gov.ph/about-us/` — HTTP 403
- `https://dhsud.gov.ph/about/` — HTTP 403
- `https://ndrrmc.gov.ph/` — HTTP 403
- `https://www.ndrrmc.gov.ph/` — HTTP 403
- `https://ndrrmc.gov.ph/index.php` — HTTP 403
- `https://ocd.gov.ph/` — certificate check failed, then HTTP 403
- `https://www.ocd.gov.ph/` — certificate check failed
- `https://ocd.gov.ph/index.php` — HTTP 403
- `https://bmb.gov.ph/` — HTTP 403
- `https://www.bmb.gov.ph/` — HTTP 403
- `https://www.denr.gov.ph/` — HTTP 403
- `https://doh.gov.ph/` — HTTP 403
- `https://cpd.gov.ph/` — HTTP 403
- `https://www.cpd.gov.ph/` — HTTP 403
- `https://popcom.gov.ph/` — connection failed
- `https://www.popcom.gov.ph/` — connection failed
- `https://www.foi.gov.ph/` — HTTP 403
- `https://www.officialgazette.gov.ph/` — HTTP 403
- `https://namria.gov.ph/about.html` — HTTP 404
- `https://pagasa.dost.gov.ph/astronomy/astronomy-in-the-philippines` — HTTP 404
- `https://pagasa.dost.gov.ph/astronomy/telescoping-and-stargazing` — HTTP 404
- `https://www.deped.gov.ph/about-deped/central-office/` — HTTP 404
- `https://www.dswd.gov.ph/mission-vision-and-core-values-2/` — timeout
- `https://www.up.edu.ph/` — redirect did not return a page

`https://geoportal.gov.ph/` opened as a map application. The retrieved HTML does not name NAMRIA and does not state a mandate, so it is not a row. NAMRIA is listed only from the opened client-service page that calls it the central mapping agency.

## Review status

Self-check against the brief: 10 active titles, 3–5 opened rows each, a source URL on every row, failed pages excluded from verified mandate text, and no personal contact data in the CSV. An independent quality-review pass was not run in this session. Status: pass with limitations. The limitations are the blocked agency sites above and the unconfirmed interest, access, and program fit on every row.
