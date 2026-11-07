# 054. A checkpoint ends on recorded results

Decided: 2026-11-08

## The problem

The ROADMAP guide did not say how a checkpoint is accepted, whether order means dependence, or which goal proves the docs a project gets. One run went through about ten checkpoint trees for lack of an answer.

## The choice

A checkpoint ends once each goal in its exit criteria has a recorded result that meets it. Checkpoints stay in order with no further rule on what depends on what. In this repo the goal for the core docs on a new project also proves the docs a project gets.

## Not chosen

- A later checkpoint must depend on the one before it: real work often runs side by side, and the rule adds nothing to the order.
- Acceptance by the user alone: it leaves nothing a later reader can check.
- A new goal for the doc set: the run on a new project already tests those docs.

## Consequences

A checkpoint with no goal has no way to end, so it is either a bag of tasks or it needs a goal.
