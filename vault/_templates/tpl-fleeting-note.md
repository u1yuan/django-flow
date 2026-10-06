<%*
const track = await tp.system.suggester(
  ["Hydroponics", "Diesel", "Shared"],
  ["hydroponics", "diesel", "shared"],
  false,
  "Track"
);
const related = await tp.system.prompt("Related note name (blank for none)", "");
const relatedTrim = (related || "").trim();
const relatedLine = relatedTrim ? `related: "[[${relatedTrim}]]"` : `related: ""`;
-%>
---
type: note
project: "[[Thesis]]"
track: <% track %>
<% relatedLine %>
tags:
  - thesis
  - note
created: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>
