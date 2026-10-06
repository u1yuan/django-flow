# Urban gap candidates — 6 October 2026

Review type: scoping. Search window: 2022-01-01 through 2026-10-06. Indexes: OpenAlex and arXiv. These are candidate gaps, not novelty claims. Hydroponics and diesel were not searched. No model was fit. Full-text PDFs were not saved in the repository.

Sources used: arXiv search and download scripts, then DOI redirects and publisher or dataset pages. OpenAlex filter calls are logged below.

## Search log

| Database | Date searched | Query | Filters | Results | Export |
| --- | --- | --- | --- | ---: | --- |
| OpenAlex | 2026-10-06 | `digital divide broadband speed test mapping review` | `publication_year:2022-2026,type:review`, sort cited_by_count desc, per-page 8 | Hung. No output captured. Process stopped. Not an empty result. | none |
| OpenAlex | 2026-10-06 | `digital divide broadband mapping` | `publication_year:2022-2026,type:article`, sort cited_by_count desc, per-page 5 | Hung for about five minutes. Exit 4294967295. No output captured. Not an empty result. | none |
| OpenAlex | 2026-10-06 | `digital divide broadband mapping` (repeat of the article filter) | same article filter | 9452. First five hits were off topic and were not opened: metaverse management, 6G visions, DESI baryon acoustic oscillations, O-RAN, and metaverse tourism. Not used as nearest studies. | not saved in the repository |
| arXiv | 2026-10-06 | `all:digital AND all:divide AND all:broadband AND submittedDate:[202201010000 TO 202610062359]` | relevance, max 8 | 8 | temp JSON only |
| arXiv | 2026-10-06 | `all:health AND all:facility AND all:accessibility AND submittedDate:[202201010000 TO 202610062359]` | relevance, max 8 | 8 | temp JSON only |
| arXiv | 2026-10-06 | `all:Ookla AND all:broadband AND submittedDate:[202201010000 TO 202610062359]` | submitted date desc, max 8 | 0 | empty output |
| arXiv | 2026-10-06 | `all:hotspot AND all:crash AND submittedDate:[202201010000 TO 202610062359]` | relevance, max 8 | 8 | temp JSON only |
| arXiv | 2026-10-06 | `all:accident AND all:hotspot AND submittedDate:[202201010000 TO 202610062359]` | submitted date desc, max 6 | 6 | temp JSON only |
| arXiv | 2026-10-06 | `all:nighttime AND all:lights AND submittedDate:[202201010000 TO 202610062359]` | relevance, max 6 | 6, computer-vision or sleep papers, not LGU radiance | temp JSON only |
| arXiv | 2026-10-06 | `all:VIIRS AND submittedDate:[202201010000 TO 202610062359]` | relevance, max 5 | 5. Not opened. See unverified leads. | temp JSON only |

## Inclusion and exclusion

Included in cards only when the 2022–2026 full text (PDF or HTML) was opened in this run and `https://doi.org/10.48550/arXiv.<id>` returned HTTP 200 to the arXiv abstract page. Preprints are labeled as preprints. An abstract sentence is used only when that sentence was read in the opened file. One quoted sentence per study, and only from opened text.

Excluded from cards: the hung OpenAlex runs; the off-topic OpenAlex repeat; the empty Ookla arXiv query; computer-vision nighttime papers; VIIRS hits that were not opened; publisher DOIs that returned 403; Earth Engine as a data path; scraping as a collection method; hydroponics and diesel.

A nighttime-radiance card was not written. The nighttime-lights query did not return LGU or VIIRS forecasting studies, the VIIRS hits were not opened, and the opened EOG page is a radiance grid rather than an LGU-month file.

## Card 1 — Measured broadband tiles and surveyed access

**Gap statement.** Opened studies of the digital divide measure advertised US plan menus, a New Zealand online panel, digital-skill clusters in three European countries, or a journal review of broadband and the Sustainable Development Goals. They do not compare those designs with a public grid of averaged speed-test results. That comparison is its own study: it asks whether places that look poorly connected in a survey or a plan menu also look poorly connected on a downloadable tile layer. It is not a larger New Zealand panel, not a causal model of intergenerational ties, and not a wider literature review.

**Nearest studies.**

1. Udit Paul, Vinothini Gunasekaran, Jiamo Liu, Tejas N. Narechania, Arpit Gupta, and Elizabeth Belding (2023). *Decoding the Divide: Analyzing Disparities in Broadband Plans Offered by Major US ISPs.* DOI [10.48550/arXiv.2302.14216](https://doi.org/10.48550/arXiv.2302.14216), resolved to https://arxiv.org/abs/2302.14216. Venue: arXiv preprint, cs.NI. Opened: PDF. Locator: section 7 Conclusion. The conclusion says the study analyzes plans from seven major ISPs across thirty US cities, covering 837 thousand street addresses, and that the authors intend to release the tool and dataset. No separate limitation sentence on measured throughput was extracted. No quote.

2. Ogutu B. Osoro and Edward J. Oughton (2024). *The role of broadband connectivity in achieving Sustainable Development Goals (SDGs).* DOI [10.48550/arXiv.2411.09708](https://doi.org/10.48550/arXiv.2411.09708), resolved to https://arxiv.org/abs/2411.09708. Venue: arXiv preprint. Opened: PDF. Locator: closing limitations paragraph. Quote: "Future literature review may benefit from authors in the other languages as well as including reputable peer-reviewed conference papers."

3. Edgar Pacheco (2024). *Exploring Age-Related Patterns in Internet Access: Insights from a Secondary Analysis of New Zealand Survey Data.* DOI [10.48550/arXiv.2310.03252](https://doi.org/10.48550/arXiv.2310.03252), resolved to https://arxiv.org/abs/2310.03252. Venue: *Media Peripheries* 18(1): 38–56, publication date 14 February 2024, as printed in the PDF. The journal site was not opened. Opened: PDF. Locator: Limitations. Quote: "To understand how trends of Internet access change over time, longitudinal evidence is needed."

4. Dalila Failli, Bruno Arpino, and Maria Francesca Marino (2023). *A finite mixture approach for the analysis of digital skills in Bulgaria, Finland and Italy: the role of socio-economic factors.* DOI [10.48550/arXiv.2311.03801](https://doi.org/10.48550/arXiv.2311.03801), resolved to https://arxiv.org/abs/2311.03801. Venue: arXiv preprint, stat.AP. Opened: PDF. Locator: section 5 Conclusion. Quote: "From a substantive point of view, future studies can address the estimation of the causal effect of intergenerational ties on the reduction of the digital divide between older adults and younger individuals."

**Candidate venues.** IEEE Access, recent-issue page https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=6287639, opened HTTP 200. Retrieved text was the title "IEEE Access | IEEE Xplore" only. No 2022–2026 article was visible, so this venue does not pass. IEEE Transactions on Intelligent Transportation Systems, https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=6979, opened HTTP 200, title only, same limit, does not pass. A Scopus source page failed on an expired certificate (see blocked pages). Indexing of comparable 2022–2026 studies was not confirmed.

**Social implication.** Affected population: people with and without modern internet access, the group named in the opened Ookla README. SDG 9, including the broadband target discussed in the opened Osoro and Oughton review. Decision: where a connectivity review should compare measured tile speed with surveyed access. Harm: tiles are about 610.8 meters on a side at the equator, so they are not household identifiers, but a slow tile can still stigmatize a neighborhood. The opened README contains the words Creative Commons, CC BY, and noncommercial; noncommercial use applies. Do not treat a slow tile as proof that an operator failed a legal duty. Do not try to re-identify Speedtest users. The README says measurements with GPS-quality locations are averaged per tile.

**Draft title.** Mapping Measured Broadband Gaps for Urban Residents Using Geographically Weighted Regression. Word count: 11.

**Subdomain.** Statistical modeling.

**Dataset lead.** Ookla global fixed and mobile performance map tiles. Official pages opened: https://github.com/teamookla/ookla-open-data and https://raw.githubusercontent.com/teamookla/ookla-open-data/master/README.md. Unit: zoom level 16 web-mercator tile, about 610.8 meters by 610.8 meters at the equator. Files named in the README: Shapefile and Apache Parquet. The README points to an AWS open-data registry that was not opened, so the download button itself was not seen. Philippine rows: the word Philippines does not appear in the README. Global coverage is stated; Philippine tiles are not confirmed. Noncommercial wording is in the README, as noted above. This is a lead, not a counted analysis file. The dataset was not downloaded.

**Claim boundary.** Associations between tile speed and survey responses are not causes. The study would not assign a legal breach, a clinical label, or a household identity.

## Card 2 — Travel access to published health facilities

**Gap statement.** Opened studies either place or upgrade facilities in Ethiopia, propose accessibility scores and illustrate them with scraped Milan emergency-department pages, or score Maryland hospital access with Alzheimer’s diagnoses, deaths, and bed counts. A separate study scores travel access from an already published facility-point file and a population denominator, and it stops there. It does not decide where to build a facility, it does not scrape appointment pages, and it does not infer who is sick.

**Nearest studies.**

1. Saeed Saleh Namadi, Jie Chen, and Deb Niemeier (2025). *Access to Healthcare for People with Alzheimer’s Disease and Related Dementias.* DOI [10.48550/arXiv.2512.09217](https://doi.org/10.48550/arXiv.2512.09217), resolved to https://arxiv.org/abs/2512.09217. Venue: arXiv preprint. Opened: PDF. Locator: Discussion. Quote: "However, incorporating additional details, such as the presence of specialized ADRD units or the number of ADRD experts in each hospital, could significantly enhance the research."

2. Yohai Trabelsi, Guojun Xiong, Fentabil Getnet, Stephane Verguet, and Milind Tambe (2026). *Health Facility Location in Ethiopia: Leveraging LLMs to Integrate Expert Knowledge into Algorithmic Planning.* DOI [10.48550/arXiv.2601.11479](https://doi.org/10.48550/arXiv.2601.11479), resolved to https://arxiv.org/abs/2601.11479. Venue: arXiv preprint, cs.AI. Opened: HTML. Locator: section 6 Conclusions. The opened conclusion describes an adaptive greedy algorithm inside an LLM refinement loop and an evaluation on three datasets. No future-work sentence was in that conclusion block. No quote.

3. Davin Choo, Yohai Trabelsi, Fentabil Getnet, Samson Warkaye Lamma, Wondesen Nigatu, Kasahun Sime, Lisa Matay, Milind Tambe, and Stephane Verguet (2025). *Optimizing Health Coverage in Ethiopia: A Learning-augmented Approach and Persistent Proportionality Under an Online Budget.* DOI [10.48550/arXiv.2509.00135](https://doi.org/10.48550/arXiv.2509.00135), resolved to https://arxiv.org/abs/2509.00135. Venue: arXiv preprint, cs.AI. Opened: HTML. Locator: problem statement in the opened HTML. The text frames facility-upgrade priority in Ethiopia as submodular maximization under online budget constraints. No separate future-work sentence was extracted. No quote.

4. G. Arbia, V. Nardelli, N. Salvini, and I. Valentini (2024). *New accessibility measures based on unconventional big data sources.* DOI [10.48550/arXiv.2401.13370](https://doi.org/10.48550/arXiv.2401.13370), resolved to https://arxiv.org/abs/2401.13370. Venue: arXiv preprint, econ.EM. Opened: HTML. Locator: opening paragraphs. Quote: "This paper contributes to this strand of literature proposing new accessibility measures that can be continuously feeded by automatic data collection." The same opened passage says the Milan emergency-department illustration was web-scraped. Scraping is not proposed here.

**Candidate venues.** Same IEEE Xplore recent-issue pages as Card 1. Both opened and both showed only the journal title. Neither passes. Scopus indexing was not confirmed.

**Social implication.** Affected population: residents represented by a Philippines OpenStreetMap health-facility extract. SDG 3. Decision: which communities sit farther from a published facility point. Harm: facility coordinates can expose small clinics. Do not attach patient records, do not infer who is sick, and do not label a community with a disease. Do not treat the map as a clinical shortage diagnosis or a staffing order. The Namadi study’s diagnosis and mortality results are not the proposed outcome.

**Draft title.** Measuring Facility Travel Access for Philippine Residents Using Two-Step Floating Catchment Area. Word count: 12.

**Subdomain.** Statistical modeling.

**Dataset lead.** Philippines Health Facilities (OpenStreetMap Export), Humanitarian OpenStreetMap Team, on HDX. Official URL opened: https://data.humdata.org/dataset/hotosm_phl_health_facilities. Unit: facility point. The opened page lists `hotosm_phl_health_facilities_points_shp.zip` (ESRI Shapefile) and `hotosm_phl_health_facilities_points_geojson.zip` (GeoJSON), and a download label of 633.8K. Philippine rows: yes, the extract is the Philippines. The page attributes OpenStreetMap contributors; a full license deed was not in the extracted text. The file was not downloaded.

**Claim boundary.** Distance to a published facility is not a cause of illness and is not a diagnosis. The study would not infer an individual health status, including for a minor, and would not assign a clinical shortage from the map alone.

## Card 3 — Fatal versus all-collision hotspot sets

**Gap statement.** Opened hotspot studies rank or forecast crashes inside Montgomery County, six Wisconsin counties, Dubai, one North Carolina highway segment, or a systemic screen whose transfer depends on local crash and road-inventory files. Alsaleh and colleagues leave other Dubai collision categories and speed or volume variables for later work. A different study holds the geography fixed and asks whether a Getis-Ord Gi* set changes when the same crash table is limited to fatal records rather than all collisions, then reports the overlap of the two sets. That is a sensitivity test of the hotspot definition. It is not a request for more Dubai categories, and it is not a finding of negligence.

**Nearest studies.**

1. Stanislav Liashkov (2025). *Identifying High-Risk Areas for Traffic Collisions in Montgomery, Maryland Using KDE and Spatial Autocorrelation Analysis.* DOI [10.48550/arXiv.2506.21930](https://doi.org/10.48550/arXiv.2506.21930), resolved to https://arxiv.org/abs/2506.21930. Venue: arXiv preprint, stat.AP. Opened: HTML. Locator: section 6 Limitations. Quote: "Initial reports may include details that have not been corroborated through further investigation, potentially leading to inaccuracies."

2. Jingwen Zhu, Keshu Wu, Pei Li, Steven T. Parker, Bin Ran, and David A. Noyce (2026). *Forecasting the Emergence and Evolution of Crash Hotspots: A Unified Deep Learning Framework for Proactive Traffic Safety.* DOI [10.48550/arXiv.2607.24168](https://doi.org/10.48550/arXiv.2607.24168), resolved to https://arxiv.org/abs/2607.24168. Venue: arXiv preprint. Opened: HTML. Locator: section 5 Conclusion. Quote: "Forecast and tracking fidelity fall in very sparse regimes, where weak signals make birth detection and phase transitions less reliable, and marginal clusters can oscillate between growth and decline without added temporal smoothing."

3. Nael Alsaleh, Noura Falis, Tareq Alsaleh, and Farah Ba Fakih (2026). *Traffic Collisions: Temporal Patterns and Severity-Weighted Hotspot Analysis.* DOI [10.48550/arXiv.2601.12548](https://doi.org/10.48550/arXiv.2601.12548), resolved to https://arxiv.org/abs/2601.12548. Venue: arXiv preprint. Opened: HTML. Locator: section 5 Conclusion. Quote: "Future research should extend this framework to additional collision categories, such as vehicle–vehicle, rollover, bicycle, and animal-related accidents, to support a more comprehensive, data-driven approach to traffic safety planning in Dubai."

4. Jennifer Sawyer and Julian Allagan (2025). *Statistical and Machine Learning Analysis of Traffic Accidents on US 158 in Currituck County: A Comparison with HSM Predictions.* DOI [10.48550/arXiv.2512.22302](https://doi.org/10.48550/arXiv.2512.22302), resolved to https://arxiv.org/abs/2512.22302. Venue: arXiv preprint. Opened: HTML. Locator: section V Conclusion. Quote: "Future research should focus on addressing these limitations through enhanced data collection, advanced feature engineering, and ensemble modeling approaches that combine the transparency of machine learning with the theoretical foundation of traditional safety performance functions."

5. Shriyan Reyya and Yao Cheng (2024). *ROADFIRST: A Comprehensive Enhancement of the Systemic Approach to Safety for Improved Risk Factor Identification and Evaluation.* DOI [10.48550/arXiv.2411.00821](https://doi.org/10.48550/arXiv.2411.00821), resolved to https://arxiv.org/abs/2411.00821. Venue: arXiv preprint. Opened: HTML. Locator: section VI Conclusions. Quote: "Despite the innovative nature and verified effectiveness of the proposed system, it should be noted the transferability of the developed system depends on a range of factors, including crash data quality, coverage of road inventory data, crash density, and the significance of the selected contributing factors."

**Candidate venues.** Same two IEEE Xplore recent-issue pages as Card 1. Both opened, both title-only, neither passes. Scopus indexing was not confirmed.

**Social implication.** Affected population: road users in the city or county whose crash file is used. SDG 3.6, the traffic-death target named in the opened Alsaleh paper. Decision: whether a fatal-only hotspot list and an all-collision hotspot list would change which sites are reviewed. Harm: precise coordinates can identify a household or a victim. A hotspot label can stigmatize a neighborhood. Do not use the map as evidence of negligence or fault. Do not publish identifiable crash points.

**Draft title.** Comparing Fatal and All-Crash Hotspots for Road Users Using Getis-Ord Gi*. Word count: 11.

**Subdomain.** Statistical modeling.

**Dataset lead.** No Philippine, multi-country, or global crash-record file was opened with a documented unit. The UK page https://www.data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-safety-data opened HTTP 200, and the visible title was "Road Safety Data - National Data Library". The extracted body was a cookie notice, so unit, license, and Philippine rows were not documented. It does not pass. Montgomery County and Dubai Pulse are named inside opened papers; those portal pages were not opened, and both are single jurisdictions. No public MMDA file was opened, and MMDA was not contacted. This card has no passing dataset lead.

**Claim boundary.** Overlap of two hotspot sets is not a cause of crashes and is not a legal finding. The study would not label a driver, a child, or a crash as a crime.

## Unverified leads

- Renteng Yuan, Qiaojun Xiang, Zhiheng Fang, and Xin Gu, arXiv:2303.12160, journal DOI 10.1080/19427867.2023.2262201. The publisher DOI page returned HTTP 403. The arXiv PDF was downloaded, but the journal DOI was not resolved, so the study is not in a card.
- Tuheen Ahmmed, Afsoon Alidadi, Zichao Zhang, Aizaz U. Chaudhry, and Halim Yanikomeroglu, arXiv:2203.08933. The record’s DOI 10.13140/RG.2.2.18223.20648 returned HTTP 403. The PDF was opened. The arXiv DOI was not in the DOI-resolution batch, so the study is not in a card.
- VIIRS arXiv hits, not opened: 2305.11910 (fuel moisture), 2503.08580 (wildfire predictability), 2603.16385 (DMSP-to-VIIRS nighttime-light calibration), 2510.26816 (VIIRS active fire), 2508.00590 (VIIRS-like nighttime light reconstruction, 1986–2024). Titles only. No radiance card.
- EOG VIIRS nighttime lights, https://eogdata.mines.edu/products/vnl/, opened. The page offers tiled and non-tiled downloads and says many of the data are under Creative Commons Attribution 4.0. Unit on the page is a radiance grid, not an LGU-month. No nearest LGU study was opened.
- Relative Wealth Index, https://data.humdata.org/dataset/relative-wealth-index, opened. Only the title rendered. Unit and Philippine rows were not visible.
- Google Open Buildings, https://sites.research.google/open-buildings/, redirected to https://sites.research.google/gr/open-buildings/. The page describes building polygon and point CSVs, a map download, a Colab country download, gsutil, and Earth Engine. Earth Engine is out. Philippines was not named in the extracted text.
- Ookla AWS registry URL appears in the opened README and was not opened.

## Blocked pages

- OpenAlex review filter: hung, no HTTP status, no output.
- OpenAlex article filter: hung about five minutes, exit 4294967295, no output.
- https://doi.org/10.1080/19427867.2023.2262201 — HTTP 403.
- https://doi.org/10.13140/RG.2.2.18223.20648 — HTTP 403.
- https://data.humdata.org/dataset/hotosm_health_facilities — HTTP 404.
- https://data.humdata.org/dataset/healthsites — HTTP 404.
- https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars — HTTP 403.
- https://ieeeaccess.ieee.org/ — certificate verification failed (expired certificate).
- https://www.scopus.com/sourceid/21100374601 — certificate verification failed (expired certificate).
