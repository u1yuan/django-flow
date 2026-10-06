# AquaVir literature expansion

> **Current project decision (2026-09-29):** TFT is the selected forecasting model; random forest fault detection requires verified labels. Statements below about LSTM as AlgoB describe the earlier literature review and were not rewritten as empirical TFT evidence. See [the model decision](model-decision-2026-09-29.md).

Generated: 2026-09-29
Review type: scoping expansion
Search window for the new queries: 2018-01-01 through 2026-09-29
Databases: OpenAlex, via the activity CLI. arXiv was retried with the activity utility script and returned HTTP 406 again.

This note adds local and foreign sources to the 2026-09-28 method review. It does not replace that review's AlgoA or AlgoB recommendation. The five studies already in the ledger (Moon, Ahn, and Son, 2018; Karimzadeh, Li, and Ahamed, 2025; Mokhtar and colleagues, 2022; Eraliev and Lee, 2023; Shu and Yang, 2026) were not re-opened on this date. Claims about them below use the ledger status already recorded.

OpenAlex supplied the new abstracts. An abstract supports only the sentence it states. A title, or an index hit whose abstract text was not returned, is a lead. No hydroponic facility file was analyzed.

## Shared constraint

Three zones and about 10,000 rows are the feasibility hope in the 2026-09-28 review. They are not a confirmed export. No hydroponic file is on disk.

## Holistic gap

The opened work answers several narrower questions, and they do not combine into a cross-zone decision.

A single line can be forecast. Moon, Ahn, and Son (2018) forecast hourly root-zone electrical conductivity on one closed-loop sweet-pepper line, without a harvest label. A single nutrient-film system can be checked for faults that someone has already labeled. Karimzadeh, Li, and Ahamed (2025) detect injected electrical-conductivity and pH sensor faults on one NFT system. A single tank can be dosed back toward a setpoint. Dela Vega, Gonzaga, and Gan Lim (2021) describe fuzzy adjustment of pH and electrical conductivity on one NFT tower. Musa, Sugeru, and Mufza (2019) apply Mamdani fuzzy logic to a PPM value from electrical conductivity and pH on one NFT system. Agustian and colleagues (2022) use a Mamdani system to set pump time for pH and TDS on one NFT system. Ions in a solution can be estimated from electrode arrays. Vu Ngoc Tuan and colleagues (2020) report deep kernel learning errors for eight ions in a closed hydroponic system. Yield, leaf images, germination, and greenhouse air are separate targets: Mokhtar and colleagues (2022), the Philippine image papers screened below, Kim and colleagues (2023), Eraliev and Lee (2023), and Shu and Yang (2026).

None of those passages evaluates whether zones are consistent with one another, or which anomalous nutrient-solution period an operator should handle first, when harvest labels are unavailable and anomaly labels are scarce. A query for English hydroponic works, 2018-01-01 through 2026-09-29, whose abstracts contain "multi-zone," "multiple zones," "zone consistency," or "multizone," returned 0 indexed works (`raw/oa-f2.json`). That count is the index count. It is not a claim that no such paper exists outside this query.

This is the same decision as rank 1 in `vault/3-notes/AquaVir research gaps.md`. The expansion checks it against Philippine sources and against methods the first review did not open. It does not rename AlgoA. Fuzzy dosing is control, not an unlabeled zone detector. The two-source bar for AlgoA is still unmet. AlgoB is unchanged: short-horizon nutrient-solution EC with a persistence baseline, on one opened full text.

## Local sources (Philippine institutions)

OA-PH1 indexed 117 English works with a Philippine institution and "hydroponic" in the title or abstract. Pages 1 and 2 were title-screened (20 titles). OA-PH-sensor indexed 75 of those with an abstract term for sensor, IoT, pH, nutrient, forecast, or anomaly. Its two pages were title-screened and overlap the first query. The other indexed titles were not opened.

### Abstract opened

Dela Vega, J. A., Gonzaga, J. A., & Gan Lim, L. A. (2021). Fuzzy-based automated nutrient solution control for a hydroponic tower system. https://doi.org/10.1088/1757-899x/1109/1/012064

Status: abstract-only. OpenAlex abstract. De La Salle University. The abstract says the system uses fuzzy logic to adjust pH and electrical conductivity, uses dosing pumps for four treatment solutions when values leave a setpoint range, and is applied on an NFT tower. The abstract states no error, accuracy, or detection metric.

### Screened out of the gap

These were read far enough to see that they answer a different question. They are not support for the holistic gap.

- Image or leaf classification, not a nutrient-solution time series. The Mapúa University abstract reports 90% device accuracy for CNN classification of romaine-lettuce leaf health (`10.1109/iicaiet55139.2022.9936763`). The De La Salle University title names a support vector machine for healthy and chlorotic lettuce leaves, and the opened abstract excerpt names CIELab color features (`10.1109/hnicem57413.2022.10109533`). The Pamantasan ng Cabuyao title names machine learning for lettuce roots; the opened excerpt describes root-rot monitoring and water-temperature control and states no metric (`10.1109/tencon55691.2022.9977465`).
- Hardware monitoring or pH actuation without a named forecasting or anomaly algorithm. Examples: De La Salle University data logger for air temperature, humidity, water temperature, water level, pH, and light (`10.1109/hnicem.2018.8666373`); Tarlac State University microcontroller pH dosing (`10.36478/jeasci.2020.523.528`); Lyceum of the Philippines University ThingSpeak greenhouse monitor (`10.25147/ijcsr.2017.001.1.149`); Mapúa University garlic ebb-and-flow monitor of pH, electrical conductivity, and water temperature (`10.1109/iccae55086.2022.9762436`).
- Crop trials, finance, or plant physiology, including onion vertical farming, commercial nutrient-solution comparisons, rice nutrient studies, and pathogen assays. Title or abstract placed them outside sensor analytics.

Sensor page 2 titles that name aquaculture, a nursery, a green wall, or another ThingSpeak monitor were not given a second abstract reading. They are unused titles, not exclusions proven from an abstract.

## Foreign sources

OA-P2-title page 2 is titles 11–20 of the 76 works indexed on 2026-09-28. OA-F1 returned 9 works. OA-F2 returned 0. The five ledger works did not reappear in these pages.

### Abstract opened

Musa, P., Sugeru, H., & Mufza, H. F. (2019). An intelligent applied fuzzy logic to prediction the parts per million (PPM) as hydroponic nutrition on the based Internet of Things (IoT). https://doi.org/10.1109/icic47613.2019.8985712

Status: abstract-only. Gunadarma University, Indonesia. The abstract says an NFT system applies Mamdani fuzzy logic to predict PPM from electrical conductivity and pH, with IoT display on a phone. It gives 1050 until 1400 PPM as the need of water spinach, not as a model error. No accuracy or error is stated.

Agustian, I., Prayoga, B. I., Santosa, H., Daratha, N., & Faurina, R. (2022). NFT hydroponic control using Mamdani fuzzy inference system. https://doi.org/10.18196/jrc.v3i3.14714

Status: abstract-only. University of Bengkulu, Indonesia. The abstract says the Mamdani system outputs on-time for pH Up, pH Down, and AB Mix pumps. It states that one to three control steps normalize pH, that one step has a response time of 60 seconds, and that TDS is normalized in one control step. That is setpoint control on one system. It does not compare zones.

Vu Ngoc Tuan, Abdul Mateen Khattak, Hui Zhu, Wanlin Gao, and Minjuan Wang (2020). Combination of multivariate standard addition technique and deep kernel learning model for determining multi-ion in hydroponic nutrient solution. https://doi.org/10.3390/s20185314

Status: abstract-only. The abstract says deep kernel learning with multivariate standard addition was tested on ten real hydroponic samples and a six-electrode array. It reports RMSE of 63.8, 8.3, 29.2, 18.5, 11.8, and 8.8 mg·L−1 for nitrate, ammonium, potassium, calcium, sodium, and chloride, with coefficients of variation below 8% for those six, and RMSE of 29.6 and 8.7 mg·L−1 for phosphate and magnesium. The task is ion concentration, not zone consistency.

Kim, T. H., Baek, S.-H., Kwon, K.-H., & Oh, S. E. (2023). Hierarchical machine learning-based growth prediction model of Panax ginseng sprouts in a hydroponic environment. https://doi.org/10.3390/plants12223867

Status: abstract-only. The abstract says artificial neural networks, support vector machines, and random forest classify germination and rottenness, and that regression predicts leaf number and stem length, from physical properties and environmental sensor data. It states germination F1 of about 99% every week, rottenness classification rising from an average of 83.5% to 98.9%, and week-1 leaf-number nRMSE of 0.27, which decreased by about 33% by week 3. The abstract does not name pH, electrical conductivity, or more than one zone.

Sharmin, S., Hossan, M. S., & Uddin, M. S. (2025). A review of machine learning approaches for predicting lettuce yield in hydroponic systems. https://doi.org/10.1016/j.atech.2025.100925

Status: abstract-only, and a review. The abstract maps machine-learning yield models. It states no model metric. A review is not an independent hydroponic evaluation for AlgoA or AlgoB.

### Leads

The abstract text was not in the OpenAlex record. No result number is taken from these titles.

- Chilin Wei, Zhu Li, Zhu Delan, Tong Xu, Zhichao Liang, Yuhan Liu, and Nana Zhao (2024). Regulation of the physicochemical properties of nutrient solution in hydroponic system based on the CatBoost model. https://doi.org/10.1016/j.compag.2024.109729
- Bouarroudj, K., Babaa, F., & Touil, A. (2025). IoT-based monitoring and control for optimized plant growth in smart greenhouses using soil and hydroponic systems. https://doi.org/10.1016/j.iot.2025.101710

OA-F-iforest indexed one work for the abstract phrase "isolation forest": Bouarroudj and colleagues (2025). Because the abstract text was absent, that phrase is an index match, not an opened method. It does not fill AlgoA.

### Screened out of the foreign pages

Wrong target or wrong setting, from the opened abstract or from a title that names the mismatch: PFAS plant-uptake models that use unsupervised principal component analysis or a variational autoencoder (`10.1021/acsestengg.4c00107`, `10.3390/toxics13070579`); wastewater phytoremediation with ensemble learning (`10.3390/pr11020478`); RGB-depth lettuce biomass (`10.1016/j.compag.2025.110299`, abstract text absent, title is imaging); phosphate colorimetry with partial least squares and principal component regression (`10.1155/2020/9251416`); bacterial network ecology (`10.3389/fpls.2024.1403226`); a basil image dataset (`10.5281/zenodo.22848388`); semi-hydroponic root-image segmentation (`10.3390/agronomy15122794`). A foxtail-millet dissertation in OA-F1 is not a hydroponic sensor study.

## What this does not change

AlgoA stays unnamed. Isolation forest, an autoencoder, and a change-point detector were not in an opened hydroponic nutrient-sensor passage. The one isolation-forest index hit has no abstract text in the saved record.

AlgoB stays the short-horizon EC forecast from the one opened full text, with a persistence baseline. The new abstracts that name a model use it for PPM, pump time, ion concentration, yield, or ginseng growth. Those are not a second nutrient-solution EC forecast.

Rank 1 in the gaps note remains the only source of the statement of the problem. This expansion is the check that Philippine and foreign pages did not already answer it.

## Quality review

Reviewed on 2026-09-29 against `raw/oa-ph1.json`, `raw/oa-ph1-p2.json`, `raw/oa-ph-sensor.json`, `raw/oa-ph-sensor-p2.json`, `raw/oa-p2-title-p2.json`, `raw/oa-f1.json`, `raw/oa-f2.json`, and `raw/oa-f-iforest.json`, and against the abstracts reconstructed from those files for every number in this note. The five ledger studies were not re-opened. The same session drafted and checked the note. A person still has to confirm each locator.

First pass, then one revision. The water-spinach band of 1050 until 1400 PPM is the plant's need in the Musa abstract, not a model error. Journal names and volume numbers that were not fields in the saved JSON were removed, so the new citations keep the OpenAlex author list, year, title, and DOI. The root-monitoring paper is not described as an image result; the opened excerpt does not say that. Follow-up on the revised note: those three findings are resolved. The RMSE list matches the Tuan abstract. The Agustian step counts and 60 seconds match that abstract. The Kim F1, rottenness, and nRMSE sentences match that abstract. Dela Vega's abstract states no metric. OA-F2 `meta.count` is 0. OA-F-iforest `meta.count` is 1 and `abstract_inverted_index` is null.

QA status: pass with limitations.

Limitations that remain:

- Locators are agent-opened. They are not human-confirmed.
- Most of the 117 Philippine titles were not opened. Pages 1 and 2, plus the sensor-filtered pages, are the screened set.
- CatBoost and the isolation-forest index hit have no abstract text in the saved JSON.
- arXiv returned HTTP 406. It added no papers.
- No facility export was analyzed. The gap is a literature gap, not a measured zone result.
