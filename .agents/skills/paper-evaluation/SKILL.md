---
name: paper-evaluation
description: Build and run a reproducible research-paper evaluation workflow whose criteria come only from named source papers. Use whenever the user asks to score papers, build a paper-evaluation rubric, desk-check a paper, compute Cohen's kappa across reviewers, or turn QA concepts from specific papers into a scored pack — even if they do not say rubric or skill.
---

# Paper evaluation

Read this file first. Read `references/integrity.md` before retrieving any paper. Read `references/pack-layout.md` before writing pack files. Use the bundled scorer at `scripts/score_papers.py` rather than rewriting it.

Source paper titles, methods, and output paths come from the **task brief**, not from this skill. Do not hard-code a research topic, dataset, or a prior worked example's criteria into a new pack.

Use `$evidence-research` and `$citation-management` for retrieval and metadata. Use `$quantitative-analysis` / `$statistical-analysis` if a reviewer asks for a different agreement statistic than the bundled unweighted kappa. Send every finished pack through `$research-quality-review`.

## Brief

If any field is missing, mark it unavailable. Do not invent a substitute.

```text
Research question or topic:
Requested output:
Input locations:
Constraints:
Acceptance criteria:
Data handling restrictions:
```

Required inputs from the brief: the source papers that **define** the criteria, the papers to **score** (they may be the same set), the output folder, and the reviewer label. If the brief names no output folder, ask once; do not write into an unrelated tree.

## Run order

1. **Retrieve** each source paper. Record URL, access date, and access level (full text or abstract only) in `source-trace.md`. An abstract supports only what it states. If **no** source paper's full text can be obtained, stop and tell the user what abstract-only scoring would lose, then wait.
2. **Extract** QA concepts with locators. Confirm or discard any candidate seeds the brief lists against the source text. Quotes are 25 words or fewer. Unverified pages are `[unverified]`.
3. **Build** the pack in the brief's output folder. File list and column names are in `references/pack-layout.md`. Copy `scripts/score_papers.py` into that pack's `scripts/` folder. Every criterion must name a source paper and a location. Tag `support_level` as `full-text`, `abstract-only`, or `adapted`.
4. **Desk-check** each paper to be scored before entering any score.
5. **Pilot-score** only as the reviewer label the brief gives. Do not invent a second reviewer. A plan or proposal is not validated work.
6. **Run** the scorer and its tests from the pack folder:

   ```text
   python -B scripts/score_papers.py
   python -B -m unittest discover -s scripts/tests -v
   ```

   A failing run is a failed result. After two failed fix attempts, stop and report the error.
7. **QA.** Route the pack through `$research-quality-review`. Apply one revision for material findings, then one follow-up QA pass. List anything still unresolved.

## Scoring rules

- Scores are `0`, `1`, `2`, or `NA`. `NA` is allowed only when that criterion's guiding question contains `NA allowed if`, and the score row must have a note.
- Every score row needs a non-empty `evidence_location`.
- Totals drop `NA` criteria from `max_points`.
- Cohen's kappa is unweighted. Labels `0`, `1`, `2`, and `NA` are categories. Compute it per criterion for each pair of reviewers who scored the same papers. With one reviewer, report that kappa was not computed. Do not fabricate the second sheet.
- Kappa on a single shared paper is unstable; say so.
- If the papers being scored are also the rubric's sources, say that the totals test consistency only.

## Stop and ask

Stop before installing packages, committing or pushing, writing outside the brief's folder, or continuing after neither source paper's full text can be obtained.
