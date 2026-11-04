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

### [P2][DISCUSSION] How to evaluate the skill

- description: which test prompts to use, and what a good run looks like in numbers
- created: 2026-11-02
- blocks: [CP4: Proven useful](ROADMAP.md#cp4-proven-useful)

### [P2][DISCUSSION] Where the details moved out in a rewrite go

- description: a rewrite moved about 190 API details out of FEATURES with no home, and most were already in the code's doc comments
- created: 2026-11-03
- next: decide whether the placement test says a detail in a doc comment needs no doc

### [P2][DISCUSSION] Type names in the FEATURES of a library

- description: FEATURES leaves out type names, yet for a library the names a user types are what the user sees
- created: 2026-11-03
- related: [the GLOSSARY guide](skills/what-we-build/references/GLOSSARY.md), whose *Term* list allows a type name as a `[MAYBE]`

### [P2][TASK] Test that an imported AGENTS.md survives a compaction

- description: Claude Code's docs say the root CLAUDE.md is re-read after a compaction, and do not say whether a file it imports with `@AGENTS.md` is
- created: 2026-11-03
- next: compact a session in a project whose CLAUDE.md holds `@AGENTS.md`, then check whether the rules are still in context
- related: [032: AGENTS.md keeps a copy of the rules that the host loads](specs/decisions/032-agents-md-keeps-a-copy-the-host-loads.md)

### [P2][TASK] Install steps for other agents

- description: [INSTALL.md](INSTALL.md) has tried steps only for Claude Code, though any agent that loads Agent Skills can use the skill
- created: 2026-11-04
- related: [037: The skill is written for any agent](specs/decisions/037-the-skill-is-written-for-any-agent.md)
