<!-- what-we-build: drafted 2026-10-12 -->

# what-we-build — Proposal

> Talk a project into being, one document at a time.

Proposed 2026-10-12. For what is built today, see [ROADMAP.md](ROADMAP.md).

## In short

Coding agents can write a project's documents in minutes. They write too much, in too many places, and they agree with everything. what-we-build is a skill that drafts a project's founding documents through a conversation: one question per document, one decision at a time, and one home for each fact.

## The shift

| Before agents | With agents |
|---|---|
| Docs are slow to write, so few exist | An agent writes ten docs in an afternoon |
| The author decides each line | The agent fills each gap with a guess |
| Docs drift slowly | Every session adds a little, in a new place |
| A reader opens one doc to find a fact | A reader opens all of them |

## Pain points

The numbers come from one real project, a macOS terminal built with coding agents over two weeks.

1. **Every fact in several places.** "What we will not build" was written in five docs: philosophy, goals, features, roadmap and the command reference.
2. **Docs that tire the reader.** The design doc had 489 lines, and the roadmap 273 lines of build logs: "Checked headless…", "Not seen…".
3. **Goals that are wishes.** "Launches quickly." "Answered with one search, most of the time." Neither can be checked.
4. **Principles that are features.** Four of ten principles restated goals. Others named screen parts.
5. **Agents that agree too fast.** Asked to discuss a design, the agent started writing files. The user had to stop it: "dont be eager to implement it first."

**The result:** docs that cost more attention than they save.

## What we want

| Pain | What what-we-build does |
|---|---|
| Every fact in several places | Each doc answers one question. A placement test gives each fact one home. Other docs link to it. |
| Docs that tire the reader | Wording rules, a voice per doc, and history kept to one dated clause per decision. |
| Goals that are wishes | Each goal needs a number. Without one, it stays open. |
| Principles that are features | Each principle must be able to reject a real feature. |
| Agents that agree too fast | One decision at a time, a recommendation with a reason, and no doc before its key points are agreed. |

Underneath all five: **the user decides.** The skill asks and recommends. It does not choose.

## What we don't want

| Not this | Why |
|---|---|
| A skill that starts on its own | A session takes an hour of the user's attention. It starts on purpose. |
| A questionnaire | Fixed questions produce filled templates, not decisions. |
| A template filler | A skeleton without a conversation is text nobody decided. |
| User manuals | Tutorials and API references answer other questions. They come later. |
| More docs than the project needs | Optional docs join only when they have a job. |

## Who it is for

Developers who start a project with a coding agent and want the thinking written down before the code. The first user is the author.

## Approach

- **One Claude Code skill,** started only by hand with `/what-we-build`.
- **Three modes:** a new project, resuming a session, revisiting docs that drifted.
- **Reference files loaded when needed,** so the skill stays short: one per doc, plus wording rules and the revisit procedure.
- **Two checks** in Python with no dependencies: broken links, and blank lines around blocks.
- **Distributed** as a public plugin, or as a folder linked into `~/.claude/skills`.

## Risks

| Risk | Mitigation |
|---|---|
| The user wants the docs, not the talk | The skill drafts quickly once a doc's key points are agreed. The talk is short questions with recommendations. |
| Too many docs for a small project | Seven core docs. The rest only when needed. |
| The skill itself grows too long | `SKILL.md` stays under 500 lines. Detail lives in reference files. |
| The agent pads or splits text | Wording rules and a list of mistakes seen in real sessions. |

## How we know it works

[GOALS.md](GOALS.md) holds the checks: the core docs drafted in one session, no fact with two homes, every goal with a number, every decision with a reason and a date.

## Documents

| Document | Answers |
|---|---|
| [PHILOSOPHY.md](PHILOSOPHY.md) | Why is it this way? |
| [GOALS.md](GOALS.md) | What do we measure? |
| [FEATURES.md](FEATURES.md) | What does it do, and what will it do? |
| [DESIGNS.md](DESIGNS.md) | How is it built, and why that way? |
| [ROADMAP.md](ROADMAP.md) | When? |
| [CHANGELOG.md](CHANGELOG.md) | What changed in each release? |
| [AGENTS.md](AGENTS.md) | How do coding agents work in this repo? |
