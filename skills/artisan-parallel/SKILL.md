---
name: artisan-parallel
description: Use when executing a plan with two or more independent, non-overlapping tasks that can benefit from concurrent agents.
---

# Split Independent Work

Map dependencies and ownership first. Parallelize only bounded tasks with no ordering, shared state, or overlapping
files. Keep schema changes, shared interfaces, and integration with one owner. Give each subagent a self-contained
brief: goal, paths, constraints, acceptance check, and report format. Do not leak session history or prescribe a
solution. Collect diffs and check results as evidence; do not trust completion claims. Integrate one task at a time,
review conflicts, and run its focused check. Run an end-to-end check after all integrations. Execute dependent work
sequentially.
