# AquaTerra title proposal: issues to address

Source: [TA3 title proposal](https://docs.google.com/document/d/1_BWHks7gI7yZhWtuWVWw030jxHhdJJNqV5VFbSV_rrg/edit?tab=t.98khqeenv0fw), reviewed 2026-10-22. This is a proposal QA log, not a record of completed analysis. Statuses describe evidence available to the group during the grilling.

## Open issues

### AQ-01 — Confirm a viable forecasting panel

- **Severity:** Critical feasibility gate
- **Status:** Open; the group said on 2026-10-22 that it has not checked the data yet.
- **Proposal location:** §4, Scope and Limitations; §3, Objectives 1–2.
- **Issue:** The proposal leaves provinces, fish categories, and study years to later selection. It has not demonstrated that the quarterly marine municipal landing volume and value records form a sufficiently complete, comparable province × category × quarter panel for model fitting and a later-period test. A listed public table is evidence of a possible source, not evidence that the selected panel is usable.
- **Evidence to inspect:** PSA OpenSTAT [volume metadata](https://openstat.psa.gov.ph/Metadata/2E4GVMP0) and [value metadata](https://openstat.psa.gov.ph/Metadata/2E4GCMP0), plus actual exports for candidate provinces, categories, and years. Record download date and table identifiers.
- **Required action:** Name a small candidate scope; export matching quarterly volume and value series; document units, category/geography definitions, missing and suppressed cells, zero values, revisions or breaks, and the number of usable quarters per series. Reserve later quarters for testing before selecting models or predictors. Confirm which historical values and reference prices would have been available at each forecast date.
- **Closure criterion:** A dated panel audit names the retained provinces, categories, years, usable quarters, exclusions, forecast dates, and held-out periods, and shows that both forecast evaluation and the proposed exposure calculation are possible. If the audit fails, reduce the scope or revise the title and objectives before implementation.

### AQ-02 — Enforce forecast-date availability for environmental predictors

- **Severity:** Critical validity gate
- **Status:** Open; the group said on 2026-10-22 that it has not checked forecast-date availability.
- **Proposal location:** §1, Area of Investigation; §3, Objective 2; §4, Scope and Limitations.
- **Issue:** The proposal names rainfall, sea surface temperature, prior typhoon exposure, and mangrove history as predictors of next-quarter landings, but does not specify the information cutoff and publication lag for each predictor. Using realized conditions from the quarter being forecast, or a historical data product that was published later, would leak future information into retrospective tests. This could invalidate the claimed forecast and the predictor-contribution comparison.
- **Required action:** Define each forecast origin (for example, the last day of the preceding quarter). For every predictor, document the observation period, original publication or revision date, geographic aggregation, and whether the value would have been known at that origin. Use only lagged observations or genuine forecasts issued by then; exclude unavailable predictors. Build historical test features with the same cutoff, including any fisheries-data publication lag.
- **Closure criterion:** A dated feature-availability table and backtest protocol show the exact value permitted at every forecast origin. Reproduce the held-out evaluation using only those values; if historical release vintages cannot be established, state the limitation and do not claim a real-time forecast evaluation from revised retrospective products.

## QA disposition

The proposal's data feasibility and forecast validity remain **unverified** while AQ-01 and AQ-02 are open. No AquaTerra dataset or model results were analyzed for this log.
