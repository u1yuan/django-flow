# AquaTerra proposal QA: issues to resolve

Source: [TA3 title proposal](https://docs.google.com/document/d/1_BWHks7gI7yZhWtuWVWw030jxHhdJJNqV5VFbSV_rrg/edit?tab=t.98khqeenv0fw). Review date: 2026-10-22. The group reported that it has not checked the proposed data or design. All 13 issues remain open.

## QA decision

**Needs revision before feasibility approval.** Three critical gates are unresolved: a usable landing-data panel (AQ-01), predictors available at each forecast date (AQ-02), and a fixed shortfall definition (AQ-03). Other issues test whether the study has enough data, adds value beyond simple baselines, and fits an undergraduate timeline. An open flag is a check to complete, not proof that the study will fail.

## Decision order

| Stage | Resolve | Evidence needed | Decision |
| --- | --- | --- | --- |
| 1. Data gate | AQ-01, AQ-06, AQ-11 | Small province–category panel audit; matched price records; source and product manifest | Keep or narrow the target and economic objective. |
| 2. Forecast gate | AQ-02, AQ-03, AQ-07 | Forecast-origin feature table; worked shortfall rule; defensible spatial joins | Keep or drop environmental predictors. |
| 3. Test gate | AQ-05, AQ-04, AQ-08, AQ-09 | Event counts; simple baselines; chronological backtest and metric plan | Decide whether GAMMs and Random Forests can both be evaluated. |
| 4. Thesis gate | AQ-13, AQ-10, AQ-12 | Primary contribution test; minimum work plan; bounded user claims | Set title, required deliverable, and optional dashboard work. |

Issue IDs stay fixed for follow-up. Each issue states the concern, required check, and evidence that closes it.

## 1. Evidence and data access

### AQ-01 — DATA: Provinces, Types of Fish

- **Severity:** Critical feasibility gate
- **Status:** Open; the group said on 2026-10-22 that it has not checked the data yet.
- **Proposal location:** §4, Scope and Limitations; §3, Objectives 1–2.
- **Issue:** The proposal leaves provinces, fish categories, and study years to later selection. It has not demonstrated that the quarterly marine municipal landing volume and value records form a sufficiently complete, comparable province × category × quarter panel for model fitting and a later-period test. A listed public table is evidence of a possible source, not evidence that the selected panel is usable.
- **Evidence to inspect:** PSA OpenSTAT [volume metadata](https://openstat.psa.gov.ph/Metadata/2E4GVMP0) and [value metadata](https://openstat.psa.gov.ph/Metadata/2E4GCMP0), plus actual exports for candidate provinces, categories, and years. Record download date and table identifiers.
- **Required action:** Name a small candidate scope; export matching quarterly volume and value series; document units, category/geography definitions, missing and suppressed cells, zero values, revisions or breaks, and the number of usable quarters per series. Reserve later quarters for testing before selecting models or predictors. Confirm which historical values and reference prices would have been available at each forecast date.
- **Closure criterion:** A dated panel audit names the retained provinces, categories, years, usable quarters, exclusions, forecast dates, and held-out periods, and shows that both forecast evaluation and the proposed exposure calculation are possible. If the audit fails, reduce the scope or revise the title and objectives before implementation.

### AQ-06 — Validate the first-sale price and gross-value calculation

- **Severity:** High economic-measure validity risk
- **Status:** Open; compatibility and historical availability have not been checked.
- **Proposal location:** §1, Shortfall and Economic Exposure module; §3, Objectives 3–4; §4, Scope and Limitations.
- **Issue:** The proposal allows direct first-sale prices or value ÷ positive volume as a proxy, but neither has been matched to the selected *marine municipal* province–category records and forecast dates. PSA has a [quarterly fisheries farmgate price table](https://openstat.psa.gov.ph/Metadata/2M4GFPF0); its published metadata do not by themselves establish that every required marine municipal series is available and compatible. Mixed subsectors, units, categories, inflation periods, or contemporaneous prices would change the interpretation. A value/volume ratio may reproduce reported value rather than serve as an independently observed price.
- **Required action:** Check direct price cells first; record subsector, province, species, period, unit (for example, pesos/kg), and release date. If using value/volume, reconcile metric tons against value in thousand pesos and explain its proxy status. Select a price known at the forecast origin, and test sensitivity with at least one predeclared alternative.
- **Closure criterion:** A worked unit calculation and source-matching table show a compatible historical price for every retained series and forecast origin, or the economic objective is narrowed. Report the result as indicative gross landing value below a benchmark, not verified income or profit loss.

### AQ-11 — Verify source claims, metadata, and release assumptions

- **Severity:** Medium research-integrity risk
- **Status:** Open; the group said it has not checked the proposal's sources.
- **Proposal location:** §2, Background and Rationale; §4, data sources; §7, References.
- **Issue:** The proposal cites literature for novelty and predictor rationale and names five public datasets, but does not attach a claim-to-source audit, exact data-product versions, access dates, release lags, or reproducible extraction plan. The presence of a DOI or bibliography entry does not verify the associated sentence. For example, the opened [Holmes et al. article](https://onlinelibrary.wiley.com/doi/abs/10.1111/fog.12541) concerns Indian oil sardine and does not establish that the proposed Philippine province/category predictors will help.
- **Required action:** Open each source used for a material claim; verify bibliographic metadata and the exact supporting passage. Record product identifiers/versions, links, licenses, geography, temporal resolution, download dates, and extraction scripts or steps. Separate literature findings from AquaTerra design choices and projected benefits.
- **Closure criterion:** A source/claim ledger and reproducible data manifest support every retained factual claim and dataset dependency; unsupported statements are qualified or removed.

## 2. Forecast definition and predictor validity

### AQ-02 — RRS: Prior Studies to define baseline/forecast origin for forecasting

- **Severity:** Critical validity gate
- **Status:** Open; the group said on 2026-10-22 that it has not checked forecast-date availability.
- **Proposal location:** §1, Area of Investigation; §3, Objective 2; §4, Scope and Limitations.
- **Issue:** The proposal names rainfall, sea surface temperature, prior typhoon exposure, and mangrove history as predictors of next-quarter landings, but does not specify the information cutoff and publication lag for each predictor. Using realized conditions from the quarter being forecast, or a historical data product that was published later, would leak future information into retrospective tests. This could invalidate the claimed forecast and the predictor-contribution comparison.
- **Required action:** Define each forecast origin (for example, the last day of the preceding quarter). For every predictor, document the observation period, original publication or revision date, geographic aggregation, and whether the value would have been known at that origin. Use only lagged observations or genuine forecasts issued by then; exclude unavailable predictors. Build historical test features with the same cutoff, including any fisheries-data publication lag.
- **Closure criterion:** A dated feature-availability table and backtest protocol show the exact value permitted at every forecast origin. Reproduce the held-out evaluation using only those values; if historical release vintages cannot be established, state the limitation and do not claim a real-time forecast evaluation from revised retrospective products.

### AQ-03 — Define the seasonal benchmark and shortfall event before testing

- **Severity:** Critical construct and evaluation gate
- **Status:** Open; the group said on 2026-10-22 that it has not checked any of the proposal's design details.
- **Proposal location:** §3, Objectives 1 and 4; §4, Scope and Limitations.
- **Issue:** “Historical seasonal benchmark,” “shortfall,” and “economically significant” are not operationally defined. Different lookback windows, statistics, trend treatment, and thresholds can create different event labels and exposure amounts. A benchmark computed from the full record would also leak test-period information.
- **Required action:** Predefine, per province–category series, a benchmark using only quarters preceding each forecast origin; specify lookback length, same-quarter statistic, minimum history, treatment of trend/structural breaks, and whether a tolerance below the benchmark is needed. Fix the economically significant threshold or ranking rule using training/validation data and an explicit planning rationale.
- **Closure criterion:** A worked example for one historical forecast date shows the input quarters, benchmark, shortfall threshold, observed event label, and exposure calculation; the rule is frozen before the final test.

### AQ-07 — Specify spatial linkage and the role of mangroves and typhoons

- **Severity:** High predictor-validity and scope risk
- **Status:** Open; spatial linkage and predictor usefulness have not been checked.
- **Proposal location:** §1, environmental predictors; §3, Objective 2; §4, limitations.
- **Issue:** A province where fish are landed need not be where they were caught, so assigning coastal rainfall, SST, cyclone exposure, or mangrove extent to that province is an untested proxy. The cited [Global Mangrove Watch v3 dataset](https://doi.org/10.5281/zenodo.6894273) provides selected annual epochs through 2020, not a quarterly mangrove series for the full proposed forecast span. JAXA now lists a newer v4.1 product, but its retrospective maps were released in 2026 and cannot simply be treated as historically available at earlier forecast dates ([JAXA dataset page](https://www.eorc.jaxa.jp/ALOS/en/dataset/gmw_e.htm)).
- **Required action:** Define the geographic footprint and aggregation for each environmental source, justify its link to landing records, and document temporal resolution and vintage. Treat mangrove history as a slow-moving, optional predictor; compare a landings-only model, a compact weather model, and additions of typhoon/mangrove features separately. Drop predictors that cannot be defensibly linked or backtested.
- **Closure criterion:** A feature dictionary and maps/tables document the spatial and temporal join, source vintage, missingness, and ablation results without causal claims.

## 3. Model feasibility and evaluation

### AQ-05 — Test whether the panel supports the proposed model complexity

- **Severity:** High feasibility and overfitting risk
- **Status:** Open pending AQ-01's panel audit.
- **Proposal location:** Title; §1, GAMM and Random Forest modules; §3, Objective 2.
- **Issue:** Quarterly records give few time points per province–category series even when the pooled row count looks large. Correlated series, rare shortfalls, many predictor variants, GAMM smooths/random effects, and Random Forest tuning reduce the effective evidence available for a fair comparison. The proposal does not set a minimum history or a complexity limit.
- **Required action:** Count usable quarters and shortfall events per retained series and across the pooled panel; document dependence among series. Predefine a compact predictor set and constrained tuning budget. Simplify geography/categories or use a simpler model if the panel cannot support both named methods.
- **Closure criterion:** A sample-size and event-count table supports the selected model structure and a held-out period; the protocol states a fallback model/scope if it does not.

### AQ-04 — Add simple forecast and decision baselines

- **Severity:** High; required to establish a Data Science contribution
- **Status:** Open; baseline comparison is not specified in the proposal.
- **Proposal location:** §3, Objective 2; §4, Scope.
- **Issue:** Comparing only GAMMs with Random Forests cannot show whether either improves on a simple seasonal or recent-history forecast. The economic layer also needs a simple prioritization comparator to show whether model forecasts improve decisions beyond historical shortfall frequency or benchmark-based ranking.
- **Required action:** Predefine at least a seasonal naive volume forecast (same quarter of the previous year) and an appropriate simple historical/rolling comparator. Apply the same forecast origins, panel, benchmarks, and metrics to every method. Compare economic ranking against a simple historical rule using the same price assumptions.
- **Closure criterion:** Held-out results report both proposed models alongside the simple baselines, with the number of forecast origins and series for every metric. A complex model is not claimed useful solely because it beats the other complex model.

### AQ-08 — Predefine a realistic chronological evaluation

- **Severity:** High validity risk
- **Status:** Open; the proposal names later periods but no exact split or rolling procedure.
- **Proposal location:** §1, Model Evaluation module; §3, Objectives 2 and 4; §4, Scope.
- **Issue:** A single unspecified “later period” may yield too few independent next-quarter forecasts and shortfall events. Tuning model variants, feature sets, benchmarks, and thresholds against the final period would overfit the test. Random row splits would be invalid for a next-quarter task.
- **Required action:** Specify rolling or expanding forecast origins, training and validation windows, a final untouched test period, and what gets refit at each origin. Keep all data preparation, benchmarks, feature selection, and price choices inside the appropriate training/validation history. Record the count of test origins, series, and shortfall events. Include uncertainty across origins or series where supportable.
- **Closure criterion:** A dated backtest diagram and executable protocol establish that every test prediction is generated from information available at its origin; final metrics carry denominators and uncertainty or an explicit small-sample limitation.

### AQ-09 — Make event and ranking metrics interpretable

- **Severity:** Medium to high evaluation risk
- **Status:** Open; event prevalence, ranking target, and success threshold are unspecified.
- **Proposal location:** §3, Objectives 2 and 4; §4, evaluation measures.
- **Issue:** Precision and recall depend on the shortfall definition and may be unstable with few events. “Reliability of ranking economically significant shortfalls” lacks a unit of analysis, top-k or threshold, and loss function. MAE, RMSE, and MASE across heterogeneous species/provinces are not directly comparable without aggregation rules and denominators.
- **Required action:** Predefine event prevalence reporting; per-series and aggregate metric rules; what is ranked (province–category–quarter combinations); top-k or threshold; and an evaluation such as recall among the top-k or error in realized gross-value shortfall. State how zero/near-zero seasonal naive errors affect MASE. Report false alarms and missed events, not only average volume error.
- **Closure criterion:** One evaluation table template shows units, denominators, event counts, and the planning decision represented by each metric before model results are seen.

## 4. Contribution and undergraduate scope

### AQ-13 — Show that the contribution exceeds a price conversion

- **Severity:** High under-scoping risk
- **Status:** Open; the claimed contribution has not been demonstrated.
- **Proposal location:** §2, Background and Rationale; §3, Objectives 3–4.
- **Issue:** The proposal correctly recognizes prior Philippine fisheries forecasting work. Turning a forecast shortfall into pesos by multiplying by a reference price is a straightforward calculation; a dashboard alone does not establish a distinct Data Science contribution. The proposed contribution becomes substantive only if the shortfall and economic-priority estimates are defined and evaluated against simple decision baselines on unseen periods.
- **Required action:** State a falsifiable primary question: whether the forecast-based method identifies and ranks future gross-value shortfalls better than a simple historical rule. Predefine an improvement criterion and report negative or inconclusive results. Keep economic interpretation indicative and distinguish predictive utility from causal or welfare claims.
- **Closure criterion:** The protocol and final results include a held-out comparison of the economic-priority output with a simple comparator, with transparent denominators and uncertainty. If the difference cannot be evaluated, narrow the contribution claim and title.

### AQ-10 — Establish a minimum viable undergraduate scope

- **Severity:** High schedule and over-scoping risk
- **Status:** Open; no deliverable priority or stop rule is specified.
- **Proposal location:** §1, seven proposed modules; title; §3, four objectives.
- **Issue:** The proposal combines multi-source geospatial data engineering, two model families, predictor ablations, shortfall-event testing, price sensitivity, economic ranking, and a web dashboard. The title commits to both GAMMs and Random Forests before panel size and feature feasibility are known. This breadth can consume the available time before the core forecast can be evaluated.
- **Required action:** Define a staged minimum: (1) a small, audited landing panel and frozen shortfall rule; (2) simple baseline and one feasible forecast model with valid backtesting; (3) compatible historical price and transparent exposure estimate. Add the second model, optional environmental features, and dashboard only after the core passes data and evaluation gates. Set a calendar decision point for reducing the title if either named method cannot be evaluated.
- **Closure criterion:** A term-by-term work plan names the required thesis result, optional extensions, owners, data gates, and the decision date for a narrower title.

### AQ-12 — Bound stakeholder and SDG claims to what the study can measure

- **Severity:** Medium scope and interpretation risk
- **Status:** Open; beneficiary needs and deployment have not been validated.
- **Proposal location:** §1, purpose and dashboard; §5, Target Beneficiaries; §6, SDG categories.
- **Issue:** Forecast and ranking accuracy alone cannot establish improved supply planning, assistance allocation, fisherfolk livelihoods, or ecological outcomes. The proposal already says rankings should not automatically determine assistance eligibility, but the intended decision process and stakeholder validation remain unspecified.
- **Required action:** Name one primary user and one concrete decision the output could inform. Decide whether stakeholder interviews/usability work are in scope; if absent, describe the dashboard as a prototype and the benefits as potential applications. Preserve the distinction between landed volume, catch location, fish populations, and household welfare.
- **Closure criterion:** The beneficiary/SDG prose and evaluation match the evidence actually collected; any claimed operational benefit is supported by a defined user evaluation, otherwise it is framed as a prospective use.

## Evidence boundary

No AquaTerra dataset, source export, or model result was analyzed for this log. Linked source pages establish only what those pages describe. Reassess after the panel audit, feature-availability table, and benchmark rule are complete.
