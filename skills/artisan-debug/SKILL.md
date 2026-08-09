---
name: artisan-debug
description:
  Use when investigating a bug, regression, failing test, production error, or unexpected behavior
  and the underlying cause is not yet established.
---

# Debug Root Causes

## Establish Evidence

- Reproduce the failure or collect the most direct evidence before editing.
- Prefer reading real state — logs, database queries, the app's own CLI — over writing bespoke debug
  scripts.
- Trace inputs, state, boundaries, and callers through the shared path.

## Locate the Cause

- Distinguish the visible symptom from the first incorrect assumption or boundary.
- Check the installed version of a suspect dependency before trusting API assumptions; many
  mysterious failures are version-assumption bugs.
- Fix the shared root cause where affected callers benefit; do not patch each symptom.

## Verify

Preserve valid behavior, avoid unrelated cleanup, and add or update a focused regression check that
fails before the fix and passes after it. Verify the reported path and state remaining uncertainty
plainly.
