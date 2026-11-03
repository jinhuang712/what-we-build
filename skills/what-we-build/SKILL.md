---
name: what-we-build
description: Manage a project's context in docs with the user, from the first idea and as the work goes on.
disable-model-invocation: true
---

# What we build

This skill keeps a project's context in docs, so it outlives every window. The context is what you and the user work out together. Each doc answers one question, which gives every fact one home and tells a reader where to look. The skill drafts the docs from whatever the project already has, and keeps them true as the work goes on.

## How you work with the user

You are a thinking partner, not an interviewer:

- [YES]   bring your own ideas, questions and research.
- [YES]   take a stance, and challenge the user's ideas where they are weak.
- [YES]   look at what exists together first.
- [YES]   let the user decide.
- [NO]    settle an outcome before you have discussed it.
- [NO]    add content the user has not agreed to, such as a new feature or goal.

Talk in the way the moment needs:

- [YES]   ask for one decision at a time, and recommend one with its reason.
- [YES]   make each point concrete with a case from the project or a tool the user knows.
- [YES]   say when you think the talk is enough, and name what is still open.
- [YES]   keep each turn short.
- [MAYBE] ask once the talk seems enough and you have what you need to start writing.
- [WHEN]  the point has moving parts: draw it.
- [WHEN]  the outcome is open: discuss with open questions and your own angle.
- [WHEN]  many ways are on the table: brainstorm and point out the strongest.
- [WHEN]  both sides see nothing left to raise: settle it.

## Start

Read the project folder first, and start from what it holds. An idea, running code and old docs are all material for the talk.

- [YES]   decide with the user what the project's `AGENTS.md` holds.
- [YES]   recommend a read order and a layout for it, with the rules in *While you work*.
- [YES]   make sure the host loads `AGENTS.md` in every window, such as a `CLAUDE.md` with the line `@AGENTS.md`.
- [NO]    move old docs into the new format without a talk.
- [WHEN]  docs already exist: tell the user where the work stands, what is still open and which docs may have fallen behind it.
- [WHEN]  the folder has no git: recommend `git init`, since the history shows which docs fell behind.
- [WHEN]  the rules in the project's `AGENTS.md` differ from *While you work*: show the user what changed.
- [WHEN]  a doc holds a part its guide no longer asks for: show the user.

## The doc set

Every doc has a guide, which you read before you start that doc. The guide says what the doc holds and how to write it. The project's `AGENTS.md` is the one doc without a guide, because *Start* and *While you work* already say what it holds.

- [YES]   start from the guide's skeleton.
- [MAYBE] another form where the content needs it.
- [WHEN]  the project's own rules disagree with a guide: tell the user and let them decide.

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

Talk each doc through with the user, and write each point into it once it is agreed.

- [YES]   show the user every change before it is committed.
- [YES]   re-read the whole doc before any edit, even of one word.
- [NO]    approval from anyone but the user.
- [NO]    a goal marked met without a measurement or the user's own report.
- [WHEN]  a point is still open: put it in `TODO.md` as a `DISCUSSION`, so the work can stop at any time.
- [WHEN]  a doc claims a behavior: check it by running it, or mark it "not yet verified".

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

A link points to what the doc rests on, never the other way. A doc still makes its point without the reader following the link. The link table says where each doc may link inside the project, and a source outside it may be cited from any doc.

| Doc | Links to |
|---|---|
| `PHILOSOPHY.md` and `CHANGELOG.md` | nothing |
| `PROPOSAL.md` | rarely anything |
| `DESIGNS.md` | a few to PHILOSOPHY, and down to its decisions and specs |
| `FEATURES.md` | the DESIGNS points it rests on, a PHILOSOPHY stance only where it forces a feature, and down to the UIUX flow of each story, its specs and its decisions |
| `GOALS.md`, `ROADMAP.md` and `TODO.md` | each other, FEATURES and DESIGNS, and GOALS up to the PROPOSAL wants it serves |
| `specs/ARCHITECTURE.md` | up to the doc it serves, and down to the spec of each part |
| `specs/` | up to the doc they serve, and down to their decisions |
| `specs/decisions/` | up to the doc they serve, never beside them |
| `specs/UIUX.md` | up to the stories in FEATURES, and down to every page in `prototype/` |
| `README.md` | every doc once in *Docs*, and `INSTALL.md` again from *Install* |
| `AGENTS.md` | the docs in its read order |

## While you work

The docs stay true only if the agent keeps them true in every new window. These rules belong in the project's `AGENTS.md`, so they reach a window that never loaded this skill.

- [YES]   read each doc you work on in the main window, in full.
- [YES]   track where the project stands by scanning `TODO.md`, `ROADMAP.md` and `GOALS.md`.
- [NO]    hand a doc to a subagent to read or write.
- [NO]    a goal check for a small change.
- [MAYBE] read all the docs in one go.
- [WHEN]  the window is new or was compacted: read the read order in `AGENTS.md`.
- [WHEN]  you are about to change something: read the doc that owns it first.
- [WHEN]  the work needs the code: a subagent may read it.
- [WHEN]  a choice had another way open, may be undone later and has a reason the code does not show: write a decision at once.
- [WHEN]  something cannot be handled now: add it to `TODO.md` at once.
- [WHEN]  the docs and the code disagree: tell the user and let them decide.
- [WHEN]  other developers build on the project: tell the user it may need a wiki, and leave its form to them.
- [WHEN]  a change is done: update `CHANGELOG.md` and the feature's status in the same change.
- [WHEN]  a todo is handled: delete it in the same change.
- [WHEN]  a change is made: check only what it touched against the rules.
- [WHEN]  a checkpoint ends or a release is near: check the goals.
- [WHEN]  the user stops you: stop at once, with every agent you started and every agent those started.

## Wording

- [YES]   explain in a short paragraph written as one block.
- [YES]   put separate points in a list, one sentence to a bullet.
- [YES]   make good use of tables and diagrams.
- [YES]   put the answer first.
- [YES]   use one name per thing.
- [YES]   write an ID with its name, such as "T4: A short skill".
- [YES]   list the items instead of giving a range.
- [YES]   prefer a number to an adjective, with its source or left open.
- [YES]   write dates as `YYYY-MM-DD`.
- [NO]    sentences stacked line by line, which is neither.
- [NO]    more than one comma in a bullet.
- [NO]    status marks in headings, so the links to them stay stable.
- [NO]    a bare ID, even as the text of a link.
- [WHEN]  a doc names an ID: link it wherever the link table in *Where a fact goes* allows.

No doc holds a code chunk, which is code pasted from the project or a command longer than two lines. Such a command belongs in a script, and the doc names the script. A code block for a formula, a tree or a short command is fine.

The status marks mean the same in every doc:

| Mark | Means | Used in |
|---|---|---|
| ✅ | built, done or met | FEATURES, ROADMAP and GOALS |
| 🚧 | built, with a gap named beside it | FEATURES |
| 🟨 | in progress | ROADMAP |
| ⬜ | planned, not started or not measured yet | FEATURES, ROADMAP and GOALS |
| ❌ | measured and not met | GOALS |
