# AGENTS.md

AGENTS.md is the instruction file for coding agents working in the repo. Many tools read it, and `CLAUDE.md` can link to it, so the rules live once. It covers what an agent cannot learn by looking: commands that must pass, rules to follow, and what never to touch.

**Owns:** commands to build, test and lint, the rules agents must follow, which doc to read first, and the guardrails.

**Add when** coding agents will work in the repo. Draft it near the end of a session, once the build commands and the rules are known.

## Guidelines

- **Give each rule its reason in a clause,** so an agent can apply it to cases the rule does not name.
- **Write the target behavior,** and keep a prohibition only for a hard guardrail. A ban puts the forbidden thing in the agent's mind.
- **Point to the placement test** for where new facts go.

| Weak | Strong |
|---|---|
| "Don't break the build." | "Run `make test` and `make lint` before you call work done. Report failures with their output." |

## Explore

Which commands must pass before work is done? What must an agent never touch? Where do new facts go?
