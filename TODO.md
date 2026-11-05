# TODO

## ongoing

### [P1][DISCUSSION] The time limit for O1: The core docs without a long talk

- description: set N in [O1: The core docs without a long talk](GOALS.md#o1-the-core-docs-without-a-long-talk), the hours of talk a new project's core docs may take
- created: 2026-11-03
- blocks: [CP2.8: The talk is proven](ROADMAP.md#cp28-the-talk-is-proven)

### [P1][DISCUSSION] The goal that proves the doc set

- description: no goal proves the features of [F3: Getting the docs](features/F3-getting-the-docs.md) since [T4: A short skill](GOALS.md#t4-a-short-skill) and [T8: A doc read in one go](GOALS.md#t8-a-doc-read-in-one-go) check only the size of the skill and its docs
- created: 2026-11-04
- blocks: [CP2.10: The doc set is proven](ROADMAP.md#cp210-the-doc-set-is-proven)
- related:
  - [CP1: Write and publish](ROADMAP.md#cp1-write-and-publish)

### [P1][TASK] Test the tagged guides in real use

- description: run the skill on a project and see whether the `[YES]` `[NO]` `[MAYBE]` `[WHEN]` lines stop the mistakes of the 2026-11-03 run
- created: 2026-11-03
- found: a run on a Go library grouped FEATURES by code module, let subagents rewrite every doc and read none itself
- next: rerun the FEATURES rewrite there and compare
- related:
  - [029: A guide is written in tagged lines](specs/decisions/029-a-guide-is-written-in-tagged-lines.md)
  - [030: The main window reads and writes the docs](specs/decisions/030-the-main-window-reads-and-writes-the-docs.md)

### [P1][TASK] Test the start pass on a real project

- description: check that the pass in [041: Every start puts the docs in the format](specs/decisions/041-every-start-puts-the-docs-in-the-format.md) truly judges each item and does not skip the talk
- created: 2026-11-05
- found: the 2026-11-05 run on a diagram tool
- blocks: [CP2.8: The talk is proven](ROADMAP.md#cp28-the-talk-is-proven)

### [P1][DISCUSSION] What a checkpoint is

- description: the ROADMAP guide says nothing on order or acceptance, and one run went through about ten checkpoint trees
- created: 2026-11-05
- found: the 2026-11-05 run on a diagram tool
- next: decide whether a later checkpoint must depend on the one before it, how a checkpoint is accepted and whether a goal may sit in several checkpoints

### [P2][DISCUSSION] How to evaluate the skill

- description: which test prompts to use and how many rounds [O2: Context survives compaction](GOALS.md#o2-context-survives-compaction) runs before it compacts, with what a good run looks like in numbers
- created: 2026-11-02
- blocks: [CP4: Proven useful](ROADMAP.md#cp4-proven-useful)

### [P2][DISCUSSION] Where the details moved out in a rewrite go

- description: a rewrite moved about 190 API details out of FEATURES with no home, and most were already in the code's doc comments
- created: 2026-11-03
- found: the rewrite of FEATURES in a run on a Go library
- next: decide whether the placement test says a detail in a doc comment needs no doc

### [P2][DISCUSSION] Type names in the FEATURES of a library

- description: FEATURES leaves out type names, yet for a library the names a user types are what the user sees
- created: 2026-11-03
- related: [the GLOSSARY guide](skills/what-we-build/references/GLOSSARY.md), whose *Term* list allows a type name as a `[MAYBE]`

### [P2][DISCUSSION] Whether a comparison can fail

- description: the GOALS guide says a comparison has no pass or fail, and the user wanted a target to beat
- created: 2026-11-05
- found: the 2026-11-05 run on a diagram tool

### [P2][DISCUSSION] A status mark for a measure

- description: a measure has no pass or fail, so its line in the Summary has no fitting mark
- created: 2026-11-05
- found: the 2026-11-05 run on a diagram tool

### [P2][DISCUSSION] Planned features in the tree or in Later

- description: the user wanted every feature not yet built in the tree, and the guide keeps maybes in *Later*
- created: 2026-11-05
- found: the 2026-11-05 run on a diagram tool

### [P2][DISCUSSION] How much finished work a doc keeps

- description: GOALS keeps only the last result, and the user wants finished checkpoints kept in full
- created: 2026-11-05
- found: the 2026-11-05 run on a diagram tool

### [P2][DISCUSSION] A doc with no guide

- description: a project log of experiments had no home in the doc set
- created: 2026-11-05
- found: the 2026-11-05 run on a diagram tool

### [P2][DISCUSSION] The comma rule and inline lists

- description: a script met the rule by swapping commas for ` · `, which left about 49 lines harder to read
- created: 2026-11-05
- found: the 2026-11-05 run on a diagram tool

### [P2][DISCUSSION] Reading the skill in a public repo

- description: `AGENTS.md` should tell each window to read the skill, yet the skill starts only by hand and other contributors do not have it
- created: 2026-11-05
- found: the 2026-11-05 run on a diagram tool
- related: [002: The skill starts only by hand](specs/decisions/002-manual-start.md)

### [P2][IDEA] Show a doc's whole structure when its talk starts

- description: the user asked for the whole tree again and again, since a line-by-line talk hides structural problems
- created: 2026-11-05
- found: the 2026-11-05 run on a diagram tool

### [P2][TASK] Test that an imported AGENTS.md survives a compaction

- description: Claude Code's docs say the root CLAUDE.md is re-read after a compaction, and do not say whether a file it imports with `@AGENTS.md` is
- created: 2026-11-03
- next: compact a session in a project whose CLAUDE.md holds `@AGENTS.md`, then check whether the rules are still in context
- related: [032: AGENTS.md keeps a copy of the rules that the host loads](specs/decisions/032-agents-md-keeps-a-copy-the-host-loads.md)

### [P2][TASK] Install steps for other agents

- description: [INSTALL.md](INSTALL.md) has tried steps only for Claude Code, though any agent that loads Agent Skills can use the skill
- created: 2026-11-04
- related: [037: The skill is written for any agent](specs/decisions/037-the-skill-is-written-for-any-agent.md)
