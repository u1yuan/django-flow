# Electricity thesis client review pack — drafts for approval

Prepared 2026-10-28. **No message has been sent.** The three outputs under discussion are (1) next household-day high-use alerts, (2) next-hour building electricity kWh forecasts and high-hour alerts, and (3) next-hour household kWh with a matched 2020+ price signal to calculate an energy charge. All observed data in a local export must be dated 2020-01-01 or later. This pack seeks feedback and a possible permitted sample. It does not ask anyone to endorse accuracy on Philippine data before testing.

## Short interview guide (20–30 minutes)

1. **Decision and user.** Which decision would a forecast or alert change? Who sees it, when must it arrive, and what action could they take? What would make a false alarm or missed event costly?
2. **Target and boundary.** For a building, is the useful quantity hourly energy (kWh), maximum demand (kW), or something else? Which building, feeder, tenant or household does the meter cover? For a household, is “high use” relative to that household's prior days, a fixed threshold, or a bill target?
3. **Records and rights.** Who owns the meter readings and can authorize a de-identified export? Are there partner, tenant or utility restrictions? What review and publication terms would apply?
4. **Schema and history.** What are the timestamp zone and interval convention; units; cumulative versus interval readings; expected cadence; start/end dates; resets; missingness; holidays or operating schedules? How much uninterrupted history exists?
5. **Tariff linkage.** If reviewing energy charges, which tariff applied to which account and dates, and is a historical interval price schedule available? Which bill components would remain outside a calculated energy charge?
6. **Evaluation and review.** Could staff review several anonymized forecast/alert examples and label whether each would have been useful? What time-based baseline, error or alert metric would be credible? Who can verify unusual dates and operating changes?
7. **Next step.** Would a small, securely transferred sample and a follow-up review be feasible? If not, what output could still be evaluated without raw data?

## Sample-data request checklist

Request only after the owner identifies an approved channel and written use terms. The analysis cutoff is **2020-01-01**: request eligible records dated 2020 onward and use no earlier readings for model inputs or targets. A minimum useful sample should be an export of real, non-imputed readings with meter or household pseudonym, timestamp, measured value, unit, interval length, timezone, and the measurement's meaning (cumulative register, interval kWh, hourly kWh, or kW). Ask for a meter inventory, data dictionary, export/version date, expected cadence, coverage dates, known resets and meter replacements, and missing-value codes. For institutional data, also request building/meter boundary, operating calendar, closures and major equipment or occupancy changes. For tariff work, request the rate schedule with effective dates from 2020 onward, time zone, account eligibility and interval mapping. Request event labels only if a related alert claim requires them. Ask whether data can be stored in the thesis workspace, whether only derived statistics may be published, retention/deletion requirements, and who signs off. Do not collect personal identifiers or operationally restricted data before approval.

**Gate:** The public dataset study can proceed separately. Local predictive accuracy requires permitted local observations and a held-out future-period test. An interview alone supports usefulness feedback, not model accuracy.

## Draft A — FEU Manila Facilities and Technical Services

**Subject:** Thesis review request: building electricity high-hour alerts

Dear Facilities and Technical Services team,

We are a Data Science thesis group studying whether next-hour building electricity forecasts and high-hour alerts would help facilities staff plan or investigate unusual energy use. Your team’s published electrical engineering and energy-conservation work makes your operational perspective especially relevant.

Would a facilities or electrical engineer be available for a 20–30 minute interview to discuss the decisions such an alert could support and what would make it useful? We would also like to learn who owns the relevant building meter records and whether a de-identified hourly kWh sample could be considered under your approval process. We would first agree on scope, transfer method, confidentiality and publication limits. We are not asking for access before that review.

Our initial modeling uses a public overseas building dataset. We would describe local performance only after separately testing authorized Philippine data. We can share a one-page concept and sample schema before a meeting.

Sincerely,  
[Group name / adviser / contact]

## Draft B — APMC or SM Offices building operations

**Subject:** Request for operational feedback on building electricity forecasts

Dear [property or engineering contact],

We are evaluating a thesis concept that forecasts a building meter’s next-hour electricity consumption in kWh and flags hours likely to be unusually high. We are seeking an engineering reviewer to tell us whether this output would support a real decision at one property.

Could we arrange a brief interview? If the concept fits, we would ask who can authorize a historical, de-identified meter export and what intervals, units, meter boundaries and operating context are available. Any data request would follow your required confidentiality and transfer process. A public description of metering or dashboards is our reason to ask, and we do not assume an export is available.

Sincerely,  
[Group name / adviser / contact]

## Draft C — consenting residential customer or Meralco program contact

**Subject:** Thesis feedback request: household electricity-use alerts and tariff interpretation

Dear [customer or program contact],

We are studying two household-facing ideas: an alert for unusually high electricity use on the next day, and a forecast of interval energy charges under a time-of-use price schedule. Our public-data exercise uses overseas readings and tariffs, so we would value your feedback on whether either output would be useful in a Philippine household and how you would interpret it.

Could we ask for a short interview? We would also like to learn whether a consenting customer can obtain daily or interval kWh history and the applicable historical prices, and who must authorize their research use. We will not treat a calculated energy charge as a complete bill, or use any account records without agreed permission and handling terms.

Sincerely,  
[Group name / adviser / contact]

## Review record to complete after any approved contact

| Candidate | End user interviewed | Data owner identified | Data available and interval | Permission / terms | Usefulness decision | Follow-up |
| --- | --- | --- | --- | --- | --- | --- |
| FEU Manila | Unverified | Unverified | Unverified | Unverified | Unverified | Pending approval to contact |
| FEU Tech | Unverified | Unverified | Unverified | Unverified | Unverified | Alternate |
| APMC | Unverified | Unverified | Unverified | Unverified | Unverified | Pending approval to contact |
| SM Offices | Unverified | Unverified | Unverified | Unverified | Unverified | Alternate |
| Residential / Meralco | Unverified | Unverified | Unverified | Unverified | Unverified | Pending approval to contact |
