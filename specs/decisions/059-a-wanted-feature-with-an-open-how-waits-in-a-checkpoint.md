# 059. A wanted feature whose how is still open waits in a checkpoint instead of in TODO

Decided: 2026-11-11

## The problem

Every open point went to `TODO.md` as a `DISCUSSION`. On a diagram tool the user found that an item there gets discussed at once, which pulled the talk away from the work. The user asked to record such points as features on a checkpoint and leave how to build them open.

## The choice

- When the user wants something and its how is still open, it is a ⬜ feature in a checkpoint with the how left open.
- `TODO.md` keeps the questions that block a doc.

## Not chosen

- A `DISCUSSION` for every open point: each one invites a talk the work does not need yet.
- Leaving the want out until its how is clear: it would live only in the window.

## Consequences

FEATURES and ROADMAP hold planned features whose design is not decided. A checkpoint still decides that design before it starts to build.
