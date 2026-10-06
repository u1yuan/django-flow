# Local-only audit of two literature-log claims

Date: 2026-09-28  
Scope: `docs/activities/litReview/LITERATURE_LOG.md` only. No publisher article, abstract, DOI resolver, metadata service, or external database was consulted. No unpublished data was used.

## Evidence ledger

| Claim in the local log | Source ID and metadata **as recorded in the log** | Exact local locator | Verification method and status | Relevance and caveat |
| --- | --- | --- | --- | --- |
| Philippine small-island grids have diesel fuel-use values of about **0.26–0.83 L/kWh** and site-specific diesel prices; the study sizes renewable microgrids against that baseline. | L1: Paul Bertheau (2020), *Supplying not electrified islands with 100% renewable energy based micro grids: A geospatial and techno-economic analysis for the Philippines*; DOI **as recorded**: `10.1016/j.energy.2020.117670`. | `LITERATURE_LOG.md`, “Local literature,” item 3, lines 15–16. | Read the log entry only. **Unverified source claim and unverified citation metadata/DOI.** No paper passage, table, abstract, or page was checked. | Potentially relevant to diesel fuel use. The log calls L/kWh “fuel efficiencies”; the unit denotes fuel volume per electrical energy, so the source’s actual metric and denominator need checking before this is described as efficiency. The final sentence linking the figures to fault-linked anomaly monitoring is the log writer’s rationale, not an observed result established here. |
| Fast RobustSTL extends RobustSTL to handle multiple seasonal cycles and improve speed with generalized ADMM, separating trend, seasonality, outliers, and noise. | F1: Qingsong Wen, Zhe Zhang, Li Yan, Liang Sun (2020), *Fast RobustSTL: Efficient and Robust Seasonal-Trend Decomposition for Time Series with Complex Patterns*; DOI **as recorded**: `10.1145/3394486.3403271`. | `LITERATURE_LOG.md`, “Foreign literature,” item 1, lines 24–25. | Read the log entry only. **Unverified source claim and unverified citation metadata/DOI.** No method section, results, abstract, or page was checked. | Relevant as a proposed decomposition method. The log does not establish that the paper tested genset efficiency, generalized ESD on its residuals, or this thesis’s combined pipeline. The application sentence is a proposed design choice. |

## Source-level verification still needed

1. **L1:** Resolve the recorded DOI and compare its title, author, year, and venue with the log. Open the publisher or authoritative full text; locate the table or passage giving the 0.26–0.83 L/kWh range, check its sample/sites, whether the range is observed or modeled, the precise metric, and any qualification. Record page/table/figure before citing the number.
2. **F1:** Resolve the recorded DOI and check title, author, year, and venue. In the official paper, locate the method passage for multiple seasonal cycles and generalized ADMM, and the evaluation passage for the speed claim. Note exact sections/pages and whether the decomposition labels in the log match the authors’ formulation.
3. **Both:** Keep the thesis-specific implications separate from each publication’s findings. Neither local entry supplies source-level support for performance on Palawan NPC-SPUG genset data or for the RobustSTL–generalized ESD combination.

## Reproducibility and limits

Local source screened: the one named literature log, sections “Local literature” and “Foreign literature.” Selection rule: audit one precise quantitative diesel claim and one central method claim. Local lookup strings: `Supplying not electrified`, `diesel fuel efficiencies`, `Fast RobustSTL`, `generalized ADMM`. Two entries selected; no external search or deduplication. This ledger confirms what the log says, **not** whether the cited publications say it. No claim above is cleared for source-verified research prose.
