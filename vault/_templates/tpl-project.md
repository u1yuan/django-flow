<%*
const status = await tp.system.suggester(
  ["ongoing", "on hold", "completed", "canceled"],
  ["ongoing", "on hold", "completed", "canceled"],
  false,
  "Status"
);
const priority = await tp.system.suggester(
  ["high", "medium", "low"],
  ["high", "medium", "low"],
  false,
  "Priority"
);
const track = await tp.system.suggester(
  ["Hydroponics", "Diesel", "Shared"],
  ["hydroponics", "diesel", "shared"],
  false,
  "Track"
);
const deadline = await tp.system.prompt("Deadline (YYYY-MM-DD, blank for none)", "");
-%>
---
type: project
status: <% status %>
priority: <% priority %>
track: <% track %>
deadline: <% deadline %>
tags:
  - thesis
  - project
created: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

## Overview

## Tasks

![[Tasks.base#This project]]

Task notes belong in `4-tasks/`. Set each task's project property to `"[[<% tp.file.title %>]]"` to list it above.

## Notes

Keep hydroponics and diesel work in separate notes when this project's track is not `shared`.
