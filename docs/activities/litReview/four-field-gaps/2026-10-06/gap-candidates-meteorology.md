# Meteorology gap candidates

Generated: 2026-10-06
Review type: scoping
Search window: 2022-01-01 through 2026-10-06
Field: meteorology (tropical heat alerts, tropical-cyclone rapid intensification, air-quality sensor anomalies)
Databases: OpenAlex (literature-search-openalex CLI) and arXiv (literature-search-arxiv CLI)

These are candidate gaps. This file does not claim that a gap is novel. No model was fit. Bulk GSOD, IBTrACS, and OpenAQ files were not downloaded.

Search used the OpenAlex and arXiv command-line tools in their skill directories. Citation-management scripts were not run. Because that skill was part of the required workflow, its current record is noted here from an arXiv `id_list` fetch and an OpenAlex DOI resolution on this run: Kassis, T., Agarwal, V., He, Y., Patel, D., and Brueckner, A. M. (2026). Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents. arXiv:2609.00065. https://doi.org/10.48550/arXiv.2609.00065

## Search log

Date searched: 2026-10-06. OpenAlex filters use `from_publication_date:2022-01-01,to_publication_date:2026-10-06` unless noted. arXiv date filter is `submittedDate:[202201010000 TO 202610062359]`. Result counts are OpenAlex `meta.count` or the arXiv result count before card-level DOI deduplication.

| Database | Date searched | Query | Filters | Results |
| --- | --- | --- | --- | --- |
| OpenAlex | 2026-10-06 | tropical heat index alert | dates above; sort cited_by_count; per-page 8 | 3908 |
| OpenAlex | 2026-10-06 | heat-health warning system | dates above; type:review; per-page 8 | 1069 |
| OpenAlex | 2026-10-06 | heat index exceedance tropical | dates above; per-page 8 | 35551 |
| OpenAlex | 2026-10-06 | rapid intensification tropical cyclone | dates above; type:review; per-page 8 | 155 |
| OpenAlex | 2026-10-06 | predicting rapid intensification tropical cyclone | dates above; per-page 8 | 7392 |
| OpenAlex | 2026-10-06 | air quality sensor anomaly detection | dates above; per-page 8 | 36052 |
| OpenAlex | 2026-10-06 | OpenAQ low-cost sensor | dates above; per-page 8 | 137 |
| OpenAlex | 2026-10-06 | heat health warning tropical cities | dates above; per-page 8 | 7086 |
| OpenAlex | 2026-10-06 | heat warning false alarm heat index | dates above; per-page 8 | 2559 |
| OpenAlex | 2026-10-06 | SHIPS rapid intensification forecast | dates above; per-page 8 | 9113 |
| OpenAlex | 2026-10-06 | rapid intensification landfall prediction | dates above; per-page 8 | 2131 |
| OpenAlex | 2026-10-06 | low-cost air quality sensor review anomaly | dates above; type:review; per-page 8 | 641 |
| OpenAlex | 2026-10-06 | OpenAQ anomaly detection | dates above; per-page 8 | 41 |
| OpenAlex | 2026-10-06 | OpenAQ | dates above; title.search:OpenAQ; per-page 8 | 13 |
| OpenAlex | 2026-10-06 | Statistical Hurricane Intensity Prediction Scheme rapid intensification | dates above; per-page 8 | 1566 |
| OpenAlex | 2026-10-06 | machine learning rapid intensification | dates above; title.search:rapid intensification; per-page 8 | 43 |
| OpenAlex | 2026-10-06 | DOI batch of shortlisted heat, cyclone, and air-quality works | doi filter; per-page 20 | 18 |
| OpenAlex | 2026-10-06 | second DOI batch (Atmosphere, npj, JGR, Theoretical and Applied Climatology, Weather and Forecasting, arXiv heat index, Georgian Geophysical Society) | doi filter; per-page 10 | 8 |
| OpenAlex | 2026-10-06 | FAST-ML and the skills paper | doi:10.48550/arxiv.2609.25505\|10.48550/arxiv.2609.00065 | 2 |
| arXiv | 2026-10-06 | all:heat AND all:index AND all:tropical | submittedDate window; max 8; sort submittedDate descending | 5 |
| arXiv | 2026-10-06 | all:rapid AND all:intensification AND all:cyclone | submittedDate window; max 6; sort submittedDate descending | 6 |
| arXiv | 2026-10-06 | all:anomaly AND all:sensor AND all:air AND all:quality | submittedDate window; max 6; sort submittedDate descending | 4 |
| arXiv | 2026-10-06 | all:heat AND all:warning AND all:health | submittedDate window; max 6; sort submittedDate descending | 4 |
| arXiv | 2026-10-06 | id_list 2609.25505, 2407.10434, 2609.00065 | id lookup | 3 |

An initial OpenAlex call did not return for several minutes. No HTTP 429 body was observed. Later calls in this run completed. The SHIPS-phrase query above matched many ship and cyclone papers that are off topic; it was not used to select nearest studies.

## Inclusion and exclusion

Included when the work was published or posted from 2022-01-01 through 2026-10-06, the DOI or arXiv record was resolved on this run, and an abstract, HTML full text, or PDF full text was opened on this run. The three cards cover heat-index or heat-health warnings, rapid intensification, and air-quality sensor anomalies.

Excluded as off topic from the broad citation-sorted and review queries: the IPCC AR6 synthesis report, COVID-19 excess mortality, chronic wounds, mycorrhizae, cloud-computing energy use, wildlife responses to cyclones, a ship-anchor accident, HVAC attack detection, and indoor aquaculture air data. OpenAlex peer-review records and duplicate software version records were excluded. Hydroponics and diesel were not searched.

The same DOI was kept once when it appeared in more than one query. A numeric count of dropped duplicate rows was not logged.

Preprints are labeled as preprints. An abstract supports only what that abstract states. A citation inside an opened paper was not treated as an opened study.

## Card 1. Transferred heat-index exceedance alerts

**Gap statement.** Opened 2024–2026 studies already score heat warnings, and they do it inside one service area: four separate U.S. city models, Australian district categories, a systematic review of heat-health warning systems, a survey of Indonesian forecasters who use one national temperature anomaly rule, and neighborhood maps for Freiburg. A candidate undergraduate study would hold out station-hours from a second tropical city and score a heat-index exceedance alert, fit in the first city, by its false-alert rate against that second city's own climatology. That test is a study with a target metric. It is the cross-city check Han and Randall place outside their analysis, and it is not the Freiburg UTCI maps, the Australian grid-sensitivity question, or the Indonesian forecaster survey.

**Nearest studies.**

1. Han, Y., and Randall, C. (2026). Machine Learning-Based Prediction of Heat Index in Selected U.S. Cities. Preprint. arXiv:2603.19488. https://doi.org/10.48550/arXiv.2603.19488. Venue: arXiv. Opened: HTML full text. Locator: results discussion. Quote: "It is possible that most southern USA cities would perform very well on the Dallas model or a similar model because of the high humidity levels in the region, but application of existing city models to other cities within their climatology region is outside the scope of our analysis."
2. Loveday, N., and Carroll, M. (2024). Evaluation and statistical correction of area-based heat index forecasts that drive a heatwave warning service. Preprint. arXiv:2407.10434. https://doi.org/10.48550/arXiv.2407.10434. Venue: arXiv. Opened: PDF full text. The arXiv record has no journal reference. Locator: PDF conclusion. Quote: "More research can be done in the future to quantify the impact of using different grids, resolve these tensions, and improve the heatwave forecasts."
3. N, S. V. S. C., and Lee, J. K. W. (2025). A Systematic Review of Heat Health Warning Systems: Enhancing the Framework Towards Effective Health Outcomes. Current Environmental Health Reports, 12, 31. https://doi.org/10.1007/s40572-025-00496-5. Opened: PDF full text. Locator: PDF introduction. Quote: "However, though the evidence indicates that HHWS are effective in reducing mortality, there is a scope to improve HHWS by developing them for local conditions and increasing research on meteorological/climatological aspects of heat waves."
4. Nugroho, Y. A., Raju, E., Putra, A. W., and Marghidan, C. P. (2026). Heat Risk Communication by Operational Meteorologists in Indonesia: Current Operational Challenges and Decision-Making Dilemmas in Heat Early Warning System. International Journal of Disaster Risk Science. https://doi.org/10.1007/s13753-026-00760-8. Opened: PDF full text. Locator: PDF introduction. Quote: "These rapid changes may affect heat early warning systems (HEWS), yet research focused on the operational challenges faced by operational meteorologists (OMs) in issuing heat early warning remains limited."
5. Ludwig, S., Briegel, F., and Christen, A. (2026). Evaluating the potential for heat warning systems to account for intra-urban variability. PLOS Climate, 5(6), e0000941. https://doi.org/10.1371/journal.pclm.0000941. Opened: HTML full text. Locator: HTML discussion. Quote: "This limitation reduces their effectiveness for targeted local action, as they may fail to detect localized heat stress in vulnerable populations."

The opened Ludwig HTML evaluates hourly UTCI maps for Freiburg in June–August 2023. The opened Loveday PDF evaluates the Australian Bureau district heatwave service with the Excess Heat Factor and states that misses and false alarms are penalized equally at a risk threshold of 0.5. The opened Nugroho PDF describes Indonesia's nationwide rule as a daily dry-bulb anomaly of more than 3 °C above the climatological average.

**Candidate venues.** Current Environmental Health Reports (2025 review above) and International Journal of Disaster Risk Science (2026 article above) published warning-system studies at the scale of a review and a national forecaster survey. Scopus sources (https://www.scopus.com/sources) returned HTTP 403 on this run. Indexing not confirmed. These venues do not pass the index check.

**Social implication.** Affected population: outdoor workers and older adults in tropical cities. SDG 3, Good Health and Well-being. Decision: whether a warning desk keeps one heat-index exceedance rule or refits it before issuing alerts in a second city. Harm: a false alert can mark a district as unsafe and spend response effort; a missed alert leaves outdoor workers without the warning. Station observations are not household records; joining them to illness reports would create a privacy risk. The opened GSOD readme forbids commercial re-export of non-U.S. data. An alert is not a diagnosis of any person.

**Draft title.** Scoring transferred heat-index exceedance alerts for tropical cities Using random forest
Word count: 11.

**Subdomain.** predictive analytics

**Dataset lead.** NOAA Integrated Surface Database, Global Hourly. Official page opened: https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database. Documented unit: station-hour. The page describes a global database of hourly and synoptic surface observations, with temperature and dew point among the elements, and browser access through the NCEI Data Access application and Climate Data Online for subset orders. Philippine rows are not named. The page says coverage is global, with the best spatial coverage in North America, Europe, Australia, and parts of Asia. No bulk file was downloaded.

Secondary lead, station-day rather than station-hour: GSOD readme opened at https://www.ncei.noaa.gov/data/global-summary-of-the-day/doc/readme.txt. The readme describes daily summaries for over 9000 worldwide stations, built from ISD, with a web folder at https://www.ncei.noaa.gov/data/global-summary-of-the-day/. For non-U.S. locations it says the data or any derived product shall not be provided to other users or be used for the re-export of commercial services. The GSOD product HTML page returned HTTP 503. Philippine stations are not listed by name in the readme.

**Claim boundary.** A false-alert rate against climatology is an agreement between an exceedance rule and station observations. It is not a cause of illness, and it is not an individual health label.

## Card 2. Pre-landfall rapid intensification

**Gap statement.** Opened 2024–2026 studies classify or forecast rapid intensification for a whole basin sample: western North Pacific cases with a net-energy predictor, a physics-machine-learning intensity model, a western North Pacific continuous intensification index, North Atlantic SHIPS predictors plus hourly cloud cover, and Southwest Pacific environmental classifiers. A candidate study would keep only storm-times inside a stated window before landfall, using public best-track records, and compare a gradient-boosting classifier with a SHIPS-style baseline on probability of detection and false-alarm ratio. The opened western North Pacific article names IBTrACS as the track source and does not contain the word landfall. The opened FAST-ML HTML treats near-landfall timing as motivation and names ensemble calibration as future work.

**Nearest studies.**

1. Kim, S.-H., Lee, W., Kang, H.-W., and Kang, S. K. (2024). Predicting rapid intensification of tropical cyclones in the western North Pacific: a machine learning and net energy gain rate approach. Frontiers in Marine Science. https://doi.org/10.3389/fmars.2023.1296274. OpenAlex publication year 2024. The opened HTML banner reads "Volume 10 - 2023". Opened: HTML full text. Locator: HTML discussion of principal components. Quote: "However, it is worth noting that PCA comes with limitations, such as reduced interpretability due to the transformation of original variables into principal components."
2. Xiao, S., Lin, J., Ehrmann, T. S., and Sarhadi, A. (2026). FAST-ML: A Hybrid Physics-Machine Learning Framework for Tropical Cyclone Intensity Forecasting. Preprint. arXiv:2609.25505. https://doi.org/10.48550/arXiv.2609.25505. Venue: arXiv, primary category physics.ao-ph. Opened: HTML full text. Locator: HTML discussion beside the lead-time figure. Quote: "Future work will explore additional perturbation strategies and statistical calibration to improve ensemble reliability."
3. Chih, C.-H., Wu, C.-C., and Huang, Y.-H. (2026). Beyond a single rapid intensification threshold: a continuous intensification rate index for tropical cyclones using vortex-scale machine learning. npj Climate and Atmospheric Science. https://doi.org/10.1038/s41612-026-01478-6. Opened: publisher abstract only. The article HTML redirected with `cookies_not_supported` and did not include the body. Locator: abstract on that page. Quote: "Existing studies often rely on static binary thresholds for RI occurrence."
4. Wu, Q., Luo, T., and Hong, J. (2025). Incorporating Hourly Convective Cloud Data Into Tropical Cyclone Rapid Intensification Forecasting With Machine Learning. Journal of Geophysical Research: Machine Learning and Computation. https://doi.org/10.1029/2025jh000595. Opened: OpenAlex abstract only. The abstract does not state a limitation or future-work sentence. It states a North Atlantic test for 2018–2023 using 6-hourly SHIPS predictors plus hourly deep-convective cloud cover, with Brier skill changes reported for 24-hour intensity thresholds of at least 25, 30, 35, and 40 knots.
5. Bhowmick, R. (2025). Southwest Pacific Tropical Cyclone Rapid Intensification Classification Utilizing Machine Learning. Atmosphere, 16(4), 456. https://doi.org/10.3390/atmos16040456. Opened: OpenAlex abstract only. MDPI HTML and PDF returned HTTP 403. The opened abstract does not include a future-work sentence. It states an evaluation on 324 Southwest Pacific tropical cyclones from 1982 to 2023, of which 81 met a 24-hour intensification of at least 15 m s−1, using decision tree, random forest, and XGBoost classifiers.

The opened Kim HTML gives the track source as IBTrACS v04r00 netCDF and describes western North Pacific training cases for 2004–2018 and a test period for 2019–2021. A text extract of that HTML contains no "landfall" token.

**Candidate venues.** Frontiers in Marine Science (2024 article above) and npj Climate and Atmospheric Science (2026 article above) published rapid-intensification studies at article scale. IEEE Xplore recent-issue URLs for IEEE Transactions on Geoscience and Remote Sensing (punumber 36) and IEEE Transactions on Network Science and Engineering (punumber 6488902) returned HTTP 200 with those journal titles, and the body was a bot-check script, so the issue lists were not read. Scopus sources returned HTTP 403. Indexing not confirmed. These venues do not pass the index check.

**Social implication.** Affected population: coastal residents in basins where tropical cyclones make landfall. SDG 13, Climate Action. Decision: whether a forecast desk adds a pre-landfall rapid-intensification flag next to existing guidance. Harm: a false flag can trigger costly movement of people; a miss leaves a coastal community with a weaker intensity cue. The candidate result would be a skill score on past tracks. It would not show that a model saved lives or prevented damage. Best-track records are not personal data. Using the flag as a certain damage forecast would misuse a probabilistic label.

**Draft title.** Classifying pre-landfall rapid intensification for tropical cyclones Using gradient boosting
Word count: 10.

**Subdomain.** predictive analytics

**Dataset lead.** IBTrACS. Official page opened: https://www.ncei.noaa.gov/products/international-best-track-archive. The page calls it the most complete global collection of tropical cyclones and a publicly available best-track dataset, with CSV, netCDF, and shapefile access, including files by storm, year, basin, or all storms. Documented unit: storm-time, as a best-track record. The opened product page does not state the reporting interval. Philippine rows are not named. The page describes a global multi-agency archive. No bulk file was downloaded.

The SHIPS developmental-data pages tried on this run did not open (connection reset). They are not the dataset lead. See unverified leads.

**Claim boundary.** A pre-landfall probability of detection or false-alarm ratio is an association between predictors and a later intensity change on past tracks. It is not a cause of damage, and it is not evidence that a forecast prevented harm.

## Card 3. Sensor-hour anomaly flags

**Gap statement.** Opened 2023–2025 studies already separate air-quality sensor faults from the monitoring network: a review that lists anomaly detection as one of five AI tasks and names data quality as a gap, a review of outdoor gas-sensor deployments that reports geographic holes and missing historical downloads, an abstract that evaluates bias and drift with a recurrent autoencoder, and an abstract that repairs a reading from earlier measurements when those measurements are not themselves anomalous. A candidate study would apply one detector to sensor-hours from a public multi-country archive and score false alerts against that archive's own quality flags, then repeat the score on a second country's sensors. The opened review states the data-quality gap and does not report that transfer score. The opened autoencoder abstract does not name the archive.

**Nearest studies.**

1. García, A., Sáez, Y., Harris, I., Huang, X., and Collado, E. (2025). Advancements in air quality monitoring: a systematic review of IoT-based air quality monitoring and AI technologies. Artificial Intelligence Review, 58. https://doi.org/10.1007/s10462-025-11277-9. Opened: PDF full text. Locator: PDF abstract, also present in the extracted full text. Quote: "Additionally, the paper identifies research gaps in the literature, particularly related to data quality, system scalability, and integration challenges in AI-driven IoT systems."
2. Okorn, K. E., and Iraci, L. T. (2024). An overview of outdoor low-cost gas-phase air quality sensor deployments: current efforts, trends, and limitations. Atmospheric Measurement Techniques, 17, 6425–6457. https://doi.org/10.5194/amt-17-6425-2024. Opened: HTML full text. Locator: HTML opening. Quote: "This also exposes gaps in monitoring efforts to date, especially regarding the availability of gas-phase measurements compared to particulate matter (PM) and geographic coverage gaps (the Global South, rural areas)."
3. Allka, X., Ferrer-Cid, P., Barceló-Ordinas, J. M., and García-Vidal, J. (2024). Pattern-Based Attention Recurrent Autoencoder for Anomaly Detection in Air Quality Sensor Networks. IEEE Transactions on Network Science and Engineering, 11(6), 6372–6381. https://doi.org/10.1109/tnse.2024.3454459. Opened: OpenAlex abstract only. The UPC PDF link failed SSL certificate verification and was not opened. The abstract does not name the monitoring network. Locator: abstract evaluation sentence. Quote: "Its performance is evaluated with two categories of anomalies, bias fault and drift anomalies, and compared with baseline models such as a feed-forward autoencoder and a transformer architecture, as well as with models not based on temporal patterns."
4. Rollo, F., Bachechi, C., and Po, L. (2023). Anomaly Detection and Repairing for Improving Air Quality Monitoring. Sensors, 23(2), 640. https://doi.org/10.3390/s23020640. Opened: OpenAlex abstract only. MDPI HTML and PDF returned HTTP 403. The opened abstract does not include a future-work sentence. Locator: abstract method sentence. Quote: "If at least some previous measurements are available and not anomalous, it trains a model and uses the prediction to repair the observations; otherwise, it exploits the previous observation."

The opened Okorn HTML also says that, for one category of networks, the authors found a live map and did not find a historical download or a public calibration explanation. The opened García PDF cites a 2015 OpenAQ platform paper. That citation was not opened and is only a lead.

**Candidate venues.** Atmospheric Measurement Techniques (2024 review above) and Artificial Intelligence Review (2025 review above) published sensor-network and AI monitoring studies at review scale. IEEE Xplore for IEEE Transactions on Network Science and Engineering returned the journal title and a bot-check body, so the issue list was not read. Scopus sources returned HTTP 403. Indexing not confirmed. These venues do not pass the index check.

**Social implication.** Affected population: residents near outdoor air-quality sensors in cities that contribute to a public archive. SDG 11, Sustainable Cities and Communities. Decision: whether a network operator withholds a sensor-hour from a public map. Harm: a false anomaly flag can stigmatize a neighborhood as polluted, or it can hide a real exceedance if the flag is trusted too quickly. The opened OpenAQ page does not say the sensors are inside homes; a household sensor would add a privacy risk. A sensor fault is not a legal emissions finding and is not a diagnosis of a person.

**Draft title.** Detecting hourly air-quality sensor anomalies for public monitors Using isolation forest
Word count: 11.

**Subdomain.** anomaly detection

**Dataset lead.** OpenAQ. Documentation page opened: https://docs.openaq.org/about/about. The page says the data are publicly available, that users must comply with third-party terms, and the docs menu lists an API key, rate limits, and "Get measurements aggregated to hours by sensor ID" plus "Get precomputed hourly measurements by sensor ID". Documented unit: sensor-hour. Philippine rows are not named. https://openaq.org/ returned a connection reset. A bulk CSV download page was not opened. This lead is an API path with a key, which is free-registration style access described in the docs, and it is not a confirmed one-click bulk file. No measurements were downloaded.

**Claim boundary.** A false-alert rate against an archive flag is an agreement between a detector and the archive's own label. It does not show the cause of a pollutant level, and it does not support a health or legal label for a person or a facility from the sensor reading alone.

## Unverified leads and blocked pages

Unverified leads, not used as nearest studies:

- Chua, P. L., and coauthors. Adapting Heat Alert Systems to Tropical Climates: A Data-driven Evaluation of the Philippine Heat Index Warnings. https://doi.org/10.2139/ssrn.7333718. OpenAlex returned the DOI with an empty abstract. The DOI URL returned HTTP 403. Not used.
- Griffin, S. M., Wimmers, A., and Velden, C. S. (2022). Predicting Rapid Intensification in North Atlantic and Eastern North Pacific Tropical Cyclones Using a Convolutional Neural Network. Weather and Forecasting. https://doi.org/10.1175/waf-d-21-0194.1. OpenAlex abstract only; `is_oa` false. The abstract has no limitation sentence in the retrieved text. Left out of the cards so the cyclone card stays with studies that were opened more fully or that state a basin and period in the abstract used above.
- Chen, B.-F., Kuo, Y.-T., and Huang, T.-S. (2023). A deep learning ensemble approach for predicting tropical cyclone rapid intensification. Atmospheric Science Letters. https://doi.org/10.1002/asl.1151. Wiley PDF returned HTTP 403. Abstract was retrieved from OpenAlex and was not used as a card quote.
- Slocum, C. J., Knaff, J. A., and Stevenson, S. N. (2023). Lightning-Based Tropical Cyclone Rapid Intensification Guidance. Weather and Forecasting. https://doi.org/10.1175/waf-d-22-0157.1. The NOAA repository PDF returned HTTP 403. Abstract only; not used in a card.
- Singh, K. S., and coauthors (2022). Prediction of rapid intensification for land-falling extremely severe cyclonic storms in the Bay of Bengal. Theoretical and Applied Climatology. https://doi.org/10.1007/s00704-022-03923-x. OpenAlex abstract empty and `is_oa` false. Publisher page not opened. Not used.
- SHIPS developmental data. https://rammb.cira.colostate.edu/research/tropical_cyclones/ships/ and https://rammb2.cira.colostate.edu/research/tropical-cyclones/ships/ and https://rammb2.cira.colostate.edu/research/tropical-cyclones/ships/ships-developmental-data/ reset the connection. Not used as a dataset lead.
- Hasenkopf and coauthors (2015), cited inside the opened García PDF as an OpenAQ platform paper. Older than the window and not opened.

Blocked or incomplete pages:

| Page | Result |
| --- | --- |
| https://www.scopus.com/sources | HTTP 403 |
| https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=36 | HTTP 200; title is the TGRS IEEE Xplore page; body is a bot-check script |
| https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=6488902 | HTTP 200; title is the TNSE IEEE Xplore page; body is a bot-check script |
| https://www.mdpi.com/1424-8220/23/2/640/htm and the PDF | HTTP 403 |
| https://www.mdpi.com/2073-4433/16/4/456/htm and the PDF | HTTP 403 |
| https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/asl.1151 | HTTP 403 |
| https://doi.org/10.2139/ssrn.7333718 | HTTP 403 |
| https://upcommons.upc.edu/bitstreams/b277ed89-9983-4698-bd95-c74c31b199c9/download | SSL certificate verification failed |
| https://repository.library.noaa.gov/view/noaa/54707/noaa_54707_DS1.pdf | HTTP 403 |
| https://www.ncei.noaa.gov/products/land-based-station/global-summary-of-the-day | HTTP 503 |
| https://openaq.org/ | connection reset |
| https://docs.openaq.org/using-the-api/v3 | HTTP 404 |
| SHIPS URLs above | connection reset |
| https://www.nature.com/articles/s41612-026-01478-6 | HTTP 200 abstract page with `cookies_not_supported`; article body not opened |
| https://www.scimagojr.com/journalsearch.php?q=Weather+and+Forecasting | HTTP 403 |
| arXiv HTML for 2407.10434 | 404 for HTML; PDF was downloaded outside the repository and opened |

## Paper URLs used

- https://doi.org/10.48550/arXiv.2603.19488
- https://doi.org/10.48550/arXiv.2407.10434
- https://doi.org/10.1007/s40572-025-00496-5
- https://doi.org/10.1007/s13753-026-00760-8
- https://doi.org/10.1371/journal.pclm.0000941
- https://doi.org/10.3389/fmars.2023.1296274
- https://doi.org/10.48550/arXiv.2609.25505
- https://doi.org/10.1038/s41612-026-01478-6
- https://doi.org/10.1029/2025jh000595
- https://doi.org/10.3390/atmos16040456
- https://doi.org/10.1007/s10462-025-11277-9
- https://doi.org/10.5194/amt-17-6425-2024
- https://doi.org/10.1109/tnse.2024.3454459
- https://doi.org/10.3390/s23020640
- https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database
- https://www.ncei.noaa.gov/data/global-summary-of-the-day/doc/readme.txt
- https://www.ncei.noaa.gov/products/international-best-track-archive
- https://docs.openaq.org/about/about
- https://arxiv.org/abs/2609.00065
