# AI interaction log

Activity label: AI-Assisted (thesis pack build). The group still has to verify accuracy.

## Session

- Date: 2026-10-31
- Reviewer label used in scores: `ai-draft`
- Task: build a paper-evaluation pack from two SYNTHETIC abstracts only; score both papers; run scorer and tests; save `run-report.txt`
- Model / agent: Cursor Grok 4.6 (subagent of the parent coding agent)
- Skill used: none. The paper-evaluation skill folder was not used as a method source. `docs/activities/litReview/paper-evaluation` was not read.

## Inputs the model was allowed to read

1. `SYNTHETIC_paper_plan.txt` — invented research-plan abstract. No results.
2. `SYNTHETIC_paper_casestudy.txt` — invented case-study abstract.

No web retrieval. No PDFs saved. No git commit or push. Python standard library only.

## Prompts (substance)

Build a pack whose criteria come only from the two SYNTHETIC papers. Write only under `paper-evaluation-workspace/iteration-1/build-pack-from-abstracts/without_skill/outputs`. Include README, source-trace.md, rubric.csv, desk-check-checklist.md, templates/evaluation-template.md, scores/scores.csv, scripts/score_papers.py, scripts/tests with a SYNTHETIC fixture, AI_INTERACTION_LOG.md. Tag each criterion `full-text`, `abstract-only`, or `adapted`. Score both papers as ai-draft. Run scorer and tests. Save `run-report.txt`. Do not invent a second reviewer. Never call the PLAN framework validated.

## What the model produced

- Rubric of 15 criteria: 13 `abstract-only`, 2 `adapted`, 0 `full-text` (no body text existed).
- Desk-check checklist that treats desk-checking as pre-check-in self-review, not inspection.
- ai-draft scores for `SYNTHETIC_PLAN` (sum 16 / 30) and `SYNTHETIC_CASE` (sum 19 / 30).
- Stdlib scorer and unittest with `SYNTHETIC_rubric.csv` / `SYNTHETIC_scores.csv`.

## Claims the model must not make

- The SYNTHETIC papers are not real publications.
- PLAN is a research plan with no results. Expert validation is a planned method only.
- **Do not call the PLAN framework validated.**
- CASE reports feasibility, a modeling-language limit, and developer acceptance. That is the reported limit of that study.

## Human verification still required

- Confirm excerpts in `source-trace.md` match the SYNTHETIC files.
- Confirm scores in `scores/scores.csv` match the abstracts.
- Confirm tests and `run-report.txt` were generated from this pack, not copied from another iteration.
