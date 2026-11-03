# 032. AGENTS.md keeps a copy of the rules that the host loads

Decided: 2026-11-03

## The problem

The skill copies the rules of *While you work* into the project's `AGENTS.md`, so they reach a window that never loaded the skill. A run on a Go library broke both halves of that. The project had no `CLAUDE.md`, and a `CLAUDE.md` in a folder above it made Claude Code skip `AGENTS.md`, so the rules never reached the window. The copy was also older than the skill, so a window that read it would still have followed old rules.

## The choice

The copy stays, because it is what survives a compaction after the skill's own text has left the window. The skill makes sure the host loads `AGENTS.md` in every window, such as a `CLAUDE.md` with the line `@AGENTS.md`. On each start it compares the copy with *While you work* and shows the user what changed.

## Not chosen

- A link to the skill in place of the copy: a window without the skill cannot follow it, and a compaction drops what the link pointed to.
- A version stamp on the copy: comparing the text finds the same drift with no mark to keep.
- A symlink from `CLAUDE.md` to `AGENTS.md` as the one way: it fails on some systems, and the import line is what Claude Code's docs recommend.

## Consequences

The copy can still fall behind between two starts of the skill. Whether Claude Code reloads an imported file after a compaction is not yet tested.
