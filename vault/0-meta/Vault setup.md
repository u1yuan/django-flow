---
title: Vault setup
type: meta
tags:
  - meta
---

# Vault setup

Open the `vault` folder as its own Obsidian vault. Notes in this folder are the thesis notebook. Literature files stay in `docs/activities/litReview/`.

## Templater

1. In Obsidian, choose **Open folder as vault** and select this `vault` directory.
2. Open **Settings → Community plugins**, turn community plugins on, and install **Templater**.
3. Enable Templater.
4. In Templater settings, set **Template folder location** to `_templates`.

Insert a template from the command palette with **Templater: Open insert template modal**. The templates use Templater prompts (`<% %>`). The core Templates plugin is off so it does not insert those tags as plain text.

## Where new notes go

| Template | Folder |
| --- | --- |
| `tpl-thesis-meeting` | `3-notes/` |
| `tpl-fleeting-note` | `3-notes/` |
| `tpl-thesis-log` | `1-plan/weekly/` |
| `tpl-project` | `2-projects/` |
| `tpl-task` | `4-tasks/` |

New files start in `3-notes/`. Move a log, project, or task into the folder in the table after you insert the template.

## Tasks

`Tasks.base` at the vault root is the task list. Open it to see every task note, or read a single view where you need it: project notes embed `This project` and weekly logs embed `Open`. Bases is a core plugin, so nothing needs installing. Tracking rules are in [[Conventions]].

## Track

Every firsthand template asks for a track: `hydroponics`, `diesel`, or `shared`. Keep the hydroponics title and the diesel title in separate notes unless the note is explicitly shared.

Linking and archive rules are in [[Conventions]].
