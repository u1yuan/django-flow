# Gap candidates — astronomy

Generated: 2026-10-06
Review type: scoping
Search window: 2022-01-01 through 2026-10-06
Field: night-sky brightness estimation and equatorial geomagnetic disturbance detection

These are candidate gaps. This file does not claim that any gap is novel.

Skills used: `literature-search-openalex` and `literature-search-arxiv`. License notices were already present under `.licenses/` and were not recreated. OpenAlex and arXiv CLI calls were made with `uv run` from those skill directories. The CLIs did not return usable JSON. Paper selection below uses arXiv HTML search pages and paper, abstract, dataset, and index pages opened in a browser on 2026-10-06. URLs of pages used are listed at the end.

## Search log

| Database | Date searched | Query | Filters | Results |
| --- | --- | --- | --- | --- |
| OpenAlex CLI `filter works` | 2026-10-06 | `night sky brightness light pollution` | `publication_year:2022-2026,type:review`; sort `cited_by_count:desc`; per-page 8 | Hung. No usable JSON. Process ran about 33 minutes and ended with exit code 4294967295. Not an empty result. |
| OpenAlex CLI `get works` | 2026-10-06 | `https://doi.org/10.1038/s41586-021-03819-2` | select `id,display_name,publication_year,doi` | Stalled. No usable record. Not an empty result. No further OpenAlex filter was started. |
| arXiv CLI `search_arxiv.py` | 2026-10-06 | `all:light AND all:pollution AND all:sky AND submittedDate:[202201010000 TO 202610062359]` | `--max_results 8`; sort `submittedDate` descending | Hung. No usable JSON after more than 11 minutes. Not an empty result. |
| arXiv HTML search | 2026-10-06 | `light pollution sky brightness` | all fields; abstracts shown; newest first; size 50. A date-range parameter was in the URL and did not remove pre-2022 hits from the opened page | Showing 1–50 of 70 |
| arXiv HTML search | 2026-10-06 | `equatorial geomagnetic disturbance OR equatorial electrojet` | all fields; abstracts shown; newest first; size 25 | Showing 1–5 of 5. One hit was announced in 2026. The other four were announced in 2019 or earlier. |
| arXiv HTML search | 2026-10-06 | `geomagnetic storm detection` | all fields; abstracts shown; newest first; size 25 | Showing 1–25 of 51 |
| arXiv HTML search | 2026-10-06 | `INTERMAGNET OR "equatorial electrojet" OR "low-latitude geomagnetic"` | all fields; abstracts shown; newest first; size 25 | Showing 1–21 of 21. Opened 2022–2026 items are a kinetic electrojet model and a single-event equatorial-electrojet reassessment, plus the separate SYM-H forecast found on the storm-detection page. |
| arXiv HTML search | 2026-10-06 | `"Globe at Night" OR VIIRS "sky brightness"` | all fields; abstracts shown; newest first; size 25 | Showing 1–25 of 328. The opened first page was dominated by general sky-brightness papers. Globe at Night was read in Barentine (2022), not as a hit title on that first page. |

## Inclusion and exclusion

Included as nearest studies only when the work was announced or published in 2022–2026 and the arXiv HTML, the arXiv abstract page, or both were opened in this run. A limitation sentence is quoted only from text that was opened. An abstract supports only what that abstract states.

Excluded from nearest studies: pre-2022 papers seen on the HTML search pages; hydroponics and diesel; Earth Engine and any bulk imagery or magnetometer archive; a health or legal label inferred from imagery; a claim that a geomagnetic disturbance caused a grid fault or a positioning failure. The retired screen counts of 323 Philippine Globe at Night rows and 274 Philippine WDPA designations are not reused as measurements.

Journal indexing: the Scopus Sources preview at `https://www.scopus.com/sources.uri?search=Monthly+Notices+of+the+Royal+Astronomical+Society` opened, and the loaded text did not list Monthly Notices, the Journal of Quantitative Spectroscopy and Radiative Transfer, or Nature Astronomy. IEEE Xplore search for `night sky brightness` returned “Unusual Traffic Detected (Error 418)” and no results list. Indexing was not confirmed. Those venues are not treated as passing.

## Card 1 — Sparse-site zenith brightness

**Gap statement.** Opened 2022–2026 studies estimate night-sky brightness with radiative-transfer maps and with dense sky-quality-meter networks. Linares and colleagues compare Illumina v2 maps of Catalonia with measurements at nineteen locations. Buhler and colleagues calibrate Otus 3 on 139 French sites using VIIRS ground radiance. Shah and colleagues rank year-to-year brightness changes at 27 stations in the northern Netherlands and on the western German Wadden coast. Barentine’s review describes Globe at Night naked-eye reports and the spectral limit of VIIRS-DNB. The open study is a held-out prediction of zenith brightness at sites that have only sparse citizen reports, with Globe at Night observations and VIIRS radiance as covariates and with a reported error. That prediction is a separate analysis from restating the VIIRS blue-light limit or from adding more photometers.

**Nearest studies.**

- John C. Barentine, 2022. “Night Sky Brightness Measurement, Quality Assessment and Monitoring.” DOI `10.1038/s41550-022-01756-2`, also `10.48550/arXiv.2207.03551`. Venue: Nature Astronomy, from the arXiv abstract page comment “accepted for publication by Nature Astronomy” and the Nature-family DOI on that page. The Nature HTML was not opened. Opened: arXiv HTML full text, `https://arxiv.org/html/2207.03551`. Locator: VIIRS-DNB paragraph in the sensing section. Quote: “The instrument is therefore effectively blind to the strong peak in white LED light emissions near 450 nm.”
- Hector Linares, Eduard Masana, Salvador J. Ribas, Manuel García-Gil, Martin Aubé, Alejandro Sánchez de Miguel, and Alexandre Simoneau, 2024 arXiv record. “Assessing light pollution in vast areas: zenith sky brightness maps of Catalonia.” DOI `10.1016/j.jqsrt.2023.108678`, also `10.48550/arXiv.2403.00112`. Venue: Journal of Quantitative Spectroscopy and Radiative Transfer, from the DOI on the arXiv abstract page. Publisher HTML was not opened, so volume and pages were not read. Opened: arXiv HTML full text, `https://arxiv.org/html/2403.00112`. Locator: abstract. Quote: “When comparing to measurements we found small differences mainly due to mismatching in the location of the points studied, and also due to differences in the natural sky brightness and atmospheric content.”
- Rolf Buhler, Philippe Deverchère, Christophe Plotard, and Sébastien Vauclair, 2025. “Multi-faceted light pollution modelling and its application to the decline of artificial illuminance in France.” DOI `10.48550/arXiv.2510.02977`. Venue: arXiv preprint; the abstract page showed no journal DOI. Opened: arXiv HTML full text, `https://arxiv.org/html/2510.02977`. Locator: Figure 6 caption. Quote: “Illuminance maps based on VIIRS-DNB data are therefore primarily useful to highlight areas where light sources are concentrated and not for a lighting analysis on the typical spatial scale of buildings or streets.”
- Farhan R. Shah, Reynier F. Peletier, Jake Noel-Storr, Dirk van der Geest, Theo Jurriens, Andreas Hänel, Tobias Hoffmann, Lisa Cordes, Robin Will, Athleen Selma Rietze, Matti Gehlen, Hans Kjeldsen, Cristina Nazzari, and Björn Poppe, 2025. “Beyond the Clouds: Advanced Data Analysis of a Dutch Sky Quality Meter Network.” DOI `10.1093/mnras/staf1200`, also `10.48550/arXiv.2507.11343`. Venue: Monthly Notices of the Royal Astronomical Society, from the DOI on the arXiv abstract page. Publisher HTML was not opened. Opened: arXiv HTML full text, `https://arxiv.org/html/2507.11343`. Locator: section 4.1, “Limitations of Trend Analyses and Future Directions.” Quote: “However, without additional contextual data, understanding the underlying drivers of these trends remains elusive.”

**Candidate venues.** Monthly Notices of the Royal Astronomical Society and the Journal of Quantitative Spectroscopy and Radiative Transfer published the comparable 2022–2025 studies whose DOIs were read on arXiv abstract pages. Scopus Sources preview was opened and did not display those titles. IEEE Xplore returned Error 418. Indexing not confirmed. These venues are not treated as passing.

**Social implication.** Affected population: residents and volunteer observers in places with few fixed photometers. Sustainable Development Goal 11, Sustainable Cities and Communities. Decision informed: where a municipality schedules a follow-up sky-brightness measurement. Harm note: Globe at Night records can show where a person observed at night, so a public file can expose presence; a brightness estimate can stigmatize a neighborhood if it is published as a ranked failure; the estimate must not be used as a health finding or as a legal lighting violation taken from imagery alone.

**Draft title.** Estimating zenith sky brightness for sparsely reported sites Using gradient boosting. Word count: 11.

**Subdomain.** predictive analytics

**Dataset lead.** Globe at Night citizen observations. Official page opened: `https://globeatnight.org/maps-data/`. The page states that observations are available to download and gives 2025 as 13421 total observations, with a CSV link `https://globeatnight.org/documents/1190/GaN2025.csv`. Unit: one citizen night-sky observation. Coverage described on the page: international campaign since 2006. Philippine rows were not listed on the opened page and were not counted in this run. The retired count of 323 Philippine rows is not reused. A second lead, not downloaded: Earth Observation Group VIIRS Nighttime Light, `https://eogdata.mines.edu/products/vnl/`, global monthly cloud-free average radiance grids and annual VIIRS nighttime lights as GeoTIFF pixels. The opened page did not name the Philippines. An Accounts link is on the page; a download was not started, so a login requirement was not tested.

**Claim boundary.** A predicted brightness is an association between reports, radiance, and the held-out observation. It is not a cause of a health outcome and not a legal status read from the image.

## Card 2 — Atmospheric contribution to sparse brightness trends

**Gap statement.** Puschnig and colleagues separate atmospheric covariates from anthropogenic zenith-brightness trends with a multivariate penalized linear regression at 26 sky-quality-meter sites, and they report that VIIRS coverage at those sites is limited to September through March. Bará’s abstract states that emission changes on the order of 1 percent per year require control of inter-annual molecular and aerosol optical depth. Shah and colleagues report that seasonal gaps in the Dutch network can bias a linear trend. The open study is to estimate a year-to-year brightness change in sparse Globe at Night series after an atmospheric covariate is included, and to report the uncertainty that comes from thin annual samples. That is a hierarchical estimation task. It asks whether a change remains after the covariate adjustment in a sparse citizen series, which is a different product from repeating the requirement that dense annual means be controlled.

**Nearest studies.**

- Johannes Puschnig, Stefan Wallner, Axel Schwope, and Magnus Näslund, 2022. “Long-term trends of light pollution assessed from SQM measurements and an empirical atmospheric model.” DOI `10.1093/mnras/stac3003`, also `10.48550/arXiv.2210.09177`. Venue: Monthly Notices of the Royal Astronomical Society, from the abstract-page comment “accepted for publication in MNRAS” and the journal DOI. Publisher HTML was not opened. Opened: arXiv HTML full text, `https://arxiv.org/html/2210.09177`. Locator: Discussion, VIIRS comparison. Quote: “First of all, VIIRS data is only available for our sites between September and March, because only during these months the satellite passes during astronomical night.”
- Salvador Bará, 2024. “Detecting changes in anthropogenic light emissions: limits due to atmospheric variability.” DOI `10.1016/j.jqsrt.2024.109187`, also `10.48550/arXiv.2405.08279`. Venue: Journal of Quantitative Spectroscopy and Radiative Transfer, from the DOI on the arXiv abstract page. Publisher HTML was not opened. Opened: abstract only at `https://arxiv.org/abs/2405.08279`. HTML conversion for `2405.08279` was unavailable, so no full-text limitation section was read. Locator: abstract. Quote: “It is shown that for reliably detecting changes in the anthropogenic light emissions of order ~1% per year, the inter-annual variability of the annual means of these atmospheric parameters in the measurement datasets must be carefully controlled or efficiently corrected for.”
- Farhan R. Shah and coauthors, 2025, as in Card 1. DOI `10.1093/mnras/staf1200`. Opened: arXiv HTML full text. Locator: section 4.1, sampling-bias paragraph. The one quoted sentence for this paper is in Card 1. The same opened section also states that summer months are under-represented and that this pattern can bias linear trend fits.
- Hector Linares and coauthors, 2024 arXiv record, as in Card 1. DOI `10.1016/j.jqsrt.2023.108678`. Opened: arXiv HTML full text. The abstract, quoted in Card 1, attributes measurement differences in part to atmospheric content.

**Candidate venues.** Monthly Notices of the Royal Astronomical Society and the Journal of Quantitative Spectroscopy and Radiative Transfer, from the journal DOIs on the opened arXiv abstract pages for Puschnig, Shah, Linares, and Bará. Scopus title records were not displayed. IEEE Xplore returned Error 418. Indexing not confirmed. These venues are not treated as passing.

**Social implication.** Affected population: communities whose outdoor-light trends might be discussed by local government. Sustainable Development Goal 11, Sustainable Cities and Communities. Decision informed: whether a reported brightening is large enough, after an atmospheric covariate, to justify a ground check of lighting. Harm note: publishing a site as “worsening” can stigmatize a town when the shift is atmospheric; citizen coordinates raise the same presence-privacy issue as in Card 1; the result must not be used as a health finding or as a legal violation taken from imagery.

**Draft title.** Estimating sparse-site brightness trends for Globe at Night observers Using hierarchical linear models. Word count: 13.

**Subdomain.** statistical modeling

**Dataset lead.** Globe at Night observations, same opened page and unit as Card 1 (`https://globeatnight.org/maps-data/`; 2025 CSV of observations). Philippine rows were not confirmed on that page. VIIRS monthly radiance grids, `https://eogdata.mines.edu/products/vnl/`, are the satellite covariate lead. The opened VIIRS page states that some areas lack good monthly coverage because of cloud. No bulk imagery was downloaded. Copernicus and Earth Engine were not used.

**Claim boundary.** An adjusted trend is an association between the citizen series, the covariate, and time. It does not establish that lighting practice caused the change, and it does not assign a health or legal label.

## Card 3 — Equatorial observatory disturbance flags

**Gap statement.** The opened 2022–2026 arXiv record for this seed is thin. Guastavino and colleagues forecast whether the global SYM-H index will fall below −50 nT using an LSTM and OMNI solar-wind series from 2005 to 2019. He and colleagues build one equatorial-electrojet proxy from INTERMAGNET magnetometers at Tatuoca, near the magnetic equator, and San Juan, outside the electrojet belt, for GRB 221009A, and they associate the pre-burst deviation with solar-wind speed and IMF Bz. Koontaweepunya and colleagues compare a collisional kinetic model of electrojet ions with particle-in-cell simulations and do not analyze observatory series. The open study is a multi-day flag for disturbance intervals in equatorial observatory minute values, with a score for coincidence against GNSS positioning-error metrics. That flag is a detector evaluation. It is distinct from correcting the L1 travel-time delay in the SYM-H forecast and from adding angular scattering to the kinetic collision operator.

**Nearest studies.**

- Sabrina Guastavino, Katsiaryna Bahamazava, Emma Perracchione, Fabiana Camattari, Gianluca Audone, Daniele Telloni, Roberto Susino, Gianalfredo Nicolini, Silvano Fineschi, Michele Piana, and Anna Maria Massone, 2024. “Forecasting Geoffective Events from Solar Wind Data and Evaluating the Most Predictive Features through Machine Learning Approaches.” DOI `10.48550/arXiv.2403.09847`. Venue: arXiv preprint; the abstract page showed no journal DOI. Opened: arXiv HTML full text, `https://arxiv.org/html/2403.09847`. Locator: section V, Conclusions. Quote: “However, if the tool worked in real time in forecasting the value of SYM-H in the hour after the acquisition of solar measurements at L1, the time required for the solar plasma to reach Earth, i.e., 30 minutes (60 minutes) for a bulk speed of 800 (400) km s-1, would also have to be accounted for.”
- Maosheng He, Quanhan Li, Shun-Rong Zhang, Jeffrey M. Forbes, Jiuhou Lei, Libo Liu, Jiankui Shi, and Chi Wang, 2026. “Reassessment of Ionospheric Responses to GRB 221009A: Disentangling Instrumental, Illumination and Geophysical Effects.” DOI `10.48550/arXiv.2605.19608`. Venue: arXiv preprint; the abstract page showed no journal DOI. Opened: arXiv HTML full text, `https://arxiv.org/html/2605.19608`. Locator: Discussion, “EEJ Variability Driven by Solar-Wind Forcing.” Quote: “The EEJ was already deviating from quiet-time levels before GRB 221009A, ruling out any burst-related origin and contradicting earlier claims of GRB-induced low-frequency fluctuations.”
- Rattanakorn Koontaweepunya, Yakov S. Dimant, and Meers M. Oppenheim, 2024. “Non-Maxwellian Ion Distribution in the Equatorial and Auroral Electrojets.” DOI `10.48550/arXiv.2408.06339`. Venue: arXiv preprint; the abstract page says “submitted to Frontiers” and shows no journal DOI. Opened: arXiv HTML full text, `https://arxiv.org/html/2408.06339`. Locator: Conclusions. Quote: “The reason for this extreme anisotropy lies in the fact that the BGK collisional operator does not include any ion angular scattering in the velocity space.”

**Candidate venues.** The opened journal DOIs in this search for comparable geomagnetic and sky-brightness work point to Monthly Notices of the Royal Astronomical Society and the Journal of Quantitative Spectroscopy and Radiative Transfer. Guastavino, He, and Koontaweepunya remained preprints on the opened abstract pages. Scopus title records were not displayed. IEEE Xplore returned Error 418. Indexing not confirmed. These venues are not treated as passing.

**Social implication.** Affected population: GNSS users and power-system operators in equatorial regions. Sustainable Development Goal 9, Industry, Innovation and Infrastructure. Decision informed: whether a flagged observatory interval is a reason to inspect positioning quality. Harm note: a flag can be misused as proof that a utility caused an outage or that a navigation service failed; this study would report coincidence only. Observatory coordinates are already public on INTERMAGNET. Linking flags to an individual’s GNSS track could expose movement and should stay out of the result.

**Draft title.** Flagging equatorial geomagnetic disturbance intervals for GNSS users Using isolation forest. Word count: 11.

**Subdomain.** anomaly detection

**Dataset lead.** INTERMAGNET observatory magnetometer series. Pages opened: `https://intermagnet.org/`, `https://intermagnet.org/data_formats.html`, and `https://intermagnet.org/data_download.html`. The download page points to a browser portal at `https://imag-data.bgs.ac.uk/GIN_V1/GINForms2` for provisional and definitive data, and to annual reference-set DOIs beginning with `https://doi.org/10.5880/INTERMAGNET.1991.2020`. Unit: observatory magnetic values, including the minute-value dissemination format IMFV1 named on the formats page. Philippine observatories were not named on the opened pages and were not counted. No magnetometer archive was downloaded. OMNIWeb is the solar-wind lead cited by Guastavino and by He; the official pages failed to open in this run and are listed under blocked pages, so OMNIWeb is not a confirmed download lead here.

**Claim boundary.** A flag and a GNSS error that occur in the same interval are an association. The result would not show that the disturbance caused a positioning failure or a grid fault.

## Card 4 — Blue-weighted brightness below the VIIRS threshold

**Gap statement.** Barentine’s opened review states that VIIRS-DNB does not sense shortward of 500 nm and therefore misses the blue LED peak near 450 nm. Buhler and colleagues, in the opened Otus 3 paper, state that direct illuminance inherits a minimum VIIRS radiance and that rural pixels are often below that threshold, while the maps describe concentrations of light rather than street-scale lighting. The open study is to predict a blue-weighted brightness number at rural sites below that threshold, trained on ground reports that are sensitive in the blue, and to publish the prediction error. That is a regression against ground reports. It is distinct from restating the instrument band limit, because the output is a site-level prediction with a test set rather than a description of the satellite band.

**Nearest studies.**

- John C. Barentine, 2022, as in Card 1. DOI `10.1038/s41550-022-01756-2`. Opened: arXiv HTML full text. The VIIRS sentence quoted in Card 1 is the locator.
- Rolf Buhler, Philippe Deverchère, Christophe Plotard, and Sébastien Vauclair, 2025, as in Card 1. DOI `10.48550/arXiv.2510.02977`. Opened: arXiv HTML full text. Locator: paragraph on the VIIRS minimum radiance for direct illuminance, in addition to the Figure 6 sentence quoted in Card 1. That paragraph states that pixels below the detection threshold usually correspond to rural areas and that the threshold should be kept in mind when using direct-illuminance maps.
- Johannes Puschnig, Stefan Wallner, Axel Schwope, and Magnus Näslund, 2022, as in Card 2. DOI `10.1093/mnras/stac3003`. Opened: arXiv HTML full text. The September–March VIIRS sentence quoted in Card 2 is the seasonal-coverage locator.
- Hector Linares and coauthors, 2024 arXiv record, as in Card 1. DOI `10.1016/j.jqsrt.2023.108678`. Opened: arXiv HTML full text. The methods section states that Illumina can compensate for missing blue information in VIIRS-DNB by using source spectra and the instrument’s spectral sensitivity. That compensation is a model input, not a ground-report prediction at unsampled rural pixels.

**Candidate venues.** Monthly Notices of the Royal Astronomical Society and the Journal of Quantitative Spectroscopy and Radiative Transfer, from the journal DOIs opened on the arXiv abstract pages. Scopus title records were not displayed. IEEE Xplore returned Error 418. Indexing not confirmed. These venues are not treated as passing.

**Social implication.** Affected population: residents of rural places that fall below the VIIRS radiance threshold. Sustainable Development Goal 11, Sustainable Cities and Communities. Decision informed: whether a ground brightness check is worth placing where the satellite pixel is dark. Harm note: a dark pixel must not be published as proof that a place has no lighting, and a bright prediction must not become a health finding or a legal violation. Citizen-report coordinates carry the presence-privacy risk already noted.

**Draft title.** Predicting blue-weighted sky brightness for VIIRS-dark rural sites Using random forest. Word count: 11.

**Subdomain.** predictive analytics

**Dataset lead.** VIIRS Nighttime Light radiance grids, page opened at `https://eogdata.mines.edu/products/vnl/`. Unit: global GeoTIFF pixel of monthly cloud-free average radiance, and annual VIIRS nighttime lights. Philippine pixels were not named on the page. No tile was downloaded. Ground labels: Globe at Night observations, `https://globeatnight.org/maps-data/`, unit one citizen observation, Philippine rows not confirmed on the opened page.

**Claim boundary.** The prediction is an association between a ground report and satellite radiance. It does not assign a health or legal label from the image.

## Unverified leads and blocked pages

- OpenAlex review filter and the later DOI probe hung or stalled. They are not empty searches.
- arXiv CLI `search_arxiv.py` for the light-pollution query hung with no JSON. Counts in the search log that have numbers come from arXiv HTML search pages, not from the CLI.
- `https://arxiv.org/html/2405.08279` returned “No HTML for '2405.08279'.” Bará (2024) is abstract-only.
- `https://omniweb.gsfc.nasa.gov/` and `https://omniweb.gsfc.nasa.gov/html/ow_data.html` returned a browser chrome error. OMNIWeb remains a lead cited by Guastavino (2024) and He (2026), not a confirmed download.
- IEEE Xplore search `night sky brightness`, years 2022–2026: “Unusual Traffic Detected (Error 418).” No journal list was opened.
- Scopus Sources preview opened at `https://www.scopus.com/sources.uri?search=Monthly+Notices+of+the+Royal+Astronomical+Society` and the loaded text did not list the target journals. Indexing not confirmed.
- Publisher HTML for Nature Astronomy, MNRAS, and JQSRT was not opened. Volume and page ranges were not read. DOIs were read on the arXiv abstract pages.
- arXiv:2603.01881, “Cross-sphere Coupling and Source Inversion of Ionospheric Disturbances Associated with the 2025 Myanmar Strike-slip Earthquake,” was visible on the five-hit electrojet search and was not opened.
- Kyba and colleagues, Scientific Reports, 2013, DOI `10.1038/srep01835`, is cited inside Barentine (2022) for Globe at Night aggregate agreement. That paper was not opened. The citation is a lead.
- Earth Engine, Copernicus accounts, scraping, and partner data requests were out of scope. No bulk imagery or magnetometer archive was saved.

## Pages used

- `https://arxiv.org/search/?searchtype=all&query=light+pollution+sky+brightness&abstracts=show&order=-announced_date_first&size=50&date-from_date=2022-01-01&date-to_date=2026-10-06&date-filter_by=date_range`
- `https://arxiv.org/search/?searchtype=all&query=equatorial+geomagnetic+disturbance+OR+equatorial+electrojet&abstracts=show&order=-announced_date_first&size=25`
- `https://arxiv.org/search/?searchtype=all&query=geomagnetic+storm+detection&abstracts=show&order=-announced_date_first&size=25`
- `https://arxiv.org/search/?searchtype=all&query=INTERMAGNET+OR+%22equatorial+electrojet%22+OR+%22low-latitude+geomagnetic%22&abstracts=show&order=-announced_date_first&size=25`
- `https://arxiv.org/search/?searchtype=all&query=%22Globe+at+Night%22+OR+VIIRS+%22sky+brightness%22&abstracts=show&order=-announced_date_first&size=25`
- `https://arxiv.org/html/2207.03551` and `https://arxiv.org/abs/2207.03551`
- `https://arxiv.org/html/2507.11343` and `https://arxiv.org/abs/2507.11343`
- `https://arxiv.org/html/2510.02977` and `https://arxiv.org/abs/2510.02977`
- `https://arxiv.org/html/2403.00112` and `https://arxiv.org/abs/2403.00112`
- `https://arxiv.org/abs/2405.08279`
- `https://arxiv.org/html/2210.09177` and `https://arxiv.org/abs/2210.09177`
- `https://arxiv.org/html/2403.09847` and `https://arxiv.org/abs/2403.09847`
- `https://arxiv.org/html/2408.06339` and `https://arxiv.org/abs/2408.06339`
- `https://arxiv.org/html/2605.19608` and `https://arxiv.org/abs/2605.19608`
- `https://globeatnight.org/` and `https://globeatnight.org/maps-data/`
- `https://eogdata.mines.edu/products/vnl/`
- `https://intermagnet.org/`, `https://intermagnet.org/data_formats.html`, and `https://intermagnet.org/data_download.html`
- `https://www.scopus.com/sources.uri?search=Monthly+Notices+of+the+Royal+Astronomical+Society`
- `https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=night%20sky%20brightness&ranges=2022_2026_Year`
