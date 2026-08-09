# Artisan Skills

A small, opinionated skill framework shared by Codex and Claude. It replaces overlapping workflow, frontend, Kotlin, React, and TypeScript prompts with concise, trigger-based skills.

## Install

Requires Python 3. From a local clone:

```sh
bin/install
bin/check
```

`bin/install` is idempotent. It links the plugin and skills into the shared agent and Claude directories, registers the Codex personal marketplace entry, and refuses to overwrite conflicting paths.

For Claude, register this checkout as a marketplace once, then install the plugin:

```sh
claude plugin marketplace add . --scope user
claude plugin install artisan-skills@artisan-skills --scope user
```

Codex discovers the plugin through the personal marketplace created by `bin/install`.

## Skills

| Skill | Use for |
| --- | --- |
| `artisan-shape` | Non-trivial scope, design, and plans |
| `artisan-build` | Focused production implementation |
| `artisan-debug` | Bugs, regressions, and failing tests |
| `artisan-review` | Diffs, pull requests, and test value |
| `artisan-parallel` | Independent, non-overlapping agent work |
| `artisan-frontend-design` | Production interface design and refinement |
| `artisan-web-art-direction` | Image-based website and product references |
| `artisan-kotlin-backend` | Kotlin/JVM, Ktor, JPA, and Java migration |
| `artisan-react` | React components, state, effects, and tests |
| `artisan-typescript` | TypeScript contracts, modules, builds, and type tests |

The Claude SessionStart hook is only a compact router; detailed instructions load only when a skill matches. It does not impose process on simple questions.

## Verify

```sh
python3 -m unittest tests/test_hook.py tests/test_install.py
bin/check
claude plugin validate --strict .
```

Each skill body is limited to 100 words. Keep new guidance specific, reusable, and evidence-backed; put project-specific conventions in that project rather than here.
