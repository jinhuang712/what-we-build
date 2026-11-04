# Architecture

what-we-build is a skill: Markdown instructions that a coding agent reads. The agent reads them when the user types `/what-we-build`. Then it writes and keeps a project's docs with the user.

```text
  the user types /what-we-build
              │
              ▼
  ┌─────────────────────────┐
  │ your agent              │ ◀── the skill folder linked
  │ loads the skill         │     into its skills folder
  └────────────┬────────────┘
               │ reads
               ▼
  ┌─────────────────────────┐
  │ The core                │
  │ what the agent always   │
  │ needs                   │
  └────────────┬────────────┘
               │ read in full with it
               ▼
  ┌─────────────────────────┐
  │ The guides              │
  │ one guide per doc       │
  └────────────┬────────────┘
               │ the agent writes with the user
               ▼
  ┌─────────────────────────┐
  │ the project's docs      │
  │ and its AGENTS.md       │
  └─────────────────────────┘
```

## The core

It holds what the agent always needs: how the talk runs, the doc set and the rules every doc follows.

- **Lives in:** [skills/what-we-build/](../skills/what-we-build/)

## The guides

There is one guide per kind of doc. The agent reads every guide when the skill starts and after each compaction.

- **Lives in:** [skills/what-we-build/references/](../skills/what-we-build/references/)
