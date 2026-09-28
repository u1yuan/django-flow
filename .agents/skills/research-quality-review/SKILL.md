---
name: research-quality-review
description: Independently review research prose, evidence, statistics, and code against a task brief and source artifacts. Use after substantive research output or for a focused research QA request.
---

# Research quality review

Read the brief, deliverable, and underlying source or run artifacts. Use `../citation-management/SKILL.md` for bibliographic checks, `../scientific-writing/SKILL.md` for claim and consistency audits, and `../statistical-analysis/SKILL.md` or `../exploratory-data-analysis/SKILL.md` for relevant numerical and data checks. Review only the modes present in the deliverable.

Check each material claim against its cited passage or result, including direction, population, units, uncertainty, and citation metadata. Recompute important numbers from available inputs. Run or inspect supplied code within the brief's permissions; a failing run is a finding, not a successful result. Check whether acceptance criteria are met and whether limitations expose missing or unsuitable data.

Return a finding list with severity, artifact location, supporting evidence, and correction or needed input. Distinguish **pass**, **pass with limitations**, and **needs revision**. Flag unverifiable claims without inventing a substitute citation. For a follow-up review, check the actual changed artifact and report each finding as resolved or unresolved. Remain independent of drafting and analysis.
