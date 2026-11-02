# AGENTS.md

Guidance for coding agents working on what-we-build. It holds what an agent cannot learn by reading the files.

## Read order

Read these when a sitting starts or after the window was compacted:

1. [PHILOSOPHY.md](PHILOSOPHY.md): the thought every change agrees with.
2. [DESIGNS.md](DESIGNS.md): the guidelines a change must meet.
3. [FEATURES.md](FEATURES.md): what the skill does.
4. [TODO.md](TODO.md): what is open.

Before a change, also read the doc that owns it.

## Layout

- The core docs sit at the root with TODO, CHANGELOG and INSTALL.
- `specs/` holds ARCHITECTURE and `decisions/`.
- The skill lives in `skills/what-we-build/`, with a guide per doc in `references/`.
- This repo does not use `plan/`.

## While you work

- Before you change something, read the doc that owns it.
- Track where the project stands by scanning `TODO.md`, `ROADMAP.md` and `GOALS.md`.
- When a choice between ways is made, write a decision in `specs/decisions/` at once.
- When something cannot be handled now, add it to `TODO.md` at once.
- When the docs and the code disagree, tell the user and let them decide.
- When a change is done, update `CHANGELOG.md` and the feature's status in the same change.
- When a todo is handled, delete it in the same change.
- Check the goals in `GOALS.md` at a moment that calls for it, such as the end of a checkpoint or a release.
- A small change never runs the goal checks.
- When the user stops you, stop.

## Rules

- **This repo is the skill's first example,** so it follows the skill's format and placement test.
- **Keep `SKILL.md` within T4: A short skill,** and put detail in a guide it points to.
- **Follow the guidelines in [DESIGNS.md](DESIGNS.md).**
- **A reader who did not write a change checks it,** and no script does.
- **Test the skill in real sessions first,** and write test prompts from what they show.
- **Never commit a doc before the user approves it.**
- **Leave the outcome open until you have discussed it with the user,** and look at what exists together first.
- **Show a change as its skeleton first and then as a diff.**

## Before you finish

- Check each sentence you changed against the *Wording* section of `skills/what-we-build/SKILL.md`.
- Check each line in a doc against that doc's guide in `skills/what-we-build/references/`.
- Check each link you touched against its target.
- Check that each fact you added or moved has no second home.
- Check that each decision you wrote says what was not chosen and why.
- Check that what you added to `skills/` is Markdown in our own words with made-up examples.

## Releasing

1. Move the *Unreleased* entries in `CHANGELOG.md` under the new version and date.
2. Set the version in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` to the same value.
3. Go through the whole goal sheet in `GOALS.md`.
4. Commit and tag `vX.Y.Z`, then push the branch and the tag.
