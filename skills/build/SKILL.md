---
name: build
description:
  Use when implementing a scoped feature, bug fix, refactor, template, or user-visible UI behavior
  after the intended outcome is known.
---

# Implement Changes

## Execute an Approved Plan

- When implementation follows an approved plan, present a concise task list before editing. Show
  dependencies and status, and keep the list current as work completes or scope changes.
- Keep small or sequential work with the primary agent. For a larger plan, fan out only bounded,
  independent, non-overlapping tasks to subagents, in proportion to useful parallelism.
- Give each subagent explicit ownership, constraints, and an acceptance check. Keep shared
  interfaces, ordered work, conflict resolution, and final integration with the primary agent;
  verify returned diffs and evidence before marking a task complete.

## Orient

- Trace the affected flow and reuse nearby patterns before adding code.
- Follow repository instructions and choose the smallest safe diff.
- Confirm a dependency exists in the manifest (`package.json`, `composer.json`) before importing it;
  never assume a library is available.

## Change

- Prefer platform and standard-library features over new dependencies or speculative abstractions.
- For domain or backend behavior, write a focused failing test at the nearest public boundary so it
  survives refactors, then implement only enough to pass.
- For templates and client-only behavior, implement first and verify the observable result; use a
  browser test when the behavior exists only in the browser.

## Prove

Run the narrowest relevant check and report what it demonstrates. Prefer a focused test over a
throwaway verification script.
