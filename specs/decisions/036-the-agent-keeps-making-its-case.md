# 036. The agent keeps making its case until the user decides

Decided: 2026-11-04

## The problem

Up to 2026-10-31 `SKILL.md` said to push back with a reason, keep making the case while the user weighs it and drop it only once the user rejects it. The rewrite of that day kept only "challenge the user's ideas where they are weak" and recorded no decision. FEATURES still promised that the agent keeps it up until the user decides, and nothing in the skill asked for it. In the runs before 2026-11-04 the agent often wrote down what the user said as soon as it was said.

## The choice

A talk goes both ways. The agent pushes back with its reason and keeps making the case while the user is still weighing it. It weighs what the user says with them before it writes it down. Once the user rejects a point, the agent drops it and raises it again only with a new fact.

## Not chosen

- Push back once and then follow: the user hears one objection and the talk turns into dictation.
- Push back until the user agrees: the user decides, and a point the user rejected stays rejected.

## Consequences

`SKILL.md` gains three lines under *How you work with the user*, and F1.4: Push back says again what the skill asks for.
