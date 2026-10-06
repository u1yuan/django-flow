# AquaVir random-forest arm (draft)

Drafted: 2026-09-29  
Scope: supervised sensor-fault detection only. Sources limited to ledger row S2 and the opened Karimzadeh passages in `algorithm-review.md`. No new literature search. No second hydroponic random-forest study is claimed.

## Dual-pipeline role

AquaVir uses two separate paths:

1. **Random forest (this arm)** — classifies **labeled** sensor faults (normal versus faulty readings, and fault type if diagnosis is in scope). It is a supervised detector. Without verified normal and fault labels, it cannot be trained or validated.
2. **TFT forecast deviations (separate arm)** — absolute forecast–observation deviations may be **ranked for operator review** by size, persistence, affected variables, and zones. That ranking is a descriptive review aid. It is **not** a trained fault detector and does **not** confirm a physical or sensor fault.

Validated random-forest classifications, when labels exist, must be reported separately from unconfirmed TFT review signals. This matches the 2026-09-29 model decision and the TA3 Anomaly Detection / Review Prioritization / Predictive Analysis modules: random forest only when verified labels are available; otherwise deviations stay unconfirmed review signals.

## Opened evidence (S2 only)

**Source.** Karimzadeh, S., Li, Z., & Ahamed, M. S. (2025). Machine learning-based fault detection and diagnosis of electrical conductivity and pH sensors in hydroponic systems. *Computers and Electronics in Agriculture, 237*, 110544. https://doi.org/10.1016/j.compag.2025.110544

**What was opened.** Publisher article HTML: highlights, abstract, introduction, experimental-setup snippet, conclusion snippet. Result tables behind the paywall were **not** opened. Status: verified for the opened HTML only (ledger S2).

**Setting.** One closed-loop NFT lettuce system (two racks, 70 butterhead lettuce heads, UC Davis; transplant 30 Aug 2023, harvest 23 Sep 2023). Faults were **artificially induced and labeled**: bias, drift, precision degradation, spike, and stuck.

**Models compared.** SVM, KNN, ANN, RF, LSTM.

**Abstract detection figures (not recomputed).** Random-forest fault detection accuracy **93.7% (EC)** and **96.5% (pH)**. The same abstract also states high diagnosis accuracies for several fault types and an ANN-versus-SVR comparison for sensor-independent EC checks (93.2% versus 49.4%). Those diagnosis and ANN/SVR figures are abstract text only; full diagnosis tables were not opened.

## What this does and does not support for AquaVir

| Supported as design precedent | Not supported |
| --- | --- |
| Supervised random forest is a documented hydroponic approach for **labeled** EC/pH sensor fault detection and diagnosis. | Unsupervised anomaly detection on unlabeled multi-zone nutrient sensors. |
| If the group later obtains verified fault labels, random forest is the algorithm to implement; KNN is the simpler baseline already in that comparison. | That Karimzadeh accuracies are AquaVir performance. |
| If labels are absent, state that the supervised detector **cannot be validated**; keep TFT deviations as review signals only. | A second opened hydroponic random-forest fault study (none is claimed here). |
| | Cross-zone consistency or unlabeled operating-anomaly detection as a random-forest result. |

## Claim map

| Claim | Source | Locator status | Caveat |
| --- | --- | --- | --- |
| Random forest is AquaVir’s planned supervised classifier for labeled sensor faults; TFT forecast deviations are a separate review ranking and are not confirmed faults | Model decision 2026-09-29; TA3 §1 Anomaly Detection, Review Prioritization, and Predictive Analysis modules | Project design text (not a paper result) | Design choice. No facility labels or RF run on AquaVir data. |
| Models compared included SVM, KNN, ANN, RF, and LSTM | S2 Karimzadeh et al. 2025 | Abstract / introduction on publisher HTML | Agent-opened HTML. Not human-confirmed. |
| Abstract reports RF fault detection accuracy 93.7% (EC) and 96.5% (pH) | S2 | Abstract on publisher HTML | Abstract figures only. Result tables not opened; not recomputed. Not AquaVir performance. |
| Faults were artificially induced and labeled (bias, drift, precision degradation, spike, stuck) on one NFT lettuce system | S2 | Abstract, introduction, experimental-setup snippet on publisher HTML | One system, two racks, 70 heads, Aug–Sep 2023. Injected labels ≠ operator-confirmed facility events. |
| Abstract reports high RF/SVM diagnosis accuracies for several EC/pH fault types; ANN 93.2% vs SVR 49.4% for sensor-independent EC fault detection | S2 | Abstract on publisher HTML | Diagnosis tables not opened. Quote only as abstract text until tables are opened. |
| This method is not an unsupervised anomaly detector | S2; algorithm review AlgoA section | Method description in opened HTML / review synthesis | Supervised classification. Does not fill the unlabeled AlgoA gap. |
| If verified fault labels are absent, the random-forest detector cannot be validated | Model decision; algorithm review “What the thesis still has to obtain”; TA3 limitations | Project constraint | No AquaVir fault-label file is confirmed on disk. |
| A second hydroponic random-forest fault-detection study supports the same result | None | Not opened | **Not claimed.** Do not invent a second study. |
| Random forest (or any detector) was evaluated on AquaVir facility data | None | No data file | **Not claimed.** |

## Gaps left for this arm

- Paywalled result tables for Karimzadeh et al. (2025) remain unopened; diagnosis numbers stay abstract-only.
- No verified AquaVir fault-label file exists in the repository, so supervised validation is blocked until labels are obtained.
- No second hydroponic random-forest fault study was opened; the arm rests on S2 alone for hydroponic RF evidence.

## Reference

Karimzadeh, S., Li, Z., & Ahamed, M. S. (2025). Machine learning-based fault detection and diagnosis of electrical conductivity and pH sensors in hydroponic systems. *Computers and Electronics in Agriculture, 237*, 110544. https://doi.org/10.1016/j.compag.2025.110544
