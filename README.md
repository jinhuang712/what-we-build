# what-we-build

![what-we-build](assets/hero.svg)

![License: MIT](https://img.shields.io/badge/license-MIT-green) ![Claude Code skill](https://img.shields.io/badge/Claude%20Code-skill-orange)

> Keep a project's context in docs.

what-we-build is a Claude Code skill that keeps a project's context in docs. You and the agent work out what to build and why. The skill writes it down so it outlives every window. It writes no doc until you agree on its key points.

## What it does

- 💬 **Talks before it writes:** it discusses each doc with you and drafts it only after you agree.
- 📍 **Starts from where you are:** an idea, running code or messy docs.
- 🏠 **Gives every fact one home:** each doc answers one question.
- 🧠 **Keeps the context while you work:** the agent reads the owning doc first and records each decision at once.
- ⏯️ **Resumes where you stopped.**

## Install

```sh
git clone https://github.com/jinhuang712/what-we-build.git ~/dev/skills/what-we-build && ln -s ~/dev/skills/what-we-build/skills/what-we-build ~/.claude/skills/what-we-build
```

Other ways to install, update or remove it are in [INSTALL.md](INSTALL.md).

## How to use

1. Open Claude Code in an empty folder.
2. Type `/what-we-build` and say in a sentence what you want to build.
3. Talk the proposal through until its key points are agreed.
4. Read the draft as before and after, then approve it.
5. The agent commits it and moves on to the philosophy.

The skill also starts from running code or messy docs, and it resumes where you stopped.

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
| [Decisions](specs/decisions/) | Why did we choose this, and what did we not choose? |
| [TODO](TODO.md) | What is open? |
| [CHANGELOG](CHANGELOG.md) | What changed? |
| [INSTALL](INSTALL.md) | How do I install, update or remove it? |
| [AGENTS](AGENTS.md) | What must a coding agent working here know? |

## Known limits

- The wording rules are written for English docs.
- It has been tested by hand and not yet with evals.

## License

[MIT](LICENSE)
