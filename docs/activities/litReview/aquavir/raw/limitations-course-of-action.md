# AquaVir: limitations and courses of action

Date: 2026-09-29  
Scope: design safeguards for TFT forecasting and random-forest fault detection. No facility metrics. No new papers. No AquaVir performance numbers.

**Framework bottleneck rule.** A failed or blocked arm must not stop the other arm. Missing fault labels block only random-forest validation. Weak or missing series block only that target's forecast. Review ranking still runs on whatever TFT forecasts are produced.

Sources used (read-only): `model-decision-2026-09-29.md`, `algorithm-review.md`, `evidence-ledger.md` (S1 Moon, S2 Karimzadeh), TA3 proposal §1 modules and §4 limitations.

---

## TFT forecasting

| # | Limitation | Course of action | Source file | Caveat |
| --- | --- | --- | --- | --- |
| T1 | TFT has not been tested on this facility. Lim et al. (2021) establishes the multi-horizon architecture, not AquaVir accuracy for these targets or zones. Moon et al. (2018) is an opened LSTM EC comparator on one soilless line, not a TFT or multi-zone result. | Evaluate TFT later against last-value persistence and same-hour-previous-day baselines on each available facility series and zone. Report MAE and RMSE in physical units at hour 1, later horizons, and across the 24-hour trajectory. Do not quote another study's error as AquaVir performance. Keep Moon et al. (2018) as a one-line EC comparator only. | `model-decision-2026-09-29.md` (Decision; Data and evaluation gate; Relationship to earlier work); `algorithm-review.md` (Gaps: reported accuracies are not AquaVir performance; What the thesis still has to obtain); TA3 §4 (models not yet tested on facility data; forecast quality depends on historical data) | Lim is an architecture citation. Moon test R²/RMSE belong to that paper's EC setup and must not be restated as AquaVir numbers. No facility export is confirmed. |
| T2 | A candidate target (pH, EC, humidity, nutrient-solution temperature, water level, light intensity, or ambient temperature) may lack adequate timestamped zone coverage. | Drop that target rather than imputing a forecast the series cannot support. Forecasting of covered targets continues. Align to an hourly grid only where the source data support it. | `model-decision-2026-09-29.md` (targets “where each is actually logged with adequate coverage”; check coverage before retaining); TA3 §1 Predictive Analysis Module and §4 Scope (each target included only where records have adequate coverage) | Weak or missing series block only that target's forecast, not the rest of the TFT arm or the review ranking on remaining forecasts. |
| T3 | Future sensor readings and interventions not known at forecast time must not be model inputs. | Allow only historical observations, zone metadata, and genuinely known future inputs such as calendar time or a documented schedule. Split chronologically by forecast origin so each 24-hour outcome window lies wholly in its assigned period. | `model-decision-2026-09-29.md` (Decision; Data and evaluation gate); TA3 §4 (historical sensor observations for predictive monitoring) | Leakage of retrospective interventions or future sensors would invalidate the evaluation even if MAE/RMSE look favorable. |

---

## Random forest fault detection

| # | Limitation | Course of action | Source file | Caveat |
| --- | --- | --- | --- | --- |
| R1 | Random forest needs verified normal and fault labels. Karimzadeh, Li, and Ahamed (2025) used artificially induced, labeled EC/pH faults; the abstract was opened and the result tables were not. AquaVir has no confirmed labeled fault file. | If suitable labels are missing, state that the supervised detector cannot be validated. Continue with ranked absolute TFT forecast deviations (size, persistence, affected variables, zones) as unconfirmed review signals. Do not treat those ranks as fault classifications. Report any later validated random-forest outputs separately from the review ranking. | `model-decision-2026-09-29.md` (Decision; label-unavailable ranking); `algorithm-review.md` (AlgoA unresolved without labels; S2 claim map); `evidence-ledger.md` S2; TA3 §1 Anomaly Detection and Review Prioritization modules; TA3 §4 (RF requires verified labels; without them performance cannot be evaluated) | Missing labels block only random-forest validation. TFT forecasting and review ranking on produced forecasts continue. Abstract accuracies (e.g. 93.7% EC / 96.5% pH) are not recomputed and are not AquaVir results. |
| R2 | Injected-fault accuracy in a methods paper is not operator-confirmed facility performance. | Evaluate random forest only on verified labels. Report precision, recall, and false alarms with the label source and denominator. Keep k-nearest neighbors as the simpler baseline named beside random forest in the 2026-09-28 review. Separate sensor faults from operating changes and data-quality errors when labeling. | `model-decision-2026-09-29.md` (Data and evaluation gate); `algorithm-review.md` (Karimzadeh comparison keeps KNN as baseline; What the thesis still has to obtain: injected faults ≠ operator-confirmed events); `evidence-ledger.md` S2 (faults artificially induced; diagnosis tables not opened) | Do not present Karimzadeh abstract figures as facility detector performance. Human confirmation of cited passages remains outstanding. |

---

## Cross-arm dependency (bottleneck)

| Blocked condition | What stops | What continues |
| --- | --- | --- |
| No verified fault labels | Random-forest training and validation metrics | TFT forecasts for eligible targets; ranked unconfirmed review signals |
| Inadequate coverage for one target | That target's TFT forecast | Forecasts for other eligible targets; review ranking on produced forecasts; RF if labels exist |
| No facility series at all | Facility TFT evaluation and RF validation | Method design, baselines named for later use, and explicit “cannot validate” statements |

---

## Ungrounded items

None of the required pairs above lacked a source caveat in the read-only files. Lim et al. (2021) appears in the model decision and TA3 references as the TFT architecture source; facility non-testing and “do not quote another study's error” are explicit in the model decision and algorithm-review gaps.
