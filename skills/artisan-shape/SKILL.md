---
name: artisan-shape
description:
  Use when defining a non-trivial feature, behavior change, or refactor before implementation,
  especially when scope, interface, trade-offs, or acceptance criteria are unclear.
---

# Shape Work

## Discover

- Read repository instructions and the affected code before proposing work.
- Separate observed facts from assumptions. Ask only for a decision that materially changes scope or
  behavior.

## Define

- State the user goal, non-goals, constraints, affected behavior, and acceptance checks.
- For work touching external systems, queues, or scheduled jobs, classify each operation: read-only
  or state-changing, idempotent or not, synchronous user path or background. Retry and
  duplicate-delivery semantics are scope, not implementation detail.
- Offer alternatives only when their trade-off is real and consequential.

## Plan

Finish with the smallest decision-complete plan: touched surfaces, behavior and interface changes,
failure handling, and verification. Avoid ceremonies, documents, and abstractions that the work does
not need.
