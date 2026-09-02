---
name: frontend-design
description:
  Use when designing, building, refining, or auditing a production web interface, page, or component
  in HTML, CSS, JavaScript, React, or another frontend stack after its visual direction is
  established.
---

# Build Production Interfaces

## Establish Direction

- Ground the interface in its audience, subject, and job. Inspect the existing stack and design
  system; confirm a library exists in the manifest before importing it.
- Choose a specific hierarchy, palette, type roles, and one earned signature rather than generic
  card rows.

## Implement States

- Use semantic, reusable components, purposeful assets, and realistic copy: no placeholder names,
  round fake numbers, or clichés such as "Elevate" and "Seamless".
- Preserve behavior and design loading, empty, error, focus, hover, and pressed states: skeletons
  that match the final layout, empty states that point to the next action, inline errors rather than
  alerts.
- Keep body text near a 65-character measure, use tabular numerals for data, and keep touch targets
  at 44px or larger.
- Make responsive layouts collapse deliberately. Use `min-height: 100dvh` rather than `h-screen`,
  never blur or grain a scrolling container, and observe visibility with `IntersectionObserver`
  rather than scroll listeners. Respect reduced motion; animate only meaningful feedback with
  transform or opacity.

## Verify

Check the rendered result at desktop and mobile sizes with no horizontal overflow, then run the
narrowest relevant test or build.
