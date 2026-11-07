# 052. A contradiction goes to the user

Decided: 2026-11-08

## The problem

A contradiction sits between a changed line and lines nobody touched, and the rules asked the agent to check only what it touched. In one review of the skill, each contradiction came up by chance or after the user pushed.

## The choice

A change to a fact or a rule starts a search of the docs for what it now contradicts. The agent also says when the user's words contradict a doc. It tells the user at once and picks no side.

## Not chosen

- Let the agent settle it: the side it picks may be the stale one, and the choice stays hidden.
- A script that compares the docs: a reader has to judge meaning, and a script only matches words.

## Consequences

The user is asked more often. A search by keyword misses a contradiction written in other words.
