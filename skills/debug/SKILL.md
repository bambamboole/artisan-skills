---
name: debug
description:
  Use when investigating a bug, regression, failing test, production error, performance regression,
  or behavior reported as broken, throwing, or slow when the underlying cause is not yet
  established.
---

# Debug Root Causes

## Establish Evidence

- Build a repeatable, fast command that shows the failure before editing; when that is impossible,
  collect the most direct evidence available.
- Prefer reading real state — logs, database queries, the app's own CLI — over writing bespoke debug
  scripts.
- Redact secrets, authentication headers, personal data, and sensitive payloads before displaying
  commands, logs, traces, or captured artifacts.
- Trace inputs, state, boundaries, and callers through the shared path.

## Locate the Cause

- Distinguish the visible symptom from the first incorrect assumption or boundary. State falsifiable
  hypotheses — if X is the cause, changing Y makes the failure disappear — and test the cheapest
  first.
- Check the installed version of a suspect dependency before trusting API assumptions; many
  mysterious failures are version-assumption bugs.
- Fix the shared root cause where affected callers benefit; do not patch each symptom.

## Verify

Preserve valid behavior, remove leftover debug instrumentation, avoid unrelated cleanup, and add or
update a focused regression check that fails before the fix and passes after it. Verify the reported
path and state remaining uncertainty plainly.
