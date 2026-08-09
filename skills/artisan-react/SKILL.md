---
name: artisan-react
description: Use when building, reviewing, or debugging React components, hooks, state, effects, rendering performance, or React tests.
---
# Build React Interfaces

Inspect local Vite conventions first. Preserve the chosen router, state, and data patterns; derive render values, localize state, and reserve effects for external synchronization with cleanup. Avoid fetch waterfalls, unnecessary client code, and memoization without measured cost. Test observable transitions, not class strings, render presence, or component internals. Use Vitest jsdom for logic, wiring, and state. Use the root Vite Vitest config and `.browser.test.tsx` with `vitest-browser-react` for input, layout, portals, focus, scrolling, drag/resize, or files; do not fake these with layout stubs or synthetic events. Run focused tests, browser tests when relevant, and the affected build/check.
