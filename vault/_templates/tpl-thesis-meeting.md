<%*
const meetingType = await tp.system.suggester(
  ["Adviser meeting", "Group meeting", "Panel / defense meeting", "Other"],
  ["adviser", "group", "panel", "other"],
  false,
  "Meeting type"
);
const track = await tp.system.suggester(
  ["Hydroponics", "Diesel", "Shared"],
  ["hydroponics", "diesel", "shared"],
  false,
  "Track"
);
const location = await tp.system.prompt("Location / platform", "");
const attendeesRaw = await tp.system.prompt("Attendees (comma-separated note names)", "");
const locationTrim = (location || "").trim().replace(/"/g, '\\"');
const locationLine = locationTrim ? `location: "${locationTrim}"` : `location: ""`;
const attendeeLines = (attendeesRaw || "")
  .split(",")
  .map((name) => name.trim())
  .filter(Boolean)
  .map((name) => `  - "[[${name}]]"`);
const attendeesBlock = attendeeLines.length
  ? `attendees:\n${attendeeLines.join("\n")}`
  : `attendees: []`;
-%>
---
type: meeting
project: "[[Thesis]]"
meeting-type: <% meetingType %>
track: <% track %>
scheduled: <% tp.date.now("YYYY-MM-DD") %>
<% locationLine %>
tags:
  - thesis
  - meeting
<% attendeesBlock %>
created: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

**Date:** <% tp.date.now("dddd, MMMM D, YYYY") %>
**Type:** <% meetingType %>
**Track:** <% track %>
**Location:** <% locationTrim %>

## Agenda

-

## Notes

## Decisions

-

## Action items

- [ ]

File each action item as its own note in `4-tasks/` with [[tpl-task]].
