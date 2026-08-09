---
name: artisan-react
description:
  Use when building, reviewing, or debugging React components, hooks, state, effects, data fetching,
  rendering performance, or React tests in an existing frontend application.
---

# Build React Interfaces

## Follow Local Architecture

- Inspect local Vite conventions, then preserve the chosen router, state, and data patterns. In a
  Lattice-based repository, read its `.ai/guidelines/` before adding code or tests.
- Derive render values, localize state, and reserve effects for external synchronization with
  cleanup.
- Render conditionals with ternaries or booleans; `{count && <Badge />}` renders a literal `0`.
- Import icons and utilities from specific module paths; barrel imports of large libraries slow
  startup and bloat bundles.
- Avoid fetch waterfalls and unnecessary client code. Skip memoization without measured cost, and
  all manual memoization when React Compiler is enabled.

## Test Observable Behavior

- Test transitions rather than class strings, render presence, or component internals.
- Use Vitest jsdom for logic, wiring, and state.
- Use the root Vite Vitest config and `.browser.test.tsx` with `vitest-browser-react` for input,
  layout, portals, focus, scrolling, drag/resize, or files. If a test wants to stub
  `getBoundingClientRect`, `ResizeObserver`, or `matchMedia`, write a browser test instead; drive
  input through locators and user events, never `dispatchEvent`.

Run focused tests, browser tests when relevant, and the affected build or check.
