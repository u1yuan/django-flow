---
name: research-coordination
description: Coordinate a bounded research request across literature, quantitative analysis, writing, and independent QA. Use when a research deliverable needs several roles or explicit evidence and QA handoffs; invoke as $research-coordination.
---

# Research coordination

Read `../../agents/README.md` and `../../agents/coordinator.md`, then only the role profiles needed for this request. A profile is a task definition, not an active agent. Use Codex's native subagent tools for independent bounded tasks when available; handle short or dependent steps directly. Coordinate edits to shared files.

Write a brief for every assigned role with: **research question or topic, requested output, input locations, constraints, acceptance criteria, data handling restrictions**. Name absent inputs explicitly. The active topic and methods come from the brief, not this skill. Specify return artifacts and dependencies. Literature search and authorized data inspection can run independently; prose that claims results waits for verified evidence and analysis.

Collect each role's artifacts, evidence or run IDs, limitations, and open questions. Check contradictions against sources or calculations before synthesis. Route every substantive deliverable through `$research-quality-review` using `../../agents/qa.md`. For a material finding, send it to the responsible role, inspect the revision, and run one follow-up QA pass. Update the final QA status after that pass so it does not still say "pending"; if the pass cannot run, state that limit. Stop the loop there and report unresolved findings clearly.

Return the requested output with traceable evidence, concrete limitations, and QA status. Do not imply unavailable data were analyzed or a citation was verified merely because it appears in a repository file.
