# Proposal 157 is two studies in one draft

Date: 31 October 2026  
Audience: the thesis group, before any submission of ThesisPro proposal #157  
Mode: explanation of the latest inclusion. The last section is a repair sequence. Follow it only if the group accepts the recommendations.

This report does not score papers, compute agreement, or claim that a model has been trained. The group has not answered the six design questions from the same evening. The recommended position below is the reviewer's position. It is not a group decision.

## Where the text came from

The live page is [ThesisPro proposal #157](https://thesispro.brightdevstudio.cloud/team/proposals/157). The page title at the time of reading was "Multi-Bed Hydroponic Crop-Stress Warning and Fault Detection Using Temporal Fusion Transformer and Random Forest". The page was read in the browser on 31 October 2026, after the on-page guideline check timestamp of 20:35 the same day. That check reports Ready, 0 blocking issues, and 0 warnings. Version history on the page says Version 1, not yet submitted.

An earlier extract the same day, saved outside the repository, still carried the title "Multivariate IoT Sensor Analytics for Multi-Zone Hydroponic Systems Using Random Forest and Temporal Fusion Transformer" and the older objectives. The readability note at `docs/activities/tp1/thesispro-readability-2026-10-31.md` scores that older wording 17 out of 30. Do not apply that score to the rewritten objectives.

The 29 September 2026 model decision in `docs/activities/litReview/aquavir/model-decision-2026-09-29.md` is a local design record. Its status line says the design is selected and its performance is unvalidated. Lim et al. 2021 and Karimzadeh, Li, and Ahamed 2025 were not re-opened for this report. Claims about those papers stay inside what that decision file already limits them to. ThingSpeak channels named on the dataset card were not opened. No partner file was on disk, and none was analyzed.

## What the new pages commit to

The title, general objective, specific objectives, scope, and limitations were rewritten. Together they describe a product the general objective calls AquaVir.

The general objective says the study helps one commercial hydroponic farm detect bed-level problems before crop damage. AquaVir learns from that farm's historical and ongoing sensor records, checks whether each reading is reliable, and forecasts each bed early enough for someone to act.

The specific objectives then split the work into five steps.

1. Prepare the partner farm's records by bed and timestamp. Remove invalid and duplicate entries. Handle missing values and physically impossible values.
2. Train a random forest to class each reading as normal or faulty. The fault words in this objective are stuck, drifting, spiking, and out-of-range. Score the forest with precision, recall, and F1. Pass only verified readings onward.
3. Train a Temporal Fusion Transformer on those verified readings. Forecast each bed's condition 24 hours ahead. Warn when a bed is heading toward harmful levels. Compare the transformer with a seasonal-naive forecast and with LightGBM. Report MASE and early-warning lead time.
4. Show four screens. The names on the page are Farm Bed Map, Sensor Health Alerts, Proactive Crop-Stress Warnings, and Daily Bed Reports.
5. Ask the partner farm's operators whether the system is usable and useful.

The scope narrows the site to one partner commercial farm in Metro Manila, using only sensors the farm already has. It adds a fifth fault class, missing readings, to the four named in specific objective 2. Fault examples come from two sources. One source is faults the partner confirms, where such records exist. The other source is faults the group inserts into the historical series. Forecasts use a 24-hour horizon and time-ordered splits. The delivered thing is a web application.

The limitations deny three things the title and the screens still imply. The system does not control or repair equipment. Crop stress is inferred from sensor readings alone. The draft says the study does not use plant images, laboratory tests of plant tissue, or yield. Fault accuracy depends on how many real fault examples the partner can provide. If those examples are few, the model relies more on simulated faults. If the partner history is shorter than three months, the models are developed first on a public hydroponic dataset, then retrained on live partner readings, and evaluated once three months exist. If no partner is secured, training and evaluation stay on the public dataset, and the conclusions are limited to that dataset.

## What the old pages still commit to

Area of Investigation, the module list, Background and Rationale, and Target Beneficiaries were not rewritten. They still describe a different study.

Area of Investigation still investigates multivariate sensor behavior across multiple hydroponic zones. It emphasizes normal operation, deviations, and temporal behavior. Anomaly detection and prioritization are the analytical methods. Forecasting is an extra question about expected sensor behavior. The module list still has a stray closing brace after "modules:". The modules are still data management, preprocessing, multi-zone analysis, a random forest for observations and drifts that deviate from normal behavior, anomaly ranking by persistence and severity and zone, a Temporal Fusion Transformer investigated as a way to estimate expected sensor behavior, and visualization.

The background still moves from Philippine agriculture to controlled-environment agriculture, then to hydroponics, then to IoT sensors across zones. It says variation can be normal operation, a difference between zones, or abnormal behavior. It attributes data-quality checks, temporal alignment, zone-level analysis, anomaly detection, and anomaly prioritization to "the feasibility study" and cites Phan et al. 2025 for that sentence. The earlier readability pass already marked that label as a mislabel. This report did not re-open Phan et al. 2025, so the mislabel stands as a drafting defect, not as a new finding about the paper. The background then calls the transformer an additional investigation. Predicted-versus-observed differences "may then provide additional information". That sentence is weaker than a warning that a bed is heading toward harmful levels.

The uncited sentence about nutrient lockout ruining crops within a few hours is still in Area of Investigation. Sportelli et al. 2025, Sgueglia et al. 2022, and Lim et al. 2021 remain in the reference list and still do not appear in the background funnel. Three reference entries still read "Other authors, N. S. I. P." Those entries are Ahmed 2021, Hassan 2023, and Kumar 2022. They are not citable records.

The beneficiary list still addresses commercial multi-zone enterprises, home growers, technology providers, researchers, and farm managers. The new scope addresses the operators and managers of one partner farm.

The dataset card still says the partner logs are not yet available. Candidates named on the card are IntelliFarm, NXTLVL Farms, Ateneo Innovation Center, and AniTech. The card lists 10,000 records. That figure is a planned count on the form, not a count from a file. The split field says a held-out test set and also says there is no split. Preprocessing on the card converts timestamps to Philippine time, aligns readings to hourly intervals per bed, removes duplicates, removes physically impossible values, fixes swapped fields, interpolates short gaps, flags long gaps, flags outliers with robust z-scores, builds time and lag features, normalizes each sensor per bed, and splits by time order.

A second card names Ateneo Innovation Center SHIELDS ThingSpeak channels 1938518, 1873072, 1984937, and 891376, with a planned 40,000 records, for validation and benchmarking. Those channels were not opened for this report. The card does not say they contain bed identifiers, fault labels, or the sensors the objectives forecast.

New references visible on the page, and not in the earlier extract's reference block, include Cho et al. 2024, Gillespie et al. 2020, Karimzadeh et al. 2025, Kudirka et al. 2023, Metin et al. 2023, Nelson et al. 2025, Rahman et al. 2026, Sulaiman et al. 2025, and Tsoukas et al. 2023. Their presence on the list does not mean a passage was checked, and it does not supply the missing harmful-range numbers.

## The premise that keeps failing

The readability pass tried to repair wording. This inclusion tries again by renaming the outcome. Both passes keep one belief. A forecast of sensor readings, compared with a harmful range, is a crop-stress warning.

The new limitations already contradict that belief. They say the study identifies conditions that are likely to harm crops, and they say the study does not measure plant health. The title and the screen name Proactive Crop-Stress Warnings still state the belief.

A third title edit that keeps the words "crop stress" would spend the next revision on the same premise. The premise has to be accepted or removed before more prose is worth writing.

## Six conflicts that would break a defense

### The warned event is not the measured event

The title warns of crop stress. Specific objective 3 warns when a bed heads toward harmful levels. The limitations say stress is inferred from sensors and that plants are not measured. No section states the sensor, the numeric range, or the source of that range.

An adviser can ask what was warned and what later showed the warning was right. Today the draft has no event definition that survives that question. A sensor crossing a stated range can be scored. Crop stress cannot be scored with the measurements the limitations allow.

Gillespie et al. 2020 and Kudirka et al. 2023 are now in the reference list, and their titles concern plant response to pH. This report did not open those papers. A title in a bibliography is not a threshold for this farm.

### The forest is trained on events the cleaning steps delete

Specific objective 1 handles missing values and physically impossible values before the forest trains. The dataset card removes values such as pH outside 0 to 14 and water level above 100 percent, interpolates short gaps, and flags outliers. Specific objective 2 and the scope ask the forest to detect spikes, out-of-range readings, and missing readings.

If those rows are removed or filled first, the positive class is gone before training. The forest then classifies a series from which the faults were already erased. Sensor Health Alerts would have nothing honest to alert on.

The two-stage handoff has a second hole. Specific objective 2 passes only verified readings to the transformer. The scope says all models use time-ordered splits. The draft never says the forest is fit only on past time, then applied forward, and that the transformer trains only on readings the forest accepted inside the training window. If the forest sees the test period before the transformer is scored, the forecast test is not a future test.

Inserted faults create a third hole. The scope adds simulated faults to the historical data. It does not say insertion happens only inside training folds, on a copy that the forecast test never sees. A spike inserted into the test window can change both the fault score and the forecast score. Those two scores would no longer be separate results.

### The fault sentence is stronger than the labels

The 29 September decision says the forest classifies labeled faults, and that a result on inserted labels is not a result on farm-confirmed faults. The decision file's note on Karimzadeh, Li, and Ahamed 2025 is limited to that point. This report does not add a new reading of that paper.

The new scope allows both partner-confirmed faults and inserted faults, and it allows the second to fill in when the first is scarce. The dataset card says the partner file does not exist yet. No fault-label file is in the repository.

The defendable sentence, if insertion is specified, is that the forest detected faults the group inserted under a stated rule, with stated counts. The sentence that the forest detected the farm's faults is not available. Writing one blended F1 across both sources would hide which sentence was tested.

### The site is both secured and still a candidate list

The general objective and the scope speak as if one Metro Manila farm is the study site and as if operators will evaluate the web app. The dataset card says the partner is to be confirmed, the logs are not yet available, and written permission is expected by early Semester 2.

Both cannot be the submission sentence. The card is the one that matches the absence of a data file. The objective overclaims a site.

The three-month fallback is a real limitation, and it changes the study. A public-channel-only result is a methods study on those channels. It is not evidence about the unnamed farm. The card does not show that the named ThingSpeak channels support bed-level faults or 24-hour forecasts of the sensors in the objectives.

### Bed and zone are still both the unit

The new sections say bed. The old sections say zone. The 29 September decision says zone, and it defines the forecast as one hourly value for each eligible sensor and zone over the next 24 hours.

Bed is the right word only if each bed has its own sensor set. If one nutrient loop feeds many beds and only the loop is sensed, a bed forecast invents a unit the sensors do not observe. The draft never defines which equipment group carries the sensors. Using both words lets a reader think the cross-zone study and the per-bed warning system are the same design.

### The forecast test changed without retiring the old one

The 29 September decision requires two comparators, last value and the same hour on the previous day. It requires MAE and RMSE in each sensor's own units at each hour of the 24-hour path. It forbids quoting another study's error as this project's error. It also forbids future sensor readings and unknown interventions as inputs.

Specific objective 3 replaces that report with seasonal-naive, LightGBM, MASE, and lead time. A seasonal-naive forecast with a 24-hour period is the same-hour-yesterday comparator under another name. LightGBM is a new third forecaster. MASE does not say whether an error of 0.2 pH matters. Lead time needs a start event and a confirming event. The draft has neither.

The objectives also never list the sensors. The September decision lists pH, electrical conductivity, humidity, nutrient-solution temperature, water level, light intensity, and ambient temperature, and only where each one is actually logged. The new phrase "each bed's condition" collapses those series into one unnamed target.

## What you can say on 31 October 2026

You can say the draft proposes a random forest for sensor-fault classes and a Temporal Fusion Transformer for 24-hour sensor forecasts, shown in a web view, for a farm that is not yet confirmed.

You can say no partner export and no fault-label file were available to this review. You can say the page itself calls crop stress an inference and excludes plant measurements. You can say the September decision still marks performance as unvalidated.

You cannot say the system warns of crop stress, that the forest finds the farm's real faults, that a partner site is secured, that harmful levels are defined, or that either model has an accuracy on this problem. A proposal is not a completed experiment. The guideline check being Ready does not resolve any conflict in this report.

## Recommended position, not a group decision

Accept these six positions only by an explicit group decision. Until then they stay recommendations.

1. The warned event is a forecasted sensor value outside a range you state before you look at the test period. Remove crop stress from the title and from the screen name. Do not add a plant measurement unless you also delete the limitation that forbids one.
2. The forest trains on the time-aligned raw series. Duplicates and clock repair are the only steps before it. Spikes, stuck runs, drift, out-of-range points, and gaps stay in the table as candidate fault rows. Fit the forest on past time only. Withhold a reading from the transformer only after that past-only forest marks it faulty. Leave the withheld times missing.
3. Keep two result sentences. One covers faults you insert, with the rule and the counts, on a copy the forecast test does not use. The other covers faults the farm confirms. Delete the second sentence if the farm has no log.
4. The dataset card is the site sentence you can defend. Rewrite the objective and the scope so the farm is prospective. Name a farm only after a data-use agreement exists.
5. Use one word for the sensed unit in every section, including the September decision if the group updates it. Use bed only when each bed has its own sensors. If the sensors sit on a shared loop, the title names the loop.
6. Keep last-value and same-hour-yesterday. Report MAE and RMSE in physical units at each horizon for each logged sensor. Call the seasonal-naive forecast that second baseline, once. LightGBM may be a third forecaster. MASE may be an extra number. Define lead time only after the warning rule in position 1 exists.

## Repair sequence if you accept that position

Do these in order. Each step removes a contradiction the next step would otherwise rewrite into new prose.

1. Replace the title's crop-stress claim with the sensor-fault claim and the 24-hour forecast warning. Either put AquaVir in the title or remove AquaVir from the general objective. One product name, in one place, is enough.
2. Write the warning rule in the scope. Name each sensor. State the numeric range and whether it comes from a cited source or from the farm's written operating limits. State that lead time is the number of hours from the first forecast hour outside the range to the first later observed hour outside the range. State that a warning the observation never confirms is a false alarm.
3. Rewrite Area of Investigation, the module list, the background, and the beneficiaries so they describe those two outputs and that one unit. Delete zone, or delete bed, after step 5 of the recommended position. Remove the stray brace.
4. Rewrite the dataset preprocessing so it no longer deletes the fault classes. State the time-ordered fit for the forest and the transformer, including the rule that inserted faults never enter the forecast test copy.
5. Replace the secured-farm sentences with the prospective-partner sentences from the dataset card. Keep the public-data fallback, and say that a public-only result does not transfer to the partner.
6. Put the September comparators and the unit errors back into specific objective 3. Keep LightGBM only as an added forecaster.
7. Delete or replace the three "Other authors, N. S. I. P." entries. Move Phan et al. 2025 out of the "feasibility study" label unless someone opens the paper and shows that it is that study. Cite the crop-loss sentence or delete it. Bring Lim et al. 2021, and the fault-detection source you actually rely on, into the background only after someone checks the passage.

## Claim register

| ID | Claim in this report | Source read for this report | Limit |
| --- | --- | --- | --- |
| C1 | Live title, objectives, scope, limitations, old sections, dataset fields, guideline status, version status, and the named new references | ThesisPro #157 page text, 31 October 2026 | Page text at that reading. Later edits can move it. |
| C2 | Older #157 title and the 17 out of 30 readability score belong to the pre-rewrite wording | `docs/activities/tp1/thesispro-readability-2026-10-31.md` and the earlier local extract | Do not reuse the score on the new objectives. |
| C3 | September design, metrics, label rule, and unvalidated status | `docs/activities/litReview/aquavir/model-decision-2026-09-29.md` | Local decision record. Lim and Karimzadeh were not re-opened. |
| C4 | No partner export and no fault-label file were analyzed | Repository check stated in C3, plus the dataset card in C1 | Absence in the card and in that decision file. A private file outside the repo would not have been visible. |

## What is still unresolved

The group has not chosen the warned event, the cleaning rule, the fault sentence, the partner sentence, the sensed unit, or the metric set. No output folder, rubric-source papers, or reviewer label were named, so no paper-scoring pack was built. No full text of Lim, Karimzadeh, Phan, Gillespie, or Kudirka was opened for this report. No ThingSpeak channel was inspected. No accuracy number in this report exists, because no model was run.
