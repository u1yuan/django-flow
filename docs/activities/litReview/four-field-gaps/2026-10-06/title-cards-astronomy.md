# Astronomy title cards

**Status.** Draft cards for a judging panel. The only evidence is `gap-candidates-astronomy.md` in this folder. No new literature was opened in this writing pass. Impact lines are targets to test later. These cards do not claim that a gap is novel.

**Limits kept.** Scopus and IEEE indexing was not confirmed. Philippine rows were not confirmed. Bará (2024) is abstract-only. OMNIWeb is an unverified lead. A sky-brightness card does not assign a health or legal label from imagery. The geomagnetic card does not claim that a disturbance caused a grid fault or a positioning failure.

**Source note.** The gap file is a scoping pass for 2022-01-01 through 2026-10-06 on night-sky brightness estimation and equatorial geomagnetic disturbance detection. It states that these are candidate gaps and that it does not claim that any gap is novel. It states that Earth Engine and any bulk imagery or magnetometer archive were out of scope, and that no bulk imagery or magnetometer archive was saved. The four cards below follow that file in order. Author-year labels, DOIs, quotes, and access results are copied from that file and were not re-resolved here. Citation-management scripts were not run. This writing pass did not fit a model.

### Source claim map

| ID | Factual sentence | Gap-card section |
| --- | --- | --- |
| S0-1 | The gap file is a scoping pass for 2022-01-01 through 2026-10-06 on night-sky brightness estimation and equatorial geomagnetic disturbance detection. | File introduction |
| S0-2 | It states that these are candidate gaps and that it does not claim that any gap is novel. | File introduction |
| S0-3 | It states that Earth Engine and any bulk imagery or magnetometer archive were out of scope, and that no bulk imagery or magnetometer archive was saved. | Inclusion and exclusion; Unverified leads and blocked pages |
| S0-4 | The four cards below follow that file in order. | Cards 1–4 |
| S0-5 | Author-year labels, DOIs, quotes, and access results are copied from that file and were not re-resolved here. | Nearest studies; Pages used; writer limit for this pass |
| S0-6 | Citation-management scripts were not run. | Writer limit for this pass |
| S0-7 | This writing pass did not fit a model. | Writer limit for this pass; Brief |
| S0-8 | Scopus and IEEE indexing was not confirmed. | Inclusion and exclusion; Candidate venues on Cards 1–4 |
| S0-9 | Philippine rows were not confirmed. | Dataset lead on Cards 1–4 |
| S0-10 | Bará (2024) is abstract-only. | Card 2 nearest studies; Unverified leads and blocked pages |
| S0-11 | OMNIWeb is an unverified lead. | Card 3 dataset lead; Unverified leads and blocked pages |
| S0-12 | A sky-brightness card does not assign a health or legal label from imagery. | Inclusion and exclusion; Claim boundary on Cards 1, 2, and 4; Brief |
| S0-13 | The geomagnetic card does not claim that a disturbance caused a grid fault or a positioning failure. | Inclusion and exclusion; Card 3 claim boundary; Brief |

## Card 1. Sparse-site zenith brightness

### Named user and decision

The named user is a municipality. The gap file names the affected population as residents and volunteer observers in places with few fixed photometers and places SDG 11, Sustainable Cities and Communities, on that line. The decision is where that municipality schedules a follow-up sky-brightness measurement.

### Demonstrable artifact

The candidate artifact is a held-out prediction of zenith brightness at sites that have only sparse citizen reports, with Globe at Night observations and VIIRS radiance as covariates and with a reported error. The recorded subdomain is predictive analytics. The dataset lead is Globe at Night citizen observations. The opened page states that observations are available to download and gives 2025 as 13421 total observations, with a CSV link. The unit is one citizen night-sky observation. Coverage described on the page is an international campaign since 2006. Philippine rows were not listed on the opened page and were not counted. The retired count of 323 Philippine Globe at Night rows is not reused. A second lead, not downloaded, is Earth Observation Group VIIRS Nighttime Light: global monthly cloud-free average radiance grids and annual VIIRS nighttime lights as GeoTIFF pixels. The opened VIIRS page did not name the Philippines. An Accounts link is on that page. A download was not started, so a login requirement was not tested. No bulk imagery was downloaded.

### One-sentence innovation

The study would report the error of a held-out zenith-brightness prediction at sites that have only sparse Globe at Night reports, with VIIRS radiance as a covariate, a separate analysis from restating the VIIRS blue-light limit Barentine (2022) records in the opened VIIRS-DNB paragraph, where the instrument is effectively blind to the strong peak in white LED light emissions near 450 nm.

### Measurable impact against a baseline

The impact line is a target to test later: the reported error of that held-out zenith-brightness prediction. The gap file does not name a baseline predictor and does not contain a computed error. This writing pass did not fit a model. A predicted brightness is an association between reports, radiance, and the held-out observation. It is not a cause of a health outcome and not a legal status read from the image.

### Transfer or scale

Opened 2022–2026 studies named on this card estimate night-sky brightness with radiative-transfer maps and with dense sky-quality-meter networks. Linares and colleagues compare Illumina v2 maps of Catalonia with measurements at nineteen locations. Buhler and colleagues calibrate Otus 3 on 139 French sites. Shah and colleagues rank year-to-year brightness changes at 27 stations in the northern Netherlands and on the western German Wadden coast. The gap file states that the held-out citizen-site prediction is a separate analysis from restating the VIIRS blue-light limit or from adding more photometers. The opened Linares abstract attributes measurement differences mainly to location mismatch, natural sky brightness, and atmospheric content. The opened Buhler Figure 6 caption states that VIIRS-DNB illuminance maps are primarily useful to highlight areas where light sources are concentrated, and not for a lighting analysis on the typical spatial scale of buildings or streets. The opened Shah limitation states that trend drivers remain elusive without additional contextual data. Scale to Philippine sites is unresolved because Philippine rows were not listed on the opened Globe at Night page and were not counted, and the opened VIIRS page did not name the Philippines. Candidate venues are Monthly Notices of the Royal Astronomical Society and the Journal of Quantitative Spectroscopy and Radiative Transfer, from DOIs read on arXiv abstract pages. The Scopus Sources preview was opened, and the loaded text did not list Monthly Notices, the Journal of Quantitative Spectroscopy and Radiative Transfer, or Nature Astronomy. IEEE Xplore search for `night sky brightness` returned “Unusual Traffic Detected (Error 418)” and no results list. Indexing was not confirmed. These venues are not treated as passing. Publisher HTML for Nature Astronomy, Monthly Notices, and the Journal of Quantitative Spectroscopy and Radiative Transfer was not opened, so volume and page ranges were not read. Buhler and colleagues remained an arXiv preprint on the opened abstract page, which showed no journal DOI. Barentine’s Nature Astronomy venue is taken from the arXiv abstract-page comment and the Nature-family DOI. The Nature HTML was not opened.

### Title

Estimating zenith sky brightness for sparsely reported sites Using gradient boosting

Word count: 11.

The draft title already matches the form "[action] [outcome] for [context or user] Using [named technique]." The technique name gradient boosting is taken from that draft title. The gap statement names the held-out prediction and the reported error and does not name gradient boosting.

### Pitch

Opened studies estimate brightness with radiative-transfer maps and dense photometer networks. A study would predict held-out zenith brightness at sparsely reported sites from Globe at Night reports and VIIRS radiance.

Word count: 30.

### Ethics line

The main risk to residents and volunteer observers is that a public Globe at Night file can expose where a person observed at night, and that a brightness estimate published as a ranked failure can stigmatize a neighborhood. The design limits that risk by keeping the estimate an association between reports, radiance, and the held-out observation, and by withholding any health finding or legal lighting violation taken from imagery alone.

### Claim map

| ID | Factual sentence | Gap-card section |
| --- | --- | --- |
| C1-01 | The named user is a municipality. | Social implication |
| C1-02 | The gap file names the affected population as residents and volunteer observers in places with few fixed photometers and places SDG 11, Sustainable Cities and Communities, on that line. | Social implication |
| C1-03 | The decision is where that municipality schedules a follow-up sky-brightness measurement. | Social implication |
| C1-04 | The candidate artifact is a held-out prediction of zenith brightness at sites that have only sparse citizen reports, with Globe at Night observations and VIIRS radiance as covariates and with a reported error. | Gap statement |
| C1-05 | The recorded subdomain is predictive analytics. | Subdomain |
| C1-06 | The dataset lead is Globe at Night citizen observations. | Dataset lead |
| C1-07 | The opened page states that observations are available to download and gives 2025 as 13421 total observations, with a CSV link. | Dataset lead |
| C1-08 | The unit is one citizen night-sky observation. | Dataset lead |
| C1-09 | Coverage described on the page is an international campaign since 2006. | Dataset lead |
| C1-10 | Philippine rows were not listed on the opened page and were not counted. | Dataset lead |
| C1-11 | The retired count of 323 Philippine Globe at Night rows is not reused. | Dataset lead; Inclusion and exclusion |
| C1-12 | A second lead, not downloaded, is Earth Observation Group VIIRS Nighttime Light: global monthly cloud-free average radiance grids and annual VIIRS nighttime lights as GeoTIFF pixels. | Dataset lead |
| C1-13 | The opened VIIRS page did not name the Philippines. | Dataset lead |
| C1-14 | An Accounts link is on that page. | Dataset lead |
| C1-15 | A download was not started, so a login requirement was not tested. | Dataset lead |
| C1-16 | No bulk imagery was downloaded. | Dataset lead; Unverified leads and blocked pages |
| C1-17 | The study would report the error of a held-out zenith-brightness prediction at sites that have only sparse Globe at Night reports, with VIIRS radiance as a covariate, a separate analysis from restating the VIIRS blue-light limit Barentine (2022) records in the opened VIIRS-DNB paragraph, where the instrument is effectively blind to the strong peak in white LED light emissions near 450 nm. | Gap statement; Nearest studies, Barentine (2022) |
| C1-18 | The impact line is a target to test later: the reported error of that held-out zenith-brightness prediction. | Gap statement; Brief |
| C1-19 | The gap file does not name a baseline predictor and does not contain a computed error. | Gap statement; writer limit |
| C1-20 | This writing pass did not fit a model. | Writer limit; Brief |
| C1-21 | A predicted brightness is an association between reports, radiance, and the held-out observation. | Claim boundary |
| C1-22 | It is not a cause of a health outcome and not a legal status read from the image. | Claim boundary |
| C1-23 | Opened 2022–2026 studies named on this card estimate night-sky brightness with radiative-transfer maps and with dense sky-quality-meter networks. | Gap statement |
| C1-24 | Linares and colleagues compare Illumina v2 maps of Catalonia with measurements at nineteen locations. | Gap statement |
| C1-25 | Buhler and colleagues calibrate Otus 3 on 139 French sites. | Gap statement |
| C1-26 | Shah and colleagues rank year-to-year brightness changes at 27 stations in the northern Netherlands and on the western German Wadden coast. | Gap statement |
| C1-27 | The gap file states that the held-out citizen-site prediction is a separate analysis from restating the VIIRS blue-light limit or from adding more photometers. | Gap statement |
| C1-28 | The opened Linares abstract attributes measurement differences mainly to location mismatch, natural sky brightness, and atmospheric content. | Nearest studies, Linares and colleagues |
| C1-29 | The opened Buhler Figure 6 caption states that VIIRS-DNB illuminance maps are primarily useful to highlight areas where light sources are concentrated, and not for a lighting analysis on the typical spatial scale of buildings or streets. | Nearest studies, Buhler and colleagues |
| C1-30 | The opened Shah limitation states that trend drivers remain elusive without additional contextual data. | Nearest studies, Shah and colleagues |
| C1-31 | Scale to Philippine sites is unresolved because Philippine rows were not listed on the opened Globe at Night page and were not counted, and the opened VIIRS page did not name the Philippines. | Dataset lead |
| C1-32 | Candidate venues are Monthly Notices of the Royal Astronomical Society and the Journal of Quantitative Spectroscopy and Radiative Transfer, from DOIs read on arXiv abstract pages. | Candidate venues |
| C1-33 | The Scopus Sources preview was opened, and the loaded text did not list Monthly Notices, the Journal of Quantitative Spectroscopy and Radiative Transfer, or Nature Astronomy. | Inclusion and exclusion; Candidate venues |
| C1-34 | IEEE Xplore search for `night sky brightness` returned “Unusual Traffic Detected (Error 418)” and no results list. | Inclusion and exclusion; Unverified leads and blocked pages |
| C1-35 | Indexing was not confirmed. | Candidate venues |
| C1-36 | These venues are not treated as passing. | Candidate venues |
| C1-37 | Publisher HTML for Nature Astronomy, Monthly Notices, and the Journal of Quantitative Spectroscopy and Radiative Transfer was not opened, so volume and page ranges were not read. | Unverified leads and blocked pages |
| C1-38 | Buhler and colleagues remained an arXiv preprint on the opened abstract page, which showed no journal DOI. | Nearest studies, Buhler and colleagues |
| C1-39 | Barentine’s Nature Astronomy venue is taken from the arXiv abstract-page comment and the Nature-family DOI. | Nearest studies, Barentine (2022) |
| C1-40 | The Nature HTML was not opened. | Nearest studies, Barentine (2022) |
| C1-41 | The draft title already matches the form "[action] [outcome] for [context or user] Using [named technique]." | Draft title; Brief |
| C1-42 | The technique name gradient boosting is taken from that draft title. | Draft title |
| C1-43 | The gap statement names the held-out prediction and the reported error and does not name gradient boosting. | Gap statement; Draft title |
| C1-44 | Opened studies estimate brightness with radiative-transfer maps and dense photometer networks. | Gap statement |
| C1-45 | A study would predict held-out zenith brightness at sparsely reported sites from Globe at Night reports and VIIRS radiance. | Gap statement |
| C1-46 | The main risk to residents and volunteer observers is that a public Globe at Night file can expose where a person observed at night, and that a brightness estimate published as a ranked failure can stigmatize a neighborhood. | Social implication |
| C1-47 | The design limits that risk by keeping the estimate an association between reports, radiance, and the held-out observation, and by withholding any health finding or legal lighting violation taken from imagery alone. | Social implication; Claim boundary |

## Card 2. Atmospheric contribution to sparse brightness trends

### Named user and decision

The gap file names the affected population as communities whose outdoor-light trends might be discussed by local government and places SDG 11, Sustainable Cities and Communities, on that line. No office is named as the user. The decision is whether a reported brightening is large enough, after an atmospheric covariate, to justify a ground check of lighting.

### Demonstrable artifact

The candidate artifact is an estimate of a year-to-year brightness change in a sparse Globe at Night series after an atmospheric covariate is included, with the uncertainty that comes from thin annual samples. The gap file calls that task a hierarchical estimation. The recorded subdomain is statistical modeling. The dataset lead is Globe at Night observations, the same opened page and unit as Card 1. Philippine rows were not confirmed on that page. VIIRS monthly radiance grids are the satellite covariate lead. The opened VIIRS page states that some areas lack good monthly coverage because of cloud. No bulk imagery was downloaded. Copernicus and Earth Engine were not used.

### One-sentence innovation

The study would estimate whether a year-to-year brightness change remains in a sparse Globe at Night series after an atmospheric covariate, and would report the uncertainty that comes from thin annual samples, a hierarchical estimation task different from repeating the control of annual-mean atmospheric variability stated in the abstract-only Bará (2024) record.

### Measurable impact against a baseline

The impact line is a target to test later: whether a year-to-year change remains after the atmospheric covariate, together with the uncertainty that comes from thin annual samples. The gap file does not name a numeric baseline and does not contain a computed uncertainty. This writing pass did not fit a model. An adjusted trend is an association between the citizen series, the covariate, and time. It does not establish that lighting practice caused the change, and it does not assign a health or legal label.

### Transfer or scale

Puschnig and colleagues separate atmospheric covariates from anthropogenic zenith-brightness trends with a multivariate penalized linear regression at 26 sky-quality-meter sites. Their opened VIIRS comparison is limited to September through March, because only then does the satellite pass during astronomical night at those sites. Bará (2024) was opened as an abstract only. The gap statement says that abstract requires control of inter-annual molecular and aerosol optical depth for emission changes on the order of 1 percent per year. The quoted abstract sentence states that reliably detecting anthropogenic emission changes of that order requires the inter-annual variability of the annual means of those atmospheric parameters to be controlled or efficiently corrected for. No full-text limitation section was read for Bará. Shah and colleagues, in the opened section already quoted on Card 1, state that summer months are under-represented and that this pattern can bias linear trend fits. The Linares abstract, quoted on Card 1, attributes measurement differences in part to atmospheric content. The gap file states that the sparse-series question is a different product from repeating the requirement that dense annual means be controlled. Scale to Philippine sites is unresolved because Philippine rows were not confirmed on the opened Globe at Night page and the opened VIIRS page did not name the Philippines. Candidate venues are Monthly Notices of the Royal Astronomical Society and the Journal of Quantitative Spectroscopy and Radiative Transfer, from the journal DOIs on the opened arXiv abstract pages for Puschnig, Shah, Linares, and Bará. Scopus title records were not displayed. IEEE Xplore returned Error 418. Indexing was not confirmed. These venues are not treated as passing. Publisher HTML was not opened, so volume and page ranges were not read.

### Title

Estimating sparse-site brightness trends for Globe at Night observers Using hierarchical linear models

Word count: 13.

The draft title already matches the form "[action] [outcome] for [context or user] Using [named technique]." The technique name hierarchical linear models is taken from that draft title. The gap statement calls the task a hierarchical estimation and does not name linear models.

### Pitch

Dense photometer studies separate atmospheric covariates from brightness trends. A later study would estimate a sparse Globe at Night year-to-year change after an atmospheric covariate and report thin-sample uncertainty.

Word count: 29.

### Ethics line

The main risk to communities whose outdoor-light trends might be discussed by local government is that publishing a site as worsening can stigmatize a town when the shift is atmospheric, and that citizen coordinates can expose where a person observed at night. The design limits that risk by reporting the adjusted association with the uncertainty from thin annual samples, and by withholding any health finding or legal violation taken from imagery.

### Claim map

| ID | Factual sentence | Gap-card section |
| --- | --- | --- |
| C2-01 | The gap file names the affected population as communities whose outdoor-light trends might be discussed by local government and places SDG 11, Sustainable Cities and Communities, on that line. | Social implication |
| C2-02 | No office is named as the user. | Social implication; writer limit |
| C2-03 | The decision is whether a reported brightening is large enough, after an atmospheric covariate, to justify a ground check of lighting. | Social implication |
| C2-04 | The candidate artifact is an estimate of a year-to-year brightness change in a sparse Globe at Night series after an atmospheric covariate is included, with the uncertainty that comes from thin annual samples. | Gap statement |
| C2-05 | The gap file calls that task a hierarchical estimation. | Gap statement |
| C2-06 | The recorded subdomain is statistical modeling. | Subdomain |
| C2-07 | The dataset lead is Globe at Night observations, the same opened page and unit as Card 1. | Dataset lead |
| C2-08 | Philippine rows were not confirmed on that page. | Dataset lead |
| C2-09 | VIIRS monthly radiance grids are the satellite covariate lead. | Dataset lead |
| C2-10 | The opened VIIRS page states that some areas lack good monthly coverage because of cloud. | Dataset lead |
| C2-11 | No bulk imagery was downloaded. | Dataset lead |
| C2-12 | Copernicus and Earth Engine were not used. | Dataset lead |
| C2-13 | The study would estimate whether a year-to-year brightness change remains in a sparse Globe at Night series after an atmospheric covariate, and would report the uncertainty that comes from thin annual samples, a hierarchical estimation task different from repeating the control of annual-mean atmospheric variability stated in the abstract-only Bará (2024) record. | Gap statement; Nearest studies, Bará (2024) |
| C2-14 | The impact line is a target to test later: whether a year-to-year change remains after the atmospheric covariate, together with the uncertainty that comes from thin annual samples. | Gap statement; Brief |
| C2-15 | The gap file does not name a numeric baseline and does not contain a computed uncertainty. | Gap statement; writer limit |
| C2-16 | This writing pass did not fit a model. | Writer limit; Brief |
| C2-17 | An adjusted trend is an association between the citizen series, the covariate, and time. | Claim boundary |
| C2-18 | It does not establish that lighting practice caused the change, and it does not assign a health or legal label. | Claim boundary |
| C2-19 | Puschnig and colleagues separate atmospheric covariates from anthropogenic zenith-brightness trends with a multivariate penalized linear regression at 26 sky-quality-meter sites. | Gap statement |
| C2-20 | Their opened VIIRS comparison is limited to September through March, because only then does the satellite pass during astronomical night at those sites. | Nearest studies, Puschnig and colleagues |
| C2-21 | Bará (2024) was opened as an abstract only. | Nearest studies, Bará (2024); Unverified leads and blocked pages |
| C2-22 | The gap statement says that abstract requires control of inter-annual molecular and aerosol optical depth for emission changes on the order of 1 percent per year. | Gap statement |
| C2-22a | The quoted abstract sentence states that reliably detecting anthropogenic emission changes of that order requires the inter-annual variability of the annual means of those atmospheric parameters to be controlled or efficiently corrected for. | Nearest studies, Bará (2024) |
| C2-23 | No full-text limitation section was read for Bará. | Nearest studies, Bará (2024) |
| C2-24 | Shah and colleagues, in the opened section already quoted on Card 1, state that summer months are under-represented and that this pattern can bias linear trend fits. | Nearest studies, Shah and colleagues |
| C2-25 | The Linares abstract, quoted on Card 1, attributes measurement differences in part to atmospheric content. | Nearest studies, Linares and colleagues |
| C2-26 | The gap file states that the sparse-series question is a different product from repeating the requirement that dense annual means be controlled. | Gap statement |
| C2-27 | Scale to Philippine sites is unresolved because Philippine rows were not confirmed on the opened Globe at Night page and the opened VIIRS page did not name the Philippines. | Dataset lead; Card 1 dataset lead |
| C2-28 | Candidate venues are Monthly Notices of the Royal Astronomical Society and the Journal of Quantitative Spectroscopy and Radiative Transfer, from the journal DOIs on the opened arXiv abstract pages for Puschnig, Shah, Linares, and Bará. | Candidate venues |
| C2-29 | Scopus title records were not displayed. | Candidate venues |
| C2-30 | IEEE Xplore returned Error 418. | Candidate venues |
| C2-31 | Indexing was not confirmed. | Candidate venues |
| C2-32 | These venues are not treated as passing. | Candidate venues |
| C2-33 | Publisher HTML was not opened, so volume and page ranges were not read. | Unverified leads and blocked pages |
| C2-34 | The draft title already matches the form "[action] [outcome] for [context or user] Using [named technique]." | Draft title; Brief |
| C2-35 | The technique name hierarchical linear models is taken from that draft title. | Draft title |
| C2-36 | The gap statement calls the task a hierarchical estimation and does not name linear models. | Gap statement; Draft title |
| C2-37 | Dense photometer studies separate atmospheric covariates from brightness trends. | Gap statement |
| C2-38 | A later study would estimate a sparse Globe at Night year-to-year change after an atmospheric covariate and report thin-sample uncertainty. | Gap statement |
| C2-39 | The main risk to communities whose outdoor-light trends might be discussed by local government is that publishing a site as worsening can stigmatize a town when the shift is atmospheric, and that citizen coordinates can expose where a person observed at night. | Social implication |
| C2-40 | The design limits that risk by reporting the adjusted association with the uncertainty from thin annual samples, and by withholding any health finding or legal violation taken from imagery. | Social implication; Claim boundary |

## Card 3. Equatorial observatory disturbance flags

### Named user and decision

The gap file names the affected population as GNSS users and power-system operators in equatorial regions and places SDG 9, Industry, Innovation and Infrastructure, on that line. No single office is named as the user. The decision is whether a flagged observatory interval is a reason to inspect positioning quality.

### Demonstrable artifact

The candidate artifact is a multi-day flag for disturbance intervals in equatorial observatory minute values, with a score for coincidence against GNSS positioning-error metrics. The gap file calls that flag a detector evaluation. The recorded subdomain is anomaly detection. The dataset lead is the INTERMAGNET observatory magnetometer series. The opened download page points to a browser portal for provisional and definitive data and to annual reference-set DOIs beginning with `10.5880/INTERMAGNET.1991.2020`. The unit is observatory magnetic values, including the minute-value dissemination format IMFV1 named on the formats page. Philippine observatories were not named on the opened pages and were not counted. No magnetometer archive was downloaded. OMNIWeb is the solar-wind lead cited by Guastavino and by He. The official OMNIWeb pages failed to open, so OMNIWeb is not a confirmed download lead. The gap file does not name a GNSS positioning-error file.

### One-sentence innovation

The study would flag multi-day disturbance intervals in equatorial observatory minute values and score coincidence against GNSS positioning-error metrics, a detector evaluation distinct from the L1 travel-time accounting Guastavino and colleagues (2024) say a real-time SYM-H forecast would still require.

### Measurable impact against a baseline

The impact line is a target to test later: a coincidence score of those flags against GNSS positioning-error metrics. The gap file does not contain a computed coincidence score. This writing pass did not fit a model. A flag and a GNSS error that occur in the same interval are an association. The result would not show that the disturbance caused a positioning failure or a grid fault.

### Transfer or scale

The opened 2022–2026 arXiv record for this seed is thin. Guastavino and colleagues forecast whether the global SYM-H index will fall below −50 nT using an LSTM and an OMNI solar-wind series from 2005 to 2019. Their opened conclusions state that a real-time forecast of SYM-H in the hour after L1 measurements would also have to account for solar-plasma travel time, given as 30 minutes at 800 km s−1 and 60 minutes at 400 km s−1. He and colleagues build one equatorial-electrojet proxy from INTERMAGNET magnetometers at Tatuoca, near the magnetic equator, and San Juan, outside the electrojet belt, for GRB 221009A, and associate the pre-burst deviation with solar-wind speed and IMF Bz. The gap file quotes that discussion as stating that the electrojet was already deviating from quiet-time levels before the burst, ruling out any burst-related origin. Koontaweepunya and colleagues compare a collisional kinetic model of electrojet ions with particle-in-cell simulations and do not analyze observatory series. Their opened conclusions attribute the model’s extreme anisotropy to the BGK collisional operator, which does not include ion angular scattering in velocity space. The gap file states that the proposed flag is distinct from correcting the L1 travel-time delay in the SYM-H forecast and from adding angular scattering to the kinetic collision operator. Philippine observatories were not named on the opened INTERMAGNET pages and were not counted. Guastavino, He, and Koontaweepunya remained preprints on the opened abstract pages. The Koontaweepunya abstract page says “submitted to Frontiers” and shows no journal DOI. The opened journal DOIs in this search for comparable geomagnetic and sky-brightness work point to Monthly Notices of the Royal Astronomical Society and the Journal of Quantitative Spectroscopy and Radiative Transfer. Scopus title records were not displayed. IEEE Xplore returned Error 418. Indexing was not confirmed. These venues are not treated as passing. Linking a flag to an individual’s GNSS track is outside the result the gap file describes.

### Title

Flagging equatorial geomagnetic disturbance intervals for GNSS users Using isolation forest

Word count: 11.

The draft title already matches the form "[action] [outcome] for [context or user] Using [named technique]." The technique name isolation forest is taken from that draft title. The gap statement names a multi-day flag and a coincidence score and does not name isolation forest.

### Pitch

Opened studies forecast global SYM-H or model electrojet ions. A later flag would mark multi-day disturbance intervals in equatorial observatory minute values and score coincidence with GNSS error metrics.

Word count: 29.

### Ethics line

The main risk to GNSS users and power-system operators in equatorial regions is that a flag can be misused as proof that a utility caused an outage or that a navigation service failed. The design limits that risk by reporting coincidence only, and by keeping an individual’s GNSS track out of the result. Observatory coordinates are already public on INTERMAGNET.

### Claim map

| ID | Factual sentence | Gap-card section |
| --- | --- | --- |
| C3-01 | The gap file names the affected population as GNSS users and power-system operators in equatorial regions and places SDG 9, Industry, Innovation and Infrastructure, on that line. | Social implication |
| C3-02 | No single office is named as the user. | Social implication; writer limit |
| C3-03 | The decision is whether a flagged observatory interval is a reason to inspect positioning quality. | Social implication |
| C3-04 | The candidate artifact is a multi-day flag for disturbance intervals in equatorial observatory minute values, with a score for coincidence against GNSS positioning-error metrics. | Gap statement |
| C3-05 | The gap file calls that flag a detector evaluation. | Gap statement |
| C3-06 | The recorded subdomain is anomaly detection. | Subdomain |
| C3-07 | The dataset lead is the INTERMAGNET observatory magnetometer series. | Dataset lead |
| C3-08 | The opened download page points to a browser portal for provisional and definitive data and to annual reference-set DOIs beginning with `10.5880/INTERMAGNET.1991.2020`. | Dataset lead |
| C3-09 | The unit is observatory magnetic values, including the minute-value dissemination format IMFV1 named on the formats page. | Dataset lead |
| C3-10 | Philippine observatories were not named on the opened pages and were not counted. | Dataset lead |
| C3-11 | No magnetometer archive was downloaded. | Dataset lead |
| C3-12 | OMNIWeb is the solar-wind lead cited by Guastavino and by He. | Dataset lead |
| C3-13 | The official OMNIWeb pages failed to open, so OMNIWeb is not a confirmed download lead. | Dataset lead; Unverified leads and blocked pages |
| C3-14 | The gap file does not name a GNSS positioning-error file. | Gap statement; Dataset lead; writer limit |
| C3-15 | The study would flag multi-day disturbance intervals in equatorial observatory minute values and score coincidence against GNSS positioning-error metrics, a detector evaluation distinct from the L1 travel-time accounting Guastavino and colleagues (2024) say a real-time SYM-H forecast would still require. | Gap statement; Nearest studies, Guastavino and colleagues |
| C3-16 | The impact line is a target to test later: a coincidence score of those flags against GNSS positioning-error metrics. | Gap statement; Brief |
| C3-17 | The gap file does not contain a computed coincidence score. | Gap statement; writer limit |
| C3-18 | This writing pass did not fit a model. | Writer limit; Brief |
| C3-19 | A flag and a GNSS error that occur in the same interval are an association. | Claim boundary |
| C3-20 | The result would not show that the disturbance caused a positioning failure or a grid fault. | Claim boundary |
| C3-21 | The opened 2022–2026 arXiv record for this seed is thin. | Gap statement |
| C3-22 | Guastavino and colleagues forecast whether the global SYM-H index will fall below −50 nT using an LSTM and an OMNI solar-wind series from 2005 to 2019. | Gap statement |
| C3-23 | Their opened conclusions state that a real-time forecast of SYM-H in the hour after L1 measurements would also have to account for solar-plasma travel time, given as 30 minutes at 800 km s−1 and 60 minutes at 400 km s−1. | Nearest studies, Guastavino and colleagues |
| C3-24 | He and colleagues build one equatorial-electrojet proxy from INTERMAGNET magnetometers at Tatuoca, near the magnetic equator, and San Juan, outside the electrojet belt, for GRB 221009A, and associate the pre-burst deviation with solar-wind speed and IMF Bz. | Gap statement |
| C3-25 | The gap file quotes that discussion as stating that the electrojet was already deviating from quiet-time levels before the burst, ruling out any burst-related origin. | Nearest studies, He and colleagues |
| C3-26 | Koontaweepunya and colleagues compare a collisional kinetic model of electrojet ions with particle-in-cell simulations and do not analyze observatory series. | Gap statement |
| C3-27 | Their opened conclusions attribute the model’s extreme anisotropy to the BGK collisional operator, which does not include ion angular scattering in velocity space. | Nearest studies, Koontaweepunya and colleagues |
| C3-28 | The gap file states that the proposed flag is distinct from correcting the L1 travel-time delay in the SYM-H forecast and from adding angular scattering to the kinetic collision operator. | Gap statement |
| C3-29 | Philippine observatories were not named on the opened INTERMAGNET pages and were not counted. | Dataset lead |
| C3-30 | Guastavino, He, and Koontaweepunya remained preprints on the opened abstract pages. | Candidate venues; Nearest studies |
| C3-31 | The Koontaweepunya abstract page says “submitted to Frontiers” and shows no journal DOI. | Nearest studies, Koontaweepunya and colleagues |
| C3-32 | The opened journal DOIs in this search for comparable geomagnetic and sky-brightness work point to Monthly Notices of the Royal Astronomical Society and the Journal of Quantitative Spectroscopy and Radiative Transfer. | Candidate venues |
| C3-33 | Scopus title records were not displayed. | Candidate venues |
| C3-34 | IEEE Xplore returned Error 418. | Candidate venues |
| C3-35 | Indexing was not confirmed. | Candidate venues |
| C3-36 | These venues are not treated as passing. | Candidate venues |
| C3-37 | Linking a flag to an individual’s GNSS track is outside the result the gap file describes. | Social implication |
| C3-38 | The draft title already matches the form "[action] [outcome] for [context or user] Using [named technique]." | Draft title; Brief |
| C3-39 | The technique name isolation forest is taken from that draft title. | Draft title |
| C3-40 | The gap statement names a multi-day flag and a coincidence score and does not name isolation forest. | Gap statement; Draft title |
| C3-41 | Opened studies forecast global SYM-H or model electrojet ions. | Gap statement |
| C3-42 | A later flag would mark multi-day disturbance intervals in equatorial observatory minute values and score coincidence with GNSS error metrics. | Gap statement |
| C3-43 | The main risk to GNSS users and power-system operators in equatorial regions is that a flag can be misused as proof that a utility caused an outage or that a navigation service failed. | Social implication |
| C3-44 | The design limits that risk by reporting coincidence only, and by keeping an individual’s GNSS track out of the result. | Social implication; Claim boundary |
| C3-45 | Observatory coordinates are already public on INTERMAGNET. | Social implication |

## Card 4. Blue-weighted brightness below the VIIRS threshold

### Named user and decision

The gap file names the affected population as residents of rural places that fall below the VIIRS radiance threshold and places SDG 11, Sustainable Cities and Communities, on that line. No office is named as the user. The decision is whether a ground brightness check is worth placing where the satellite pixel is dark.

### Demonstrable artifact

The candidate artifact is a prediction of a blue-weighted brightness number at rural sites below the VIIRS radiance threshold, trained on ground reports that are sensitive in the blue, with the prediction error published. The gap file calls that product a regression against ground reports. The recorded subdomain is predictive analytics. The dataset lead is VIIRS Nighttime Light radiance grids. The unit is a global GeoTIFF pixel of monthly cloud-free average radiance, and annual VIIRS nighttime lights. Philippine pixels were not named on the opened page. No tile was downloaded. Ground labels are Globe at Night observations, with the unit one citizen observation. Philippine rows were not confirmed on the opened Globe at Night page.

### One-sentence innovation

The study would publish the prediction error of a blue-weighted brightness number at rural sites below the VIIRS radiance threshold, trained on ground reports that are sensitive in the blue, a test-set regression that the opened methods section of Linares and colleagues (2024 arXiv record) does not provide when it treats Illumina’s compensation for missing blue information in VIIRS-DNB as a model input rather than a ground-report prediction at unsampled rural pixels.

### Measurable impact against a baseline

The impact line is a target to test later: the published prediction error of that blue-weighted brightness number. The gap file does not name a baseline predictor and does not contain a computed error. This writing pass did not fit a model. The prediction is an association between a ground report and satellite radiance. It does not assign a health or legal label from the image.

### Transfer or scale

Barentine’s opened review states that VIIRS-DNB does not sense shortward of 500 nm and therefore misses the blue LED peak near 450 nm. The gap file states that the open study is distinct from restating that instrument band limit, because the output is a site-level prediction with a test set rather than a description of the satellite band. Buhler and colleagues state that direct illuminance inherits a minimum VIIRS radiance and that pixels below the detection threshold usually correspond to rural areas. Their opened Figure 6 caption, quoted on Card 1, states that those maps are primarily useful to highlight areas where light sources are concentrated, and not for a lighting analysis on the typical spatial scale of buildings or streets. Puschnig and colleagues supply the September–March VIIRS coverage limit quoted on Card 2. Linares and colleagues state that Illumina can compensate for missing blue information in VIIRS-DNB by using source spectra and the instrument’s spectral sensitivity, and the gap file states that this compensation is a model input, not a ground-report prediction at unsampled rural pixels. A dark pixel is not published here as proof that a place has no lighting. Scale to Philippine sites is unresolved because Philippine pixels were not named on the opened VIIRS page and Philippine rows were not confirmed on the opened Globe at Night page. Candidate venues are Monthly Notices of the Royal Astronomical Society and the Journal of Quantitative Spectroscopy and Radiative Transfer, from the journal DOIs opened on the arXiv abstract pages. Scopus title records were not displayed. IEEE Xplore returned Error 418. Indexing was not confirmed. These venues are not treated as passing. Buhler and colleagues remained an arXiv preprint. Publisher HTML was not opened, so volume and page ranges were not read.

### Title

Predicting blue-weighted sky brightness for VIIRS-dark rural sites Using random forest

Word count: 11.

The draft title already matches the form "[action] [outcome] for [context or user] Using [named technique]." The technique name random forest is taken from that draft title. The gap statement calls the product a regression against ground reports and does not name random forest.

### Pitch

VIIRS misses the blue LED peak, and rural pixels often fall below its radiance threshold. A later regression would predict blue-weighted brightness there from ground reports and publish the error.

Word count: 30.

### Ethics line

The main risk to residents of rural places below the VIIRS radiance threshold is that a dark pixel can be published as proof that a place has no lighting, and that a bright prediction can be treated as a health finding or a legal violation. The design limits that risk by keeping the prediction an association between a ground report and satellite radiance, and by withholding any health or legal label taken from the image. Citizen-report coordinates carry the presence-privacy risk already recorded for Globe at Night.

### Claim map

| ID | Factual sentence | Gap-card section |
| --- | --- | --- |
| C4-01 | The gap file names the affected population as residents of rural places that fall below the VIIRS radiance threshold and places SDG 11, Sustainable Cities and Communities, on that line. | Social implication |
| C4-02 | No office is named as the user. | Social implication; writer limit |
| C4-03 | The decision is whether a ground brightness check is worth placing where the satellite pixel is dark. | Social implication |
| C4-04 | The candidate artifact is a prediction of a blue-weighted brightness number at rural sites below the VIIRS radiance threshold, trained on ground reports that are sensitive in the blue, with the prediction error published. | Gap statement |
| C4-05 | The gap file calls that product a regression against ground reports. | Gap statement |
| C4-06 | The recorded subdomain is predictive analytics. | Subdomain |
| C4-07 | The dataset lead is VIIRS Nighttime Light radiance grids. | Dataset lead |
| C4-08 | The unit is a global GeoTIFF pixel of monthly cloud-free average radiance, and annual VIIRS nighttime lights. | Dataset lead |
| C4-09 | Philippine pixels were not named on the opened page. | Dataset lead |
| C4-10 | No tile was downloaded. | Dataset lead |
| C4-11 | Ground labels are Globe at Night observations, with the unit one citizen observation. | Dataset lead |
| C4-12 | Philippine rows were not confirmed on the opened Globe at Night page. | Dataset lead |
| C4-13 | The study would publish the prediction error of a blue-weighted brightness number at rural sites below the VIIRS radiance threshold, trained on ground reports that are sensitive in the blue, a test-set regression that the opened methods section of Linares and colleagues (2024 arXiv record) does not provide when it treats Illumina’s compensation for missing blue information in VIIRS-DNB as a model input rather than a ground-report prediction at unsampled rural pixels. | Gap statement; Nearest studies, Linares and colleagues |
| C4-14 | The impact line is a target to test later: the published prediction error of that blue-weighted brightness number. | Gap statement; Brief |
| C4-15 | The gap file does not name a baseline predictor and does not contain a computed error. | Gap statement; writer limit |
| C4-16 | This writing pass did not fit a model. | Writer limit; Brief |
| C4-17 | The prediction is an association between a ground report and satellite radiance. | Claim boundary |
| C4-18 | It does not assign a health or legal label from the image. | Claim boundary |
| C4-19 | Barentine’s opened review states that VIIRS-DNB does not sense shortward of 500 nm and therefore misses the blue LED peak near 450 nm. | Gap statement |
| C4-20 | The gap file states that the open study is distinct from restating that instrument band limit, because the output is a site-level prediction with a test set rather than a description of the satellite band. | Gap statement |
| C4-21 | Buhler and colleagues state that direct illuminance inherits a minimum VIIRS radiance and that pixels below the detection threshold usually correspond to rural areas. | Gap statement; Nearest studies, Buhler and colleagues |
| C4-22 | Their opened Figure 6 caption, quoted on Card 1, states that those maps are primarily useful to highlight areas where light sources are concentrated, and not for a lighting analysis on the typical spatial scale of buildings or streets. | Nearest studies, Buhler and colleagues |
| C4-23 | Puschnig and colleagues supply the September–March VIIRS coverage limit quoted on Card 2. | Nearest studies, Puschnig and colleagues |
| C4-24 | Linares and colleagues state that Illumina can compensate for missing blue information in VIIRS-DNB by using source spectra and the instrument’s spectral sensitivity, and the gap file states that this compensation is a model input, not a ground-report prediction at unsampled rural pixels. | Nearest studies, Linares and colleagues |
| C4-25 | A dark pixel is not published here as proof that a place has no lighting. | Social implication |
| C4-26 | Scale to Philippine sites is unresolved because Philippine pixels were not named on the opened VIIRS page and Philippine rows were not confirmed on the opened Globe at Night page. | Dataset lead |
| C4-27 | Candidate venues are Monthly Notices of the Royal Astronomical Society and the Journal of Quantitative Spectroscopy and Radiative Transfer, from the journal DOIs opened on the arXiv abstract pages. | Candidate venues |
| C4-28 | Scopus title records were not displayed. | Candidate venues |
| C4-29 | IEEE Xplore returned Error 418. | Candidate venues |
| C4-30 | Indexing was not confirmed. | Candidate venues |
| C4-31 | These venues are not treated as passing. | Candidate venues |
| C4-32 | Buhler and colleagues remained an arXiv preprint. | Nearest studies, Buhler and colleagues, as in Card 1 |
| C4-33 | Publisher HTML was not opened, so volume and page ranges were not read. | Unverified leads and blocked pages |
| C4-34 | The draft title already matches the form "[action] [outcome] for [context or user] Using [named technique]." | Draft title; Brief |
| C4-35 | The technique name random forest is taken from that draft title. | Draft title |
| C4-36 | The gap statement calls the product a regression against ground reports and does not name random forest. | Gap statement; Draft title |
| C4-37 | VIIRS misses the blue LED peak, and rural pixels often fall below its radiance threshold. | Gap statement |
| C4-38 | A later regression would predict blue-weighted brightness there from ground reports and publish the error. | Gap statement |
| C4-39 | The main risk to residents of rural places below the VIIRS radiance threshold is that a dark pixel can be published as proof that a place has no lighting, and that a bright prediction can be treated as a health finding or a legal violation. | Social implication |
| C4-40 | The design limits that risk by keeping the prediction an association between a ground report and satellite radiance, and by withholding any health or legal label taken from the image. | Social implication; Claim boundary |
| C4-41 | Citizen-report coordinates carry the presence-privacy risk already recorded for Globe at Night. | Social implication |

## Unresolved inputs

1. Scopus indexing was not confirmed. The Sources preview at `https://www.scopus.com/sources.uri?search=Monthly+Notices+of+the+Royal+Astronomical+Society` opened, and the loaded text did not list Monthly Notices of the Royal Astronomical Society, the Journal of Quantitative Spectroscopy and Radiative Transfer, or Nature Astronomy. Those venues are not treated as passing.
2. IEEE indexing was not confirmed. The Xplore search for `night sky brightness`, years 2022–2026, returned “Unusual Traffic Detected (Error 418)” and no results list. The gap file does not record a separate IEEE search for the geomagnetic seed.
3. Philippine rows were not confirmed. Globe at Night rows were not listed on the opened page and were not counted. The retired count of 323 Philippine Globe at Night rows is not reused, and the retired count of 274 Philippine WDPA designations is not reused. The opened VIIRS page did not name the Philippines. Philippine observatories were not named on the opened INTERMAGNET pages and were not counted. No bulk imagery or magnetometer archive was downloaded.
4. Bará (2024), DOI `10.1016/j.jqsrt.2024.109187` and `10.48550/arXiv.2405.08279`, is abstract-only. `https://arxiv.org/html/2405.08279` returned “No HTML for '2405.08279'.” No full-text limitation section was read. The about-1-percent-per-year statement is the opened abstract, not a full-text result of this writing pass.
5. OMNIWeb is an unverified lead. `https://omniweb.gsfc.nasa.gov/` and `https://omniweb.gsfc.nasa.gov/html/ow_data.html` failed to open. Guastavino (2024) and He (2026) cite it. It is not a confirmed download. The 2005–2019 OMNI series is their described input, not a file saved here.
6. No GNSS positioning-error file is named. The Card 3 coincidence score against those metrics is a target to test, not a computed result, and it is not evidence that a disturbance caused a positioning failure or a grid fault.
7. No model was fit. Reported prediction error, thin-sample uncertainty, and the GNSS coincidence score are targets to test. Baseline predictors are not named for Cards 1, 2, and 4.
8. Draft-title technique names are unresolved against the gap statements. Gradient boosting (Card 1), isolation forest (Card 3), and random forest (Card 4) are not named in those gap statements. Card 2 says “hierarchical estimation,” and the draft title says “hierarchical linear models.”
9. Publisher HTML for Nature Astronomy, Monthly Notices, and the Journal of Quantitative Spectroscopy and Radiative Transfer was not opened. Volume and page ranges were not read. DOIs were read on arXiv abstract pages. Linares is labeled a 2024 arXiv record while the journal DOI is `10.1016/j.jqsrt.2023.108678`. That year label was not reconciled.
10. Guastavino (2024), He (2026), Koontaweepunya (2024), and Buhler (2025) remained preprints on the opened abstract pages, with no journal DOI recorded there. Koontaweepunya is recorded as “submitted to Frontiers.”
11. OpenAlex CLI calls hung or stalled, and the arXiv CLI light-pollution search hung. Those runs are not empty searches. Numeric search counts in the gap file come from arXiv HTML pages. The light-pollution HTML date filter did not remove pre-2022 hits. A VIIRS login requirement was not tested.
12. These leads were not opened and are not nearest studies: arXiv:2603.01881, and Kyba and colleagues, Scientific Reports, 2013, DOI `10.1038/srep01835`, cited inside Barentine (2022). Earth Engine, Copernicus accounts, scraping, and partner data requests were out of scope.
13. Citation-management scripts were not run. Bibliographic strings were not re-resolved. No ethics approval, author list, analysis plan, or AI-use declaration is in the gap file. SDG labels are the social-implication lines as written there.
