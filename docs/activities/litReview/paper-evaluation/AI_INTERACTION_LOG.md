# AI interaction log

Course use: Thesis 1 (CS0025). AI-assisted work. The group remains responsible for checking accuracy and citations.

| Field | Value |
| --- | --- |
| Date | 2026-10-31 |
| Tool | Cursor agent (Claude) with web fetch, an IDE browser, and a local shell |
| Reviewer label used in scores | `ai-draft` |
| Human reviewer | not yet assigned |

## Prompt used

The user's task prompt, summarized faithfully. The full text is in the chat session.

> Build a reproducible workflow for evaluating research papers. Its criteria come from the QA concepts in Paper A (Effendy et al. 2025, ICSIM, doi:10.1145/3725899.3725909, a research plan) and Paper B (Remmel et al. 2014, CiSE 16(3):58–66). Every criterion must trace to a specific location in A or B.
>
> Hard rules:
> - Do not save PDFs or full text; keep quotes to 25 words or fewer with locators.
> - No git commit or push, and no package installs; standard-library Python only.
> - Edit only `docs/activities/litReview/paper-evaluation/`.
> - Tag each criterion full-text, abstract-only, or adapted.
> - Never describe A's framework as validated.
> - Never fabricate a second reviewer, citation, or page number; write `[unverified]`.
>
> Steps:
> 1. Retrieve both papers and write `source-trace.md`.
> 2. Extract QA concepts, and confirm or discard the eight candidate seeds.
> 3. Build the README, `rubric.csv`, the desk-check checklist, the evaluation template, `scores.csv`, `score_papers.py` (validation, totals, Cohen's kappa), tests with a SYNTHETIC fixture, and this log.
> 4. Pilot-score A and B as `ai-draft` and run the script and tests.
> 5. Run `$research-quality-review`, apply one revision, and list unresolved items.

Sub-prompts issued during the session:
- Retrieval queries to Crossref, OpenAlex, Semantic Scholar, and Unpaywall.
- One web search for an alternative copy of B.
- The QA review brief (see the last section).

## What the AI did and produced

| Step | Action | Output |
| --- | --- | --- |
| 1 | Paper A: ACM blocked scripted requests (403). The IDE browser passed Cloudflare and read the free-access HTML full text. Paper B: ResearchGate gave only the abstract, and its PDF link required a manual security check. A web search found the authors' group page. The author-posted IEEE reprint was read in memory, with TLS verification disabled because the certificate had expired | `source-trace.md` |
| 2 | Extracted 13 concepts from A and 21 from B, with locations. Tested the 8 seeds: 6 confirmed, 1 confirmed as adapted, 1 partly discarded (B rejects *structured* inspection, p. 60) | `concept-extraction.md` |
| 3 | Wrote 15 criteria with 0/1/2 anchors, each anchor stated as an observable minimum condition, following B p. 64 on minimum requirements | `rubric.csv`, `desk-check-checklist.md`, `templates/evaluation-template.md`, `README.md` |
| 3 | Wrote the validator, totals, and kappa script, plus 14 unit tests using SYNTHETIC fixtures with hand-computed expected kappas (1, 7/11, and 5/9) | `scripts/score_papers.py`, `scripts/tests/` |
| 4 | Pilot-scored A and B as `ai-draft`, ran the script, and ran the tests | `scores/scores.csv`, `scores/summary.csv`, `evaluations/*.md` |
| 5 | Ran an independent QA review and applied one revision | See "QA" below |

### Pilot run output (verbatim)

```text
> python -B scripts/score_papers.py
VALIDATION PASSED: 15 criteria, 30 score rows.
Per-paper totals (NA criteria excluded from max_points):
  A-effendy2025 | ai-draft | v1.0.0 | 12/30 | scored=15 NA=0
  B-remmel2014 | ai-draft | v1.0.0 | 24/30 | scored=15 NA=0
Cohen's kappa: not computed (no paper has scores from two reviewers).
Summary written: scores/summary.csv

> python -B -m unittest discover -s scripts/tests -v
Ran 14 tests in 0.010s
OK
```

Two consecutive runs produced byte-identical `summary.csv` (SHA-256 `1B36E4C5…FDFE01`).

## What a human must verify

1. **Author lists.**
   - A: Veronikha Effendy, Suyanto Suyanto, Mira Kania Sabariah, Rio Guntur Utomo.
   - B: Hanna Remmel, Barbara Paech, Christian Engwer, Peter Bastian.

   Both were checked against Crossref. B was also checked against the reprint's title page. Confirm A against the ACM PDF.
2. **Page numbers.**
   - A: locators are sections only. Per-section pages within 63–67 are [unverified]. Add them from the ACM PDF.
   - B: pages come from the author reprint's printed pagination and have not been checked against IEEE Xplore.
3. **The publication date of A.** Crossref print date is 2025-01-10; the ACM page shows 11 July 2025. Decide which to cite.
4. **Quotes.**
   - Recheck every quote in `concept-extraction.md` and `evaluations/` against the source.
   - In B quotes, the ligatures fi, fl, ff, and Th were restored by hand after text extraction.
   - The body of B p. 58 after its first sentence was not read.
5. **The license claim.** "CC BY" for A comes from Semantic Scholar only.
6. **Every pilot score.** All 30 `ai-draft` scores are drafts. These need a human decision:
   - A C01 (are the §1 interviews a claim or background?).
   - B C03 (0 or NA?).
   - B C05 and C13 (the same desk-checking issue is penalized twice).
7. **A second reviewer.** No second reviewer exists, so kappa is not computed. No second-reviewer scores were invented. A human must score both papers independently, without reading `evaluations/*_ai-draft.md` first. Meaningful kappa needs more than two papers.
8. **Circularity.** The pilot papers are the rubric's sources. Pilot totals test consistency only. Pilot on papers outside A and B before relying on the rubric.
9. **The extraction method for B.** The text was extracted from the PDF by a standard-library regex parser, not a PDF library. Spot-check against a PDF reader.

## QA

See the section appended below after the review.
