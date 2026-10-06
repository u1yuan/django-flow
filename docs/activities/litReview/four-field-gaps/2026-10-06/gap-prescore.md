# Pre-score — four fields

Scored 6 October 2026 from the title cards and the gap files in this folder. Astronomy was added after `title-cards-astronomy.md` was written. The point rules did not change.

This is a 30-point screen. Feasibility is not included. No model was fit, and no dataset was counted. A high score does not mean a title is approved.

## How points were assigned

**Publishability (0–10).** Up to 4 points for a difference from nearest studies whose DOIs were opened. Up to 4 points for a limitation or future-work sentence, quoted from opened text, that the gap actually answers. 2 points only if at least two Scopus- or IEEE-indexed venues from 2022–2026 were confirmed. No field confirmed indexing, so that 2 points is 0 on every card.

**Competition-level design (0–10).** Up to 2 points for each of: a named user and decision, a demonstrable artifact, a one-sentence innovation traced to the gap card, a metric against a baseline written as a target, and transfer or scale. A generic office, an unconfirmed holdout, or a metric with no baseline file scores 1 on that element.

**Social implication (0–10).** Up to 3 for a named population, 2 for an SDG, 2 for a decision, and 3 for a harm note that covers privacy, stigma, and misuse.

**Gates.** G1 is a title of at most 16 words that names a technique. G2 is one of the ten Data Science subdomains. G6 is the claim boundary: no causal wording, no individual diagnosis of a minor, and no legal or health label from imagery. A card that fails G1, G2, or G6 is dropped. A card with no plausible dataset lead does not advance to the data search even if the gates pass.

## Scores

| Field | Card | Publishability | Design | Social | Total | G1 | G2 | G6 | Advance |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| Psychology | 1. Leave-one-economy belonging transport | 6 | 7 | 9 | 22 | Pass, 11 words, LightGBM | Predictive analytics | Pass | Yes |
| Psychology | 2. Country-holdout bullying classification | 5 | 7 | 9 | 21 | Pass, 8 words, LightGBM | Predictive analytics | Pass | Yes |
| Psychology | 3. Income-group calibration | 4 | 7 | 8 | 19 | Pass, 11 words, logistic regression | Data governance and ethics | Pass | Yes, with a data condition |
| Urban | 2. Facility travel access | 4 | 6 | 9 | 19 | Pass, 12 words, two-step floating catchment area | Statistical modeling | Pass | Yes, with a data condition |
| Urban | 1. Measured broadband tiles | 3 | 5 | 8 | 16 | Pass, 11 words, geographically weighted regression | Statistical modeling | Pass | Yes |
| Urban | 3. Fatal versus all-crash hotspots | 5 | 7 | 9 | 21 | Pass, 11 words, Getis-Ord Gi* | Statistical modeling | Pass | No |
| Meteorology | 1. Transferred heat-index alerts | 6 | 9 | 9 | 24 | Pass, 11 words, random forest | Predictive analytics | Pass | Yes |
| Meteorology | 3. Sensor-hour anomaly flags | 5 | 8 | 9 | 22 | Pass, 11 words, isolation forest | Anomaly detection | Pass | Yes, with a data condition |
| Meteorology | 2. Pre-landfall rapid intensification | 4 | 8 | 9 | 21 | Pass, 10 words, gradient boosting | Predictive analytics | Pass | Yes |
| Astronomy | 1. Sparse-site zenith brightness | 5 | 7 | 9 | 21 | Pass, 11 words, gradient boosting | Predictive analytics | Pass | Yes |
| Astronomy | 4. Blue-weighted brightness below VIIRS | 5 | 7 | 9 | 21 | Pass, 11 words, random forest | Predictive analytics | Pass | Yes |
| Astronomy | 2. Sparse-site brightness trends | 5 | 6 | 8 | 19 | Pass, 13 words, hierarchical linear models | Statistical modeling | Pass | Yes |
| Astronomy | 3. Equatorial observatory disturbance flags | 3 | 5 | 8 | 16 | Pass, 11 words, isolation forest | Anomaly detection | Pass | No |

## What was kept

Psychology keeps all three, in the order above. Card 3 advances only if the data search opens a downloadable school-survey file and a public income classification. Philippine GSHS rows and the income-group merge were not opened.

Urban keeps cards 2 and 1. Card 2 still needs a population-denominator file; the facility extract alone cannot produce the score. Card 3 does not advance: the gap file records no passing crash-record lead, and a card must name one before the data search.

Meteorology keeps all three, in the order above. Card 3 advances only if the data search finds a manual file download. The opened OpenAQ page describes an API with a key, not a bulk file. Card 2 may use IBTrACS. The SHIPS pages did not open, so they are not the lead.

Astronomy keeps cards 1, 4, and 2. Those are the top three scores. Cards 1 and 4 tie at 21; card 1 is listed first because the title names a municipality. Card 2 uses the same Globe at Night file as card 1, so one failed download can stop more than one card. Card 3 does not advance. It is fourth. Its nearest studies stayed preprints, the quoted limitations are not the flag it proposes, no GNSS error file is named, and OMNIWeb did not open.

## Why the points landed where they did

Psychology card 1 has three opened full texts and a Liao limitation on transferable benefit, plus Allohibi’s future-work sentence that names belonging. The education office is generic, PISA 2022 Philippine rows were not confirmed, and the OECD page returned HTTP 403. Card 2’s Low limitation asks for research across many US states after a Utah-only model, which is adjacent to a country holdout. The opened TIMSS 2019 page does not name bullying items. Card 3’s Chen and Man studies are abstract-only, and Allohibi’s measurement-invariance limit is about mathematics anxiety, not a bullying classifier.

Urban card 2 has an opened Philippine facility-point file on HDX. Namadi’s limitation asks for clinical hospital detail, and this card refuses that extension rather than answering it, so the publishability points stay low. No health agency is named. Urban card 1 has an opened Ookla README and a noncommercial flag. No separate limitation sentence on measured throughput was extracted from Paul and colleagues, and no agency is named. Urban card 3 has the clearer hotspot contrast and still stops, because the UK page was a cookie notice and no other crash file was opened.

Meteorology card 1 is the strongest design in this pass: a warning desk, a second-city holdout, and a false-alert rate against that city’s climatology, tied to the cross-city check Han and Randall place outside their analysis. Random forest is the draft title’s technique, not a name in the gap statement. Philippine stations are not named, and non-U.S. GSOD is noncommercial. Card 3’s García review names data quality as a gap and does not report the transfer score. The quality-flag column was not named on the OpenAQ page. Card 2’s pre-landfall window is not in the opened IBTrACS page, the SHIPS pages did not open, and Kim’s year label conflicts between OpenAlex 2024 and an HTML banner reading Volume 10 - 2023.

## Astronomy points

Card 1 has a named municipality, an opened Globe at Night CSV link for 2025 (13,421 observations on that page), and opened full texts for Barentine, Linares, Buhler, and Shah. The innovation says the held-out prediction is separate from restating Barentine’s VIIRS blue-light sentence, so that quote is not a limitation the gap answers. No baseline predictor is named. Philippine rows were not on the opened page. The Scopus preview did not list the journals, and IEEE Xplore returned Error 418.

Card 4 uses the same two leads. Linares’s opened methods section treats Illumina’s blue-light compensation as a model input, and the card asks for a ground-report prediction error at rural pixels below the VIIRS threshold. No office is named, and no baseline predictor is named.

Card 2’s Bará record is abstract-only. The abstract requires control of atmospheric variability for changes near 1 percent per year, and the card calls its sparse-series estimate a different product from repeating that control. No office is named.

Card 3’s Guastavino, He, and Koontaweepunya records remained preprints. The Guastavino sentence is about solar-plasma travel time, and the card says its flag is distinct from that correction. INTERMAGNET’s download page did open. The coincidence score still needs a GNSS error file, which is not named. A flag is not scored as a cause of a positioning failure or a grid fault.
