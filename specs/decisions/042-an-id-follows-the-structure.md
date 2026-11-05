# 042. An ID follows the structure

Decided: 2026-11-05

## The problem

An ID was meant never to change, so an agent treated a wrong structure as cheaper to keep than to fix. In a run on a diagram tool it listed renumbering as a cost, chose plans for keeping their numbers and left gaps in the checkpoints. The user had to push for every rebuild.

## The choice

An ID follows the format in the skill's *IDs* table and changes when the structure changes. A rename fixes every link and mention in the same change.

## Not chosen

- Keep IDs fixed: the numbers then outrank the structure they label.
- Keep an ID while its structure holds: the agent would still have to judge whether it holds.
- Add a mapping table of old IDs: it serves the docs and not the reader, and git keeps the history.

## Consequences

The ban on reusing an old ID is gone. A link from outside the project can break after a rebuild, so a released project says so in its changelog.
