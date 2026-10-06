# Lim et al. (2021) — design-claim passages

**Citation:** Lim, B., Arık, S. Ö., Loeff, N., & Pfister, T. (2021). Temporal Fusion Transformers for interpretable multi-horizon time series forecasting. *International Journal of Forecasting*, 37(4), 1748–1764. https://doi.org/10.1016/j.ijforecast.2021.03.012

**Opened sources (this extraction):**

| Attempt | URL | Result |
| --- | --- | --- |
| Publisher DOI | https://doi.org/10.1016/j.ijforecast.2021.03.012 | Failed (fetch timed out) |
| Publisher HTML | https://www.sciencedirect.com/science/article/pii/S0169207021000637 | Failed (Cloudflare / access error page; full text not readable) |
| Open-access full text | https://ar5iv.labs.arxiv.org/html/1912.09363 | Opened successfully (HTML full text of arXiv:1912.09363, same authors/title as the IJF article) |

**Scope note:** Passages below support architectural design claims in Lim et al. They do **not** claim that this paper tested hydroponic sensors or AquaVir facility data. Evaluation domains in the opened text are general real-world forecasting datasets (e.g. retail, electricity, traffic, volatility), not AquaVir.

**Extraction status:** Full-text (open-access ar5iv), not abstract-only.

---

## 1. Multi-horizon outputs

- **Locator opened:** §1 Introduction (opening paragraphs); §3 Multi-horizon Forecasting (Eq. 1 and surrounding text); Abstract
- **Paraphrase:** The paper defines multi-horizon forecasting as predicting the target at many future steps at once, and TFT is trained to emit forecasts for a set of horizons \(\tau \in \{1,\ldots,\tau_{\max}\}\) simultaneously (direct multi-step outputs, including quantile forecasts at each horizon).

**Supported by opened passage:** yes

---

## 2. Static covariates

- **Locator opened:** §1 Introduction (Fig. 1 discussion); §3 Multi-horizon Forecasting (entity static covariates \(\bm{s}_i\)); §4.3 Static Covariate Encoders
- **Paraphrase:** Each entity can carry time-invariant static metadata. TFT uses dedicated static covariate encoders (GRNs) to produce context vectors that condition variable selection and temporal processing elsewhere in the network.

**Supported by opened passage:** yes

---

## 3. Known future inputs

- **Locator opened:** §1 Introduction (Fig. 1; “known information about the future”); §3 Multi-horizon Forecasting (known inputs \(\bm{x}_{i,t}\)); §4 Model Architecture (Fig. 2 caption)
- **Paraphrase:** Time-dependent inputs are split so that *known* inputs can be predetermined into the future (examples given include calendar features such as day-of-week or holidays). The forecast equation uses known inputs from the look-back window through the forecast horizon \(t+\tau\).

**Supported by opened passage:** yes

---

## 4. Historical observations

- **Locator opened:** §1 Introduction (past-observed / exogenous series observed only in the past); §3 Multi-horizon Forecasting (observed inputs \(\bm{z}_{i,t}\)); §4.5.1 Locality Enhancement (encoder over past selected features)
- **Paraphrase:** *Observed* inputs are exogenous series measurable only at each step and unknown beforehand. The model conditions on a finite look-back of past targets and past observed inputs up to forecast start time \(t\), while known inputs may extend beyond \(t\).

**Supported by opened passage:** yes

---

## 5. Variable selection / interpretability

- **Locator opened:** Abstract; §1 Introduction (three interpretability use cases); §4.2 Variable Selection Networks; §4.4 Interpretable Multi-Head Attention
- **Paraphrase:** TFT applies instance-wise variable selection networks (with Softmax weights) to static and time-dependent inputs to emphasize salient features and down-weight noisy ones. Interpretable multi-head attention and related components are presented so users can inspect globally important variables, persistent temporal patterns, and significant events—not only black-box forecasts.

**Supported by opened passage:** yes

---

## Claim support summary

| Design claim | Supported by opened full-text passage? |
| --- | --- |
| Multi-horizon outputs | Yes |
| Static covariates | Yes |
| Known future inputs | Yes |
| Historical observations | Yes |
| Variable selection / interpretability | Yes |
