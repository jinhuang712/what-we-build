<!-- what-we-build: approved 2026-11-02 -->

# Features

What what-we-build does today, and what it will and won't do. Each feature is described from the user's side: what you type, what you see and what you decide. How far each feature has been used in real life is in [ROADMAP.md](ROADMAP.md).

Two words have one meaning each here:

- A **session** is one what-we-build conversation, from `/what-we-build` to the last approval.
- A **sitting** is one Claude Code session.

A session can span several sittings through resume.

Status: ✅ built · 🚧 built with a gap named in its section · ⬜ planned.

## Summary

**Running a session**

| Capability | What it does | Feature | Status |
|---|---|---|---|
| Start from where the project is | an idea, running code or messy docs | [F1: Start and talk each doc through](#f1-start-and-talk-each-doc-through) | ✅ |
| Agree the doc set | you confirm the docs and where they live | [F1: Start and talk each doc through](#f1-start-and-talk-each-doc-through) | ✅ |
| Talk each doc through | discuss, brainstorm or decide with a recommendation | [F1: Start and talk each doc through](#f1-start-and-talk-each-doc-through) | ✅ |
| Push back | the agent says what does not fit and why | [F1: Start and talk each doc through](#f1-start-and-talk-each-doc-through) | ✅ |
| See the change | every change is shown as before and after | [F1: Start and talk each doc through](#f1-start-and-talk-each-doc-through) | ✅ |
| Commit after approval | a doc is committed only after you approve it | [F1: Start and talk each doc through](#f1-start-and-talk-each-doc-through) | ✅ |
| Marks | a hidden mark on each doc's first line says `drafted` or `approved` | [F2: Resume](#f2-resume) | ✅ |
| Resume | a later sitting continues at the first doc not approved | [F2: Resume](#f2-resume) | ✅ |

**Keeping the context**

| Capability | What it does | Feature | Status |
|---|---|---|---|
| Read order | the project's `AGENTS.md` says which docs to read first | [F5: Keep the context while you work](#f5-keep-the-context-while-you-work) | ✅ |
| Read before a change | the agent reads the doc that owns a thing before it changes it | [F5: Keep the context while you work](#f5-keep-the-context-while-you-work) | ✅ |
| Record at once | a decision or an open item is written down when it comes up | [F5: Keep the context while you work](#f5-keep-the-context-while-you-work) | ✅ |
| Ask on a mismatch | when the docs and the code disagree you decide | [F5: Keep the context while you work](#f5-keep-the-context-while-you-work) | ✅ |
| Done means recorded | a finished change updates CHANGELOG and the feature's status | [F5: Keep the context while you work](#f5-keep-the-context-while-you-work) | ✅ |

**Getting the docs**

| Capability | What it does | Feature | Status |
|---|---|---|---|
| Core docs | the seven docs every project gets | [F3: The doc set](#f3-the-doc-set) | ✅ |
| Recommended docs | TODO, CHANGELOG and `specs/decisions/` from the start | [F3: The doc set](#f3-the-doc-set) | ✅ |
| Optional docs | specs and the rest only when the project needs them | [F3: The doc set](#f3-the-doc-set) | ✅ |
| A guide per doc | what the doc owns and what it leaves out | [F3: The doc set](#f3-the-doc-set) | ✅ |
| A default layout | the reasons at the root with `specs/` and `plan/` beside them | [F3: The doc set](#f3-the-doc-set) | ✅ |
| Wording rules | short lines and one name per thing | [F4: Wording rules](#f4-wording-rules) | ✅ |

## Running a session

### F1: Start and talk each doc through

**Status:** ✅

You bring an idea, a codebase or a pile of docs. The skill reads the folder and starts from what it finds.

| The folder holds | The skill starts by |
|---|---|
| An idea and nothing written | discussing the idea with you |
| Running code and no docs | reading the code and then discussing each doc |
| Messy docs | sorting them into the doc set and then discussing the gaps |
| Docs with marks and not all approved | resuming ([F2: Resume](#f2-resume)) |
| Docs with marks and all approved | reporting where the project stands and what may have drifted ([F2: Resume](#f2-resume)) |
| Something that disagrees with your request | asking you |

First you agree the doc set and where the docs live. You go through the project's `AGENTS.md` with the agent and decide together what it should hold. The agent recommends the read order, the layout and the work rules of [F5: Keep the context while you work](#f5-keep-the-context-while-you-work). Then each doc goes through the same loop:

1. You talk it through until its key points are agreed.
2. The agent drafts it and marks it `drafted`.
3. You see the change as before and after.
4. You approve it, and the mark becomes `approved`.
5. The agent commits it.

The docs come in order: PROPOSAL → PHILOSOPHY → DESIGNS → GOALS → FEATURES → ROADMAP → README. Each one builds on the ones before it, so you never answer the same question twice. Every choice comes with a recommendation. The agent pushes back when something does not fit and keeps it up until you decide.

- **Design:** [DESIGNS 6: Trust the model](DESIGNS.md#6-trust-the-model)
- **Why:** [001: One skill holds every start](specs/decisions/001-one-skill-for-every-start.md) and [007: DESIGNS comes third, before GOALS and FEATURES](specs/decisions/007-designs-third.md)

### F2: Resume

**Status:** ✅

A session can stop at any point and pick up in a later sitting. Each drafted doc carries a mark on its first line that does not show when rendered. The mark becomes `approved` when you approve the doc. It goes back to `drafted` whenever the doc is edited again. On a later `/what-we-build` the agent reads the marks and tells you where the session stopped. It continues at the first doc in the order that is not approved. When every doc is approved, it reports where the project stands and what changed since each approval. You then see which doc may have fallen behind. A doc that grows one entry at a time carries no mark, such as TODO or CHANGELOG.

- **Design:** [DESIGNS 2: The docs are the state](DESIGNS.md#2-the-docs-are-the-state)
- **Why:** [008: A resume with nothing to draft looks for drift](specs/decisions/008-resume-looks-for-drift.md)

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
| The folder and your request disagree | the agent asks you which to follow | [F1: Start and talk each doc through](#f1-start-and-talk-each-doc-through) |
| A fact has no doc to own it | the agent asks you what to do with it | [F1: Start and talk each doc through](#f1-start-and-talk-each-doc-through) |
| A number is not known | it stays open in the doc | [F1: Start and talk each doc through](#f1-start-and-talk-each-doc-through) |
| The docs and the code disagree | the agent tells you and you decide | [F5: Keep the context while you work](#f5-keep-the-context-while-you-work) |
| The window was compacted | the agent reads the read order again | [F5: Keep the context while you work](#f5-keep-the-context-while-you-work) |
| You stop the agent | it stops | [F5: Keep the context while you work](#f5-keep-the-context-while-you-work) |

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
