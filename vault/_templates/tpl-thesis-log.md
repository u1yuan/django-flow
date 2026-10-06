<%*
const term = await tp.system.suggester(
  ["Pre-thesis", "Term 1 (Aug–Dec 2026)", "Term 2 (Jan–Mar 2027)", "Term 3 (Apr–Jun 2027)"],
  ["pre-thesis", "term-1", "term-2", "term-3"],
  false,
  "Term"
);
const track = await tp.system.suggester(
  ["Hydroponics", "Diesel", "Shared"],
  ["hydroponics", "diesel", "shared"],
  false,
  "Track"
);
-%>
---
type: log
project: "[[Thesis]]"
term: <% term %>
track: <% track %>
week-of: <% tp.date.now("YYYY-MM-DD") %>
status: active
tags:
  - thesis
  - log
created: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

**Week of:** <% tp.date.now("MMMM D, YYYY") %>
**Term:** <% term %>
**Track:** <% track %>

## Accomplished

-

## In progress

-

## Blockers

-

## Next week

Each next action is a task note in `4-tasks/` with `due` on or before <% tp.date.now("YYYY-MM-DD", 7) %>.

![[Tasks.base#Open]]

## Notes

Decisions and open questions from this week. A diesel note must not claim that an anomaly caused a fault.
