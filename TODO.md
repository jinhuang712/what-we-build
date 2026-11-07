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
- blocks: [CP2.8: The talk is proven](ROADMAP.md#cp28-the-talk-is-proven)

### [P1][DISCUSSION] What a checkpoint is

- description: the ROADMAP guide says nothing on order or acceptance, and one run went through about ten checkpoint trees
- created: 2026-11-05
- found: the 2026-11-05 run on a diagram tool
- next:
  - decide whether a later checkpoint must depend on the one before it
  - decide how a checkpoint is accepted
  - decide which goal proves the features of [F3: Getting the docs](features/F3-getting-the-docs.md)
- blocks: [CP2.10: The doc set is proven](ROADMAP.md#cp210-the-doc-set-is-proven)

### [P1][DISCUSSION] How far the start pass verifies

- description: a pass over docs already in format should cost far less than this run
- created: 2026-11-05
- found: the 2026-11-05 run on a diagram tool, which read about 472KB and checked licenses and CI at about $3 before any edit

### [P1][ISSUE] A reading pass misses a wording rule

- description: a pass that read every doc called the fix thorough while lines broke a rule of *Wording*, and the check should catch that without a search step for each rule
- created: 2026-11-08
- found: the 2026-11-08 run on a diagram tool, which left 49 lines with three or more "and" while its lint, tests and links all passed

### [P1][DISCUSSION] A pass says what it read and how

- description: the proof of a pass should name what was read in full and what was only sampled
- created: 2026-11-08
- found: the 2026-11-08 run on a diagram tool, which admitted that its pass before had only sampled the docs

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
