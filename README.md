# Artisan Skills

A small, opinionated skill framework shared by Codex and Claude. It replaces overlapping workflow,
frontend, visual exploration, PHP, React, TypeScript, writing, and Git/GitHub prompts with concise,
trigger-based skills.

## Install

The recommended path installs the complete plugin from GitHub without a checkout:

```sh
claude plugin marketplace add bambamboole/artisan-skills
claude plugin install artisan@artisan
```

For intentionally narrow setups, individual skills also install with the
[skills CLI](https://www.skills.sh): `npx skills add bambamboole/artisan-skills`.

## Develop

Requires Python 3. Formatting Markdown also requires Node.js 20+.

```sh
bin/install
bin/check
```

`bin/install` is idempotent. It links the plugin and skills into the shared agent and Claude
directories, registers the Codex personal marketplace entry, and refuses to overwrite conflicting
paths.

For Claude development against the checkout, register it as a local marketplace once, then install
the plugin:

```sh
claude plugin marketplace add . --scope user
claude plugin install artisan@artisan --scope user
```

Codex discovers the plugin through the personal marketplace created by `bin/install`. Installed
skills are namespaced as `artisan:<skill>`, such as `artisan:build` and `artisan:writing`.

## Skills

| Skill                  | Use for                                               |
| ---------------------- | ----------------------------------------------------- |
| `shape`                | Non-trivial scope, design, and plans                  |
| `build`                | Focused production implementation                     |
| `debug`                | Bugs, regressions, and failing tests                  |
| `review`               | Diffs, pull requests, and test value                  |
| `parallel`             | Independent, non-overlapping agent work               |
| `frontend-design`      | Production interface design, refinement, and audits   |
| `visual-brainstorming` | 2–3 locally reviewed Tailwind HTML directions         |
| `php`                  | PHP apps, plain Composer packages, Laravel/Symfony    |
| `react`                | React components, state, effects, and tests           |
| `typescript`           | TypeScript contracts, modules, builds, and type tests |
| `writing`              | Clear, evidence-backed English technical prose        |
| `git-and-github`       | Clean commits, feature branches, pushes, and PRs      |

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

## License

MIT. The `writing` skill adapts [agent-style](https://github.com/yzhao062/agent-style) (CC BY 4.0);
see `LICENSE.md`.
