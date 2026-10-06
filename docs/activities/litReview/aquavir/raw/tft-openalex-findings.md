# OpenAlex TFT search findings (AquaVir)

Search date: 2026-09-29  
Scope: OpenAlex only, via `docs/activities/litReview/.agents/skills/literature-search-openalex` CLI.  
Window: English works, 2018-01-01 through 2026-09-29, not retracted.  
Raw JSON: `docs/activities/litReview/aquavir/raw/oa-tft-*.json`  
This note does not update the evidence ledger, search log, dual-model justification, TA3 proposal, or AI interaction log.

## Queries and counts

| ID | File | Filter summary | Indexed | First-page titles screened |
| --- | --- | --- | ---: | ---: |
| OA-TFT-domain | `oa-tft-domain.json` | title/abstract "Temporal Fusion Transformer"; abstract hydroponic \| greenhouse \| nutrient \| "controlled environment" | 97 | 10 |
| OA-TFT-vs-lstm | `oa-tft-vs-lstm.json` | title/abstract "Temporal Fusion Transformer"; abstract LSTM \| "long short-term memory" | 962 | 10 |
| OA-TFT-sensor-env | `oa-tft-sensor-env.json` | title/abstract "Temporal Fusion Transformer"; abstract sensor \| environmental \| multi-horizon \| greenhouse \| hydroponic | 922 | 10 |
| OA-TFT-hydro | `oa-tft-hydro.json` | title/abstract "Temporal Fusion Transformer"; abstract hydroponic \| aquaponic(s) \| soilless \| "nutrient solution" | **3** | **3** (complete set) |
| OA-TFT-greenhouse | `oa-tft-greenhouse.json` | title/abstract greenhouse; abstract TFT \| "Temporal Fusion Transformer" | 21 | 10 |

Sort on all calls: `cited_by_count:desc`. Per page: 10.

### Screening note on bag-of-words hits

OA-TFT-domain and OA-TFT-greenhouse pull many false positives (for example "greenhouse gases," urban energy "CityTFT," surveillance video, TFT-LCD manufacturers). Those were title- or abstract-screened out of the on-topic shortlist. OA-TFT-vs-lstm and OA-TFT-sensor-env are dominated by electricity, PV, load, traffic, and emotion-recognition papers.

## Hydroponic TFT result

**No opened paper applies TFT to a hydroponic (nutrient-solution) EC, pH, or multi-zone hydroponic sensor forecast.**

The only complete OpenAlex set for TFT plus hydroponic / aquaponic / soilless / nutrient-solution language is OA-TFT-hydro (**3** works):

1. Metin, Kaşif, and Catal (2023) — aquaponics nitrate forecast (opened; see below). Aquaponics is described as merging hydroponics with aquaculture; it is **not** a pure hydroponic EC/pH multi-zone study.
2. Chaudhary and colleagues (2026), https://doi.org/10.1007/s41870-025-03020-y — title names IoT smart farming and a hybrid deep model; **no abstract** in the saved OpenAlex record → **lead**.
3. Sarvakar, Patel, and Yadava (2026), https://doi.org/10.1201/9781003637264-9 — plant/crop disease chapter; wrong task → excluded.

## Closest opened sources (2–3)

### 1. Metin, Kaşif, and Catal (2023) — aquaponics nitrate with TFT

| Field | Value |
| --- | --- |
| Bibliographic | Metin, A., Kaşif, A., & Catal, C. (2023). Temporal fusion transformer-based prediction in aquaponics. *The Journal of Supercomputing*. Published 6 June 2023. |
| DOI | https://doi.org/10.1007/s11227-023-05389-8 |
| OpenAlex | in `oa-tft-hydro.json`, `oa-tft-domain.json` |
| What was opened | Publisher HTML (Springer Nature Link article page), including abstract, methods (dataset, baselines, metrics), results discussion, and conclusions. Full numeric cells of Tables 4–6 were not extracted from the HTML table widgets. |
| Status | **Opened passage** (not abstract-only). |
| Task as stated | Forecast **nitrate** levels in an **aquaponics** environment (soilless system merging hydroponics and aquaculture). Dataset: Ogbuokiri / Udanor et al. labelled aquaponics fish-pond water-quality sensors (temperature, turbidity, dissolved oxygen, pH, ammonia, nitrate, plus fish physical attributes); nine freshwater catfish ponds; resampled to 60 s; 421,140 chronological points; 90/8/2 train/validation/test. |
| Baselines named | ELM; LSTM; Encoder–Decoder LSTM; Attention LSTM; TFT. |
| Metrics named | MAE, MSE, Explained Variance, RMSE, R²; one-hour sequences emphasized in the abstract. |
| Passage claims used here | Abstract: TFT was proposed and validated for nitrate forecast; experimental results show significant improvements over baseline models in MAE, MSE, and Explained Variance for one-hour sequences. Conclusions: proposed model provided **0.0322 MSE** for predicting nitrate; TFT outperforms baselines on the metrics in Table 4; performance worsens as the forecasting period lengthens; sequences longer than one hour become impractical for attention memory. |
| Caveat | Aquaponics nitrate, not hydroponic multi-zone EC/pH. Does **not** establish AquaVir facility performance. Per-method MAE/RMSE from Table 4 were not re-read as individual numbers from the HTML tables. |

### 2. López Santos and colleagues (2022) — TFT vs LSTM on multi-horizon environmental / PV series

| Field | Value |
| --- | --- |
| Bibliographic | López Santos, M., García-Santiago, X., Echevarría Camarero, F., Blázquez Gil, G., & Carrasco Ortega, P. (2022). Application of Temporal Fusion Transformer for day-ahead PV power forecasting. *Energies, 15*(14), 5232. |
| DOI | https://doi.org/10.3390/en15145232 |
| OpenAlex | in `oa-tft-vs-lstm.json`, `oa-tft-sensor-env.json` |
| What was opened | Publisher HTML (MDPI), including abstract, methods, results text around Tables 7–8, and conclusions. |
| Status | **Opened passage**. |
| Task as stated | Predict **hourly day-ahead PV power** at six facilities (Germany and Australia) using meteorological, solar-angle, and calendar inputs. |
| Comparators | ARIMA, MLP, LSTM, XGBoost, TFT. |
| Metrics | RMSE, MAE, MASE, R² (and quantile loss for TFT). |
| Passage claims used here | Abstract and results: TFT is more accurate than the other algorithms for PV generation at these facilities. Table 7 (Germany / Australia columns as printed): **TFT** RMSE 0.276 / 0.064, MAE 0.120 / 0.033, MASE 0.390 / 0.100, R² 0.983 / 0.998; **LSTM** RMSE 0.343 / 0.118, MAE 0.162 / 0.064, MASE 0.846 / 0.191, R² 0.975 / 0.994. Conclusions: TFT outperformed the other models for PV energy production in the six facilities. |
| Caveat | Photovoltaic power, **not** hydroponic sensors. Supports a TFT-versus-LSTM comparison on multi-horizon environmental series only in that PV setting. Do not quote these errors as AquaVir performance. |

### 3. Lim and colleagues (2021) — TFT architecture (sensor-env hit; design only)

| Field | Value |
| --- | --- |
| Bibliographic | Lim, B. Y., Arık, S. Ö., Loeff, N., & Pfister, T. (2021). Temporal Fusion Transformers for interpretable multi-horizon time series forecasting. *International Journal of Forecasting*. |
| DOI | https://doi.org/10.1016/j.ijforecast.2021.03.012 |
| OpenAlex | top hit in `oa-tft-sensor-env.json` (also arXiv preprint DOI `10.48550/arxiv.1912.09363` in the same file) |
| What was opened | OpenAlex reconstructed abstract only in this pass (full design-passage reading of static covariates / known future inputs / historical observations was **not** completed here). |
| Status | **Abstract-only** for this OpenAlex deliverable. |
| Task / claim from abstract | Introduces TFT for multi-horizon forecasting with static covariates, known future inputs, and past-only exogenous series; reports performance improvements on real-world datasets (datasets not hydroponic). |
| Caveat | Architecture paper. Not domain evidence for hydroponics. |

## What these searches do **not** support

- No claim that TFT beat LSTM (or XGBoost) on **hydroponic** EC/pH or multi-zone nutrient-solution data.
- Metin’s TFT-over-LSTM result is for **aquaponics nitrate**, one-hour sequences, on a published pond water-quality dataset.
- López Santos’s TFT-over-LSTM result is for **day-ahead PV power**.
- No facility AquaVir MAE/RMSE or fault scores appear in these OpenAlex results.

## Leads not opened as evidence

- Chaudhary et al. (2026), https://doi.org/10.1007/s41870-025-03020-y — IoT smart-farming hybrid DL title; abstract missing in OpenAlex → **lead**.
- Nazir et al. (2023), https://doi.org/10.1016/j.rineng.2023.100888 — TFT vs LSTM/TCN on smart-grid energy demand (abstract in `oa-tft-vs-lstm.json`); off-domain for AquaVir sensors; not opened beyond abstract text in the JSON.
- Frison et al. (2024), https://doi.org/10.1016/j.energy.2024.132745 — DHN heat demand; mentions greenhouses as heat sinks; CNN beat TFT on MAPE in the abstract → not a hydroponic TFT win.

## Paper URLs used

- https://doi.org/10.1007/s11227-023-05389-8 (Metin et al.; Springer HTML opened)
- https://doi.org/10.3390/en15145232 (López Santos et al.; MDPI HTML opened)
- https://doi.org/10.1016/j.ijforecast.2021.03.012 (Lim et al.; abstract via OpenAlex only in this pass)
