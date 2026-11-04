# 037. The skill is written for any agent

Decided: 2026-11-04

## The problem

The README called what-we-build a Claude Code skill, and INSTALL and ARCHITECTURE named only Claude Code. The skill is plain Markdown in the Agent Skills format, so any agent that loads skills can use it. Only the install steps were written for Claude Code alone.

## The choice

The skill is written for any agent that loads Agent Skills. The docs name Claude Code only where a step was tried there, such as the install steps and the read limit of T8: A doc read in one go. A rule that depends on one agent's file, such as `CLAUDE.md`, names it as an example.

## Not chosen

- A skill for Claude Code alone: nothing in it needs Claude Code, so the name would turn away users of other agents.
- Install steps for every agent at once: nobody has tried them, and INSTALL holds only steps that work as written.

## Consequences

README, INSTALL and ARCHITECTURE speak of your agent. INSTALL keeps the Claude Code steps, and a TODO item asks for the others.
