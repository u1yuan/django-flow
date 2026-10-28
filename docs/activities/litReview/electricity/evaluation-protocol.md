# Electricity thesis: preregistration-style feasibility and evaluation protocol

**Status:** proposed methods, 28 October 2026. No model or Philippine validation result is reported here. This work is separate from the hydroponics and diesel tracks.

**Data-date requirement:** use observation timestamps on or after 2020-01-01 for outcomes, predictors, tariffs, weather, and any other time-varying input. If a source spans earlier years, exclude those rows before building features, splits, or counts. A dataset's publication date is not its observation date.

## Gate and observation units

The course Data Science guideline, section 4.1, calls for at least 10,000 dataset records; section 4.4 requires ethical sourcing and privacy compliance. For this screen, a record means one **valid prediction target** after cleaning and creation of the required history, not one raw reading, overlapping window, or filled-in target. Report the number of distinct households or meters, their eligible dates, and the distribution of target counts per entity alongside the total. An eligible total is a feasibility check, not a claim of 10,000 independent entities.

| Topic | Observation unit and outcome | Minimum gate | Target exclusions |
| --- | --- | --- | --- |
| Household high-use alert | Household-day; next day's measured kWh and a binary high-use label | 10,000 complete future household-days with valid history | Missing or reset cumulative readings that prevent a measured daily difference; partial day; missing required lag; duplicate or unresolvable timestamps |
| Institutional high-load forecast | Electricity meter-hour; next hour's measured energy in kWh | 10,000 valid future meter-hours with required history | Non-electricity meters, invalid units, missing target or lag, duplicate or unresolvable timestamps |
| Time-of-use charge forecast | Household-hour; next hour's measured kWh and its matched 2020+ price signal | 10,000 measured future intervals with valid history and a unique timestamp-to-price match | Missing/ambiguous price, missing energy target or lag, duplicate or unresolvable timestamps |

Before counting, record the exact source release and files, time zone and daylight-saving convention, timestamp meaning (interval start or end), units, duplicates, negative or reset values, expected cadence, and missingness by entity and time. A gap cannot be bridged by treating two distant readings as one interval. Keep raw data immutable and publish only scripts, aggregate counts, and a source manifest unless reuse terms allow more. The iFlex price-signal join requires the correct publication time and effective interval; a date-only match is insufficient. For RECON-SL, monthly consumption is contextual information unless billing-cycle boundaries are confirmed. Never use future monthly totals as forecast inputs.

## Forecast and alert design after a gate passes

Use a chronological split with a final untouched future test period. Choose feature engineering, high-use threshold, model, and hyperparameters on training and validation periods only. Produce lag features solely from observations available at forecast issue time. Prefer a common global calendar cutoff so simultaneous households or meters do not leak future information across entities. Report the period, entity coverage, and missingness of each split; check whether a held-out-entity test is feasible as a separate transfer question.

Compare against simple, time-aware baselines: last observed interval, same interval on the previous day, and same interval on the previous week where history exists. For daily household kWh, use previous day and same day of week in the prior week. Evaluate kWh forecasts with MAE and a scale-aware measure whose denominator is stated; do not use MAPE where zero or near-zero consumption makes it unstable. Report pooled error and the distribution of per-household or per-meter error, including the number of entities that can be scored. Score only observed targets; record how many predictions each baseline could make.

For a household high-use alert, predefine a training-period threshold (for example, an entity-specific upper quantile only if enough training days exist) and apply it unchanged to future days. Record the threshold rule, number of positive future days, precision, recall, and false alerts per household-month; compare with a simple historical-use alert. A forecast-derived institutional high-hour alert uses a separately fixed kWh threshold and the observed high-hour label. It is **hourly energy**, not instantaneous demand or a billed demand charge.

For time-of-use, calculate each forecast interval's energy charge as predicted kWh multiplied by the verified matched price, with price units converted explicitly. Compare with the analogous charge calculated from observed kWh; aggregate only over fully specified intervals and report coverage. This excludes fixed fees, taxes, other billing components, and Philippine tariff claims. If future price publication is unavailable at forecast issue time, evaluate an operational scenario using only the price then known, or mark the charge forecast infeasible.

## Client validation and final choice

Use structured interviews to test the decision each output would support, the action window, tolerable error or alert burden, and whether an authorized data owner can provide comparable historical readings. Keep user feedback separate from statistical accuracy. Do not assume published descriptions of a metering system imply export access. Obtain written data-use terms before any local transfer; minimize or de-identify household data as required by the owner and ethics review. Test Philippine predictive performance only on permitted local observations, with a separate chronological evaluation.

Recommend a final topic in this order: valid relevant data, measurable target, willing operational validator, then feasible access and reuse terms. A topic without 10,000 eligible targets stops at the data gate. A topic with public-data feasibility but no local access may support a foreign-data methods study, with transfer to the Philippines stated as unvalidated. No supervised fault-detection claim belongs to these three topics without verified fault labels.

## Pending decisions and evidence

- Actual eligible target counts and source-specific exclusions: see the data feasibility report when completed.
- Final license and redistribution terms: see the source ledger; publisher or owner permission controls any redistribution.
- Household high-use threshold and minimum history: freeze after source inspection and before test-period scoring.
- Philippine operational reviewer, authorized data export, historical rates, and any ethics approval: unverified.

**Local guideline:** `docs/CS-Guideline-as-of-Nov-17-as-430pm-without-signature (1).md`, sections 4.1 and 4.4, inspected 28 October 2026. The existing local edit to that file was not made for this activity.
