<!-- what-we-build: drafted 2026-10-13 -->

# what-we-build — Proposal

> Talk a project into being, one document at a time.

Proposed 2026-10-12. For where the work stands today, see [ROADMAP.md](ROADMAP.md).

## In short

You have an idea. You ask your coding agent for a README, a design doc and a roadmap. Ninety seconds later you have 2,000 confident words, and most of them describe decisions you never made.

Agents write documents faster than people think, and they fill every gap with a guess that sounds sure. what-we-build is a skill that drafts a project's founding documents through a conversation instead: one question per document, one home for each fact, and nothing written before you agree.

## The shift

| Before agents | With agents |
|---|---|
| Docs are slow to write, so few exist | An agent writes a whole doc set in one sitting |
| The author decides each line | The agent fills each gap with a guess |
| Docs drift slowly | Every sitting adds a little, in a new place |
| A reader opens one doc to find a fact | A reader opens all of them |

## Pain points

The numbers come from one real project built with coding agents over two weeks.

1. **Every fact in several places.** "What we will not build" was written in five docs: philosophy, goals, features, roadmap and the command reference.
2. **Docs that tire the reader.** The design doc had 489 lines, and the roadmap 273 lines of build logs: "Checked headless…", "Not seen…".
3. **Goals that are wishes.** "Launches quickly." "Answered with one search, most of the time." Neither can be checked.
4. **Principles that are features.** Four of ten principles restated goals. Others named screen parts.
5. **Agents that agree too fast.** Asked to discuss a design, the agent started writing files. The user had to stop it: "dont be eager to implement it first."

**The result:** docs that cost more attention than they save.

## The idea

**Each document answers exactly one question.** Then every fact has exactly one home: a reader always knows where to look, and a change is made in one place.

| Doc | The one question it answers |
|---|---|
| PROPOSAL (this file) | Why did we start this? |
| [PHILOSOPHY](PHILOSOPHY.md) | Why is it this way? |
| [GOALS](GOALS.md) | What do we measure? |
| [FEATURES](FEATURES.md) | What does it do, and what will it do? |
| [DESIGNS](DESIGNS.md) | How is it built, and why that way? |
| [ROADMAP](ROADMAP.md) | When, and how far along? |
| [README](README.md) | What is this, and how do I start? |

This repo's own docs use the same set.

## What we want

| Pain | What what-we-build does |
|---|---|
| Every fact in several places | One question per doc (above). A placement test gives each new fact its home. Other docs link to it. |
| Docs that tire the reader | Wording rules, a style per doc, and history kept to one dated clause per decision. |
| Goals that are wishes | Each goal needs a number. Without one, it stays open. |
| Principles that are features | Each principle picks a side a sensible team could reverse, and names one thing it refuses. |
| Agents that agree too fast | Discussion and brainstorming before decisions, a recommendation with a reason when a choice is ready, and no doc before its key points are agreed. |

Underneath all five: **the user decides.** The skill asks and recommends. It does not choose.

## How it works

The user types `/what-we-build` in an empty folder and says what they want to build. The agent talks it through with them. A doc often opens wide and ends with a choice:

```text
PROPOSAL.md answers: why did we start this?

Agent: Let's list what hurts first, as fast as it comes. I'll start:
       receipts lost in email, card lines with no receipt,
       an evening each month matching them by hand.
User:  Add one: finance asks for the same receipt twice.
Agent: Four pains. If you could fix only one, which would it be?
       A. Matching by hand: it costs an evening every month (recommended)
       B. Lost receipts
       C. Something else: ...
```

- **Talk, not a form:** discussion and brainstorming open each doc, and a recommended choice closes each point.
- **In order:** each doc builds on the ones before it, and is written only after its key points are agreed.
- **Strict where it counts:** a pain needs an example, a principle must pick a side and refuse one thing, a goal needs a number, a decision needs a reason and the option it beat.
- **Marked as it goes:** each doc stays `drafted` until the user approves it, so a session can stop and resume later.

The exact behavior is in [FEATURES.md](FEATURES.md) → F1–F2.

## What we don't want

| Not this | Why |
|---|---|
| A faster way to get confident text | Asking the agent directly already gives you pages of confident text about decisions nobody made. |
| A form to fill in | Templates and fixed questionnaires produce answers, not decisions. |
| Something that runs on its own | A session needs your full attention, so it starts when you type it. |

The full list of what is not planned, with reasons: [FEATURES.md → Not planned](FEATURES.md#not-planned).

## Who it is for

Developers who start a project with a coding agent and want the thinking written down before the code. The first user is the author.

## Approach

- **One Claude Code skill,** started only by hand with `/what-we-build`.
- **Two modes:** a new project, and resuming a session.
- **Reference files loaded when needed,** so the skill stays short: one per doc, plus the wording rules.
- **Distributed** as a public plugin, or as a folder linked into `~/.claude/skills`.

## Risks

| Risk | Mitigation |
|---|---|
| The user wants the docs, not the talk | The skill drafts quickly once a doc's key points are agreed. A recommendation comes with every choice, so a ready decision takes one answer. |
| Too many docs for a small project | Seven core docs. The rest only when needed. |
| The skill itself grows too long | `SKILL.md` has a line limit (GOALS.md G6). Detail lives in reference files. |
| The agent pads or splits text | Wording rules, and rules that name the session failure behind them. |

## How we know it works

[GOALS.md](GOALS.md) holds the checks: the core docs drafted and approved in one sitting, no fact with two homes, every goal with a number, every decision with a reason and a date.
