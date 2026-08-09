---
name: artisan-review
description:
  Use when reviewing a code diff, pull request, staged change, or test suite for concrete
  correctness, maintainability, and verification risks without editing unless asked.
---

# Review for Actionable Risk

## Read the Change

- Read project rules, the changed flow, and relevant callers before judging the diff.
- Check behavior, reuse, abstraction boundaries, failure handling, and observable test coverage.
- Check the diff against its stated intent separately: missing requirements and unrequested scope
  are findings, and neither axis may mask the other.

## Report Signal

- Report only concrete, actionable findings. Name the location, impact, and smallest correction.
- Flag missed reuse, needless complexity, broken behavior, wrong ownership, or a test that does not
  prove a meaningful change: render-only tests, styling-class pins, absence-only assertions, and
  mock tautologies earn deletion, not praise.
- Confirm new imports and dependencies exist in the manifest.
- When a hunk you are already reading raises a concrete correctness doubt, trace it to ground and
  report a verified defect or an explicit question; do not defer it.
- Do not request generic tests, documentation, style preferences, or speculative cleanup, and do not
  flag what a linter or type checker already catches or pre-existing issues on untouched lines.

If there are no findings, say so and name the dimensions checked. Keep test ownership at the layer
where behavior is observable.
