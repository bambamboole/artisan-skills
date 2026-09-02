---
name: shape
description:
  Use when planning or defining a non-trivial feature, behavior change, or refactor before
  implementation, especially when scope, interface, trade-offs, or acceptance criteria are unclear.
---

# Shape Work

## Discover

- Read repository instructions and the affected code before proposing work.
- Separate observed facts from assumptions. Whenever purpose, scope, constraints, or success
  criteria are not fully clear, ask 2-3 focused clarifying questions before proposing a plan; never
  fill the gap with a guess.
- Do not write code, scaffold, or invoke an implementation skill until the plan is approved.

## Define

- State the user goal, non-goals, constraints, affected behavior, and acceptance checks.
- For work touching external systems, queues, or scheduled jobs, classify each operation: read-only
  or state-changing, idempotent or not, synchronous user path or background. Retry and
  duplicate-delivery semantics are scope, not implementation detail.
- Offer alternatives only when their trade-off is real and consequential.

## Plan

- Finish with the smallest decision-complete plan: touched surfaces, behavior and interface changes,
  failure handling, and verification. Avoid ceremonies and abstractions that the work does not need.
- Honor the user's preference or repository convention for plan storage. If neither exists, ask
  whether to publish the approved plan as a GitHub issue; recommend it for GitHub-hosted work so the
  plan outlives the local checkout.
- Issue creation changes external state. Confirm the target repository and get approval to publish,
  then create one issue, read it back to verify its title and body, and return its URL.
- If the user chooses a local plan, write it to `plans/YYYY-MM-DD-<topic>.md`. Ensure `plans/` is
  gitignored; never commit local plans.
