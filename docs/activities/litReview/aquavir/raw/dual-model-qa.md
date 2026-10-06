# Independent QA — AquaVir dual-model justification

Date: 2026-09-29  
Reviewer role: independent research QA (did not draft the deliverable)  
Skill: `$research-quality-review` / `.agents/agents/qa.md`

## Brief (checked)

Whether the AquaVir dual-model justification claims only what opened sources support for TFT forecasting and supervised random-forest fault detection, including limitations and the course of action that keeps one arm from blocking the other.

**Deliverable under review:** `docs/activities/litReview/aquavir/dual-model-justification.md`  
**Also checked for consistency (not rewritten):** TA3 §2 rationale paragraph; `AI_INTERACTION_LOG.md` latest row; ledger S6–S8 and gaps; raw notes listed in the brief.

**Status: pass with limitations**

## Summary

The justification keeps TFT design claims on Lim ar5iv passages, treats Moon as a one-line EC comparator, keeps Karimzadeh RF figures abstract-only and supervised-only, fences Metin (aquaponics nitrate) and López Santos (PV) as non-AquaVir performance, copies the cross-arm bottleneck safeguards, and does not invent facility metrics. One material gap remains: the arXiv screening found a greenhouse TFT actuator paper with a 95% figure that the draft never fences by name. Process: the draft embeds a prior QA verdict that this file supersedes.

## Checks performed

| Check | Result |
| --- | --- |
| Lim design table / claim map vs `raw/lim-2021-passages.md` (multi-horizon, static covariates, known future, historical, variable selection) | Supported on opened ar5iv; publisher ScienceDirect not claimed as opened |
| Moon kept as one-line EC comparator only (ledger S1) | Pass |
| RF arm vs `raw/rf-arm-draft.md` and ledger S2 (supervised labeled faults; 93.7% / 96.5% abstract-only; not AquaVir; not unsupervised) | Pass |
| Metin = aquaponics nitrate, not hydroponic EC/pH (S7 / `tft-openalex-findings.md`) | Explicitly non-claimed as AquaVir/hydroponic performance |
| López Santos = PV, not hydroponic (S8) | Explicitly non-claimed |
| Greenhouse preprint arXiv 2512.11852: actuator classification; 95% not forecast accuracy (`tft-arxiv-findings.md`, `arxiv-2512.11852-passage.md`) | Figure not quoted; **explicit named fence missing** (Finding F1) |
| Limitations + bottleneck table vs `raw/limitations-course-of-action.md` and model decision | Material content matches; one-arm-blocked / other-continues rule present |
| TA3 §2 rationale paragraph | Consistent with justification claim ceiling; no facility accuracy claimed |
| AI log latest row | Records synthesis + prior “pass with limitations”; this review is authoritative for status |

## Findings

### F1 — Medium — Missing named non-claim for arXiv 2512.11852

- **Locator:** `dual-model-justification.md` § “Why TFT for the forecast arm”, paragraph “What opened TFT-adjacent searches do not support” (sentence on arXiv TFT queries / AX-TFT-*).
- **Evidence:** `raw/tft-arxiv-findings.md` (AX-TFT-1 sole hit `2512.11852v1`: greenhouse; sensors as inputs; actuator control settings; metric “95% test accuracy”). `raw/arxiv-2512.11852-passage.md` confirms actuator-setting classification, not sensor-series forecasting; no hydroponics named; 95% is classification accuracy.
- **Problem:** The draft correctly states that no returned abstract named hydroponics and does not quote 95%. It does not name the only domain-adjacent arXiv hit or forbid using that accuracy as forecast performance. That is a missing limitation / non-claim relative to the brief’s hard constraint.
- **Exact revision for the writer:** After the arXiv sentence in that paragraph, add one sentence such as: “The only domain-adjacent arXiv hit (AX-TFT-1 / arXiv:2512.11852) is smart-greenhouse actuator-setting classification, not sensor-series forecasting; its reported ~95% classification accuracy must not be quoted as forecast accuracy or as hydroponic or AquaVir TFT performance.” Optionally mirror the same fence in the claim map as an explicit non-claim row. Do not add new literature beyond naming this already-opened hit.

### F2 — Low (process) — Embedded QA status in the deliverable

- **Locator:** `dual-model-justification.md` § “QA status” (closing block asserting pass with limitations).
- **Evidence:** That block was written with the draft; this independent review is the QA artifact required by the brief (`raw/dual-model-qa.md`).
- **Problem:** A self-contained “QA status” inside the justification can conflict with or pre-empt the independent review (and missed F1).
- **Exact revision for the writer:** Replace the embedded QA section with a one-line pointer to `raw/dual-model-qa.md`, or delete that section so status lives only in the QA file. Do not treat the embedded block as the review of record.

## Non-findings (constraints checked and clear)

- No use of another study’s error (Moon, Metin, López Santos, Karimzadeh) as AquaVir performance.
- Random forest framed only as supervised labeled detection; unlabeled TFT deviation ranks kept as unconfirmed review signals.
- Lim design claims attributed to ar5iv of arXiv:1912.09363, not ScienceDirect.
- Cross-arm table: missing labels stop RF validation only; weak coverage stops that target only; no facility series stops facility evaluation but keeps design / “cannot validate” statements.
- Unresolved inputs already listed (no facility export/labels; Karimzadeh tables paywalled; Lim publisher unopened; human locator confirmation pending) — treated as documented limitations, not new overclaims.

## Acceptance criteria

| Criterion | Met? |
| --- | --- |
| Material overclaims listed with severity and file locator | Yes (none beyond documented ceilings; F1 is missing fence, not an overclaim in the current text) |
| Missing limitation / bottleneck safeguard listed | Yes (F1); bottleneck table itself is present |
| Status pass / pass with limitations / fail | **pass with limitations** |
| Exact writer revision stated for material problems | Yes (F1, F2) |
| Justification not rewritten by QA | Yes — only this file written |

## Outcome

**Status: pass with limitations**

Material path: resolve F1 (named fence for arXiv 2512.11852). Process path: resolve F2 (remove or retarget embedded QA). Facility and paywall gaps remain blocking for empirical claims, not for this design note.

---

## Follow-up pass (2026-09-29)

Checked only the writer revisions for F1 and F2. Settled claims from the first pass were not reopened. No new literature search.

| Finding | Status | Evidence |
| --- | --- | --- |
| F1 | **Closed** | `dual-model-justification.md` names AX-TFT-1 / arXiv:2512.11852 (Bashir, Henna, and Furey, 2025) as smart-greenhouse actuator-setting classification; ~95% is stated as classification accuracy and must not be used as sensor-forecast or AquaVir/hydroponic TFT performance. Ledger L7 matches `raw/arxiv-2512.11852-passage.md`. TA3 §2 rationale still does not use that figure as forecast support. |
| F2 | **Closed** | Justification § “Revision and QA pointer” points at `raw/dual-model-qa.md` and no longer embeds a self-declared pass as the review of record. |

**Follow-up status: pass with limitations**

Unresolved limits unchanged (not cleared): no AquaVir facility export or fault labels; Karimzadeh result tables abstract-only / paywalled; Lim publisher page unopened (ar5iv design passages only); no opened hydroponic TFT-vs-LSTM win; human confirmation of agent-opened locators still pending.
