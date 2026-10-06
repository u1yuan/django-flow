# AquaVir dual-model justification: TFT forecast arm and random-forest fault arm

Date: 2026-09-29  
Status: design justification; facility performance unvalidated  
Decision record: [model-decision-2026-09-29.md](model-decision-2026-09-29.md)

## Purpose

AquaVir is one analytics pipeline with **two separate model arms**. This note states why a Temporal Fusion Transformer (TFT) is the forecast arm and why random forest is the supervised fault arm, what opened passages support, and how a blocked arm must not stop the other. It does not report AquaVir facility accuracy.

The 2026-09-28 [algorithm review](algorithm-review.md) recommended LSTM for EC forecasting. That review remains a historical record. The 2026-09-29 group decision selected TFT for next-24-hour, hourly forecasts by zone and kept random forest for labeled sensor faults.

## Pipeline roles (outputs stay separate)

| Arm | Role | Output | Not this arm |
| --- | --- | --- | --- |
| **TFT forecasting** | Multi-horizon forecast of each eligible sensor target by zone for the next 24 hourly steps | Forecast trajectories (and, when used for review, absolute forecast–observation deviations ranked by size, persistence, variables, and zones) | Confirmed sensor-fault labels or validated fault classifications |
| **Random forest** | Supervised classification of **labeled** sensor faults (normal versus faulty; fault type if diagnosis is in scope) | Validated fault classifications **only when** verified normal and fault labels exist | Unsupervised anomaly detection; confirmation that a TFT deviation is a physical or sensor fault |

When labels are absent, ranked TFT deviations remain **unconfirmed review signals**. Validated random-forest alerts, if later available, must be reported separately from that ranking ([model decision](model-decision-2026-09-29.md); TA3 Anomaly Detection / Review Prioritization / Predictive Analysis modules).

## Why TFT for the forecast arm

Lim, Arık, Loeff, and Pfister (2021) introduce TFT for interpretable multi-horizon time series forecasting. The publisher ScienceDirect page did not open in this pass. Design claims below are taken from the opened ar5iv HTML of arXiv:1912.09363 (same authors and title as the *International Journal of Forecasting* article). That text supports architecture fit to AquaVir’s intended forecast shape; it does **not** establish accuracy on hydroponic facility sensors or zones.

| Design need for AquaVir | Lim et al. (2021) design claim (opened ar5iv) |
| --- | --- |
| One forecast per hour for the next 24 hours per eligible target and zone | Multi-horizon outputs: forecasts for horizons \(\tau \in \{1,\ldots,\tau_{\max}\}\) at once |
| Zone identity as time-invariant context | Static covariates with dedicated encoders that condition the rest of the network |
| Calendar time or a documented schedule known at forecast origin | Known future inputs that may extend through the forecast horizon |
| Past sensor readings only up to forecast start | Historical / observed inputs known only in the past look-back |
| Emphasis on salient inputs among many sensor and metadata channels | Instance-wise variable selection (and related interpretability components) |

Eligible targets remain those actually logged with adequate coverage among pH, EC, humidity, nutrient-solution temperature, water level, light intensity, and ambient temperature. Inputs may include historical observations, zone metadata, and genuinely known future inputs. Future sensor readings and interventions not known at forecast time must not be used ([model decision](model-decision-2026-09-29.md)).

**Comparator, not TFT evidence.** Moon, Ahn, and Son (2018) remain the one-line opened EC forecasting comparator: LSTM on one closed-loop soilless line for hourly root-zone EC. That study does not establish TFT or multi-zone performance for every listed AquaVir target (ledger S1).

**What opened TFT-adjacent searches do not support.** No opened passage shows TFT beating LSTM or XGBoost on hydroponic EC/pH or multi-zone nutrient-solution series. OpenAlex screening found no pure hydroponic multi-zone EC/pH TFT forecast study. Opened Metin, Kaşif, and Catal (2023) apply TFT to aquaponics nitrate; opened López Santos and colleagues (2022) apply TFT to day-ahead PV power. Those results must not be quoted as AquaVir or hydroponic nutrient-sensor performance (ledger S7–S8). arXiv TFT queries in this session returned abstracts; none named hydroponics (search log AX-TFT-*). The only domain-adjacent arXiv hit (AX-TFT-1 / arXiv:2512.11852; Bashir, Henna, and Furey, 2025, *Explainable AI for Smart Greenhouse Control*) is smart-greenhouse **actuator-setting classification**, not sensor-series forecasting: sensors are inputs, and the opened full text reports about **95% classification accuracy** for actuator settings; that figure must not be used as sensor-forecast accuracy or as AquaVir or hydroponic TFT performance (ledger L7; `raw/arxiv-2512.11852-passage.md`).

## Why random forest for the supervised fault arm

Karimzadeh, Li, and Ahamed (2025) compared SVM, KNN, ANN, random forest, and LSTM on labeled EC and pH sensor faults in one closed-loop NFT lettuce system. Faults were artificially induced and labeled (bias, drift, precision degradation, spike, stuck). The opened publisher HTML covers highlights, abstract, introduction, experimental-setup and conclusion snippets; result tables were not opened (ledger S2).

From that abstract-only numeric layer: random-forest fault detection accuracy **93.7% (EC)** and **96.5% (pH)**. Those figures are abstract text, not recomputed tables, and are **not** AquaVir performance. The study supports supervised random forest as a documented hydroponic approach for **labeled** EC/pH sensor faults. It does not support unsupervised anomaly detection on unlabeled multi-zone nutrient sensors, and it does not show that a random forest can learn confirmed faults without labels.

If verified AquaVir fault labels are missing, state that the supervised detector **cannot be validated**. Keep k-nearest neighbors as the simpler baseline already named in that comparison when labels later exist.

## Claim map

| Claim | Source | Locator | Status |
| --- | --- | --- | --- |
| AquaVir uses TFT for next-24-hour hourly forecasts by zone and random forest for labeled sensor faults; outputs stay separate; without labels, TFT deviations are unconfirmed review signals | Model decision 2026-09-29; TA3 §1 modules | Project design text | Design choice. No facility TFT or RF run. |
| TFT emits multi-horizon forecasts for a set of horizons at once | Lim et al. 2021 (S6) | ar5iv HTML of arXiv:1912.09363, §1, §3 (Eq. 1), Abstract | Verified for opened ar5iv full text. Not hydroponic facility accuracy. |
| TFT uses static covariates with dedicated encoders | Lim et al. 2021 (S6) | ar5iv §1, §3, §4.3 | Same. |
| TFT uses known future inputs through the forecast horizon | Lim et al. 2021 (S6) | ar5iv §1, §3, §4 / Fig. 2 | Same. |
| TFT conditions on historical / past-observed inputs in a look-back | Lim et al. 2021 (S6) | ar5iv §1, §3, §4.5.1 | Same. |
| TFT applies variable selection (and related interpretability components) | Lim et al. 2021 (S6) | ar5iv Abstract, §1, §4.2, §4.4 | Same. |
| Moon et al. 2018 is the opened one-line EC forecast comparator (LSTM, one soilless line) | Moon et al. 2018 (S1) | Publisher full text (ledger S1) | Verified. Not a TFT or multi-zone result. |
| No opened claim that TFT beat LSTM/XGBoost on hydroponic EC/pH multi-zone data | OpenAlex TFT screening; claim ceiling | Search notes / absence | Explicit non-claim. Adjacent opens are aquaponics nitrate (S7) and PV (S8). |
| Random forest is a documented supervised detector for labeled EC/pH sensor faults in hydroponics | Karimzadeh et al. 2025 (S2) | Publisher HTML abstract / introduction | Verified for opened HTML. Tables not opened. |
| Abstract reports RF detection 93.7% EC and 96.5% pH; faults injected and labeled | Karimzadeh et al. 2025 (S2) | Abstract on publisher HTML | Abstract-only figures. Not recomputed. Not AquaVir performance. |
| Without verified fault labels, the RF detector cannot be validated | Model decision; TA3 §4; limitations note | Project constraint | No AquaVir fault-label file confirmed on disk. |
| Ranked absolute TFT forecast deviations are review aids, not confirmed faults | Model decision; TA3 Review Prioritization | Project design | Descriptive ranking only. |

## Limitations and courses of action

Copied from `raw/limitations-course-of-action.md` (2026-09-29). Framework rule: a blocked arm does not stop the other.

### TFT forecasting

| # | Limitation | Course of action |
| --- | --- | --- |
| T1 | TFT has not been tested on this facility. Lim et al. (2021) establishes architecture, not AquaVir accuracy. Moon et al. (2018) is an LSTM EC comparator on one soilless line, not TFT or multi-zone. | Evaluate TFT later against last-value persistence and same-hour-previous-day baselines on each available facility series and zone. Report MAE and RMSE in physical units at hour 1, later horizons, and across the 24-hour trajectory. Do not quote another study's error as AquaVir performance. Keep Moon as a one-line EC comparator only. |
| T2 | A candidate target may lack adequate timestamped zone coverage. | Drop that target rather than imputing a forecast the series cannot support. Forecasting of covered targets continues. Align to an hourly grid only where source data support it. |
| T3 | Future sensor readings and interventions not known at forecast time must not be model inputs. | Allow only historical observations, zone metadata, and genuinely known future inputs. Split chronologically by forecast origin so each 24-hour outcome window lies wholly in its assigned period. |

### Random forest fault detection

| # | Limitation | Course of action |
| --- | --- | --- |
| R1 | Random forest needs verified normal and fault labels. Karimzadeh used artificially induced, labeled EC/pH faults; abstract opened, tables not. AquaVir has no confirmed labeled fault file. | If suitable labels are missing, state that the supervised detector cannot be validated. Continue with ranked absolute TFT forecast deviations as unconfirmed review signals. Do not treat those ranks as fault classifications. Report any later validated RF outputs separately. |
| R2 | Injected-fault accuracy in a methods paper is not operator-confirmed facility performance. | Evaluate RF only on verified labels. Report precision, recall, and false alarms with label source and denominator. Keep KNN as the simpler baseline. Separate sensor faults from operating changes and data-quality errors when labeling. |

### Cross-arm bottleneck

| Blocked condition | What stops | What continues |
| --- | --- | --- |
| No verified fault labels | Random-forest training and validation metrics | TFT forecasts for eligible targets; ranked unconfirmed review signals |
| Inadequate coverage for one target | That target's TFT forecast | Forecasts for other eligible targets; review ranking on produced forecasts; RF if labels exist |
| No facility series at all | Facility TFT evaluation and RF validation | Method design, baselines named for later use, and explicit “cannot validate” statements |

## Unresolved inputs

- No authorized AquaVir facility export or fault-label file is confirmed in the repository.
- Karimzadeh result tables remain paywalled; diagnosis numbers stay abstract-only.
- Lim publisher HTML was not opened; design claims rest on ar5iv of arXiv:1912.09363.
- Human confirmation of agent-opened locators is still outstanding.
- No second opened hydroponic random-forest fault study beyond S2.

## References

Karimzadeh, S., Li, Z., & Ahamed, M. S. (2025). Machine learning-based fault detection and diagnosis of electrical conductivity and pH sensors in hydroponic systems. *Computers and Electronics in Agriculture, 237*, 110544. https://doi.org/10.1016/j.compag.2025.110544

Lim, B., Arık, S. Ö., Loeff, N., & Pfister, T. (2021). Temporal Fusion Transformers for interpretable multi-horizon time series forecasting. *International Journal of Forecasting, 37*(4), 1748–1764. https://doi.org/10.1016/j.ijforecast.2021.03.012 (design passages opened via https://ar5iv.labs.arxiv.org/html/1912.09363)

López Santos, M., García-Santiago, X., Echevarría Camarero, F., Blázquez Gil, G., & Carrasco Ortega, P. (2022). Application of Temporal Fusion Transformer for day-ahead PV power forecasting. *Energies, 15*(14), 5232. https://doi.org/10.3390/en15145232

Metin, A., Kaşif, A., & Catal, C. (2023). Temporal fusion transformer-based prediction in aquaponics. *The Journal of Supercomputing*. https://doi.org/10.1007/s11227-023-05389-8

Moon, T., Ahn, T. I., & Son, J. E. (2018). Forecasting root-zone electrical conductivity of nutrient solutions in closed-loop soilless cultures via a recurrent neural network using environmental and cultivation information. *Frontiers in Plant Science, 9*, Article 859. https://doi.org/10.3389/fpls.2018.00859

## Revision and QA pointer

Independent QA of record: [`raw/dual-model-qa.md`](raw/dual-model-qa.md). Findings F1 and F2 were revised; the follow-up pass closed both and recorded **pass with limitations**. Unresolved limits in that file (facility data, Karimzadeh abstract-only tables, Lim publisher page, no hydroponic TFT-vs-LSTM win, human locator confirmation) remain.
