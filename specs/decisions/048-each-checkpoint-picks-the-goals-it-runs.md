# 048. Each checkpoint picks the goals it runs from GOALS

Decided: 2026-11-06

## The problem

The ROADMAP guide ruled out one goal in two checkpoints, and the GOALS guide said a goal runs at every checkpoint from its first one. So the goal decided when it ran. In a run on a diagram tool the first rule forced a choice of one checkpoint for each goal, though cost and speed matter at every checkpoint. The user rejected that rule, and no decision had recorded it.

## The choice

GOALS is the rubric for the project's whole life. Each checkpoint names the goals it runs, and one goal may run in many checkpoints. A parent still leaves its sub-checkpoints' goals to them, and a release runs every goal that can run.

## Not chosen

- A goal in one checkpoint only: it hides a regression once that checkpoint is done.
- Every goal at every checkpoint: a goal may not be able to run yet, and each run costs time.
- A goal that lists its checkpoints: it gives the schedule a second home.

## Consequences

A checkpoint must say which goals it runs, so a goal left out of a later checkpoint goes unchecked until the release.
