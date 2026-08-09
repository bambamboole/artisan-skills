---
name: artisan-review
description: Use when reviewing a code diff, pull request, staged changes, or the value and ownership of tests.
---

# Review Signal

Review without editing unless asked. Read the changed flow and relevant project rules. Report only concrete, actionable
findings: missed reuse, needless complexity or work, wrong abstraction boundary, broken behavior, or a test that does
not prove an observable change. Prefer the smallest correction and name its location. Do not request generic extra
tests, documentation, style preferences, or speculative cleanup. If there are no findings, say so and name the
dimensions checked. Keep test ownership at the layer where behavior is observable.
