<!-- what-we-build: drafted 2026-10-13 -->

# Designs

How what-we-build is built, and why it is built that way. The skill is a set of Markdown instructions that an agent reads, plus two small scripts. This doc holds the choices behind that shape. What the skill does for the user is in [FEATURES.md](FEATURES.md).

## Design principles

These hold everywhere in the repo. Each one says what it forbids.

- **Short core, detail on demand.** `SKILL.md` holds what every session needs: the roles, the rules, the flow. Each doc's guide, the wording rules and the revisit procedure live in reference files that the agent reads only when a step points to them. This keeps the always-read part small, so the agent attends to it. It forbids growing `SKILL.md` with material only some sessions use.
- **The docs are the state.** A mark on the first line of each doc records whether it is drafted or approved. It forbids a separate state file, which would drift from the docs it describes.
- **No dependencies.** Markdown and Python's standard library. It forbids anything a user must install before the first session.
- **Our own words.** The wording rules borrow methods from controlled languages such as ASD-STE100, and from other writing guides, rewritten for this skill. It forbids copying text from a standard or another skill.

## Structure

The repo is both a Claude Code plugin and a plain skill folder.

- `skills/what-we-build/SKILL.md` holds what every session needs.
- `skills/what-we-build/references/` holds what only some sessions need: one guide per doc, the wording rules, the revisit procedure.
- `skills/what-we-build/scripts/` holds the two checks.
- Decided 2026-10-12: the plugin manifest sits at the repo root, so the repo installs as a plugin and also works when its skill folder is linked into `~/.claude/skills`. Install steps are in [README.md](README.md).

The repo's own docs are written in the format the skill teaches, so they double as its example.

## Triggering

Behavior: FEATURES.md → Not planned (starting on its own).

- Decided 2026-10-12: `disable-model-invocation: true` in the frontmatter keeps the skill out of automatic use, so it loads only when the user types the command.
- An earlier Claude Code bug blocked the slash command too for skills with this field (anthropics/claude-code#26251). It was closed as a duplicate on 2026-02-20.

## Modes

Behavior: FEATURES.md → F1, F2, F3.

- Decided 2026-10-12: one skill with three modes, not three skills. The modes share the roles, the rules and the wording, and a user should not need to know which skill to call.

## Session state

Behavior: FEATURES.md → F2.

- Decided 2026-10-12: an HTML comment on each doc's first line, `<!-- what-we-build: drafted YYYY-MM-DD -->`, later `approved`. It is invisible when rendered, it travels with the file, and a resume needs no other state. The idea of per-section fill marks comes from jig's `vision-elicitation` skill (MIT). The format here is our own.
- Decided 2026-10-13: an edit resets the mark (FEATURES.md → F2), because a stale `approved` would claim an agreement that never happened.

## Checks

Behavior: FEATURES.md → F6.

- `blank_lines.py` compares every non-blank line before and after, and writes only when they all match. So it can repair layout without any risk to content.

## Prior art

- Decided 2026-10-12: build our own instead of using jig's `vision-elicitation` (ramboz/jig, MIT). That skill runs a fixed 13-section questionnaire after jig's own scaffold and fills two templates. The doc set, the conversation with push-back, the goals with numbers and the manual start are what this skill is for, and jig's skill has none of them.
- The writing guidance of mattpocock/skills (MIT) shaped three rules in 0.2.0: state the target instead of the ban, treat a doc that restates the code as a cache, and record only decisions that are hard to reverse, surprising and a real trade-off.

## Licensing

MIT. See [LICENSE](LICENSE).

## Open questions

- How to evaluate the skill: which test prompts, and what a good session looks like in numbers. (ROADMAP.md → M3.)
