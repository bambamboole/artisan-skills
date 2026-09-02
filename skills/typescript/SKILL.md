---
name: typescript
description:
  Use when building, reviewing, debugging, or migrating TypeScript or JavaScript types, modules,
  package APIs, builds, or type tests.
---

# Write TypeScript Contracts

## Inspect the Boundary

- Read `tsconfig`, package exports, Vite build configuration, and nearby code before changing types.
- Preserve strict compiler, module-resolution, and public-package conventions; keep flags such as
  `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, and `verbatimModuleSyntax` when
  configured.

## Model Precisely

- Express runtime distinctions with object types, discriminated unions, and type guards.
- Use `unknown` at untrusted boundaries. Minimize assertions and `any`.
- Use type-only imports and preserve public exports, declaration output, and package boundaries. Do
  not change paths, configuration, or dependencies without cause.
- Avoid type gymnastics and circular dependencies. When instantiation gets excessively deep, prefer
  interfaces over large intersections and split oversized unions.
- Where a server owns the wire contract, generate and commit client types from it so drift fails the
  type check.

## Verify

Add behavior tests and type tests (`expectTypeOf` in `*.test-d.ts`) only for meaningful public or
generic contracts. Run `tsc --noEmit`, configured type coverage or lint, focused Vitest, and the
affected library build as one-shot commands, never watch processes. For published packages, run
`publint --strict` and `@arethetypeswrong/cli`; they catch export-map regressions type checks miss.
