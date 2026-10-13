---
name: what-we-build
description: Draft a new project's founding documents by talking each one through with the user, in discussion, brainstorming and clear decisions. Proposal, philosophy, goals, features, designs, roadmap and README, where each document answers one question, so every fact has one home. Also resumes an unfinished session.
disable-model-invocation: true
---

# What we build

Use this skill to define a project in writing, together with the user. The user brings the idea. You talk it through with them, discussing, brainstorming and deciding, and turn what you agree into documents. Each document answers one question, so each fact has one home and a reader always knows where to look.

The conversation is the method. A document records decisions. It cannot make them, and text written before the thinking is done looks finished when it is not. So a document is written only after its key points are agreed. The user decides. You recommend, push back once with a reason, and then follow the user's call.

## The doc set

Seven documents form the core of a new project. Each one answers a single question, and together they cover why the project exists, what it must achieve, what it does, how it is built and when it ships.

| Doc | Answers | Owns | Leaves out |
|---|---|---|---|
| `PROPOSAL.md` | Why did we start this? | the shift, pain points, the idea, what we want, what we don't want, approach, risks | exact behavior, numbers to check, progress |
| `PHILOSOPHY.md` | Why is it this way? | the belief behind the project, a few principles that each pick a side and refuse one thing, a tie-break | any feature the product has, setting or screen |
| `GOALS.md` | What do we measure? | checks, each with the want it serves, a number, a method and a status | anything vague, non-goals |
| `FEATURES.md` | What does it do, and what will it do? | behavior from the user's side, each feature's status (built, built with a gap, planned), *Later*, *Not planned* | type names, code paths, design reasons, progress |
| `DESIGNS.md` | How is it built, and why that way? | design principles with their costs and checks, decisions with the option each beat and a dated reason, open questions | user-visible behavior (link the feature), a map of the code |
| `ROADMAP.md` | When, and how far along? | milestones, tasks, progress, exit criteria that point to goals | behavior, the *Later* list |
| `README.md` | What is this, and how do I start? | a short description, what it does, install, first use, known limits, links | detail another doc owns |

Add an optional doc only when the project needs it. Give every doc a job, because only a doc with a job gets kept true.

Each kind of doc has its own guide. Read the guide for a doc before you start that doc, and only that guide. A guide holds everything the session needs about its doc.

Core docs:

- [PROPOSAL.md](references/docs/PROPOSAL.md)
- [PHILOSOPHY.md](references/docs/PHILOSOPHY.md)
- [GOALS.md](references/docs/GOALS.md)
- [FEATURES.md](references/docs/FEATURES.md)
- [DESIGNS.md](references/docs/DESIGNS.md)
- [ROADMAP.md](references/docs/ROADMAP.md)
- [README.md](references/docs/README.md)

Optional docs:

- [UIUX.md](references/docs/UIUX.md)
- [CLI.md](references/docs/CLI.md)
- [GLOSSARY.md](references/docs/GLOSSARY.md)
- [AGENTS.md](references/docs/AGENTS.md)
- [CHANGELOG.md](references/docs/CHANGELOG.md)
- [TODO.md](references/docs/TODO.md)
- [CONTRIBUTING.md](references/docs/CONTRIBUTING.md)
- [SECURITY.md](references/docs/SECURITY.md)
- [RUNBOOK.md](references/docs/RUNBOOK.md)
- [decision records](references/docs/decision-records.md)

## Rules between docs

These rules keep a doc set easy to trust: one place to look for each fact, and each doc readable on its own.

- **One home per fact.** A fact lives in the doc that owns it. When a fact has two homes, one of them goes stale, and the reader cannot tell which.
- **Each doc reads on its own.** Summarize what your reader needs to follow, and link only for depth. A reader who must jump between files to understand one point has been handed the work of assembling the doc.
- **A summary is shorter than its owner.** Any doc may summarize what its reader needs, and the README and the proposal summarize the most. A summary may repeat the owner's records, such as the list of docs in a README. The same detail written out in two docs is a second home, not a summary.
- **The owner changes first.** When a fact changes, update its summaries in the same change, so they never disagree. The same holds for the skill's rules: when a rule changes, check the docs written under the old one. Version 0.2.0 changed five rules, and five docs kept the old ones until the next audit.
- **Place each fact with the placement test** below, so two writers put the same fact in the same doc.
- **Reasons have homes.** Why something will not be built goes in `FEATURES.md` → *Not planned*, because that is where someone looks before proposing it. Why something is built a certain way goes in `DESIGNS.md`, beside the design. A design decision that only carries out a product decision links to that reason instead of restating it.
- **Claims are checked.** A statement about behavior, such as an install command or a command name, is checked by running it, or marked "not yet verified". A goal or criterion is met only with a measurement or the user's own report, made by someone who did not write the change. A claim nobody checked is a guess that looks like a fact: one rewrite marked two goals met, and an independent count failed both.
- **The code is a home too.** A doc repeats the code, the config or a command's output only when looking it up is expensive. It keeps what looking cannot find: the reason, the convention, the trap. A restated fact goes stale the day the code changes.
- **History stays short.** A decision keeps one clause: what, why, and the date (`Decided 2026-10-12: ...`). The story of how it was reached lives in git. A rewrite that removed every date left rules nobody could explain.
- **Headings are addresses.** Code comments and other docs cite headings (`DESIGNS.md → Decisions`). Keep them stable. When one must change, search the code and the docs for references first, and fix every one in the same change. Renamed headings once broke the comments that pointed to them.
- **One language per doc set,** so a reader never switches languages mid-doc.

### The placement test

Ask the questions in order. The first yes names the fact's home.

| Question | Home |
|---|---|
| Is it a reason that applies to many things? | `PHILOSOPHY.md` |
| Can it be checked with a number? | `GOALS.md` |
| Can the user see it or do it? | `FEATURES.md` for what happens and whether it is built, `UIUX.md` for how it looks, `CLI.md` for a command |
| Is it a feature the project will not build? | `FEATURES.md` → *Not planned* |
| Is it about code, files, processes or a design decision? | `DESIGNS.md` |
| Is it about when, or about progress? | `ROADMAP.md` |
| Did it ship in a release? | `CHANGELOG.md` |

## How each doc is written

Every section of every doc has up to three layers, in this order:

| Layer | Gives the reader |
|---|---|
| Description | what this part is and why it matters, in a short paragraph |
| Guidelines | how to do it well, each with its reason |
| Specifics | tables, skeletons, commands, examples |

A section with only specifics is a list of rules nobody can apply: a rewrite that cut every repeat left docs nobody could learn from. A section with only description gives the reader nothing to act on.

Write in your default voice. Each doc has its own style, meaning its form, given in its guide. For example, `GOALS.md` is a short intro and one table of checks, and `PHILOSOPHY.md` is one screen: a short preamble, one line per principle, and a tie-break. The full wording rules are in [references/wording.md](references/wording.md).

In every doc, pick the format by the shape of the data, even when the same records appear in another doc: a table for records, a list for parallel items, sentences for reasoning. Turning a table into inline links to avoid a repeat made a README harder to read. Judge a doc by how fast a reader finds a fact, not by its line count. Sessions met line limits by deleting blank lines, and doubled a doc with nested lists.

## Choose the mode

Read the project folder first. Then pick one:

| Mode | When | Go to |
|---|---|---|
| New | no founding docs exist, docs exist without marks, or the user starts a new project | [New project](#new-project-talk-it-through) |
| Resume | the docs carry marks, and not every doc is approved | [Resume](#resume) |

When the user passed an argument (`new` or `resume`), use it. When the folder and the request disagree, ask.

## New project: talk it through

A session turns an idea into the founding docs. It works because the user makes each decision while it is still cheap to change, before any text exists that looks finished.

### 1. Frame it

The first minutes decide what the session is about. Ask for the idea in one or two sentences, and who it is for. Look at the folder (existing code, a README, notes) and say what you found in one line, so the user knows what you will build on. When the folder holds docs under other names, map them to this set: a PRD to `FEATURES.md`, a vision doc to `PROPOSAL.md` and `PHILOSOPHY.md`, an ARCHITECTURE.md or design doc to `DESIGNS.md`, and an ADR to a decision record.

### 2. Agree on the doc set

Recommend the core seven plus the optional docs that fit, each with one clause of reason. Each optional doc's guide says when the project needs it. The user confirms or changes the list.

### 3. Work through the docs, in order

`PROPOSAL.md` → `PHILOSOPHY.md` → `GOALS.md` → `FEATURES.md` → `DESIGNS.md` → `ROADMAP.md` → `README.md`.

The order matters, because each doc builds on the ones before it. Each doc's guide says what it takes from the docs before it, and where an optional doc fits in the order.

For each doc:

1. **Open it.** Name the doc and the one question it answers, so the user knows what kind of decision comes next.
2. **Carry forward.** List what earlier docs already settled that this doc builds on. The user answered those once, and asking again wastes their attention.
3. **Explore the key points** listed in the doc's guide, in the way of talking that fits where the user is: discuss, brainstorm or decide (see [How to talk](#how-to-talk)). Open the doc wide, then narrow it down, and close each point with a clear choice.
4. **Push back on what does not fit.** Each doc's guide lists the mistakes it invites, such as an adjective where `GOALS.md` needs a number. Say why once. When the user rejects it, drop it: the user decides.
5. **Draft.** Start from the guide's skeleton and style, and follow [references/wording.md](references/wording.md). Keep every skeleton heading, and write "None yet" under one that has nothing to hold, so a reader sees the gap. Write the file with a `drafted` mark on its first line. Show the path and the key lines, not the whole file, unless it is short.
6. **Approve.** Ask for changes or approval. On approval, change the mark to `approved` and move on.

The mark is an HTML comment, invisible when rendered. It is the only state the skill keeps, so a session can stop, and resume after Claude Code restarts:

```markdown
<!-- what-we-build: drafted 2026-10-12 -->
<!-- what-we-build: approved 2026-10-12 -->
```

Only the user approves: write `approved` after the user says so. Any later edit sets the mark back to `drafted`, with the date of the edit, because the user has not read the new text.

The core docs carry a mark, and so does an optional doc that a session drafts as a whole, such as `UIUX.md`. A doc that grows one entry at a time, such as `CHANGELOG.md` or `TODO.md`, carries none.

### 4. Close the session

Report each doc with its status (approved, drafted, skipped) and the open questions the user still owns. Leave an unknown number open. A guessed number looks like a decision the user made.

### How to talk

Writing the docs is a conversation, not a form: a session run as a questionnaire felt like filling in one. A point that is still forming needs room. A point that is ready needs a clear choice. Read where the user is, and talk in the way that fits:

| Way | When it fits | What you do |
|---|---|---|
| Discuss | The idea is still forming, or the user is thinking out loud | Ask open questions, reflect back what you heard, offer another angle, test the weak spots, and build on the user's ideas. No options yet. |
| Brainstorm | Early in a doc, or when the user is stuck | List many options quickly, together, without judging them. Then group them and point out the strongest. |
| Decide | A choice is ready | Give lettered options, mark one as recommended, and give the reason in a clause. |

Each doc usually moves through all three: open up, narrow down, decide, then write. Take the cue from the user. A long, exploratory message or "not sure" asks for discussion. "Let's brainstorm" or a stalled answer asks for a brainstorm. A clear fork asks for a decision. Offer a switch when it would help: "Want to brainstorm this one first?"

### Conversation rules

- **Ask for one decision per question when deciding.** Batch up to four independent questions in one message, numbered, each with lettered options. More than four, and the user starts skimming.
- **Recommend, with the reason in one clause.** The user decides.
- **Agree first, then write, one doc at a time.** A doc is written only after its key points are agreed. Drafting three docs before the first was agreed wasted the user's time.
- **Ask for facts, numbers and dates.** When the user does not know one yet, mark it open.
- **Keep each turn short.** The docs hold the detail. The chat holds the decisions.
- **When the user stops you, stop.** Wait for an explicit go before you write again.

## Resume

Read every doc in the set and its mark. Summarize in a few lines: approved docs, drafted docs, the doc to continue. Continue at the first doc in the order above that is not approved. Re-read the approved docs before you ask anything, so you carry their answers forward.
