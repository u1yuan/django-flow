# AI interaction log

Course use: Thesis 1 (CS0025). AI-assisted work. The group remains responsible for checking accuracy.

| Field | Value |
| --- | --- |
| Date | 2026-10-31 |
| Tool | Cursor agent, local file read, local Python |
| Reviewer label used in scores | `ai-draft` |
| Human reviewer | not assigned |
| Web retrieval | not used (brief forbid it) |
| Package installs | none |
| Git commit or push | none |

## Brief (six fields)

```text
Research question or topic:
  Build a paper-evaluation pack whose criteria come only from two SYNTHETIC
  invented abstracts (PLAN and CASE).
Requested output:
  Full pack plus run-report.txt in the named output folder.
Input locations:
  .agents/skills/paper-evaluation/evals/files/SYNTHETIC_paper_plan.txt
  .agents/skills/paper-evaluation/evals/files/SYNTHETIC_paper_casestudy.txt
Constraints:
  Do not retrieve the web. Do not save PDFs. Do not git commit or push.
  Python standard library only. Write only in the named output folder.
  Reviewer label ai-draft. Do not invent a second reviewer.
  Never call the PLAN framework validated.
  Tag each criterion full-text, abstract-only, or adapted.
Acceptance criteria:
  Required files present. Criteria trace to the two abstracts.
  Support levels are the three allowed tags. PLAN not described as validated.
  No PDF. scores.csv reviewers are only ai-draft. Scorer and tests pass.
  At least one criterion on performance reporting or model comparison.
  At least one criterion on feasibility and acceptance as separate questions.
Data handling restrictions:
  SYNTHETIC invented text only. Quotes 25 words or fewer. No invented DOI.
```

Unavailable inputs: real bibliographic metadata, full-text body, a second reviewer, and any facility or empirical dataset.

## Prompt used

The parent task, summarized:

> Read `.agents/skills/paper-evaluation/SKILL.md` and `references/` in full. Build a pack whose criteria come only from the two SYNTHETIC papers. Do not retrieve the web, save PDFs, or git commit or push. Python standard library only. Reviewer `ai-draft`. Include README, source-trace.md, rubric.csv, desk-check-checklist.md, templates/evaluation-template.md, scores/scores.csv, scripts/score_papers.py, scripts/tests with a SYNTHETIC fixture, and AI_INTERACTION_LOG.md. Score both papers, run the scorer and tests, and save `run-report.txt`. Do not invent a second reviewer. Never call the PLAN framework validated.

`$evidence-research` and `$citation-management` were not used for retrieval. The brief forbids the web, and the files invent no DOI.

## What the AI did and produced

| Step | Action | Output |
| --- | --- | --- |
| 1 | Read both local SYNTHETIC files. No web retrieval | `source-trace.md` |
| 2 | Extracted 7 PLAN concepts and 8 CASE concepts. Confirmed brief seeds against those sentences. Discarded "PLAN framework validated" and "desk-checking is a structured inspection" | `concept-extraction.md` |
| 3 | Wrote 8 criteria with observable 0/1/2 anchors | `rubric.csv` and the rest of the pack |
| 3 | Copied `scripts/score_papers.py` and the skill's SYNTHETIC test fixtures | `scripts/` |
| 4 | Desk-checked and pilot-scored both papers as `ai-draft` only | `evaluations/`, `scores/scores.csv` |
| 5 | Ran the scorer and unittest discover from the pack folder | `scores/summary.csv`, `run-report.txt` |
| 6 | `$research-quality-review` against the brief and the two abstracts; one revision pass if needed | See QA below |

### Pilot run

Recorded in `run-report.txt` after the scorer and tests. Expected totals if validation passes:

```text
SYN-PLAN | ai-draft | v1.0.0 | 3/8 | scored=4 NA=4
SYN-CASE | ai-draft | v1.0.0 | 10/16 | scored=8 NA=0
Cohen's kappa: not computed (no paper has scores from two reviewers).
```

Hand check of totals: SYN-PLAN scores 2, 0, 0, 1 plus four NA → 3 points, max 8. SYN-CASE scores 2, 0, 1, 1, 2, 2, 1, 1 → 10 points, max 16. QA lowered SYN-CASE C08 from 2 to 1 because acceptance is not qualified by the reported limit.

## What a human must verify

1. **Source files.** Confirm the two SYNTHETIC `.txt` files still match the quotes in `concept-extraction.md` and `evaluations/`.
2. **Every `ai-draft` score.** All 16 rows are drafts. Open items: SYN-PLAN C03 (0 vs 1); SYN-CASE C08 (kept at 1 after QA).
3. **A second reviewer.** No second reviewer exists. Kappa was not computed. Do not invent a second sheet. A human should score both papers without reading `evaluations/*_ai-draft.md` first. Meaningful kappa needs more than two papers.
4. **Circularity.** The scored papers are the rubric sources. Totals test consistency only.
5. **PLAN status.** Confirm no pack sentence calls the planned guidelines a validated framework.

## QA

`$research-quality-review` against the brief, the two SYNTHETIC abstracts, `rubric.csv`, `scores/scores.csv`, `scores/summary.csv`, and `run-report.txt`. Citation-management was not used: there is no real DOI or publisher record. Totals were recomputed by hand. Kappa was not computed (one reviewer).

**Verdict after the first pass: needs revision.** One material score error.

| Severity | Artifact | Evidence | Correction |
| --- | --- | --- | --- |
| Material | SYN-CASE C08 = 2 | Score-2 requires each finding to be qualified by the method limit. Abstract: feasibility is qualified ("was feasible, but…"); "Developers accepted both parts" is not | Changed to 1; reran scorer. New total 10/16 |
| Minor | `run-report.txt` | First capture included PowerShell NativeCommandError lines from unittest stderr | Rewrote the report from a Python subprocess run |
| Minor | `rubric.csv` C06 | First draft left commas unquoted in the 0/1/2 anchors | Quoted before the first passing scorer run |

Follow-up QA after those edits: **pass with limitations.**

| Finding | Status |
| --- | --- |
| SYN-CASE C08 overscore | Resolved. Sheet and summary now 1 and 10/16 |
| run-report noise | Resolved. File shows VALIDATION PASSED, 3/8 and 10/16, kappa not computed, 11 tests OK |
| PLAN described as validated | Resolved. Pack sentences deny that claim |
| Second-reviewer sheet invented | Resolved. Reviewer column is only `ai-draft` |
| PDF written | Resolved. None present |
| Abstract-only sources; no body locators | Unresolved by design. Brief forbade web retrieval |
| No second reviewer; kappa not computed | Unresolved. A human reviewer is required |
| Circularity: scored papers are the rubric sources | Unresolved. Totals test consistency only |
| SYN-PLAN C03 (0 vs 1) | Unresolved. Human judgment |

Acceptance check: C02 traces to model-performance reporting for comparison (SYN-PLAN Abstract). C05 traces to feasibility and acceptance as separate questions (SYN-CASE Abstract). Support levels are `adapted` (C01) and `abstract-only` (C02–C08). `full-text` is unused.
