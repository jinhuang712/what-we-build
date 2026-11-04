# Architecture

what-we-build is a skill: Markdown instructions that a coding agent reads. The agent reads them when the user types `/what-we-build`. Then it writes and keeps a project's docs with the user.

```text
  the user types /what-we-build
              │
              ▼
  ┌─────────────────────────┐
  │ Claude Code             │ ◀── the skill folder linked
  │ loads the skill         │     into ~/.claude/skills
  └────────────┬────────────┘
               │ reads
               ▼
  ┌─────────────────────────┐
  │ SKILL.md                │
  │ the protocol and rules  │
  └────────────┬────────────┘
               │ read in full with it
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

## SKILL.md

It holds what the agent always needs: the protocol, the doc set and the rules.

- **Lives in:** `skills/what-we-build/`

## The guides

There is one guide per kind of doc. The agent reads every guide when the skill starts and after each compaction.

- **Lives in:** `skills/what-we-build/references/`

## The project's docs

They are what the skill produces. This repo's own docs are the first example.

- **Lives in:** the project's folder
