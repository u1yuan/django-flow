# AquaVir search protocol

Generated: 2026-09-28
Review type: scoping
Active track: multi-zone hydroponic IoT analytics (AquaVir). The diesel-genset literature log is out of scope.

## Research questions

1. Which anomaly-detection algorithms are used on multivariate hydroponic or controlled-environment sensor streams, and which fit unlabeled multi-zone monitoring?
2. Which prediction targets appear in that literature, and which remain feasible when harvest or yield labels are unavailable?
3. Which single algorithm should be AlgoA (anomaly detection) and which should be AlgoB (predictive analytics)?

## Design constraints used as recommendation filters

These come from the feasibility study as design constraints, not as measured AquaVir results. No facility dataset is on disk, so this review does not analyze sensor records.

- Analytics on existing zone sensors. Hardware design is excluded.
- Expected variables: pH, EC/TDS, nutrient-solution temperature, water level, humidity, and dosing or maintenance context when a study uses it.
- Anomalies are expected to be scarce or unlabeled. A method that needs a large labeled anomaly set cannot be the primary AlgoA choice.
- Open-source Python on a laptop, with an operator-readable zone alert. A deep model is eligible only if included papers show a clear gain and report a simpler baseline.
- Hoped data shape is at least three zones and on the order of 10,000 timestamped multivariate rows. That dataset is not confirmed. Every recommendation states its data requirement.

Candidate families named in the feasibility file (zone baseline or clustering, reconstruction-based multivariate anomaly detection, change-point or drift detection) are options to test against the literature, not preset winners. Survey citations in that file (Belay 2023, Cook 2020, Chatterjee 2022) are leads until a DOI record and a relevant passage are checked.

## Sources and window

- OpenAlex, via `docs/activities/litReview/.agents/skills/literature-search-openalex` CLI only.
- arXiv, via `docs/activities/litReview/.agents/skills/literature-search-arxiv` utility scripts only.
- DOI and bibliographic metadata checks via `.agents/skills/citation-management` (Crossref / OpenAlex lookup). This is verification, not a third discovery database.
- Publication window: 2018-01-01 through 2026-09-28.
- Language: English.
- Publication types: journal articles, conference papers, and preprints. Preprints stay labeled as preprints.
- Retracted works are excluded when the index marks them retracted.

## Search strings

OpenAlex filters applied to every `--search` below:

`from_publication_date:2018-01-01,to_publication_date:2026-09-28,language:en,is_retracted:false`

| ID | Database | Query |
| --- | --- | --- |
| OA-A1 | OpenAlex | hydroponic anomaly detection sensor |
| OA-A2 | OpenAlex | hydroponic IoT fault detection pH EC |
| OA-A3 | OpenAlex | greenhouse nutrient solution outlier detection multivariate |
| OA-P1 | OpenAlex | hydroponic sensor forecast pH EC temperature |
| OA-P2 | OpenAlex | hydroponic predictive analytics nutrient dosing |
| OA-P3 | OpenAlex | hydroponic yield prediction IoT sensors |
| AX-A1 | arXiv | `(ti:hydroponic OR abs:hydroponic) AND (abs:"anomaly detection" OR abs:"fault detection" OR ti:anomaly)` |
| AX-P1 | arXiv | `(ti:hydroponic OR abs:hydroponic) AND (abs:forecast OR abs:prediction OR ti:predict) AND (abs:pH OR abs:sensor OR abs:nutrient)` |

Known-lead DOI lookups, not counted as search hits until retrieved:

- Cook, Mısırlı, and Fan (2020), https://doi.org/10.1109/JIOT.2019.2958185
- Chatterjee and Ahmed (2022), Internet of Things, 19, 100568 (DOI to resolve, not assumed)
- Belay et al. (2023), Sensors, 23 (DOI to resolve, not assumed)

Sort OpenAlex by `cited_by_count:desc`. Request 10 results per query, then a second page only if the first page is still on-topic. arXiv `--max_results` is 10 per query, sorted by relevance. Raw JSON stays under `docs/activities/litReview/aquavir/raw/`.

## Inclusion

A study is included when all of the following hold:

- The system is hydroponic, soilless, nutrient-film, deep-water culture, or a controlled-environment nutrient-solution or greenhouse sensor setting that reports multivariate environmental or solution measurements.
- The paper names at least one anomaly-detection or predictive algorithm.
- The paper names a dataset, deployment, or experimental setup.
- The paper reports an evaluation: a metric, a baseline comparison, or a stated operational result.
- Title, abstract, or full text is in English and the publication date is inside the window.

Surveys and method reviews may be included as method maps. They do not by themselves count as independent support for naming AlgoA or AlgoB on hydroponic data.

## Exclusion

- Wrong setting: diesel generation, power systems, or another non-agricultural domain.
- Hardware-only monitoring with no named analytics algorithm.
- Image-only plant vision or disease classification without a multivariate sensor time series.
- No named algorithm, or no dataset and no evaluation.
- Duplicate of an already screened work (DOI, then arXiv id, then normalized title plus first author and year).
- Outside the date window, not English, retracted, or full text unavailable when the recommendation would depend on a claim the abstract does not state.

Record the exclusion reason. Do not drop conflicting or negative findings that otherwise meet inclusion.

## Screening and extraction

1. Title.
2. Abstract. An abstract supports only the sentence it states.
3. Full text for any study used in the algorithm decision. Opening the relevant passage is required before a claim is marked verified.

Extraction fields: study id, bibliographic metadata, DOI or stable URL, design, setting and variables, algorithm, prediction or detection target, dataset, comparator, metric and reported result, label requirement, limitations, verification status, and locator.

## Decision rule

Prediction target for AlgoB: compare sensor-state forecast, dosing or pH intervention, and yield. Prefer the target that is repeated in hydroponic multivariate sensor studies and does not require a labeled harvest dataset. State the rejected targets and the evidence for rejection.

Name one primary algorithm per slot only when at least two independent sources support it for that target on a hydroponic or nutrient-solution sensor task. A general IoT survey is not one of those two sources. If that bar is not met, keep the best-supported candidate, mark confidence as limited, and name one simpler baseline the thesis should still implement.

Score eligible candidates on:

1. Directness: hydroponic or nutrient-solution multivariate sensors, then near-analog greenhouse sensors.
2. Label fit: usable when anomaly labels or yield labels are scarce.
3. Open-source Python implementability on a laptop.
4. Operator-readable zone output.
5. A reported evaluation with a named metric or baseline.

## Verification status labels

- **Verified:** DOI or stable bibliographic record checked, and the relevant full-text passage opened.
- **Abstract-only:** metadata checked, but the supporting passage was not opened. Cannot carry a recommendation claim.
- **Lead:** named in the feasibility file or in another paper, not yet retrieved.
- **Excluded:** screened out, with a reason.

## Outputs

- `docs/activities/litReview/aquavir/search-log.md`
- `docs/activities/litReview/aquavir/evidence-ledger.md`
- `docs/activities/litReview/aquavir/algorithm-review.md`

## Protocol amendments (2026-09-28)

The original strings above were run. Two limits changed what could be screened:

- OpenAlex `--search` treats the query as a bag of words. The first pages were highly cited agriculture reviews with little hydroponic algorithm content. Title-and-abstract filters were added and are logged as OA-A1-title through OA-P3-title and OA-nutrient. Those filters are part of the record, not a silent replacement of the original strings.
- Unauthenticated OpenAlex requests returned HTTP 429. Later queries completed only after retries. No API key was present.
- The arXiv utility script returned HTTP 406 after the query reached `export.arxiv.org`. A descriptive `User-Agent` was set and the query was retried. The 406 remained. No arXiv result list was retrieved. Europe PMC and Crossref were used only to open abstracts or full text for works already identified, not as a third discovery database.

## Data handling

No partner, customer, or facility records are in this review. Do not send restricted documents to external services. Search queries go only to OpenAlex, arXiv, and citation-metadata endpoints. Downloaded open papers, if any, stay in `docs/activities/litReview/aquavir/raw/` and are cited by URL.
