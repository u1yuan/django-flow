# Candidate gaps: adolescent belonging, bullying, and wellbeing classification

Generated: 2026-10-06
Review type: scoping
Search window: 2022-01-01 through 2026-10-06
Field: psychology
Indexes: OpenAlex CLI (`docs/activities/litReview/.agents/skills/literature-search-openalex`) and arXiv CLI (`docs/activities/litReview/.agents/skills/literature-search-arxiv`), both run with `uv run` from those skill directories.

These are candidate gaps. This file does not claim that a gap is novel. No model was fit. No survey microdata were downloaded. Population patterns only: no card proposes identifying, diagnosing, or labeling an individual child or adolescent.

Citation-management and the activity search skills contributed to the search and identifier checks. Kassis, T., Agarwal, V., He, Y., Patel, D., & Brueckner, A. M. (2026). *Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents.* arXiv:2609.00065. https://doi.org/10.48550/arXiv.2609.00065. Author list and year were taken from the arXiv API record `2609.00065v2` retrieved on 2026-10-06. That record did not list a journal DOI.

## Research question

Which 2022–2026 gaps in adolescent belonging, bullying, or wellbeing classification are specific enough for an undergraduate Data Science thesis, without diagnosing an individual minor, and which public multi-country dataset could later test each gap?

## Search log

| Database | Date searched | Query | Filters | Results | Export |
| --- | --- | --- | --- | ---: | --- |
| OpenAlex | 2026-10-06 | full text has "adolescent bullying machine learning review" | `from_publication_date:2022-01-01`, `to_publication_date:2026-10-06`, `type:review`, sort cited_by_count desc, per_page 8 | 210 | temp `oa-reviews.json` |
| OpenAlex | 2026-10-06 | title-abstract has "adolescent bullying machine learning" | same dates, per_page 8 | 99 | temp `oa-bully-ml.json` |
| OpenAlex | 2026-10-06 | title-abstract has "school belonging prediction adolescents" | same dates, per_page 8 | 5 | temp `oa-belong.json` |
| OpenAlex | 2026-10-06 | title-abstract has "well-being classification fairness adolescent" | same dates, per_page 8 | 9 | temp `oa-fair.json` |
| OpenAlex | 2026-10-06 | title-abstract has "PISA bullying machine learning" | same dates, per_page 8 | 10 | temp `oa-pisa.json` |
| OpenAlex | 2026-10-06 | title-abstract has "bullying prediction cross-country transfer" | same dates, per_page 8 | 0 | temp `oa-transfer.json` |
| OpenAlex | 2026-10-06 | title-abstract has "GSHS machine learning wellbeing" | same dates, per_page 8 | 0 | temp `oa-gshs.json` |
| OpenAlex | 2026-10-06 | title-abstract has "school belonging PISA machine learning" | same dates, per_page 6 | 11 | temp `oa-belong-pisa.json` |
| OpenAlex | 2026-10-06 | title-abstract has "bullying victimization external validation" | same dates, per_page 6 | 6 | temp `oa-external.json` |
| OpenAlex | 2026-10-06 | title-abstract has "World Values Survey well-being machine learning" | same dates, per_page 6 | 156 | temp `oa-wvs.json` |
| OpenAlex | 2026-10-06 | title-abstract has "Global School-based Student Health Survey bullying" | same dates, per_page 6 | 204 | temp `oa-gshs2.json` |
| OpenAlex | 2026-10-06 | title-abstract has "algorithmic fairness adolescent mental health" | same dates, per_page 6 | 15 | temp `oa-fair2.json` |
| OpenAlex | 2026-10-06 | title-abstract has "TIMSS bullying students" | same dates, per_page 6 | 44 | temp `oa-timss.json` |
| OpenAlex | 2026-10-06 | full text has the Ghazanchyan and Kumar title | same dates, per_page 3 | 1441 | temp `oa-arxiv-resolve.json`; first hit matched the preprint |
| OpenAlex | 2026-10-06 | title-abstract has "TIMSS bullying mathematics" | same dates, `is_oa:true`, per_page 5 | 43 | temp `oa-timss-oa.json` |
| arXiv | 2026-10-06 | `all:adolescent AND all:bullying AND all:classification` | sort submittedDate descending, max_results 5 | 0 entries (CLI printed no JSON) | none |
| arXiv | 2026-10-06 | `ti:bullying` | sort submittedDate descending, max_results 3 | 3 | stdout |
| arXiv | 2026-10-06 | `all:PISA AND all:belonging` | relevance, max_results 5 | 5, of which 1 was on student stress and PISA 2022 | temp `ax-pisa.log` |
| arXiv | 2026-10-06 | `all:GSHS AND all:bullying` | relevance, max_results 5 | 0 entries (CLI printed no JSON) | none |
| arXiv | 2026-10-06 | `ti:cyberbullying AND ti:detection AND cat:cs.LG` | relevance, max_results 5 | 5 | temp `ax-cyber.log` |
| arXiv | 2026-10-06 | `all:wellbeing AND all:fairness AND all:classification` with submittedDate 20220101 to 20261006 | relevance, max_results 8 | 1 | temp `ax-fair.json` |
| arXiv | 2026-10-06 | `id_list:2606.00791,2005.06625,2009.01046` | max_results 5 | 3 | temp `ax-ids.log` |

The arXiv script prints JSON only when at least one entry is parsed, and it prints a growing JSON object inside the entry loop. A run with no JSON was recorded as zero entries after a `ti:bullying` probe showed that the same CLI returns papers. The first OpenAlex CLI call in this session did not return. Later calls completed. No HTTP 429 response body was captured.

## Inclusion and exclusion

Included when the record was from 2022-01-01 through 2026-10-06, the abstract or full text concerned adolescent school belonging, bullying victimization, or a wellbeing or anxiety outcome in a school survey, and the design was a classifier, a machine-learning predictor comparison, or a multi-country survey analysis that shows what those models have not yet tested.

Excluded: reviews whose titles were about COVID-19 mental health, social media, organizational change, or clinical treatment rather than school belonging or bullying classification (the 210-review query); cyberbullying text, GIF, or chatbot classifiers, because a TIMSS, PISA, or GSHS student questionnaire cannot test them; the 2020 arXiv preprints *Generalisation of Cyberbullying Detection* (2009.01046) and *Cyberbullying Detection with Fairness Constraints* (2005.06625), which are outside the window; the fairness naive Bayes preprint 2202.11499, which is a US Census demonstration attached to a wellbeing symposium rather than an adolescent school survey; World Values Survey hits that were adult happiness, stress, or cybersecurity rather than adolescent school classification. Hydroponics and diesel were not searched. Duplicates were collapsed on DOI. Papers with an empty OpenAlex abstract and no opened full text were not used as nearest studies.

## Card 1. Leave-one-economy transport of school belonging

### Gap statement

Opened 2022–2026 studies already predict adolescent school belonging, or they put belonging beside stress and anxiety in PISA machine-learning models. Liao, Qin, and Li fit a separate LightGBM model in each PISA 2022 economy and compare predictor ranks for belonging. Lim, Yoo, Rho, and Ryu use group Mnet on PISA 2015 to select belonging predictors from a large variable pool. Pan and Cutumisu’s abstract reports random forest and k-nearest neighbours models developed on the UK PISA 2018 file and on the Japan file for life satisfaction, with belonging-adjacent school climate among the predictors they discuss. Allohibi fits gradient-boosted models of mathematics anxiety in six Arab PISA 2022 systems and names belonging as later work. Ghazanchyan and Kumar split PISA 2022 into six continental case studies and model achievement from stress, wellbeing, and belonging indicators. What those designs leave open is a pre-specified transport check: train a belonging model on student responses from other economies and score it on a held-out economy’s student responses, reporting only economy-level error. That check is a study of predictive transport. Liao’s own limitation is that stable predictor ranks are not a transferable intervention benefit and are not a causal effect. A holdout error does not restate that sentence, and it does not establish a cause.

### Nearest studies

1. Liao, Y., Qin, P., & Li, R. (2026). Cross-economy stability of predictor rankings for adolescent school belonging and mathematics anxiety: an explainable machine-learning analysis of PISA 2022. *Frontiers in Psychology*, 17, 1875261. https://doi.org/10.3389/fpsyg.2026.1875261. Opened: full HTML at https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1875261/full. The abstract in that HTML says outcome-valid belonging models used 561,339 students in 78 economies and per-economy LightGBM with TreeSHAP. Locator: section 4.5 Limitations. Quote: "Cross-economy stable predictive salience is therefore not evidence of a common psychological mechanism or a transferable intervention benefit."
2. Allohibi, O. (2026). What predicts adolescents’ mathematics anxiety in the Middle East and North Africa? An interpretable machine learning analysis of six Arab education systems in PISA 2022. *Frontiers in Psychology*, 17, 1929157. https://doi.org/10.3389/fpsyg.2026.1929157. Opened: full HTML at https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1929157/full. The abstract in that HTML says the sample is 47,652 students in six Arab systems. Locator: section 5.10 Limitations and future research. Quote: "Future work should extend the outcome-flip paradigm to other affective targets in MENA (belonging, fear of failure), exploit TIMSS 2023 for younger cohorts, and, most importantly, pair the observational hierarchy identified here with randomized efficacy-building and anti-bullying interventions to convert predictive leverage into causal knowledge."
3. Ghazanchyan, A., & Kumar, S. (2026). Global patterns in student stress and academic performance: A machine learning study using PISA 2022. Preprint, arXiv:2606.00791. https://doi.org/10.48550/arxiv.2606.00791. Opened: arXiv HTML saved from `download_paper.py` for 2606.00791. OpenAlex `get`/`filter` on 2026-10-06 returned this DOI for that title. The opened abstract says the analysis split PISA 2022 into six continental case studies and included wellbeing and sense of belonging among the indicators. Locator: limitations paragraph. Quote: "First, the observational nature of the PISA 2022 dataset prevents causal interpretation of the reported relationships."
4. Pan, Z., & Cutumisu, M. (2023). Using machine learning to predict UK and Japanese secondary students' life satisfaction in PISA 2018. *British Journal of Educational Psychology*, 94(2), 474–498. https://doi.org/10.1111/bjep.12657. Opened: abstract only, from the OpenAlex work record. Publisher HTML and pdfdirect returned HTTP 403. Locator: abstract. Quote: "Two supervised ML models, random forest (RF) and k-nearest neighbours (KNN), were developed based on the UK data and the Japan data in PISA 2018."
5. Lim, H. J., Yoo, J. E., Rho, M., & Ryu, J. J. (2022). Exploration of variables predicting sense of school belonging using the machine learning method—Group Mnet. *Psychological Reports*, 127(3), 1502–1526. https://doi.org/10.1177/00332941221133005. Opened: abstract only, from the OpenAlex work record. The SAGE page was not requested. Locator: abstract. Quote: "Using 2015 data from the Program for International Student Assessment (PISA), we sought to identify variables related to school belonging by searching for hundreds of predictors in one model using the group Mnet machine learning technique."

### Candidate venues

*Frontiers in Psychology* published Liao et al. (2026) and Allohibi (2026). *British Journal of Educational Psychology* published Pan and Cutumisu (2023). Scopus source search `https://www.scopus.com/sources.uri` returned HTTP 403. IEEE Xplore `https://ieeexplore.ieee.org/document/11538625` returned HTTP 202 with an empty body. SCImago ISSN pages for 1664-1078 and 1471-2458 returned HTTP 403. Indexing was not confirmed. These venues do not pass the Scopus or IEEE rule.

### Social implication

Affected population: adolescent students who answer school-belonging items in a public international student file. Filipino students are the intended held-out group only if that file’s documentation shows Philippine rows. This run confirmed Philippine rows for TIMSS 2019 Grade 4, not for PISA 2022. One Sustainable Development Goal: SDG 4, Quality education. Decision informed: whether an education office should treat belonging patterns from a model fitted in other school systems as informative for Philippine aggregate results. Harm note: student-survey rows are privacy-sensitive even when public-use; a country-level belonging summary can stigmatize a national school system; using the model to label an individual student would be a misuse this study must not support.

### Draft title

Testing leave-one-economy transport of school belonging for Philippine students Using LightGBM

Word count: 11.

### Subdomain

Predictive analytics.

### Dataset lead

This is a lead, not a counted dataset. No microdata were downloaded.

Opened page: TIMSS 2019 International Database, https://timss2019.org/international-database/, retrieved 2026-10-06. The page states that the public-use database includes student achievement data and student, home, teacher, school, and national context data for 64 countries and 8 benchmarking participants, at fourth and eighth grades, with SPSS and SAS files linked from the page. Philippines is on the Grade 4 country-download list in that HTML. Philippines was not on the Grade 8 list in the same HTML. The page does not name a school-belonging item, so item availability is still unchecked. Observation unit for a later study: student response in the Grade 4 public-use file.

PISA 2022 is the file the belonging studies analyze. Liao’s opened HTML names the BELONG index and items ST034Q01TA–ST034Q06TA. The OECD dataset page https://www.oecd.org/en/data/datasets/pisa-2022-database.html returned HTTP 403, so the download path and Philippine rows were not confirmed from documentation. The opened Liao HTML does not name the Philippines.

### Claim boundary

Transport error is an association between a fitted function and held-out responses. It is not evidence that a school practice caused belonging. The output is economy-level error, not an individual belonging label and not a diagnosis.

## Card 2. Country-holdout classification of bullying victimization

### Gap statement

Low and colleagues fit LightGBM to 345,506 Utah student responses from the SHARP survey and interpret bullying victimization with SHAP. Their limitations section says the data are only from Utah and calls for research across many states. Gao and colleagues’ abstract reports machine-learning models, including random forest, for verbal, physical, relational, and cyber victimization in one Chinese adolescent sample of 1,981 students aged 11–18, with five-fold cross-validation inside that sample. Mokgwathi uses hierarchical linear models on the South African TIMSS 2023 Grade 9 file and treats bullying items as predictors of mathematics achievement inside that system. The opening those designs leave is a country holdout on a public multi-country student file: fit one bullying-item classifier on some countries’ student responses and report classification error for held-out countries, including the Philippine Grade 4 TIMSS 2019 file if the context questionnaire contains the items. That protocol is a predictive comparison across places. It is not a restatement of Low’s request for more US states, and it does not turn Mokgwathi’s within-South-Africa associations into a cause.

### Nearest studies

1. Low, E., Monsen, J., Schow, L., Roberts, R., Collins, L., Johnson, H., Hanson, C. L., & Snell, Q. O. (2025). Predicting bullying victimization among adolescents using the risk and protective factor framework: a large-scale machine learning approach. *BMC Public Health*, 25, 321. https://doi.org/10.1186/s12889-025-21521-0. Opened: full HTML at https://link.springer.com/article/10.1186/s12889-025-21521-0. The abstract on that record says LightGBM was fit to Utah SHARP responses. Locator: Limitations and future research, final paragraph. Quote: "To have a broader understanding of the risk and protective factor bullying victimization profiles among adolescents, future research should be conducted on data across many, if not all, states."
2. Gao, Y., chen, w., Wang, Y., Fei, S., & Sun, D. (2026). Toward precision prevention: machine learning-identified risk and protective factors for distinct bullying victimization types among Chinese adolescents. *BMC Public Health*, 26. https://doi.org/10.1186/s12889-026-27447-5. Author spelling "wei chen" is the OpenAlex display name. Opened: abstract only, from the OpenAlex work record. BMC and Springer HTML returned a client-challenge page, not the article. Locator: abstract. Quote: "Chinese adolescents (n = 1,981, aged 11-18 years) completed measures of bullying victimization, depression, anxiety, friendship quality, emotion regulation, social support, school climate, trait anger, and moral disengagement bullying behavior."
3. Mokgwathi, M. S. (2026). Bullying victimisation and mathematics achievement in South African schools: an educational psychology perspective using TIMSS 2023. *Frontiers in Education*, 11. https://doi.org/10.3389/feduc.2026.1825403. Opened: full HTML at https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1825403/full. The article date line on that page is 20 May 2026. Locator: section 9 Limitations. Quote: "The use of a large-scale international dataset and multilevel modelling procedures therefore provides useful information about how students’ experiences and school climate indicators correspond with patterns of mathematics achievement within the South African education system."

### Candidate venues

*BMC Public Health* published Low et al. (2025) and Gao et al. (2026). *Frontiers in Education* published Mokgwathi (2026). The same Scopus, IEEE Xplore, and SCImago checks as in Card 1 failed or returned an empty body. Indexing was not confirmed. These venues do not pass.

### Social implication

Affected population: adolescents in school surveys, with Philippine Grade 4 students in the TIMSS 2019 public-use list as a possible held-out group. One Sustainable Development Goal: SDG 3, Good health and well-being. Decision informed: whether a pooled bullying classifier’s error stays small enough, at country level, to inform a ministry’s reading of another country’s survey pattern. Harm note: public-use student files can still be privacy-sensitive in combination with school identifiers; country rankings can stigmatize a school system; deploying the classifier as a tool to flag an individual child would be a misuse.

### Draft title

Comparing country-holdout bullying classification for adolescents Using LightGBM

Word count: 8.

### Subdomain

Predictive analytics.

### Dataset lead

This is a lead, not a counted dataset. No microdata were downloaded.

Opened page: https://timss2019.org/international-database/. Documented contents and the Philippine Grade 4 listing are as in Card 1. Observation unit: student response, with school and teacher context files also present on the page. The opened database page does not name bullying items. Mokgwathi’s opened TIMSS 2023 article describes verbal, relational, physical, and cyber items in the 2023 South African file. That does not establish that the 2019 public-use file has the same items.

The WHO GSHS overview https://www.who.int/teams/noncommunicable-diseases/surveillance/systems-tools/global-school-based-student-health-survey was opened. It says GSHS uses a self-administered school questionnaire on behavioural risk and protective factors among young people aged 13 to 17 years, and it points to a data-and-reporting section for data sets. That page does not list countries, so Philippine rows are not known from it. The data-and-reporting section was not opened.

### Claim boundary

A country difference in classification error is not evidence that poverty, school policy, or bullying caused the error. Results stay at country or country-year aggregates. The study does not assign a bullying label to a named student.

## Card 3. Income-group calibration of a bullying classifier

### Gap statement

Multi-country GSHS papers in this window relate poverty indicators to bullying or mental-health prevalence. Chen and colleagues analyze six poverty indicators against country-level bullying prevalence in 16 GSHS countries. Man, Liu, and Xue use ordinary least squares on 167,286 adolescents aged 12–17 in 65 GSHS countries from 2003–2015 and describe parental support as a protective correlate of mental health among bullied adolescents. Allohibi’s opened PISA 2022 analysis reports a stable predictor ranking for mathematics anxiety across six Arab systems that span a wide income range, and it limits cross-system claims to predictor order rather than absolute magnitudes. None of these opened texts report a student-level classifier whose calibration or false-negative rate is compared across World Bank income groups. That comparison is a study: one pre-specified classifier, group metrics only, income group assigned at country level. It does not restate Chen’s country-level poverty correlations, and it does not identify which students are bullied.

### Nearest studies

1. Chen, L., Chen, Y., Ran, H., Che, Y., Fang, D., Li, Q., Shi, Y., & Liu, S. (2024). Social poverty indicators with school bullying victimization: evidence from the global school-based student health survey (GSHS). *BMC Public Health*, 24, 615. https://doi.org/10.1186/s12889-024-18119-3. Opened: abstract only, from the OpenAlex work record. BMC and Springer HTML returned a client-challenge page. Locator: abstract. Quote: "In this cross-sectional study, we analyzed the association between 6 commonly used social poverty indicators (Poverty Headcount Ratio, PHR; Poverty Gap, PG; Squared Poverty Gap, SPG; monthly household per capita income, PCI; Watts' Poverty Index, WPI; the Gini Index, Gini) and the prevalence of school bullying at country level by using the Global school-based Student Health Survey (GSHS) database."
2. Man, X., Liu, J., & Xue, Z. (2022). Effects of bullying forms on adolescent mental health and protective factors: A global cross-regional research based on 65 countries. *International Journal of Environmental Research and Public Health*, 19(4), 2374. https://doi.org/10.3390/ijerph19042374. Opened: abstract only, from the OpenAlex work record. MDPI HTML and PDF returned HTTP 403. Locator: abstract. Quote: "Data were drawn from adolescents aged 12-17 years in 65 countries from the Global School-based Student Health Survey between 2003 and 2015."
3. Allohibi (2026), full citation and opened HTML as in Card 1. Used here for the cross-system income and magnitude limit, not for the belonging future-work sentence. Locator: section 5.2 discussion of cross-system comparison, as rendered in the opened HTML. Quote: "Second, formal measurement invariance of the questionnaire indices across the six systems was not established (Section 3.2); the cross-system claims made here therefore concern the ordering of predictors within systems, which is unaffected by system-specific scale shifts, and not comparisons of construct means or absolute effect magnitudes across systems."

### Candidate venues

*BMC Public Health* published Chen et al. (2024). *International Journal of Environmental Research and Public Health* published Man et al. (2022). *Frontiers in Psychology* published Allohibi (2026). Index pages were not opened, as recorded under Card 1. Indexing was not confirmed. These venues do not pass.

### Social implication

Affected population: adolescents in pooled school surveys, including the GSHS age band of 13 to 17 years documented on the opened WHO page, and students in public TIMSS files. One Sustainable Development Goal: SDG 3, Good health and well-being. Decision informed: whether a ministry should trust a single pooled bullying classifier equally for lower-income and higher-income participating countries. Harm note: income-group error rates can stigmatize poorer countries if they are narrated as higher-risk populations; survey microdata remain privacy-sensitive; using group-calibration results to screen or punish an individual adolescent would be a misuse.

### Draft title

Auditing income-group calibration of bullying classification for adolescents Using logistic regression

Word count: 11.

### Subdomain

Data governance and ethics.

### Dataset lead

This is a lead, not a counted dataset. No microdata were downloaded.

Primary opened documentation: WHO GSHS overview, URL and age band as in Card 2. Observation unit in Chen’s abstract is the country prevalence. The later calibration study’s unit would be the student response, with metrics aggregated to country income group. Philippine GSHS rows were not stated on the opened WHO page.

Supporting opened file: TIMSS 2019 public-use database, Philippine Grade 4 rows as in Card 1. Income group would be a country attribute merged later from a public income classification. That merge was not done here.

World Values Survey Wave 7 navigation page https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp was opened. The extracted text is a download menu for Wave 7 (2017–2022). It does not document the respondent unit or Philippine rows, so it is not used as a dataset lead for this adolescent card.

### Claim boundary

A difference in calibration across income groups is not evidence that national income caused bullying or caused the model error. The study reports group rates only. It does not produce a legal or health label for a student, and it does not label a minor from imagery.

## Unverified leads

- Yan, W., Yuan, Y., Yang, M., Zhang, P., & Peng, K. (2023). Detecting the risk of bullying victimization among adolescents: A large-scale machine learning approach. *Computers in Human Behavior*. https://doi.org/10.1016/j.chb.2023.107817. OpenAlex resolved the DOI, year, venue, and authors. The abstract field was empty. The DOI URL returned an Elsevier redirect stub, and the article was not opened.
- Wen and colleagues (2024), https://doi.org/10.1016/j.jad.2024.11.057, and Ran and colleagues (2023), https://doi.org/10.1016/j.jad.2022.12.094. OpenAlex records had empty abstracts. Publisher pages were not opened.
- Haw and King (2023), https://doi.org/10.1007/s11218-023-09773-3, and Wang, King, and Leung (2022), https://doi.org/10.1007/s12187-022-09997-3. OpenAlex records had empty abstracts. Pages were not opened.
- Traditional bullying and cyberbullying as main drivers of low mathematics achievement in South African schools: Evidence from TIMSS 2019, https://doi.org/10.1080/20004508.2023.2173122. DOI page returned HTTP 403.
- School bullying as a moderator of gender differences in mathematics achievement: Evidence from TIMSS, https://doi.org/10.33225/pec/26.84.157. DOI page returned HTTP 403.
- School belonging, student bullying, and school disciplinary climate in TIMSS top-performance countries (2023). OpenAlex returned the title with no DOI. The paper was not opened.
- arXiv cyberbullying-detection papers returned by `ti:cyberbullying AND ti:detection AND cat:cs.LG`, including 2402.04088, 2409.12263, and 2512.07838. Screened out as text or image classification rather than school-survey rows.
- IEEE conference paper https://doi.org/10.1109/iraset68627.2026.11538625 appeared in the PISA bullying search. The Xplore page was empty. The paper was not read.
- Philippine PISA 2022 conference paper https://doi.org/10.1007/978-3-032-33997-3_34 appeared in search results. It concerns English-at-home and achievement, and it was not opened.

## Blocked pages

- https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-025-21521-0 and the matching `/counter/pdf/` URL: client-challenge HTML. The Springer HTML for this DOI was later opened and is the full text used for Low et al.
- https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-026-27447-5, https://link.springer.com/article/10.1186/s12889-026-27447-5, and the BMC pdf counter URL: client-challenge HTML.
- https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-024-18119-3, https://link.springer.com/article/10.1186/s12889-024-18119-3, and the BMC pdf counter URL: client-challenge HTML.
- https://www.mdpi.com/1660-4601/19/4/2374/htm and https://www.mdpi.com/1660-4601/19/4/2374/pdf: HTTP 403.
- https://bpspsychub.onlinelibrary.wiley.com/doi/full/10.1111/bjep.12657, https://doi.org/10.1111/bjep.12657, and https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/bjep.12657: HTTP 403.
- https://doi.org/10.1016/j.chb.2023.107817: redirect stub only.
- https://doi.org/10.1080/20004508.2023.2173122 and https://doi.org/10.33225/pec/26.84.157: HTTP 403.
- https://www.oecd.org/en/data/datasets/pisa-2022-database.html: HTTP 403.
- https://www.scopus.com/sources.uri: HTTP 403.
- https://ieeexplore.ieee.org/document/11538625: HTTP 202, empty body.
- https://www.scimagojr.com/journalsearch.php?q=1471-2458&tip=iss and https://www.scimagojr.com/journalsearch.php?q=1664-1078&tip=iss: HTTP 403.

## Paper URLs used

- https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1875261/full
- https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1929157/full
- https://arxiv.org/html/2606.00791
- https://doi.org/10.48550/arxiv.2606.00791
- https://link.springer.com/article/10.1186/s12889-025-21521-0
- https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1825403/full
- OpenAlex abstract records for https://doi.org/10.1111/bjep.12657, https://doi.org/10.1177/00332941221133005, https://doi.org/10.1186/s12889-026-27447-5, https://doi.org/10.1186/s12889-024-18119-3, and https://doi.org/10.3390/ijerph19042374
- https://timss2019.org/international-database/
- https://www.who.int/teams/noncommunicable-diseases/surveillance/systems-tools/global-school-based-student-health-survey
- https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp
