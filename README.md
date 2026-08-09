# Artisan Skills

A small, opinionated skill framework shared by Codex and Claude. It replaces overlapping workflow,
frontend, visual exploration, PHP, React, TypeScript, and writing prompts with concise,
trigger-based skills.

## Install

Requires Python 3. Formatting Markdown also requires Node.js 20+.

```sh
bin/install
bin/check
```

`bin/install` is idempotent. It links the plugin and skills into the shared agent and Claude
directories, registers the Codex personal marketplace entry, and refuses to overwrite conflicting
paths.

For Claude, register this checkout as a marketplace once, then install the plugin:

```sh
claude plugin marketplace add . --scope user
claude plugin install artisan@artisan --scope user
```

Codex discovers the plugin through the personal marketplace created by `bin/install`. Installed
skills are namespaced as `artisan:<skill>`, such as `artisan:writing`.

## Skills

| Skill                          | Use for                                               |
| ------------------------------ | ----------------------------------------------------- |
| `artisan-shape`                | Non-trivial scope, design, and plans                  |
| `artisan-build`                | Focused production implementation                     |
| `artisan-debug`                | Bugs, regressions, and failing tests                  |
| `artisan-review`               | Diffs, pull requests, and test value                  |
| `artisan-parallel`             | Independent, non-overlapping agent work               |
| `artisan-frontend-design`      | Production interface design, refinement, and audits   |
| `artisan-visual-brainstorming` | 2–3 locally reviewed Tailwind HTML directions         |
| `artisan-php`                  | PHP apps, plain Composer packages, Laravel/Symfony    |
| `artisan-react`                | React components, state, effects, and tests           |
| `artisan-typescript`           | TypeScript contracts, modules, builds, and type tests |
| `writing`                      | Clear, evidence-backed English technical prose        |

The Claude SessionStart hook is only a compact router; detailed instructions load only when a skill
matches. It does not impose process on simple questions.

## Format Markdown

    bin/format
    bin/format --check
    bin/format README.md skills/writing/SKILL.md

The command uses pinned OxFmt and only formats Markdown by default. Pass one or more Markdown paths
or quoted globs to narrow the scope.

## Verify

```sh
python3 -m unittest tests/test_hook.py tests/test_install.py tests/test_format.py
bin/check
claude plugin validate --strict .
```

Skill bodies should be concise. Keep them guidance specific, reusable, and evidence-backed; use
headings and lists to expose real decisions, and put project-specific conventions in that project
rather than here.
