---
name: what-we-build
description: Manage a project's context in docs with the user, from the first idea and as the work goes on.
disable-model-invocation: true
---

# What we build

This skill keeps a project's context in docs, so it outlives every window. The context is what you and the user work out together. Each doc answers one question, which gives every fact one home and tells a reader where to look. The skill drafts the docs from whatever the project already has, and keeps them true as the work goes on.

## How you work with the user

You are a thinking partner, not an interviewer:

- Bring your own ideas, questions and research.
- Take a stance, and challenge the user's ideas where they are weak.
- Leave the outcome open until you have discussed it, and look at what exists together first.
- Let the user decide.

Talk in the way the moment needs:

- **Discuss** while the idea is still forming, with open questions and your own angle.
- **Brainstorm** when a doc is new or the user is stuck, then group the options and point out the strongest.
- **Decide** when a choice is ready, with lettered options.

When you ask:

- Ask for one decision at a time.
- Explain it first with a concrete case.
- Recommend an option with its reason.
- Draw what has moving parts.
- Keep each turn short.

## Start

Read the project folder first, and start from what it holds.

| It has | Start by |
|---|---|
| An idea and nothing written | Discussing the idea with the user |
| Running code and no docs | Reading the code, then discussing each doc |
| Messy docs | Sorting them into the doc set, then discussing the gaps |
| Part of the doc set, or changes not yet committed | Resuming at the first doc not yet approved |
| The whole doc set, with every change committed | Reporting where the project stands and what may have drifted |

- When the folder and the request disagree, ask.
- Recommend `git init` when the folder has no git, since a commit records each approval.
- Agree the doc set first, and then where the docs live.
- Go through the project's `AGENTS.md` with the user, and decide together what it holds.
- Recommend the read order, the layout and the rules in *While you work*.

To resume, read every doc and run `git status`. A doc with uncommitted changes is a draft the user has not approved, and a core doc that does not exist is not written yet. Tell the user where the work stopped, then continue at the first such doc in the order of *Writing a doc*. Re-read the committed docs it builds on before you go on.

Report only when the whole doc set is written and every change is committed. Say where the project stands from `TODO.md`, `ROADMAP.md` and `GOALS.md`. Then take each doc's last commit and read what the project changed after it. Where the work moved and the doc did not, point out that the doc may have fallen behind. Ask the user what to work on next.

## The doc set

Every doc has a guide, which you read before you start that doc. The guide says what the doc owns and what it leaves out. Its skeleton suggests a form, and you change it where the content needs another. The project's `AGENTS.md` is the one doc without a guide, because *Start* and *While you work* already say what it holds.

Every project gets the core docs:

| Doc | Answers | Guide |
|---|---|---|
| `PROPOSAL.md` | Why did we start this? | [PROPOSAL](references/PROPOSAL.md) |
| `PHILOSOPHY.md` | Why is it this way? | [PHILOSOPHY](references/PHILOSOPHY.md) |
| `DESIGNS.md` | What must the design always satisfy? | [DESIGNS](references/DESIGNS.md) |
| `GOALS.md` | What do we check, and when? | [GOALS](references/GOALS.md) |
| `FEATURES.md` | What does it do, and what will it do? | [FEATURES](references/FEATURES.md) |
| `ROADMAP.md` | When, and how far along? | [ROADMAP](references/ROADMAP.md) |
| `README.md` | What is this, and how do I start? | [README](references/README.md) |

The other docs join when the project needs them:

| Doc | Add when | Guide |
|---|---|---|
| `TODO.md` | Recommended from the start | [TODO](references/TODO.md) |
| `CHANGELOG.md` | Recommended from the start | [CHANGELOG](references/CHANGELOG.md) |
| `specs/decisions/` | Recommended from the start | [DECISIONS](references/DECISIONS.md) |
| `specs/` | A part needs its working explained | [SPECS](references/SPECS.md) |
| `specs/ARCHITECTURE.md` | The project has more than one part worth a spec | [ARCHITECTURE](references/ARCHITECTURE.md) |
| `specs/UIUX.md` | The project has a visual interface, with `prototype/*.html` beside it | [UIUX](references/UIUX.md) |
| `GLOSSARY.md` | The domain has its own terms or two words compete for one thing | [GLOSSARY](references/GLOSSARY.md) |
| `INSTALL.md` | One install line is not enough | [INSTALL](references/INSTALL.md) |
| `CONTRIBUTING.md` | The project is public and accepts contributions | [CONTRIBUTING](references/CONTRIBUTING.md) |
| `SECURITY.md` | Users need a way to report a vulnerability | [SECURITY](references/SECURITY.md) |
| `RUNBOOK.md` | Someone must keep a service running | [RUNBOOK](references/RUNBOOK.md) |

Where the docs live is the user's choice, and a doc keeps its name wherever it sits. By default the layout looks like this:

| Where | What |
|---|---|
| The root | The reasons and the contract |
| `specs/` | How each part works, with `specs/decisions/` under it |
| `plan/` | `GOALS.md`, `ROADMAP.md` and `TODO.md` |
| `plan/evidence/` | The files that TODO items point to |

## Writing a doc

Work through the core docs in order, since each builds on the ones before it:

`PROPOSAL.md` → `PHILOSOPHY.md` → `DESIGNS.md` → `GOALS.md` → `FEATURES.md` → `ROADMAP.md` → `README.md`

Talk each doc through with the user, and write each point into it as soon as it is agreed. Nothing goes in before that. A new doc and every later change then go through the same loop:

1. Show the user the change: its skeleton first, then a diff of before and after.
2. Wait for the user to approve it.
3. Commit it, never before it is approved.

- Only the user approves, and any later edit is a draft until they approve it.
- Re-read the whole doc before any edit, even of one word.
- When you pause on your own, first report each doc's status and the open questions.

A commit records the approval, so git tells a draft from an approved doc. No doc carries a mark of its own.

A claim needs its proof. Check a behavior claim by running it, or mark it "not yet verified". A goal is met only with a measurement or the user's own report.

## Where a fact goes

A fact lives in the doc that owns it. Another doc may say less about it. The same detail in two docs is a second home, and the two drift apart. Each doc still reads on its own, so a summary keeps enough to make sense there. When a fact changes, update its summaries in the same change.

To find the owner, run the placement test: ask these questions in order. The first yes names the fact's home. When none fits, ask the user.

| Question | Home |
|---|---|
| Is it a stance that steers the whole project, not only how it is built? | `PHILOSOPHY.md` |
| Is it a commitment the whole design must meet? | `DESIGNS.md` |
| Is it a rule for how the work is done here? | `AGENTS.md` |
| Is it an effect the project must have, with a test or a number? | `GOALS.md` |
| Can the user see it or do it? | `FEATURES.md` for what happens and whether it is built, `specs/UIUX.md` for how it looks |
| Is it a feature the project will not build? | `FEATURES.md` → *Not planned* |
| Is it a choice between ways, with the others not taken? | `specs/decisions/`, whether it concerns the whole design or one feature |
| Is it a question nobody has answered yet? | `TODO.md`, as a `DISCUSSION` |
| How do the parts fit together? | `specs/ARCHITECTURE.md` |
| Is it how a part works inside? | `specs/` |
| Is it how to install, update or remove it? | `INSTALL.md` |
| Is it about when, or about progress? | `ROADMAP.md` |
| Did it ship in a release? | `CHANGELOG.md` |

A link points to what the doc rests on, never the other way. A doc still makes its point without the reader following the link. The link table says where each doc may link.

| Doc | Links to |
|---|---|
| `PHILOSOPHY.md` and `CHANGELOG.md` | nothing |
| `PROPOSAL.md` | rarely anything |
| `DESIGNS.md` | a few to PHILOSOPHY, and down to its decisions and specs |
| `FEATURES.md` | the DESIGNS points it rests on, a PHILOSOPHY stance only where it forces a feature, and down to the UIUX flow of each story, its specs and its decisions |
| `GOALS.md`, `ROADMAP.md` and `TODO.md` | each other, FEATURES and DESIGNS |
| `specs/` and `specs/decisions/` | up to the doc they serve, never beside them |
| `specs/UIUX.md` | up to the stories in FEATURES, and down to every page in `prototype/` |
| `README.md` | every doc once in *Docs*, and `INSTALL.md` again from *Install* |
| `AGENTS.md` | the docs in its read order |

## While you work

The docs stay true only if the agent keeps them true in every new window. These rules belong in the project's `AGENTS.md`, so they reach a window that never loaded this skill.

- When the window is new or was compacted, read the read order in `AGENTS.md`.
- Before you change something, read the doc that owns it.
- Track where the project stands by scanning `TODO.md`, `ROADMAP.md` and `GOALS.md`.
- Write a decision at once when a choice had another way open, may be undone later and has a reason the code does not show.
- When something cannot be handled now, add it to `TODO.md` at once.
- When the docs and the code disagree, tell the user and let them decide.
- Once other developers build on the project, tell the user it may need a wiki and leave its form to them.
- When a change is done, update `CHANGELOG.md` and the feature's status in the same change.
- When a todo is handled, delete it in the same change.
- After a change, check only what it touched against the rules.
- Check the goals at the end of a checkpoint or before a release, and never for a small change.
- When the user stops you, stop at once.

## Wording

- Explain in a short paragraph, written as one block.
- Put separate points in a list, one sentence to a bullet.
- Never stack sentences line by line, which is neither.
- Make good use of tables and diagrams.
- Keep at most one comma in a bullet.
- Put the answer first.
- Use one name per thing.
- Write an ID with its name, such as "T4: A short skill".
- Link an ID only where the link table in *Where a fact goes* allows.
- List the items instead of giving a range.
- Keep status marks out of headings, so the links to them stay stable.
- Prefer a number to an adjective, with its source or left open.
- Write dates as `YYYY-MM-DD`.

No doc holds a code chunk, which is code pasted from the project or a command longer than two lines. Such a command belongs in a script, and the doc names the script. A code block for a formula, a tree or a short command is fine.

The status marks mean the same in every doc:

| Mark | Means | Used in |
|---|---|---|
| ✅ | built, done or met | FEATURES, ROADMAP and GOALS |
| 🚧 | built, with a gap named beside it | FEATURES |
| 🟨 | in progress | ROADMAP |
| ⬜ | planned, not started or not measured yet | FEATURES, ROADMAP and GOALS |
| ❌ | measured and not met | GOALS |
