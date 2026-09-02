---
name: php
description:
  Use when building, reviewing, or debugging a PHP application, API, CLI command, Composer package,
  Laravel/Symfony feature, queue job, external service integration, test, or database interaction.
---

# Build PHP Applications

## Orient

- Read `composer.json` first: PHP version, framework or none, and `scripts`. Run checks through
  defined Composer scripts (`composer test`, `lint`, `analyse`) rather than raw `vendor/bin`
  commands.
- Read root tooling configs (`phpstan.neon*`, `pint.json`, `phpunit.xml`) before writing code and
  match their level and style. Use strict types where they fit.

## Implement

- Keep HTTP controllers thin. Validate boundaries, use explicit request/response and domain types,
  and isolate persistence and external I/O.
- Wrap multi-step writes in a transaction. Retry external calls only when idempotent, with
  exponential backoff and jitter; a timed-out state-changing request may already have side effects.
- Avoid global state, dynamic properties, and unbounded arrays at public boundaries.
- In Laravel or Symfony, prefer framework validation, dependency injection, migrations, and test
  helpers.
- In a plain Composer package, skip framework scaffolding: construct objects directly in tests, keep
  classes `final` with `declare(strict_types=1)`, and mirror `tests/` to `src/`. Libraries commit no
  `composer.lock` and test across their supported PHP range.

## Verify

Add a focused Pest test; retain PHPUnit only when the suite requires it. Prefer PHPStan to Psalm.
Use Rector for compatible automated refactors or upgrades, review its diff, then run the narrowest
relevant formatter, analysis, test, and build commands.
