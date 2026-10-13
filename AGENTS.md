# AGENTS.md

Guidance for coding agents working on what-we-build. These rules cover what an agent cannot learn by reading the files.

## Read first

- [PHILOSOPHY.md](PHILOSOPHY.md): the choices every change must agree with.
- [FEATURES.md](FEATURES.md): what the skill does.
- [DESIGNS.md](DESIGNS.md): how it is built, and why.

## Rules

- **This repo uses its own format.** Place every fact with the placement test in `skills/what-we-build/SKILL.md`, because this repo is the skill's first example and must follow it.
- **Keep `SKILL.md` within the limit in GOALS.md G6.** Detail goes into a reference file that `SKILL.md` points to, because the agent reads `SKILL.md` in every session.
- **Follow the design principles in DESIGNS.md,** including no dependencies, our own words and made-up examples. They keep the skill installable anywhere, and free of borrowed text and of other projects.
- **Keep the marks honest.** Only the user approves a doc. An agent writes `drafted`, because an `approved` the user never gave claims an agreement that did not happen.
- **Show changes before asking for approval,** as before-and-after text, because the user reviews changes side by side.

## Before you finish

Run both checks on every doc, so no broken link or crowded block reaches a commit:

```sh
python3 skills/what-we-build/scripts/check_links.py *.md skills/what-we-build/*.md skills/what-we-build/references/*.md skills/what-we-build/references/docs/*.md
python3 skills/what-we-build/scripts/blank_lines.py *.md skills/what-we-build/*.md skills/what-we-build/references/*.md skills/what-we-build/references/docs/*.md
```

## Releasing

1. Move the *Unreleased* entries in [CHANGELOG.md](CHANGELOG.md) under the new version and date.
2. Set the version in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` to the same value.
3. Commit, tag `vX.Y.Z`, and push the branch and the tag.
