# Features

What what-we-build does today, and what it will and won't do. Each feature is described from the user's side: what you type, what you see and what you decide.

Status: ✅ built · 🚧 built, with a gap named beside it · ⬜ planned. A ✅ says the skill does it, and whether it works on a real project is checked in ROADMAP and GOALS.

## Summary

```
Features
├── ✅ F1: Writing the docs with you — the skill starts from your folder and talks each doc through with you
│   ├── ✅ F1.1: Start from where the project is — an idea, running code or old docs
│   ├── ✅ F1.2: Agree the doc set — you confirm the docs and where they live
│   ├── ✅ F1.3: Talk each doc through — discuss, brainstorm or decide with a recommendation
│   ├── ✅ F1.4: Push back — the agent says what does not fit and why
│   ├── ✅ F1.5: See the change — every change is shown as before and after
│   └── ✅ F1.7: Resume — you stop at any point and pick up later
├── ✅ F2: Keeping the context — the docs stay true as the work goes on
│   ├── ✅ F2.1: Keep the context while you work — the agent reads the owning doc first and records at once
│   └── ✅ F2.2: A wiki when others build on it — the agent tells you when the project may need one
└── ✅ F3: Getting the docs — the docs a project needs, each with a guide
    ├── ✅ F3.1: The core docs — the seven docs every project gets
    ├── ✅ F3.2: Docs that join later — the recommended docs and the ones a project grows into
    ├── ✅ F3.3: A guide per doc — what each doc owns and what it leaves out
    ├── ✅ F3.4: A default layout — the reasons at the root with specs/ and plan/ beside them
    └── ✅ F3.5: Wording rules — short bullets and one name per thing
```

## F1: Writing the docs with you

**Status:** ✅

The skill starts from your folder and talks each doc through with you, from the first agreed point to the commit. You can stop at any point and pick up later.

- **Design:** [DESIGNS 6: Trust the model](DESIGNS.md#6-trust-the-model)
- **Why:** [001: One skill holds every start](specs/decisions/001-one-skill-for-every-start.md) and [007: DESIGNS comes third, before GOALS and FEATURES](specs/decisions/007-designs-third.md)

### F1.1: Start from where the project is

**Status:** ✅

You bring an idea, a codebase or a pile of old docs. The agent reads the folder first, and whatever it finds is material for the talk with you. When part of the doc set is already written, the work picks up where it stopped ([F1.7: Resume](#f17-resume)).

**Stories:**

- Whoever types `/what-we-build` starts from what the folder already holds, so nobody starts from a blank form.

### F1.2: Agree the doc set

**Status:** ✅

You agree with the agent which docs the project gets and where they live. You also decide together what the project's `AGENTS.md` should hold. The agent recommends the read order, the layout and the work rules of [F2.1: Keep the context while you work](#f21-keep-the-context-while-you-work).

**Stories:**

- You confirm which docs the project gets and where they live, so no doc exists without a job.

### F1.3: Talk each doc through

**Status:** ✅

The docs come in order: PROPOSAL → PHILOSOPHY → DESIGNS → GOALS → FEATURES → ROADMAP → README. Each one builds on the ones before it, so you never answer the same question twice. Every choice comes with a recommendation. The agent says when it thinks the talk is enough and what is still open, and you judge it together.

- **Why:** [031: The skill leaves the form of the talk open](specs/decisions/031-the-skill-leaves-the-form-of-the-talk-open.md)

**Stories:**

- You talk a doc through point by point with the agent, so the doc says what you decided.

### F1.4: Push back

**Status:** ✅

The agent pushes back when something does not fit. It keeps it up until you decide.

**Stories:**

- You hear why an idea does not fit before it goes into a doc, so a weak point is caught early.

### F1.5: See the change

**Status:** ✅

You see each change before it is committed. The agent writes each point into its doc once you agree it, and nothing before. It commits the change once you approve it.

**Stories:**

- You approve a change only after you have seen it, so nothing reaches a doc behind your back.

### F1.7: Resume

**Status:** ✅

You can stop at any point and pick up later, because every agreed point is already in its doc and every open one is in `TODO.md`. On a later `/what-we-build` the agent tells you where the work stands, what is still open and which docs may have fallen behind it.

- **Design:** [DESIGNS 2: The docs are the state](DESIGNS.md#2-the-docs-are-the-state)
- **Why:** [008: A resume with nothing to draft looks for drift](specs/decisions/008-resume-looks-for-drift.md) and [024: Approval lives in the conversation](specs/decisions/024-approval-lives-in-the-conversation.md)

**Stories:**

- You come back another day and the agent picks up at the first doc that is not finished.
- You return to a finished doc set and learn which docs fell behind the work.

## F2: Keeping the context

**Status:** ✅

The docs stay true as the work goes on, not only while they are first written.

- **Stance:** [What should a project manage?](PHILOSOPHY.md#what-should-a-project-manage)

### F2.1: Keep the context while you work

**Status:** ✅

The agent reads the doc that owns a thing before it changes it. It reads and writes every doc in its own window, and hands only the code to a subagent. It records an open item at once. It records a decision at once too, but only for a choice that had another way open, may be undone later and has a reason the code does not show. When the docs and the code disagree, it asks you.

The skill starts only when you type `/what-we-build`, so these rules live in the project's `AGENTS.md`, which the agent reads whenever its window is new. You agree to record them there when you go through it with the agent.

- **Design:** [DESIGNS 2: The docs are the state](DESIGNS.md#2-the-docs-are-the-state)
- **Why:** [002: The skill starts only by hand](specs/decisions/002-manual-start.md) and [030: The main window reads and writes the docs](specs/decisions/030-the-main-window-reads-and-writes-the-docs.md)

**Stories:**

- An agent in a new window reads the docs in the read order, so it knows the project before it works.
- The agent reads each doc itself before a rewrite, so it learns the project instead of passing it to a subagent.
- You find the open items and the decisions written down at once, so nothing lives only in the window.

### F2.2: A wiki when others build on it

**Status:** ✅

When other developers start to build on your project, often with their own agents, the source alone leaves them guessing how to use it. The agent tells you then that the project may need a wiki. What the wiki holds and where it lives is your call, and the skill gives it no guide.

- **Why:** [023: The skill points to a wiki and leaves its form to the project](specs/decisions/023-the-skill-points-to-a-wiki.md)

**Stories:**

- You hear at the right time that the project may need a wiki, so the developers who build on it do not have to read the source.

## F3: Getting the docs

**Status:** ✅

A project gets the docs it needs and no more. Each kind of doc has a guide.

- **Design:** [DESIGNS 1: A short core with detail on demand](DESIGNS.md#1-a-short-core-with-detail-on-demand)
- **Why:** [005: One guide file per kind of doc](specs/decisions/005-one-guide-per-kind-of-doc.md)

### F3.1: The core docs

**Status:** ✅

Every project gets seven core docs: PROPOSAL · PHILOSOPHY · DESIGNS · GOALS · FEATURES · ROADMAP · README.

**Stories:**

- You get the seven docs every project needs, so the reasons and the contract are written down.

### F3.2: Docs that join later

**Status:** ✅

| Kind | Docs |
|---|---|
| Recommended for every project | TODO · CHANGELOG · `specs/decisions/` |
| Optional | `specs/` with ARCHITECTURE and UIUX · GLOSSARY · INSTALL · CONTRIBUTING · SECURITY · RUNBOOK |

The recommended docs start once you agree the doc set. A finding or a change then has a home from the start. The optional docs join only when the project needs them.

**Stories:**

- You add an optional doc only when the project needs it, so you keep no doc without a job.

### F3.3: A guide per doc

**Status:** ✅

The agent reads a doc's guide before it starts that doc. The guide says in `[YES]`, `[NO]`, `[MAYBE]` and `[WHEN]` lines what the doc holds, what goes elsewhere and how to write it. Where a model tends to blur a doc's core idea, the guide says what it is and is not.

**Stories:**

- The agent reads a doc's guide before it writes that doc, so each doc holds only what it owns.

### F3.4: A default layout

**Status:** ✅

You choose where the docs live. By default the layout looks like this:

- The reasons and the contract sit at the root.
- `specs/` holds how each part works, with `specs/decisions/` under it.
- `plan/` holds GOALS, ROADMAP and TODO.

You decide with the agent whether `AGENTS.md` records the layout.

**Stories:**

- You keep the default layout or choose your own, and each doc keeps its name wherever it sits.

### F3.5: Wording rules

**Status:** ✅

The docs come out in plain and precise English. A reader finds a fact fast and understands it the first time, because every doc explains in short paragraphs, keeps a bullet to one sentence and calls each thing by one name. Status marks, IDs and dates look the same in every doc, and no doc pastes code.

**Stories:**

- A reader finds a fact on the first read, because every doc uses the same plain wording.

## When something fails

| Case | What you see | Feature |
|---|---|---|
| The folder and your request disagree | the agent asks you which to follow | F1.1: Start from where the project is |
| A fact has no doc to own it | the agent asks you what to do with it | F1.3: Talk each doc through |
| A number is not known | it stays open in the doc | F1.3: Talk each doc through |
| The docs and the code disagree | the agent tells you and you decide | F2.1: Keep the context while you work |
| The window was compacted | the agent reads the read order again | F2.1: Keep the context while you work |
| You stop the agent | it stops at once with every agent it started | F2.1: Keep the context while you work |

## Later, if needed

| Idea | Note |
|---|---|
| Place one fact | `/what-we-build place "<fact>"` runs the placement test on one new fact and edits the doc that owns it |
| Wording rules in other languages | One file per language, written in that language and not translated |

## Not planned

| Not this | Why |
|---|---|
| Starting on its own | The talk needs your full attention ([002: The skill starts only by hand](specs/decisions/002-manual-start.md)). |
| Drafting without a conversation | Text nobody decided is the problem the skill exists to solve. |
| A fixed questionnaire or template | Fixed questions fill forms. Decisions come from a conversation. |
| More docs than the project needs | Only a doc with a job gets kept true. |
| Choosing how a product should feel | That is the user's call. The skill records the user's words when they bring them. |
| Writing or shaping a wiki | What it holds depends on the project, so the skill only says when one may be needed ([F2.2: A wiki when others build on it](#f22-a-wiki-when-others-build-on-it)). |
| A whole `AGENTS.md` | The skill recommends only the read order, the layout and the work rules. Claude Code's `/init` writes the rest from the code. |
| Standard texts such as LICENSE | They need a choice of a standard text, not a discussion. |
| Scripts that check the docs | The skill is Markdown only, so a reader checks the links and the facts ([DESIGNS 3: No dependencies](DESIGNS.md#3-no-dependencies)). |
