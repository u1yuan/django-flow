<%*
const status = await tp.system.suggester(
  ["todo", "doing", "in-progress", "waiting", "in-review", "on-hold", "done", "completed", "canceled", "archived"],
  ["todo", "doing", "in-progress", "waiting", "in-review", "on-hold", "done", "completed", "canceled", "archived"],
  false,
  "Status"
);
const priority = await tp.system.suggester(
  ["high", "medium", "low", "none"],
  ["high", "medium", "low", "none"],
  false,
  "Priority"
);
const track = await tp.system.suggester(
  ["Hydroponics", "Diesel", "Shared"],
  ["hydroponics", "diesel", "shared"],
  false,
  "Track"
);
const due = await tp.system.prompt("Due date (YYYY-MM-DD, blank for none)", "");
const scheduled = await tp.system.prompt("Scheduled date (YYYY-MM-DD, blank for none)", "");
const projectLink = await tp.system.prompt("Project note name", "Thesis");
const projTrim = (projectLink || "").trim();
const projLine = projTrim ? `project: "[[${projTrim}]]"` : `project: "[[Thesis]]"`;
-%>
---
type: task
status: <% status %>
priority: <% priority %>
track: <% track %>
due: <% due %>
scheduled: <% scheduled %>
<% projLine %>
tags:
  - thesis
  - task
created: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

## Notes and sub-tasks

- [ ]
