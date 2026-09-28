---
name: quantitative-analysis
description: Assess and analyze authorized research data with reproducible calculations, assumptions, and limitations. Use for data feasibility, exploratory inspection, statistical analysis, or results handoff.
---

# Quantitative analysis

Read the brief and identify the research question, data location, authorization, unit of observation, variables, design, and requested result. Use `../exploratory-data-analysis/SKILL.md` to inspect supported local formats and data quality within its security boundaries. Use `../statistical-analysis/SKILL.md` to choose tests, check assumptions, calculate effects and uncertainty, and report results when inference is warranted.

Separate observed data, preprocessing decisions, exploratory patterns, and confirmatory claims. Preserve raw data; document exclusions, missingness, units, denominators, grouping, time alignment, and potential leakage. Run code only against authorized inputs. Keep executable code, environment or version notes, parameters, and output artifacts sufficient to reproduce numeric results. Check key calculations independently where practical.

If data are absent, unsupported, too sparse, or missing required fields, stop short of statistical claims. Return the exact data requirements and what can still be assessed. If code fails, report the failure and affected results; fix and rerun where within scope, otherwise mark those results unavailable.
