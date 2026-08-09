---
name: artisan-visual-brainstorming
description:
  Use when exploring and selecting a visual direction for an interface, product, site, dashboard, or
  flow before production implementation, especially when the user needs concrete HTML mockups to
  compare.
---

# Explore Interface Directions

## Frame the Decision

- Ask 2–4 outcome-changing questions about audience and job, brand or content constraints, viewport,
  and non-negotiables.
- State sensible defaults when answers are unavailable.

## Produce Alternatives

- Create 2–3 self-contained Tailwind CDN HTML directions with responsive states and distinct
  hierarchy, palette, and composition. Pick fonts first, then colors that suit them; give each
  direction one signature move.
- Avoid the habitual text-left/image-right hero. Vary section scale within a direction while holding
  palette, type, and radius language constant.
- Copy `assets/visual-direction-switcher.html` before each body, copy its JavaScript beside every
  page, and configure the JSON list.

## Inspect and Choose

Start `bin/visual-serve -port 0 FOLDER`, inspect each direction at 375px and 1440px — horizontal
overflow on mobile is a failure — and present URLs with concrete trade-offs. Iterate only on the
selected direction.
