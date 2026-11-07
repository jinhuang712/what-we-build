# 053. A project with a command line must have CLI.md

Decided: 2026-11-08

## The problem

The guide for `CLI.md` was removed in 0.4.0 because a command reference copies the program. That left the flags and exit codes of a project with no home, and `--help` shows neither a planned command nor what a script may rely on.

## The choice

`CLI.md` comes back as the contract of the command line, and the program follows it. It holds every command and flag with its status, its output and its exit codes. A project with a command line that a person or another program calls must have it, and the user can drop it only as they drop a core doc.

## Not chosen

- Keep the flags in FEATURES: a contract for scripts would crowd the user's view of what the project does.
- Keep only what `--help` cannot say: a small tool would get a nearly empty doc, and a new window would still have to run the program to see its commands.
- Restore the old guide: it drew no line against FEATURES and read as a copy of the program.
- An optional doc: a rule that leaves room is read as a choice.

## Consequences

The commands live in the program and in the doc, so the two can drift, and every change to a command must change `CLI.md` too. Every window that starts the skill reads one more guide, and `SKILL.md` moves closer to its size limit.
