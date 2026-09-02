---
name: review
description:
  Use when reviewing a code diff, pull request, staged change, or test suite for concrete
  correctness, maintainability, and verification risks without editing unless asked.
---

# Review for Actionable Risk

## Establish the Review

- Resolve the review boundary to commits before reading: honor named refs; otherwise compare `HEAD`
  with the accessible remote default branch's merge base and state that assumption.
- Find the source of intent in the request, issue, or specification. If none exists, state that
  limit. Read project rules, the changed flow, and relevant callers.

## Check the Change

- Compare implementation and intent separately; report missing requirements and unrequested scope.
- Check behavior, reuse, ownership, failure handling, and observable test coverage.
- Treat delegated findings as leads. Verify each against the full diff, code, and intent, and
  independently account for every changed file.

## Report Signal

- Report only verified, actionable findings with location, impact, and smallest correction.
- Flag broken behavior, needless complexity, or tests that prove no meaningful change: render-only
  tests, styling-class pins, absence-only assertions, and mock tautologies earn deletion, not
  praise.
- Confirm new imports and dependencies exist in the manifest.
- Trace concrete doubts to a verified defect or explicit question. Skip generic requests, style
  preferences, speculative cleanup, automated-tool findings, and pre-existing issues.

If there are no findings, say so and name the dimensions checked. Keep test ownership at the layer
where behavior is observable.
