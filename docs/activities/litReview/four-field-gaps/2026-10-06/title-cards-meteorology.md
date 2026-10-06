# Meteorology title cards

**Status.** Draft cards for a judging panel. The only evidence is `gap-candidates-meteorology.md` in this folder. No new literature was opened in this writing pass. Impact lines are targets to test later.

**Source note.** The gap file states that these are candidate gaps, that it does not claim that a gap is novel, and that no model was fit. It states that bulk GSOD, IBTrACS, and OpenAQ files were not downloaded. The three cards below follow that file in order. Author-year labels and access results are copied from that file and were not re-resolved here.

### Source claim map

| ID | Factual sentence | Gap-card section |
| --- | --- | --- |
| S0-1 | The gap file states that these are candidate gaps, that it does not claim that a gap is novel, and that no model was fit. | File introduction |
| S0-2 | It states that bulk GSOD, IBTrACS, and OpenAQ files were not downloaded. | File introduction |
| S0-3 | Author-year labels and access results are copied from that file and were not re-resolved here. | File introduction (citation-management scripts were not run); writer limit for this pass |

## Card 1. Transferred heat-index exceedance alerts

### Named user and decision

The named user is a warning desk. The gap file names the affected population as outdoor workers and older adults in tropical cities and places SDG 3, Good Health and Well-being, on that line. The decision is whether that desk keeps one heat-index exceedance rule or refits it before issuing alerts in a second city.

### Demonstrable artifact

The candidate artifact is a heat-index exceedance alert fit in a first city and scored on held-out station-hours from a second tropical city. The dataset lead is the opened NOAA Integrated Surface Database, Global Hourly, with station-hour as the documented unit and with temperature and dew point among the elements. The page describes browser access through the NCEI Data Access application and Climate Data Online for subset orders. Philippine rows are not named on that page. The page says coverage is global, with the best spatial coverage in North America, Europe, Australia, and parts of Asia. No bulk ISD file was downloaded. The secondary lead is GSOD, documented in the gap file as a station-day summary. The opened GSOD readme, as recorded in the gap file, describes daily summaries for over 9000 worldwide stations, built from ISD, and does not list Philippine stations by name. The GSOD product HTML page returned HTTP 503. For non-U.S. locations, the readme states that the data or any derived product shall not be provided to other users or be used for the re-export of commercial services. The gap file does not state a heat-index formula or a numeric exceedance cutoff for the candidate alert.

### One-sentence innovation

The study would hold out station-hours from a second tropical city and score a heat-index exceedance alert, fit in the first city, by its false-alert rate against that second city's own climatology, the cross-city check Han and Randall (2026) place outside their analysis.

### Measurable impact against a baseline

The impact line is a target to test later: the false-alert rate of that transferred alert against the second city's own climatology. The gap file states that no model was fit and calls this comparison a target metric. The gap file does not contain a computed false-alert rate for this candidate test. The gap file states that a false-alert rate against climatology is an agreement between an exceedance rule and station observations, that it is not a cause of illness, and that it is not an individual health label.

### Transfer or scale

The transfer is the second-city holdout of an alert fit in the first city. The gap file states that this test is the cross-city check Han and Randall place outside their analysis, and that it is not the Freiburg UTCI maps, the Australian grid-sensitivity question, or the Indonesian forecaster survey. Scale to Philippine stations is unresolved because Philippine rows are not named on the opened ISD page and Philippine stations are not listed by name in the GSOD readme. Scopus sources returned HTTP 403. Indexing of Current Environmental Health Reports and International Journal of Disaster Risk Science was not confirmed. Those venues do not pass the index check. The unverified Chua and coauthors Philippine heat-index preprint was not used as a nearest study.

### Title

Scoring transferred heat-index exceedance alerts for tropical cities Using random forest

Word count: 11.

The draft title already matches the form "[action] [outcome] for [context or user] Using [named technique]." The technique name random forest is taken from that draft title. The gap statement names the false-alert test and does not name random forest.

### Pitch

Opened studies score heat warnings inside one service area. A warning desk would fit a heat-index exceedance alert in one tropical city and score its false-alert rate on a second city's station-hours.

Word count: 32.

### Ethics line

The main risk to outdoor workers and older adults is that a false alert can mark a district as unsafe and spend response effort, and that a missed alert leaves outdoor workers without the warning. The design limits that risk by scoring station observations, which are not household records, and by leaving those observations unjoined to illness reports. The gap file states that an alert is not a diagnosis of any person. Non-U.S. GSOD rows stay under the opened readme limit: the data or any derived product shall not be provided to other users or be used for the re-export of commercial services.

### Claim map

| ID | Factual sentence | Gap-card section |
| --- | --- | --- |
| C1-01 | The named user is a warning desk. | Social implication |
| C1-02 | The gap file names the affected population as outdoor workers and older adults in tropical cities and places SDG 3, Good Health and Well-being, on that line. | Social implication |
| C1-03 | The decision is whether that desk keeps one heat-index exceedance rule or refits it before issuing alerts in a second city. | Social implication |
| C1-04 | The candidate artifact is a heat-index exceedance alert fit in a first city and scored on held-out station-hours from a second tropical city. | Gap statement |
| C1-05 | The dataset lead is the opened NOAA Integrated Surface Database, Global Hourly, with station-hour as the documented unit and with temperature and dew point among the elements. | Dataset lead |
| C1-06 | The page describes browser access through the NCEI Data Access application and Climate Data Online for subset orders. | Dataset lead |
| C1-07 | Philippine rows are not named on that page. | Dataset lead |
| C1-08 | The page says coverage is global, with the best spatial coverage in North America, Europe, Australia, and parts of Asia. | Dataset lead |
| C1-09 | No bulk ISD file was downloaded. | Dataset lead; file introduction (bulk GSOD not downloaded) |
| C1-10 | The secondary lead is GSOD, documented in the gap file as a station-day summary. | Dataset lead |
| C1-11 | The opened GSOD readme, as recorded in the gap file, describes daily summaries for over 9000 worldwide stations, built from ISD, and does not list Philippine stations by name. | Dataset lead |
| C1-12 | The GSOD product HTML page returned HTTP 503. | Dataset lead; Blocked or incomplete pages |
| C1-13 | For non-U.S. locations, the readme states that the data or any derived product shall not be provided to other users or be used for the re-export of commercial services. | Dataset lead; Social implication |
| C1-14 | The gap file does not state a heat-index formula or a numeric exceedance cutoff for the candidate alert. | Dataset lead (elements named; no formula recorded); writer limit |
| C1-15 | The study would hold out station-hours from a second tropical city and score a heat-index exceedance alert, fit in the first city, by its false-alert rate against that second city's own climatology, the cross-city check Han and Randall (2026) place outside their analysis. | Gap statement; Nearest studies, Han and Randall (2026), HTML full text |
| C1-16 | The impact line is a target to test later: the false-alert rate of that transferred alert against the second city's own climatology. | Gap statement; Brief (impact metrics are targets) |
| C1-17 | The gap file states that no model was fit and calls this comparison a target metric. | File introduction; Gap statement |
| C1-18 | The gap file does not contain a computed false-alert rate for this candidate test. | File introduction; Gap statement |
| C1-19 | The gap file states that a false-alert rate against climatology is an agreement between an exceedance rule and station observations, that it is not a cause of illness, and that it is not an individual health label. | Claim boundary |
| C1-20 | The transfer is the second-city holdout of an alert fit in the first city. | Gap statement |
| C1-21 | The gap file states that this test is the cross-city check Han and Randall place outside their analysis, and that it is not the Freiburg UTCI maps, the Australian grid-sensitivity question, or the Indonesian forecaster survey. | Gap statement |
| C1-22 | Scale to Philippine stations is unresolved because Philippine rows are not named on the opened ISD page and Philippine stations are not listed by name in the GSOD readme. | Dataset lead |
| C1-23 | Scopus sources returned HTTP 403. | Candidate venues; Blocked or incomplete pages |
| C1-24 | Indexing of Current Environmental Health Reports and International Journal of Disaster Risk Science was not confirmed. | Candidate venues |
| C1-25 | Those venues do not pass the index check. | Candidate venues |
| C1-26 | The unverified Chua and coauthors Philippine heat-index preprint was not used as a nearest study. | Unverified leads |
| C1-27 | The draft title already matches the form "[action] [outcome] for [context or user] Using [named technique]." | Draft title; Brief |
| C1-27a | The technique name random forest is taken from that draft title. | Draft title |
| C1-28 | The gap statement names the false-alert test and does not name random forest. | Gap statement; Draft title |
| C1-29 | Opened studies score heat warnings inside one service area. | Gap statement |
| C1-29a | A warning desk would fit a heat-index exceedance alert in one tropical city and score its false-alert rate on a second city's station-hours. | Gap statement; Social implication |
| C1-30 | The main risk to outdoor workers and older adults is that a false alert can mark a district as unsafe and spend response effort, and that a missed alert leaves outdoor workers without the warning. | Social implication |
| C1-31 | The design limits that risk by scoring station observations, which are not household records, and by leaving those observations unjoined to illness reports. | Social implication |
| C1-32 | The gap file states that an alert is not a diagnosis of any person. | Social implication |
| C1-33 | Non-U.S. GSOD rows stay under the opened readme limit: the data or any derived product shall not be provided to other users or be used for the re-export of commercial services. | Social implication; Dataset lead |

## Card 2. Pre-landfall rapid intensification

### Named user and decision

The named user is a forecast desk. The gap file names the affected population as coastal residents in basins where tropical cyclones make landfall and places SDG 13, Climate Action, on that line. The decision is whether that desk adds a pre-landfall rapid-intensification flag next to existing guidance.

### Demonstrable artifact

The candidate artifact is a gradient-boosting classifier kept to storm-times inside a stated window before landfall, using public best-track records, and compared with a SHIPS-style baseline on probability of detection and false-alarm ratio. The dataset lead is the opened IBTrACS page. The gap file records that the page calls IBTrACS the most complete global collection of tropical cyclones and a publicly available best-track dataset, with CSV, netCDF, and shapefile access. The documented unit is storm-time, as a best-track record. The opened product page does not state the reporting interval. Philippine rows are not named. The page describes a global multi-agency archive. No bulk IBTrACS file was downloaded. The SHIPS developmental-data pages tried on the gap-file run did not open, and they are not the dataset lead. The gap file does not state the length of the pre-landfall window, and the IBTrACS dataset lead does not describe a landfall indicator.

### One-sentence innovation

The study would keep only storm-times inside a stated window before landfall, a restriction for which the opened Kim et al. (2024) western North Pacific HTML contains no landfall token and names IBTrACS v04r00 as the track source, and would compare a gradient-boosting classifier with a SHIPS-style baseline on probability of detection and false-alarm ratio.

### Measurable impact against a baseline

The impact line is a target to test later: probability of detection and false-alarm ratio for that pre-landfall classifier against a SHIPS-style baseline. The gap file states that no model was fit. The gap file does not contain a computed probability of detection or false-alarm ratio for this candidate comparison. The gap file states that a pre-landfall probability of detection or false-alarm ratio is an association between predictors and a later intensity change on past tracks, that it is not a cause of damage, and that it is not evidence that a forecast prevented harm.

### Transfer or scale

The opened studies named on this card classify or forecast rapid intensification for a whole basin sample. The opened FAST-ML HTML, recorded as a preprint, treats near-landfall timing as motivation and names ensemble calibration as future work. The gap file records Kim et al. with OpenAlex publication year 2024 and an opened HTML banner that reads "Volume 10 - 2023." Chih et al. (2026) was opened as a publisher abstract only because the article HTML did not include the body. Wu et al. (2025) and Bhowmick (2025) were opened as OpenAlex abstracts only, and this card does not use their reported scores as the candidate baseline. Unverified cyclone leads, including the Bay of Bengal landfall record with an empty OpenAlex abstract, were not used as nearest studies. Philippine rows are not named on the opened IBTrACS page, so a Philippine storm subset is unresolved. Scopus sources returned HTTP 403. IEEE Xplore recent-issue pages for IEEE Transactions on Geoscience and Remote Sensing and IEEE Transactions on Network Science and Engineering returned HTTP 200 with a bot-check body, so the issue lists were not read. Indexing was not confirmed. Frontiers in Marine Science and npj Climate and Atmospheric Science do not pass the index check in the gap file.

### Title

Classifying pre-landfall rapid intensification for tropical cyclones Using gradient boosting

Word count: 10.

The draft title already matches the required form. Gradient boosting is named in the gap statement as the candidate classifier.

### Pitch

Studies in this set classify rapid intensification on whole-basin samples. A forecast desk would keep only pre-landfall storm-times and compare gradient boosting with a SHIPS-style baseline on detection and false-alarm ratio.

Word count: 31.

### Ethics line

The main risk to coastal residents is that a false flag can trigger costly movement of people, and that a miss leaves a coastal community with a weaker intensity cue. The design limits that risk by reporting a skill score on past tracks and by keeping best-track records, which are not personal data, as the evidence base. The gap file states that the candidate result would not show that a model saved lives or prevented damage, and that using the flag as a certain damage forecast would misuse a probabilistic label.

### Claim map

| ID | Factual sentence | Gap-card section |
| --- | --- | --- |
| C2-01 | The named user is a forecast desk. | Social implication |
| C2-02 | The gap file names the affected population as coastal residents in basins where tropical cyclones make landfall and places SDG 13, Climate Action, on that line. | Social implication |
| C2-03 | The decision is whether that desk adds a pre-landfall rapid-intensification flag next to existing guidance. | Social implication |
| C2-04 | The candidate artifact is a gradient-boosting classifier kept to storm-times inside a stated window before landfall, using public best-track records, and compared with a SHIPS-style baseline on probability of detection and false-alarm ratio. | Gap statement |
| C2-05 | The dataset lead is the opened IBTrACS page. | Dataset lead |
| C2-06 | The gap file records that the page calls IBTrACS the most complete global collection of tropical cyclones and a publicly available best-track dataset, with CSV, netCDF, and shapefile access. | Dataset lead |
| C2-07 | The documented unit is storm-time, as a best-track record. | Dataset lead |
| C2-08 | The opened product page does not state the reporting interval. | Dataset lead |
| C2-09 | Philippine rows are not named. | Dataset lead |
| C2-10 | The page describes a global multi-agency archive. | Dataset lead |
| C2-11 | No bulk IBTrACS file was downloaded. | Dataset lead; file introduction |
| C2-12 | The SHIPS developmental-data pages tried on the gap-file run did not open, and they are not the dataset lead. | Dataset lead; Unverified leads |
| C2-13 | The gap file does not state the length of the pre-landfall window, and the IBTrACS dataset lead does not describe a landfall indicator. | Gap statement; Dataset lead; writer limit |
| C2-14 | The study would keep only storm-times inside a stated window before landfall, a restriction for which the opened Kim et al. (2024) western North Pacific HTML contains no landfall token and names IBTrACS v04r00 as the track source, and would compare a gradient-boosting classifier with a SHIPS-style baseline on probability of detection and false-alarm ratio. | Gap statement; Nearest studies, Kim et al. |
| C2-15 | The impact line is a target to test later: probability of detection and false-alarm ratio for that pre-landfall classifier against a SHIPS-style baseline. | Gap statement; Brief |
| C2-16 | The gap file states that no model was fit. | File introduction |
| C2-17 | The gap file does not contain a computed probability of detection or false-alarm ratio for this candidate comparison. | File introduction; Gap statement |
| C2-18 | The gap file states that a pre-landfall probability of detection or false-alarm ratio is an association between predictors and a later intensity change on past tracks, that it is not a cause of damage, and that it is not evidence that a forecast prevented harm. | Claim boundary |
| C2-19 | The opened studies named on this card classify or forecast rapid intensification for a whole basin sample. | Gap statement |
| C2-20 | The opened FAST-ML HTML, recorded as a preprint, treats near-landfall timing as motivation and names ensemble calibration as future work. | Gap statement; Nearest studies, Xiao et al. (FAST-ML) |
| C2-21 | The gap file records Kim et al. with OpenAlex publication year 2024 and an opened HTML banner that reads "Volume 10 - 2023." | Nearest studies, Kim et al. |
| C2-22 | Chih et al. (2026) was opened as a publisher abstract only because the article HTML did not include the body. | Nearest studies, Chih et al.; Blocked or incomplete pages |
| C2-23 | Wu et al. (2025) and Bhowmick (2025) were opened as OpenAlex abstracts only, and this card does not use their reported scores as the candidate baseline. | Nearest studies, Wu et al. and Bhowmick |
| C2-24 | Unverified cyclone leads, including the Bay of Bengal landfall record with an empty OpenAlex abstract, were not used as nearest studies. | Unverified leads |
| C2-25 | Philippine rows are not named on the opened IBTrACS page, so a Philippine storm subset is unresolved. | Dataset lead |
| C2-26 | Scopus sources returned HTTP 403. | Candidate venues; Blocked or incomplete pages |
| C2-27 | IEEE Xplore recent-issue pages for IEEE Transactions on Geoscience and Remote Sensing and IEEE Transactions on Network Science and Engineering returned HTTP 200 with a bot-check body, so the issue lists were not read. | Candidate venues; Blocked or incomplete pages |
| C2-28 | Indexing was not confirmed. | Candidate venues |
| C2-29 | Frontiers in Marine Science and npj Climate and Atmospheric Science do not pass the index check in the gap file. | Candidate venues |
| C2-30 | The draft title already matches the required form. | Draft title; Brief |
| C2-30a | Gradient boosting is named in the gap statement as the candidate classifier. | Gap statement; Draft title |
| C2-31 | Studies in this set classify rapid intensification on whole-basin samples. | Gap statement |
| C2-31a | A forecast desk would keep only pre-landfall storm-times and compare gradient boosting with a SHIPS-style baseline on detection and false-alarm ratio. | Gap statement; Social implication |
| C2-32 | The main risk to coastal residents is that a false flag can trigger costly movement of people, and that a miss leaves a coastal community with a weaker intensity cue. | Social implication |
| C2-33 | The design limits that risk by reporting a skill score on past tracks and by keeping best-track records, which are not personal data, as the evidence base. | Social implication |
| C2-34 | The gap file states that the candidate result would not show that a model saved lives or prevented damage, and that using the flag as a certain damage forecast would misuse a probabilistic label. | Social implication |

## Card 3. Sensor-hour anomaly flags

### Named user and decision

The named user is a network operator. The gap file names the affected population as residents near outdoor air-quality sensors in cities that contribute to a public archive and places SDG 11, Sustainable Cities and Communities, on that line. The decision is whether that operator withholds a sensor-hour from a public map.

### Demonstrable artifact

The candidate artifact is one detector applied to sensor-hours from a public multi-country archive, scored for false alerts against that archive's own quality flags, then scored again on a second country's sensors. The dataset lead is the opened OpenAQ documentation page. The gap file records that the page says the data are publicly available and that users must comply with third-party terms. The docs menu lists an API key, rate limits, and "Get measurements aggregated to hours by sensor ID" plus "Get precomputed hourly measurements by sensor ID". The documented unit is sensor-hour. Philippine rows are not named. The openaq.org home page returned a connection reset. A bulk CSV download page was not opened. The gap file describes this lead as an API path with a key, free-registration style access in the docs, and not a confirmed one-click bulk file. No measurements were downloaded. The OpenAQ dataset lead does not name a quality-flag column. The comparison with the archive's own quality flags remains a target to test.

### One-sentence innovation

The study would score one detector's false alerts against a public archive's own quality flags and repeat that score on a second country's sensors, a transfer score the opened García et al. (2025) review does not report when it identifies data quality as a research gap.

### Measurable impact against a baseline

The impact line is a target to test later: that false-alert rate against the archive's own quality flags, repeated on a second country. The gap file states that no model was fit. The gap file does not contain a computed false-alert rate for this candidate detector. The gap file states that a false-alert rate against an archive flag is an agreement between a detector and the archive's own label, that it does not show the cause of a pollutant level, and that it does not support a health or legal label for a person or a facility from the sensor reading alone.

### Transfer or scale

The transfer is the repeat score on a second country's sensors, which the opened García review does not report. The opened Okorn and Iraci HTML states geographic coverage gaps, including the Global South and rural areas, and, for one category of networks, a live map without a historical download or a public calibration explanation found by those authors. That Okorn statement is separate from the OpenAQ access limit on this card. Allka et al. (2024) and Rollo, Bachechi, and Po (2023) were opened as OpenAlex abstracts only. The Allka abstract does not name the monitoring network. The García PDF cites a 2015 OpenAQ platform paper that was not opened. Philippine rows are not named on the opened OpenAQ page, so a Philippine sensor subset is unresolved. Scopus sources returned HTTP 403. The IEEE Xplore page for IEEE Transactions on Network Science and Engineering returned the journal title and a bot-check body, so the issue list was not read. Indexing was not confirmed. Atmospheric Measurement Techniques and Artificial Intelligence Review do not pass the index check in the gap file.

### Title

Detecting hourly air-quality sensor anomalies for public monitors Using isolation forest

Word count: 11.

The draft title already matches the required form. The technique name isolation forest is taken from that draft title. The gap statement says "one detector" and does not name isolation forest.

### Pitch

A review names data quality as a gap and reports no transfer score. An operator would score one detector against the archive's quality flags, then repeat that score on a second country.

Word count: 32.

### Ethics line

The main risk to residents near the sensors is that a false anomaly flag can stigmatize a neighborhood as polluted, and that a flag trusted too quickly can hide a real exceedance. The design limits that risk by scoring the detector against the archive's own quality flags. The opened OpenAQ page does not say the sensors are inside homes, and the gap file states that a household sensor would add a privacy risk. The gap file states that a sensor fault is not a legal emissions finding and is not a diagnosis of a person.

### Claim map

| ID | Factual sentence | Gap-card section |
| --- | --- | --- |
| C3-01 | The named user is a network operator. | Social implication |
| C3-02 | The gap file names the affected population as residents near outdoor air-quality sensors in cities that contribute to a public archive and places SDG 11, Sustainable Cities and Communities, on that line. | Social implication |
| C3-03 | The decision is whether that operator withholds a sensor-hour from a public map. | Social implication |
| C3-04 | The candidate artifact is one detector applied to sensor-hours from a public multi-country archive, scored for false alerts against that archive's own quality flags, then scored again on a second country's sensors. | Gap statement |
| C3-05 | The dataset lead is the opened OpenAQ documentation page. | Dataset lead |
| C3-06 | The gap file records that the page says the data are publicly available and that users must comply with third-party terms. | Dataset lead |
| C3-07 | The docs menu lists an API key, rate limits, and "Get measurements aggregated to hours by sensor ID" plus "Get precomputed hourly measurements by sensor ID". | Dataset lead |
| C3-08 | The documented unit is sensor-hour. | Dataset lead |
| C3-09 | Philippine rows are not named. | Dataset lead |
| C3-10 | The openaq.org home page returned a connection reset. | Dataset lead; Blocked or incomplete pages |
| C3-11 | A bulk CSV download page was not opened. | Dataset lead |
| C3-12 | The gap file describes this lead as an API path with a key, free-registration style access in the docs, and not a confirmed one-click bulk file. | Dataset lead |
| C3-13 | No measurements were downloaded. | Dataset lead |
| C3-14 | The OpenAQ dataset lead does not name a quality-flag column. | Dataset lead; writer limit |
| C3-15 | The comparison with the archive's own quality flags remains a target to test. | Gap statement; Brief |
| C3-16 | The study would score one detector's false alerts against a public archive's own quality flags and repeat that score on a second country's sensors, a transfer score the opened García et al. (2025) review does not report when it identifies data quality as a research gap. | Gap statement; Nearest studies, García et al. |
| C3-17 | The impact line is a target to test later: that false-alert rate against the archive's own quality flags, repeated on a second country. | Gap statement; Brief |
| C3-18 | The gap file states that no model was fit. | File introduction |
| C3-19 | The gap file does not contain a computed false-alert rate for this candidate detector. | File introduction; Gap statement |
| C3-20 | The gap file states that a false-alert rate against an archive flag is an agreement between a detector and the archive's own label, that it does not show the cause of a pollutant level, and that it does not support a health or legal label for a person or a facility from the sensor reading alone. | Claim boundary |
| C3-21 | The transfer is the repeat score on a second country's sensors, which the opened García review does not report. | Gap statement; Nearest studies, García et al. |
| C3-22 | The opened Okorn and Iraci HTML states geographic coverage gaps, including the Global South and rural areas, and, for one category of networks, a live map without a historical download or a public calibration explanation found by those authors. | Nearest studies, Okorn and Iraci |
| C3-23 | That Okorn statement is separate from the OpenAQ access limit on this card. | Nearest studies, Okorn and Iraci; Dataset lead |
| C3-24 | Allka et al. (2024) and Rollo, Bachechi, and Po (2023) were opened as OpenAlex abstracts only. | Nearest studies, Allka et al. and Rollo et al. |
| C3-25 | The Allka abstract does not name the monitoring network. | Nearest studies, Allka et al. |
| C3-26 | The García PDF cites a 2015 OpenAQ platform paper that was not opened. | Nearest studies, García et al.; Unverified leads |
| C3-27 | Philippine rows are not named on the opened OpenAQ page, so a Philippine sensor subset is unresolved. | Dataset lead |
| C3-28 | Scopus sources returned HTTP 403. | Candidate venues; Blocked or incomplete pages |
| C3-29 | The IEEE Xplore page for IEEE Transactions on Network Science and Engineering returned the journal title and a bot-check body, so the issue list was not read. | Candidate venues; Blocked or incomplete pages |
| C3-30 | Indexing was not confirmed. | Candidate venues |
| C3-31 | Atmospheric Measurement Techniques and Artificial Intelligence Review do not pass the index check in the gap file. | Candidate venues |
| C3-31a | The draft title already matches the required form. | Draft title; Brief |
| C3-32 | The technique name isolation forest is taken from that draft title. | Draft title |
| C3-33 | The gap statement says "one detector" and does not name isolation forest. | Gap statement; Draft title |
| C3-34 | A review names data quality as a gap and reports no transfer score. | Gap statement; Nearest studies, García et al. |
| C3-34a | An operator would score one detector against the archive's quality flags, then repeat that score on a second country. | Gap statement; Social implication |
| C3-35 | The main risk to residents near the sensors is that a false anomaly flag can stigmatize a neighborhood as polluted, and that a flag trusted too quickly can hide a real exceedance. | Social implication |
| C3-36 | The design limits that risk by scoring the detector against the archive's own quality flags. | Gap statement; Social implication |
| C3-37 | The opened OpenAQ page does not say the sensors are inside homes, and the gap file states that a household sensor would add a privacy risk. | Social implication |
| C3-38 | The gap file states that a sensor fault is not a legal emissions finding and is not a diagnosis of a person. | Social implication |

## Unresolved inputs

1. Scopus indexing was not confirmed. `https://www.scopus.com/sources` returned HTTP 403. The named venues do not pass the index check in the gap file.
2. IEEE indexing was not confirmed. Recent-issue pages for IEEE Transactions on Geoscience and Remote Sensing (punumber 36) and IEEE Transactions on Network Science and Engineering (punumber 6488902) returned a bot-check body, so the issue lists were not read. Card 1's venues were not checked against IEEE in the gap file.
3. Philippine rows are not named on the opened ISD, GSOD, IBTrACS, or OpenAQ pages. No bulk file was downloaded, so this file does not establish whether Philippine stations or sensors are present.
4. OpenAQ is an API path with a key, rate limits, and hourly endpoints, and it is not a confirmed one-click bulk file. `https://openaq.org/` returned a connection reset. `https://docs.openaq.org/using-the-api/v3` returned HTTP 404. No measurements were downloaded. The dataset lead does not name a quality-flag column.
5. GSOD outside the United States is noncommercial under the opened readme: the data or any derived product shall not be provided to other users or be used for the re-export of commercial services. The GSOD product HTML page returned HTTP 503. Philippine stations are not named in the readme.
6. No model was fit. False-alert rates, probability of detection, and false-alarm ratio are targets to test, not computed results.
7. The first tropical city, the second tropical city, the pre-landfall window length, and the second country are not named. The gap file does not state a heat-index formula or an exceedance cutoff. The IBTrACS lead does not state the reporting interval or describe a landfall indicator.
8. SHIPS developmental-data pages reset the connection and are not a dataset lead, so the predictor file for a SHIPS-style baseline is unresolved.
9. Random forest (card 1) and isolation forest (card 3) are draft-title technique names. Those gap statements do not name the algorithms. Gradient boosting is named in the card 2 gap statement.
10. Kim et al. remain unresolved on year: OpenAlex publication year 2024, opened HTML banner "Volume 10 - 2023."
11. These nearest studies stay abstract-only or blocked and are not the innovation anchors: Chih et al. (publisher abstract only; article body not opened), Wu et al. (OpenAlex abstract only; no limitation sentence), Bhowmick (OpenAlex abstract only; MDPI HTTP 403), Allka et al. (OpenAlex abstract only; UPC PDF failed SSL verification; network not named), and Rollo et al. (OpenAlex abstract only; MDPI HTTP 403; no future-work sentence). Their reported scores are not this file's results.
12. FAST-ML is a preprint. Its opened future-work sentence is ensemble calibration. Loveday and Carroll (2024) are a preprint with no journal reference in the arXiv record, and they are not the card 1 innovation anchor.
13. The 2015 OpenAQ platform paper cited in the opened García PDF was not opened. The Chua and coauthors Philippine heat-index preprint was not used (empty OpenAlex abstract; DOI HTTP 403).
14. ISD best spatial coverage is stated as North America, Europe, Australia, and parts of Asia. A second tropical city's station-hours were not confirmed in a downloaded subset.
15. A numeric count of dropped duplicate DOI rows was not logged. Citation-management scripts were not run. The gap file's Kassis et al. (2026) skills-paper note is not a meteorology nearest study, and this file adds no reference list.
16. No ethics approval, author list, analysis plan, or AI-use declaration is in the gap file. SDG labels are the social-implication lines as written there.
