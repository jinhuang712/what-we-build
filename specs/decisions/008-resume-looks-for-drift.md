<!-- what-we-build: approved 2026-11-02 -->

# 008. A resume with nothing to draft looks for drift

Decided: 2026-11-02

## The problem

The skill manages a project over its whole life, so every doc being approved is the usual state and not the end. A resume that only looks for the first doc not approved then has nothing to do.

## The choice

The agent reports where the project stands from TODO, ROADMAP and GOALS. Then it looks at what changed since the date in each doc's mark. It points out where a doc may have fallen behind. It asks the user what to work on next.

## Not chosen

- Only the status: the status docs do not record drift, so the case most worth raising is missed.
- Looking for drift only when the user asks: drift is dangerous because nobody notices it.

## Consequences

A resume reads the history since each approval date, which costs more on a busy project.
