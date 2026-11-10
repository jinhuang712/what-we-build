# 041. Every start puts the docs in the format

Decided: 2026-11-05

## The problem

A rule told the agent not to move old docs into the new format before a talk, since a test on three repos had shown it skipping the talk. In a run on a diagram tool the talk then drifted from design to design for hours, and three core docs were never reached. The user had to direct each step, and the structures that broke their guides were found by the user.

## The choice

Every start first puts every doc in the skill's format, on the agent's own and with no condition. The pass judges each item again and rebuilds any structure that breaks its guide. It adds no new fact or point and raises no design topic. What only the user can give goes to `TODO.md` as a `DISCUSSION`. The pass ends with the proof for each doc and the list of open topics, and the talk starts after it.

This replaces the rule against moving old docs before a talk.

## Not chosen

- Keep the talk first: the user directs every step and the cleanup never ends.
- Run the pass only when a doc breaks its guide: the agent would judge that the pass is not needed.
- Let the pass settle small design topics: "small" is a judgment, and the pass would turn into a talk.

## Consequences

Every start costs a pass over the whole doc set. The agent changes docs before the user has seen them, so git must be in place and a commit waits for the user. An old risk may return: a pass can look finished while nothing was truly judged. A run on a real project must test this.
