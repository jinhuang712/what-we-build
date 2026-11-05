# 043. TODO waits for spare time

Decided: 2026-11-05

## The problem

The skill told the agent when to add an item and when to delete a finished one, and nothing sent it back to the list. Items only piled up. Tying the list to a start or to the end of a checkpoint would break into work still under way.

## The choice

The agent goes through `TODO.md` with the user once the work at hand is done and nothing is next. Both conditions must hold. A `P0` item stays outside this rule, since it is broken now and comes first.

## Not chosen

- Clean the list at each start: the agent stops a pass half done to talk about old items.
- Clean the list at the end of a checkpoint: other work may be open at that moment.
- A `next` field on every item: it fills a form and does not bring the agent back to the list.

## Consequences

An item can wait a long time on a busy project. The agent has one more thing to do at the end of the work, and the user decides how far it goes.
