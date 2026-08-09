---
name: artisan-php
description: Use when building, reviewing, or debugging PHP applications, APIs, CLI commands, Composer packages, Laravel/Symfony code, tests, or database access.
---
# Build PHP Applications

Inspect `composer.json`, the framework version, quality tooling, and nearby code first. Follow the project’s conventions and PHP-version baseline; use strict types where they fit. Keep HTTP/controllers thin; validate input at boundaries; use explicit request/response and domain types; isolate persistence and external I/O. Avoid global state, dynamic properties, and unbounded arrays at public boundaries. For Laravel/Symfony, use framework validation, dependency injection, migrations, and test helpers instead of hand-rolled equivalents. Add a focused PHPUnit or Pest test, then run the narrowest relevant formatter, static analysis, and test command.
