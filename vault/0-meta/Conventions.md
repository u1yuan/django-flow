---
title: Conventions
type: meta
tags:
  - meta
---

# Conventions

This note is the linking and archive reference for the thesis vault.

## Properties

- Use ISO dates: `YYYY-MM-DD`.
- Quote wikilinks in YAML: `project: "[[Thesis]]"`.
- Set `track` to `hydroponics`, `diesel`, or `shared`.
- The hydroponics title and the diesel title stay in separate notes unless `track` is `shared`.
- A diesel note must not claim that an anomaly caused a fault.

## Folders

| Folder           | What belongs there          |
| ---------------- | --------------------------- |
| `0-meta/`        | Vault conventions           |
| `1-plan/weekly/` | Weekly thesis logs          |
| `2-projects/`    | Project notes               |
| `3-notes/`       | Meetings and fleeting notes |
| `4-tasks/`       | One task per file           |
| `5-archives/`    | Completed or canceled notes |
| `_templates/`    | Templater templates         |
| `Tasks.base`     | The task tracker            |

## Tasks

Every task is one note with `type: task` and the properties in `_templates/tpl-task.md`. New task notes go in `4-tasks/`. `Tasks.base` is the tracker: it collects every note whose `type` is `task`, so a task stays tracked after it moves to `5-archives/`. A checkbox in the body of a note is a sub-step of that note's task, so it is not a task on its own.

A task reaches the right view when `status` is one of the values in the template and `due` and `scheduled` are ISO dates or blank. Set `project` to a quoted wikilink so the task shows in that project's note. Set `track` to group the task in the `Open` view.

Views: `Open`, `Overdue`, `Today`, `Upcoming`, `Inbox`, `This project`, `Done`. Embed one with `![[Tasks.base#Open]]`. `This project` compares `project` against `this`, so it lists the tasks of whichever note holds the embed.

Edit views in Obsidian, or in `Tasks.base` directly. Obsidian rewrites that file when you change a view, so keep hand edits small.

## Archive

Move a completed or canceled note to `5-archives/` and keep the same relative path. Example: `4-tasks/draft-protocol.md` becomes `5-archives/4-tasks/draft-protocol.md`. Set `status` to `completed` or `canceled` before the move.

## Literature

Source files under `docs/activities/litReview/` stay in that folder. A vault note may link to a repository path. A link is not a verified citation.

## Templates

Files in `_templates/` may contain Templater tags. Notes created from those templates must contain resolved values, not `<% %>` tags.
