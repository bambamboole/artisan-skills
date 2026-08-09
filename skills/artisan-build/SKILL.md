---
name: artisan-build
description:
  Use when implementing a scoped feature, bug fix, refactor, template, or user-visible UI behavior
  after the intended outcome is known.
---

# Implement Changes

## Orient

- Trace the affected flow and reuse nearby patterns before adding code.
- Follow repository instructions and choose the smallest safe diff.
- Confirm a dependency exists in the manifest (`package.json`, `composer.json`) before importing it;
  never assume a library is available.

## Change

- Prefer platform and standard-library features over new dependencies or speculative abstractions.
- For domain or backend behavior, write a focused failing test, then implement only enough to pass.
- For templates and client-only behavior, implement first and verify the observable result; use a
  browser test when the behavior exists only in the browser.

## Prove

Run the narrowest relevant check and report what it demonstrates. Prefer a focused test over a
throwaway verification script.
