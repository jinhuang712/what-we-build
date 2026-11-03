# TODO

## ongoing

### [P1][DISCUSSION] The time limit for O1: The core docs without a long talk
- description: set N in [O1: The core docs without a long talk](GOALS.md#o1-the-core-docs-without-a-long-talk), the hours of talk a new project's core docs may take
- created: 2026-11-03
- blocks: [CP3: First real use](ROADMAP.md#cp3-first-real-use)

### [P2][DISCUSSION] How to evaluate the skill
- description: which test prompts to use, and what a good run looks like in numbers
- created: 2026-11-02
- blocks: [CP4: Proven useful](ROADMAP.md#cp4-proven-useful)

### [P1][TASK] Test the tagged guides in real use
- description: run the skill on a project and see whether the `[YES]` `[NO]` `[MAYBE]` `[WHEN]` lines stop the mistakes of the 2026-11-03 run
- created: 2026-11-03
- found: a run on a Go library grouped FEATURES by code module, let subagents rewrite every doc and read none itself
- next: rerun the FEATURES rewrite there and compare
- related: [029: A guide is written in tagged lines](specs/decisions/029-a-guide-is-written-in-tagged-lines.md) and [030: The main window reads and writes the docs](specs/decisions/030-the-main-window-reads-and-writes-the-docs.md)

### [P2][DISCUSSION] Where the details moved out in a rewrite go
- description: a rewrite moved about 190 API details out of FEATURES with no home, and most were already in the code's doc comments
- created: 2026-11-03
- next: decide whether the placement test says a detail in a doc comment needs no doc

### [P2][DISCUSSION] Type names in the FEATURES of a library
- description: FEATURES leaves out type names, yet for a library the names a user types are what the user sees
- created: 2026-11-03
- related: the `[MAYBE]` type name line in the GLOSSARY guide

### [P2][DISCUSSION] Reading again after a compaction
- description: the run skipped the read order after a compaction although the rule says to read it, and the user does not want a check that thickens the rules
- created: 2026-11-03

### [P2][TASK] Test that an imported AGENTS.md survives a compaction
- description: Claude Code's docs say the root CLAUDE.md is re-read after a compaction, and do not say whether a file it imports with `@AGENTS.md` is
- created: 2026-11-03
- next: compact a session in a project whose CLAUDE.md holds `@AGENTS.md`, then check whether the rules are still in context
- related: [032: AGENTS.md keeps a copy of the rules that the host loads](specs/decisions/032-agents-md-keeps-a-copy-the-host-loads.md)
