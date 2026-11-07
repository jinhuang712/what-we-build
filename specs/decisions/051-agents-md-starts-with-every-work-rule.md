# 051. AGENTS.md starts with every work rule

Decided: 2026-11-08

## The problem

A window that never loaded the skill has only `AGENTS.md`. The skill told the agent to suggest rules and agree them with the user one at a time, so most projects got a soft and partial set. Windows then skipped the cleanup, and the rule against adding all the rules at once worked against the rule that a rule holds until the user rejects it.

## The choice

The start pass writes every rule of *While you work* in `AGENTS.md`, and the user rejects the ones they do not want. Two rules give cleanup a moment: a change that lands and a checkpoint that ends.

## Not chosen

- One rule at a time: the set stays partial, and each rule costs the user a talk.
- A hook at the end of each turn: it reaches only some agents, and it fires too often.

## Consequences

`AGENTS.md` is longer, and every window reads it. The cleanup still rests on the agent reading the rule, since nothing forces it.
