# 018. Every doc fits in one read

Decided: 2026-11-02

## The problem

M3: Length of the core docs counted the lines of the 7 core docs and stood at 885 against 614 at v0.4.0. The count rose whenever a doc gained structure, such as a section per goal, and it said nothing about whether a doc had grown too long. What matters is that the agent re-reads the whole doc before any edit, so one read must return all of it.

## The choice

T8: A doc read in one go replaces M3: Length of the core docs. Every doc stays within one Claude Code read.

## Not chosen

- Keeping the line count: a number with no limit and no link to any harm.
- A limit set by taste such as 300 lines per doc: it would fail a doc that reads fine and pass one that does not.

## Consequences

The limit follows the tool, so it moves when Claude Code changes its read limits.
