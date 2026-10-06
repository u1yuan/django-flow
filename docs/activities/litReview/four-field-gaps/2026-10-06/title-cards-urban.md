# Urban title cards — 6 October 2026

Draft for a judging panel. The only evidence is `gap-candidates-urban.md`. These cards restate candidate gaps from a scoping pass. They are not novelty claims, fitted results, or confirmed venue indexing.

Limits kept on the cards: IEEE recent-issue pages did not pass, and Scopus indexing was not confirmed. Card 3 has no passing crash-record lead. Philippine rows were not confirmed for Ookla.

This writing pass did not reopen sources, download a dataset, or fit a model. Hydroponics and diesel stay out. Bibliographic strings are copied from the gap file and were not re-validated here. Human verification against the opened text is still required. Not submission-ready.

## Card 1 — Measured broadband tiles and surveyed access

### Named user and decision

The named population is people with and without modern internet access, the group named in the opened Ookla README. The recorded decision is where a connectivity review should compare measured tile speed with surveyed access. The development goal named for this card is SDG 9, including the broadband target discussed in the opened Osoro and Oughton review. No agency is named as the user.

### Demonstrable artifact

The proposed artifact is a later comparison of surveyed access or an advertised plan menu with a public grid of averaged speed-test results. Geographically weighted regression is the technique named in the draft title. No model was fit. The dataset lead is Ookla global fixed and mobile performance map tiles. The opened pages are `https://github.com/teamookla/ookla-open-data` and `https://raw.githubusercontent.com/teamookla/ookla-open-data/master/README.md`. The documented unit is a zoom level 16 web-mercator tile, about 610.8 meters by 610.8 meters at the equator, in files the README names as Shapefile and Apache Parquet. The README points to an AWS open-data registry that was not opened, so the download button itself was not seen. The dataset was not downloaded. This lead is not a counted analysis file. Philippine rows were not confirmed: the word Philippines does not appear in the README, global coverage is stated, and Philippine tiles are not confirmed. The recorded subdomain is statistical modeling.

### One-sentence innovation

The candidate gap asks whether places that look poorly connected in a survey or a plan menu also look poorly connected on a public grid of averaged speed-test results, a comparison the opened conclusion of Paul and colleagues (2023) does not make: that conclusion analyzes plans from seven major ISPs across thirty US cities, covering 837 thousand street addresses, and no separate limitation sentence on measured throughput was extracted.

### Measurable impact against a baseline

The impact figure is a target to test later, not a result: whether places classed as poorly connected on a survey or a plan menu are also poorly connected on the tile layer, with the survey or plan menu as the comparison design named in the gap statement. No agreement measure, coefficient, sample size, or effect estimate is recorded. The gap statement records that this comparison is its own study: it is not a larger New Zealand panel, not a causal model of intergenerational ties, and not a wider literature review. Associations between tile speed and survey responses are not causes. The study would not assign a legal breach, a clinical label, or a household identity.

### Transfer or scale

Global coverage is stated in the README, and Philippine tiles are not confirmed, so a Philippine transfer is not established by the lead. The opened nearest studies measure advertised US plan menus, a New Zealand online panel, digital-skill clusters in Bulgaria, Finland, and Italy, or a review of broadband and the Sustainable Development Goals. IEEE Access (`https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=6287639`) and IEEE Transactions on Intelligent Transportation Systems (`https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=6979`) opened with HTTP 200 and returned only the journal title, so neither venue passes. A Scopus source page failed on an expired certificate, and indexing of comparable 2022–2026 studies was not confirmed. Noncommercial use applies: the opened README contains the words Creative Commons, CC BY, and noncommercial.

### Title

Mapping Measured Broadband Gaps for Urban Residents Using Geographically Weighted Regression.

Word count: 11.

### Pitch

Surveys, plan menus, skill clusters, and a broadband review do not compare access with public averaged speed-test tiles. A later geographically weighted regression would test that comparison as an association.

Word count: 30.

### Ethics line

A slow tile can still stigmatize a neighborhood; tiles are about 610.8 meters on a side at the equator and the README says GPS-quality locations are averaged per tile, and the design would not re-identify Speedtest users or treat a slow tile as proof that an operator failed a legal duty.

### Claim map

| Claim | Factual sentence | Gap-card section |
| --- | --- | --- |
| C1-01 | The named population is people with and without modern internet access, the group named in the opened Ookla README. | Card 1, Social implication |
| C1-02 | The recorded decision is where a connectivity review should compare measured tile speed with surveyed access. | Card 1, Social implication |
| C1-03 | The development goal named for this card is SDG 9, including the broadband target discussed in the opened Osoro and Oughton review. | Card 1, Social implication |
| C1-04 | No agency is named as the user. | Card 1, Social implication (no office is named there) |
| C1-05 | The proposed artifact is a later comparison of surveyed access or an advertised plan menu with a public grid of averaged speed-test results. | Card 1, Gap statement |
| C1-06 | Geographically weighted regression is the technique named in the draft title. | Card 1, Draft title |
| C1-07 | No model was fit. | File header |
| C1-08 | The dataset lead is Ookla global fixed and mobile performance map tiles. | Card 1, Dataset lead |
| C1-09 | The opened pages are the Ookla GitHub repository and the README raw URL. | Card 1, Dataset lead |
| C1-10 | The documented unit is a zoom level 16 web-mercator tile, about 610.8 meters by 610.8 meters at the equator, in Shapefile and Apache Parquet. | Card 1, Dataset lead |
| C1-11 | The README points to an AWS open-data registry that was not opened, so the download button itself was not seen. | Card 1, Dataset lead |
| C1-12 | The dataset was not downloaded. This lead is not a counted analysis file. | Card 1, Dataset lead |
| C1-13 | Philippine rows were not confirmed: the word Philippines does not appear in the README, global coverage is stated, and Philippine tiles are not confirmed. | Card 1, Dataset lead |
| C1-14 | The recorded subdomain is statistical modeling. | Card 1, Subdomain |
| C1-15 | The candidate gap asks whether places that look poorly connected in a survey or a plan menu also look poorly connected on a public grid of averaged speed-test results. | Card 1, Gap statement |
| C1-16 | Paul and colleagues (2023) are the opened plan-menu study: seven major ISPs, thirty US cities, 837 thousand street addresses, and no separate limitation sentence on measured throughput was extracted. | Card 1, Nearest studies, item 1 |
| C1-17 | The impact comparison is a target to test later, not a result. No agreement measure, coefficient, sample size, or effect estimate is recorded. | File header; Card 1 has no result numbers |
| C1-18 | The comparison is its own study: it is not a larger New Zealand panel, not a causal model of intergenerational ties, and not a wider literature review. | Card 1, Gap statement |
| C1-19 | Associations between tile speed and survey responses are not causes. The study would not assign a legal breach, a clinical label, or a household identity. | Card 1, Claim boundary |
| C1-20 | Global coverage is stated in the README, and Philippine tiles are not confirmed, so a Philippine transfer is not established by the lead. | Card 1, Dataset lead |
| C1-21 | The opened nearest studies cover US plan menus, a New Zealand online panel, digital-skill clusters in Bulgaria, Finland, and Italy, or a broadband and SDG review. | Card 1, Gap statement; Nearest studies, items 1–4 |
| C1-22 | Both IEEE recent-issue pages opened with HTTP 200, showed only the journal title, and do not pass. Scopus indexing was not confirmed after an expired-certificate failure. | Card 1, Candidate venues; Blocked pages |
| C1-23 | Noncommercial use applies. The opened README contains the words Creative Commons, CC BY, and noncommercial. | Card 1, Social implication; Dataset lead |
| C1-24 | Title and word count 11 are the draft title, unchanged. | Card 1, Draft title |
| C1-25 | The pitch restates the gap, the draft-title technique, and the association boundary. It adds no result. | Card 1, Gap statement; Draft title; Claim boundary |
| C1-26 | A slow tile can still stigmatize a neighborhood. Tiles are about 610.8 meters on a side at the equator. Measurements with GPS-quality locations are averaged per tile. | Card 1, Social implication |
| C1-27 | The design would not re-identify Speedtest users or treat a slow tile as proof that an operator failed a legal duty. | Card 1, Social implication |

## Card 2 — Travel access to published health facilities

### Named user and decision

The named population is residents represented by a Philippines OpenStreetMap health-facility extract. The recorded decision is which communities sit farther from a published facility point. The development goal named for this card is SDG 3. No health agency is named as the user.

### Demonstrable artifact

The proposed artifact is a travel-access score from an already published facility-point file and a population denominator, stopping at that score. Two-step floating catchment area is the technique named in the draft title. No model was fit. The dataset lead is Philippines Health Facilities (OpenStreetMap Export), Humanitarian OpenStreetMap Team, on HDX. The opened URL is `https://data.humdata.org/dataset/hotosm_phl_health_facilities`. The documented unit is a facility point. The opened page lists `hotosm_phl_health_facilities_points_shp.zip` (ESRI Shapefile) and `hotosm_phl_health_facilities_points_geojson.zip` (GeoJSON), and a download label of 633.8K. Philippine rows are known for this extract: the extract is the Philippines. The page attributes OpenStreetMap contributors. A full license deed was not in the extracted text. The file was not downloaded. The gap statement names a population denominator, and no population-denominator file, unit, or URL was opened. The recorded subdomain is statistical modeling.

### One-sentence innovation

The candidate study scores travel access from an already published facility-point file and a population denominator and then stops, which is separate from the discussion limitation in Namadi, Chen, and Niemeier (2025), who score Maryland hospital access with Alzheimer’s diagnoses, deaths, and bed counts and write that specialized ADRD units or the number of ADRD experts in each hospital could enhance that research.

### Measurable impact against a baseline

The impact figure is a target to test later, not a result. The gap card does not name a numeric baseline, a catchment radius, or a computed access score. The social-implication decision, which communities sit farther from a published facility point, is the comparison the later score would inform. The gap statement records the stops: the study does not decide where to build a facility, does not scrape appointment pages, and does not infer who is sick. Distance to a published facility is not a cause of illness and is not a diagnosis. The Namadi study’s diagnosis and mortality results are not the proposed outcome. The study would not infer an individual health status, including for a minor, and would not assign a clinical shortage from the map alone.

### Transfer or scale

The facility extract is the Philippines, so the point file is a Philippine lead. The population denominator required by the gap statement was not opened, so the score cannot be produced from the facility file alone. The opened nearest studies place or upgrade facilities in Ethiopia, illustrate accessibility scores with scraped Milan emergency-department pages, or score Maryland hospital access. Scraping is not proposed. IEEE Access and IEEE Transactions on Intelligent Transportation Systems are the same recent-issue pages as Card 1: both opened, both showed only the journal title, and neither passes. Scopus indexing was not confirmed. The download label 633.8K is a page label, not a counted facility analysis.

### Title

Measuring Facility Travel Access for Philippine Residents Using Two-Step Floating Catchment Area.

Word count: 12.

### Pitch

Opened studies site facilities, scrape appointment pages, or score hospitals with clinical counts. This proposal would score travel access from a published Philippine facility file and a population denominator, then stop.

Word count: 31.

### Ethics line

Facility coordinates can expose small clinics, and a map can be misread as a disease label or a clinical shortage; the design would use published points only, attach no patient records, infer no individual health status, including for a minor, and issue no staffing order.

### Claim map

| Claim | Factual sentence | Gap-card section |
| --- | --- | --- |
| C2-01 | The named population is residents represented by a Philippines OpenStreetMap health-facility extract. | Card 2, Social implication |
| C2-02 | The recorded decision is which communities sit farther from a published facility point. | Card 2, Social implication |
| C2-03 | The development goal named for this card is SDG 3. | Card 2, Social implication |
| C2-04 | No health agency is named as the user. | Card 2, Social implication (no office is named there) |
| C2-05 | The proposed artifact scores travel access from an already published facility-point file and a population denominator, and it stops there. | Card 2, Gap statement |
| C2-06 | Two-step floating catchment area is the technique named in the draft title. No model was fit. | Card 2, Draft title; file header |
| C2-07 | The dataset lead is the HOTOSM Philippines health-facilities extract on HDX, and the official URL was opened. | Card 2, Dataset lead |
| C2-08 | The unit is a facility point. The page lists the shapefile and GeoJSON zip names and a download label of 633.8K. | Card 2, Dataset lead |
| C2-09 | Philippine rows are known: the extract is the Philippines. | Card 2, Dataset lead |
| C2-10 | The page attributes OpenStreetMap contributors. A full license deed was not in the extracted text. The file was not downloaded. | Card 2, Dataset lead |
| C2-11 | A population denominator is named in the gap statement. No denominator file, unit, or URL was opened, so the score cannot be produced from the facility file alone. | Card 2, Gap statement; Dataset lead |
| C2-12 | The recorded subdomain is statistical modeling. | Card 2, Subdomain |
| C2-13 | The innovation points to Namadi, Chen, and Niemeier (2025): Maryland hospital access scored with Alzheimer’s diagnoses, deaths, and bed counts, with a discussion limitation on specialized ADRD units or ADRD expert counts. The candidate study does not take that clinical extension. | Card 2, Nearest studies, item 1; Gap statement; Social implication |
| C2-14 | No numeric baseline, catchment radius, or computed access score is recorded. The farther-from-a-published-point decision is a later target, not a result. | Card 2, Social implication; file header |
| C2-15 | The study does not decide where to build a facility, does not scrape appointment pages, and does not infer who is sick. | Card 2, Gap statement |
| C2-16 | Distance to a published facility is not a cause of illness and is not a diagnosis. The study would not infer an individual health status, including for a minor, and would not assign a clinical shortage from the map alone. | Card 2, Claim boundary |
| C2-17 | The Namadi study’s diagnosis and mortality results are not the proposed outcome. | Card 2, Social implication |
| C2-18 | The facility extract is the Philippines. Ethiopia, Milan, and Maryland are the places in the opened nearest studies. The Milan illustration was web-scraped, and scraping is not proposed. | Card 2, Dataset lead; Gap statement; Nearest studies, item 4 |
| C2-19 | The same two IEEE pages do not pass. Scopus indexing was not confirmed. | Card 2, Candidate venues |
| C2-20 | The 633.8K download label is a page label, not a counted analysis file. | Card 2, Dataset lead |
| C2-21 | Title and word count 12 are the draft title, unchanged. | Card 2, Draft title |
| C2-22 | The pitch restates the gap statement and the stop rule. It adds no result. | Card 2, Gap statement |
| C2-23 | Facility coordinates can expose small clinics. The design would not attach patient records, infer who is sick, label a community with a disease, or treat the map as a clinical shortage diagnosis or a staffing order. | Card 2, Social implication; Claim boundary |

## Card 3 — Fatal versus all-collision hotspot sets

### Named user and decision

The named population is road users in the city or county whose crash file is used. That city or county is not fixed in this card, because no passing crash-record file was opened. The recorded decision is whether a fatal-only hotspot list and an all-collision hotspot list would change which sites are reviewed. The development goal named for this card is SDG 3.6, the traffic-death target named in the opened Alsaleh paper. No road agency is named as the user.

### Demonstrable artifact

The proposed artifact is a sensitivity test of the hotspot definition: a Getis-Ord Gi* set from one crash table limited to fatal records, the Getis-Ord Gi* set from all collisions in that same table, and the overlap of the two sets. No model was fit. This card has no passing dataset lead. The UK page `https://www.data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-safety-data` opened with HTTP 200, and the visible title was "Road Safety Data - National Data Library". The extracted body was a cookie notice, so unit, license, and Philippine rows were not documented. That page does not pass. Montgomery County and Dubai Pulse are named inside opened papers. Those portal pages were not opened, and both are single jurisdictions. No public MMDA file was opened, and MMDA was not contacted. The recorded subdomain is statistical modeling. Without a passing crash file, the overlap cannot be computed from this record.

### One-sentence innovation

The candidate study holds the geography fixed and asks whether a Getis-Ord Gi* set changes when the same crash table is limited to fatal records rather than all collisions, then reports the overlap of the two sets, which the gap card separates from the later work Alsaleh and colleagues (2026) name for other Dubai collision categories and for speed or volume variables.

### Measurable impact against a baseline

The impact figure is a target to test later, not a result: the overlap between the fatal-only Getis-Ord Gi* set and the all-collision Getis-Ord Gi* set. The all-collision set is the comparison set named in the gap statement. No overlap value is recorded, and no passing crash-record file is available to compute one. The gap statement records that this is a sensitivity test of the hotspot definition. It is not a request for more Dubai categories, and it is not a finding of negligence. Overlap of two hotspot sets is not a cause of crashes and is not a legal finding. The study would not label a driver, a child, or a crash as a crime.

### Transfer or scale

The opened hotspot studies rank or forecast crashes inside Montgomery County, six Wisconsin counties, Dubai, one North Carolina highway segment, or a systemic screen whose transfer depends on local crash and road-inventory files. Reyya and Cheng (2024), in the opened conclusions, tie transfer to crash data quality, coverage of road inventory data, crash density, and the significance of the selected contributing factors. Montgomery County and Dubai, as named in the dataset lead, are single jurisdictions, and their portals were not opened. No Philippine crash file passed. IEEE Access and IEEE Transactions on Intelligent Transportation Systems are the same recent-issue pages as Card 1: both opened, both title-only, and neither passes. Scopus indexing was not confirmed.

### Title

Comparing Fatal and All-Crash Hotspots for Road Users Using Getis-Ord Gi*.

Word count: 11.

### Pitch

Opened studies rank or forecast local crash hotspots. A later Getis-Ord Gi* test would compare fatal-only and all-collision sets on one table and report overlap once a crash file passes.

Word count: 30.

### Ethics line

Precise crash coordinates can identify a household or a victim, and a hotspot label can stigmatize a neighborhood; the design would not publish identifiable crash points and would not treat the overlap as negligence, fault, or a crime label for a driver, a child, or a crash.

### Claim map

| Claim | Factual sentence | Gap-card section |
| --- | --- | --- |
| C3-01 | The named population is road users in the city or county whose crash file is used. | Card 3, Social implication |
| C3-02 | No passing crash-record file was opened, so the city or county is not fixed. | Card 3, Dataset lead |
| C3-03 | The recorded decision is whether a fatal-only hotspot list and an all-collision hotspot list would change which sites are reviewed. | Card 3, Social implication |
| C3-04 | The development goal named for this card is SDG 3.6, the traffic-death target named in the opened Alsaleh paper. | Card 3, Social implication |
| C3-05 | No road agency is named as the user. | Card 3, Social implication (no office is named there) |
| C3-06 | The proposed artifact holds geography fixed, compares a Getis-Ord Gi* set for fatal records with a Getis-Ord Gi* set for all collisions on the same crash table, and reports the overlap. | Card 3, Gap statement; Draft title |
| C3-07 | No model was fit. | File header |
| C3-08 | This card has no passing dataset lead. | Card 3, Dataset lead |
| C3-09 | The UK road-safety page opened with HTTP 200, showed the title "Road Safety Data - National Data Library", and the extracted body was a cookie notice, so unit, license, and Philippine rows were not documented. It does not pass. | Card 3, Dataset lead |
| C3-10 | Montgomery County and Dubai Pulse are named inside opened papers. Those portal pages were not opened, and both are single jurisdictions. | Card 3, Dataset lead |
| C3-11 | No public MMDA file was opened, and MMDA was not contacted. | Card 3, Dataset lead |
| C3-12 | The recorded subdomain is statistical modeling. | Card 3, Subdomain |
| C3-13 | The innovation points to Alsaleh and colleagues (2026), who leave other Dubai collision categories and speed or volume variables for later work. The candidate study is the fatal-versus-all-collision overlap test. | Card 3, Gap statement; Nearest studies, item 3 |
| C3-14 | The overlap is a target to test later. No overlap value is recorded, and without a passing crash file it cannot be computed from this record. | Card 3, Gap statement; file header; Dataset lead |
| C3-15 | The test is a sensitivity test of the hotspot definition. It is not a request for more Dubai categories, and it is not a finding of negligence. | Card 3, Gap statement |
| C3-16 | Overlap of two hotspot sets is not a cause of crashes and is not a legal finding. The study would not label a driver, a child, or a crash as a crime. | Card 3, Claim boundary |
| C3-17 | Opened hotspot studies cover Montgomery County, six Wisconsin counties, Dubai, one North Carolina highway segment, or a systemic screen. | Card 3, Gap statement |
| C3-18 | Reyya and Cheng (2024) state that transfer depends on crash data quality, road-inventory coverage, crash density, and the significance of the selected contributing factors. | Card 3, Nearest studies, item 5 |
| C3-19 | The same two IEEE pages do not pass. Scopus indexing was not confirmed. | Card 3, Candidate venues |
| C3-20 | Title and word count 11 are the draft title, unchanged. | Card 3, Draft title |
| C3-21 | The pitch restates the gap and the missing passing crash file. It adds no result. | Card 3, Gap statement; Dataset lead |
| C3-22 | Precise coordinates can identify a household or a victim. A hotspot label can stigmatize a neighborhood. The design would not publish identifiable crash points or use the map as evidence of negligence or fault. | Card 3, Social implication |

## Unresolved inputs

- IEEE Access and IEEE Transactions on Intelligent Transportation Systems recent-issue pages returned HTTP 200 and the journal title only. Neither venue passes on cards 1, 2, or 3. The Scopus source page `https://www.scopus.com/sourceid/21100374601` failed on an expired certificate. Indexing of comparable 2022–2026 studies was not confirmed. `https://ieeeaccess.ieee.org/` also failed certificate verification.
- Ookla Philippine rows were not confirmed. The word Philippines does not appear in the opened README. Global coverage is stated. The AWS open-data registry named in the README was not opened. The dataset was not downloaded. The arXiv Ookla query returned 0, which the gap file treats as an empty output for that query, not as proof that no Ookla study exists outside it.
- The README license words recorded in the gap file are Creative Commons, CC BY, and noncommercial. A full license name and version were not extracted there. Noncommercial use is the recorded limit.
- Geographically weighted regression appears in the card 1 draft title. The gap statement does not specify the outcome coding, covariates, bandwidth, or kernel. The draft title’s phrase "Urban Residents" is not matched by a confirmed urban-only or Philippine tile subset.
- Paul and colleagues (2023): no separate limitation sentence on measured throughput was extracted. Pacheco (2024): the journal site was not opened; *Media Peripheries* 18(1): 38–56 and the date 14 February 2024 are as printed in the PDF. Osoro and Oughton (2024) and Failli, Arpino, and Marino (2023) are preprints in the gap file. Their quoted limitations are a wider review and a causal intergenerational question, and the gap statement keeps the tile comparison separate from both.
- Card 2 names a population denominator and does not record a denominator file, unit, or URL. Two-step floating catchment area has no catchment radius in the gap file. The HOTOSM full license deed was not in the extracted text. The file was not downloaded. The 633.8K label was not verified as a facility count.
- Trabelsi and colleagues (2026) and Choo and colleagues (2025): no future-work sentence was extracted from the opened conclusion or problem-statement blocks. Arbia and colleagues (2024): the opened passage says the Milan emergency-department illustration was web-scraped. Scraping stays out.
- Card 3 has no passing crash-record lead. The UK road-safety extract was a cookie notice. Montgomery County and Dubai Pulse portals were not opened. No public MMDA file was opened, and MMDA was not contacted. `https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars` returned HTTP 403. Overlap cannot be computed until a crash file with a documented unit is opened.
- OpenAlex review and article calls hung with no captured output. They are not empty results. A repeat article filter returned 9452 hits; the first five were off topic and were not used as nearest studies.
- No nighttime-radiance card was written. The nighttime-lights query did not return LGU or VIIRS forecasting studies. Listed VIIRS arXiv hits were not opened. The opened EOG page is a radiance grid, not an LGU-month file.
- Studies and pages left outside the cards remain unverified leads or blocked pages: Yuan and colleagues (publisher DOI HTTP 403), Ahmmed and colleagues (ResearchGate DOI HTTP 403), the Relative Wealth Index page (title only; unit and Philippine rows not visible), and Google Open Buildings (Philippines not named in the extracted text; Earth Engine is out). `https://data.humdata.org/dataset/hotosm_health_facilities` and `https://data.humdata.org/dataset/healthsites` returned HTTP 404.
- This writing pass did not re-resolve DOIs or reopen PDFs or HTML. Author-year strings, locators, and quotations in the gap file are not independently verified here.
- No ethics approval, author list, analysis plan, or venue disclosure text is in the gap file. Impact numbers are absent. Every metric above is a target for a later test.
- Hydroponics and diesel were not searched and are outside these cards.
