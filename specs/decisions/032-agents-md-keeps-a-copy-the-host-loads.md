# 032. AGENTS.md keeps a copy of the rules that the host loads

Decided: 2026-11-03

Partly replaced by 037: The skill is written for any agent, under which `CLAUDE.md` is one example of a file the agent makes load `AGENTS.md`.

## The problem

The skill copies the rules of *While you work* into the project's `AGENTS.md`, so they reach a window that never loaded the skill. A run on a Go library broke both halves of that. The project had no `CLAUDE.md`, and a `CLAUDE.md` in a folder above it made Claude Code skip `AGENTS.md`, so the rules never reached the window. The copy was also older than the skill, and it said some rules in the project's own words.

## The choice

The copy stays, because it is what survives a compaction after the skill's own text has left the window. The skill makes every window load `AGENTS.md`, and adds a `CLAUDE.md` with the line `@AGENTS.md` when the project has none. The agent decides with the user what goes in `AGENTS.md`, rule by rule and never all at once.

## Not chosen

- A link to the skill in place of the copy: a window without the skill cannot follow it, and a compaction drops what the link pointed to.
- A version stamp on the copy: it is a mark to keep and says nothing about which rule changed.
- A check on each start that compares the copy with *While you work*: a project words the rules its own way, so the check turned into a procedure the agent skipped.
- A symlink from `CLAUDE.md` to `AGENTS.md` as the one way: it fails on some systems, and the import line is what Claude Code's docs recommend.

## Consequences

The copy can fall behind the skill, and the agent finds that out by reading `AGENTS.md` in the talk. On 2026-11-05 a test with one Claude Code process found a file imported with `@AGENTS.md` still in context after a compaction.
