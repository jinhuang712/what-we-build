<!-- what-we-build: drafted 2026-10-13 -->

# what-we-build

> Talk a project into being, one document at a time.

what-we-build is a Claude Code skill for the start of a project. It writes no document until you have agreed on its key points.

Coding agents write documents faster than people think, and they fill every gap with a guess that sounds sure. This skill slows the writing down to the speed of your decisions: you talk each document through first, and the agent writes down what you agreed.

> **Status:** how far it has been used, and what comes next, is in [ROADMAP.md](ROADMAP.md).

## What it does

- **Talks before it writes.** It discusses and brainstorms with you, recommends a choice when one is ready, and drafts a doc only after you agree on its key points.
- **Pushes back** on goals without numbers and principles that are really features.
- **Gives every fact one home:** seven documents, each answering one question.
- **Resumes** where you stopped, and **revisits** docs that drifted.

## What you get

| Doc | The question it answers |
|---|---|
| [PROPOSAL](PROPOSAL.md) | Why did we start this? |
| [PHILOSOPHY](PHILOSOPHY.md) | Why is it this way? |
| [GOALS](GOALS.md) | What do we measure? |
| [FEATURES](FEATURES.md) | What does it do, and what will it do? |
| [DESIGNS](DESIGNS.md) | How is it built, and why that way? |
| [ROADMAP](ROADMAP.md) | When, and how far along? |
| README | What is this, and how do I start? |

This repo's own docs were written with the skill, so each link is an example of its output.

## Install

### As a plugin

```sh
claude plugin marketplace add jinhuang712/what-we-build
claude plugin install what-we-build@what-we-build
```

The command is then `/what-we-build:what-we-build`, because a plugin's skills carry the plugin's name (not yet verified with this plugin).

### As a personal skill

```sh
git clone https://github.com/jinhuang712/what-we-build.git ~/dev/skills/what-we-build
ln -s ~/dev/skills/what-we-build/skills/what-we-build ~/.claude/skills/what-we-build
```

The command is then `/what-we-build`. Start a new Claude Code session after you install it.

## When to reach for it

| Situation | Type |
|---|---|
| You are starting a project | `/what-we-build` |
| You stopped halfway | `/what-we-build resume` |
| Your docs repeat each other or drifted from the code | `/what-we-build revisit` |

It starts only when you type it. Installed as a plugin, type `/what-we-build:what-we-build` in place of `/what-we-build`.

## Known limits

- It writes English docs. Wording rules for other languages are on the *Later* list.
- It has been tested by hand, not yet with evals.

## More documents

[Changelog](CHANGELOG.md) · [Agents](AGENTS.md) (for coding agents working here)

## License

[MIT](LICENSE)
