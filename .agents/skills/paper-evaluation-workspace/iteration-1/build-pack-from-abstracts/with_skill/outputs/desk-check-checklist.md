# Desk-check checklist (one reviewer, before scoring)

Complete this pass for each paper before entering any score. Record the result in the Desk-check section of that paper's evaluation file.

**Origin.** The pass adapts the SYN-CASE abstract: desk-checking is a checklist-guided self-review before check-in, not a structured inspection. Using that sentence as a paper-evaluation step is an adaptation. Each item states the minimum that counts as done.

| # | Item | Minimum requirement to tick |
| --- | --- | --- |
| 1 | **Identity.** Title and any bibliographic fields match the copy used | The copy is named. Unavailable authors, venue, pages, or DOI are written as unavailable. None of those fields is invented |
| 2 | **Copy used.** Local SYNTHETIC file, publisher, reprint, or preprint | Path or URL and access date recorded |
| 3 | **Access level.** Full text or abstract only | Recorded. If abstract only, every criterion the abstract does not address is scored from that abstract or marked NA where the guiding question allows it |
| 4 | **Locator scheme.** Pages, sections, Title, or Abstract | Chosen and stated. Page numbers that cannot be seen are `[unverified]`, never estimated |
| 5 | **Full read without scoring** | Every heading in the copy is listed once |
| 6 | **Study status.** Plan, protocol, or completed study | Decided from the title, abstract, and verb tense, with the location noted. A plan is not treated as validated work |
| 7 | **Rubric version** | The `rubric_version` from `rubric.csv` is copied into the evaluation file and the score rows |
| 8 | **Evidence search for each criterion** | For each criterion, either a location or the parts searched without finding evidence (for example, "searched Abstract: none") |
| 9 | **Quotes** | Copied verbatim, 25 words or fewer, each with a locator |
| 10 | **NA decisions** | NA only where the guiding question contains `NA allowed if`, with the condition restated in the note |
| 11 | **Circularity.** Is this paper a source of the rubric? | If yes, the evaluation says the scores test rubric consistency only |
| 12 | **Integrity** | No PDF or full text saved. No claim that a plan's framework was validated. No invented page numbers, scores, citations, or second reviewer |

After the checklist is complete, score each criterion with `rubric.csv`, enter the rows in `scores/scores.csv`, and run the script (see `README.md`).
