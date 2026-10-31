# ThesisPro readability review (funnel rubric)

Date: 2026-10-31  
Source: ThesisPro draft v1 proposals #144, #153, #156, #157, #173 (read-only extract; full text kept outside the repo).  
Prior content review: [ThesisPro proposal evaluation](cff3fd7b-f22c-4499-81e1-61be813ae1d7). This pass covers narrative funnel, established-work framing, and prose only.

## Rubric (6 × 1–5, total 30)

| Criterion | 1 | 3 | 5 |
| --- | --- | --- | --- |
| **Opening** | No clear broad problem | Broad problem stated but weakly cited | Global or national problem stated with citation |
| **Narrowing** | Jumps levels or repeats the same level | Some transitions; one detour | Each paragraph narrows (national → local → setting) |
| **Established work** | Gap asserted with no prior work named | Prior work listed, little contrast | Each named work cited, what it does, where it stops; gap follows |
| **Gap and question** | Gap missing or unrelated to objectives | Gap stated; link to question uneven | Explicit gap from contrast; study question follows |
| **Ending** | Title, objectives, scope, or contribution misaligned | Mostly aligned; one weak objective or scope clash | One general objective matches title; SOs measurable; scope/limitations agree |
| **Prose and support** | Hard to follow; many unsupported claims | Readable with several citation or clarity issues | Clear topic flow; in-text citations match reference list |

## Scoreboard (ranked)

| Rank | ID | Title (short) | Total /30 | Biggest funnel break |
| --- | --- | --- | --- | --- |
| 1 | #144 | Fish landing shortfalls / mangrove (AquaTerra) | **24** | Title implies exposure *from* mangrove change while Limitations deny causal mangrove effects |
| 2 | #153 | Explainable GIS DSS / native trees | **23** | Area says one reforestation site; Scope and datasets say four sites |
| 3 | #173 | Crime forecasting + streetlights, Quezon City | **22** | Title foregrounds forecasting; general objective is streetlight placement DSS |
| 4 | #156 | Post-delivery tomato shelf life | **18** | Established literature thin before methods; Scope names Google Maps Routes API while dataset cards exclude Google Maps content |
| 5 | #157 | Multi-zone hydroponic IoT analytics | **17** | Background names little established multi-zone analytics; Scope hedges TFT while SO2 commits; title differs from agreed AquaVir name |

**QA note.** Quotes were checked against `%TEMP%\thesispro-readability\*.md` extracts (2026-10-31). Citation accuracy was not re-verified against publisher text (per plan).

---

## #144 — Forecasting Municipal Fish Landing Shortfalls and Economic Exposure from Mangrove Change Using GAMMs and Random Forests

**Total: 24/30** — Opening 4, Narrowing 4, Established work 5, Gap 4, Ending 3, Prose 4.

### Funnel map

| Level | Carrier sentence (quoted or missing) |
| --- | --- |
| Broad problem | "Municipal fisheries support the income, employment, and food supply of Philippine coastal communities. FAO (2024) identifies small-scale fisheries as an important source of rural livelihoods…" |
| Local context | "…Dumilag et al. (2023) document income and food-security difficulties experienced by municipal fisherfolk in Magallanes, Sorsogon…" / "Oceana (2026) reported an estimated annual loss of approximately 45 million kilograms of fish catch…" |
| Established work | "Recent Philippine research has already established a forecasting approach… Bokingkito et al. (2026)…" / "The study will adapt the sequential Random Forest–GAMM approach of Nesslage et al. (2021)…" / Holmes et al. (2021) on testing environmental predictors on unseen data |
| Gap | "AquaTerra instead focuses on evaluating province- and fish-category forecasts for seasonal supply shortfalls and their associated gross landing value at risk." |
| Research question | Implicit: whether RF–GAMM forecasts plus shortfall and value-at-risk ranking improve planning beyond prior fisheries forecasting and seasonal baselines |
| Objectives / contribution | General objective names AquaTerra, RF–GAMM, shortfalls, gross landing value at risk; contribution paragraph bounds claims (no confirmed revenue loss) |

### Established-work check

| Prior work (as named) | Contrasted with this study? |
| --- | --- |
| Bokingkito et al. (2026) — regional fisheries forecasting with XAI | Yes — forecasting itself is not the contribution |
| Nesslage et al. (2021) — RF then GAMM for landings | Yes — adapted to Philippine municipal panel |
| Holmes et al. (2021) — environmental covariates on unseen periods | Yes — motivates predictor testing and shortfall detection |
| Rahman et al. (2022), Galparsoro et al. (2024) | In reference list only — not used in background funnel |

### Funnel breaks

- Title leads with GAMMs and Random Forests and says "Economic Exposure **from Mangrove Change**," but Limitations state the study "will **not establish causal effects** of mangrove change or typhoons."
- Specific Objective 5 (DTI collaboration) is outreach, not a measurable research outcome; it weakens the ending.
- Area of Investigation front-loads methods before the background pays off the economic-exposure story (minor detour).

### Paragraph-level issues

- Strong contrast paragraph on Bokingkito avoids overstating novelty (good).
- "Economic exposure" is carefully bounded in background (good); title does not match that caution.

### Rewrite suggestions

- **Title:** Lead with supply shortfall and gross landing value at risk; move RF–GAMM to subtitle; replace "from Mangrove Change" with "with Mangrove and Typhoon Covariates" or similar non-causal wording.
- **SO5:** Move collaboration to Scope or a separate stakeholder plan; replace with a measurable validation objective if it stays in SOs.

---

## #153 — An Explainable GIS Decision Support System Using MaxEnt, AHP, and Edge Sensing for Philippine Native Trees

**Total: 23/30** — Opening 4, Narrowing 3, Established work 5, Gap 4, Ending 4, Prose 3.

### Funnel map

| Level | Carrier sentence |
| --- | --- |
| Broad problem | "The Philippines has diverse native and endemic tree species that contribute to biodiversity conservation, watershed protection…" |
| Local context | DENR site-matching emphasis (no in-text citation on the DENR policy sentence) |
| Established work | Dolores et al. (2020) GIS–AHP; Zurbito et al. (2024) MaxEnt; edge/IoT (Roostaei et al., 2023) |
| Gap | "These studies show that GIS-AHP, MaxEnt, and edge sensing are individually useful, but they address different parts of the site-selection problem." |
| Research question | Integrated explainable DSS combining the three lines |
| Objectives / contribution | General objective and SO4 (interpretability) align with "explainable" in title |

### Established-work check

| Prior work | Contrasted? |
| --- | --- |
| Dolores et al. (2020) | Yes — static maps, no continuous micro-site monitoring |
| Zurbito et al. (2024) | Yes — single species; no AHP or edge DSS |
| Roostaei et al. (2023) | Yes — monitoring only, not integrated with MaxEnt/AHP |
| Onte et al. (2026), Casisirano et al. (2024) | References only — not in background funnel |

### Funnel breaks

- **Site count:** Area says "a selected reforestation site"; Scope dataset card says sensors at "**four proposed reforestation sites**."
- **Roostaei et al. (2023)** appears in Background but **missing from References** (prose/support failure).
- DENR regional matching claim in Background lacks a reference entry matching that policy statement (Forest Management Bureau guides appear only under dataset sources).

### Paragraph-level issues

- Area opening grammar: "forest restoration planning." reads incomplete.
- "Explainable" is developed (Explainability module, SO4) — prior handoff that it is "never developed" **does not hold** on live text.

### Rewrite suggestions

- Fix site count in one place (one pilot site vs four sites) across Area, Scope, and datasets.
- Add Roostaei et al. (2023) to References or replace the in-text citation.
- Cite DENR/FMB source for the site-matching policy sentence.

---

## #156 — Post-Delivery Tomato Shelf-Life Prediction Using Polynomial and Support Vector Regression

**Total: 18/30** — Opening 3, Narrowing 3, Established work 3, Gap 3, Ending 3, Prose 3.

### Funnel map

| Level | Carrier sentence |
| --- | --- |
| Broad problem | "Tomatoes can lose marketable quality before they reach consumers…" |
| Local context | "In the Nueva Ecija–Divisoria market channel, Antolin et al. (2022)…" |
| Established work | Shankaraswamy and Radhika (2024) on polynomial shelf-life modeling — brief |
| Gap | **missing** — no explicit "prior work stops at X; we address Y" sentence |
| Research question | Implicit — post-delivery shelf life from IoT exposure and delivery variables |
| Objectives / contribution | General objective matches IoT + PR vs SVR; dashboard SO present |

### Established-work check

| Prior work | Contrasted? |
| --- | --- |
| Antolin et al. (2022) — postharvest loss context | Partial — sets local problem, not method landscape |
| Shankaraswamy and Radhika (2024) | Partial — method mentioned, limits not contrasted |
| Al-Dairi, Pathare, ElManawy et al. | Mostly reference-list depth only |

### Funnel breaks

- Title leads with Polynomial and SVR before the supply-chain problem.
- Scope: "**Google Maps Routes API**" for traffic-aware routes; dataset card states "**Google Maps Content is excluded from model inputs**" and cites Maps Platform terms — reader cannot tell what the model actually uses.
- Dataset card: "Based on the **supplied Tomortality proposal**" — pasted template breaks narrative cohesion.

### Rewrite suggestions

- Add one background paragraph naming 2–3 shelf-life / cold-chain prediction studies and what each omits (post-delivery, route exposure, Philippine channel).
- Align Scope and dataset cards on whether route features enter the model or only metadata/provenance.
- Retitle toward post-delivery shelf-life decision support; move PR/SVR to subtitle.

---

## #157 — Multivariate IoT Sensor Analytics for Multi-Zone Hydroponic Systems Using Random Forest and Temporal Fusion Transformer

**Total: 17/30** — Opening 4, Narrowing 4, Established work 2, Gap 3, Ending 2, Prose 2.  
**Track note:** Group agreed title (*AquaVir: Multi-Zone Hydroponic Sensor Forecasting and Fault Detection with TFT and Random Forest*, 2026-09-29) differs from ThesisPro wording; flagged as consistency only.

### Funnel map

| Level | Carrier sentence |
| --- | --- |
| Broad problem | "Agriculture in the Philippines is facing numerous challenges from erratic weather, shrinking farmland, and water shortages…" (Climate Adaptation Platform, 2025) |
| Local context | Hydroponics, multi-zone commercial setups, IoT sensors (Chavare et al., 2025) |
| Established work | **Thin in Background** — Phan et al. (2025) cited as "feasibility study" for analytical components; Sportelli et al., Sgueglia et al., Lim et al. only in References |
| Gap | Multivariate multi-zone analytics with anomaly prioritization and forecasting — asserted more than derived from contrast |
| Research question | Data-driven zone behavior, anomalies, prioritization, temporal modeling |
| Objectives / contribution | Four aims bundled in general objective; SO4 merges forecast metrics with RF classification grammar |

### Established-work check

| Prior work | In background funnel? | Contrasted? |
| --- | --- | --- |
| IoT hydroponics monitors (Chavare et al., 2025) | Yes | Partial — sensors named, not compared to multi-zone analytics |
| Phan et al. (2025) | Yes | Mislabeled as "feasibility study" in prose |
| Sportelli et al. (2025) — platform gaps | No | — |
| Sgueglia et al. (2022) — IoT anomaly detection SLR | No | — |
| Lim et al. (2021) — TFT | No | — |
| Pang et al. (2021), Tuli et al. (2022) | No | — |

### Funnel breaks (handoff leads verified)

- Titles/algorithms lead: **confirmed.**
- "ruin entire crops within a few hours": **confirmed**, no citation.
- SO4 garbled: "**TFT forecasts against appropriate time-series baselines to evaluate random-forest classification**…" — **confirmed.**
- Scope: TFT "**investigated as a potential modeling approach**" vs SO2 commits to TFT 24-hour forecasts — **confirmed.**
- Malformed references "**Other authors, N. S. I. P.**" (Ahmed, Hassan, Kumar): **confirmed.**
- Typo in modules list: "`consisting of the following modules:}`" — **confirmed.**
- Explainable title mismatch: N/A for this proposal.

### Rewrite suggestions

- Add a short established-work paragraph: monitoring prototypes (Sportelli et al.), anomaly-detection reviews (Sgueglia et al.), TFT for interpretable forecasting (Lim et al.), then state the integrated multi-zone gap.
- Split SO4 into forecast evaluation vs RF fault-classification evaluation.
- Align Scope and SO2 on TFT commitment or soften SO2.
- Fix Phan citation label; add citation or soften crop-loss sentence.
- Consider aligning ThesisPro title with AquaVir for adviser continuity.

---

## #173 — Integrating Urban Lighting and Crime History for Spatiotemporal Crime Forecasting Using XGBoost in Quezon City

**Total: 22/30** — Opening 3, Narrowing 4, Established work 4, Gap 4, Ending 3, Prose 4.

### Funnel map

| Level | Carrier sentence |
| --- | --- |
| Broad problem | **Weak at global level** — opens with "predictive analytics, spatiotemporal modeling, and public infrastructure planning" then Quezon City |
| Local context | Task Force Streetlighting (Quezon City Government, 2024); crime vs lighting deficiency tension |
| Established work | Chalfin et al. (2022), Giménez-Santana et al. (2026); Du and Ding (2023) on prediction challenges; Makkulawu et al. (2023), Roussel & Böhm (2023) on GIS decision support and geospatial XAI |
| Gap | Decision-support linking forecasts to **verified lighting gaps**, not crime-only or lighting-only rankings |
| Research question | Combined prioritization for streetlight **placement** |
| Objectives / contribution | General objective: "**explainable streetlight placement recommendations**… using nighttime crime forecasts and verified lighting gaps" |

### Established-work check

| Prior work | Contrasted? |
| --- | --- |
| Du and Ding (2023) — sparsity, interpretability, weak DSS use | Yes |
| Crime prediction / XGBoost literature (Shwartz-Ziv & Armon, 2022) | Partial — method justification |
| Agila (archive) ARIMA crime mapping Manila | Not cited in proposal text |

### Funnel breaks

- **Title vs ending:** Title stresses "**Spatiotemporal Crime Forecasting Using XGBoost**"; general objective is a **streetlight placement** DSS (forecasting is means, not the stated end).
- **SDGSAT role:** Crime preprocessing "**spatial matching with SDGSAT-1 Glimmer**" and segment-level light extraction vs Limitations: satellite brightness "**supplementary**… not a substitute for site-level lighting assessment" — **confirmed** tension; funnel should state primary vs supplementary once.

### Rewrite suggestions

- Open with national urban safety or crime-concentration evidence (e.g. Weisburd et al., 2024 already in references), then Quezon City.
- Retitle to foreground streetlight placement DSS; keep XGBoost forecasting in subtitle.
- One sentence in Scope or Limitations on whether SDGSAT drives gap assessment or only contextual validation.

---

## Handoff leads — confirm / drop

| Lead | Verdict |
| --- | --- |
| Four titles lead with algorithms | **Confirmed** (#144–#157, #173) |
| #144 title causation vs limitations | **Confirmed** |
| #144 SO5 DTI collaboration | **Confirmed** |
| #157 SO4 garbled, TFT scope, crop hours, Phan label, bad refs, AquaVir title | **Confirmed** |
| #173 forecast title vs placement objective; SDGSAT supplementary vs preprocessing | **Confirmed** |
| #153 one vs four sites; Roostaei missing from refs; DENR uncited | **Confirmed** |
| #153 explainable never developed | **Dropped** — SO4 and modules address explainability |
| #156 Google Maps vs dataset exclusion; Tomortality paste | **Confirmed** |

---

*Word counts (proposal sections only): #144 470; #153 355; #156 298; #157 452; #173 326 (all under 700).*
