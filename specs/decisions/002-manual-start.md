# 002. The skill starts only by hand

Decided: 2026-10-12

## The problem

An agent can load a skill on its own when a prompt seems to match.

## The choice

The skill sets `disable-model-invocation: true`. A session starts only when the user types `/what-we-build`.

## Not chosen

- Automatic loading: a session needs the user's full attention, and a skill that loads itself starts one when the user is busy with something else.

## Consequences

A user who never types the command never sees the skill.
