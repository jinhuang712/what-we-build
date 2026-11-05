# 046. A window reads the skill where it is installed

Decided: 2026-11-05

## The problem

The rules in `AGENTS.md` tell each new window to read the skill. The skill is personal and starts only by hand, so a contributor to a public repo has no copy to read. In a run on a diagram tool the rule was left out of `AGENTS.md` for that reason, and no window was told to read the skill any more.

## The choice

The rule stays in `AGENTS.md` with a condition: a window reads the skill if it is installed, and then reads every doc in the read order.

## Not chosen

- Copy the skill into each project: the copy falls behind and gives the skill a second home.
- Leave the rule out: the owner's own windows then never read the guides.

## Consequences

A window without the skill works from `AGENTS.md` and the docs alone, so it may write a doc against its guide. The next start with the skill brings that doc back in line.
