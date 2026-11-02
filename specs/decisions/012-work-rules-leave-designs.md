# 012. This repo's work rules leave DESIGNS

Decided: 2026-11-03

## The problem

DESIGNS held three guidelines that steer how this repo is worked on and not what the skill must be. They said that readers check the docs instead of scripts, that the skill is tested by use first and that the repo is its own first example. The last one was also a rule in AGENTS.md, so it had two homes. A project that copies this repo would learn to put its work rules in DESIGNS.

## The choice

The three move to *Rules* in AGENTS.md, which the placement test now names as the home of a rule for how the work is done. DESIGNS keeps the six commitments the skill must meet wherever it runs. That the skill ships no check scripts stays in FEATURES under *Not planned* and rests on DESIGNS 3: No dependencies.

## Not chosen

- Keeping readers check the docs in DESIGNS: its product side is already covered by no dependencies, and the rest is how this repo is checked.
- Keeping all three as design guidelines: each would keep a second home or teach the wrong placement.

## Consequences

DESIGNS lists 6 guidelines. The links from FEATURES and ROADMAP to the old guideline 7 now point to DESIGNS 3: No dependencies.
