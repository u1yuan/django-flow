# Electricity thesis feasibility package

Prepared 28 October 2026 for the three locked electricity topics. This folder is separate from the hydroponics and diesel work. The [source ledger](source-ledger.md) has official dataset URLs, publisher claims, access and reuse caveats, and the Philippine client priority matrix. The [data feasibility report](data-feasibility.md) gives target definitions, the current gate status, access evidence, and a future counting procedure. The [evaluation protocol](evaluation-protocol.md) defines time-based comparisons and claims permitted after a gate passes. The [client pack](client-outreach-pack.md) contains an interview guide, sample-data request, and **unsent** outreach drafts. The [AI interaction log](AI_INTERACTION_LOG.md) records AI assistance. The [QA report](qa-review.md) records independent review when complete.

**Date cutoff:** every observation used must be dated 2020-01-01 or later, including targets, features, tariff matches and external regressors. The initial candidate matrix in the feasibility report is superseded where its source predates the cutoff.

| Topic | 10,000 valid-target gate | Operational review | Current decision |
| --- | --- | --- | --- |
| Next-day household high-use alerts | Pending full RECON-SL count; its 2022–2025 dates meet cutoff | Residential/customer route unconfirmed | Retain for data screening |
| Next-hour institutional high-load forecasts | Pending COFACTOR count restricted to 2020+; BDG2's 2016–2017 readings are excluded | FEU Manila first reviewer candidate; no participation confirmed | Retain for data and client screening |
| Time-of-use energy-charge forecasting | Pending iFlex 2020–2021 count and price join; London's 2013 tariff cohort is excluded | Meralco/customer tariff review unconfirmed | Retain for data screening |

**Philippine local series found:** NGCP hourly demand by grid is a public post-2020 candidate for grid-level work, but it is not a household or institutional meter series. No public local dataset matching the three customer-level targets was verified. Client-provided local data, if authorized, must contain only 2020+ observations. No local data or client permission is confirmed, no model has been fit, and no Philippine predictive accuracy is claimed. No dataset was downloaded; official URLs are supplied for later access.

The next decision point is to review the source and outreach pack with the group, obtain files only if authorized in a later step, and run the three gates. The final topic is then selected by valid relevant data, measurable target, a willing operational validator, and feasible access terms, in that order.
