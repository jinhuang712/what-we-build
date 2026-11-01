---
name: what-we-build
description: Manage a project's context in docs with the user, from the first idea and as the work goes on.
disable-model-invocation: true
---

# What we build

This skill manages a project's context: what you and the user work out together, kept in docs so it outlives every session. It drafts the docs from an idea, from running code or from messy docs, and keeps them true while the work goes on. Each doc answers one question, so every fact has one home and a reader knows where to look.

- It is a discussion, not an interview.
- Bring your own ideas.
- Bring questions and research.
- Take a stance and say why.
- Challenge the user's ideas.
- The user decides.
- Write a doc only after its key points are agreed.

## Working protocol

### Writing a doc

Each doc goes through the same loop:

1. Discuss until its key points are agreed.
2. Draft it with a `drafted` mark.
3. Show the user the changes as before and after.
4. Wait for the user to approve, then mark it `approved`.
5. Commit it, never before it is approved.
6. Move to the next doc.

- Only the user approves.
- Any later edit sets the mark back to `drafted`.
- Leave an unknown number open.
- At the end, report each doc's status and the open questions.
- Even when only one word or row should be edited, re-read the whole doc before editing anything.

The mark is the first line of a doc:

```markdown
<!-- what-we-build: drafted 2026-10-12 -->
<!-- what-we-build: approved 2026-10-12 -->
```

- A doc that grows one entry at a time carries no mark.

### While you work

- When a session starts or the window was compacted, read the read order in `AGENTS.md`.
- Before you change something, read the doc that owns it.
- When a choice between ways is made, write a decision at once.
- When something cannot be handled now, add it to `TODO.md` at once.
- When the docs and the code disagree, tell the user and let them decide.
- When a change is done, update `CHANGELOG.md` and the feature's status in the same change.
- When a todo is handled, delete it in the same change.
- When the user stops you, stop.

## How to talk

| Way | When it fits | What you do |
|---|---|---|
| Discuss | The idea is still forming, or the user is thinking out loud | Ask open questions, offer your own angle, and challenge weak spots. No options yet. |
| Brainstorm | Early in a doc, or when the user is stuck | List many options quickly, without judging them. Then group them and point out the strongest. |
| Decide | A choice is ready | Give lettered options, mark one as recommended, and give the reason in a clause. |

- Take the cue from the user.
- Ask one decision per question when deciding.
- Recommend one option with the reason.
- Explain before you ask.
- Show one concrete case.
- Offer your own list beside the user's.
- Say what you would add and what you doubt.
- Draw what has moving parts.
- Keep each turn short.

## Choose the start

Read the project folder first.

| It has | Start by |
|---|---|
| An idea and nothing written | Discussing the idea with the user |
| Running code and no docs | Reading the code, then discussing each doc |
| Messy docs | Sorting them into the doc set, then discussing the gaps |
| Docs with marks and not all approved | Resuming |

- Ask when the folder and the request disagree.
- Ask the user what to do with what no doc owns.
- Agree the doc set first.
- Then agree where the docs live.
- Write the read order into the project's `AGENTS.md`.
- Work through the docs in this order:

`PROPOSAL.md` → `PHILOSOPHY.md` → `DESIGNS.md` → `GOALS.md` → `FEATURES.md` → `ROADMAP.md` → `README.md`

- Each doc builds on the ones before it.
- Follow the wording rules when you write.

### Resuming

- Read every doc and its mark.
- Summarize the approved docs, the drafted docs and the doc to continue.
- Continue at the first doc in the order that is not approved.
- Re-read the approved docs before you ask anything.

## The doc set

| Doc | Answers |
|---|---|
| `PROPOSAL.md` | Why did we start this? |
| `PHILOSOPHY.md` | Why is it this way? |
| `DESIGNS.md` | What must the design always satisfy? |
| `GOALS.md` | What do we measure? |
| `FEATURES.md` | What does it do, and what will it do? |
| `ROADMAP.md` | When, and how far along? |
| `README.md` | What is this, and how do I start? |

- Each doc has a guide.
- The guide says what the doc owns and leaves out.
- Read a doc's guide before you start that doc.
- Add an optional doc only when the project needs it.

Core docs:

- [PROPOSAL.md](references/PROPOSAL.md)
- [PHILOSOPHY.md](references/PHILOSOPHY.md)
- [DESIGNS.md](references/DESIGNS.md)
- [GOALS.md](references/GOALS.md)
- [FEATURES.md](references/FEATURES.md)
- [ROADMAP.md](references/ROADMAP.md)
- [README.md](references/README.md)

Beside the core, the first three are recommended for every project:

- [TODO.md](references/TODO.md)
- [CHANGELOG.md](references/CHANGELOG.md)
- [specs/decisions/](references/DECISIONS.md): one file per fork the project took
- [specs/](references/SPECS.md): how each part works, and `specs/UIUX.md` with `prototype/*.html` for a visual interface
- [specs/ARCHITECTURE.md](references/ARCHITECTURE.md): the map of the parts and how they connect
- [GLOSSARY.md](references/GLOSSARY.md)
- [CONTRIBUTING.md](references/CONTRIBUTING.md)
- [SECURITY.md](references/SECURITY.md)
- [RUNBOOK.md](references/RUNBOOK.md)

### The placement test

Ask the questions in order. The first yes names the fact's home.

| Question | Home |
|---|---|
| Is it a stance that steers the whole project, not only how it is built? | `PHILOSOPHY.md` |
| Can it be checked with a number? | `GOALS.md` |
| Can the user see it or do it? | `FEATURES.md` for what happens and whether it is built, `specs/UIUX.md` for how it looks |
| Is it a feature the project will not build? | `FEATURES.md` → *Not planned* |
| Is it a choice between ways, with the others not taken? | `specs/decisions/`, whether it concerns the whole design or one feature |
| Is it a question nobody has answered yet? | `TODO.md`, as a `DISCUSSION` |
| Is it a commitment the whole design must meet? | `DESIGNS.md` |
| How do the parts fit together? | `specs/ARCHITECTURE.md` |
| Is it how a part works inside? | `specs/` |
| Is it about when, or about progress? | `ROADMAP.md` |
| Did it ship in a release? | `CHANGELOG.md` |

## Rules

- A fact lives in the doc that owns it.
- Another doc may summarize it.
- The same detail in two docs is a second home.
- Each doc reads on its own.
- Link only for depth.
- When a fact changes, update its summaries in the same change.
- Why something will not be built goes in `FEATURES.md` → *Not planned*.
- Why something is built a certain way goes in `specs/decisions/`.
- Check a behavior claim by running it, or mark it "not yet verified".
- A goal is met only with a measurement or the user's own report.
- Never put a code chunk in a doc.
- Where the docs live is the user's choice.
- The default keeps the reasons and the contract at the root.
- `specs/` holds how each part works, with `specs/decisions/` under it.
- `plan/` holds `GOALS.md`, `ROADMAP.md`, `TODO.md` and `plan/evidence/`.
- A doc keeps its name wherever it sits.
- Record the layout in the project's `AGENTS.md`.

## Wording

- Turn a paragraph that could be bullets into bullets.
- Keep one sentence on a line.
- Keep at most one comma on a line.
- Explanatory prose stays prose, as in `PHILOSOPHY.md`.
- Put the answer first.
- Use one name per thing.
- Prefer a number to an adjective.
- Write dates as `YYYY-MM-DD`.
- Give every number its source, or leave it open.
- Use tables for facts that share a shape.

| Mark | Means | Used in |
|---|---|---|
| ✅ | built, done, or met | FEATURES, ROADMAP, GOALS |
| 🚧 | built, with a gap named beside it | FEATURES |
| 🟨 | in progress | ROADMAP |
| ⬜ | planned, not started, or not yet measured | FEATURES, ROADMAP, GOALS |
| ❌ | measured and not met | GOALS |
