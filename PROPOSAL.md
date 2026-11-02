# what-we-build — Proposal

> Keep a project's context in docs.

Proposed 2026-10-12.

## In short

You build a project with a coding agent over many sessions. On day one you agree on what to build and why. Some weeks later the agent is writing code for a project you no longer recognize.

Nothing was built badly. The context was lost: what you decided and why.

what-we-build keeps that context in docs, made with you through discussion. Each doc answers one question, so every fact has one home. Nothing is written down before you agree.

## Why it should exist

Building is no longer the hard part. An agent implements almost anything it is told, and fast. What goes wrong is the context around the work.

### Pain points

The first five come from one real project built with coding agents over two weeks. The rest come from building this skill.

#### Every fact in several places

"What we will not build" was written in five docs:

- The philosophy.
- The goals.
- The features.
- The roadmap.
- The command reference.

A change to it had to be made five times, and it never was.

#### Docs that tire the reader

| Doc | Size | What filled it |
|---|---|---|
| Design | 489 lines | Every detail of every part |
| Roadmap | 273 lines | Build logs, such as "Checked headless…" |

#### Goals that are wishes

> Launches quickly.

> Answered with one search, most of the time.

Neither goal can be checked.

#### Principles that are features

Four of ten principles restated goals. Others named parts of the screen.

#### Agents that agree too fast

Asked to discuss a design, the agent started writing files. The user had to stop it:

> dont be eager to implement it first

#### Agents that do not record

A rule said to write a changelog entry with every change. The agent forgot it twice in one session. What an agent records has no fixed shape, so nobody can say where it went.

#### Docs patched until nobody can read them

A doc was edited in twenty small patches. It lost its shape, and no person could read it. The agent reading it got lost too.

#### Context lost to the window

Past about 600K tokens the agent grew confused. Then the window was compacted, and the session's decisions were gone. The next session did not know what the last one had been doing.

#### Docs not read

1. A requirement was agreed and written down.
2. The code came out a different shape.
3. Asked about it, the agent searched for a long time.
4. It found the doc and said the doc was right.

#### Work from git alone

A new session read the file tree and the log. They said what changed and not why. The session continued the last change with no way to know whether it was right.

**The result:** the work drifts away from what was agreed.

## Why now

Agents changed what is cheap and what gets lost.

| Before agents | With agents |
|---|---|
| Docs are slow to write, so few exist | An agent writes a whole doc set in one sitting |
| The author decides each line | The agent fills each gap with a guess |
| A project lives in a few heads | A project lives across many sessions that forget |
| Docs drift slowly | Every session adds a little in a new place |

## The idea

**Keep the project's context in docs, and give each fact one home.**

Each doc answers one question. A reader always knows where to look, and a change is made in one place. The agent writes the docs with the user and reads them before it works.

| Doc | The one question it answers |
|---|---|
| PROPOSAL (this file) | Why did we start this? |
| PHILOSOPHY | Why is it this way? |
| DESIGNS | What must the design always satisfy? |
| FEATURES | What does it do, and what will it do? |
| `specs/` | How does each part work? |
| `specs/decisions/` | Why did we choose this, and what did we not choose? |
| GOALS | What do we measure? |
| ROADMAP | When, and how far along? |
| TODO | What is open? |
| CHANGELOG | What changed? |
| README | What is this, and how do I start? |

This repo's own docs use the same set.

## What we want

- **One home for every fact:** each doc answers one question, and a placement test places each new fact.
- **Context that outlives the session:** what is decided goes into a doc at once.
- **Docs a person can read:** each doc follows its guide and is re-read in full before any edit.
- **An agent that reads before it works:** the project's `AGENTS.md` names the read order.
- **Goals that can be checked:** each goal needs a number or stays open.
- **The user decides:** nothing is committed before the user approves it.

## What we don't want

- **A faster way to get confident text:** asking the agent directly already gives that.
- **A form to fill in:** templates and fixed questionnaires produce answers, not decisions.
- **Something that runs on its own:** a session needs your full attention, so it starts when you type it.

## Who it is for

It is for developers who build a project with a coding agent over many sessions and want its context kept. The first user is the author.

## Risks

| Risk | What reduces it |
|---|---|
| The user wants the docs, not the talk | The skill drafts quickly once a doc's key points are agreed. Every choice comes with a recommendation. |
| Too many docs for a small project | Seven core docs. The rest only when needed. |
| The skill itself grows too long | `SKILL.md` has a line limit. Detail lives in the guides. |
| The docs fall behind the work | The agent updates the owning doc in the change that does the work. |
