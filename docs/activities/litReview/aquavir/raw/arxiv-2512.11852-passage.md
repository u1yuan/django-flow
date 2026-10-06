# Passage extract — arXiv 2512.11852

**Title:** Explainable AI for Smart Greenhouse Control: Interpretability of Temporal Fusion Transformer in the Internet of Robotic Things  
**Authors:** Muhammad Jawad Bashir, Shagufta Henna, Eoghan Furey  
**Year:** 2025 (arXiv posted 2025-12-04; note: Accepted in 36th Irish Signals and Systems Conference, ISSC 2025)  
**arXiv id:** 2512.11852 (opened as `2512.11852`; HTML version; abs/pdf equivalents: https://arxiv.org/abs/2512.11852, https://arxiv.org/pdf/2512.11852)  
**What was opened:** Full text via arXiv HTML — https://arxiv.org/html/2512.11852 (not abstract-only).

This note answers only from that opened full text. It is **not** an AquaVir performance result and **not** claimed here as a hydroponic nutrient-solution forecasting study unless the passage itself says so.

---

## Five answers (from opened full text)

### 1. Does it name hydroponics or a nutrient solution?

**No hydroponics.** The opened text does not use “hydroponic(s)” or “nutrient solution.”

It does use related greenhouse / drainage language: “nutrient flow features” (Conclusion), “nutrient levels” (local LIME discussion for one actuator class), and feature name `EC_drain_PC` described as electrical conductivity in drainage (Results §V-D1). Domain framing is **smart / autonomous greenhouse** (Autonomous Greenhouse Challenge cherry-tomato data), not hydroponics as a named system.

### 2. What is the prediction or control target?

**Actuator settings / actuator commands** for greenhouse control.

The study uses TFT to map multivariate sensor inputs to **actuator states** (framed as classification of actuator setting classes). Sixteen actuators were clustered into **six setting classes**; the model predicts those classes. Network / problem sections state the goal as predicting optimal **actuator commands** from sensor measurements.

### 3. Does it forecast sensor series (pH, EC, temperature, humidity, water level, light) or something else?

**Something else: actuator control settings (commands / classes), not forecasts of sensor time series as the model output.**

Sensors (e.g. temperature, humidity, CO₂, light, outer climate, plus greenhouse sensors including irrigation-related and drainage EC among others) are **inputs**. The modeled output is **actuator control / setting classes** (heating, ventilation, CO₂ dosing, irrigation schedules, lighting, curtains, etc.), not next-step forecasts of pH, EC, temperature, humidity, water level, or light as targets.

### 4. What metric does the opened passage state, with the comparator if named?

**Stated metrics for this TFT model (no competing baseline model named against these numbers):**

- **Test / classification accuracy of 95%** (abstract; also “classification accuracy of 95%” in Introduction and Conclusion) on a class-imbalanced actuator-control dataset.
- Training accuracy reaching **97%**; validation accuracy approaching **95%** (§V-C).
- Class-wise **F1-Score exceeding 0.88** (§V-C).

**Comparator:** The results section does **not** name a baseline model (e.g. LSTM, RF) against which this 95% accuracy is compared. Related work cites other LSTM / greenhouse papers, but those are not reported as head-to-head metrics for this experiment.

### 5. Is TFT compared with LSTM?

**No empirical TFT-vs-LSTM comparison** for this greenhouse actuator task.

LSTM appears as (a) an **internal TFT component** (LSTM encoder in Algorithm 1 / §IV-A) and (b) **related work** on other greenhouse forecasting systems. The opened Results do not report a side-by-side accuracy (or other metric) of TFT versus a standalone LSTM baseline.

---

## Integrity note

Do not treat this paper as AquaVir empirical performance, as hydroponic pH/EC sensor forecasting, or as a TFT-vs-LSTM bake-off unless a later verified source states that. This extract is limited to what the opened HTML full text of arXiv 2512.11852 says.
