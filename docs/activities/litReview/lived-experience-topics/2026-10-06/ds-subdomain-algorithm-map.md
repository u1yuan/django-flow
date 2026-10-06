# Data Science subdomain and algorithm map: lived-experience ideas

Compiled: 6 October 2026. Scope: the 58 kept ideas in `idea-pool.md` (37) and `fields-apm/idea-pool.md` (21).

Every algorithm here is a design proposal. No model was trained, no file was opened for this map, and no record count changes from the two evidence ledgers. Where a row cites a ledger figure, the figure belongs to the ledger, with the ledger's caveat. A baseline named here is the comparison the idea's own draft question implies. It is not a measured score.

Subdomain labels are the 10 Data Science research areas in section 3 of `docs/CS-Guideline-as-of-Nov-17-as-430pm-without-signature (1).md`, word for word: Data Mining, Big Data Analytics, Predictive Analytics, Feature Engineering, Recommendation Systems, Data Visualization, Anomaly Detection, Statistical Modeling, Data Governance and Ethics, and Edge and IoT Data Analytics. Algorithm names follow Appendix A of the same guideline where it has one. Standard statistical methods are added where a question needs them.

Not mapped: L07, T04, and T06, which the scorecard dropped on the record gate, and A08, P08, and M07, which were written as exclusions. This file does not replace AquaVir or the diesel record.

## Track warning

The guideline puts Natural Language Processing (NLP), Computer Vision, and Deep Learning in the AI list, not the Data Science list. Machine Learning and Explainable AI are also AI-list items. A Data Science title should name a Data Science area and the problem. The model is the technique, not the area.

Text ideas are therefore framed as Data Mining, with Feature Engineering as the secondary area. The core method is TF-IDF features with a linear model: Naive Bayes, logistic regression, or a linear SVM. A fine-tuned multilingual or Tagalog Transformer appears only as a comparison row. A title led by a Transformer may read as AI track.

The same rule covers three other spots. LSTM in C06 is an optional comparison. A06 works on track features that a detector already produced; a study that starts from raw video is Computer Vision. SHAP in P01 is a reading aid for the model, not the contribution.

## Archetype summary

The ideas fall into 11 problem shapes. The number is the "Shape" column in the full table.

1. **Next-period event alert.** S01, C01, C05, C07, T01, T05, A01, A03, M01, M03. Primary: Predictive Analytics. Methods: logistic regression as the model baseline, then random forest, then XGBoost or LightGBM. Metrics: PR-AUC, F1, and Brier score against the idea's own rule (persistence, same hour last week, ordinary rain days, a seasonal rate, or climatology).
2. **Continuous forecast.** S08, C06, T02, T03, T08. Primary: Predictive Analytics, or Statistical Modeling where the question explains a change rather than forecasts it (S08, T03). Methods: ridge or lasso, gradient boosting, quantile regression, optional LSTM. Metrics: MAE and MASE against a naive forecast.
3. **Text classification.** C08, O01, O02, O06, O08, L02, L04, L06, P02, P04. Primary: Data Mining. Secondary: Feature Engineering, except L04. Methods: TF-IDF with Naive Bayes, logistic regression, or linear SVM, then a Transformer as comparison. Metric: macro F1 against a keyword, length, rule, or historical-rate baseline.
4. **Topic discovery and clustering.** S02, S04, L05, O07. Primary: Data Mining. Methods: LDA, BERTopic (embeddings, UMAP, HDBSCAN), k-means or hierarchical clustering, and MinHash near-duplicate detection for O07. Metrics: topic coherence and silhouette score.
5. **Review flags without labels.** S05, O05, L01, L08, T07, A05, M06, M08. Primary: Anomaly Detection. Methods: robust z-score or median absolute deviation (MAD) against a peer group, isolation forest, local outlier factor (LOF), and change-point detection (PELT or CUSUM) for T07 and O05. Metric: precision at k on a sample a person reviews. A flag is a prompt for review. It is not a finding of fraud, corruption, or wrongdoing.
6. **Time to event.** S07, L03, M05. Primary: Statistical Modeling. Methods: Kaplan-Meier, Cox proportional hazards, random survival forest. Metrics: concordance index and integrated Brier score against a median or no-skill baseline.
7. **Calendar and intervention effects.** S03, S06, P03, P06, M04. Primary: Statistical Modeling. Methods: segmented regression, SARIMA with an intervention term, and Poisson or negative binomial models with calendar terms. Metric: effect size with a confidence interval.
8. **Spatial and network questions.** C02, C03, C04. Primary: Data Visualization for C02, Statistical Modeling for C03 and C04. Methods: shortest-path or isochrone accessibility, Getis-Ord Gi* hotspots, Poisson or negative binomial count models.
9. **Recommender.** O03. Primary: Recommendation Systems. Methods: popularity baseline, matrix factorization, hero-pair win model. Metric: hit rate at k.
10. **Survey models.** P01, P07, A07. Primary: Statistical Modeling. Methods: OLS, regularized regression, gradient boosting with SHAP, and leave-one-country-out validation for P01. These are associations, not causal effects.
11. **Ideas that do not fit one pattern.** A02 (SGP4 orbit propagation, then a classifier against a sighting log), A04 (ranking classifier), A06 (track features with random forest), O04 (information extraction, then quantile regression), M02 (forecast verification scores, then a classifier that predicts misses), and P05 (paired error test with McNemar's test, with Data Governance and Ethics as the secondary area).

## Full mapping table

Abbreviations: LR, logistic regression. RF, random forest. NB, Naive Bayes. SVM, support vector machine. KM, Kaplan-Meier. Cox, Cox proportional hazards. RSF, random survival forest. LOF, local outlier factor. MAD, median absolute deviation. NegBin, negative binomial. C-index, concordance index. "Text set" means TF-IDF + NB; LR; linear SVM; Transformer (comparison only).

Algorithms run from simplest to most complex. "Reviewed" means a sample a person checks by hand.

| ID | Shape | Problem | Primary subdomain | Secondary subdomain | Baseline from draft question | Candidate algorithms | Metric | Fit warning |
| --- | ---: | --- | --- | --- | --- | --- | --- | --- |
| S01 | 1 | Same-day class suspension per LGU | Predictive Analytics | Feature Engineering | Persistence rule | LR; RF; XGBoost or LightGBM | PR-AUC, F1, Brier | Prior Naive Bayes model exists (ledger) |
| S02 | 4 | Forum themes by academic month | Data Mining | Statistical Modeling | Off-season theme share | LDA; BERTopic; k-means on embeddings | Topic coherence, silhouette | Comment history not opened |
| S03 | 7 | Commits before deadlines | Statistical Modeling | Data Mining | Non-deadline weeks | Poisson; NegBin with calendar terms; segmented regression | Rate ratio with CI | Org list is not a commit count |
| S04 | 4 | Crowded and thin thesis topics | Data Mining | Data Visualization | Title keyword counts | TF-IDF + k-means; hierarchical clustering; LDA; BERTopic | Silhouette, topic coherence | No thesis file downloaded (ledger) |
| S05 | 5 | Bedspace listing red flags | Anomaly Detection | Feature Engineering | Single red-flag rule list | Rule score; isolation forest; LOF | Precision at k, reviewed | High privacy risk; flag is not fraud |
| S06 | 7 | Abstract style after Nov 2022 | Statistical Modeling | Feature Engineering | Prior trend | Style features; segmented regression; SARIMA with intervention | Level and slope change with CI | Corpus shift only, no student label |
| S07 | 6 | Stipend release lag | Statistical Modeling | Predictive Analytics | All-agency median lag | KM; Cox; RSF | C-index, integrated Brier | Scholarship slice may be small |
| S08 | 2 | Campus meal price vs city move | Statistical Modeling | Anomaly Detection | City-wide retail series | Panel regression; ridge; LightGBM; quantile regression | MAE, MASE | Menu snapshots not opened |
| C01 | 1 | Rail disruption next hour | Predictive Analytics | Feature Engineering | Same as last hour | TF-IDF + LR; RF; LightGBM | PR-AUC, F1, Brier | No complaint corpus opened (ledger) |
| C02 | 8 | Barangays losing walk access | Data Visualization | Statistical Modeling | Pre-modernization coverage | Shortest-path isochrones; Getis-Ord Gi*; Poisson or NegBin | Population share in walk range | Stop-times are not barangay outcomes (ledger) |
| C03 | 8 | Heat on the station walk | Statistical Modeling | Data Visualization | Same-hour climatology | LR; LightGBM; Getis-Ord Gi* | PR-AUC, Brier | Overlaps stopped heat titles |
| C04 | 8 | Crash segment-hour hotspots | Statistical Modeling | Data Visualization | Exposure-only baseline | Poisson or NegBin with exposure offset; Getis-Ord Gi*; LightGBM | Deviance, hotspot precision | Extract may be restricted |
| C05 | 1 | Flood-day impassable segments | Predictive Analytics | Statistical Modeling | Ordinary rain days | LR; RF; LightGBM | PR-AUC, F1, Brier | Reports may be far fewer than segment-days |
| C06 | 2 | Busway travel-time spread | Predictive Analytics | Big Data Analytics | Timetable | Quantile regression; LightGBM; LSTM (comparison) | MAE, MASE, pinball loss | Feed may not exist or be archived |
| C07 | 1 | Next-hour station crowding | Predictive Analytics | Statistical Modeling | Same hour last week | LR; RF; LightGBM | PR-AUC, F1 | Hourly ridership not confirmed |
| C08 | 3 | Traffic-status text vs rain | Data Mining | Feature Engineering | Rain-and-calendar tabular model | Text set | Macro F1 | Post count alone may fall short |
| O01 | 3 | Incentive-like Taglish reviews | Data Mining | Feature Engineering | Rating threshold and duplicate rule | Text set | Macro F1 | No fraud labels; FiReCS fallback (ledger) |
| O02 | 3 | Taglish scam messages | Data Mining | Feature Engineering | Keyword list | Text set | Macro F1, false alarms on delivery notices | No labeled corpus opened |
| O03 | 9 | Match draft suggestion | Recommendation Systems | Predictive Analytics | Most-picked hero or pair | Popularity; matrix factorization; hero-pair win model (LR, LightGBM) | Hit rate at k, log loss | No Philippine filter in docs read (ledger) |
| O04 | 11 | Salary ranges by role and city | Data Mining | Statistical Modeling | Pooled role median | Rule extraction; quantile regression; LightGBM | Extraction F1, pinball loss | High ethics risk; count uncertain |
| O05 | 5 | Discount claim vs price path | Anomaly Detection | Statistical Modeling | Item's own recent price path | Rule check; robust z or MAD; change-point | Precision at k, reviewed | Terms may forbid collection (ledger) |
| O06 | 3 | Engagement-bait headlines | Data Mining | Feature Engineering | Length and punctuation rules | Text set | Macro F1 | Label source not named |
| O07 | 4 | Seller clusters with copied reviews | Data Mining | Anomaly Detection | Exact-duplicate text match | MinHash LSH; TF-IDF + hierarchical clustering; DBSCAN | Link precision, reviewed; silhouette | Terms apply; no seller accusation |
| O08 | 3 | Scam-like job posts | Data Mining | Feature Engineering | Keyword list | Text set | Macro F1 | Terms apply; flag is not a crime finding |
| L01 | 5 | Procurement award flags | Anomaly Detection | Statistical Modeling | Peer-item price | Robust z or MAD vs peers; isolation forest; LOF | Precision at k, reviewed | Row count not opened (ledger) |
| L02 | 3 | Late or denied FOI requests | Data Mining | Feature Engineering | Agency historical rate | Text set; LightGBM on text plus agency | Macro F1, PR-AUC | Portal not counted |
| L03 | 6 | Time to court decision | Statistical Modeling | Predictive Analytics | Court's median | KM; Cox; RSF | C-index, integrated Brier | Decisions name parties |
| L04 | 3 | Everyday ordinance topics | Data Mining | Data Governance and Ethics | Topic keyword rules | Text set | Macro F1 | Scattered sources; weak record path |
| L05 | 4 | Repeat audit observations | Data Mining | Feature Engineering | Boilerplate-text match | TF-IDF cosine; LDA; BERTopic | Topic coherence, link precision | COA page timed out (ledger) |
| L06 | 3 | Bills that stall | Data Mining | Feature Engineering | Last Congress's advanced bills | Text set; LightGBM on text plus path | Macro F1, PR-AUC | Bill versions not counted |
| L08 | 5 | Precinct data-quality flags | Anomaly Detection | Data Governance and Ethics | Neighbors and past turnout | Spatial robust z or MAD; LOF; isolation forest | Precision at k, reviewed | High sensitivity; flag is not fraud |
| T01 | 1 | Next-week price-spike alert | Predictive Analytics | Feature Engineering | Persistence forecast | LR; RF; LightGBM | PR-AUC, F1, Brier | Old PSA series ends 2021 (ledger) |
| T02 | 2 | Student basket next month | Predictive Analytics | Statistical Modeling | Last month's basket price | Ridge or lasso; LightGBM; quantile regression | MAE, MASE | National weekly averages would not reach 10,000 (ledger) |
| T03 | 2 | Export flows after shocks | Statistical Modeling | Predictive Analytics | Peer-product baseline | Panel fixed effects; ridge; LightGBM | MAE vs peer baseline | Indirect lived link; no extract opened |
| T05 | 1 | Slow port-clearance weeks | Predictive Analytics | Statistical Modeling | Seasonal baseline | LR; RF; LightGBM | PR-AUC, F1, Brier | AIS may be paid; monthly totals fail |
| T07 | 5 | Tariff-line import surges | Anomaly Detection | Statistical Modeling | Year-ago value | Robust z; PELT or CUSUM change-point; LightGBM residuals | Precision at k, reviewed | API cap is not a count (ledger) |
| T08 | 2 | Remittance corridors and prices | Predictive Analytics | Statistical Modeling | Price-only forecast | Ridge; panel model; LightGBM | MAE, MASE | Depends on T01's price panel |
| A01 | 1 | Clouded-out observing night | Predictive Analytics | Feature Engineering | Same as last night | LR; RF; LightGBM | PR-AUC, F1, Brier | No hourly cloud archive opened (ledger) |
| A02 | 11 | Bright satellite pass | Predictive Analytics | Feature Engineering | Deterministic pass list alone | SGP4 propagation; LR; RF | PR-AUC vs sighting log | No sighting log opened (ledger) |
| A03 | 1 | Meteor-shower detections | Predictive Analytics | Statistical Modeling | Non-shower nights | Poisson regression; RF; LightGBM | Poisson deviance, PR-AUC | Philippine camera may not exist |
| A04 | 11 | Rank transient alerts | Predictive Analytics | Feature Engineering | Brightest first | LR; RF; LightGBM ranker | Precision at k, NDCG | Follow-up label source not named |
| A05 | 5 | Off-range variable-star reports | Anomaly Detection | Data Governance and Ethics | Star's recent range | Rolling robust z or MAD; isolation forest | Precision at k, reviewed | Observer codes identify people |
| A06 | 11 | Meteor, plane, or satellite track | Feature Engineering | Predictive Analytics | Speed rule | Track features; decision tree; RF; LightGBM | Macro F1 | No labeled set opened; raw video is CV |
| A07 | 10 | Moonlight and reported sleep | Statistical Modeling | Feature Engineering | Calendar-only model | OLS; mixed-effects regression; LightGBM | Effect size with CI | No sleep file named; personal data |
| P01 | 10 | Money worry and life satisfaction | Statistical Modeling | Predictive Analytics | Demographics-only model | OLS; ridge or lasso; LightGBM with SHAP; leave-one-country-out | Held-out RMSE, R² | Philippine file too small (ledger) |
| P02 | 3 | Helpful late-night replies | Data Mining | Feature Engineering | Reply length | Text set | Macro F1, PR-AUC | Mental-health text; no crisis detector |
| P03 | 7 | Exam-week stress language | Statistical Modeling | Data Mining | Forum's own baseline rate | Lexicon rates; segmented regression; Poisson with calendar terms | Rate ratio with CI | A rate is not a diagnosis |
| P04 | 3 | Filipino cyberbullying text | Data Mining | Feature Engineering | English keyword list | Text set | Macro F1 | Ethics score 1; do not brief |
| P05 | 11 | English model error on Taglish | Statistical Modeling | Data Governance and Ethics | Same model's English error | Existing sentiment model as instrument; McNemar test; bootstrap CI | Error-rate gap with CI | No parallel English set opened (ledger) |
| P06 | 7 | Sleep timing in exam weeks | Statistical Modeling | Predictive Analytics | Ordinary weeks | Segmented regression; mixed-effects regression; LightGBM | Shift in minutes with CI | No public sleep file named |
| P07 | 10 | Disaster worry in adults | Statistical Modeling | Feature Engineering | Income-controls model | OLS; ordinal LR; LightGBM | Coefficient with CI | Association only; sample may be small |
| M01 | 1 | Rain on the walk | Predictive Analytics | Feature Engineering | Persistence and climatology | LR; RF; LightGBM | PR-AUC, Brier skill | ClimGridPh is daily, not hourly (ledger) |
| M02 | 11 | Forecast said fine | Predictive Analytics | Statistical Modeling | Persistence forecast | Verification scores; LR; LightGBM on misses | PR-AUC on misses, Brier | No issue-time archive opened (ledger) |
| M03 | 1 | Rain in the PE window | Predictive Analytics | Statistical Modeling | Seasonal frequency | LR; RF; LightGBM | PR-AUC, Brier skill | Same lead as M01; keep one |
| M04 | 7 | First monsoon school weeks | Statistical Modeling | Predictive Analytics | Same-station climatology | NegBin with calendar terms; quantile regression | Effect size with CI | One cell is under 10,000 days (ledger) |
| M05 | 6 | Thunderstorm lead time | Statistical Modeling | Predictive Analytics | No-skill baseline | KM; Cox; RSF | C-index, integrated Brier | Event count may fall short |
| M06 | 5 | Roadside sensor disagreement | Anomaly Detection | Edge and IoT Data Analytics | Simple calibration line | Robust regression residuals; isolation forest; LOF | Precision at k, reviewed | Already a gap card; not reopened |
| M08 | 5 | Gauge vs satellite rain | Anomaly Detection | Statistical Modeling | Gauge hour-to-hour persistence | Paired error model; isolation forest; LightGBM on disagreement | Precision at k, reviewed; MAE | Philippine gauge truth not opened |

## Ledger notes behind the warnings

Rows marked "(ledger)" rest on one of the two evidence ledgers. The figures below are the ledgers' figures. None was re-opened for this map.

- **S01.** The ledger opened the HabagatPlus PDF (Salvilla and Fabregas). It states a Naive Bayes recommender on rainfall, wind, and temperature from 17 of 116 PAGASA stations, 2012–2021, with an average accuracy of 82.05% in its Table III. The weather file was provided by PAGASA, and the PDF gives no public download link for the suspension file. A new study has to beat that model on comparable data or ask a different question, such as an LGU-day unit scored with Brier against persistence. An 82.05% accuracy on a different file is not a target the new model can be compared with directly.
- **C01.** No public complaint corpus was opened. A complaint is not proof the train failed.
- **C02.** The ledger counted lines in the Sakay GTFS files. Stop-times exceed 10,000 only under its unchecked header assumption, and routes, trips, and stops are each under 10,000. A stop-time is one scheduled stop on one trip, not a barangay that lost service. A Transitland page returned in search shows service dates in 2013–2014 on an older fetch. No modernization-era feed was opened, and the license is a DOTC developer license, not Creative Commons. The before-and-after map needs a second feed.
- **O01.** The fake-review version has no opened fraud labels. The ledger's fallback is FiReCS, whose card states 10,487 rows with negative, neutral, and positive labels under CC-BY-4.0. That turns the question into sentiment, so the rating-threshold baseline has to be restated for the fallback. A search-returned Shopee seller page forbids bots, crawlers, and automated collection. That is a terms lead, not a reading of the full agreement, and the proposal does not scrape Shopee again.
- **O03.** One OpenDota docs page describes a free tier of 50,000 calls a month and 60 requests a minute. The filters read did not include a Philippines flag. No match file was downloaded.
- **L01.** The BetterGov mirror is CC0, and 500.37 MB is a file size, not a row count. The 2014 comparison page's 183,619 award notices is twelve years old. Neither is a 2026 count.
- **L05.** The COA annual audit report page timed out. No observation was counted.
- **S04.** A filtered HERDIN figure was seen in search and not used. No thesis file was downloaded.
- **T01 and T02.** The PSA retail series the ledger checked was discontinued effective February 2021, so it ends before the 2023 onion spike. The DA weekly files were listed, not opened. National weekly averages of a short list would not reach 10,000.
- **T07.** The Comtrade free API returns up to 100,000 records per call. That is a cap, not a count of Philippine rows. No extract was downloaded.
- **A01.** No public bulk hourly cloud or rain archive for Philippine stations was opened. ClimGridPh is daily rainfall, not night-time cloud.
- **A02.** A CelesTrak catalog page dated 27 March 2026 lists 33,054 objects. Objects are not passes over a city. No pass was propagated, no sighting log was opened, and no license to republish the elements was in the returned text.
- **M01, M03, and M04.** The ledger opened the ClimGridPh technical report abstract: daily gridded rainfall at about 1 km, from 52 PAGASA synoptic stations merged with GPM/IMERG, 2001–2020. On that lead, M01's next-hour question becomes next-day rain, which makes it close to M03. The ledger's calendar arithmetic gives 7,305 days per cell, so a single campus cell is under 10,000 records and the study needs enough cells. The product was not downloaded.
- **M02.** No archive of forecasts as issued was opened. A tool README in search says the public pages serve only the latest forecast.
- **P01.** The IHSN catalog lists the Philippine WVS Wave 7 file at 1,200 cases. A WVS page says Wave 7 has more than 80,000 respondents, and that global file was not counted. Philippine-only analysis fails the 10,000-record rule. Leave-one-country-out needs the global file, and WVS terms forbid redistributing it.
- **P05.** The FiReCS card describes a Taglish sentiment corpus. It does not describe a test of English against Taglish error, and no parallel English set was opened.

## Mapping calls to check

These assignments were judgment calls. QA or the group may move them.

- C06 is the only Big Data Analytics row and M06 the only Edge and IoT Data Analytics row. C06 could be read as Edge and IoT, since vehicle locations come from on-board devices. It is placed under Big Data Analytics because the archived feed is analyzed after collection, not at the edge.
- L02 and L06 predict an outcome and could be Predictive Analytics. They stay under Data Mining with the other text ideas.
- A04 ranks alerts and could carry Recommendation Systems as its secondary area.
- A06 is Feature Engineering only if the tracks already exist. If the group starts from clips, it moves to the AI track.
- C03 and L04 state no baseline in their draft questions. Same-hour climatology and topic keyword rules were chosen as the closest fit.
- C07 can be a count forecast scored by MAE and MASE instead of an alert scored by PR-AUC.

## Subdomain coverage count

Each idea has one primary and one secondary area, so the secondary column also sums to 58.

| Subdomain | Primary | Secondary | Total |
| --- | ---: | ---: | ---: |
| Data Mining | 15 | 2 | 17 |
| Big Data Analytics | 0 | 1 | 1 |
| Predictive Analytics | 16 | 9 | 25 |
| Feature Engineering | 1 | 21 | 22 |
| Recommendation Systems | 1 | 0 | 1 |
| Data Visualization | 1 | 3 | 4 |
| Anomaly Detection | 8 | 2 | 10 |
| Statistical Modeling | 16 | 15 | 31 |
| Data Governance and Ethics | 0 | 4 | 4 |
| Edge and IoT Data Analytics | 0 | 1 | 1 |

Predictive Analytics, Statistical Modeling, and Data Mining carry most of the pool. Big Data Analytics and Edge and IoT Data Analytics are thin: C06 and M06 are the only plausible candidates, both as secondary areas, and both depend on feeds that were not opened. Recommendation Systems has only O03. Data Governance and Ethics appears only as a secondary area (L04, L08, A05, P05). A group that wants one of the thin areas as its title area should say so before the next check round.

## AI-use note

This map was drafted with an AI assistant on 6 October 2026 from the idea pools, scorecards, evidence ledgers, and the CS guideline named above. The assistant opened no new source and trained no model. The group still has to check every subdomain assignment, baseline, and algorithm choice, and confirm each ledger figure against the opened source before it goes into a proposal. Record this use in the activity's AI interaction log.
