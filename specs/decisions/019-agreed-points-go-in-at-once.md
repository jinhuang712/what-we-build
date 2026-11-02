# 019. Agreed points go into the doc at once

Decided: 2026-11-03

## The problem

SKILL.md said to write a doc only after its key points were agreed. Points agreed for a doc not yet drafted lived only in the window, and DESIGNS 2 named their loss as its cost. That broke the want in the proposal that what is decided goes into a doc at once, and it lost exactly the context the skill exists to keep.

## The choice

Each point goes into its doc as soon as it is agreed, and nothing goes in before that. The doc stays an uncommitted draft until the user approves it, so git still tells a draft from an approved doc.

## Not chosen

- Parking agreed points in TODO.md until the doc is drafted: TODO holds what is open, and an agreed point is no longer open.
- Accepting the loss: it gives up the promise that context outlives the window.

## Consequences

A draft may stand half written until its last point is agreed. A resume finds the agreed points in the uncommitted draft.
