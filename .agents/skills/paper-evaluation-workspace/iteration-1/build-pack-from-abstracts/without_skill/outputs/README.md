# Paper-evaluation pack (abstract-derived, SYNTHETIC sources)

Reviewer label for this build: **ai-draft**.

This pack scores papers against a rubric taken only from two invented SYNTHETIC texts (not real publications). No web retrieval, no PDFs, and no second reviewer were used.

**Constraint:** Paper PLAN is a research plan with no results. Do not call the PLAN framework validated.

## Sources (read-only; not copied here)

| ID | File | Genre |
| --- | --- | --- |
| PLAN | `SYNTHETIC_paper_plan.txt` | Research plan. Three gaps, three planned methods, no results. |
| CASE | `SYNTHETIC_paper_casestudy.txt` | Case study. Feasibility and acceptance as separate questions; desk-checking defined as pre-check-in self-review. |

## Criterion tags

Every rubric row is tagged:

- `abstract-only` — wording taken from a SYNTHETIC abstract.
- `adapted` — combined or rephrased from both abstracts for pack use.
- `full-text` — reserved for body text. **None** in this pack: the SYNTHETIC files contain title plus abstract only.

See `source-trace.md` for the excerpt behind each row.

## Pack layout

| Path | Role |
| --- | --- |
| `source-trace.md` | Criterion-to-excerpt map |
| `rubric.csv` | Scored criteria, tags, 0–2 scale |
| `desk-check-checklist.md` | Pre-check-in self-review checklist (not a structured inspection) |
| `templates/evaluation-template.md` | Blank evaluation form |
| `scores/scores.csv` | ai-draft scores for both SYNTHETIC papers |
| `scripts/score_papers.py` | Stdlib scorer |
| `scripts/tests/` | Unittest plus SYNTHETIC fixtures |
| `AI_INTERACTION_LOG.md` | AI-assisted work log |
| `run-report.txt` | Scorer output from this run |

## How to score

1. Desk-check the target paper with `desk-check-checklist.md` (self-review, not inspection).
2. Fill `templates/evaluation-template.md` or add rows to `scores/scores.csv`.
3. Use only the reviewer label **ai-draft** unless a human later replaces this draft.
4. Run the scorer (Python 3, standard library only):

```text
python scripts/score_papers.py --out run-report.txt
```

Optional flags: `--rubric`, `--scores`, `--reviewer`, `--pack-root`.

5. Run tests:

```text
python -m unittest discover -s scripts/tests -v
```

## Scoring rules

- Scale: `0` absent, `1` partial, `2` fully addressed. `NA` is allowed and excluded from totals.
- One reviewer in this pack: `ai-draft`.
- A planned literature study, expert validation, or two-team pilot in PLAN is a **method plan**, not a completed result.
- Desk-checking in this pack means checklist-guided self-review before check-in. It is not a structured inspection.
- Feasibility and acceptance are separate questions (CASE).
- Variability modeling that cannot represent all important variants must be recorded as a limit, not as full coverage.

## What this pack does not claim

- The SYNTHETIC papers are not real.
- PLAN methods were not executed here.
- Expert validation listed in PLAN does not validate a framework.
- CASE reports feasibility, a modeling-language limit, and developer acceptance. That is the reported limit of that study.
