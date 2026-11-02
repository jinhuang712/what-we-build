<!-- what-we-build: approved 2026-11-02 -->

# Architecture

what-we-build is a skill: Markdown instructions that a coding agent reads. The agent reads them when the user types `/what-we-build`. Then it writes and keeps a project's docs with the user.

```text
  the user types /what-we-build
              │
              ▼
  ┌─────────────────────────┐
  │ Claude Code             │ ◀── installed from .claude-plugin/
  │ loads the skill         │     or a linked folder
  └────────────┬────────────┘
               │ reads
               ▼
  ┌─────────────────────────┐
  │ SKILL.md                │
  │ the protocol and rules  │
  └────────────┬────────────┘
               │ a step points to
               ▼
  ┌─────────────────────────┐
  │ references/             │
  │ one guide per doc       │
  └────────────┬────────────┘
               │ the agent writes with the user
               ▼
  ┌─────────────────────────┐
  │ the project's docs      │
  │ and its AGENTS.md       │
  └─────────────────────────┘
```

## The plugin manifest

It tells Claude Code how to install the skill as a plugin.

- **Lives in:** `.claude-plugin/`
- **Why:** [003](decisions/003-plugin-manifest-at-the-repo-root.md)

## SKILL.md

It holds what every session needs: the protocol, the doc set and the rules.

- **Lives in:** `skills/what-we-build/`
- **Why:** [001](decisions/001-one-skill-for-every-start.md) and [005](decisions/005-one-guide-per-kind-of-doc.md)

## The guides

There is one guide per kind of doc. The agent reads a guide before it starts that doc.

- **Lives in:** `skills/what-we-build/references/`

## The project's docs

They are what the skill produces. This repo's own docs are the first example.

- **Lives in:** the project's folder
