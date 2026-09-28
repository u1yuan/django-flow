# Research agent team

Start a research workflow by invoking `$research-coordination` with a question, deliverable, and available inputs. The coordinator reads the role profiles here, creates a bounded brief for each needed role, and uses Codex's native subagent tools. These Markdown files describe roles; they do not start agents or grant tools or data access. A single agent may handle a small dependent task when delegation adds no value.

| Profile | Skill | Handoff |
| --- | --- | --- |
| [Coordinator](coordinator.md) | `$research-coordination` | Briefs, integrated result, QA status |
| [Literature researcher](literature-researcher.md) | `$evidence-research` | Evidence ledger and gaps |
| [Statistical analyst](statistical-analyst.md) | `$quantitative-analysis` | Reproducible analysis and limitations |
| [Writer](writer.md) | `$research-writing` | Draft with claim provenance |
| [QA](qa.md) | `$research-quality-review` | Findings with severity and evidence |

## Required task brief

Pass all six fields to every subagent. Mark unavailable inputs explicitly instead of filling gaps with guesses.

```text
Research question or topic:
Requested output:
Input locations:
Constraints:
Acceptance criteria:
Data handling restrictions:
```

Add an output path or return format, dependencies, and a deadline only when relevant. Assign independent work in parallel; wait for its artifacts before drafting or checking dependent claims. Each role returns artifact locations, evidence or run identifiers, limitations, and open questions. The coordinator retains responsibility for synthesis and sends substantive outputs through QA. For a material QA finding, return the finding to the responsible role and run one follow-up QA pass; report anything unresolved.

For example, one brief may concern diesel generator efficiency anomalies and another multi-zone hydroponic sensor consistency. Their names and methods belong in their briefs, never in the reusable profiles or skills. Check data availability before promising an analysis for either.

Codex's [multi-agent guidance](https://developers.openai.com/api/docs/guides/agents-api/multi-agent) recommends bounded independent tasks and coordination for shared-file edits. Its [skills guidance](https://developers.openai.com/api/docs/guides/tools-skills) distinguishes reusable `SKILL.md` instructions from the running agent.
