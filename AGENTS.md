# AGENTS.md

Guidance for coding agents working on what-we-build. It holds what an agent cannot learn by reading the files.

## Read order

Read these when the window is new or was compacted:

1. [PHILOSOPHY.md](PHILOSOPHY.md): the thought every change agrees with.
2. [DESIGNS.md](DESIGNS.md): the guidelines a change must meet.
3. [FEATURES.md](FEATURES.md): what the skill does.
4. [ROADMAP.md](ROADMAP.md): where the work stands.
5. [GOALS.md](GOALS.md): what is checked and its last result.
6. [TODO.md](TODO.md): what is open.

## Layout

- The core docs sit at the root with TODO, CHANGELOG and INSTALL.
- `specs/` holds ARCHITECTURE and `decisions/`.
- The skill lives in `skills/what-we-build/`, with a guide per doc in `references/`.
- This repo does not use `plan/`.

## While you work

- [YES]   read each doc you work on in the main window, in full.
- [YES]   track where the project stands by scanning `TODO.md`, `ROADMAP.md` and `GOALS.md`.
- [NO]    hand a doc to a subagent to read or write.
- [NO]    a goal check for a small change.
- [MAYBE] read all the docs in one go.
- [WHEN]  you are about to change something: read the doc that owns it first.
- [WHEN]  the work needs the code: a subagent may read it.
- [WHEN]  a choice had another way open, may be undone later and has a reason the code does not show: write a decision in `specs/decisions/` at once.
- [WHEN]  something cannot be handled now: add it to `TODO.md` at once.
- [WHEN]  the docs and the code disagree: tell the user and let them decide.
- [WHEN]  other developers build on the project: tell the user it may need a wiki, and leave its form to them.
- [WHEN]  a change is done: update `CHANGELOG.md` and the feature's status in the same change.
- [WHEN]  a todo is handled: delete it in the same change.
- [WHEN]  a change is made: check only what it touched against the rules.
- [WHEN]  a checkpoint ends or a release is near: check the goals in `GOALS.md`.
- [WHEN]  the user stops you: stop at once, with every agent you started and every agent those started.

## Rules

- [YES]   follow the skill's format and placement test, since this repo is the skill's first example.
- [YES]   keep `SKILL.md` within T4: A short skill, and put detail in a guide it points to.
- [YES]   follow the guidelines in [DESIGNS.md](DESIGNS.md).
- [YES]   test the skill in real use first, and write test prompts from what they show.
- [YES]   show a change as its skeleton first and then as a diff of before and after.
- [NO]    a script that checks the links and the facts in the docs, since a reader does.
- [NO]    a doc committed before the user approves it.
- [NO]    an outcome settled before you have discussed it with the user and looked at what exists together.

## Before you finish

- Check each sentence you changed against the *Wording* section of `skills/what-we-build/SKILL.md`.
- Check each line in a doc against that doc's guide in `skills/what-we-build/references/`.
- Check each link you touched against its target.
- Check that each fact you added or moved has no second home.
- Check that each decision you wrote says what was not chosen and why.
- Check that each list of tagged lines in `skills/` holds at least two kinds of tag in the order `[YES]` `[NO]` `[MAYBE]` `[WHEN]`.
- Check that what you added to `skills/` is Markdown in our own words, with examples that meet DESIGNS 5: Examples the reader knows.

## Releasing

1. Move the *Unreleased* entries in `CHANGELOG.md` under the new version and date.
2. Go through every goal in `GOALS.md` that can run by then.
3. Commit and tag `vX.Y.Z`, then push the branch and the tag.
