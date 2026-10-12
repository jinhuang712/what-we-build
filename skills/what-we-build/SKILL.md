---
name: what-we-build
description: Draft a new project's founding documents by talking each one through with the user, one decision at a time. Proposal, philosophy, goals, features, designs, roadmap and README, where each document answers one question, so every fact has one home. Also resumes an unfinished session, and revisits a doc set that has drifted.
disable-model-invocation: true
---

# What we build

Use this skill to define a project in writing, together with the user. The user brings the idea. You ask the questions that turn it into documents, one decision at a time. Each document answers one question, so each fact has one home and no document repeats another.

The conversation is the method. A document is written only after its key points are agreed. The user decides. You recommend, push back once with a reason, and then follow the user's call.

## The doc set

| Doc | Answers | Owns | Leaves out |
|---|---|---|---|
| `PROPOSAL.md` | Why did we start this? | the shift, pain points, what we want, what we don't want, approach, risks | exact behavior, numbers, status |
| `PHILOSOPHY.md` | Why is it this way? | what the core value means, a few principles, design words, the test for every change | any feature, setting or screen |
| `GOALS.md` | What do we measure? | checks, each with a number and a status | anything vague, non-goals |
| `FEATURES.md` | What does it do, and what will it do? | behavior from the user's side, status, *Later*, *Not planned* | type names, code paths, design reasons |
| `DESIGNS.md` | How is it built, and why that way? | design principles, structure, data, formats, decisions with dated reasons | user-visible behavior (link the feature) |
| `ROADMAP.md` | When? | milestones, tasks, exit criteria that point to goals | behavior, the *Later* list |
| `README.md` | What is this, and how do I start? | one paragraph, install, first use, known limits, links | anything another doc owns |

These seven are the core set for a new project. Add an optional doc only when the project needs it: `UIUX.md`, `CLI.md`, `GLOSSARY.md`, `AGENTS.md`, `CHANGELOG.md`, `TODO.md`, `CONTRIBUTING.md`, `SECURITY.md`, `RUNBOOK.md` or decision records.

Read [references/docs.md](references/docs.md) before you start a document. For each doc it gives the questions to ask, the skeleton, the voice and the signs that the doc is done. It also maps other common names (PRD, ARCHITECTURE.md, ADR, vision doc) to this set.

## Rules between docs

- **One home per fact.** A fact lives in the doc that owns it. Other docs link to it.
- **Summaries in two places only.** `PROPOSAL.md` and `README.md` may summarize other docs, at pitch level, with a link to the owner.
- **Place a fact by asking, in order:**
  1. Is it a reason that applies to many things? `PHILOSOPHY.md`.
  2. Can it be checked with a number? `GOALS.md`.
  3. Can the user see it or do it? `FEATURES.md` for what happens, `UIUX.md` for how it looks, `CLI.md` for a command.
  4. Is it about code, files, processes or a decision? `DESIGNS.md`.
  5. Is it about when, or about status? `ROADMAP.md`.
  6. Did it ship in a release? `CHANGELOG.md`.
- **History stays short.** A decision keeps one clause: what, why, and the date (`decided 2026-10-12: ...`). No logs of what was checked, no stories.
- **Headings are addresses.** Code comments and other docs cite headings (`DESIGNS.md → Search`). Keep them stable. When one must change, fix every reference.
- **One language per doc set.** Do not mix languages inside the docs.

## Choose the mode

Read the project folder first. Then pick one:

| Mode | When | Go to |
|---|---|---|
| New | no founding docs exist, or the user starts a new project | [New project](#new-project-talk-it-through) |
| Resume | docs carry `what-we-build` marks and some are not approved | [Resume](#resume) |
| Revisit | docs exist without marks, or the user says they drifted, overlap or are hard to read | [Revisit](#revisit) |

When the user passed an argument (`new`, `resume`, `revisit`), use it. When the folder and the request disagree, ask.

## New project: talk it through

### 1. Frame it

Ask for the idea in one or two sentences, and who it is for. Look at the folder: existing code, a README, notes. Say what you found in one line.

### 2. Agree on the doc set

Recommend the core seven plus the optional docs that fit. For example, `CLI.md` when there is a command-line tool, `UIUX.md` when there is a visual interface, `GLOSSARY.md` when the domain has its own terms. The user confirms or changes the list.

### 3. Work through the docs, in order

`PROPOSAL.md` → `PHILOSOPHY.md` → `GOALS.md` → `FEATURES.md` → `DESIGNS.md` → `ROADMAP.md` → `README.md`. Put an optional doc where it fits: `UIUX.md` and `CLI.md` after `FEATURES.md`, `GLOSSARY.md` from the first doc on (it grows as terms appear), `AGENTS.md`, `CONTRIBUTING.md` and `SECURITY.md` last.

For each doc:

1. **Open it.** Name the doc and the one question it answers.
2. **Carry forward.** List what earlier docs already settled that this doc builds on. Do not ask again what the user already answered.
3. **Ask the key questions** from [references/docs.md](references/docs.md), one decision at a time. Give lettered options and mark one as recommended, with the reason in a clause.
4. **Push back on what does not fit.** An adjective where `GOALS.md` needs a number. A feature inside `PHILOSOPHY.md`. A decision in `DESIGNS.md` without a reason. A pain point with no example. Say why once. When the user rejects it, drop it.
5. **Draft.** Write the file with a `drafted` mark on its first line. Show the path and the key lines, not the whole file, unless it is short.
6. **Approve.** Ask for changes or approval. On approval, change the mark to `approved` and move on.

The mark is an HTML comment, invisible when rendered. It is the only state the skill keeps:

```markdown
<!-- what-we-build: drafted 2026-10-12 -->
<!-- what-we-build: approved 2026-10-12 -->
```

Only the user approves. Never write `approved` on a doc the user has not read.

### 4. Close the session

Run the checks in [Checks](#checks). Then report each doc with its status (approved, drafted, skipped) and the open questions the user still owns. Unknown numbers stay open. Never invent one.

### Conversation rules

- One decision per question. Batch up to four independent questions in one message, numbered, each with lettered options.
- Recommend, and say why in one clause. The user decides.
- Do not write a doc before its key points are agreed.
- Do not invent facts, numbers or dates. Ask, or mark the item as open.
- Keep each turn short. The docs hold the detail, the chat holds the decisions.
- When the user stops you, stop. Wait for an explicit go before writing again.

## Resume

Read every doc in the set and its mark. Summarize in a few lines: approved docs, drafted docs, the doc to continue. Continue at the first doc in the order above that is not approved. Re-read the approved docs before you ask anything, so you carry their answers forward.

## Revisit

Use this mode when the docs exist but overlap, sprawl or drifted from the code. The short version:

1. **Audit.** List every doc with its size and last change. Find facts stated in more than one doc, facts in the wrong doc, and stale claims. Show the overlaps as a table.
2. **Agree on roles.** Show each doc's question and boundaries, as in [The doc set](#the-doc-set). The user confirms or changes them.
3. **Rewrite**, one doc at a time or in parallel with subagents. Each subagent gets a written brief with the roles, the wording rules and the mistakes below.
4. **Verify.** Compare against the old version (`git show HEAD:<file>`) for lost facts. Run the checks. Check every claim of "met" or "done" against evidence.
5. **Review.** The user reads the result before anything is committed.

[references/revisit.md](references/revisit.md) has the full procedure and a brief template for subagents.

## Wording

Write plain, precise English. The full rules are in [references/wording.md](references/wording.md). The ones that matter most:

- One name per thing, and one thing per name. Use the project's own names.
- Short sentences, one point each. Conditions first. Active voice.
- Pick the format by the shape of the data: a table for records, a code block for commands, a numbered list for steps, sentences for reasoning.
- Numbers instead of adjectives, wherever a number exists.
- No filler, no emphasis words, no hedging spread through the text.

Each doc also has its own voice, given in [references/docs.md](references/docs.md). `PHILOSOPHY.md` may reflect. `GOALS.md` stays cold.

## Checks

Run both scripts from this skill's folder on the project's docs:

```sh
python3 scripts/check_links.py <project>/*.md
python3 scripts/blank_lines.py <project>/*.md
```

- `check_links.py` reports relative links and `#anchors` that do not resolve.
- `blank_lines.py` puts one blank line around headings, tables, lists and code fences. It changes only blank lines, and it fails when any other line would change.

## Mistakes to avoid

These come from real sessions.

- **Line limits get gamed.** Asked for fewer lines, writers delete blank lines or squeeze paragraphs. Asked for short sentences, they split them into nested lists that double the length. Judge quality, not counts, and never nest lists.
- **No history loses the reasons.** Removing every date and decision story leaves rules nobody can explain. Keep one dated clause per decision.
- **"Met" without evidence.** A goal or exit criterion is met only when a measurement or the user's own report says so. Otherwise it is open.
- **Principles that are features.** "Sessions come first" or "no badges" is a feature or a screen rule. A principle states a value that can reject a feature.
- **Goals that are wishes.** "Fast", "easy" and "usually" are not goals. Ask for the number, or leave the goal open.
- **Renamed headings break links.** Search the code and the docs for references before a heading changes.
- **Eager drafting.** Writing three docs before the first is agreed wastes the user's time. One doc, agreed, then the next.
