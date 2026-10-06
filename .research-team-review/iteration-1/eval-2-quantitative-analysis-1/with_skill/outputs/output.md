# Hydroponic zone anomaly analysis: data feasibility

## Decision

The feasibility study supports a **conditional plan** for multi-zone anomaly analysis, but analysis is **not currently possible from this document alone**. It provides no zone-level sensor export or operational event records. The study itself says that no facility or dataset has been confirmed and rates dataset feasibility 2/5 ([feasibility study, lines 148–152](../../../docs/activities/litReview/docs/TS31_Django_FeasibilityStudy_TargetTitles%20(1).md)). Its proposed 10,000+ zone-time records are a collection target, not an observed sample size ([line 31](../../../docs/activities/litReview/docs/TS31_Django_FeasibilityStudy_TargetTitles%20(1).md)). No anomaly count, score, rate, effect size, or test result can be calculated.

## Required data and checks

The proposed observational unit is one **zone × timestamp × multivariate sensor/operational state** ([line 31](../../../docs/activities/litReview/docs/TS31_Django_FeasibilityStudy_TargetTitles%20(1).md)). To assess whether those observations support the intended comparisons, obtain an authorized sample export and data dictionary with:

- A stable facility and zone identifier; confirmation that at least three zones are operationally distinct and reasonably comparable.
- Timestamp, time zone, logging interval, historical start/end dates, and synchronization method across sensors and zones. Document duplicate, missing, and misaligned timestamps.
- Actual available sensor measurements, including the study's candidate pH, EC/TDS, nutrient-solution temperature, water level, and any humidity data; units, sensor IDs, calibration/maintenance history, valid ranges, and missing or fault codes.
- Operational context with timestamps and zone/asset links where available: pump activity, dosing, water replacement, maintenance, interventions, crop stage, equipment status, and historical alerts. These factors may explain shifts that should not automatically be called anomalies ([project overview, line 27](../../../docs/activities/litReview/docs/TS31_Django_FeasibilityStudy_TargetTitles%20(1).md)).
- Event definitions and operator-reviewed records, if alert usefulness, false alarms, detection delay, or anomaly recall are to be evaluated. Record the reviewed period and denominator, including what remains unlabeled.
- Data-access permission and export format, coverage, retention, missingness, and sensor-fault/drift information. The proposal explicitly calls for these validation steps before zone comparison or scoring ([lines 29–31](../../../docs/activities/litReview/docs/TS31_Django_FeasibilityStudy_TargetTitles%20(1).md)).

Once an authorized extract exists, first audit coverage and quality by zone and time, align comparable measurements, distinguish sensor faults from operational events, and define baseline/training and evaluation periods before estimating zone consistency or anomaly performance. Any such result would need its actual observed denominator and validation method. This document permits only the feasibility judgment above.
