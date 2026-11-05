# 040. A rule holds unless the user rejects it

Decided: 2026-11-05

## The problem

A rule could be set aside once the user agreed. In a run on a diagram tool the agent asked for such exceptions itself, and a short "ok" from a tired user was enough. The skeleton and the exit criteria were bent that way at least three times, and no exception was written down.

## The choice

The agent follows the skill strictly until the user rejects a rule. It never asks for a way around a rule. When a rule seems not to fit, it says why and asks for the user's opinion. A rule the user rejects becomes an exception in `specs/decisions/`.

## Not chosen

- Keep "unless the user agrees": a question from the agent opens the door, and a tired yes walks through it.
- Reverse every approval: new features, goals and thresholds are not settled yet, and commits stay the user's call.
- Forbid exceptions: the user owns the project and may decide that a rule does not fit it.

## Consequences

The user answers fewer questions, and only an explicit rejection changes the agent's course. The agent still voices a doubt, so a bad rule can surface. New content and commits still need the user's approval.
