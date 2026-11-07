# 050. ROADMAP keeps each checkpoint's goal results

Decided: 2026-11-08

## The problem

GOALS holds only the last result of each goal, and a newer result replaces it. A goal runs in many checkpoints and may get worse as the work goes on. Nobody could then tell a goal that fell back from a goal that was never met.

## The choice

ROADMAP records each goal's result and date in the exit criteria of the checkpoint that ran it. That record stays as it was. GOALS holds the result now, and ROADMAP holds the result then. A goal that fails later goes to `TODO.md` as an `ISSUE`.

## Not chosen

- A history inside each goal in GOALS: the goal is a rubric, and when it ran belongs to the schedule.
- Reopen a finished checkpoint when a goal fails: the checkpoint did meet the goal when it ended.
- Fill old records from the current result: a result nobody recorded would look measured.

## Consequences

A goal's number can sit in two docs with different values, and both are true. A checkpoint that ended before this rule shows no record.
