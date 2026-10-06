# Vault Schema Reference

**Vault root:** `vault/` at the repository root (the parent directory of `.agents`)

**Canonical conventions:** See `0-meta/Conventions.md` in the vault. This document extends that file for Secretary sub-agents.

---

## Folder Map (PARA + numbered)

| Folder | Purpose | Note types |
|--------|---------|------------|
| `0-meta/` | Vault metadata, conventions | meta |
| `1-plan/` | Weekly thesis logs. Daily, monthly, quarterly, and yearly notes go in subfolders when they exist | daily, log |
| `2-projects/` | Project notes, and goal notes when a goal is its own file | project, goal |
| `3-notes/` | Meetings, fleeting notes, people, organizations | note, meeting, person, organization |
| `4-tasks/` | Task notes, one task per file | task |
| `5-archives/` | Completed or canceled notes, mirroring the original path | any |
| `Tasks.base` | Task tracker at the vault root | — do not edit |
| `_templates/` | Templater templates | — reference only |

**Triage rules:**
- New tasks → `4-tasks/`
- New projects → `2-projects/` (subfolder if multi-file project)
- New goals → `2-projects/`
- New areas → `3-notes/`
- Meetings, fleeting notes → `3-notes/` (subfolder by topic if clustered)
- People → `3-notes/`
- Organizations → `3-notes/`
- Completed/canceled items → `5-archives/<original-path>`

---

## Linking Conventions

### YAML frontmatter wikilinks (required)

All inter-note references in YAML **must** use quoted wikilink form:

```yaml
project: "[[ACM TechSprint Asteria 2026]]"
area: "[[fit-acm]]"
goal: "[[Midterm Proficiency]]"
person: "[[Eron Diaz]]"
```

Bare strings will NOT update on rename. Setting: **Automatically update internal links** (enabled).

### Body wikilinks

Use standard `[[Note Name]]` or `[[path/to/note|Display]]` in markdown body.

### Attendees (meeting notes)

```yaml
attendees:
  - "[[Eron Diaz]]"
  - "[[Valirie Turbanos]]"
```

---

## Frontmatter Schemas

Secretary agents write **resolved values** (no Templater tags). Match `_templates/tpl-*.md` structure.

### daily

```yaml
---
type: daily
date: 2026-06-20
tags:
  - plan/daily
---
```

**Body sections:** nav links (prev/next day), Bases embeds (Overdue, Today, Upcoming, Inbox, Meetings, Projects), Daily Journal prompts.

**Template:** `_templates/tpl-daily.md`

### task

```yaml
---
type: task
status: todo          # todo | doing | in-progress | waiting | in-review | on-hold | done | completed | canceled | archived
priority: high        # high | medium | low | none
track: diesel         # hydroponics | diesel | shared
due: 2026-06-22       # ISO date or empty
scheduled: 2026-06-20 # ISO date or empty
project: "[[project-name]]"
person:               # optional wikilink
tags: []
created: 2026-06-20
---
```

`type`, `status`, `track`, `due`, `scheduled`, and `project` are what place a task on `Tasks.base`. A task without `type: task` is untracked.

**Body:** `# Title`, `## Notes and sub-tasks` with checkboxes for sub-steps.

**Folder:** `4-tasks/` | **Template:** `_templates/tpl-task.md`

### project

```yaml
---
type: project
status: ongoing       # ongoing | on hold | completed | canceled
priority: high        # high | medium | low
goal: "[[goal-name]]"
area: "[[area-name]]"
deadline: 2027-06-30
completed_date:
tags: []
created: 2026-06-20
---
```

**Body:** SMART outcome block, Overview, Remaining/Completed task embeds, Notes & References.

**Folder:** `2-projects/` | **Template:** `_templates/tpl-project.md`

### goal

```yaml
---
type: goal
status: ongoing
area: "[[area-name]]"
target_date: 2026-12-31
achieved_date:
tags: []
created: 2026-06-20
---
```

**Folder:** `2-projects/` | **Template:** `_templates/tpl-goal.md`

### area

```yaml
---
type: area
tags: []
created: 2026-06-20
---
```

**Body:** Overview, Active Goals/Projects embeds, Notes & Resources.

**Folder:** `3-notes/` | **Template:** `_templates/tpl-area.md`

### meeting

```yaml
---
type: meeting
scheduled: 2026-06-02
location: MS Teams
tags:
  - notes/meeting
attendees:
  - "[[Person Name]]"
project: "[[Project Name]]"
created: 2026-06-02
---
```

**Body:** Date/Location/Attendees header, Agenda, Notes, Action Items (wikilink tasks in `4-tasks/`).

**Folder:** `3-notes/` | **Template:** `_templates/tpl-meeting.md`

### person

```yaml
---
type: person
role: Title
organization: "[[Org Name]]"
email:
phone:
last_contact:
status: Active        # Active | Inactive | Lead | Partner
tags:
  - notes/people
created: 2026-06-20
---
```

**Folder:** `3-notes/` | **Template:** `_templates/tpl-person.md`

### fleeting note

```yaml
---
type: note
tags: []
related:
created: 2026-06-20
---
```

**Folder:** `3-notes/` | **Template:** `_templates/tpl-fleeting-note.md`

---

## Obsidian Bases

Agents **never modify** `.base` files. Ensure correct frontmatter so notes appear in views.

`Tasks.base` at the vault root is the only base. It is the task tracker.

- **Source:** every markdown note with `type: task`, in any folder, including archived tasks
- **Key properties:** status, track, due, scheduled, priority, project
- **Views:** Open (grouped by track), Overdue, Today, Upcoming (14 days), Inbox (no due and no scheduled), This project (`project == this`), Done
- **Open statuses:** not done/completed/canceled/archived
- **Embeds:** `![[Tasks.base#This project]]` in a project note, `![[Tasks.base#Open]]` in a weekly log

```markdown
![[Tasks.base#Overdue]]
![[Tasks.base#Today]]
```

---

## Task Formats

### Task notes (the only tracked form)

One task per file in `4-tasks/` with the YAML properties above. `Tasks.base` reads those properties and is the tracker. Write the frontmatter so a new task lands on the right views.

### Inline checkboxes (sub-steps only)

A checkbox belongs under `## Notes and sub-tasks` in a task note, or as a step inside another note. It is not a tracked task.

```markdown
- [ ] Sub-step of this note's task
- [x] Finished sub-step ✅ 2026-06-20
```

When a checkbox in a meeting or log note describes real work, propose a task note in `4-tasks/` for it and wikilink the note to that task.

### Queries in other notes

Use a Bases embed such as `![[Tasks.base#Open]]`. Do not add `tasks` or `dataview` query blocks for tracking; they bypass the Base.

---

## Periodic Notes

Driven by **Periodic Notes** plugin (not core Daily Notes):

| Period | Format | Folder | Template |
|--------|--------|--------|----------|
| Daily | `YYYY-MM-DD` | `1-plan/daily` | `_templates/tpl-daily.md` |
| Weekly | `YYYY-[W]WW` | `1-plan/weekly` | `_templates/tpl-weekly.md` |
| Monthly | `YYYY-MM` | `1-plan/monthly` | `_templates/tpl-monthly.md` |
| Quarterly | `YYYY-[Q]Q` | `1-plan/quarterly` | `_templates/tpl-quarterly.md` |
| Yearly | `YYYY` | `1-plan/yearly` | `_templates/tpl-yearly.md` |

**Dates:** Always ISO `YYYY-MM-DD`. Natural language dates should resolve to this format.

---

## QuickAdd Commands (existing automation)

Secretary complements — does not duplicate — these commands.

### Template commands

| Command | Template | Target folder |
|---------|----------|---------------|
| Add Course Module | `tpl-course-module.md` | `2-projects/11-courses/modules` |
| New Task | `tpl-task.md` | `4-tasks` |
| New Project | `tpl-project.md` | `2-projects` |
| New Goal | `tpl-goal.md` | `2-projects` |
| New Area | `tpl-area.md` | `3-notes` |
| New Person | `tpl-person.md` | `3-notes` |
| New Organization | `tpl-organization.md` | `3-notes` |
| New Meeting | `tpl-meeting.md` | `3-notes` |
| New Fleeting Note | `tpl-fleeting-note.md` | `3-notes` |
| New Cornell Note | `tpl-cornell.md` | `3-notes` |

### Macros

| Macro | Script | Behavior |
|-------|--------|----------|
| Archive (recursive) | `_scripts/archive-recursive.js` | Set status completed/canceled, move to `5-archives/<path>`, offer co-archive backlinks |
| Self Test | `_scripts/quickadd-self-test.js` | QuickAdd validation |

**When Secretary archives:** Mirror Archive macro logic — update frontmatter status, move to `5-archives/<mirror-path>`, update backlinks in dependent notes.

---

## Templater Syntax (templates only)

Templates use Templater; Secretary writes resolved output:

| Pattern | Meaning |
|---------|---------|
| `<% tp.date.now("YYYY-MM-DD") %>` | Today's date |
| `<% tp.date.now("dddd, MMMM D, YYYY") %>` | Formatted date |
| `<% tp.date.now("YYYY-MM-DD", -1) %>` | Yesterday |
| `<% tp.file.title %>` | Note filename |

**Secretary rule:** Never write Templater tags into vault files. Resolve to literal values.

---

## Status Enums

| Type | Valid status values |
|------|---------------------|
| task | todo, doing, in-progress, waiting, in-review, on-hold, done, completed, canceled, archived |
| project | ongoing, on hold, completed, canceled |
| goal | ongoing, on hold, completed, canceled |

**Archive trigger statuses:** completed, canceled

---

## Maintenance Checks

Report during any operation:

1. **Broken wikilinks** — `[[target]]` with no matching file
2. **Missing frontmatter** — note in typed folder without `type` field
3. **Wrong folder** — task in `3-notes/`, project in `4-tasks/`, etc.
4. **Unquoted YAML links** — `project: [[name]]` instead of `project: "[[name]]"`
5. **Orphan notes** — no inbound links and not in `1-plan/daily`
6. **Stale ongoing** — `status: ongoing` with `deadline` in the past

---

## Plugins (context)

| Plugin | Relevance |
|--------|-----------|
| periodic-notes | Daily/weekly/monthly note creation |
| templater-obsidian | Template folder `_templates/` |
| quickadd | Note creation commands and macros |
| dataview | Legacy queries in some notes |
| obsidian-tasks-plugin | `tasks` code blocks |
| obsidian-git | Vault sync |
| omnisearch | Enhanced search |
| bases (core) | `Tasks.base` at the vault root |
| nldates-obsidian | Natural language date parsing |
