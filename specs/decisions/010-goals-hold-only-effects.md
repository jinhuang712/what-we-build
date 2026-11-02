# 010. Goals hold only effects

Decided: 2026-11-02

## The problem

GOALS mixed the effects the skill must have with rules the work must keep, such as one home per fact or no code chunks. A rule written as a goal with a limit of 0 gave the rule a second home. Rules marked `every change` also made every small edit run the goal sheet.

## The choice

GOALS holds only effects, each tied to a want or a risk in the proposal. A rule lives in its own home: SKILL.md, DESIGNS or AGENTS.md. After a change the agent checks only the rules that change touched. The goals are checked at a moment that calls for it, such as the end of a checkpoint or a release. A small change never runs them. The rules that only a real session shows become the scoring criteria of B1: Session quality.

## Not chosen

- Rules kept as threshold and constraint goals: each rule would keep two homes that drift apart.
- Every cheap goal checked with every change: a one-word fix would run the sheet for nothing.

## Consequences

The goals that were rules are gone, and their IDs are not reused. A missing want shows as a want with no goal, which is how M4: Docs that fell behind was found.
