# Desk-check checklist (one reviewer, before scoring)

Complete this pass for each paper before entering any score. Record the result in the "Desk-check" section of that paper's evaluation file.

**Origin.** The checklist adapts the desk-checking idea in Remmel et al. (2014): the author reads their own work one more time before checking it in (p. 59; checklist sidebar, p. 63). Like that paper, this is a self-review and not a structured inspection (p. 60). That paper also reports that subjective checklist items need minimum requirements (p. 64). Each item below therefore states the minimum that counts as done.

| # | Item | Minimum requirement to tick |
| --- | --- | --- |
| 1 | **Identity.** The DOI resolves and the title, authors, venue, year, and pages match a metadata source | The metadata source is named (for example, Crossref), and every mismatch is written down |
| 2 | **Copy used.** Publisher version, author reprint, or preprint | URL and access date recorded. If it is not the publisher version, say whether pagination matches the publisher's |
| 3 | **Access level.** Full text or abstract only | Recorded. If abstract only, every criterion the abstract does not address is scored with the note "abstract-only: not assessable" and listed under open items |
| 4 | **Locator scheme.** Pages, sections, or both | Chosen and stated. Page numbers that cannot be seen in the copy are written as `[unverified]`, never estimated |
| 5 | **Full read without scoring** | Every section heading has been listed once |
| 6 | **Study status.** Plan, protocol, or completed study | Decided from the title, abstract, and the tense of the method, with the location noted |
| 7 | **Rubric version** | The `rubric_version` from `rubric.csv` is copied into the evaluation file and the score rows |
| 8 | **Evidence search for each criterion** | For each criterion, either a location or the sections searched without finding evidence (for example, "searched §§1–5: none") |
| 9 | **Quotes** | Copied verbatim, 25 words or fewer, each with a locator. Text-extraction repairs (for example, restored ligatures) are flagged |
| 10 | **NA decisions** | NA only where the criterion's guiding question contains "NA allowed if", with the condition restated in the note |
| 11 | **Circularity.** Is this paper a source of the rubric? | If yes, the evaluation says that its scores test rubric consistency only and are not independent evidence |
| 12 | **Integrity** | No PDF or full text saved in the repository. No claim that a plan's framework was validated. No invented page numbers, scores, or citations |

After the checklist is complete, score each criterion with `rubric.csv`, enter the rows in `scores/scores.csv`, and run the script (see `README.md`).
