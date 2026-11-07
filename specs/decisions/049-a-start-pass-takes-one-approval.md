# 049. A start pass takes one approval

Decided: 2026-11-07

## The problem

Start asks the agent to work alone, and *Writing a doc* asks it to show every change before a commit. A user may also keep a rule to ask before any edit. In a run on a diagram tool the pass stopped before its first edit and later broke into single turns.

## The choice

When the pass needs approval, the agent asks once for the whole pass. A topic the user opens pauses the pass, and the agent goes back to it after the talk.

## Not chosen

- An approval per doc: it pulls the user back in for work that adds nothing new.
- No approval at all: it breaks a rule the user set outside the skill.

## Consequences

The user sees the pass as a whole at its end, so a wrong edit can sit in many commits by then. The proof for each doc is how they find it.
