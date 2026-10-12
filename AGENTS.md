# AGENTS.md

Guidance for coding agents working on what-we-build.

## Read first

- [PHILOSOPHY.md](PHILOSOPHY.md): the test every change must pass.
- [FEATURES.md](FEATURES.md): what the skill does.
- [DESIGNS.md](DESIGNS.md): how it is built, and why.

## Rules

- **This repo uses its own format.** Place every fact with the placement test in `skills/what-we-build/SKILL.md`. One home per fact. Other docs link to it.
- **Keep `SKILL.md` under 500 lines.** Detail goes into a reference file that `SKILL.md` points to.
- **Scripts use only Python's standard library.** No dependencies.
- **Write the rules in our own words.** Copy no text from style standards or other skills.
- **Keep the marks honest.** Only the user approves a doc. An agent writes `drafted`, never `approved`.

## Before you finish

```sh
python3 skills/what-we-build/scripts/check_links.py *.md skills/what-we-build/*.md skills/what-we-build/references/*.md
python3 skills/what-we-build/scripts/blank_lines.py *.md skills/what-we-build/*.md skills/what-we-build/references/*.md
```

## Releasing

Bump the version in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` together, and add a section to [CHANGELOG.md](CHANGELOG.md).
