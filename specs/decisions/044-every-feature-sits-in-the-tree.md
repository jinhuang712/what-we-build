# 044. Every feature sits in the tree

Decided: 2026-11-05

## The problem

FEATURES kept the ideas not yet planned in a *Later* list outside its tree. In a run on a diagram tool the user wanted to see the whole product in one tree, and the list hid what might come.

## The choice

*Later* is gone. A feature not yet built sits in the tree as ⬜ and in a checkpoint. A last checkpoint holds the features that wait for a need.

## Not chosen

- Keep *Later* for maybes: the whole product is then split across two lists.
- Keep both, with *Later* for ideas nobody will commit to: an agent would have to judge which list each idea joins.

## Consequences

A ⬜ no longer promises that a feature will be built soon, so the last checkpoint must say that its features wait for a need. The tree grows longer.
