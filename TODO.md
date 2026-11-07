# TODO

## ongoing

### [P1][DISCUSSION] The time limit for O1: The core docs without a long talk

- description: set N in [O1: The core docs without a long talk](GOALS.md#o1-the-core-docs-without-a-long-talk), the hours of talk a new project's core docs may take
- created: 2026-11-03
- blocks: [CP2.8: The talk is proven](ROADMAP.md#cp28-the-talk-is-proven)

### [P1][TASK] Test the start pass on a real project

- description: check that the pass in [041: Every start puts the docs in the format](specs/decisions/041-every-start-puts-the-docs-in-the-format.md) truly judges each item and does not skip the talk
- created: 2026-11-05
- found: the 2026-11-05 run on a diagram tool, which read every guide itself and still grouped FEATURES by noun
- next: run it in a new window, since the 2026-11-08 run came after a compaction in an old one and still carried that talk
- blocks: [CP2.8: The talk is proven](ROADMAP.md#cp28-the-talk-is-proven)

### [P2][DISCUSSION] How to evaluate the skill

- description: which test prompts to use and how many rounds [O2: Context survives compaction](GOALS.md#o2-context-survives-compaction) runs before it compacts, with what a good run looks like in numbers
- created: 2026-11-02
- blocks: [CP4: Proven useful](ROADMAP.md#cp4-proven-useful)

### [P2][IDEA] Show a doc's whole structure when its talk starts

- description: the user asked for the whole tree again and again, since a line-by-line talk hides structural problems
- created: 2026-11-05
- found: the 2026-11-05 run on a diagram tool

### [P2][ISSUE] A hung command after the turn ended

- description: an unbounded grep moved to the background as the agent ended its turn, which left the run idle for 10 minutes
- created: 2026-11-05
- found: the 2026-11-05 run on a diagram tool

### [P2][TASK] Install steps for other agents

- description: [INSTALL.md](INSTALL.md) has tried steps only for Claude Code, though any agent that loads Agent Skills can use the skill
- created: 2026-11-04
- related: [037: The skill is written for any agent](specs/decisions/037-the-skill-is-written-for-any-agent.md)
