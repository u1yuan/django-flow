# AquaVir TFT — arXiv search findings

Skill used: `docs/activities/litReview/.agents/skills/literature-search-arxiv` (`scripts/search_arxiv.py` only).  
Window: `submittedDate:[201801010000 TO 202609292359]` (2018-01-01 through 2026-09-29).  
No HTTP 406 on these runs. Abstract-only; no PDFs downloaded.

Paper URLs used for these findings:

- https://arxiv.org/abs/2512.11852
- https://arxiv.org/abs/2511.00552
- https://arxiv.org/abs/2301.05911
- https://arxiv.org/abs/2511.19090

Raw JSON: `ax-tft-1.json`, `ax-tft-2.json`, `ax-tft-3.json` under this `raw/` folder.

---

## Query 1 — TFT + hydroponic / greenhouse / nutrient / CEA sensor forecasting

**Query:**

```text
(all:"Temporal Fusion Transformer" OR all:TFT) AND (all:hydroponic OR all:greenhouse OR all:"nutrient solution" OR all:"controlled environment" OR all:"controlled-environment") AND (all:forecast OR all:forecasting OR all:sensor) AND submittedDate:[201801010000 TO 202609292359]
```

**Result count:** 1  
**Raw:** `ax-tft-1.json`

| Title | id | Hydroponics in abstract? | Sensor target in abstract? | TFT in abstract? | Metric in abstract? |
| --- | --- | --- | --- | --- | --- |
| Explainable AI for Smart Greenhouse Control: Interpretability of Temporal Fusion Transformer in the Internet of Robotic Things | 2512.11852v1 | No (greenhouse only) | Yes — names temperature, humidity, CO₂, light, outer climate as sensor inputs; modeled output is actuator control settings, not sensor forecasts | Yes | Yes — 95% test accuracy |

Abstract-only note: this hit is greenhouse actuator control with TFT explainability, not hydroponic nutrient-solution forecasting.

---

## Query 2 — TFT vs LSTM, multi-horizon / environmental / sensor forecasting

**Query:**

```text
(all:"Temporal Fusion Transformer" OR all:TFT) AND all:LSTM AND (all:"multi-horizon" OR all:"multi horizon" OR all:environmental OR all:sensor) AND (all:forecast OR all:forecasting) AND submittedDate:[201801010000 TO 202609292359]
```

**Result count:** 3  
**Raw:** `ax-tft-2.json`

| Title | id | Hydroponics in abstract? | Sensor target in abstract? | TFT in abstract? | Metric in abstract? |
| --- | --- | --- | --- | --- | --- |
| Temporal Fusion Transformer for Multi-Horizon Probabilistic Forecasting of Weekly Retail Sales | 2511.00552v1 | No | No (weekly retail sales; temperature is an exogenous signal) | Yes | Yes — RMSE, R²; abstract also says TFT outperforms LSTM among baselines |
| Day-Ahead PV Power Forecasting Based on MSTL-TFT | 2301.05911v2 | No | No explicit sensor target (day-ahead PV power; meteorological factors named) | Yes | No named numeric metric (claims “more accurate” vs BP, LSTM, XGBoost, etc.) |
| Optimization of Deep Learning Models for Dynamic Market Behavior Prediction | 2511.19090v1 | No | No (per-SKU retail demand/revenue) | Yes (benchmark among transformers) | Yes — MAE, RMSE, sMAPE, MASE, Theil’s U₂; LSTM/GRU among baselines |

None of these three abstracts name hydroponics.

---

## Query 3 — TFT vs LSTM, environmental / sensor / greenhouse / hydroponic (tighter)

**Query:**

```text
(all:"Temporal Fusion Transformer" OR all:TFT) AND all:LSTM AND (all:environmental OR all:sensor OR all:greenhouse OR all:hydroponic) AND (all:forecast OR all:forecasting) AND submittedDate:[201801010000 TO 202609292359]
```

**Result count:** 1  
**Raw:** `ax-tft-3.json`

| Title | id | Hydroponics in abstract? | Sensor target in abstract? | TFT in abstract? | Metric in abstract? |
| --- | --- | --- | --- | --- | --- |
| Day-Ahead PV Power Forecasting Based on MSTL-TFT | 2301.05911v2 | No | No explicit sensor target (PV + meteorological factors) | Yes | No named numeric metric (comparative “more accurate” vs LSTM and others) |

---

## Plain outcome

- arXiv API calls **succeeded** (not HTTP 406).
- **Zero** abstracts name hydroponics.
- **One** domain-adjacent greenhouse TFT hit (`2512.11852v1`): sensors named as inputs; target is actuator settings with 95% accuracy — abstract-only.
- TFT-vs-LSTM hits are retail multi-horizon sales and PV day-ahead forecasting, not hydroponic / nutrient-solution sensor series.
