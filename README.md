<!-- what-we-build: drafted 2026-10-12 -->

# what-we-build

> Talk a project into being, one document at a time.

what-we-build is a Claude Code skill for the start of a project. You bring the idea. The agent asks the questions that turn it into the founding documents, one decision at a time, and writes each document only after you agree on it. Each document answers one question, so every fact has one home.

> **Status: 0.1.0.** Written and published. Not yet used on a real project end to end (see [ROADMAP.md](ROADMAP.md)).

## What it does

- **Drafts the founding docs through a conversation.** Proposal, philosophy, goals, features, designs, roadmap and README, in that order. Optional docs join when the project needs them.
- **Asks one decision at a time,** with a recommendation and its reason. You decide.
- **Pushes back** on goals without numbers, principles that are really features, and decisions without reasons.
- **Resumes** a session from marks on each doc.
- **Revisits** a doc set that overlaps, sprawls or drifted from the code.

| Doc | Answers |
|---|---|
| PROPOSAL | Why did we start this? |
| PHILOSOPHY | Why is it this way? |
| GOALS | What do we measure? |
| FEATURES | What does it do, and what will it do? |
| DESIGNS | How is it built, and why that way? |
| ROADMAP | When? |
| README | What is this, and how do I start? |

## Install

### As a plugin

```sh
claude plugin marketplace add jinhuang712/what-we-build
claude plugin install what-we-build@what-we-build
```

The command is then `/what-we-build:what-we-build`.

### As a personal skill

```sh
git clone https://github.com/jinhuang712/what-we-build.git ~/dev/skills/what-we-build
ln -s ~/dev/skills/what-we-build/skills/what-we-build ~/.claude/skills/what-we-build
```

The command is then `/what-we-build`. Start a new Claude Code session after you install it.

## Use

In a project folder, start Claude Code and type:

```text
/what-we-build             start, or pick the mode from what the folder holds
/what-we-build resume      continue at the first doc that is not approved
/what-we-build revisit     clean up a doc set that drifted
```

The skill never starts on its own.

## Known limits

- It writes English docs. Wording rules for other languages are on the *Later* list.
- It has been tested by hand, not yet with evals.

## Documents

[Proposal](PROPOSAL.md) (why we started) · [Philosophy](PHILOSOPHY.md) (why it is this way) · [Goals](GOALS.md) (what we measure) · [Features](FEATURES.md) (what it does) · [Designs](DESIGNS.md) (how it is built) · [Roadmap](ROADMAP.md) (when) · [Changelog](CHANGELOG.md) · [Agents](AGENTS.md) (for coding agents working here)

## License

[MIT](LICENSE)
