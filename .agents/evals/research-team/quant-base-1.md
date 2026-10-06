# Baseline evaluation 1: Hydroponic zone anomaly analysis

**Source:** `docs/activities/litReview/docs/TS31_Django_FeasibilityStudy_TargetTitles (1).md`, hydroponics proposal and final recommendation only. No raw data were available or analyzed.

**Assessment:** The proposed analysis is technically plausible but cannot yet be performed or empirically evaluated. The study proposes a zone-by-timestamp multivariate record, zone baselines, cross-zone consistency scores, and prioritized anomaly alerts. It explicitly says the facility, data access, and dataset have not been confirmed; dataset feasibility is rated 2/5. Its conclusion is conditional on securing at least three operationally distinct zones and sufficient usable sensor and operational data. The suggested 10,000+ records are a collection target, not an observed sample size or evidence of performance.

**Fields and evidence still needed:**

- A real export with zone identifiers, timestamps and time zone, sensor identifiers, units, logging frequency, historical coverage, and enough overlapping records to compare at least three operationally meaningful zones.
- Actual time series for the available measurements. The proposal names pH, EC/TDS, nutrient-solution temperature, and water level; it also mentions humidity and other contextual variables. Which of these are logged, at what quality and cadence, must be verified.
- Operational context for interpretation and fair comparisons: pump activity, dosing, water replacement, maintenance and interventions, crop stage, equipment status, and historical alerts where available.
- Data-quality evidence: missingness, timestamp alignment, implausible readings, sensor drift or faults, calibration/maintenance history, and any changes in logging or zone operation.
- Event records or operator review of flagged periods to judge alert usefulness and false alarms. The proposal notes that anomaly labels may be limited and operator confirmation is needed.
- Written permission, data dictionary, and a sample extract to establish access and the meaning of each field.

**Permissible conclusion now:** A conditional feasibility judgment and a data-validation plan. No anomaly rate, zone ranking, detection accuracy, false-alarm reduction, or intervention effect can be calculated from this proposal alone. Bibliography entries support background rationale, not a measured result for this facility.
