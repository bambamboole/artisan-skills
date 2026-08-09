---
name: artisan-parallel
description:
  Use when an approved plan contains two or more bounded, independent, non-overlapping tasks that
  can be safely owned and verified concurrently.
---

# Coordinate Parallel Work

## Qualify

- Map dependencies, files, interfaces, and ownership first.
- Parallelize only work with no ordering, shared state, or overlapping files. Keep schema changes,
  shared interfaces, and integration with one owner.

## Delegate

Give each subagent a self-contained brief: goal, the files it may create or modify, constraints, the
interfaces it produces for other tasks, acceptance check, and report format. Do not leak session
history or prescribe a solution.

## Integrate

Collect diffs and check results as evidence, not completion claims. Treat uncommitted changes you
did not make as another agent's work; never clean or overwrite them. Integrate one task at a time,
resolve conflicts, run focused checks, then run an end-to-end check. Execute dependent work
sequentially.
