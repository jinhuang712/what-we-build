# Features

What what-we-build does today, and what it will and won't do. Each feature is described from the user's side: what you type, what you see and what you decide.

Two words have one meaning each here:

- A **session** is one what-we-build conversation, from `/what-we-build` to the last approval.
- A **sitting** is one Claude Code session.

A session can span several sittings through resume.

Status: ✅ built · 🚧 built with a gap named in its section · ⬜ planned.

## Summary

**Running a session**

| Capability | What it does | Status |
|---|---|---|
| Start from where the project is | an idea, running code or messy docs | ✅ |
| Agree the doc set | you confirm the docs and where they live | ✅ |
| Talk each doc through | discuss, brainstorm or decide with a recommendation | ✅ |
| Push back | the agent says what does not fit and why | ✅ |
| See the change | every change is shown as before and after | ✅ |
| Commit after approval | a doc is committed only after you approve it | ✅ |
| Resume | a later sitting continues at the draft or the first doc not yet written | ✅ |

**Keeping the context**

| Capability | What it does | Status |
|---|---|---|
| Read order | the project's `AGENTS.md` says which docs to read first | ✅ |
| Read before a change | the agent reads the doc that owns a thing before it changes it | ✅ |
| Record at once | a decision or an open item is written down when it comes up | ✅ |
| Ask on a mismatch | when the docs and the code disagree you decide | ✅ |
| Done means recorded | a finished change updates CHANGELOG and the feature's status | ✅ |

**Getting the docs**

| Capability | What it does | Status |
|---|---|---|
| Core docs | the seven docs every project gets | ✅ |
| Recommended docs | TODO, CHANGELOG and `specs/decisions/` from the start | ✅ |
| Optional docs | specs and the rest only when the project needs them | ✅ |
| A guide per doc | what the doc owns and what it leaves out | ✅ |
| A default layout | the reasons at the root with `specs/` and `plan/` beside them | ✅ |
| Wording rules | short lines and one name per thing | ✅ |

## Running a session

### F1: Start and talk each doc through

**Status:** ✅

You bring an idea, a codebase or a pile of docs. The skill reads the folder and starts from what it finds.

| The folder holds | The skill starts by |
|---|---|
| An idea and nothing written | discussing the idea with you |
| Running code and no docs | reading the code and then discussing each doc |
| Messy docs | sorting them into the doc set and then discussing the gaps |
| The doc set with uncommitted changes | resuming ([F2: Resume](#f2-resume)) |
| The doc set with every change committed | reporting where the project stands and what may have drifted ([F2: Resume](#f2-resume)) |
| Something that disagrees with your request | asking you |

First you agree the doc set and where the docs live. You go through the project's `AGENTS.md` with the agent and decide together what it should hold. The agent recommends the read order, the layout and the work rules of [F5: Keep the context while you work](#f5-keep-the-context-while-you-work). Then each doc goes through the same loop:

1. You talk it through until its key points are agreed.
2. The agent drafts it.
3. You see the change as before and after.
4. You approve it, and the agent commits it.

The docs come in order: PROPOSAL → PHILOSOPHY → DESIGNS → GOALS → FEATURES → ROADMAP → README. Each one builds on the ones before it, so you never answer the same question twice. Every choice comes with a recommendation. The agent pushes back when something does not fit and keeps it up until you decide.

- **Design:** [DESIGNS 6: Trust the model](DESIGNS.md#6-trust-the-model)
- **Why:** [001: One skill holds every start](specs/decisions/001-one-skill-for-every-start.md) and [007: DESIGNS comes third, before GOALS and FEATURES](specs/decisions/007-designs-third.md)

### F2: Resume

**Status:** ✅

A session can stop at any point and pick up in a later sitting. Git tells the agent which docs you approved. On a later `/what-we-build` the agent tells you where the session stopped. It continues at the uncommitted draft or at the first doc in the order not yet written. When every change is committed, it reports where the project stands and what changed since each doc's last commit. You then see which doc may have fallen behind.

- **Design:** [DESIGNS 2: The docs are the state](DESIGNS.md#2-the-docs-are-the-state)
- **Why:** [008: A resume with nothing to draft looks for drift](specs/decisions/008-resume-looks-for-drift.md) and [009: Git tells a draft from an approved doc](specs/decisions/009-git-tells-a-draft-from-an-approved-doc.md)

## Keeping the context

### F5: Keep the context while you work

**Status:** ✅

The docs stay true after the first session. The agent follows these rules in every sitting:

| When | The agent |
|---|---|
| A sitting starts or the window was compacted | reads the read order in `AGENTS.md` |
| It is about to change something | reads the doc that owns it |
| It needs to know where the project stands | scans `TODO.md`, `ROADMAP.md` and `GOALS.md` |
| A choice between ways is made | writes a decision at once |
| Something cannot be handled now | adds it to `TODO.md` at once |
| The docs and the code disagree | tells you and lets you decide |
| A change is done | updates `CHANGELOG.md` and the feature's status |
| A todo is handled | deletes it in the same change |
| You stop it | stops |

The skill starts only when you type `/what-we-build`. The rules still reach every sitting through the project's `AGENTS.md`. You agree to record them there when you go through it with the agent.

- **Design:** [DESIGNS 2: The docs are the state](DESIGNS.md#2-the-docs-are-the-state)
- **Why:** [002: The skill starts only by hand](specs/decisions/002-manual-start.md)

## Getting the docs

### F3: The doc set

**Status:** ✅

| Kind | Docs |
|---|---|
| Core | PROPOSAL · PHILOSOPHY · DESIGNS · GOALS · FEATURES · ROADMAP · README |
| Recommended for every project | TODO · CHANGELOG · `specs/decisions/` |
| Optional | `specs/` with ARCHITECTURE and UIUX · GLOSSARY · CONTRIBUTING · SECURITY · RUNBOOK |

The recommended docs start once you agree the doc set. A finding or a change then has a home from the start. The optional docs join only when the project needs them.

Each kind of doc has a guide. The agent reads it before it starts that doc. The guide says what the doc owns and what it leaves out.

You choose where the docs live. By default the layout looks like this:

- The reasons and the contract sit at the root.
- `specs/` holds how each part works, with `specs/decisions/` under it.
- `plan/` holds GOALS, ROADMAP and TODO.

You decide with the agent whether `AGENTS.md` records the layout.

- **Design:** [DESIGNS 1: A short core with detail on demand](DESIGNS.md#1-a-short-core-with-detail-on-demand)
- **Why:** [005: One guide file per kind of doc](specs/decisions/005-one-guide-per-kind-of-doc.md)

### F4: Wording rules

**Status:** ✅

The docs come out in plain and precise English. A reader finds a fact fast and understands it the first time.

| Rule | What you see in the docs |
|---|---|
| Paragraphs or bullets | A paragraph is one block and a bullet is one sentence |
| Short sentences | A sentence holds at most one comma |
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
| The folder and your request disagree | the agent asks you which to follow | F1: Start and talk each doc through |
| A fact has no doc to own it | the agent asks you what to do with it | F1: Start and talk each doc through |
| A number is not known | it stays open in the doc | F1: Start and talk each doc through |
| The docs and the code disagree | the agent tells you and you decide | F5: Keep the context while you work |
| The window was compacted | the agent reads the read order again | F5: Keep the context while you work |
| You stop the agent | it stops | F5: Keep the context while you work |

## Later, if needed

| Idea | Note |
|---|---|
| Place one fact | `/what-we-build place "<fact>"` runs the placement test on one new fact and edits the doc that owns it |
| Wording rules in other languages | One file per language, written in that language and not translated |

## Not planned

| Not this | Why |
|---|---|
| Starting on its own | A session needs the user's full attention, so it starts when the user types it. |
| Drafting without a conversation | Text nobody decided is the problem the skill exists to solve. |
| A fixed questionnaire or template | Fixed questions fill forms. Decisions come from a conversation. |
| More docs than the project needs | Only a doc with a job gets kept true. |
| Choosing how a product should feel | That is the user's call. The skill records the user's words when they bring them. |
| User manuals such as tutorials and API references | They say how to use the product, not why it is this way. |
| A whole `AGENTS.md` | The skill recommends only the read order, the layout and the work rules. Claude Code's `/init` writes the rest from the code. |
| Standard texts such as LICENSE | They need a choice of a standard text, not a discussion. |
| Scripts that check the docs | A reader checks the links and the facts ([DESIGNS 7: Readers check the docs, not scripts](DESIGNS.md#7-readers-check-the-docs-not-scripts)). |
