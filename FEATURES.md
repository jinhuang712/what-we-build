# Features

What what-we-build does today, and what it will and won't do. Each feature is described from the user's side: what you type, what you see and what you decide.

Status: ✅ built · 🚧 built with a gap named in its section · ⬜ planned.

## Summary

```
Features
├── 🚧 F1: Writing the docs with you — the skill starts from your folder and takes each doc from talk to commit
│   ├── ✅ F1.1: Start from where the project is — an idea, running code or messy docs
│   ├── ✅ F1.2: Agree the doc set — you confirm the docs and where they live
│   ├── ✅ F1.3: Talk each doc through — discuss, brainstorm or decide with a recommendation
│   ├── ✅ F1.4: Push back — the agent says what does not fit and why
│   ├── ✅ F1.5: See the change — every change is shown as before and after
│   ├── ✅ F1.6: Commit after approval — nothing is committed before you approve it
│   └── 🚧 F1.7: Resume — the work picks up later from the docs, not yet verified
├── ✅ F2: Keeping the context — the docs stay true as the work goes on
│   └── ✅ F2.1: Keep the context while you work — the agent reads the owning doc first and records at once
└── ✅ F3: Getting the docs — the docs a project needs, each with a guide
    ├── ✅ F3.1: The core docs — the seven docs every project gets
    ├── ✅ F3.2: Docs that join later — the recommended docs and the ones a project grows into
    ├── ✅ F3.3: A guide per doc — what each doc owns and what it leaves out
    ├── ✅ F3.4: A default layout — the reasons at the root with specs/ and plan/ beside them
    └── ✅ F3.5: Wording rules — short bullets and one name per thing
```

## F1: Writing the docs with you

**Status:** 🚧 [F1.7: Resume](#f17-resume) is not yet verified

The skill starts from your folder. Then each doc goes through one loop from talk to commit, and the work picks up later from the docs.

- **Design:** [DESIGNS 6: Trust the model](DESIGNS.md#6-trust-the-model)
- **Why:** [001: One skill holds every start](specs/decisions/001-one-skill-for-every-start.md) and [007: DESIGNS comes third, before GOALS and FEATURES](specs/decisions/007-designs-third.md)

### F1.1: Start from where the project is

**Status:** ✅

You bring an idea, a codebase or a pile of docs. The skill reads the folder and starts from what it finds.

| The folder holds | The skill starts by |
|---|---|
| An idea and nothing written | discussing the idea with you |
| Running code and no docs | reading the code and then discussing each doc |
| Messy docs | sorting them into the doc set and then discussing the gaps |
| The doc set with uncommitted changes | resuming ([F1.7: Resume](#f17-resume)) |
| The doc set with every change committed | reporting where the project stands and what may have drifted ([F1.7: Resume](#f17-resume)) |
| Something that disagrees with your request | asking you |

### F1.2: Agree the doc set

**Status:** ✅

First you agree the doc set and where the docs live. You go through the project's `AGENTS.md` with the agent and decide together what it should hold. The agent recommends the read order, the layout and the work rules of [F2.1: Keep the context while you work](#f21-keep-the-context-while-you-work).

### F1.3: Talk each doc through

**Status:** ✅

The docs come in order: PROPOSAL → PHILOSOPHY → DESIGNS → GOALS → FEATURES → ROADMAP → README. Each one builds on the ones before it, so you never answer the same question twice. You talk a doc through until its key points are agreed. Every choice comes with a recommendation.

### F1.4: Push back

**Status:** ✅

The agent pushes back when something does not fit. It keeps it up until you decide.

### F1.5: See the change

**Status:** ✅

The agent drafts a doc only after its key points are agreed. You see the draft and every later change as before and after.

### F1.6: Commit after approval

**Status:** ✅

You approve a doc, and the agent commits it. Nothing is committed before you approve it.

### F1.7: Resume

**Status:** 🚧 not yet verified on a real resume

The work can stop at any point and pick up later from the docs. Git tells the agent which docs you approved. On a later `/what-we-build` the agent tells you where the work stopped. It continues at the uncommitted draft or at the first doc in the order not yet written. When every change is committed, it reports where the project stands and what changed since each doc's last commit. You then see which doc may have fallen behind.

- **Design:** [DESIGNS 2: The docs are the state](DESIGNS.md#2-the-docs-are-the-state)
- **Why:** [008: A resume with nothing to draft looks for drift](specs/decisions/008-resume-looks-for-drift.md) and [009: Git tells a draft from an approved doc](specs/decisions/009-git-tells-a-draft-from-an-approved-doc.md)

## F2: Keeping the context

**Status:** ✅

The docs stay true as the work goes on, because the agent keeps them true in every new window.

### F2.1: Keep the context while you work

**Status:** ✅

In every new window the agent reads the doc that owns a thing before it changes it, records each decision and open item at once, and asks you when the docs and the code disagree.

The skill starts only when you type `/what-we-build`. The rules still reach every new window through the project's `AGENTS.md`. You agree to record them there when you go through it with the agent.

- **Design:** [DESIGNS 2: The docs are the state](DESIGNS.md#2-the-docs-are-the-state)
- **Why:** [002: The skill starts only by hand](specs/decisions/002-manual-start.md)

## F3: Getting the docs

**Status:** ✅

A project gets the docs it needs and no more. Each kind of doc has a guide.

- **Design:** [DESIGNS 1: A short core with detail on demand](DESIGNS.md#1-a-short-core-with-detail-on-demand)
- **Why:** [005: One guide file per kind of doc](specs/decisions/005-one-guide-per-kind-of-doc.md)

### F3.1: The core docs

**Status:** ✅

Every project gets seven core docs: PROPOSAL · PHILOSOPHY · DESIGNS · GOALS · FEATURES · ROADMAP · README.

### F3.2: Docs that join later

**Status:** ✅

| Kind | Docs |
|---|---|
| Recommended for every project | TODO · CHANGELOG · `specs/decisions/` |
| Optional | `specs/` with ARCHITECTURE and UIUX · GLOSSARY · INSTALL · CONTRIBUTING · SECURITY · RUNBOOK |

The recommended docs start once you agree the doc set. A finding or a change then has a home from the start. The optional docs join only when the project needs them.

### F3.3: A guide per doc

**Status:** ✅

The agent reads a doc's guide before it starts that doc. The guide says what the doc owns and what it leaves out.

### F3.4: A default layout

**Status:** ✅

You choose where the docs live. By default the layout looks like this:

- The reasons and the contract sit at the root.
- `specs/` holds how each part works, with `specs/decisions/` under it.
- `plan/` holds GOALS, ROADMAP and TODO.

You decide with the agent whether `AGENTS.md` records the layout.

### F3.5: Wording rules

**Status:** ✅

The docs come out in plain and precise English. A reader finds a fact fast and understands it the first time.

| Rule | What you see in the docs |
|---|---|
| Paragraphs or bullets | A paragraph is one block and a bullet is one sentence |
| Short bullets | A bullet holds at most one comma |
| Bullets for lists | A list is never packed into a sentence |
| Prose for reasons | An argument stays prose, as in PHILOSOPHY |
| One name per thing | A word means the same thing in every doc |
| Numbers with sources | A number instead of an adjective, with its source |
| Shared status marks | ✅ 🚧 🟨 ⬜ ❌ mean the same in every doc |
| No code chunks | A doc explains and never pastes code |

- **Design:** [DESIGNS 4: Our own words over borrowed text](DESIGNS.md#4-our-own-words-over-borrowed-text)

## When something fails

| Case | What you see | Feature |
|---|---|---|
| The folder and your request disagree | the agent asks you which to follow | F1.1: Start from where the project is |
| A fact has no doc to own it | the agent asks you what to do with it | F1.3: Talk each doc through |
| A number is not known | it stays open in the doc | F1.3: Talk each doc through |
| The docs and the code disagree | the agent tells you and you decide | F2.1: Keep the context while you work |
| The window was compacted | the agent reads the read order again | F2.1: Keep the context while you work |
| You stop the agent | it stops | F2.1: Keep the context while you work |

## Later, if needed

| Idea | Note |
|---|---|
| Place one fact | `/what-we-build place "<fact>"` runs the placement test on one new fact and edits the doc that owns it |
| Wording rules in other languages | One file per language, written in that language and not translated |

## Not planned

| Not this | Why |
|---|---|
| Starting on its own | [002: The skill starts only by hand](specs/decisions/002-manual-start.md) |
| Drafting without a conversation | Text nobody decided is the problem the skill exists to solve. |
| A fixed questionnaire or template | Fixed questions fill forms. Decisions come from a conversation. |
| More docs than the project needs | Only a doc with a job gets kept true. |
| Choosing how a product should feel | That is the user's call. The skill records the user's words when they bring them. |
| User manuals such as tutorials and API references | They say how to use the product, not why it is this way. |
| A whole `AGENTS.md` | The skill recommends only the read order, the layout and the work rules. Claude Code's `/init` writes the rest from the code. |
| Standard texts such as LICENSE | They need a choice of a standard text, not a discussion. |
| Scripts that check the docs | The skill is Markdown only, so a reader checks the links and the facts ([DESIGNS 3: No dependencies](DESIGNS.md#3-no-dependencies)). |
