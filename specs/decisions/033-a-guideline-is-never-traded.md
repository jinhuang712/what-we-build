# 033. A guideline is never traded

Decided: 2026-11-03

## The problem

The DESIGNS guide of 0.4.0 ended the page with the order that decides when two guidelines collide. Later versions dropped it with no decision, so a project written under 0.4.0 kept the section. In a run on a Go library the agent reviewed DESIGNS against the new guide, kept the order and offered to extend it to all ten guidelines. Only the user remembered that the skill no longer asks for it.

## The choice

DESIGNS holds no order for when guidelines collide. A guideline is a commitment that is not up for negotiation, and an order says which one gives way, so it would make every guideline negotiable. When two seem to collide, one of them is not yet a guideline, and the user decides which. On each start the skill also shows the user any part of a doc that its guide no longer asks for, so a dropped part does not live on in old docs.

## Not chosen

- Keep the order: it turns hard commitments into weights, and a reader can no longer name the one guideline a design breaks.
- Drop the section from the guide in silence, as before: old docs keep it and the next agent defends it.

## Consequences

A project that held such an order rewrites the guidelines in it until none has to give way.
