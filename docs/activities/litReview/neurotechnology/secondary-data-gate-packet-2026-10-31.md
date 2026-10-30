# Neurotechnology secondary-data gate packet

**Prepared:** 31 October 2026 (Asia/Manila)  
**Decision:** No neurotechnology title is cleared for submission. This packet implements the checks that can be prepared before a source is acquired; it is not a proposal, raw-data audit, ethics clearance, or empirical result.  
**Track:** New neurotechnology concept, separate from AquaVir and the diesel study. The existing AquaVir TA3 proposal is not revised here.

## 1. Named source and present decision
`
The first source inspected is [EEG RKI / OpenNeuro `ds008496`](https://www.nemar.org/dataset/on008496), DOI `10.82901/nemar.on008496`. NEMAR identifies its copy as v1.0.0 and cites OpenNeuro v1.0.3. Its [dataset description](https://data.nemar.org/on008496/v1.0.0/dataset_description.json) lists CC0; NEMAR reports 1.17 GB of data and a 0.2 GB archive. The [participants table](https://data.nemar.org/on008496/v1.0.0/participants.tsv) lists 15 IDs, `sub-001` through `sub-015`, while the [README](https://data.nemar.org/on008496/v1.0.0/README.md) describes essay writing under different AI conditions. These are public-file and metadata findings, not counts of usable participants. No raw EEG file was downloaded or analyzed for this packet.

**One-run field inspection.** The [general active-AI event dictionary](https://github.com/OpenNeuroDatasets/ds008496/blob/main/task-activeai_events.json) defines task-condition and baseline markers. The opened [sub-001 active-AI event table](https://data.nemar.org/on008496/v1.0.0/sub-001/eeg/sub-001_task-activeai_events.tsv), however, contains only `onset`, `duration`, and `sample`, with one row and `duration` recorded as `n/a`. Its exact two-line public metadata witness, opened through NEMAR's root directory and `sub-001/eeg/` file listing (which redirected to the versioned NEMAR GitHub raw file), is:

```text
onset	duration	sample
4.29445975	n/a	1099.3817
```

A dictionary does not prove that its possible markers occur in a particular run. The [sub-001 EEG sidecar](https://data.nemar.org/on008496/v1.0.0/sub-001/eeg/sub-001_task-activeai_eeg.json) describes one continuous 2,348-second recording at 256 Hz from an Emotiv EPOC X; its [channel table](https://data.nemar.org/on008496/v1.0.0/sub-001/eeg/sub-001_task-activeai_channels.tsv) lists 14 EEG channels, including frontal AF3, F7, F3, F4, F8 and AF4, plus quality-related channels. Neither file establishes usable frontal theta. The full participant/run inventory and raw signal quality have not been audited; other directory links were not consistently retrievable in this metadata check.

| Candidate | Current route | Reason and next discriminating check |
| --- | --- | --- |
| Original titles 1, 3, 8, 11 and the other exposure-based titles | **Stop for `ds008496` as currently documented** | Published fields do not establish consultation duration, prompt frequency, reliance, or a later matched AI-free target block. Title 8 also requires fNIRS. Reopen only if a *same-participant* source supplies those missing fields and block structure. |
| Next-window EEG band-power forecasting within the AI-assisted writing condition | **Inspection candidate only** | Earlier EEG windows might be used to predict later windows from the same recording. Verify signal files, event alignment, usable frontal channels, window coverage, participant count, and the school's record-count interpretation before considering this a title. This changes the research question; it does not measure an effect of AI use. |

Do not read an event's `duration` as time consulting AI. Do not join AI logs from unrelated writers to these EEG recordings. A large count of overlapping windows cannot substitute for independent participants or establish out-of-person generalization.

## 2. Source intake: evidence required from one owner

The group can use this table for `ds008496` or for a specific company/client export. Enter a source locator, document version, and verifier for every supplied item. Record **unavailable** explicitly. Keep restricted exports outside this repository.

| Item to request or verify | Minimum evidence | Current state |
| --- | --- | --- |
| Source identity and owner | Dataset ID/version or named client export, contact, protocol, collection dates | `ds008496` is named; no client export identified |
| Use and reporting rights | License or signed agreement covering research analysis, derived results, figures, publication, retention, deletion, and onward sharing | Public source described as CC0 in the [NEMAR record](https://www.nemar.org/dataset/on008496); school review route still unknown |
| Stable inventory | File manifest, checksums/version, formats, sizes, access method, data dictionary | NEMAR v1.0.0, reported 1.17 GB dataset / 0.2 GB archive; no complete local inventory or checksums |
| Participants and sessions | Pseudonymous participant ID; session/run ID; task order, repeated measures, exclusions | Public table lists 15 IDs; eligible counts and full run structure unknown |
| Neural signal | Raw or documented processed EEG/fNIRS, channel montage/location, units, sample rate, reference, sampling clock, quality/artifact flags | One inspected active-AI run: 14 EEG channels at 256 Hz; signal quality uninspected; no fNIRS confirmed |
| Task and baseline | Condition, writing/summarization task, source/target block IDs, AI permitted/free flag, start/end times, comparable baseline | Possible markers in general dictionary; inspected `sub-001` event table has one row and no block labels; matched future block unconfirmed |
| AI exposure | Per-consultation start/end, prompt count, duration, predeclared reliance measure, source block linkage | Not in general dictionary or inspected `sub-001` event table |
| Clock join | Common clock or synchronization map, time zone, drift checks, participant and block keys | Unverified |
| Institutional route | Written adviser/ethics-office determination for secondary human data, including any exemption or review | Unavailable locally; do not infer an exemption from CC0 |
| Practical limits | Confirmed budget, storage/compute capacity, access date, submission deadline, person who can clarify protocol | Budget and deadline unconfirmed |

## 3. Exposure–outcome join test

For a next-block title, create one row per **participant × source block × later target block**. Each row must have a documented, earlier AI exposure, a baseline for the target measure, and a later matched AI-free target. Apply the following checks in order; stop a title when a required link fails.

1. Join participant IDs across signal, task, and AI-use files without guessing identity. Record unmatched IDs and duplicates.
2. Convert all clocks to one documented time base. Measure clock drift and resolve uncertain time ordering before extracting any pre-target exposure.
3. Confirm that the stated exposure is observed within the source block: consultation duration, consultation count, reliance measure, or last-consultation timestamp. A condition label alone fails this test.
4. Confirm the target block starts after the source block, has the same participant, the claimed task and AI-free condition, and a recorded baseline. Reject ambiguous or overlapping blocks.
5. Verify neural channels, units and quality flags for both baseline and target; specify the band-power or oxygenation calculation *before* comparing blocks.
6. Count eligible rows **after** each exclusion and report the number of unique participants and sessions alongside rows. Do not count windows as independent people.

| Count to enter after source inspection | Value | Evidence / exclusion rule |
| --- | --- | --- |
| Source participants / sessions / runs | **15 listed IDs; eligible participants, sessions and runs unknown** | [Public participant table](https://data.nemar.org/on008496/v1.0.0/participants.tsv); full run inventory and exclusion audit pending |
| Participants with readable signal and required channels | **Unknown** | Signal and montage audit |
| Rows with same-participant exposure–target join | **Unknown** | Joined keys and temporal audit |
| Rows with matched AI-free target and baseline | **Unknown** | Protocol and event audit |
| Eligible rows after missingness/artifact exclusions | **Unknown** | Reproducible exclusion log |
| Unique eligible participants / sessions | **Unknown** | Deduplicated IDs |
| Eligible records under the school's 10,000-record rule | **Unknown** | Adviser-approved record definition plus post-exclusion count |

**Current result for `ds008496`:** neither the public event dictionary nor the inspected `sub-001` event table passes step 3 for the original exposure-based titles; the table also does not document a later matched AI-free target. This is a one-run inspection, not a claim about every participant file or an eligible raw-file count. Even if the narrower within-recording question passes the signal checks, its validation design and contribution require separate review.

## 4. Analysis feasibility protocol, conditional on authorized local data

Before model fitting, preserve raw files and write a versioned manifest with hashes, units, sampling rates, events, and participant/run IDs. Record every unreadable file, missing channel, clock issue, artifact exclusion, and remaining denominator. Do not upload restricted client data to the repository or external services.

For the narrower within-recording idea, define a nonoverlapping source window and later target window entirely within the AI-assisted condition. Choose the horizon from the **observed** run lengths and event boundaries, not from a desired title. Predefine spectral estimation, artifact rules, minimum usable window length, and frontal-channel selection after inspecting the montage. Keep windows from a participant together in train, validation, or test for a claim about unseen participants; if only within-person forecasting is defensible, label the evaluation accordingly. Compare a proposed model with persistence and a simple participant-history baseline using the same splits and eligible windows. Report error per participant as well as pooled error. Do not claim skill, adequacy, or effects until those runs succeed.

The local [CS thesis guideline](../../../CS-Guideline-as-of-Nov-17-as-430pm-without-signature%20%281%29.md) §4.1 requires at least 10,000 dataset records for Data Science. The group is in the Data Science specialization in the existing [TA3 form](../../tp1/TA3%20%5BAI-Assisted%5D%20%E2%80%93%20First%20Title%20Proposal.md). Ask the adviser what counts as a record for EEG forecasting, then compute that count **after** exclusions. The statistical independence and train/test split still depend on participants and sessions, even if the school accepts windows as records.

## 5. Decisions to obtain before a proposal

| Decision needed | Who must supply it | Evidence to record | Status |
| --- | --- | --- | --- |
| Select `ds008496` for a bounded raw audit, or identify one specific alternative export | Group and data owner | Source ID/version or export description and access path | Open |
| Confirm access and permitted publication/storage | Dataset terms or client owner | License/agreement and any restrictions | Open |
| Confirm secondary human-data review or exemption route | Thesis adviser / relevant university office | Written determination and conditions | Open |
| Define how §4.1's 10,000 records applies to EEG windows | Thesis adviser | Written record definition; later post-exclusion count | Open |
| Set budget and submission deadline | Group and course adviser | Approved budget and dated milestones | Open |
| Confirm whether source protocol can answer method questions | Dataset authors or named client contact | Protocol or documented clarification | Open |

The immediately usable question for an adviser or source owner is: **“Can this specific source supply same-participant, time-aligned EEG/fNIRS and AI-use events plus a later matched AI-free target, and what school record and ethics rules apply?”** For `ds008496`, ask specifically whether individual AI consultation logs or a matched later AI-free block exist beyond the published event schema. If the answer is no, do not keep the original titles open on that source.

After the group has evidence for all gates, choose one question the fields actually support. Only then prepare a new neurotechnology TA3 proposal using its area, rationale, objectives, scope, beneficiaries, SDG (if supportable), and references. The [TA2 RRL/RRS template](../docs/TA2%20%5BAI-Assisted%5D%20-%20Django.md) also calls for local and foreign literature/studies and an AI interaction log. Those sections need a separate screened source set; this bounded feasibility screen is not that review. The [guideline](../../../CS-Guideline-as-of-Nov-17-as-430pm-without-signature%20%281%29.md) §§2.1–2.2 also limits the title to 16 words and requires a named method.

## AI interaction entry for this packet

| Date | Group member | Tool and purpose | Output used | Human verification and decision pending |
| --- | --- | --- | --- | --- |
| 31 October 2026 | To be identified by the group | Codex converted the neurotechnology feasibility handoff into a source-intake, join, audit and decision packet. | This file; no model result or proposal text. | Group verifies source locators and data rights; adviser/office confirms record definition and secondary-data review route; group enters the interaction in the course log if this work is used. |

**Independent research QA:** Pass with limitations after one follow-up check. The participant-count wording and the exact TSV witness were corrected and rechecked. The reviewer independently verified the NEMAR summary, general event dictionary, EEG sidecar and local guideline, but the direct TSV files were unavailable through its web tool; their row-level details rely on the separate public-metadata inspection. Full run and raw-signal audits, institutional determinations, budget and deadline remain open.
