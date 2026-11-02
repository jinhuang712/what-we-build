# 023. The skill points to a wiki and leaves its form to the project

Decided: 2026-11-03

## The problem

Some projects are built on by many other developers, who often work with their own agents. Without a wiki those developers and their agents can only read the source to learn how to use the project, and they guess at its interfaces. FEATURES ruled out user manuals because they say how to use the product and not why it is this way, so the skill never raised the need at all.

## The choice

A wiki is not part of the doc set. Once other developers build on the project, the agent tells the user that it may need a wiki. The rule sits in *While you work*, so it reaches every window through AGENTS.md at the point in the project's life when the need appears. What the wiki holds and where it lives is left to the project, and the skill gives it no guide.

## Not chosen

- A wiki as an optional doc with its own guide: what a wiki needs differs from project to project, and a guide would shape what only the project can judge.
- Saying nothing about a wiki: the developers who build on the project would be left with the source.

## Consequences

FEATURES gains F2.2: A wiki when others build on it, and its *Not planned* list says the skill does not write or shape a wiki. The rules of the doc set do not apply to a wiki.
