---
type: note
project: "[[Thesis]]"
track: hydroponics
related: "[[AquaVir algorithm review]]"
tags:
  - thesis
  - note
created: 2026-09-28
---

# AquaVir research gaps

> **Current project decision (2026-09-29):** The group selected TFT for multi-sensor forecasting and plans random forest fault detection if verified labels become available. This note's LSTM EC discussion remains a dated evidence-gap assessment. See `docs/activities/litReview/aquavir/model-decision-2026-09-29.md`.

**Track:** hydroponics
**Date:** 2026-09-28
**QA status:** pass with limitations, after one revision and one follow-up review on 2026-09-28

This note ranks research gaps in the opened AquaVir algorithm review so the group can draft a statement of the problem. It adds no new search and no facility analysis. Paths below are pointers. A path is not a verified citation. Passages were opened by an agent. A person in the group still has to confirm each locator before the text is course-final.

Source review: [[AquaVir algorithm review]]. Repository path: `docs/activities/litReview/aquavir/algorithm-review.md`
Evidence ledger: [[AquaVir evidence ledger]]. Repository path: `docs/activities/litReview/aquavir/evidence-ledger.md`

## Shared constraint

Three zones and about 10,000 rows are the feasibility hope in that review. They are not a confirmed export. No hydroponic file is on disk. That constraint is stated once here. It does not set every feasibility score to 1.

## How the scores work

Each research gap has two integers from 1 to 5. These are rubric judgments on 2026-09-28. They are not measurements from a facility dataset.

**Priority**

- 5: opened hydroponic work does not answer the gap, and the gap is central to the AquaVir decision (scarce anomaly labels, no harvest label, nutrient-solution sensors, more than one zone).
- 3: a method was opened, and the opened setting is a different setting from the one this gap asks about.
- 1: the review already rejected that target.

**Feasibility for this group**

- 5: an opened method can be used without new labels once a minimal export exists.
- 3: the gap needs the unconfirmed multi-zone export, and it does not need fault labels or harvest labels.
- 2: the gap can be named without choosing a detector, and filling it with a method would require a detector this review did not open.
- 1: the gap needs fault labels or harvest labels, or stating the gap would require naming a detector the review did not open.

Sort by priority descending, then feasibility descending. The same priority keeps the higher feasibility first.

One ledger check changed an expected feasibility score. Short-horizon EC transfer was expected at feasibility 3. The ledger asks for enough hourly EC history before an LSTM is fit. It does not require more than one zone for that method. Moon, Ahn, and Son (2018) used one cultivation line (S1). That matches feasibility 5. The rank stays third because priority is 3. The statement of the problem still comes only from rank 1.

## Ranked research gaps

| Rank | Gap | Priority | Feasibility | Evidence the score uses |
| --- | --- | --- | --- | --- |
| 1 | Cross-zone consistency and anomaly prioritization | 5 | 3 | No opened passage evaluates cross-zone consistency. S1 is one line. S2 is one NFT system and is not an unlabeled zone-consistency detector. |
| 2 | Unsupervised detection of unlabeled operating anomalies on nutrient-solution sensors | 5 | 2 | AlgoA has no opened unsupervised winner on hydroponic nutrient sensors. Filling that slot would name a detector the review did not open. |
| 3 | Transfer of short-horizon nutrient-solution EC forecasting past the single opened full text | 3 | 5 | S1 opened an LSTM for hourly root-zone EC with no harvest label. A persistence baseline (repeat the last hourly EC) is the comparison the review already names. S4 is not an EC source. |
| 4 | Fault detection from operator-confirmed events | 3 | 1 | S2 opened supervised random forest for injected, labeled EC and pH faults. Operator-confirmed events are a different label source. This file of labels is not on disk. |
| 5 | Yield prediction, or a dosing or pH-intervention class, from the AquaVir sensor list | 1 | 1 | The review rejected both as the prediction target. S3 needs a harvest weight and plant measurements. No opened paper predicted a dosing class from the zone-sensor list. |

Rank 1 is the only source of the statement of the problem below. Ranks 2 through 5 stay in this matrix.

### Rank 1. Cross-zone consistency and anomaly prioritization

The opened nutrient-solution studies are S1 and S2. Moon, Ahn, and Son (2018) forecast hourly root-zone EC on one closed-loop sweet-pepper line and do not use a harvest label (S1). Karimzadeh, Li, and Ahamed (2025) detect injected EC and pH sensor faults on one NFT system with two racks, and those faults were labeled (S2). The ledger states that S2 is not an unlabeled zone-consistency detector. The review states that nothing opened evaluates cross-zone consistency, and that zone ranking remains a thesis problem. S3, S4, and S5 stay in the later ranks.

Priority is 5 because that comparison is unanswered in the opened set and it is the multi-zone part of the AquaVir decision. Feasibility is 3 because a real answer needs a multi-zone export with zone identifiers, and the questions do not require fault labels or a harvest label. This rank does not name an anomaly detector. AlgoA stays unresolved.

### Rank 2. Unsupervised nutrient-sensor anomalies

The review found no unsupervised detector that met the two-source bar on hydroponic nutrient sensors. The strongest opened hydroponic anomaly result is supervised random forest, and it needs fault labels (S2). Shu and Yang (2026) flag labeled anomalies in greenhouse light, temperature, humidity, and CO₂ (S5). Those sensors are not nutrient-solution pH or EC, so S5 does not name AlgoA. Isolation forest, reconstruction autoencoders, and change-point detectors were not in an opened hydroponic passage.

Priority is 5 because unlabeled nutrient-sensor detection is unanswered and central. Feasibility is 2 because the absence can be stated here, while a method claim would name a detector the review did not open. This rank is separate from rank 1: rank 1 asks how zones compare and which period an operator should handle first; rank 2 asks which detector to use. The statement of the problem does not answer rank 2.

### Rank 3. Short-horizon EC forecast beyond one opened full text

S1 is the only opened full text that forecasts a nutrient-solution series AquaVir expects to have. The test fit in that paper is weaker than the validation fit, on a held-out week from the same line. Eraliev and Lee (2023) are abstract-only and forecast air temperature, humidity, and CO₂ (S4). That abstract is not a second EC source.

Priority is 3 because LSTM was opened and the open question is transfer to a new series, not the absence of a method. Feasibility is 5 because that opened method, with a persistence baseline, needs no harvest label and no fault label once an hourly EC series exists. Multi-zone structure is rank 1's requirement.

### Rank 4. Operator-confirmed fault detection

S2 reports a supervised comparison on faults that were artificially induced and labeled: bias, drift, precision degradation, spike, and stuck. The abstract's detection figures were opened. The paywalled result tables were not opened, so those figures stay the abstract's figures. The review treats injected faults as different from operator-confirmed events.

Priority is 3 because random forest was opened for the injected-fault setting. Feasibility is 1 because this gap needs a label file AquaVir does not have. Random forest remains the algorithm to implement only if the group later labels faults. It is not the primary detector for unlabeled zone data.

### Rank 5. Yield or dosing class

Mokhtar and colleagues (2022) predict lettuce fresh weight from leaf number, water consumption, dry weight, stem length, and stem diameter (S3). Those inputs are not the AquaVir list of pH, EC/TDS, solution temperature, water level, and humidity. The target needs a harvest weight. No opened paper predicted a dosing or pH-intervention class from multivariate zone sensors. The review did not select either target.

Priority is 1 because the review rejected the target. Feasibility is 1 because a yield answer needs harvest measurements that are not on disk. This rank is not a second problem statement.

## Statement of the problem

Draft for Chapter 1. It uses rank 1 only. It reports no facility result and names no detector.

Moon, Ahn, and Son (2018) forecast hourly root-zone electrical conductivity on one closed-loop sweet-pepper line and do not use a harvest label. Karimzadeh, Li, and Ahamed (2025) detect injected electrical-conductivity and pH sensor faults on one NFT system; those faults were labeled. Neither passage evaluates whether zones are consistent with one another, or which anomalous period an operator should handle first. The study condition for that question is separate from S2's labels: harvest labels are unavailable, and anomaly labels are expected to be scarce.

Specifically, this study seeks to answer the following questions:

1. How can a baseline for each zone be formed from whichever of pH, EC/TDS, solution temperature, water level, and humidity a facility export contains, when no harvest label is available?
2. How can those baselines be compared so that zones are ranked by consistency with one another?
3. How can anomalous periods be prioritized for operator follow-up when fault labels are scarce?

Answering these questions waits on a facility export with timestamps and zone identifiers. That export is not on disk. AlgoA remains unresolved, and this draft does not fill it.

## Holistic gap after the 2026-09-29 expansion

The expansion does not replace this draft. It asks whether Philippine work, or methods other than the LSTM and random-forest pair, already answer rank 1. They do not. Forecasting, labeled fault detection, fuzzy setpoint dosing, ion estimation, yield, leaf images, and greenhouse air each address a single system or a different target. No opened passage compares zones or prioritizes an unlabeled nutrient-solution period. An OpenAlex query for multi-zone language in English hydroponic abstracts, through 2026-09-29, indexed 0 works. The full check, with claim status, is in `docs/activities/litReview/aquavir/literature-expansion.md`. The vault pointer is [[AquaVir literature expansion]]. A path is not a verified citation.

## Search limits

These limits are not research gaps. They have no priority score and no feasibility score. They must not be rewritten as the statement of the problem.

- arXiv returned no records (HTTP 406).
- OpenAlex prediction search page 2 was retrieved on 2026-09-29. The 76-work set is unchanged. Titles 11–20 are screened in the expansion note. This bullet no longer means the page is missing.
- Several 2025–2026 titles were not opened. Métwalli and colleagues (2025), *Engineering Applications of Artificial Intelligence, 157*, 111214, https://doi.org/10.1016/j.engappai.2025.111214, has a checked DOI and author list. The Crossref record retrieved for this review had no abstract. The full text was not opened. The SSRN record `10.2139/ssrn.5079228` was not opened.
- Accuracies printed in the algorithm review were copied from opened passages. They are not AquaVir performance. This note does not repeat those accuracies.
- Course AI-use logging remains the group's responsibility.

## Claim map

| Claim                                                                                                               | Evidence                                                    | Status                                                                                    |
| ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| S1 forecasts hourly root-zone EC on one sweet-pepper line, uses no harvest label, and is not multi-zone             | Ledger S1                                                   | Agent-opened full text. Not human-confirmed.                                              |
| S2 detects injected, labeled EC and pH faults on one NFT system and is not an unlabeled zone-consistency detector   | Ledger S2                                                   | Agent-opened HTML, including the abstract. Result tables not opened. Not human-confirmed. |
| S3 predicts lettuce fresh weight from plant and water measurements, not from the AquaVir sensor list alone          | Ledger S3                                                   | Agent-opened full text. Not human-confirmed.                                              |
| S4 forecasts air temperature, humidity, and CO₂ in an abstract only, and is not an EC source                        | Ledger S4                                                   | Abstract-only. Full text not opened. Not human-confirmed.                                 |
| S5 uses greenhouse light, temperature, humidity, and CO₂, and is not hydroponic nutrient-solution support for AlgoA | Ledger S5                                                   | Agent-opened HTML. Not human-confirmed.                                                   |
| No opened passage evaluates cross-zone consistency                                                                  | Algorithm review, thematic synthesis, checked against S1–S5 | Bounded to the opened set. Search limits above still apply.                               |
| No hydroponic facility file was analyzed                                                                            | Ledger gaps; algorithm review                               | Absence of a file on disk.                                                                |
| Priority and feasibility integers                                                                                   | Rubric in this note                                         | Judgments. Not data results.                                                              |

## Quality review

Reviewed on 2026-09-28 against the algorithm review and the evidence ledger. Modes checked: claim wording, citation metadata as copied from those two files, and the ranking rules in this note. No statistics were recomputed. No code was run. DOI strings were not looked up again in this pass.

First pass, then one revision:

- Moderate. The draft statement of the problem spoke as if every opened study either forecast one line or classified injected faults. S3 predicts yield, S4 forecasts air climate, and S5 detects greenhouse climate anomalies. The revision names Moon, Ahn, and Son (2018) and Karimzadeh, Li, and Ahamed (2025) only.
- Moderate. Scarce anomaly labels could be read as a description of S2. The ledger says S2's faults were induced and labeled. The revision states that study condition apart from S2.
- Minor. Specific question 1 said "nutrient-solution temperature." The review's series list says "solution temperature." The revision uses that list.

Follow-up on the revised note: those three findings are resolved. The statement of the problem still uses rank 1 only. The claim-map verb for S2 is "detects," matching the ledger target. Rank order is priority 5/5/3/3/1 and feasibility 3/2/5/1/1.

Limitations that remain:

- A person has not confirmed the S1–S5 locators.
- No facility file was analyzed. The scores are rubric judgments.
- AlgoA is unnamed.
- "No opened passage" is limited to this search. The search limits section still applies.
- EC-transfer feasibility is 5 after the ledger check described above. That replaced an expected 3. The rank stays 3, and the statement of the problem stays with rank 1.

## Unresolved

- A person still needs to confirm the locators for S1–S5.
- No facility export, zone count, fault labels, or harvest labels are on disk.
- AlgoA is still unnamed. This note does not assign isolation forest, an autoencoder, or a change-point detector.
- The statement of the problem is a draft from rank 1. Ranks 2 through 5 are not folded into its specific questions.

## References

References follow the algorithm review. Metadata below is copied from that review and the ledger. Human confirmation of each locator is still open.

Eraliev, O., & Lee, C.-H. (2023). Performance analysis of time series deep learning models for climate prediction in indoor hydroponic greenhouses at different time intervals. *Plants, 12*(12), 2316. https://doi.org/10.3390/plants12122316

Karimzadeh, S., Li, Z., & Ahamed, M. S. (2025). Machine learning-based fault detection and diagnosis of electrical conductivity and pH sensors in hydroponic systems. *Computers and Electronics in Agriculture, 237*, 110544. https://doi.org/10.1016/j.compag.2025.110544

Mokhtar, A., El-Ssawy, W., He, H., Al-Anasari, N., Sammen, S. Sh., Gyasi-Agyei, Y., & Abuarab, M. (2022). Using machine learning models to predict hydroponically grown lettuce yield. *Frontiers in Plant Science, 13*. https://doi.org/10.3389/fpls.2022.706042

Moon, T., Ahn, T. I., & Son, J. E. (2018). Forecasting root-zone electrical conductivity of nutrient solutions in closed-loop soilless cultures via a recurrent neural network using environmental and cultivation information. *Frontiers in Plant Science, 9*. https://doi.org/10.3389/fpls.2018.00859

Shu, J., & Yang, D. (2026). CNN-LSTM-POT-based anomaly detection for smart greenhouse sensor data: A real-time edge deployment approach. *Future Internet, 18*(4), 205. https://doi.org/10.3390/fi18040205
