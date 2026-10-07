# Idea pool: astronomy, psychology, and meteorology

Compiled: 6 October 2026. Same rules as `../idea-pool.md`. Every source is a lead. Nothing in this file was counted or cited as verified.

Lived-experience rule: each idea starts from something a student in the Philippines can actually run into. An abstract catalog question does not qualify.

This pass does not revive titles the 6 October screens already stopped or parked:

- Night-sky brightness from Globe at Night in the Philippines (323 rows, 2006–2024).
- Dark-sky site ranking (248 eNIPAS areas; 274 WDPA designations).
- Filipino adolescent loneliness latent classes (7,763 respondents ages 13–17, below 10,000).
- Urban heat alerts scored only inside very strong El Niño seasons (920 overlapping seasons, not independent events).
- Parked handoff titles: rapid-intensification physics models, Martian surface classification, Earth-to-Mars detection transfer.

Two meteorology leads already have gap cards in `four-field-gaps/2026-10-06/gap-candidates-meteorology.md` (transferred heat-index alerts; OpenAQ sensor-hour flags). They are not copied here as new ideas. The conditional heat-alert and LGU-radiance titles in `four-field-titles/2026-10-06/opportunity-map.md` stay on that track.

## Astronomy



### A01. Will the org's telescope night be clouded out?

- Hook: The astronomy org books the rooftop, carries the telescope up, and the sky is milk.
- Draft question: Can a model, using only weather available the afternoon before, flag Philippine station-nights that will be too cloudy for a visual observation, better than "same as last night"?
- Draft technique: gradient boosting.
- Data lead: a public hourly weather or reanalysis archive joined to night hours. Unverified.
- Record unit: station-night.
- Why 10,000 might be reachable: stations times nights. Not opened. This is a cloud forecast, not a night-sky brightness estimate, and it does not use the 323 Globe at Night rows.



### A02. When a bright satellite will cross the photo

- Hook: A phone photo of the Moon gets a bright streak, and nobody knows if it will happen again during the observation.
- Draft question: For a list of Philippine cities and nights, when does a public orbit catalog predict a bright pass above a stated elevation?
- Draft technique: a deterministic pass model plus a classifier only if the outcome is "pass / no pass" against a reported sighting log.
- Data lead: a public two-line element catalog (CelesTrak is the lead). Unverified.
- Record unit: satellite-city-night, or catalog element.
- Why 10,000 might be reachable: many satellites times nights. A sighting log alone may be small. Not opened.
- Ethics: orbits, not people. This is not a dark-sky conservation-site ranking.



### A03. Was the meteor shower actually visible from here?

- Hook: The group chat says the Perseids are on, the roof is cloudy or bright, and people argue about whether anyone saw one.
- Draft question: Do public camera detections near the Philippines rise on shower nights above the non-shower baseline, and can weather improve a next-night detection forecast?
- Draft technique: gradient boosting or a count model.
- Data lead: a public meteor-camera network. Unverified.
- Record unit: camera-hour or detection.
- Why 10,000 might be reachable: cameras times hours. A Philippine-only camera may not exist. Not opened.



### A04. Which new point of light is worth a student follow-up?

- Hook: Alert emails arrive all night, and a student club cannot look at all of them.
- Draft question: Can a classifier rank public transient alerts for visual follow-up better than "brightest first"?
- Draft technique: classifier.
- Data lead: a public transient-alert stream. Unverified.
- Record unit: alert.
- Why 10,000 might be reachable: survey streams are large. A Philippine-sky filter is not confirmed. Not opened.
- Ethics: no personal data. Weak local hook if the stream is global.



### A05. Variable-star observations that do not match the star's usual range

- Hook: An amateur observer submits a brightness that is far from the star's recent values and cannot tell a real change from a bad estimate.
- Draft question: Which public variable-star observations are unusual relative to that star's recent range, as a data-quality flag?
- Draft technique: anomaly detection.
- Data lead: AAVSO or another public variable-star archive. Unverified.
- Record unit: observation.
- Why 10,000 might be reachable: the global archive is a candidate. A Philippine-observer slice may be small. Not opened.
- Ethics: observer codes can identify people. Drop observer names. A flag is not a claim that the observer cheated.



### A06. Airplane, meteor, or satellite in a night-sky clip

- Hook: Someone yells "meteor," and the streak was a plane.
- Draft question: Can a model separate meteors, aircraft, and satellites in public night-sky camera clips better than a speed rule?
- Draft technique: classifier.
- Data lead: a labeled public night-sky video or detection set. Unverified.
- Record unit: track or clip.
- Why 10,000 might be reachable: unknown until a labeled set is opened. Not opened.



### A07. Moonlit nights and reported sleep

- Hook: A bright full moon through a window without a curtain, on a school night.
- Draft question: Do public sleep or mood records shift with lunar illumination after calendar controls?
- Draft technique: regression.
- Data lead: a public sleep dataset with dates, joined to a lunar-phase table. Unverified.
- Record unit: person-night.
- Why 10,000 might be reachable: only if the sleep file is large. A lunar table alone is a few thousand days and fails. Not opened.
- Ethics: sleep records can be personal. Use a public research dataset with a clear license. No diagnosis.



### A08. Campus light and the limiting magnitude a student can reach

- Hook: The same binoculars show more stars in the province than beside the campus floodlights.
- Draft question: This idea is listed only to exclude it. The ground sample used for Philippine night-sky brightness was 323 Globe at Night rows.
- Draft technique: none. Do not carry forward.
- Data lead: Globe at Night. Already opened in the 6 October astronomy screen.
- Record unit: report. Already below 10,000 for the Philippines.
- Why 10,000 might be reachable: it is not, for the Philippine ground sample. Pixel expansion does not create new ground reports.



## Psychology

No idea here diagnoses a person, labels a minor, or revives the stopped adolescent loneliness title.

### P01. Money worry and life satisfaction, adults only

- Hook: The allowance runs out before the month does, and "how are you" is really about money.
- Draft question: Among adults, do financial-stress items improve a life-satisfaction model over a demographics-only baseline, and does a model trained without the Philippines travel to the Philippine sample?
- Draft technique: regularized regression or gradient boosting.
- Data lead: World Values Survey or a similar public adult survey. Unverified.
- Record unit: respondent. A Philippine-only slice may fall under 10,000 even if the global file does not. The global file is the candidate unit.
- Why 10,000 might be reachable: multi-country waves. Not opened.
- Ethics: adults, public survey, no individual diagnosis. Not the stopped ages-13–17 loneliness analysis.



### P02. Which late-night reply is actually useful?

- Hook: A student posts at 1 a.m. about not coping, and the first replies are jokes, lectures, or something practical.
- Draft question: Can a text model flag public peer-support replies that later readers mark as helpful, better than reply length?
- Draft technique: text classifier.
- Data lead: a public peer-support forum with a helpfulness signal. Unverified.
- Record unit: reply.
- Why 10,000 might be reachable: large forums. Not opened.
- Ethics: high. Mental-health text. De-identify. Do not build a crisis detector and do not claim a reply prevents harm.



### P03. Exam-month stress language, without a clinical label

- Hook: The week before finals, student posts get shorter and more hopeless, then recover.
- Draft question: Does the rate of stress-related language in a public student forum rise in exam weeks above the forum's own baseline?
- Draft technique: lexicon or classifier rates inside an interrupted time series.
- Data lead: public student-forum timestamps. Unverified.
- Record unit: post.
- Why 10,000 might be reachable: comment histories. Not opened. Overlaps S02, but the outcome is stress language rather than topic mix.
- Ethics: public text, usernames removed. A rate is not a diagnosis of any poster.



### P04. Filipino cyberbullying text

- Hook: A group chat or comment thread turns into insults, and the target is a classmate.
- Draft question: Can a Filipino or Taglish classifier catch bullying text that an English keyword list misses?
- Draft technique: text classifier.
- Data lead: a public labeled Filipino cyberbullying corpus. Unverified.
- Record unit: message.
- Why 10,000 might be reachable: uncertain. Many shared-task sets are smaller. Not opened.
- Ethics: high. Texts may describe minors. Do not infer the age of an author. Do not identify targets. If the corpus is mostly about minors, stop.



### P05. Does an English wellbeing model fail on Taglish?

- Hook: A wellness app scores an English sentence and a Taglish sentence about the same bad week differently.
- Draft question: On parallel or comparable public texts, is a wellbeing or sentiment model's error higher on Taglish than on English?
- Draft technique: a paired error comparison, with a classifier as the instrument.
- Data lead: a public bilingual or Taglish sentiment set. Unverified. The Shopee review card in the other track is star ratings, not wellbeing.
- Record unit: text.
- Why 10,000 might be reachable: unknown. Not opened.
- Ethics: do not turn a sentiment error into a mental-health diagnosis.



### P06. Sleep timing against an academic calendar

- Hook: Sleep slides later every long exam week and does not fully come back.
- Draft question: Do public sleep-timing records shift around exam calendars more than around ordinary weeks?
- Draft technique: interrupted time series or gradient boosting.
- Data lead: a public dated sleep dataset. Unverified.
- Record unit: person-night.
- Why 10,000 might be reachable: only if a large public file exists. A 30-person class diary will fail. Not opened.
- Ethics: use a research dataset with a license. No clinical claim.



### P07. Disaster worry in an adult survey

- Hook: After a typhoon, students talk about home before they talk about the quiz.
- Draft question: Do adults in recently affected areas report higher worry or lower life satisfaction than adults elsewhere in the same survey wave, after income controls?
- Draft technique: regression.
- Data lead: a public adult survey with place and date. Unverified.
- Record unit: respondent.
- Why 10,000 might be reachable: uncertain. A single post-disaster sample is often small. Not opened.
- Ethics: adults. No individual diagnosis. Association only, not "the typhoon caused the score."



### P08. Adolescent loneliness latent classes

- Hook: Listed only to exclude it.
- Draft technique: none. Do not carry forward.
- Data lead: WHO GSHS catalog 944, already opened in the 6 October screen.
- Record unit: respondent ages 13–17. The opened upper bound was 7,763.
- Why 10,000 might be reachable: it is not, for that age band.



## Meteorology



### M01. Will it rain on the walk between buildings?

- Hook: The forecast is "cloudy," the next class is across the open quad, and the downpour starts halfway.
- Draft question: Can a next-hour rain classifier, using only data available at the decision time, beat persistence and the hour's climatology at Philippine stations or grid cells?
- Draft technique: gradient boosting.
- Data lead: a public hourly rain or satellite-rain series. Unverified.
- Record unit: station-hour or grid-hour.
- Why 10,000 might be reachable: hours accumulate. Not opened. This is rain, not a heat-index alert, and it is not an El Niño-regime study.
- Ethics: no personal data.



### M02. The forecast said fine

- Hook: Students leave the dorm because the posted forecast looked safe, and they are soaked by lunch.
- Draft question: On days with an archived public forecast, how often does the forecast category miss the observed rain or temperature, relative to a persistence forecast?
- Draft technique: a verification score. A model is in the title only if the study forecasts the miss, not if it only tabulates hits.
- Data lead: an archive of forecasts as issued, plus observations. Unverified. The heat-alert screen already found that iHeatMap and iRISE-UP issue-time archives were not opened.
- Record unit: forecast-day or station-day.
- Why 10,000 might be reachable: only if issued forecasts were archived. A handful of typhoon case studies will fail. Not opened.



### M03. Outdoor class and PE window

- Hook: PE and fieldwork get cancelled after everyone has changed, because the rain arrived in the scheduled hour.
- Draft question: For a fixed afternoon window, can yesterday's weather forecast the chance of rain better than the seasonal frequency?
- Draft technique: gradient boosting.
- Data lead: same family as M01. Unverified.
- Record unit: station-day window.
- Why 10,000 might be reachable: stations times days. Not opened.
- Note: this is the daily version of M01. Keep only one if the data lead is the same.



### M04. First monsoon week of classes

- Hook: Classes start, and the first real monsoon week floods the usual route.
- Draft question: Are the first school weeks of the monsoon wetter or less predictable than other weeks at the same stations?
- Draft technique: a comparative model with climatology as the baseline.
- Data lead: station or grid rainfall by day. Unverified.
- Record unit: station-day inside a defined window. A unit of "year" cannot reach 10,000.
- Why 10,000 might be reachable: station-days can. Not opened.



### M05. Thunderstorm lead time for an open court

- Hook: An intramural game is mid-set when the sky goes dark, and the warning is someone pointing up.
- Draft question: How many minutes of lead time does a public lightning or radar field give before rain starts at a station, compared with a no-skill baseline?
- Draft technique: survival model or gradient boosting.
- Data lead: a public lightning network or radar archive, plus a rain gauge. Unverified.
- Record unit: storm-station event, or minute. Minute-rows can be large and highly dependent. The event count may be the honest unit and may fall short. Not opened.



### M06. Roadside air on the commute

- Hook: The queue at the station smells like exhaust, and the city's daily air reading does not match that corner.
- Draft question: Which roadside sensor-hours disagree with a nearby reference monitor beyond a simple calibration line?
- Draft technique: anomaly detection.
- Data lead: OpenAQ hourly measurements. A gap card already records this lead. Philippine rows were not named there. Not reopened for this file.
- Record unit: sensor-hour.
- Why 10,000 might be reachable: hours. Not counted in this pass.
- Note: not a new gap. Included so the scorecard can prefer a lived question the gap file did not already write.



### M07. Humid heat on the unsheltered walk

- Hook: Listed only to point at existing work.
- Draft technique: none as a new idea.
- Data lead: the conditional heat-alert title and C03 in the commute pool.
- Record unit: station-hour. Not counted.
- Why 10,000 might be reachable: not re-estimated here.



### M08. Gauge versus satellite rain at the campus

- Hook: The satellite product shows a storm, and the ground outside the building is dry, or the reverse.
- Draft question: Where and when does a public satellite rain estimate disagree with a Philippine gauge beyond the gauge's own hour-to-hour persistence?
- Draft technique: gradient boosting or a paired error model.
- Data lead: a satellite rain product plus a gauge archive. Unverified. The earlier handoff noted that Philippine gauge truth for a precipitation product was not opened.
- Record unit: gauge-hour.
- Why 10,000 might be reachable: gauges times hours, if the gauge file exists. Not opened.



## Pool count

24 ideas: A01–A08, P01–P08, M01–M08.

Excluded from any shortlist by rules already applied: A08, P08, M07.