# Pack layout

Write only the files the brief asks for. The usual pack is:

```text
<output-folder>/
  README.md
  source-trace.md
  concept-extraction.md          # optional but useful
  rubric.csv
  desk-check-checklist.md
  templates/evaluation-template.md
  evaluations/<paper_id>_<reviewer>.md
  scores/scores.csv
  scores/summary.csv             # written by the scorer; do not edit by hand
  scripts/score_papers.py        # copy from this skill's scripts/
  scripts/tests/test_score_papers.py
  scripts/tests/fixtures/        # filenames and first lines labelled SYNTHETIC
  AI_INTERACTION_LOG.md
  .gitignore                     # at least __pycache__/, *.pyc, *.pdf
```

A worked instance of this layout lives at `docs/activities/litReview/paper-evaluation/` in the thesis1 repository. Use it as a format example. Do not copy its criterion text or scores into a new pack unless the brief names the same source papers.

## `rubric.csv` columns

Exactly:

`criterion_id,rubric_version,criterion,guiding_question,score_0_anchor,score_1_anchor,score_2_anchor,source_paper,source_location,support_level`

`support_level` is one of `full-text`, `abstract-only`, `adapted`.

Each `0`/`1`/`2` anchor states an observable minimum, not a quality adjective. That pattern comes from treating subjective checklist items as needing a stated minimum.

## `scores/scores.csv` columns

Exactly:

`paper_id,doi,reviewer,rubric_version,criterion_id,score,evidence_location,note`

One row per paper, reviewer, and criterion. `rubric_version` must match the rubric.

## README

State run order, inputs, outputs, how a new reviewer reproduces a score, support-level counts, and that a second independent reviewer is required before kappa is meaningful.

## Desk-check

A single-reviewer pass before scoring. Record identity, copy used, access level, locator scheme, study status (plan vs completed), rubric version, evidence search, quote limit, NA decisions, circularity, and the no-PDF rule.

## Evaluation template

One file per paper per reviewer. Fields include DOI, access level, and, for each criterion, evidence location and a quote of 25 words or fewer.

## Tests

Label invented fixtures `SYNTHETIC` in both the filename and the first line (`# SYNTHETIC ...`). Cover unknown IDs, out-of-range scores, missing `evidence_location`, and a hand-computed kappa on a two-reviewer fixture.

## Scorer

Copy `../scripts/score_papers.py`. It validates, writes totals, and writes unweighted Cohen's kappa. Output is deterministic (sorted rows, four decimal places, no clock). Exit `1` means validation failed and `summary.csv` was not written. Exit `2` means a missing file or a wrong header.
