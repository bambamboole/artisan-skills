---
name: artisan-typescript
description: Use when building, reviewing, debugging, or migrating TypeScript and JavaScript, including types, modules, package APIs, builds, and type tests.
---
# Write TypeScript Contracts

Inspect tsconfig, package exports, Vite build, and nearby code before changing types. Preserve strict compiler and module-resolution conventions. Express runtime distinctions with precise object types, discriminated unions, and type guards; use `unknown` at untrusted boundaries and minimize assertions or `any`. Use type-only imports and preserve public exports, declaration output, and package boundaries; do not change paths, configuration, or dependencies without cause. Avoid type gymnastics and circular dependencies. Add behavior tests and type tests only for meaningful public or generic contracts. Run `tsc --noEmit`, type coverage/lint where configured, focused Vitest, and the affected library build.
