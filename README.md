# what-we-build

![what-we-build](assets/hero.svg)

![License: MIT](https://img.shields.io/badge/license-MIT-green) ![Agent Skill](https://img.shields.io/badge/Agent-Skill-orange)

> Keep a project's context in docs.

what-we-build is an agent skill. It talks your project through with you and writes what you decide into a few docs, so every new window of your agent still knows it. Nothing goes into a doc before you agree it.

## What it does

- 💬 **Talks before it writes:** it discusses each doc with you and writes down only what you agree.
- 🤔 **Pushes back:** it says why an idea is weak and keeps making its case until you decide.
- ✅ **Proves each doc is done:** it checks every line against the doc's guide and shows you what each check found.
- 📍 **Starts from where you are:** an idea, running code or docs it did not write.
- 🏠 **Gives every fact one home:** each doc answers one question.
- 🧠 **Keeps the context while you work:** the agent reads the owning doc first and records each decision at once.
- ⏯️ **Resumes where you stopped:** every agreed point is already in its doc and every open one in TODO.

## Install

```sh
git clone https://github.com/jinhuang712/what-we-build.git ~/dev/skills/what-we-build && ln -s ~/dev/skills/what-we-build/skills/what-we-build ~/.claude/skills/what-we-build
```

How to update or remove it is in [INSTALL.md](INSTALL.md).

## How to use

- **Start:** type `/what-we-build` in your project folder and say what you want, such as "a CLI for my reading notes".
- **The folder:** the agent reads it first, whether it is empty or holds code or old docs.
- **The talk:** the agent goes through each doc with you one point at a time.
- **The commit:** each doc is committed once you approve it.

Afterwards the folder holds:

```
reading-notes/
├── AGENTS.md         what every new window reads first
├── PROPOSAL.md       why it exists
├── PHILOSOPHY.md     why it is this way
├── DESIGNS.md        what the design must always satisfy
├── FEATURES.md       what it does
├── CLI.md            how it is called
├── README.md         what it is and how to start
├── CHANGELOG.md      what changed
├── specs/decisions/  why each choice was made
└── plan/
    ├── GOALS.md      what is checked
    ├── ROADMAP.md    how far along it is
    └── TODO.md       what is still open
```

## Architecture

```text
/what-we-build ──▶ SKILL.md ──▶ references/ ──▶ your docs
```

## Docs

This repo's docs were written with the skill, so each one is an example of its output.

| Doc | Answers |
|---|---|
| [PROPOSAL](PROPOSAL.md) | Why did we start this? |
| [PHILOSOPHY](PHILOSOPHY.md) | Why is it this way? |
| [DESIGNS](DESIGNS.md) | What must the design always satisfy? |
| [GOALS](GOALS.md) | What do we check, and when? |
| [FEATURES](FEATURES.md) | What does it do, and what will it do? |
| [ROADMAP](ROADMAP.md) | When, and how far along? |
| [Architecture](specs/ARCHITECTURE.md) | How do the parts fit together? |
| [Decisions](specs/decisions/) | Why this and not the other ways? |
| [TODO](TODO.md) | What is open? |
| [CHANGELOG](CHANGELOG.md) | What changed? |
| [INSTALL](INSTALL.md) | How do I install, update or remove it? |
| [AGENTS](AGENTS.md) | What must a coding agent working here know? |

## Known limits

- The wording rules are written for English docs.

## License

[MIT](LICENSE)
