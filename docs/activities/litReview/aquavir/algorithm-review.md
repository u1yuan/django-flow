# Literature review: algorithms for AquaVir

> **Current project decision (2026-09-29):** The group selected TFT for next-24-hour forecasts of available sensor readings by zone. Random forest fault detection remains conditional on verified labels. The LSTM EC recommendation below is the historical outcome of this 2026-09-28 review, not the current model choice. See [the model decision](model-decision-2026-09-29.md). No facility data were analyzed for either decision.

Generated: 2026-09-28
Review type: scoping
Search window: 2018-01-01 through 2026-09-28
Databases: OpenAlex and arXiv. arXiv returned no hits (HTTP 406). Crossref and Europe PMC were used to check metadata and one abstract. Protocol and query log: `search-protocol.md`, `search-log.md`. Evidence status: `evidence-ledger.md`.

This is a method-selection review. It does not analyze a facility dataset. No hydroponic records are on disk. Feasibility notes are design constraints, not results. The diesel literature log was not used.

QA status: pass with limitations, after one revision and one follow-up review on 2026-09-28. Limitations that remain: AlgoA is unresolved; AlgoB rests on one opened EC full text; the Eraliev and Lee abstract is not a second EC source; no facility data were analyzed; a person still needs to confirm the locators. The follow-up also noted that the ledger still said “64 units.” That phrase was changed to “64 perceptrons” after the follow-up and was not sent through a second review.

## Research question

Which one anomaly-detection algorithm (AlgoA) and which one predictive algorithm (AlgoB) should a multi-zone hydroponic IoT study use, if harvest labels are not available and anomaly labels are expected to be scarce?

## Recommendation

**Prediction target.** Short-horizon forecast of nutrient-solution electrical conductivity (EC). Air temperature, humidity, and CO₂ are a related climate-forecast task, not a substitute for EC. Yield prediction and dosing-class prediction are not the target.

**AlgoB.** Long short-term memory (LSTM), for the next hours of root-zone EC. Confidence is limited. Nutrient-solution EC has one opened full text (Moon, Ahn, and Son, 2018). Eraliev and Lee (2023) is abstract-only and forecasts air temperature, humidity, and CO₂, so it is not a second EC source and does not meet the two-source bar. The thesis should still implement a persistence baseline (repeat the last hourly EC).

**AlgoA.** No unsupervised detector met the two-source bar on hydroponic nutrient sensors. The strongest opened hydroponic result is supervised random forest for labeled EC and pH sensor faults. That method needs fault labels, so it is not the primary detector for unlabeled zone data. Until those labels exist, AlgoA stays unresolved. Do not fill the gap with an algorithm this review did not open.

Title, 14 words, counting the hyphenated compound as one word:

**AquaVir: Multi-Zone Hydroponic IoT Analytics with LSTM EC Forecasts and Random Forest Fault Detection**

The fault-label condition does not fit in 15 words. It stays in the recommendation above: random forest is only for labeled EC and pH sensor faults. LSTM is the short-horizon nutrient-solution EC forecast.

## Search strategy

OpenAlex full-text search and title-and-abstract filters, 2018–2026, English, not retracted. arXiv queries for hydroponic anomaly detection and hydroponic sensor prediction did not return records. Inclusion required a hydroponic or soilless sensor setting, a named algorithm, a dataset, and an evaluation. Hardware-only papers, image-only plant vision, and the diesel track were out of scope. Claims in the decision were checked against an opened passage. Abstracts were not upgraded to full-text findings.

## Inclusion and what the opened studies actually did

### Nutrient-solution EC can be forecast with LSTM, on one soilless line

Moon, Ahn, and Son (2018) predicted hourly root-zone EC in a closed-loop sweet-pepper culture. A single-layer LSTM with 64 perceptrons had validation R² 0.92 and RMSE 0.07, and test R² 0.72 and RMSE 0.08. LSTM beat the GRU variants they trained. ARIMA, multivariate regression, and multilayer perceptrons could not be trained for the multi-input, multi-horizon output they used. That is a limit of their setup, not a published error for ARIMA. Data were hourly means from 10-second readings, 15 October–31 December 2014, one cultivation line. The test week was 25–31 December (120 rows). The model does not use a harvest label.

This is the only opened full text that forecasts a nutrient-solution sensor AquaVir expects to have. It is not a multi-zone study, and the test fit is weaker than the validation fit.

### A second hydroponic time-series paper also favors LSTM, but only in the abstract, and not for EC

Eraliev and Lee (2023) compared a deep neural net, LSTM, and a 1D convolutional net on one week of one-minute readings from an indoor hydroponic greenhouse. The abstract says all three predicted temperature, humidity, and CO₂, and that LSTM was better at the shorter intervals (1, 5, 10, and 15 minutes). The full text was not opened, and the abstract gives no error value. The variables are greenhouse air, not pH or EC. This paper supports the direction of the LSTM choice. It does not, by itself, justify naming LSTM.

### Yield prediction is a different task and needs plant measurements

Mokhtar and colleagues (2022) predicted lettuce fresh weight from leaf number, water consumption, dry weight, stem length, and stem diameter in NFT and aeroponic systems. XGBoost using all of those inputs had RMSE 8.88 g. SVR on the same inputs had RMSE 9.55 g. Random forest and a deep net were also fit. The inputs are not the AquaVir list (pH, EC/TDS, solution temperature, water level, humidity). The target requires a harvest weight. That is why yield is rejected as AlgoB's target for a study with no confirmed yield file.

No opened paper predicted a dosing or pH-intervention class from multivariate zone sensors. That target is not selected.

### Hydroponic EC and pH fault detection, when labels exist, favored random forest

Karimzadeh, Li, and Ahamed (2025) compared SVM, k-nearest neighbors, an artificial neural net, random forest, and LSTM on a closed-loop NFT lettuce system (two racks, 70 heads, 30 August–23 September 2023). Faults were injected and labeled: bias, drift, precision degradation, spike, and stuck. The abstract reports random-forest detection accuracy of 93.7% for EC and 96.5% for pH. The same abstract reports high diagnosis accuracies for several fault types and an ANN-versus-SVR comparison for detecting EC faults from other variables (93.2% versus 49.4%). The paywalled result tables were not opened, so those figures are the abstract's figures, not a recomputation.

This is the direct hydroponic anomaly paper in the opened set. It is supervised. AquaVir does not have a labeled fault file. The protocol bars a method that needs a large labeled anomaly set from being the primary AlgoA. Random forest is the algorithm to implement if the group later labels faults. The simpler model already in that comparison is k-nearest neighbors. It is the baseline to keep beside random forest, not a second winner.

### A greenhouse residual detector is not the hydroponic result

Shu and Yang (2026) detect anomalies in light, temperature, humidity, and CO₂ with CNN-LSTM residuals and a peaks-over-threshold cutoff. Their sensitivity check reports F1 92.2% at a 0.99 quantile. They compare LSTM, BeatGAN, and THOC. Anomalies were labeled, including deliberate disturbances, on 40,320 points from seven days. The sensors are not nutrient-solution pH or EC. The model is deep. It does not name AlgoA.

## Thematic synthesis

Sensor-state forecasting is the prediction target that showed up in opened hydroponic or soilless sensor work without a harvest label. LSTM is the algorithm in the one opened nutrient-solution EC study (Moon, Ahn, and Son, 2018). Eraliev and Lee (2023) also name LSTM, but only in an abstract, and only for air climate. That is directional support. It is not a second EC study and it does not meet the two-source bar. Yield models exist, and Mokhtar and colleagues is a clear one, but they answer a labeled harvest question with plant measurements.

Anomaly work on the nutrient solution itself, in the opened set, is supervised sensor-fault classification. Random forest led that comparison. Unsupervised multi-zone detection of unlabeled operating anomalies was not established. Isolation forest, reconstruction autoencoders, and change-point detectors were not in an opened hydroponic passage, so they are not recommended here. Surveys named in the feasibility file were not opened and are not evidence.

Nothing opened evaluates cross-zone consistency. Zone ranking remains a thesis problem, not a finding of these papers.

## What the thesis still has to obtain

- A facility export with timestamps, zone identifiers, and the available series among pH, EC/TDS, solution temperature, water level, and humidity. Three zones and about 10,000 rows were the feasibility hope. They are not confirmed.
- Enough history for an hourly or finer EC series before an LSTM is fit. Moon and colleagues used a season of one line and still lost accuracy on the held-out week.
- If random forest fault detection is attempted: labels for normal versus faulty readings, with the fault type if diagnosis is in scope. Injected faults in a methods paper are not the same as operator-confirmed events.
- A persistence forecast beside LSTM, and k-nearest neighbors beside random forest if fault labels are collected.
- Human confirmation of the passages cited below.

## Gaps and limitations

- AlgoB rests on one full text. The second LSTM paper is abstract-only and forecasts different variables.
- AlgoA has no unlabeled hydroponic winner.
- arXiv was unavailable (HTTP 406). OpenAlex prediction search page 2 (76 indexed works, 10 titles read) was not retrieved.
- Several 2025–2026 hydroponic titles in the search, including Métwalli and colleagues (2025), were not opened.
- Reported accuracies are copied from the opened passages. They are not AquaVir performance.
- Course AI-use logging remains the group's responsibility. Sources opened for this review are the URLs in the ledger and the references below.

## References

Eraliev, O., & Lee, C.-H. (2023). Performance analysis of time series deep learning models for climate prediction in indoor hydroponic greenhouses at different time intervals. *Plants, 12*(12), 2316. https://doi.org/10.3390/plants12122316

Karimzadeh, S., Li, Z., & Ahamed, M. S. (2025). Machine learning-based fault detection and diagnosis of electrical conductivity and pH sensors in hydroponic systems. *Computers and Electronics in Agriculture, 237*, 110544. https://doi.org/10.1016/j.compag.2025.110544

Mokhtar, A., El-Ssawy, W., He, H., Al-Anasari, N., Sammen, S. Sh., Gyasi-Agyei, Y., & Abuarab, M. (2022). Using machine learning models to predict hydroponically grown lettuce yield. *Frontiers in Plant Science, 13*. https://doi.org/10.3389/fpls.2022.706042

Moon, T., Ahn, T. I., & Son, J. E. (2018). Forecasting root-zone electrical conductivity of nutrient solutions in closed-loop soilless cultures via a recurrent neural network using environmental and cultivation information. *Frontiers in Plant Science, 9*. https://doi.org/10.3389/fpls.2018.00859

Shu, J., & Yang, D. (2026). CNN-LSTM-POT-based anomaly detection for smart greenhouse sensor data: A real-time edge deployment approach. *Future Internet, 18*(4), 205. https://doi.org/10.3390/fi18040205

## Claim map

| Claim | Source | Locator opened | Passage status |
| --- | --- | --- | --- |
| LSTM validation R² 0.92, RMSE 0.07; test R² 0.72, RMSE 0.08 for root-zone EC | S1 Moon et al. 2018 | Abstract and results table in the Frontiers full text | Agent-opened passage. Not human-confirmed. |
| LSTM was more accurate than GRU; ARIMA, multivariate regression, and MLP could not be trained on that setup | S1 | Results paragraph after Table 3 | Agent-opened passage. Not human-confirmed. |
| Test set is 25–31 Dec 2014, 120 rows; one sweet-pepper line | S1 | Data-split paragraph | Agent-opened passage. Not human-confirmed. |
| LSTM outperformed DNN and 1D-CNN at shorter intervals for temperature, humidity, and CO₂. This is not a second EC source. | S4 Eraliev and Lee 2023 | Abstract archived in `raw/eraliev-2023-abstract.md`. Full text not opened. | Abstract-only. Not a second nutrient-solution EC study. |
| XGBoost RMSE 8.88 g and SVR RMSE 9.55 g for lettuce fresh weight; scenario 3 inputs are leaf number, water consumption, dry weight, stem length, and stem diameter | S3 Mokhtar et al. 2022 | Abstract and results paragraphs | Agent-opened passage. Not human-confirmed. |
| Random forest EC/pH fault detection 93.7% and 96.5%; faults were injected | S2 Karimzadeh et al. 2025 | Abstract and introduction on the publisher HTML | Agent-opened abstract text. Diagnosis tables not opened. Not human-confirmed. |
| ANN 93.2% vs SVR 49.4% for sensor-independent EC fault detection | S2 | Abstract on the publisher HTML | Agent-opened abstract text. Not human-confirmed. |
| CNN-LSTM-POT F1 92.2% at quantile 0.99 on greenhouse light, temperature, humidity, and CO₂ | S5 Shu and Yang 2026 | Sensitivity paragraph and dataset paragraph | Agent-opened passage. Not used as AlgoA. Not human-confirmed. |
| Isolation forest, autoencoders, or change-point detection won on multi-zone hydroponic sensors | None | Not opened | Not claimed |
| These algorithms were run on AquaVir data | None | No data file | Not claimed |

## Search log

See `search-log.md`.

## Unresolved inputs

- Full text of Eraliev and Lee (2023), so the LSTM climate comparison can move from abstract-only to verified.
- Full text of Karimzadeh, Li, and Ahamed (2025) beyond the open HTML, if diagnosis accuracies are quoted outside the abstract.
- A second opened hydroponic study of unlabeled multivariate anomaly detection, if AlgoA is to be named.
- Facility data, zone count, and any fault or harvest labels.
