# 021. FEATURES links to all a feature rests on and all that builds it

Decided: 2026-11-03

## The problem

FEATURES lists every capability the project must have, so the design, the build and the progress meet there. A feature could link to a few DESIGNS points and down to its specs and decisions. The FEATURES skeleton had no place for how a feature looks, so a feature never reached its section in `specs/UIUX.md` or its page in `prototype/`. It could not reach a PHILOSOPHY stance either, even when that stance was the reason the feature exists.

## The choice

A feature links up to the DESIGNS guidelines it rests on, and to a PHILOSOPHY stance only when the stance forces the feature. It links down to everything that builds it: the flows of its stories in `specs/UIUX.md`, its specs and its decisions. What the feature rests on and what builds it set the number of links, and no count does. The checkpoint that delivers a feature stays in ROADMAP, which links to the feature.

## Not chosen

- Free links to PHILOSOPHY: every feature would gain a link to the thought as decoration.
- A link from each feature to its checkpoint: the checkpoint would have two homes, and each change to the plan would touch FEATURES.
- Only adding UIUX and the prototype: a feature would still lose the stance that forces it.

## Consequences

A reader can start at any feature and reach its reason and its build without a search.
