# Literature Review: Astronomical analytics title screen

Generated: 6 October 2026
Review type: scoping
Search window: 2021–2026, plus essential earlier product, atlas, and dataset papers
Databases and official pages: Crossref REST API; arXiv API; Europe PMC full text for one article; Earth Observation Group (EOG) VIIRS Nighttime Lights product page and license PDF; SDGSAT-1 Open Science Program page; Zenodo record 4002935; DENR-BMB Protected Area Information System (PAIS); Protected Planet legal terms; Geoportal Philippines homepage

This file screens three working titles and three handoff titles. It is not a completed dataset audit, a model run, or a title approval. Search snippets were not treated as evidence. An abstract is labeled abstract-only and supports only what it states. A Crossref title without an opened abstract or full text is a lead.

User-Agent on API and page requests: `thesis1-litreview/1.0 (https://github.com/u1yuan/django-flow)`.

No VIIRS raster, HiRISE image zip, or protected-area boundary file was downloaded.

## Research question

For a Philippine undergraduate CS Data Science thesis, which astronomical-analytics titles are supportable when the priority outcomes are access to visible stars and local-government lighting decisions? Satellite upward radiance, ground-observed sky brightness, ecological effects, and tourism benefits stay separate outcomes. VIIRS radiance is not treated here as measured visible sky brightness, multispectral skyglow, or ecological disruption.

Technical frame:

- Domain: Philippine nighttime lights and night-sky access.
- Techniques named in the working titles: XGBoost; XGBoost with satellite–ground observations; NSGA-II.
- Comparison: persistence or linear trend for radiance; held-out ground sites for sky brightness; expert-validated site criteria for prioritization.
- Evaluation: usable-record audit, held-out places or years, and a baseline. No model was fit in this screen.

## Search strategy

Scoping protocol, set before collection on 6 October 2026:

- Indexes: Crossref `https://api.crossref.org/works` and arXiv `https://export.arxiv.org/api/query`. Semantic Scholar Graph API was attempted and returned HTTP 429 for every query, so it contributed no records.
- OpenAlex CLI was not used.
- Dates: `from-pub-date:2021-01-01` where a filter was applied; undated or earlier queries were used for product papers, the world atlas, Sky Quality Meter (SQM) methods, and the HiRISE label set.
- Language: English records returned by the APIs. The SDGSAT page also contains a Chinese parallel text; quotations below are from the English strings in the official page bundle.
- Publication types: journal articles, preprints, datasets, and official data-rights pages.
- Screening: title, then abstract or official page, then full text when a public HTML or PMC XML copy opened. Crossref relevance totals are bag-of-words totals. Only the top-ranked records were screened. This is not a systematic review of every hit.
- Full text that did not open: MDPI HTML returned HTTP 403. Several Elsevier and Nature abstracts were absent from Crossref. Those items stay title-level leads.

## Inclusion and exclusion criteria

Included when the record did at least one of the following:

- Defined the VIIRS nighttime-light product, its units, or its rights.
- Separated upward radiance, zenith or SQM sky brightness, ecological response, or tourism.
- Reported Philippine nighttime-light or artificial-light-at-night work, or was the nearest opened method paper for forecasting, sky-brightness estimation, or dark-sky site selection.
- Stated access conditions for SDGSAT-1, NIPAS/PAIS, WDPA/WDPCA, or the HiRISE label set.
- Tested astronomical or Martian image classification in a way that bears on the parked handoff titles.

Excluded at title or abstract screen:

- Wrong outcome: rice night temperature, occupational health, Alzheimer’s disease, sleep-stage contrastive learning, plant-disease transfer-learning reviews, and generic XGBoost sales or medical papers.
- Wrong place treated as if it were Philippine coverage: Hong Kong, Granada, Texas, and the Guangdong–Hong Kong–Macao Greater Bay Area were kept only as method comparisons and were not counted as Philippine ground samples.
- Hydroponics, diesel genset anomalies, and Native Trees were not searched.

Duplicate handling: DOI first, then arXiv identifier, then title. The arXiv record `2007.01150` carries publisher DOI `10.1016/j.jenvman.2019.06.128`; the journal PDF was not opened separately. Aksaker’s correction DOI `10.1186/s40645-026-00802-1` was not treated as a second study. One duplicate pair was collapsed.

## Word counts

Whitespace tokens. A hyphenated token counts as one word. All six titles are within the 16-word cap. The three working titles each name a technique.

| Title | Words | Technique token |
| --- | ---: | --- |
| Forecasting Philippine LGU Nighttime-Light Growth Using XGBoost for Dark-Sky Planning | 10 | XGBoost |
| Estimating Philippine Night-Sky Brightness Using XGBoost and Satellite–Ground Observations | 9 | XGBoost |
| Prioritizing Philippine Dark-Sky Conservation Sites Using NSGA-II and Nighttime-Light Trends | 10 | NSGA-II |
| Quantifying Light Pollution Dynamics and Ecological Disruption Using Multi-Spectral Nighttime Satellite Imagery | 12 | none named; “Multi-Spectral” is a sensor description |
| Cross-Domain Deep Learning: Adapting Astronomical Source-Detection Algorithms for Terrestrial Satellite Feature Extraction | 12 | Deep Learning; source-detection algorithms, unnamed |
| Unsupervised Contrastive Learning for Classifying Martian and Terrestrial Surface Features: A Satellite Topology Study | 14 | Unsupervised Contrastive Learning |

`Satellite–Ground` is one whitespace token. `Learning:` and `Features:` keep the colon inside the token.

## Record-count arithmetic used in this screen

The plan’s LGU arithmetic is a design, not an extract. 1,493 municipalities + 149 cities = 1,642 local government units (LGUs). 1,642 × 12 = 19,704 potential LGU-month rows in one year. That figure is not a count of verified valid observations, cloud-free months, or independent places. No VIIRS extract was built here. Stacking years would repeat the same places. EOG states that monthly coverage fails in many tropical areas because of cloud, so a zero in the average-radiance grid is not evidence that no lights were observed.

The eNIPAS protected-area count opened on PAIS is 248 areas, not 10,000 independent sites.

The HiRISE label set contains 64,947 images formed from 10,815 original landmarks drawn from 232 source images. The augmented copies are not independent records.

## Evidence summary

Strongest opened distinction: VIIRS Day/Night Band products are cloud-screened upward radiance in nanowatts per square centimeter per steradian. Zenith artificial night-sky brightness is a different quantity. Falchi and colleagues model it from VIIRS DNB inputs and calibrate it with a large ground set. Bará and colleagues show that SQM-band sky brightness and VIIRS-DNB top-of-atmosphere radiance can move in opposite directions when lighting spectra change. Aksaker and colleagues map dark-sky places with VIIRS radiance and, for visualization, convert that radiance with a log equation. That conversion is not a Philippine held-out ground test.

Philippine nighttime-light papers opened at abstract level use VIIRS as an economic proxy. They do not estimate visible-star access.

No opened source counts comparable Philippine ground sky-brightness sites. The 2016 world atlas has a Philippines row of modeled percentages. Those percentages are not a ground-site inventory.

Dark-sky site selection opened at abstract level uses expert and multi-criteria methods in the Greater Bay Area, and a random-forest title exists for global site selection. No opened study applies NSGA-II to Philippine dark-sky sites. PAIS states 248 protected areas under eNIPAS and does not publish a shapefile-download license on the pages opened. Protected Planet forbids commercial use of WDPCA materials and derivative works without written permission, and forbids redistribution.

SDGSAT-1 data on the official Open Science Program page require an approved proposal, a user agreement, and scientific-research use. The program text does not supply paired Philippine ecological measurements.

## Thematic synthesis

### Upward radiance is the VIIRS measurement

EOG’s monthly product is a cloud-free Day/Night Band composite. The average-radiance field is `avg_rade9h`, in nW/cm²/sr, at 15 arc seconds, EPSG:4326. The page warns that tropical cloud cover leaves months without good coverage and that users must consult the cloud-free-observations file. Elvidge and colleagues describe annual V.2 grids built from monthly cloud-free radiance averages, with background zeroing that depends on how many cloud-free observations exist. They present the series as suitable for change detection of radiance, not as a sky-brightness product.

Rights opened in the EOG license PDF: many EOG datasets, including VIIRS nighttime lights (VNL), are under Creative Commons Attribution 4.0. The PDF says users may copy, modify, and distribute for any purpose, including commercial use, with attribution and a statement of changes. Reports should cite the listed VNL papers. That license does not convert radiance into sky brightness, ecology, or tourism demand.

Bustamante-Calabria and colleagues, writing about Granada, state that VIIRS/DNB acquires data late at night after much nocturnal lighting has already been switched off. A Philippine LGU forecast of monthly radiance would be a forecast of that late-night upward signal.

### Sky brightness is modeled or measured on the ground

Falchi and colleagues (2016) present an atlas of zenith artificial night-sky brightness “modelled with VIIRS DNB data and calibrated with more than 35,000 observations.” The opened text does not say how many of those observations are in the Philippines. The country table reports modeled percentages of population and area under brightness thresholds. For the Philippines row the population percentages are 8.7, 91.3, 67.2, 47.6, 26.5, and 7.2, and the area percentages are 35.6, 64.4, 20.9, 6.1, 0.7, and 0.1, under the successive thresholds ≤1.7, >1.7, >14, >87, >688, and >3000 μcd/m². Those are atlas outputs from the 2016 paper, not 2021–2026 ground campaigns and not LGU-month counts.

Bará, Rigueiro, and Lima show in a single-scattering model that visual, scotopic, SQM-band, and VIIRS-DNB indicators can trend differently, including in opposite directions, when lamps change spectrum and angular pattern. An XGBoost model that learns VIIRS radiance therefore has not, on this evidence, learned SQM sky brightness.

Aksaker and colleagues analyze VIIRS composite trends at 216 International Dark-Sky Places. The opened article HTML says the map radiation unit is nW cm⁻² sr⁻¹, and that they convert it for visualization with SQM = 20.0 − 1.9 × log(AL), citing earlier work. A string search of that HTML found no “Philippine.” Their machine-learning sentence is about decision-tree, random-forest, and gradient-boosting regression on that global IDSP set. It is not an XGBoost forecast for Philippine LGUs, and it is not a result computed in this screen.

So, Pun, and Liu describe a decade of SQM photometry in Hong Kong and state that the in-situ sampling has a temporal resolution satellites do not provide. The abstract is about Hong Kong.

No Globe at Night or SQM catalog with a Philippine site count was opened.

### Ecology and tourism are different claims

Baquiran and colleagues, with a University of the Philippines Marine Science Institute affiliation on the Crossref record, report a short-term artificial-light experiment on the microbiome of *Acropora digitifera*. The abstract says exposure had no large-scale effect on the community, with some taxa enriched. The abstract does not use satellite imagery and does not state a field-site country in the text that was read. It does not measure nationwide ecological disruption.

Fan and colleagues’ abstract frames light pollution as a source of ecological degradation, then describes a suitability study: Delphi consultation, GIS, and multi-criteria decision-making in the Greater Bay Area, using nighttime light levels plus weather, air quality, population, transport, and tourism infrastructure. The abstract’s findings mention ecotourism potential and nighttime tourism for that region. That is a planning interpretation in another country, not a Philippine visitor census and not an NSGA-II result.

SDGSAT-1 glimmer papers located by title (Wu and colleagues 2025; Jia and colleagues 2024) concern light-pollution identification or coastal light-type classification. Their abstracts were not in Crossref and the full texts were not opened, so they are not evidence of an ecological response variable.

### Philippine nighttime lights already proxy economic activity

Pagaduan’s abstract reports that VIIRS nighttime lights predict urban subnational GDP in the Philippines better than rural activity, and that cropland productivity improves the rural proxy. The outcome is economic activity. Ramel, Legaspi, and Pajaron’s 2026 title is about nighttime lights and land values in the Philippines; Crossref had no abstract, and the paper was not opened. These studies are the nearest opened Philippine VIIRS literature. They leave a lighting-decision question only if the outcome is restated as radiance, and they do not establish a dark-sky or visible-star result.

### Site prioritization, boundaries, and NSGA-II

PAIS states that the eNIPAS Act of 2018 brings the total number of protected areas to 248, previously 240 under the NIPAS law. The about page defines protected areas and lists categories, including protected landscapes and seascapes with recreation and tourism opportunities, and it lists recognition of local communities and Indigenous Peoples among the law’s features. It does not offer a public polygon license. `https://pais.bmb.gov.ph/downloads` and `https://pais.bmb.gov.ph/map` returned HTTP 404. The contact page gives institutional routes (DENR Central Office and BMB in Quezon City). `https://www.bmb.gov.ph/` returned HTTP 403 behind a Cloudflare challenge and was not read. Geoportal Philippines’ homepage opened as a map application and contained no boundary-license text.

Protected Planet’s legal page, opened 6 October 2026, governs World Database on Protected and Conserved Areas (WDPCA) materials. It says neither the materials nor derivative works may be put to commercial use without prior written permission of UNEP-WCMC, and that the data may not be sublicensed or redistributed. Publication is allowed when the data are not downloadable and attribution is visible. Noncommercial thesis use is not the same as a permission to derive and republish boundary files.

Fan and colleagues already combine expert judgment with spatial criteria for dark-sky-park suitability outside the Philippines. Li and colleagues’ 2026 *Remote Sensing of Environment* title states a random-forest model for global dark-sky quality and potential park sites; the abstract was not deposited and the PDF was not opened. A Crossref query for “NSGA-II dark sky park” did not rank an NSGA-II dark-sky paper in the first five items. The NSGA-II siting abstract that did surface in an earlier query is about highway weather stations (Li, SSRN), which is a different decision.

A 248-area decision set does not meet a 10,000-independent-site rule. Filling the record count with VIIRS pixel-times would count correlated radiance cells, not independent candidate sites.

### Handoff methods that do not become Philippine Earth-observation theses on the opened evidence

Wagstaff and colleagues started from AlexNet trained on Earth images and used transfer learning for Mars rover and orbital images in the PDS Imaging Atlas. That is Earth-to-Mars adaptation of a classifier, not adaptation of an astronomical source-detection code to Philippine satellite features, and the abstract describes supervised deployment rather than an unsupervised contrastive study.

The Zenodo HiRISE set version 3.2 is CC BY 4.0. Its classes, as described on the record, are Martian: bright dune, dark dune, crater, slope streak, impact ejecta, spiders, Swiss cheese, and other. It does not supply Philippine landform labels. Grouping by the 232 source images, or at least by the 10,815 original landmarks, is required before any split. The image zip files were not downloaded.

Biswas and Tešić’s Crossref title is domain adaptation with contrastive learning for object detection in satellite imagery (*IEEE Transactions on Geoscience and Remote Sensing*, 2024). No abstract was deposited and the PDF was not opened, so the title is a lead that terrestrial satellite domain adaptation already exists. It does not document an astronomical source extractor, a Philippine label set, or an open high-resolution target collection.

## Gaps and limitations

For each gap below, “nearest opened study” is a study whose abstract or full text was actually opened, unless the row says the nearest item is title metadata only. An unsearched absence is not called novel.

| Gap | Nearest opened study | Proposed difference | Evidence still needed |
| --- | --- | --- | --- |
| LGU-month forecast of Philippine upward radiance for lighting review | Pagaduan 2022 abstract uses Philippine VIIRS for urban GDP. Aksaker 2026 HTML uses VIIRS trends and gradient boosting at 216 global dark-sky places, with no Philippine match in the opened text. | Predict LGU-month radiance with XGBoost against persistence and a linear trend, for a lighting-review list, with the outcome named as radiance. | A real extract: LGU geometry rights, cloud-free counts, missing months, and eligible rows after those exclusions. A lighting decision the radiance trend can inform. |
| Philippine night-sky brightness from satellite and ground data | Falchi 2016 models zenith brightness from VIIRS and calibrates with more than 35,000 observations, without a Philippine subset count in the opened passages. So 2026 abstract is a Hong Kong SQM series. Bará arXiv abstract shows VIIRS and SQM-band indicators can diverge. | Held-out Philippine sites and a model that predicts a stated ground instrument, not radiance relabeled as sky brightness. | An opened inventory of comparable Philippine ground observations, instrument, units, and site count large enough for held-out sites. |
| NSGA-II ranking of Philippine dark-sky conservation sites | Fan 2025 abstract: Delphi, GIS, and multi-criteria suitability in the Greater Bay Area. Li 2026 is title-only for random-forest global site selection. PAIS: 248 eNIPAS areas and no download license on the pages opened. | A Philippine ranking whose objectives were set by named experts and checked in the field. | Written boundary permission, expert-validated criteria, field checks, and a record unit that survives correlation and the 10,000-record rule. Tourism demand was not opened. |
| Multispectral imagery as ecological disruption | SDGSAT-1 program text: approved research use, not an ecological dataset. Baquiran 2020 abstract: short-term coral-microbiome response to artificial light, not satellite multispectral mapping. Wu 2025 and Jia 2024 are title leads on glimmer imagery. | Paired Philippine glimmer scenes and an ecological measurement defined separately from radiance. | Approved SDGSAT-1 scenes, the user agreement, and ecological observations. Not established here. |
| Astronomical source detection transferred to Philippine land features | Wagstaff 2018 abstract transfers an Earth-trained network to Mars. Biswas 2024 is a title lead on terrestrial satellite domain adaptation. | A named Philippine target, open imagery, 10,000 eligible labels, a terrestrial-only baseline, and a beneficiary. | All four of those items. The handoff’s WorldView/Planet target was not opened as an open collection. |
| Unsupervised contrastive classification of Martian and terrestrial surfaces | Zenodo 4002935 describes labeled, augmented HiRISE landmarks and Martian classes. Wagstaff 2018 is supervised CNN classification. | Matched Philippine landform classes, independent labels, and a local adopter. | Those labels and an adopter. The opened label set does not provide them. |

Limitations of this screen:

- Semantic Scholar was blocked by HTTP 429. The second index that returned records is arXiv.
- Crossref totals are not counts of relevant papers. Screening used the top of each result list.
- MDPI full text was blocked. Elvidge 2021, Fan 2025, So 2026, and Baquiran 2020 are abstract-only even when the abstract is detailed.
- Elsevier items without a Crossref abstract were not read (Li 2026; Wu 2025; Jia 2024; Jackson 2025; Kocifaj 2023; Barentine 2022).
- The SDGSAT user agreement itself was not opened. The program page says a detailed agreement is signed after approval.
- PSA’s municipality and city counts were not re-counted. The 1,642 and 19,704 figures remain the brief’s arithmetic.
- No organization was contacted. Listing a bureau is not evidence of interest or data access.

## Title cards

### 1. Forecasting Philippine LGU Nighttime-Light Growth Using XGBoost for Dark-Sky Planning

- Question: Can monthly VIIRS upward radiance, aggregated to Philippine LGUs, be forecast with XGBoost so that a local government can review lighting growth?
- Technique: XGBoost. The title has 10 words.
- Beneficiary: A city or municipal environment office reviewing outdoor-lighting growth. The plan names candidate offices; this screen did not confirm interest. PhilSA is a plausible technical reviewer of radiance processing, not of visible-star access.
- Data source and rights: EOG monthly cloud-free DNB composites and the annual VNL series derived from them. The license PDF places VNL under CC BY 4.0, including commercial use, with attribution and a change notice. LGU boundaries were not licensed in this screen. Geoportal Philippines’ homepage had no such text. NAMRIA terms were not opened.
- Record-count gate: Unmet. 19,704 is the potential LGU-month count for one year of 1,642 LGUs. It is not a verified valid-observation count. Tropical cloud gaps mean some months lack good coverage. Rows for the same LGU are repeated months, not independent places. Gate status: conditional on an extract that reports eligible LGU-months after cloud, geometry, and missingness rules.
- Baseline and validation: Not run. A defensible design, if the outcome stays radiance, is previous-year same-month persistence and a linear trend, with whole provinces or years held out. Reporting XGBoost skill on unanalyzed pixels is not available from this screen. Aksaker’s reported R² above 0.6 is their gradient-boosting result on global dark-sky places, not a Philippine XGBoost score.
- Nearest prior art: Pagaduan 2022 (Philippine VIIRS as an urban GDP proxy; abstract-only). Aksaker 2026 (VIIRS trends at existing International Dark-Sky Places; verified HTML). Elvidge 2021 (radiance change-detection series; abstract-only). Bará arXiv:1909.10909 (VIIRS radiance and SQM brightness can diverge; abstract-only).
- Social implication: A radiance-growth list could help an LGU see where late-night upward light is increasing. It does not by itself show whether people can see more stars, whether wildlife is affected, or whether a tourism product exists.
- Adoption value: Only after the outcome is named as upward radiance and the missing-month audit exists. A “dark-sky planning” label overclaims the measurement.
- Ethics: CC BY attribution is required. Do not describe a dark community as losing starlight because its radiance rose. Do not join unpublished boundary files. No personal contacts were collected.
- Three-trimester feasibility: Reading the product and building a provincial pilot is plausible. A national LGU-month model is not feasible until geometry rights and cloud-free counts are audited. That audit is the first trimester’s gate, not a modeling task.
- Gate: **Revise.** Keep XGBoost and LGU radiance. Remove visible-star and dark-sky claims from the outcome. A 7-word revision that names the technique is “Forecasting Philippine LGU Nighttime-Radiance Growth Using XGBoost.” Proceed only after the record-count extract. Decisive sources: EOG monthly-composite page and license PDF, together with Bará’s arXiv abstract that VIIRS-DNB radiance and SQM-band brightness are different indicators.

### 2. Estimating Philippine Night-Sky Brightness Using XGBoost and Satellite–Ground Observations

- Question: Can XGBoost, trained on satellite radiance and Philippine ground observations, estimate night-sky brightness at held-out Philippine sites?
- Technique: XGBoost. The title has 9 words. `Satellite–Ground` is one word.
- Beneficiary: An observing-site or environment office that needs a sky-brightness estimate. PAGASA’s astronomy section is named in the plan as a method reviewer. Instrument records were not opened.
- Data source and rights: VIIRS radiance can be used under the EOG CC BY 4.0 terms above. Ground labels do not exist in any file opened here. Falchi’s atlas is a 2016 model product with its own article license; it is not a substitute for new Philippine photometry. Aksaker’s log conversion is a visualization equation inside a 2026 paper, not a data license for Philippine SQM values.
- Record-count gate: Unmet. Global calibration counts do not establish Philippine coverage. The opened Falchi passages do not state a Philippine observation count. Hong Kong’s SQM series is not a Philippine series. Held-out sites require more than one Philippine site with comparable instruments. Gate status: stop until that inventory is opened and counted.
- Baseline and validation: Not run. The minimum design is a published conversion equation, such as the one Aksaker applies for display, versus XGBoost, scored only on held-out Philippine sites. Without those sites the comparison cannot be computed.
- Nearest prior art: Falchi 2016 (verified PMC text: modeled zenith brightness from VIIRS, calibrated with more than 35,000 observations). Bará arXiv:1909.10909 (abstract-only: indicators can move oppositely). Bustamante-Calabria arXiv:2011.09252 (abstract-only: ground and satellite comparison in Granada, and VIIRS observes late at night). So 2026 (abstract-only: Hong Kong SQM). Aksaker 2026 (verified HTML: radiance-to-SQM display conversion).
- Social implication: Visible-star access is the outcome this title names. The opened literature does not show that a radiance model delivers that outcome in the Philippines.
- Adoption value: None until local ground sites exist. A national map produced from a foreign conversion equation would repeat a known model risk rather than test Philippine accuracy.
- Ethics: Do not present citizen-science totals from other countries as Philippine coverage. Do not collect observer identities. A sky-brightness map can affect lighting enforcement and should not be issued from radiance alone.
- Three-trimester feasibility: Not feasible as stated. Building a new national photometer network is field infrastructure, not a three-trimester CS analysis of data already public. Using only the 2016 atlas would study a model, not new Philippine ground truth.
- Gate: **Stop.** Decisive sources: Falchi 2016 PMC text, which separates modeled sky brightness from VIIRS inputs and does not give a Philippine ground-site count, and So 2026’s abstract, which is a Hong Kong SQM program. Aksaker’s conversion equation does not replace held-out Philippine sites.

### 3. Prioritizing Philippine Dark-Sky Conservation Sites Using NSGA-II and Nighttime-Light Trends

- Question: Can NSGA-II rank Philippine conservation sites for dark-sky protection using nighttime-light trends and expert criteria?
- Technique: NSGA-II. The title has 10 words.
- Beneficiary: DENR-BMB is the agency PAIS describes as managing protected-area information. The plan also names tourism and astronomy reviewers. None has confirmed a dark-sky ranking role in a source opened here.
- Data source and rights: VIIRS trends can be computed from EOG CC BY 4.0 radiance if the outcome stays radiance. Protected-area polygons are not cleared. PAIS published no download license on the about or contact pages, and the downloads path 404ed. WDPCA terms require written permission for commercial use of the materials and of derivative works, and they forbid redistribution. A thesis map that lets readers download boundaries would conflict with that redistribution clause unless UNEP-WCMC or the Philippine data holder permits it.
- Record-count gate: Unmet for sites. PAIS states 248 protected areas under eNIPAS. That is the opened decision-unit count. It is far below 10,000 independent sites. VIIRS cells inside those areas would be correlated observations of radiance, not 10,000 places. Gate status: stop on the site unit.
- Baseline and validation: Not run. Fan and colleagues already use expert consultation and multi-criteria scoring. A new optimizer needs those criteria first, then a comparison with a simple weighted sum, then field checks on held-out sites. NSGA-II without a validated objective function does not create a conservation result.
- Nearest prior art: Fan 2025 abstract (Delphi, GIS, multi-criteria dark-sky-park suitability in the Greater Bay Area, including a tourism-infrastructure criterion). Aksaker 2026 (trends at places already designated, not a Philippine search for new sites). Li 2026 title only (random forest for global dark-sky park siting). Li SSRN abstract (NSGA-II for highway weather stations, a different siting problem).
- Social implication: Protected areas already have communities, Indigenous Peoples, and management boards in the PAIS description of eNIPAS. A rank list that ignores those arrangements can misdirect attention. Tourism benefit is a separate, unopened outcome. Fan’s abstract discusses ecotourism in the Greater Bay Area, which is not Philippine demand.
- Adoption value: Low until BMB or a protected-area office confirms the decision, the criteria, and the boundary terms. A radiance layer alone does not prioritize a conservation site.
- Ethics: No boundary file was downloaded. Do not treat WDPA derivatives as freely republishable. Do not score Indigenous or community land as an optimization surface from satellite radiance. Expert criteria and field checks are still required and were not opened.
- Three-trimester feasibility: Not feasible as a site-ranking thesis. Permission, criteria, and field checks are external gates. The 248-area count does not satisfy the record rule by site.
- Gate: **Stop.** Decisive sources: PAIS about page (248 eNIPAS areas and no download offer) and the Protected Planet legal page (derivative works and commercial use need written permission; no redistribution). Fan 2025 shows expert multi-criteria siting already published for another region, and it is not NSGA-II.

## Handoff dispositions

### Quantifying Light Pollution Dynamics and Ecological Disruption Using Multi-Spectral Nighttime Satellite Imagery

Disposition: **Conditional extension only. Do not activate.** Twelve words. The title does not name an algorithm.

Opened sources that keep the condition in place:

- EOG and Elvidge 2021: VIIRS DNB products are radiance composites, not a multispectral skyglow product.
- SDGSAT-1 Open Science Program page: free access follows proposal approval; the research period should not exceed 24 months; data “can only be used for scientific research”; global and intercontinental requests are not supported; investigators sign a detailed user agreement. The agreement PDF was not opened.
- Baquiran 2020 abstract: a short-term organism-level artificial-light result, not a satellite ecological map.
- Wu 2025 and Jia 2024: title leads on SDGSAT-1 glimmer and light type or residential light pollution. Full texts were not opened, so they are not ecological-disruption evidence.

The opened record does not change the handoff into an active title. Paired Philippine imagery and a separately measured ecological outcome are still absent.

### Cross-Domain Deep Learning: Adapting Astronomical Source-Detection Algorithms for Terrestrial Satellite Feature Extraction

Disposition: **Park.** Twelve words. The opened evidence does not change the reason.

Wagstaff 2018’s abstract adapts an Earth-image network to Mars imagery. That is the reverse direction from the title, and it is supervised classification for a NASA archive rather than a Philippine beneficiary. Biswas and Tešić 2024’s title indicates contrastive domain adaptation for satellite object detection; the paper was not opened, so it cannot be claimed as a finished terrestrial baseline. No Philippine label set of 10,000 eligible records was opened. The handoff’s WorldView/Planet target was not opened as an open dataset. The park stands.

### Unsupervised Contrastive Learning for Classifying Martian and Terrestrial Surface Features: A Satellite Topology Study

Disposition: **Park.** Fourteen words. The opened HiRISE record strengthens the original reason rather than removing it.

Zenodo `10.5281/zenodo.4002935` (version 3.2, published 16 September 2020, creators Gary Doran, Emily Dunkel, Steven Lu, and Kiri Wagstaff, Jet Propulsion Laboratory, license CC BY 4.0) states 64,947 landmark images from 10,815 original landmarks and 232 source images. Of the originals, 9,022 were augmented by three rotations, horizontal flip, vertical flip, and random brightness adjustment; 1,793 were not augmented. Classes described on the record are Martian landforms, and “other” is a catch-all that “makes up the majority of our data set.” A random split of the 64,947 files would leak the 232 source images. Wagstaff 2018 is a supervised CNN paper, not an unsupervised contrastive Mars–Earth study. No Philippine landform labels or local adopter were opened. The park stands.

## Claim-level evidence ledger

Status values: verified-passage, abstract-only, lead, excluded.

| ID | Claim or question | Metadata | DOI or URL | Locator | Status | Caveat |
| --- | --- | --- | --- | --- | --- | --- |
| EOG-VNL | Monthly VIIRS composites are cloud-free DNB radiance. Tropical cloud cover blocks good monthly coverage. A zero in the average-radiance image does not mean no lights were observed. | Earth Observation Group, Payne Institute, Colorado School of Mines. Product page retrieved 6 October 2026. | https://eogdata.mines.edu/products/vnl/ | Section “Monthly Cloud-free DNB Composite.” Quote: “it is imperative that users of these data utilize the cloud-free observations file and not assume a value of zero in the average radiance image means that no lights were observed.” Unit line: “Unit (avg_rade9h) nW/cm 2 /sr.” Resolution “15 arc second.” | verified-passage | Page text, not a raster audit. Coverage box 180W–180E, 75N–65S includes the Philippines geographically. That is not a count of valid LGU-months. |
| EOG-LIC | VNL may be copied, modified, and distributed for any purpose, including commercial use, with attribution and a change notice. | EOG Products — Data Access and Licensing. PDF retrieved 6 October 2026. | https://eogdata.mines.edu/files/EOG_products_CC_License.pdf | Page 1. Quote: “makes many of their datasets publicly available under the Creative Commons Attribution 4.0 International license (CC-BY 4.0). These include the DMSP nighttime lights, VIIRS nighttime lights (VNL).” And: “users are allowed to copy, modify, and distribute data in any format for any purpose, including commercial use.” | verified-passage | Exhibit 2 requires citation of the relevant VNL papers. The PDF also points licensing questions to EOG and the Mines technology-transfer office. |
| ELVIDGE-2021 | Annual V.2 nighttime lights are monthly cloud-free radiance averages, filtered for fires, aurora, and background. Dim-light detection and cloud-free counts affect the product. The series is aimed at change detection. | Elvidge CD, Zhizhin M, Ghosh T, Hsu FC, Taneja J. Remote Sensing. 2021;13(5):922. | https://doi.org/10.3390/rs13050922 | Crossref JATS abstract. Quote: “produced using monthly cloud-free radiance averages made from low light imaging day/night band (DNB) data.” Background isolation “under 1 nW/cm2/sr.” “The DR threshold for zeroing out background rises as the number of cloud-free observations falls.” “optimizing the set for change detection analyses.” | abstract-only | MDPI HTML returned HTTP 403. No sample of Philippine grid cells was read. |
| FALCHI-2016 | The world atlas is zenith artificial night-sky brightness modeled from VIIRS DNB and calibrated with ground observations. Upward emission functions are inputs to the maps. The Philippines has a row of modeled population and area percentages. | Falchi F, Cinzano P, Duriscoe D, Kyba CCM, Elvidge CD, Baugh K, Portnov BA, Rybnikova NA, Furgoni R. Science Advances. 2016;2(6):e1600377. | https://doi.org/10.1126/sciadv.1600377 ; PMC4928945 | Europe PMC full text XML. Abstract sentence: “The world atlas of zenith artificial night sky brightness is modelled with VIIRS DNB data and calibrated with more than 35,000 observations.” Figure caption: “Upward emission functions used to compute the maps.” Country table headers include brightness thresholds ≤1.7, >1.7, >14, >87, >688, and >3000 μcd/m², split into Population (%) and Area (%). Philippines population cells: 8.7, 91.3, 67.2, 47.6, 26.5, 7.2. Area cells: 35.6, 64.4, 20.9, 6.1, 0.7, 0.1. | verified-passage | The 35,000 observations are not broken out by country in the passages read. The Philippines numbers are modeled percentages, not ground-site counts and not 2021–2026 measurements. |
| BARA-2019 | SQM-band zenith brightness and VIIRS-DNB top-of-atmosphere radiance can show different and even opposite behavior when lighting spectra change. | Bará S, Rigueiro I, Lima RC. arXiv:1909.10909. Publisher DOI on the arXiv record: 10.1016/j.jqsrt.2019.106644. Submitted 24 September 2019. | https://arxiv.org/abs/1909.10909 | arXiv abstract. Quote: “these indicators may show different, even opposite behaviors.” Indicators named include “the brightness in the specific photometric band of the widely used Sky Quality Meter (SQM), and the top-of-atmosphere radiance detected by the VIIRS-DNB.” | abstract-only | Journal PDF not opened. Single-scattering model, not a Philippine empirical fit. |
| BUSTAMANTE-2020 | Ground and satellite light comparisons are possible, and VIIRS/DNB acquires data late at night after much lighting is off. The opened case is Granada. | Bustamante-Calabria M, Sánchez de Miguel A, Martín-Ruiz S, Ortiz JL, Vílchez JM, Pelegrina A, and others. arXiv:2011.09252. Publisher DOI on the record: 10.3390/rs13020258. | https://arxiv.org/abs/2011.09252 | arXiv abstract. Quote: “the SNPP-VIIRS/DNB instrument, which acquires data late at night after most human nocturnal activity has already occurred and much associated lighting has been turned off.” The study location in the abstract is Granada, Spain, 14 March to 31 May 2020. | abstract-only | Not Philippine. Do not import their PM10–sky-brightness expression as a local result. |
| FALCHI-2020-ARXIV | The atlas of night-sky brightness, VIIRS-recorded radiance, and GDP are used as separate inputs in a USA–Europe comparison. | Falchi F, Furgoni R, Gallaway TA, Rybnikova NA, Portnov BA, Baugh K, and others. arXiv:2007.01150. Publisher DOI on the record: 10.1016/j.jenvman.2019.06.128. | https://arxiv.org/abs/2007.01150 | arXiv abstract. Quote: “Using data from the New World Atlas of Artificial Night Sky Brightness, VIIRS-recorded radiance and Gross Domestic Product (GDP) data, we compared light pollution levels.” | abstract-only | Journal version not opened separately. Geography is USA and Europe. |
| AKSAKER-2026 | VIIRS composites are used to study light trends at 216 International Dark-Sky Places. The map unit is radiance. A log equation converts it to SQM units for visualization. Gradient boosting is one of their models. The opened HTML does not mention the Philippines. | Aksaker N, Bayazıt M, Kurt Z, and others. Progress in Earth and Planetary Science. 2026;13:2. Published 12 January 2026. | https://doi.org/10.1186/s40645-025-00739-x | Open-access HTML on Springer Nature Link. Abstract: “This study analyses light pollution trends in International Dark-Sky Places (IDSPs) using VIIRS night light composite data.” “Currently, there are 216 IDSPs in the world.” “Machine learning models including decision tree regression (DTR), random forest regression (RFR) and gradient boosting regression (GBR) provided good predictive accuracy (R² > 0.6).” Figure 3 discussion: “The map in Fig. 3 shows the ALAN, where the radiation unit is nW cm⁻² sr⁻¹.” Conversion: “SQM = 20.0 − 1.9 × log(AL).” | verified-passage | Their R² is their reported fit, not a result of this screen, and the places are existing global designations. The SQM equation is a display conversion. A correction DOI exists and was not read. |
| SO-2026 | Hong Kong night-sky brightness was monitored with SQM photometers for a decade. The abstract says satellite systems do not provide that sub-minute sampling. | So CW, Pun CSJ, Liu S. Remote Sensing. 2026;18(11):1691. | https://doi.org/10.3390/rs18111691 | Crossref abstract. Quote: “Photometric data were collected nightly and continuously from multiple locations equipped with a Sky Quality Meter.” “The in situ observation frequency was at sub-minute intervals, characterizing nighttime profiles with a temporal resolution that other monitoring systems (e.g., satellites) cannot provide.” | abstract-only | Hong Kong, not the Philippines. MDPI HTML returned HTTP 403. |
| PAGADUAN-2022 | Higher-quality VIIRS nighttime lights predict urban subnational GDP in the Philippines and still do not explain rural economic activity very well. | Pagaduan JA. Asian Economic Journal. 2022;36(3):288–317. | https://doi.org/10.1111/asej.12278 | Crossref abstract. Quote: “the higher-quality VIIRS NTL data predict urban economic activity sufficiently well for both light-intense and dimly lit regions but still do not explain rural economic activity very well.” | abstract-only | Economic proxy. Not sky brightness, ecology, or a lighting ordinance. |
| RAMEL-2026 | A 2026 paper’s title links nighttime lights and land values in the Philippines. | Ramel RCD, Legaspi JD, Pajaron MC. Remote Sensing Letters. 2026;17(5):465–477. Crossref affiliation includes University of the Philippines. | https://doi.org/10.1080/2150704x.2026.2650396 | Crossref title and issue metadata. No abstract field. | lead | Full text not opened. Not used as a sky-brightness result. |
| FAN-2025 | Dark-sky-park suitability in the Greater Bay Area is studied with Delphi expert consultation, GIS, and multi-criteria decision-making, using nighttime light levels among other criteria. The abstract also discusses ecotourism. | Fan D, Chen Z, Liu Y, and others. Land. 2025;14(8):1561. | https://doi.org/10.3390/land14081561 | Crossref abstract. Quote: “we employ Delphi expert consultation, GIS spatial analysis, and multi-criteria decision-making to identify optimal DSP locations.” Resource base includes “nighttime light levels.” Findings mention “high ecotourism potential” and later “nighttime tourism.” | abstract-only | Not the Philippines and not NSGA-II. Ecological degradation appears as framing. The described analysis is suitability, not a measured biological response. |
| LI-RSE-2026 | A 2026 paper’s title says global dark-sky quality and potential park sites are studied with multi-source data and a random forest. | Li Z, Xing R, Ling Q, and others. Remote Sensing of Environment. 2026;333:115114. | https://doi.org/10.1016/j.rse.2025.115114 | Crossref title, volume, and article number. Abstract field empty. | lead | Method and sample size were not verified beyond the title. |
| LI-SSRN-NSGA | Constraint-guided NSGA-II is described for highway weather-station siting. | Li Z. SSRN. DOI issued 2026 in the Crossref record. | https://doi.org/10.2139/ssrn.7396619 | Crossref abstract. Quote: “this study formulates a multi-objective optimization (MOO) model and develops a constraint-guided Non-dominated Sorting Genetic Algorithm II (NSGA-II) for highway RWIS siting.” | abstract-only | Wrong decision. Shows the algorithm in another siting problem. Preprint. |
| BAQUIRAN-2020 | Short-term artificial light had no large-scale effect on the *Acropora digitifera* microbiome in the reported experiment, with some taxa enriched. | Baquiran JIP, Nada MAL, Campos CLD, and others. Microorganisms. 2020;8(10):1566. First-author affiliation on Crossref: Marine Science Institute, University of the Philippines Diliman. | https://doi.org/10.3390/microorganisms8101566 | Crossref abstract. Quote: “Exposure to ALAN had no large-scale effect on the coral microbiome, although taxa affiliated with Rhodobacteraceae, Caulobacteraceae, Burkholderiaceae, Lachnospiraceae, and Ruminococcaceae were significantly enriched.” | abstract-only | Not satellite multispectral mapping. The abstract does not name the field site. Affiliation is not a nationwide ecological dataset. |
| SDGSAT-ABOUT | SDGSAT-1 data are provided after proposal approval, for scientific research, within a period not exceeding 24 months, with a signed user agreement. Large global requests are outside the program. | International Research Center of Big Data for Sustainable Development Goals. SDGSAT-1 Open Science Program, About the Program. Page retrieved 6 October 2026. | https://www.sdgsat.ac.cn/sciencePlan/aboutPro | English text in the page’s application bundle (`chunk-19b7e4f5`), because the HTML shell requires JavaScript. Quotes: “The SDGSAT-1 data will be provided free of charge following the approval of the submitted proposal.” “The applied research period should not exceed 24 months, starting from the date of the approval of the proposal.” “The acquired data can only be used for scientific research.” “data covering large spatial scales, such as global and intercontinental scale, cannot be supported through this program.” “the principal investigator and co-investigators are required to sign a detailed user agreement for SDGSAT-1 data.” | verified-passage | The user-agreement file was not opened. “Scientific research” only is the commercial restriction the page states; it does not use the word “commercial” in the strings read. |
| ZENODO-HIRISE | The HiRISE label set has 64,947 images from 10,815 original landmarks and 232 source images, with specified augmentations and Martian classes, under CC BY 4.0. | Doran G, Dunkel E, Lu S, Wagstaff K. Mars orbital image (HiRISE) labeled data set version 3.2. 16 September 2020. | https://doi.org/10.5281/zenodo.4002935 | Zenodo metadata description and license field. Quote: “This dataset contains a total of 64,947 landmark images that were detected and extracted from HiRISE browse images, spanning 232 separate source images.” “This set was formed from 10,815 original landmarks.” Augmentations listed: 90°, 180°, and 270° rotations, horizontal flip, vertical flip, and random brightness adjustment. “Other is a catch-all class” and “makes up the majority of our data set.” License id `cc-by-4.0`. | verified-passage | Image zip files were not downloaded. Class names are from the record’s prose, not a re-count of the CSV. |
| WAGSTAFF-2018 | A CNN trained on Earth images was adapted by transfer learning to Mars imagery and deployed for content search. | Wagstaff K, Lu Y, Stanboli A, Grimes K, Gowda T, Padams J. Proceedings of the AAAI Conference on Artificial Intelligence. 2018;32(1). | https://doi.org/10.1609/aaai.v32i1.11404 | Crossref abstract. Quote: “We started with the AlexNet convolutional neural network, which was trained on Earth images, and used transfer learning to adapt the network for use with Mars images.” | abstract-only | Opposite transfer direction from the handoff title. Supervised classification, not unsupervised contrastive learning. AAAI PDF not opened. |
| BISWAS-2024 | A 2024 paper’s title is domain adaptation with contrastive learning for object detection in satellite imagery. | Biswas D, Tešić J. IEEE Transactions on Geoscience and Remote Sensing. 2024;62:1–15. | https://doi.org/10.1109/tgrs.2024.3391621 | Crossref title and pagination. Abstract field empty. | lead | Not evidence of an astronomical source extractor or of Philippine labels. |
| PAIS-ABOUT | eNIPAS brings the protected-area total to 248. The page states the legal framework and does not state a public shapefile license. | DENR Biodiversity Management Bureau, Protected Area Information System, About. Retrieved 6 October 2026. | https://pais.bmb.gov.ph/about | Page text. Quote: “The eNIPAS Act of 2018 brings to 248 the total number of Protected Areas in the Philippines, previously 240 under the NIPAS law.” Quote: “NIPAS and eNIPAS define protected areas as portions of land and water set aside by reason of their unique physical and biological significance, managed to enhance biological diversity and protected against destructive human exploitation.” A salient-features line reads “Recognition of local communities and Indigenous Peoples.” | verified-passage | `/downloads` and `/map` returned HTTP 404. This is not a finding that no file exists anywhere, only that these official pages do not grant a download. |
| PAIS-CONTACT | BMB publishes an institutional contact route in Quezon City. | PAIS Contact. Retrieved 6 October 2026. | https://pais.bmb.gov.ph/contact | Page text. Biodiversity Management Bureau, Ninoy Aquino Parks and Wildlife Center, 1100 Diliman, Quezon City; landline (02) 924-6031; bmb@bmb.gov.ph. | verified-passage | A public directory is not permission, interest, or a data-sharing agreement. No person was contacted. |
| WDPA-LEGAL | WDPCA materials and derivative works need prior written permission for commercial use. Redistribution and sublicensing are not allowed. | UNEP-WCMC and IUCN, Protected Planet legal terms. Retrieved 6 October 2026. | https://www.protectedplanet.net/en/legal | Page text. Quote: “Neither (a) the WDPCA Materials and the GD-PAME Materials nor (b) any work derived from or based upon the WDPCA Materials and the GD-PAME Materials (“Derivative Works") may be put to Commercial Use without the prior written permission of UNEP-WCMC.” Quote: “You may not redistribute the WDPCA and GD-PAME Data contained in the WDPCA and GD-PAME in whole or in part.” Commercial use includes use by a for-profit entity or revenue generation by a nonprofit. | verified-passage | The page uses WDPCA for the World Database on Protected and Conserved Areas. Noncommercial reading is not a right to republish boundaries. |
| GEOPORTAL | The national geoportal homepage opened and did not display a boundary-license statement in the extracted text. | Geoportal Philippines. Retrieved 6 October 2026. | https://geoportal.gov.ph/ | Homepage text is a map-application shell (Map Builder, hazards, tourism, and other apps). No license paragraph was present in the extracted text. | verified-passage | Absence of a license paragraph on the homepage is not a finding that administrative boundaries are free to use. |
| WU-2025 | Title only: nighttime light pollution in residential areas of megacities is identified from SDGSAT-1 glimmer imagery. | Wu Y, Huang C, Ye Y, and others. Remote Sensing of Environment. 2025;328:114894. | https://doi.org/10.1016/j.rse.2025.114894 | Crossref title. Abstract field empty. | lead | Not ecological disruption. Not opened. |
| JIA-2024 | Title only: coastal nighttime-light types are classified with the SDGSAT-1 Glimmer Imager. | Jia M, Zeng H, Chen Z, and others. Remote Sensing of Environment. 2024;305:114104. | https://doi.org/10.1016/j.rse.2024.114104 | Crossref title. Abstract field empty. | lead | “Type classification” is not, by title alone, a multispectral ecological measurement. |
| JACKSON-2025 | Title only: sky brightness in Texas is compared between International Dark Sky Places and control communities. | Jackson AP, Anderson SJ, Currit N, and others. Journal of Environmental Management. 2025;381:124842. | https://doi.org/10.1016/j.jenvman.2025.124842 | Crossref title. Abstract field empty. | lead | Texas, not the Philippines. Not used as a coverage claim. |
| EXCL-NOISE | Top Crossref ranks for broad nighttime-light queries included rice night temperature, Alzheimer’s disease, and unrelated gradient-boosting papers. | Examples: 10.1111/pce.14046; 10.3389/fnins.2024.1378498; 10.5220/0012958300004508. | Those DOIs | Title screen only. | excluded | Wrong outcome or wrong technique context. |

## Search log

Search date for every row: 6 October 2026. User-Agent: `thesis1-litreview/1.0 (https://github.com/u1yuan/django-flow)`. Export means the identifiers retained in this file after title screening. Crossref `total-results` is the API total, not the number judged relevant.

| Database | Date searched | Query | Filters | Results | Export |
| --- | --- | --- | --- | --- | --- |
| Crossref | 2026-10-06 | `query=Philippines VIIRS nighttime lights municipalities` | from-pub-date 2018-01-01, rows 15 | API total 59,901; top ranks were global VIIRS methods, not Philippine dark-sky papers | Elvidge-related VIIRS method leads; no Philippine sky-brightness paper in the top 15 |
| Crossref | 2026-10-06 | `query=light pollution Philippines nighttime` | from-pub-date 2010-01-01, rows 6 | API total 747,878; top ranks were global health and exposure papers | Excluded at title; none retained as Philippine sky-brightness studies |
| Crossref | 2026-10-06 | `query=Manila night sky brightness light pollution` | none, rows 6 | API total 1,175,848 | Kocifaj 2023 title retained as a modeling-bias lead; So 2026 retained; no Manila ground study in the top 6 |
| Crossref | 2026-10-06 | `query=sky quality meter VIIRS radiance correlation` | from-pub-date 2016-01-01, rows 6 | API total 1,155,911; top ranks were VIIRS clear-sky radiative-transfer papers, a different “radiance” | Excluded as the wrong radiance (daytime satellite calibration, not night-sky brightness) |
| Crossref | 2026-10-06 | `query=dark sky park random forest nighttime` | from-pub-date 2020-01-01, rows 6 | API total 648,608 | Li 2026 RSE title; Aksaker 2026; Fan-adjacent dark-sky planning titles |
| Crossref | 2026-10-06 | `query=NSGA-II protected area conservation site selection` | from-pub-date 2015-01-01, rows 6 | API total 1,380,969; top 6 were general conservation texts, not NSGA-II dark-sky papers | None retained from that top 6 |
| Crossref | 2026-10-06 | `query=NSGA-II dark sky park` | rows 5 | API total 3,071,094; top 5 were dark-sky items that are not NSGA-II | None retained; supports the statement that this query did not surface an NSGA-II dark-sky study |
| Crossref | 2026-10-06 | `query=SDGSAT-1 glimmer light pollution` | from-pub-date 2022-01-01, rows 6 | API total 294,046 | Wu 2025; Jia 2024; other SDGSAT application titles as leads |
| Crossref | 2026-10-06 | `query=HiRISE image classification` and `query.author=Wagstaff&query.title=Mars imagery` | rows 5–6 | HiRISE title search total 1,231,999; Wagstaff Mars-imagery search total 11 | Wagstaff 2018 retained; other HiRISE geology titles not used |
| Crossref | 2026-10-06 | `query=light pollution night&query.affiliation=Philippines` | rows 8 | API total 318 | Baquiran 2020 retained; rice and pesticide papers excluded |
| Crossref | 2026-10-06 | `query.title=nighttime lights&query.affiliation=Philippines` | rows 8 | API total 7 | Pagaduan 2022 and Ramel 2026 retained; fishing-ground and heat-island titles noted and not used as sky-brightness evidence |
| Crossref | 2026-10-06 | `query.title=International Dark Sky Places VIIRS` | rows 5 | API total 1,036,810 | Aksaker 2026 and Jackson 2025 title |
| Crossref | 2026-10-06 | `query.title=new world atlas of artificial night sky brightness` | rows 3 | API total 4,627,491 | Falchi 2016; Cinzano 2001 noted as the earlier atlas and not re-read |
| Crossref | 2026-10-06 | Works endpoint for the DOIs listed in the ledger | none | 16 DOI lookups, plus Elvidge 2021 | Abstracts where deposited; empty abstract recorded as lead or abstract-only as shown |
| Crossref | 2026-10-06 | Earlier broad queries (`VIIRS nighttime`, `XGBoost nighttime light prediction`, `artificial light at night ecological`) | mixed | Several HTTP 429 responses after the first burst; those queries were repeated later in narrower form | No unique included paper came only from the rate-limited burst |
| arXiv | 2026-10-06 | `all:"light pollution" AND all:VIIRS AND all:brightness` | max_results 5 | 5 entries returned; `totalResults` was not captured by the parser | Bará 1909.10909; Falchi 2007.01150; Bustamante-Calabria 2011.09252. Other entries (France modeling; Egypt site selection) were not needed beyond the screen |
| arXiv | 2026-10-06 | `all:SDGSAT-1 AND all:nighttime` | max_results 5 | 2 entries returned, on fishing-vessel detection and earthquake SAR recovery | Excluded; they are not SDGSAT ecological studies |
| arXiv | 2026-10-06 | `all:HiRISE AND all:classification AND all:convolutional` | max_results 5 | No entries in the response | Empty for this string |
| arXiv | 2026-10-06 | `all:NSGA-II AND all:"protected area"` | max_results 5 | No entries in the response | Empty for this string |
| arXiv | 2026-10-06 | `id_list=2007.01150,1909.10909,2011.09252` | exact ids | 3 records | Full abstracts used in the ledger |
| Semantic Scholar | 2026-10-06 | Eight queries on Philippine VIIRS, SQM, dark-sky parks, NSGA-II, source detection, HiRISE, Globe at Night, and SDGSAT ecology | year filters 2015–2026 or 2018–2026 | HTTP 429 on all eight | No records. Not counted as a successful second index |
| Europe PMC | 2026-10-06 | DOI lookups and PMC4928945 full text XML | none | Falchi 2016 full text opened; several MDPI DOIs had no Europe PMC hit | Falchi passages and the Philippines table row |
| Official pages | 2026-10-06 | EOG VNL page, EOG license PDF, Zenodo API, SDGSAT about bundle, PAIS about and contact, Protected Planet legal, Geoportal homepage | public HTML, PDF, or JSON only | Pages listed in the ledger | Rights and counts quoted above |

Earlier arXiv calls in the same session returned HTTP 429 before the successful calls above. Those failed calls are not counted as searches that returned literature.

## References

Aksaker N, Bayazıt M, Kurt Z, et al. Light pollution trends for International Dark Sky Places using VIIRS nighttime light composite data. *Progress in Earth and Planetary Science*. 2026;13:2. https://doi.org/10.1186/s40645-025-00739-x

Bará S, Rigueiro I, Lima RC. Monitoring transition: expected night sky brightness trends in different photometric bands. arXiv:1909.10909. 2019. https://arxiv.org/abs/1909.10909

Baquiran JIP, Nada MAL, Campos CLD, et al. The prokaryotic microbiome of *Acropora digitifera* is stable under short-term artificial light pollution. *Microorganisms*. 2020;8(10):1566. https://doi.org/10.3390/microorganisms8101566

Biswas D, Tešić J. Domain adaptation with contrastive learning for object detection in satellite imagery. *IEEE Transactions on Geoscience and Remote Sensing*. 2024;62:1–15. https://doi.org/10.1109/tgrs.2024.3391621

Bustamante-Calabria M, Sánchez de Miguel A, Martín-Ruiz S, et al. Effects of the COVID-19 lockdown on urban light emissions: ground and satellite comparison. arXiv:2011.09252. 2020. https://arxiv.org/abs/2011.09252

Doran G, Dunkel E, Lu S, Wagstaff K. Mars orbital image (HiRISE) labeled data set version 3.2. Zenodo; 2020. https://doi.org/10.5281/zenodo.4002935

Earth Observation Group. VIIRS nighttime lights. https://eogdata.mines.edu/products/vnl/

Earth Observation Group. EOG products — data access and licensing. https://eogdata.mines.edu/files/EOG_products_CC_License.pdf

Elvidge CD, Zhizhin M, Ghosh T, Hsu FC, Taneja J. Annual time series of global VIIRS nighttime lights derived from monthly averages: 2012 to 2019. *Remote Sensing*. 2021;13(5):922. https://doi.org/10.3390/rs13050922

Falchi F, Cinzano P, Duriscoe D, et al. The new world atlas of artificial night sky brightness. *Science Advances*. 2016;2(6):e1600377. https://doi.org/10.1126/sciadv.1600377

Falchi F, Furgoni R, Gallaway TA, et al. Light pollution in USA and Europe: the good, the bad and the ugly. arXiv:2007.01150. 2020. https://arxiv.org/abs/2007.01150

Fan D, Chen Z, Liu Y, et al. Integrating dark sky conservation into sustainable regional planning: a site suitability evaluation for dark sky parks in the Guangdong–Hong Kong–Macao Greater Bay Area. *Land*. 2025;14(8):1561. https://doi.org/10.3390/land14081561

International Research Center of Big Data for Sustainable Development Goals. SDGSAT-1 Open Science Program: about the program. https://www.sdgsat.ac.cn/sciencePlan/aboutPro

Jackson AP, Anderson SJ, Currit N, et al. Sky brightness in Texas: a comparative study between international dark sky places and control communities. *Journal of Environmental Management*. 2025;381:124842. https://doi.org/10.1016/j.jenvman.2025.124842

Jia M, Zeng H, Chen Z, et al. Nighttime light in China's coastal zone: the type classification approach using SDGSAT-1 Glimmer Imager. *Remote Sensing of Environment*. 2024;305:114104. https://doi.org/10.1016/j.rse.2024.114104

Li Z. Multi-objective site selection for highway RWIS stations using a constraint-guided NSGA-II. SSRN. https://doi.org/10.2139/ssrn.7396619

Li Z, Xing R, Ling Q, et al. Exploring global dark sky quality and potential dark sky park site selection: integrating multi-source spatial data with random forest model. *Remote Sensing of Environment*. 2026;333:115114. https://doi.org/10.1016/j.rse.2025.115114

Pagaduan JA. Do higher-quality nighttime lights and net primary productivity predict subnational GDP in developing countries? Evidence from the Philippines. *Asian Economic Journal*. 2022;36(3):288–317. https://doi.org/10.1111/asej.12278

Protected Area Information System. About. https://pais.bmb.gov.ph/about

Protected Area Information System. Contact. https://pais.bmb.gov.ph/contact

Ramel RCD, Legaspi JD, Pajaron MC. Illuminating the land: the effects of nighttime lights on land values in the Philippines. *Remote Sensing Letters*. 2026;17(5):465–477. https://doi.org/10.1080/2150704x.2026.2650396

So CW, Pun CSJ, Liu S. Decade-long photometric observations of light pollution and cloud effects on night sky brightness in Hong Kong. *Remote Sensing*. 2026;18(11):1691. https://doi.org/10.3390/rs18111691

UNEP-WCMC and IUCN. Protected Planet legal terms. https://www.protectedplanet.net/en/legal

Wagstaff K, Lu Y, Stanboli A, Grimes K, Gowda T, Padams J. Deep Mars: CNN classification of Mars imagery for the PDS Imaging Atlas. *Proceedings of the AAAI Conference on Artificial Intelligence*. 2018;32(1). https://doi.org/10.1609/aaai.v32i1.11404

Wu Y, Huang C, Ye Y, et al. Identification and evaluation of nighttime light pollution in residential gathering area of megacities based on SDGSAT-1 glimmer imagery. *Remote Sensing of Environment*. 2025;328:114894. https://doi.org/10.1016/j.rse.2025.114894

## Open questions

- No VIIRS extract exists in this screen, so eligible LGU-months after cloud screening and a legal boundary join are unknown.
- No Philippine SQM, photometer, or Globe at Night site list was opened, so a held-out-site design cannot be sized.
- PAIS does not, on the pages opened, state how to obtain NIPAS polygons. BMB’s own site returned HTTP 403. Whether a separate DENR request path exists was not established.
- The SDGSAT-1 user agreement’s exact redistribution and publication clauses were not read.
- Li 2026, Wu 2025, Jia 2024, Jackson 2025, and Ramel 2026 still need full texts before any of their methods or sample sizes are cited as findings.
- It was not established whether any Philippine site is among the 216 International Dark-Sky Places in Aksaker’s set. The opened HTML had no “Philippine” string.
- Expert criteria, field-check protocols, and tourism demand were not opened. They remain requirements, not results.
