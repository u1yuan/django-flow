# AquaVir model decision: TFT forecasting and random forest fault detection

Date: 2026-09-29  
Status: selected design; performance unvalidated

## Decision

The group selected a **Temporal Fusion Transformer (TFT)** for multivariate sensor forecasting and plans a **random forest** for supervised sensor-fault detection. The working title is *AquaVir: Multi-Zone Hydroponic Sensor Forecasting and Fault Detection with TFT and Random Forest*. This supersedes the LSTM EC model choice in the [2026-09-28 algorithm review](algorithm-review.md) as a project decision. It does not change that review's evidence or imply that a TFT has been tested on hydroponic facility data.

The forecasting targets are pH, electrical conductivity (EC), humidity, nutrient-solution temperature, water level, light intensity, and ambient temperature **where each is actually logged with adequate coverage**. For each eligible target and zone, the intended output is one forecast per hour for the next 24 hours. TFT can use historical sensor observations, zone metadata, and genuinely known future inputs such as calendar time or a documented schedule. Future sensor readings and interventions not known at forecast time must not be used as inputs. The original TFT work establishes the architecture's multi-horizon design, not its accuracy for this facility or these seven targets ([Lim et al., 2021](https://doi.org/10.1016/j.ijforecast.2021.03.012)).

The random forest would classify **labeled** sensor faults. A hydroponic EC/pH study reports random-forest fault detection on artificially induced, labeled faults; it does not show that a random forest can learn confirmed faults from unlabeled zone data ([Karimzadeh, Li, and Ahamed, 2025](https://doi.org/10.1016/j.compag.2025.110544)). If suitable labels are unavailable, report that the supervised detector cannot be validated; forecast deviations may still be shown for operator review but are not confirmed faults.

When labels are unavailable, the dashboard may rank absolute TFT forecast deviations for operator review by size, persistence, affected sensor variables, and zones. This ranking is a descriptive review aid, not a trained fault detector or evidence of a physical fault. Report any validated random-forest classifications separately from these unconfirmed review signals.

## Data and evaluation gate

- Obtain authorized, timestamped, zone-identified records and a data dictionary. Check each proposed target's units, logging frequency, missingness, historical coverage, sensor resolution, and maintenance or control events before retaining it. No facility export or fault-label file is confirmed in this repository.
- Align readings to an hourly grid only where the source data support it. Compare TFT with last-value persistence and same-hour-previous-day forecasts for each available target and zone. Report MAE and RMSE in the target's physical units at hour 1, each later horizon, and across the 24-hour trajectory. Do not quote another study's error as AquaVir performance.
- Split chronologically by forecast origin so each 24-hour outcome window lies wholly in its assigned training, validation, or test period. Fit preprocessing on training data, tune on validation, and use the final test once. Do not give TFT future sensor readings or retrospectively recorded interventions.
- Evaluate the random forest only if normal and faulty examples have verified labels. Separate sensor faults from operating changes and data-quality errors, and report fault-specific precision, recall, and false alarms with the label source and denominator.

## Relationship to earlier work

[Moon, Ahn, and Son (2018)](https://doi.org/10.3389/fpls.2018.00859) support LSTM forecasting of root-zone EC on one soilless cultivation line. That remains a relevant comparator, but does not establish performance for TFT or for multi-zone forecasts of every listed sensor. The [earlier algorithm review](algorithm-review.md), its [evidence ledger](evidence-ledger.md), and the feasibility study remain dated records rather than results of the new design.

This decision was assisted by AI discussion and is recorded in the course [AI interaction log](../../tp1/AI_INTERACTION_LOG.md). The group must independently check citations and method claims before submission.
