# 010. Goals hold only effects, and the placement test asks about rules first

Decided: 2026-11-02

## The problem

GOALS mixed the effects the skill must have with rules the work must keep, such as one home per fact or no code chunks. A rule written as a goal with a limit of 0 gave the rule a second home. Rules marked `every change` also made every small edit run the goal sheet. The placement test fed the mix: its second question asked whether a fact can be checked with a test or a number, and almost every rule can.

## The choice

GOALS holds only effects, each tied to a want or a risk in the proposal. A rule lives in its own home: SKILL.md, DESIGNS or AGENTS.md. Right after the stance question the placement test asks whether a fact is a commitment the whole design must meet, then whether it is a rule for how the work is done here, and only then whether it is an effect with a test or a number. After a change the agent checks only the rules that change touched. The goals are checked at a moment that calls for it, such as the end of a checkpoint or a release, and a small change never runs them. The rules that only a real run shows become the scoring criteria of B1: Run quality.

## Not chosen

- Rules kept as threshold and constraint goals: each rule would keep two homes that drift apart.
- Every cheap goal checked with every change: a one-word fix would run the sheet for nothing.
- Only rewording the GOALS question to ask for an effect: the line between an effect and a rule would rest on the agent's judgment alone.
- A push-back in the GOALS guide only: it catches a rule after it was placed, not before.

## Consequences

The goals that were rules are gone. A missing want shows as a want with no goal, which is how M4: Docs that fell behind was found. A fact that is a design commitment and can also be checked goes to DESIGNS first.
