# Idea pool: lived-experience Data Science topics

Compiled: 6 October 2026. Screening ideas only. Every data source below is a lead. No page was opened for this file, no record was counted, and no citation was verified. A plausible path to 10,000 records is not an opened count.

Domains: student life, commuting, online life, law and governance, trade and globalization. Philippine context. Law and trade ideas are kept only when an ordinary person could feel the problem directly.

Hard gates, applied later and not assumed to be passed here: at least 10,000 records, ethical sourcing under the Data Privacy Act of 2012, and a title of at most 16 words that names a technique. See `docs/CS-Guideline-as-of-Nov-17-as-430pm-without-signature (1).md`, sections 4.1 and 4.4, and the title rule used in `docs/activities/litReview/four-field-titles/2026-10-06/opportunity-map.md`.

This track does not replace AquaVir or the diesel record.

## Student life

### S01. Class-suspension nowcast

- Hook: `#WalangPasok` often arrives after students are already on the road.
- Draft question: Can a classifier, using only rainfall, wind signals, and earlier announcements available that morning, flag the local governments that will suspend classes that day better than a persistence rule?
- Draft technique: gradient boosting or a text-plus-tabular classifier.
- Data lead: public suspension posts, PAGASA bulletins, rainfall grids. Unverified.
- Record unit: local-government school day.
- Why 10,000 might be reachable: many local governments times many school days times several years. The announcements themselves may be far fewer than the day grid. Count not opened.
- Ethics: public posts only; drop usernames.

### S02. What students actually post about

- Hook: Enrollment, thesis, and money stress dominate student forums, and the mix changes by month.
- Draft question: Which themes in Philippine student forums rise in enrollment season, midterms, and thesis month?
- Draft technique: topic model (LDA or BERTopic).
- Data lead: public Reddit communities such as r/studentsph and r/peyups. Unverified.
- Record unit: post or comment.
- Why 10,000 might be reachable: comment histories over several years. Not opened.
- Ethics: public text; remove usernames before storage.

### S03. Midnight-commit cramming index

- Hook: Student-organization repositories go quiet for weeks, then spike after midnight before a deadline.
- Draft question: Do public commit timestamps of Philippine university GitHub organizations cluster before known academic calendar deadlines?
- Draft technique: temporal clustering or a calendar regression.
- Data lead: public GitHub commit metadata for university organizations. Unverified.
- Record unit: commit.
- Why 10,000 might be reachable: commit logs grow quickly. Not opened. Organization lists are not a record count.
- Ethics: public metadata only; no private repositories; no claim that a person cheated.

### S04. Overused undergraduate thesis titles

- Hook: Groups keep proposing the same titles because nobody mapped what was already submitted.
- Draft question: Which undergraduate thesis topics in Philippine university repositories are crowded, and which nearby topics are thin?
- Draft technique: text clustering or topic model.
- Data lead: university repository metadata (titles, abstracts, years). Unverified.
- Record unit: thesis record.
- Why 10,000 might be reachable: several universities over many years. A single repository may fall short. Not opened.
- Ethics: public metadata; do not rank or shame named students.

### S05. Bedspace-listing red flags

- Hook: Students lose deposits to bedspace listings that reuse photos or refuse a walkthrough.
- Draft question: Which public bedspace listings carry repeatable red-flag patterns (reused photos, off-platform payment pressure, missing address)?
- Draft technique: classifier or anomaly rules plus a simple model.
- Data lead: public marketplace or forum listings. Unverified.
- Record unit: listing.
- Why 10,000 might be reachable: large marketplaces. Not opened.
- Ethics: listings contain phone numbers and addresses. High privacy risk. De-identify before any store. A flag is not an accusation of fraud.

### S06. Thesis-abstract style shift after 2022

- Hook: Thesis abstracts started to sound the same after generative writing tools spread.
- Draft question: Did the measurable writing style of Philippine undergraduate abstracts shift after November 2022, relative to the prior trend?
- Draft technique: interrupted time-series or a text classifier with a pre/post split.
- Data lead: dated abstracts in university repositories. Unverified.
- Record unit: abstract.
- Why 10,000 might be reachable: same pool as S04. Not opened.
- Ethics: report a corpus shift. Do not label any student as having used a tool.

### S07. Stipend-release lag

- Hook: Government scholarship stipends arrive months after the semester they were meant to cover.
- Draft question: Which agencies and months show the longest gap between a public stipend obligation and a recorded release?
- Draft technique: survival model or gradient boosting on delay.
- Data lead: DBM allotment or disbursement tables, joined to public scholarship announcements. Unverified.
- Record unit: release transaction or allotment line.
- Why 10,000 might be reachable: national disbursement tables can be large; a scholarship-only slice may not be. Not opened.
- Ethics: public fiscal records; no student names.

### S08. Near-campus meal price index

- Hook: The same rice meal costs more every semester, and students cannot tell a real increase from a one-store spike.
- Draft question: Can a model track a student meal basket near campuses and separate a city-wide food move from a single-store jump?
- Draft technique: panel regression or gradient boosting.
- Data lead: public menu posts or food-delivery menu snapshots, plus a retail price series. Unverified.
- Record unit: menu item on a date.
- Why 10,000 might be reachable: many items times many stores times many days. Not opened.
- Ethics: public prices; no customer orders.

## Commuting

### C01. Rail disruption complaints

- Hook: Riders learn that the train stopped from a reply thread, not from the operator.
- Draft question: Can public complaint text, joined to operator advisories, classify the disruption type and flag the next hour better than "same as the last hour"?
- Draft technique: text classifier, optionally with a gradient-boosted alert layer.
- Data lead: public posts about MRT-3 and LRT-1, plus operator advisory pages. Unverified.
- Record unit: post, or station-hour if advisories are gridded.
- Why 10,000 might be reachable: years of posts. A station-hour grid is larger than the post count. Neither was opened.
- Ethics: public posts; remove usernames. A complaint is not proof the train failed.

### C02. Route coverage after jeepney modernization

- Hook: A route that existed on the ride to school disappears, and the replacement does not reach the same barangays.
- Draft question: Which populated barangays lost walk-access to a transit stop when traditional jeepney routes were replaced by modern PUV routes?
- Draft technique: network accessibility measures, with a classifier or regression only if a modeled outcome is needed.
- Data lead: a Philippine GTFS feed and a population grid. Unverified.
- Record unit: barangay, or stop-time if the feed is the dataset. Barangays may fall under 10,000, so the eligible unit has to be stated before this can proceed.
- Why 10,000 might be reachable: stop-times can be large even when route counts are small. Not opened.
- Ethics: public transport data. No rider traces.

### C03. Heat on the walk to the station

- Hook: The uncomfortable part of the commute is the unsheltered walk, not the ride.
- Draft question: At which station-hours does a heat index computed from public weather exceed a walk-discomfort threshold?
- Draft technique: gradient boosting or a spatial model.
- Data lead: weather station or reanalysis hours joined to station locations. Unverified.
- Record unit: station-hour.
- Why 10,000 might be reachable: hours accumulate. The earlier four-field screen did not count Philippine station-hours with paired temperature and humidity, and it stopped related heat titles. This idea overlaps that screen. Not a new count.
- Ethics: no personal data.

### C04. Crash hour-and-place patterns

- Hook: The same corner is dangerous on Friday night and ordinary on Tuesday morning.
- Draft question: Which road segments and hours concentrate reported crashes, beyond a simple exposure baseline?
- Draft technique: spatial count model or gradient boosting.
- Data lead: MMDA or local crash records. Unverified.
- Record unit: crash record.
- Why 10,000 might be reachable: several years of metro crashes. A public extract may be aggregated or restricted. Not opened.
- Ethics: crash records can contain names and plate numbers. Use de-identified locations and times only.

### C05. Flood-day commute failure

- Hook: One heavy afternoon cancels the ride home, and the warning is a photo in a group chat.
- Draft question: Which rail segments and major roads are reported impassable once rainfall passes a threshold, compared with ordinary rain days?
- Draft technique: classifier on segment-days.
- Data lead: rainfall grids plus public flood or rider reports. Unverified.
- Record unit: segment-day.
- Why 10,000 might be reachable: segments times days. Report counts may be much smaller. Not opened.
- Ethics: public reports; no private chat logs.

### C06. Busway travel-time reliability

- Hook: The carousel bus is fast on the poster and unpredictable at 6 p.m.
- Draft question: How much of EDSA Carousel travel time is explained by hour, rain, and incidents, relative to a timetable baseline?
- Draft technique: gradient boosting or quantile regression.
- Data lead: GTFS-Realtime or another public vehicle-location feed. Unverified. The feed may not exist or may not be archived.
- Record unit: vehicle-stop observation or trip.
- Why 10,000 might be reachable: high-frequency locations, if an archive exists. Not opened.
- Ethics: vehicle locations, not rider identities.

### C07. Station-hour crowding

- Hook: One station is packable at 7 a.m. and empty two stops later.
- Draft question: Can historical boardings forecast the next hour's crowding well enough to beat the same hour last week?
- Draft technique: gradient boosting.
- Data lead: hourly station ridership, if an operator publishes it. Unverified.
- Record unit: station-hour.
- Why 10,000 might be reachable: stations times hours times years. A published monthly total would not qualify. Not opened.
- Ethics: aggregates only.

### C08. Traffic-status text versus weather

- Hook: People decide whether to leave campus from a traffic account's color words.
- Draft question: Do public traffic-status posts track rainfall and calendar effects, or do they lag and repeat?
- Draft technique: text classifier plus a tabular baseline.
- Data lead: public traffic-agency posts and a rainfall series. Unverified.
- Record unit: post, or road-segment hour.
- Why 10,000 might be reachable: segment-hours. Post counts alone may not. Not opened.
- Ethics: public agency text.

## Online life

### O01. Incentivized Taglish product reviews

- Hook: A product with hundreds of five-star reviews still arrives broken, and the reviews repeat the same sentence.
- Draft question: Can a model separate repetitive or incentive-like Taglish reviews from the rest better than a rating threshold and a duplicate-text rule?
- Draft technique: text classifier.
- Data lead: public marketplace reviews. Unverified. Platform terms may forbid scraping.
- Record unit: review.
- Why 10,000 might be reachable: review volume is large if access is allowed. Not opened.
- Ethics: public text; drop reviewer names. A model score is not proof of fraud. Terms of service are a kill risk.

### O02. Taglish scam messages

- Hook: The text says a parcel is held, a bank account is locked, or a relative needs load, and it arrives every week.
- Draft question: Can a Taglish classifier catch scam messages that a keyword list misses, without swallowing ordinary delivery notices?
- Draft technique: text classifier.
- Data lead: a public labeled Taglish SMS or chat corpus. Unverified. A self-built corpus may not reach 10,000 labeled messages.
- Record unit: message.
- Why 10,000 might be reachable: only if a public corpus is already large. Not opened.
- Ethics: messages can contain account numbers and names. Store labels and redacted text only.

### O03. Public match draft suggestion

- Hook: Friends lose the game in the draft, then argue about it for the rest of the night.
- Draft question: Does a draft recommender trained on public matches beat the most-picked hero or hero-pair baseline on held-out matches?
- Draft technique: recommender or gradient boosting.
- Data lead: a public match API (OpenDota is the clearest lead; a mobile-game API is unverified). Unverified.
- Record unit: match.
- Why 10,000 might be reachable: public match archives are large. A Philippine-server slice is not confirmed. Not opened.
- Ethics: public match data. Low personal-data risk if account names are dropped.

### O04. Salary posts by role and city

- Hook: Nobody knows whether an offer is normal until someone posts a number anonymously.
- Draft question: What pay ranges do anonymous public posts report by role and city, and which posts are too vague to use?
- Draft technique: information extraction plus a regression.
- Data lead: a public careers forum. Unverified.
- Record unit: post.
- Why 10,000 might be reachable: uncertain. A single forum's salary threads may fall short. Not opened.
- Ethics: high. Posts contain employers, salaries, and sometimes names. De-identify. Do not build a person-level file.

### O05. "Lowest price" claims versus history

- Hook: The app says the price is the lowest in 30 days on the day the voucher expires.
- Draft question: How often does a displayed discount claim disagree with the item's own recent public price path?
- Draft technique: anomaly rules or a classifier.
- Data lead: repeated public price snapshots. Unverified. Terms may forbid collection.
- Record unit: item-day.
- Why 10,000 might be reachable: items times days. Not opened.
- Ethics: prices, not buyers. A mismatch is not proof of a deceptive act.

### O06. Engagement-bait headlines

- Hook: The headline promises a scandal; the article is a quote and a photo.
- Draft question: Can a headline-only classifier flag engagement-bait Taglish news better than length and punctuation rules?
- Draft technique: text classifier.
- Data lead: public headlines from Philippine news sites. Unverified.
- Record unit: headline.
- Why 10,000 might be reachable: news volume. Not opened.
- Ethics: public headlines. Do not label a named outlet as dishonest; report a text class.

### O07. Seller clusters with copied reviews

- Hook: Three shop names sell the same gadget with the same review paragraphs.
- Draft question: Do review-text clusters link sellers that a shopper would treat as independent?
- Draft technique: clustering or near-duplicate detection.
- Data lead: public reviews and seller identifiers. Unverified.
- Record unit: review, with seller as an attribute.
- Why 10,000 might be reachable: same pool as O01. Not opened.
- Ethics: seller names are business identities. Do not accuse a named seller of a crime. Terms of service apply.

### O08. Likely-scam job posts

- Hook: The posting asks for a registration fee, a Telegram-only interview, or a government-looking name.
- Draft question: Can a classifier flag public job posts with scam-like patterns better than a keyword list?
- Draft technique: text classifier.
- Data lead: public job posts. Unverified.
- Record unit: job post.
- Why 10,000 might be reachable: large boards. Not opened.
- Ethics: posts name people and phone numbers. Redact them. A flag is not a finding that the employer committed a crime. Terms of service apply.

## Law and governance

Anomaly scores in this section are flags for human review. They are not findings of corruption, liability, or wrongdoing.

### L01. Procurement red flags in public awards

- Hook: A flood-control or road project is awarded, and the street outside still floods.
- Draft question: Which public award records are unusual on price, bidding window, or split-value patterns, relative to peer items, in a way a reviewer could check?
- Draft technique: anomaly detection or isolation forest, plus a peer-price baseline.
- Data lead: PhilGEPS award or bid notices. Unverified.
- Record unit: award or line item.
- Why 10,000 might be reachable: national procurement volume. Not opened.
- Ethics: records name firms and officials. Publish methods and aggregate rates. Do not name a firm as corrupt. Public records.

### L02. Late or denied information requests

- Hook: A citizen asks for a document and the request sits until the deadline passes.
- Draft question: Does request text and agency predict a late or denied public information request better than the agency's own historical rate?
- Draft technique: text-plus-tabular classifier.
- Data lead: the public eFOI portal. Unverified.
- Record unit: request.
- Why 10,000 might be reachable: unknown until the portal is counted. Not opened.
- Ethics: requests can contain personal details. Use public fields only and drop requester names.

### L03. Time to a court decision

- Hook: Families wait years to learn how a case ended.
- Draft question: Do case type and court predict time from filing or docketing to promulgation better than the court's median?
- Draft technique: survival model.
- Data lead: Supreme Court E-Library or LawPhil decision dates. Unverified.
- Record unit: decision.
- Why 10,000 might be reachable: decision archives over decades. Not opened. A catalog of courts is not a record count.
- Ethics: decisions name parties. Report durations and case types, not a ranking of named persons.

### L04. Ordinances people actually bump into

- Hook: A city has a curfew, a plastic ban, or a tricycle rule, and a newcomer finds out by being stopped.
- Draft question: Which everyday topics (traffic, curfew, noise, plastic, business permits) appear in local ordinances, and which cities publish machine-readable text?
- Draft technique: text classifier.
- Data lead: LGU ordinance portals or gazettes. Unverified and scattered.
- Record unit: ordinance or section.
- Why 10,000 might be reachable: weak. Compilation across cities is the only plausible path. Not opened.
- Ethics: public law. Low personal-data risk.

### L05. Repeat audit observations

- Hook: The same agency is told the same thing in the next year's audit.
- Draft question: Which audit-observation themes recur for the same agency, beyond a boilerplate-text baseline?
- Draft technique: topic model plus a repeat-link rule.
- Data lead: COA annual audit reports. Unverified.
- Record unit: observation paragraph or finding.
- Why 10,000 might be reachable: many agencies times many findings times years. PDF extraction may fail. Not opened.
- Ethics: public audits. A repeated observation is not a finding of corruption.

### L06. Bills that stall

- Hook: A bill is filed every Congress and never becomes something a resident can use.
- Draft question: Does bill text and committee path predict advancement better than "bills that advanced last Congress"?
- Draft technique: text-plus-tabular classifier.
- Data lead: Congress bill status pages. Unverified.
- Record unit: bill-version or bill.
- Why 10,000 might be reachable: several Congresses of bills and versions. Not opened.
- Ethics: public legislative text. Low personal-data risk.

### L07. Lower-court congestion

- Hook: A simple case sits because the branch is buried.
- Draft question: Which court branches have older active cases than their peers, after case-type mix?
- Draft technique: regression or survival model.
- Data lead: a public case-level judiciary extract. Unverified. Annual statistical tables are not case records.
- Record unit: case.
- Why 10,000 might be reachable: not plausible on current public leads. Aggregate yearbooks cannot supply case rows.
- Ethics: case records name parties. Would require a de-identified extract that is not in hand.

### L08. Precinct count data-quality flags

- Hook: On election night, one precinct's tally looks nothing like its neighbors.
- Draft question: Which precinct returns are unusual relative to neighboring precincts and historical turnout, as data-quality flags?
- Draft technique: spatial anomaly detection.
- Data lead: public precinct-level election returns. Unverified.
- Record unit: precinct-contest.
- Why 10,000 might be reachable: precinct counts are large. Not opened.
- Ethics: high sensitivity. Flags are data-quality checks, not findings of electoral fraud. Do not publish a precinct as "stolen."

## Trade and globalization

### T01. Rice and onion price-spike watch

- Hook: The 2023 onion spike and recurring rice jumps show up first in the market, then in the group chat.
- Draft question: Can import volume, tariff events, and weather improve a next-week retail price-spike alert over a persistence forecast?
- Draft technique: gradient boosting.
- Data lead: PSA retail prices, import or tariff series, weather. Unverified.
- Record unit: market-commodity-week, if a market panel exists. A national monthly price is not enough.
- Why 10,000 might be reachable: many markets times weeks times a few staples. A short national series will fail. Not opened.
- Ethics: public prices. No household identities.

### T02. Student grocery basket and the peso

- Hook: Instant noodles, canned fish, coffee, and rice move even when a student's allowance does not.
- Draft question: Do the peso, import unit values, and tariffs explain next-month moves in a fixed student grocery basket better than last month's basket price?
- Draft technique: gradient boosting or a regularized regression with a persistence baseline.
- Data lead: retail price series plus exchange rates and trade unit values. Unverified.
- Record unit: market-item-week, or item-day if a retail panel exists.
- Why 10,000 might be reachable: only with a market or item panel. A handful of national CPI series will fail. Not opened.
- Ethics: public prices.

### T03. Which Philippine-made goods lost foreign buyers

- Hook: A relative's factory shifts from one buyer country to another, and the reason is not visible from the shop floor.
- Draft question: Which product-partner export flows changed after a tariff or demand shock, relative to a peer-product baseline?
- Draft technique: gradient boosting or a panel model.
- Data lead: UN Comtrade Philippine exports. Unverified.
- Record unit: product-partner-year or product-partner-month.
- Why 10,000 might be reachable: detailed product codes times partners times years. Not opened.
- Ethics: public trade statistics. Lived-experience link is indirect (jobs and factory orders, not a daily errand).

### T04. Cross-border parcel surge

- Hook: Small parcels from overseas apps arrive cheaper than the mall, until a tax rule changes.
- Draft question: Did parcel counts or values shift around de minimis or duty changes?
- Draft technique: interrupted time series.
- Data lead: a parcel-level or fine-grained customs series. Unverified. No such public series is named.
- Record unit: parcel or parcel-day.
- Why 10,000 might be reachable: not on a known public lead. Monthly customs totals will fail.
- Ethics: parcel records can identify buyers. Would need aggregates.

### T05. Port waiting and late imported goods

- Hook: An online order sits "at the port" for weeks.
- Draft question: Do public vessel-wait or berth statistics at Manila predict slower clearance weeks better than a seasonal baseline?
- Draft technique: gradient boosting.
- Data lead: port statistics or a public AIS archive. Unverified. AIS access may be paid or limited.
- Record unit: vessel-call or AIS position.
- Why 10,000 might be reachable: AIS positions can be large; published monthly port totals cannot. Not opened.
- Ethics: vessels, not shoppers.

### T06. Fuel price pass-through to fares

- Hook: Pump prices move every week; jeepney fares move by petition, late and in jumps.
- Draft question: How many weeks do fare petitions lag fuel-price moves?
- Draft technique: lag regression or event study.
- Data lead: weekly fuel prices and fare orders. Unverified.
- Record unit: week. This unit cannot reach 10,000 records in a thesis window.
- Why 10,000 might be reachable: it cannot, if the unit is the week or the fare order.
- Ethics: public prices. Low risk. Fails the record gate on the unit.

### T07. Tariff-line import surges

- Hook: A gadget or grocery import suddenly gets cheap or scarce, and the reason is a tariff line, not the brand.
- Draft question: Which tariff lines show import surges or collapses that a simple year-ago baseline misses?
- Draft technique: change-point detection or gradient boosting.
- Data lead: detailed import statistics by tariff line and month. Unverified.
- Record unit: tariff-line-month, optionally by partner.
- Why 10,000 might be reachable: thousands of lines times months. Not opened.
- Ethics: public statistics.

### T08. Remittance corridors and local prices

- Hook: When deployments to one country slow, the allowance a household receives changes before any news article explains it.
- Draft question: Do deployment or remittance-corridor moves improve a forecast of local retail prices over a price-only baseline?
- Draft technique: gradient boosting or a panel model.
- Data lead: deployment or remittance series by corridor, plus retail prices. Unverified.
- Record unit: corridor-month joined to a price panel. Corridor-months alone may fall short; the price panel is the candidate unit.
- Why 10,000 might be reachable: uncertain and depends on T01's price panel. Not opened.
- Ethics: public aggregates only. No worker identities.

## Pool count

40 ideas: S01–S08, C01–C08, O01–O08, L01–L08, T01–T08.

Not in this pool, because they are already tracked elsewhere: AquaVir hydroponics, diesel-genset anomalies, and the two conditional titles in `four-field-titles/2026-10-06/opportunity-map.md` (urban heat alerts; LGU nighttime radiance). C03 overlaps the heat screen and is tagged as such.
