<!-- what-we-build: drafted 2026-10-12 -->

# Designs

How what-we-build is built and why. Behavior is in [FEATURES.md](FEATURES.md).

## Design principles

- **Manual start only.** The skill never loads itself. The user types `/what-we-build`.
- **Short core, detail on demand.** `SKILL.md` holds the roles, the rules and the flow. Each doc's questions and skeleton, the wording rules and the revisit procedure live in reference files that the agent reads when it needs them.
- **The docs are the state.** A mark on the first line of each doc records drafted or approved. There is no state file to drift from the docs.
- **No dependencies.** Markdown and Python's standard library. Nothing to install.
- **Our own words.** The wording rules borrow methods from controlled languages such as ASD-STE100, and copy no text from them.

## Structure

```text
what-we-build/
├── .claude-plugin/
│   ├── plugin.json          the plugin manifest
│   └── marketplace.json     lets `claude plugin marketplace add` find it
├── skills/what-we-build/
│   ├── SKILL.md             roles, rules, modes, flow, mistakes to avoid
│   ├── references/
│   │   ├── docs.md          per doc: question, owns, leaves out, voice, ask, skeleton, done when
│   │   ├── wording.md       wording rules and the voice of each doc
│   │   └── revisit.md       the revisit procedure and a brief template for subagents
│   └── scripts/
│       ├── check_links.py   broken relative links and anchors
│       └── blank_lines.py   blank lines around blocks
└── PROPOSAL.md, PHILOSOPHY.md, GOALS.md, FEATURES.md, DESIGNS.md, ROADMAP.md, README.md, ...
```

The repo's own docs follow the skill's format.

## Triggering

Behavior: FEATURES.md → F1.

- `disable-model-invocation: true` in the frontmatter keeps the skill out of automatic use (decided 2026-10-12: a session costs the user an hour of attention, so it starts on purpose). An earlier Claude Code bug that blocked the slash command too (anthropics/claude-code#26251) was closed as a duplicate on 2026-02-20.
- An argument picks the mode: `new`, `resume` or `revisit`. Without one, the skill reads the folder and picks.

## Modes

Behavior: FEATURES.md → F1, F2, F3.

- One skill with three modes, not three skills (decided 2026-10-12): the modes share the roles, the rules and the wording, and a user should not need to know which one to call.
- The revisit procedure sits in its own reference file, because a new-project session never needs it.

## Session state

Behavior: FEATURES.md → F2.

- An HTML comment on the first line: `<!-- what-we-build: drafted YYYY-MM-DD -->`, then `approved` (decided 2026-10-12). It is invisible when rendered, it travels with the file, and a resume reads it with no other state. The idea of per-section fill marks comes from jig's `vision-elicitation` skill (MIT). The format here is our own.
- Only the user approves. The skill never writes `approved` on a doc the user has not read.

## Checks

Behavior: FEATURES.md → F6.

- `check_links.py` follows GitHub's heading slugs: lowercase, punctuation removed, spaces to hyphens, `-1`, `-2` for repeated headings. It skips code spans, fenced blocks and external links.
- `blank_lines.py` compares every non-blank line before and after. It writes only when they match, so it can never change content.
- Both were tested on crafted files with known bad links, and on a real doc set of 9 files.

## Prior art

- jig's `vision-elicitation` (ramboz/jig, MIT) runs a fixed 13-section questionnaire after jig's own scaffold and fills two templates. Decided 2026-10-12 to build our own: the doc set, the conversation with push-back, the goals with numbers and the manual trigger are what this skill is for, and jig's skill has none of them.

## Distribution

- A public GitHub repo with a plugin manifest at the root, so `claude plugin marketplace add jinhuang712/what-we-build` installs it. As a plugin, the command is `/what-we-build:what-we-build`.
- The author links the skill folder into `~/.claude/skills/what-we-build`, so the command is `/what-we-build`.
- The name was chosen on 2026-10-12 after a GitHub search: no repo had it. `docs-compass` was dropped because `mongodb/docs-compass` exists.

## Licensing

MIT. See [LICENSE](LICENSE).

## Open questions

- How to evaluate the skill: which test prompts, and what a good session looks like in numbers.
