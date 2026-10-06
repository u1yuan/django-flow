# Title cards: psychology

Field: psychology.
Evidence: `gap-candidates-psychology.md` in this folder. That file is the only evidence for the claims below.
Status: draft panel cards. Not a fitted model, not a completed study, and not a novelty claim.
Scope: three candidate gaps, in source order. Population patterns only. No card identifies, diagnoses, or labels an individual child or adolescent.

Opened, abstract-only, blocked, and unconfirmed labels are the gap file’s labels. This writing pass did not re-open pages, resolve DOIs again, or download microdata.

## Card 1. Leave-one-economy transport of school belonging

### Named user and decision

The named user is an education office. The decision is whether belonging patterns from a model fitted in other school systems are informative for Philippine aggregate results. The affected population is adolescent students who answer school-belonging items in a public international student file. Filipino students are the intended held-out group only if that file’s documentation shows Philippine rows. This run confirmed Philippine rows for TIMSS 2019 Grade 4, not for PISA 2022. The gap card links the decision to SDG 4, Quality education.

### Demonstrable artifact

The artifact is an economy-level error report for a belonging model trained on other economies’ student responses and scored on a held-out economy. The named technique is LightGBM, from the draft title. The gap card places the study in predictive analytics. Liao’s opened HTML names the BELONG index and items ST034Q01TA–ST034Q06TA. The observation unit for a later TIMSS study is the student response in the Grade 4 public-use file. The TIMSS 2019 page does not name a school-belonging item, so item availability is still unchecked. No microdata were downloaded, and the gap file records no fitted transport error.

### One-sentence innovation

The proposed transport check trains a belonging model on student responses from other economies and scores only economy-level error on a held-out economy, which Liao, Qin, and Li (2026) leave open: the section 4.5 limitation recorded in the gap card is that stable predictor ranks are not a transferable intervention benefit and are not a causal effect, and the gap statement states that a holdout error does not establish a cause.

### Measurable impact against a baseline

The impact to test later is economy-level error when the training economies exclude the scored economy, set against Liao, Qin, and Li’s within-economy LightGBM design. The gap card states no baseline error number and no success threshold. Transport error is an association between a fitted function and held-out responses. The claim boundary states that the output is economy-level error, not an individual belonging label and not a diagnosis. These impact lines are targets, not results.

### Transfer or scale

Liao’s opened abstract says outcome-valid belonging models used 561,339 students in 78 economies and per-economy LightGBM with TreeSHAP. Allohibi’s opened abstract says the sample is 47,652 students in six Arab systems, and the opened future-work locator names belonging as later work. Ghazanchyan and Kumar’s opened abstract says the analysis split PISA 2022 into six continental case studies and included wellbeing and sense of belonging, and their limitations paragraph says the observational dataset prevents causal interpretation. Pan and Cutumisu were opened as an abstract only; the gap statement says that abstract reports random forest and k-nearest neighbours on the UK and Japan PISA 2018 files for life satisfaction, with belonging-adjacent school climate among the predictors discussed. Lim, Yoo, Rho, and Ryu were opened as an abstract only; the abstract quote says group Mnet on PISA 2015 searched hundreds of predictors of school belonging in one model. PISA 2022 is the file the belonging studies analyze. The OECD dataset page returned HTTP 403, so the download path and Philippine rows were not confirmed from documentation, and the opened Liao HTML does not name the Philippines. The opened TIMSS 2019 page states a public-use database for 64 countries and 8 benchmarking participants at fourth and eighth grades, lists the Philippines on the Grade 4 country-download list, and does not list the Philippines on the Grade 8 list in that HTML. *Frontiers in Psychology* published Liao et al. (2026) and Allohibi (2026), and the *British Journal of Educational Psychology* published Pan and Cutumisu (2023). Indexing was not confirmed, and the gap card states that these venues do not pass the Scopus or IEEE rule.

### Title

Testing leave-one-economy transport of school belonging for Philippine students Using LightGBM

Word count: 11.

This is the gap card’s draft title, retained because that wording already has the required form. Philippine rows in PISA 2022 were not confirmed from documentation.

### Pitch

Within-economy belonging models leave open whether a fit from other school systems informs a held-out economy. LightGBM trained on other economies' student responses would report only economy-level transport error.

Pitch word count: 29. This count is a count of the pitch, not a study result.

### Ethics line

A country-level belonging summary can stigmatize a national school system, and student-survey rows are privacy-sensitive even in a public-use file. The design limits that harm by reporting economy-level error only and by not using the model to label an individual student.

### Claim map

| ID | Factual sentence | Gap-card section |
| --- | --- | --- |
| C1-01 | The named user is an education office. | Card 1, Social implication |
| C1-02 | The decision is whether belonging patterns from a model fitted in other school systems are informative for Philippine aggregate results. | Card 1, Social implication |
| C1-03 | The affected population is adolescent students who answer school-belonging items in a public international student file. | Card 1, Social implication |
| C1-04 | Filipino students are the intended held-out group only if that file’s documentation shows Philippine rows. | Card 1, Social implication |
| C1-05 | This run confirmed Philippine rows for TIMSS 2019 Grade 4, not for PISA 2022. | Card 1, Social implication |
| C1-06 | The gap card links the decision to SDG 4, Quality education. | Card 1, Social implication |
| C1-07 | The artifact is an economy-level error report for a belonging model trained on other economies’ student responses and scored on a held-out economy. | Card 1, Gap statement |
| C1-08 | The named technique is LightGBM, from the draft title. | Card 1, Draft title |
| C1-09 | The gap card places the study in predictive analytics. | Card 1, Subdomain |
| C1-10 | Liao’s opened HTML names the BELONG index and items ST034Q01TA–ST034Q06TA. | Card 1, Dataset lead |
| C1-11 | The observation unit for a later TIMSS study is the student response in the Grade 4 public-use file. | Card 1, Dataset lead |
| C1-12 | The TIMSS 2019 page does not name a school-belonging item, so item availability is still unchecked. | Card 1, Dataset lead |
| C1-13 | No microdata were downloaded, and the gap file records no fitted transport error. | Card 1, Dataset lead; file header (“No model was fit”) |
| C1-14 | The proposed transport check trains a belonging model on student responses from other economies and scores only economy-level error on a held-out economy, which Liao, Qin, and Li (2026) leave open: the section 4.5 limitation recorded in the gap card is that stable predictor ranks are not a transferable intervention benefit and are not a causal effect, and the gap statement states that a holdout error does not establish a cause. | Card 1, Gap statement; Nearest studies, item 1 (full HTML; section 4.5) |
| C1-15 | The impact to test later is economy-level error when the training economies exclude the scored economy, set against Liao, Qin, and Li’s within-economy LightGBM design. | Card 1, Gap statement |
| C1-16 | The gap card states no baseline error number and no success threshold. | Card 1, Gap statement and Social implication (no numeric cutoff is written) |
| C1-17 | Transport error is an association between a fitted function and held-out responses. | Card 1, Claim boundary |
| C1-18 | The claim boundary states that the output is economy-level error, not an individual belonging label and not a diagnosis. | Card 1, Claim boundary |
| C1-19 | These impact lines are targets, not results. | File header (“No model was fit”); title-card brief |
| C1-20 | Liao’s opened abstract says outcome-valid belonging models used 561,339 students in 78 economies and per-economy LightGBM with TreeSHAP. | Card 1, Nearest studies, item 1 |
| C1-21 | Allohibi’s opened abstract says the sample is 47,652 students in six Arab systems, and the opened future-work locator names belonging as later work. | Card 1, Nearest studies, item 2 |
| C1-22 | Ghazanchyan and Kumar’s opened abstract says the analysis split PISA 2022 into six continental case studies and included wellbeing and sense of belonging, and their limitations paragraph says the observational dataset prevents causal interpretation. | Card 1, Nearest studies, item 3 |
| C1-23 | Pan and Cutumisu were opened as an abstract only; the gap statement says that abstract reports random forest and k-nearest neighbours on the UK and Japan PISA 2018 files for life satisfaction, with belonging-adjacent school climate among the predictors discussed. | Card 1, Gap statement; Nearest studies, item 4 (abstract only) |
| C1-24 | Lim, Yoo, Rho, and Ryu were opened as an abstract only; the abstract quote says group Mnet on PISA 2015 searched hundreds of predictors of school belonging in one model. | Card 1, Nearest studies, item 5 (abstract only) |
| C1-25 | PISA 2022 is the file the belonging studies analyze. | Card 1, Dataset lead |
| C1-26 | The OECD dataset page returned HTTP 403, so the download path and Philippine rows were not confirmed from documentation, and the opened Liao HTML does not name the Philippines. | Card 1, Dataset lead |
| C1-27 | The opened TIMSS 2019 page states a public-use database for 64 countries and 8 benchmarking participants at fourth and eighth grades, lists the Philippines on the Grade 4 country-download list, and does not list the Philippines on the Grade 8 list in that HTML. | Card 1, Dataset lead |
| C1-28 | *Frontiers in Psychology* published Liao et al. (2026) and Allohibi (2026), and the *British Journal of Educational Psychology* published Pan and Cutumisu (2023). | Card 1, Candidate venues |
| C1-29 | Indexing was not confirmed, and the gap card states that these venues do not pass the Scopus or IEEE rule. | Card 1, Candidate venues |
| C1-30 | The title is “Testing leave-one-economy transport of school belonging for Philippine students Using LightGBM”. | Card 1, Draft title |
| C1-31 | Word count: 11. | Card 1, Draft title |
| C1-32 | Philippine rows in PISA 2022 were not confirmed from documentation. | Card 1, Dataset lead |
| C1-33 | Within-economy belonging models leave open whether a fit from other school systems informs a held-out economy. | Card 1, Gap statement |
| C1-34 | LightGBM trained on other economies' student responses would report only economy-level transport error. | Card 1, Gap statement; Draft title (LightGBM) |
| C1-35 | A country-level belonging summary can stigmatize a national school system, and student-survey rows are privacy-sensitive even in a public-use file. | Card 1, Social implication |
| C1-36 | The design limits that harm by reporting economy-level error only and by not using the model to label an individual student. | Card 1, Social implication; Claim boundary |

## Card 2. Country-holdout classification of bullying victimization

### Named user and decision

The named user is a ministry. The decision is whether a pooled bullying classifier’s error stays small enough, at country level, to inform a ministry’s reading of another country’s survey pattern. The gap card states no numeric cutoff for “small enough.” The affected population is adolescents in school surveys, with Philippine Grade 4 students in the TIMSS 2019 public-use list as a possible held-out group. The gap card links the decision to SDG 3, Good health and well-being.

### Demonstrable artifact

The artifact is a country-level classification-error report for one bullying-item classifier fit on some countries’ student responses and scored on held-out countries. The named technique is LightGBM, from the draft title. The gap card places the study in predictive analytics. Philippine Grade 4 in TIMSS 2019 is in that report only if the context questionnaire contains the bullying items. The opened TIMSS 2019 database page does not name bullying items. Mokgwathi’s description of verbal, relational, physical, and cyber items in the 2023 South African file does not establish those items in the 2019 public-use file. No microdata were downloaded, and the gap file records no fitted classification error.

### One-sentence innovation

The proposed country holdout fits one bullying-item classifier on some countries’ student responses and reports classification error for held-out countries, which Low and colleagues (2025) leave open when their limitations section calls for research across many states after a Utah-only LightGBM, and the gap statement calls this a predictive comparison across places that does not turn Mokgwathi’s (2026) within-South-Africa associations into a cause.

### Measurable impact against a baseline

The impact to test later is classification error on held-out countries, set against within-place fits already described in the gap card: Low and colleagues’ Utah LightGBM, and Gao and colleagues’ five-fold cross-validation inside one sample. Gao and colleagues were opened as an abstract only. The gap card states no error value and no threshold. A country difference in classification error is not evidence that poverty, school policy, or bullying caused the error. Results stay at country or country-year aggregates. These impact lines are targets, not results.

### Transfer or scale

Low and colleagues’ opened full HTML is the Utah SHARP LightGBM; the gap statement records 345,506 Utah student responses. Gao and colleagues’ abstract, the only text opened, reports machine-learning models, including random forest, for verbal, physical, relational, and cyber victimization in one Chinese sample of 1,981 students aged 11–18, with five-fold cross-validation inside that sample. Mokgwathi’s opened full HTML uses hierarchical linear models on the South African TIMSS 2023 Grade 9 file and treats bullying items as predictors of mathematics achievement inside that system. The opened TIMSS 2019 page lists Philippine Grade 4 rows, as used in Card 1, and also links student, home, teacher, school, and national context files. The opened WHO GSHS overview says GSHS uses a self-administered school questionnaire on behavioural risk and protective factors among young people aged 13 to 17 years and points to a data-and-reporting section. That page does not list countries, so Philippine GSHS rows are not known from it, and the data-and-reporting section was not opened. *BMC Public Health* published Low et al. (2025) and Gao et al. (2026), and *Frontiers in Education* published Mokgwathi (2026). The gap card records the same failed or empty Scopus, IEEE Xplore, and SCImago checks as in Card 1. Indexing was not confirmed, and these venues do not pass.

### Title

Comparing country-holdout bullying classification for adolescents Using LightGBM

Word count: 8.

This is the gap card’s draft title, retained because that wording already has the required form.

### Pitch

Utah LightGBM results leave a country holdout open. LightGBM fit on other countries' student responses would report country-level error, with Philippine Grade 4 only if TIMSS 2019 items exist.

Pitch word count: 29. This count is a count of the pitch, not a study result.

### Ethics line

Country rankings can stigmatize a school system, and public-use student files can still be privacy-sensitive in combination with school identifiers. The design limits that harm by keeping results at country or country-year aggregates and by not assigning a bullying label to a named student.

### Claim map

| ID | Factual sentence | Gap-card section |
| --- | --- | --- |
| C2-01 | The named user is a ministry. | Card 2, Social implication |
| C2-02 | The decision is whether a pooled bullying classifier’s error stays small enough, at country level, to inform a ministry’s reading of another country’s survey pattern. | Card 2, Social implication |
| C2-03 | The gap card states no numeric cutoff for “small enough.” | Card 2, Social implication (the phrase is present; no number is written) |
| C2-04 | The affected population is adolescents in school surveys, with Philippine Grade 4 students in the TIMSS 2019 public-use list as a possible held-out group. | Card 2, Social implication |
| C2-05 | The gap card links the decision to SDG 3, Good health and well-being. | Card 2, Social implication |
| C2-06 | The artifact is a country-level classification-error report for one bullying-item classifier fit on some countries’ student responses and scored on held-out countries. | Card 2, Gap statement |
| C2-07 | The named technique is LightGBM, from the draft title. | Card 2, Draft title |
| C2-08 | The gap card places the study in predictive analytics. | Card 2, Subdomain |
| C2-09 | Philippine Grade 4 in TIMSS 2019 is in that report only if the context questionnaire contains the bullying items. | Card 2, Gap statement |
| C2-10 | The opened TIMSS 2019 database page does not name bullying items. | Card 2, Dataset lead |
| C2-11 | Mokgwathi’s description of verbal, relational, physical, and cyber items in the 2023 South African file does not establish those items in the 2019 public-use file. | Card 2, Dataset lead |
| C2-12 | No microdata were downloaded, and the gap file records no fitted classification error. | Card 2, Dataset lead; file header (“No model was fit”) |
| C2-13 | The proposed country holdout fits one bullying-item classifier on some countries’ student responses and reports classification error for held-out countries, which Low and colleagues (2025) leave open when their limitations section calls for research across many states after a Utah-only LightGBM, and the gap statement calls this a predictive comparison across places that does not turn Mokgwathi’s (2026) within-South-Africa associations into a cause. | Card 2, Gap statement; Nearest studies, items 1 and 3 |
| C2-14 | The impact to test later is classification error on held-out countries, set against within-place fits already described in the gap card: Low and colleagues’ Utah LightGBM, and Gao and colleagues’ five-fold cross-validation inside one sample. | Card 2, Gap statement; Nearest studies, items 1 and 2 |
| C2-15 | Gao and colleagues were opened as an abstract only. | Card 2, Nearest studies, item 2 |
| C2-16 | The gap card states no error value and no threshold. | Card 2, Gap statement and Social implication (no numeric cutoff is written) |
| C2-17 | A country difference in classification error is not evidence that poverty, school policy, or bullying caused the error. | Card 2, Claim boundary |
| C2-18 | Results stay at country or country-year aggregates. | Card 2, Claim boundary |
| C2-19 | These impact lines are targets, not results. | File header (“No model was fit”); title-card brief |
| C2-20 | Low and colleagues’ opened full HTML is the Utah SHARP LightGBM; the gap statement records 345,506 Utah student responses. | Card 2, Gap statement; Nearest studies, item 1 (full HTML) |
| C2-21 | Gao and colleagues’ abstract, the only text opened, reports machine-learning models, including random forest, for verbal, physical, relational, and cyber victimization in one Chinese sample of 1,981 students aged 11–18, with five-fold cross-validation inside that sample. | Card 2, Gap statement; Nearest studies, item 2 (abstract only) |
| C2-22 | Mokgwathi’s opened full HTML uses hierarchical linear models on the South African TIMSS 2023 Grade 9 file and treats bullying items as predictors of mathematics achievement inside that system. | Card 2, Gap statement; Nearest studies, item 3 (full HTML) |
| C2-23 | The opened TIMSS 2019 page lists Philippine Grade 4 rows and also links student, home, teacher, school, and national context files. | Card 2, Dataset lead; Card 1, Dataset lead |
| C2-24 | The opened WHO GSHS overview says GSHS uses a self-administered school questionnaire on behavioural risk and protective factors among young people aged 13 to 17 years and points to a data-and-reporting section. | Card 2, Dataset lead |
| C2-25 | That WHO page does not list countries, so Philippine GSHS rows are not known from it, and the data-and-reporting section was not opened. | Card 2, Dataset lead |
| C2-26 | *BMC Public Health* published Low et al. (2025) and Gao et al. (2026), and *Frontiers in Education* published Mokgwathi (2026). | Card 2, Candidate venues |
| C2-27 | The gap card records the same failed or empty Scopus, IEEE Xplore, and SCImago checks as in Card 1. Indexing was not confirmed, and these venues do not pass. | Card 2, Candidate venues |
| C2-28 | The title is “Comparing country-holdout bullying classification for adolescents Using LightGBM”. | Card 2, Draft title |
| C2-29 | Word count: 8. | Card 2, Draft title |
| C2-30 | Utah LightGBM results leave a country holdout open. | Card 2, Gap statement; Nearest studies, item 1 |
| C2-31 | LightGBM fit on other countries' student responses would report country-level error, with Philippine Grade 4 only if TIMSS 2019 items exist. | Card 2, Gap statement; Draft title; Dataset lead |
| C2-32 | Country rankings can stigmatize a school system, and public-use student files can still be privacy-sensitive in combination with school identifiers. | Card 2, Social implication |
| C2-33 | The design limits that harm by keeping results at country or country-year aggregates and by not assigning a bullying label to a named student. | Card 2, Social implication; Claim boundary |

## Card 3. Income-group calibration of a bullying classifier

### Named user and decision

The named user is a ministry. The decision is whether a ministry should trust a single pooled bullying classifier equally for lower-income and higher-income participating countries. The affected population is adolescents in pooled school surveys, including the GSHS age band of 13 to 17 years documented on the opened WHO page, and students in public TIMSS files. The gap card links the decision to SDG 3, Good health and well-being.

### Demonstrable artifact

The artifact is a group-metric report for one pre-specified student-level bullying classifier: calibration and false-negative rate compared across World Bank income groups, with income group assigned at country level. The named technique is logistic regression, from the draft title. The gap card places the study in data governance and ethics. The classifier’s observation unit would be the student response, and the reported metrics would be aggregated to country income group. The report contains no list of which students are bullied. No microdata were downloaded, and the income-group merge was not done.

### One-sentence innovation

The proposed comparison, which the gap statement says none of the opened texts report, uses one pre-specified student-level bullying classifier and compares calibration and false-negative rate across country-level World Bank income groups; Allohibi (2026) supplies the written limit in section 5.2, where cross-system claims for mathematics anxiety stay at within-system predictor order because measurement invariance was not established, and the Chen and colleagues (2024) and Man, Liu, and Xue (2022) texts were opened as abstracts only.

### Measurable impact against a baseline

The impact to test later is whether calibration and the false-negative rate of that one pre-specified classifier differ across World Bank income groups, compared with the same classifier’s later pooled metrics with no income-group split. The gap card states no calibration value, no false-negative rate, and no income-group table. Chen and colleagues’ country-level poverty associations are not this classifier comparison. A difference in calibration across income groups is not evidence that national income caused bullying or caused the model error. The study reports group rates only. These impact lines are targets, not results.

### Transfer or scale

Chen and colleagues were opened as an abstract only; that abstract analyzes six social poverty indicators against country-level bullying prevalence in 16 GSHS countries. Man, Liu, and Xue were opened as an abstract only; that abstract draws on 167,286 adolescents aged 12–17 in 65 GSHS countries from 2003 to 2015 and describes parental support as a protective correlate of mental health among bullied adolescents. Chen’s abstract unit is the country prevalence. Allohibi’s opened HTML, used here for the cross-system magnitude limit, reports a stable predictor ranking for mathematics anxiety across six Arab PISA 2022 systems that span a wide income range. The primary documentation lead is the WHO GSHS overview named in Card 2. Philippine GSHS rows were not stated on that page. TIMSS 2019 Philippine Grade 4 rows, as recorded in Card 1, are a supporting lead. Income group would be a country attribute merged later from a public income classification, and that merge was not done. The opened World Values Survey Wave 7 navigation page is a download menu for Wave 7 (2017–2022) and does not document the respondent unit or Philippine rows, so it is not a dataset lead for this card. *BMC Public Health* published Chen et al. (2024), the *International Journal of Environmental Research and Public Health* published Man et al. (2022), and *Frontiers in Psychology* published Allohibi (2026). Index pages were not opened. Indexing was not confirmed, and these venues do not pass.

### Title

Auditing income-group calibration of bullying classification for adolescents Using logistic regression

Word count: 11.

This is the gap card’s draft title, retained because that wording already has the required form.

### Pitch

Opened multi-country GSHS papers relate poverty indicators to bullying or mental-health prevalence, not to income-group classifier calibration. One logistic regression would report only group calibration and the false-negative rate.

Pitch word count: 29. This count is a count of the pitch, not a study result.

### Ethics line

Income-group error rates can stigmatize poorer countries if they are narrated as higher-risk populations, and survey microdata remain privacy-sensitive. The design limits that harm by reporting group rates only, by not screening or punishing an individual adolescent, and by not producing a legal or health label for a student or a label from imagery.

### Claim map

| ID | Factual sentence | Gap-card section |
| --- | --- | --- |
| C3-01 | The named user is a ministry. | Card 3, Social implication |
| C3-02 | The decision is whether a ministry should trust a single pooled bullying classifier equally for lower-income and higher-income participating countries. | Card 3, Social implication |
| C3-03 | The affected population is adolescents in pooled school surveys, including the GSHS age band of 13 to 17 years documented on the opened WHO page, and students in public TIMSS files. | Card 3, Social implication |
| C3-04 | The gap card links the decision to SDG 3, Good health and well-being. | Card 3, Social implication |
| C3-05 | The artifact is a group-metric report for one pre-specified student-level bullying classifier: calibration and false-negative rate compared across World Bank income groups, with income group assigned at country level. | Card 3, Gap statement |
| C3-06 | The named technique is logistic regression, from the draft title. | Card 3, Draft title |
| C3-07 | The gap card places the study in data governance and ethics. | Card 3, Subdomain |
| C3-08 | The classifier’s observation unit would be the student response, and the reported metrics would be aggregated to country income group. | Card 3, Dataset lead |
| C3-09 | The report contains no list of which students are bullied. | Card 3, Gap statement |
| C3-10 | No microdata were downloaded, and the income-group merge was not done. | Card 3, Dataset lead |
| C3-11 | The proposed comparison, which the gap statement says none of the opened texts report, uses one pre-specified student-level bullying classifier and compares calibration and false-negative rate across country-level World Bank income groups; Allohibi (2026) supplies the written limit in section 5.2, where cross-system claims for mathematics anxiety stay at within-system predictor order because measurement invariance was not established, and the Chen and colleagues (2024) and Man, Liu, and Xue (2022) texts were opened as abstracts only. | Card 3, Gap statement; Nearest studies, items 1–3 |
| C3-12 | The impact to test later is whether calibration and the false-negative rate of that one pre-specified classifier differ across World Bank income groups, compared with the same classifier’s later pooled metrics with no income-group split. | Card 3, Gap statement; Social implication |
| C3-13 | The gap card states no calibration value, no false-negative rate, and no income-group table. | Card 3, Gap statement and Dataset lead (no such figures are written) |
| C3-14 | Chen and colleagues’ country-level poverty associations are not this classifier comparison. | Card 3, Gap statement |
| C3-15 | A difference in calibration across income groups is not evidence that national income caused bullying or caused the model error. | Card 3, Claim boundary |
| C3-16 | The study reports group rates only. | Card 3, Gap statement; Claim boundary |
| C3-17 | These impact lines are targets, not results. | File header (“No model was fit”); title-card brief |
| C3-18 | Chen and colleagues were opened as an abstract only; that abstract analyzes six social poverty indicators against country-level bullying prevalence in 16 GSHS countries. | Card 3, Gap statement; Nearest studies, item 1 (abstract only) |
| C3-19 | Man, Liu, and Xue were opened as an abstract only; that abstract draws on 167,286 adolescents aged 12–17 in 65 GSHS countries from 2003 to 2015 and describes parental support as a protective correlate of mental health among bullied adolescents. | Card 3, Gap statement; Nearest studies, item 2 (abstract only) |
| C3-20 | Chen’s abstract unit is the country prevalence. | Card 3, Dataset lead |
| C3-21 | Allohibi’s opened HTML, used here for the cross-system magnitude limit, reports a stable predictor ranking for mathematics anxiety across six Arab PISA 2022 systems that span a wide income range. | Card 3, Gap statement; Nearest studies, item 3 |
| C3-22 | The primary documentation lead is the WHO GSHS overview named in Card 2. | Card 3, Dataset lead |
| C3-23 | Philippine GSHS rows were not stated on that page. | Card 3, Dataset lead |
| C3-24 | TIMSS 2019 Philippine Grade 4 rows are a supporting lead. | Card 3, Dataset lead; Card 1, Dataset lead |
| C3-25 | Income group would be a country attribute merged later from a public income classification, and that merge was not done. | Card 3, Dataset lead |
| C3-26 | The opened World Values Survey Wave 7 navigation page is a download menu for Wave 7 (2017–2022) and does not document the respondent unit or Philippine rows, so it is not a dataset lead for this card. | Card 3, Dataset lead |
| C3-27 | *BMC Public Health* published Chen et al. (2024), the *International Journal of Environmental Research and Public Health* published Man et al. (2022), and *Frontiers in Psychology* published Allohibi (2026). | Card 3, Candidate venues |
| C3-28 | Index pages were not opened. Indexing was not confirmed, and these venues do not pass. | Card 3, Candidate venues |
| C3-29 | The title is “Auditing income-group calibration of bullying classification for adolescents Using logistic regression”. | Card 3, Draft title |
| C3-30 | Word count: 11. | Card 3, Draft title |
| C3-31 | Opened multi-country GSHS papers relate poverty indicators to bullying or mental-health prevalence, not to income-group classifier calibration. | Card 3, Gap statement |
| C3-32 | One logistic regression would report only group calibration and the false-negative rate. | Card 3, Gap statement; Draft title (logistic regression) |
| C3-33 | Income-group error rates can stigmatize poorer countries if they are narrated as higher-risk populations, and survey microdata remain privacy-sensitive. | Card 3, Social implication |
| C3-34 | The design limits that harm by reporting group rates only, by not screening or punishing an individual adolescent, and by not producing a legal or health label for a student or a label from imagery. | Card 3, Social implication; Claim boundary |

## Skill note

Drafting used the local research-writing, scientific-writing, and citation-management skills. The gap file already records this citation from the arXiv API record `2609.00065v2` retrieved on 2026-10-06, and states that the record did not list a journal DOI: Kassis, T., Agarwal, V., He, Y., Patel, D., & Brueckner, A. M. (2026). *Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents.* arXiv:2609.00065. https://doi.org/10.48550/arXiv.2609.00065. This writing pass did not re-fetch that record.

## Unresolved inputs

- No model was fit. Economy-level error, held-out classification error, calibration, and false-negative rate are targets to test later. The gap file states no baseline number and no success threshold, including no cutoff for “small enough.”
- LightGBM on Cards 1 and 2, and logistic regression on Card 3, are the draft titles’ technique names. The gap statements say “a belonging model” and “one pre-specified classifier” without those algorithm names in the protocol sentences.
- Card 1 keeps the draft title’s phrase “Philippine students.” Philippine rows in PISA 2022 were not confirmed. The OECD dataset page returned HTTP 403, and Liao’s opened HTML does not name the Philippines.
- The TIMSS 2019 international-database page lists the Philippines for Grade 4 and not for Grade 8. It does not name a school-belonging item or a bullying item. Item availability is unchecked. Mokgwathi’s TIMSS 2023 South African items do not establish the 2019 items.
- Philippine GSHS rows are not known. The opened WHO overview does not list countries, and the data-and-reporting section was not opened.
- The World Bank income-group merge was not done. No public income-classification file was opened in the gap file.
- The World Values Survey Wave 7 page does not document the respondent unit or Philippine rows and is not a dataset lead for Card 3.
- Abstract only: Pan and Cutumisu (2023); Lim, Yoo, Rho, and Ryu (2022); Gao and colleagues (2026); Chen and colleagues (2024); Man, Liu, and Xue (2022).
- Indexing was not confirmed for every named venue. Scopus, IEEE Xplore, and SCImago checks failed, returned an empty body, or were not opened. Those venues do not pass.
- Dataset leads are not counted datasets. No survey microdata were downloaded.
- The gap file does not claim that any gap is novel. These cards do not add that claim.
- Unverified leads and blocked pages in the gap file were not used as nearest studies and were not opened in this writing pass.
- This writing pass did not re-resolve DOIs, rebuild BibTeX, or re-check bibliographic fields against Crossref or the publisher pages.
- The Scientific Agent Skills citation above is the gap file’s 2026-10-06 arXiv API note. It was not re-fetched here.
- No protocol, registration, ethics approval, analysis plan, authorship record, or venue instruction check exists for a later study. This file is not submission-ready.
