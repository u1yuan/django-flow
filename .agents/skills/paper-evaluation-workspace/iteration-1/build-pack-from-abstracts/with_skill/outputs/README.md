# Paper-evaluation pack (SYNTHETIC sources)

Track: shared. This pack scores research papers with criteria taken only from two invented SYNTHETIC abstracts supplied in the brief:

- **SYN-PLAN:** *A Quality-Task Checklist for Model Comparison — A Research Plan.* Local file `evals/files/SYNTHETIC_paper_plan.txt`. A research plan with no results. Its planned quality-assurance guidelines are not a validated framework.
- **SYN-CASE:** *A Case Study on Desk-Checking and Variability Coverage.* Local file `evals/files/SYNTHETIC_paper_casestudy.txt`. A completed case study abstract.

No PDF or full-text body is stored here. Quotes are 25 words or fewer. DOI, authors, venue, and pages are unavailable; none were invented.

The papers being scored are also the rubric's sources. Totals test consistency of the rubric against those abstracts. They are not independent evidence that the rubric is valid, and they are not a quality ranking of the two papers.

## Files

| File | Role |
| --- | --- |
| `source-trace.md` | Local paths, access date, abstract-only access, and locator limits |
| `concept-extraction.md` | QA concepts from each abstract, with confirmed or discarded seeds |
| `rubric.csv` | 8 criteria, scored 0–2 (`rubric_version` 1.0.0) |
| `desk-check-checklist.md` | Single-reviewer pass to complete before scoring |
| `templates/evaluation-template.md` | Per-paper evaluation form |
| `evaluations/` | Completed forms: `SYN-PLAN_ai-draft.md` and `SYN-CASE_ai-draft.md` |
| `scores/scores.csv` | One row per paper, reviewer, and criterion |
| `scores/summary.csv` | Written by the scorer. Do not edit by hand |
| `scripts/score_papers.py` | Copied from the paper-evaluation skill. Standard library only |
| `scripts/tests/` | Unit tests. Fixtures are named and headed `SYNTHETIC` |
| `AI_INTERACTION_LOG.md` | Prompts, outputs, QA, and the human verification list |
| `run-report.txt` | Scorer stdout and unittest output from this pack folder |

## Run order

1. **Retrieve.** For this pack the sources are the two local SYNTHETIC files. Record path, access date, and access level in the evaluation form. An abstract supports only what it states.
2. **Desk-check.** Work through `desk-check-checklist.md` and record the results in the form.
3. **Score.** Copy `templates/evaluation-template.md` to `evaluations/<paper_id>_<reviewer>.md`. Score every criterion using `rubric.csv`. Keep a location and a quote of 25 words or fewer.
4. **Enter.** Add one row per criterion to `scores/scores.csv`. The script rejects incomplete sheets.
5. **Run the script and tests** from this folder:

   ```text
   python -B scripts/score_papers.py
   python -B -m unittest discover -s scripts/tests -v
   ```

   `-B` stops Python writing `__pycache__`. A failing run is a failed result. Do not edit `summary.csv` by hand.

## Inputs and outputs

- **Inputs:** `rubric.csv` and `scores/scores.csv`. The header must match the script exactly.
- **Validation** (exit 1, summary not written) catches unknown IDs, out-of-range scores, missing `evidence_location`, NA without `NA allowed if` or without a note, a version mismatch, duplicates, conflicting DOIs, and a missing criterion on a sheet.
- **Outputs:** stdout and `scores/summary.csv`.
  - `total` rows: points, max points, and NA count per paper and reviewer. NA criteria are dropped from `max_points`.
  - `kappa` rows: unweighted Cohen's kappa per criterion for each pair of reviewers who scored the same papers. Labels `0`, `1`, `2`, and `NA` are categories.
- **Determinism:** sorted rows, four decimal places, no clock.
- **Kappa status:** `undefined` when expected agreement is 1; `unstable` when reviewers share fewer than two papers.

With one reviewer, kappa is not computed. A second independent reviewer is required before kappa is meaningful. Kappa on a single shared paper is unstable.

## How a new reviewer reproduces a score

1. Use `rubric_version` 1.0.0. If anchors change, bump the version and rescore. Do not mix versions.
2. Read the same local copies listed in `source-trace.md`. Use Title and Abstract as locators.
3. Complete the desk-check, then score every criterion **without reading** `evaluations/*_ai-draft.md` or `scores/scores.csv`.
4. Add rows under your own reviewer label. Run the script. Kappa rows for your pair with `ai-draft` appear only after that second sheet exists.
5. To reproduce one score, open the recorded location, read the quote in context, and apply the anchor's minimum condition.

Do not invent a second reviewer sheet to obtain kappa.

## Support levels

- **full-text:** a body passage was opened. **Not used** (0). Both sources are abstracts only.
- **abstract-only:** the concept is a sentence in the supplied Abstract or Title.
- **adapted:** the criterion extends a stated label to a scoring rule the source does not state.

The 0/1/2 anchors are operational wording in every case.

| Support level | Criteria | Count |
| --- | --- | --- |
| full-text | none | 0 |
| abstract-only | C02–C08 | 7 |
| adapted | C01 | 1 |

## Pilot (reviewer `ai-draft`, 2026-10-31)

See `run-report.txt` and `scores/summary.csv` for the machine totals after the scorer run. Expected from the entered sheet:

| Paper | Total | Note |
| --- | --- | --- |
| SYN-PLAN | 3/8 | Plan abstract. Four NA criteria. Planned guidelines are not treated as validated |
| SYN-CASE | 10/16 | Completed case-study abstract. No NA |

**Interpretation limit.** These totals test that the rubric can be applied to its own source abstracts. They do not validate the SYN-PLAN framework, and they do not rank the two papers. SYN-CASE scores higher in part because several criteria were taken from its abstract. SYN-PLAN scores lower in part because it is a plan and several criteria reward reported evidence a plan cannot yet have.

## Open items for a human

See `AI_INTERACTION_LOG.md` § "What a human must verify".
