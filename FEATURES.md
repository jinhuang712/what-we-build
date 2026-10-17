<!-- what-we-build: drafted 2026-10-17 -->

# Features

What what-we-build does today, and what it will and won't do. Each feature is described from the user's side: what you type, what you see, what you decide. How far each feature has been used in real life is in [ROADMAP.md](ROADMAP.md).

Two words have one meaning each here. A **session** is one what-we-build conversation, from `/what-we-build` to the last approval. A **sitting** is one Claude Code session. A session can span several sittings, through resume.

Status: ✅ built · 🚧 built, with the gap named in its section · ⬜ planned.

## TL;DR

Every capability by group, with the feature it belongs to and its status. The details follow below, in the same order.

**Running a session**

| Capability | What it does | Feature | Status |
|---|---|---|---|
| Choose the mode | reads the folder, then starts a new project or resumes | F1 | ✅ |
| Pick the mode yourself | `new` or `resume` as an argument | F1 | ✅ |
| Frame the idea | you say the idea and who it is for, and the skill says what the folder already holds | F1 | ✅ |
| Agree on the doc set | you confirm or change the recommended docs | F1 | ✅ |
| Talk each doc through | discuss, brainstorm or decide, with a recommendation whenever a choice is ready | F1 | ✅ |
| Plain questions | each choice is explained in plain words, with a concrete case or a real sample, before you are asked | F1 | ✅ |
| Options tied to cases | each option names the case where it matters | F1 | ✅ |
| Choices drawn | a choice with several moving parts is shown as a small diagram first | F1 | ✅ |
| Your own list, discussed | a list you bring, such as principles, gets the agent's additions and doubts before it is adopted | F1 | ✅ |
| Push back | a push-back with its reason when something does not fit, kept up until you decide | F1 | ✅ |
| Open points parked | a point that needs design you are not ready for goes to TODO, then to the roadmap, so the doc can close | F1 | ✅ |
| Write after you agree | a doc is written only after its key points are agreed, and marked `drafted` | F1 | ✅ |
| Fixes across the whole doc | when you point out one wrong word, every place with the same idea is fixed | F1 | ✅ |
| Approve | your approval turns the mark to `approved` | F1 | ✅ |
| Docs in order | each doc builds on the ones before it, so you never answer twice | F1 | ✅ |
| Close | each doc's status, and the questions you still own | F1 | ✅ |
| Marks | an invisible mark on each doc's first line says `drafted` or `approved` | F2 | ✅ |
| Resume | a later sitting continues at the first doc that is not approved | F2 | ✅ |

**Getting the docs**

| Capability | What it does | Feature | Status |
|---|---|---|---|
| Core docs | PROPOSAL, PHILOSOPHY, DESIGNS, GOALS, FEATURES, ROADMAP and README | F3 | ✅ |
| TODO and CHANGELOG from the start | recommended for every project, and created once the doc set is agreed | F3 | ✅ |
| Optional docs | UIUX, GLOSSARY, CONTRIBUTING, SECURITY and RUNBOOK, only when the project needs them | F3 | ✅ |
| A guide per doc | the questions, the push-back and the form fit that doc | F3 | ✅ |
| Other names mapped | a PRD maps to FEATURES, and an ARCHITECTURE.md to DESIGNS | F3 | ✅ |
| One name per thing | a word means the same thing in every doc | F4 | ✅ |
| Short sentences | one point per sentence, with conditions first | F4 | ✅ |
| Numbers with sources | a number instead of an adjective, and a source for every number that states a fact | F4 | ✅ |
| Shared status marks | ✅ 🚧 🟨 ⬜ ❌ mean the same in every doc | F4 | ✅ |
| A form per doc | for example, GOALS is a short intro and two tables, goals and benchmarks | F4 | ✅ |
| An outline up front | FEATURES opens with a TL;DR of every capability, and DESIGNS with the principles it is built around | F4 | ✅ |
| Principles that drive decisions | each design principle asks a question of new requirements and lists the decisions it drives. A feature's own decisions stay with the feature | F4 | ✅ |
| Philosophy from questions | each stance comes from your answer, then is tested against books and papers | F4 | ✅ |

## Running a session

### F1 — New project: talk it through ✅

A session turns an idea into the founding documents of a project.

- You bring one or two sentences.
- The skill talks each document through with you until its key points are clear, then writes it down. Some points need discussion, some a brainstorm, and some a clear choice.
- You stay in charge throughout: every choice comes with a recommendation, and nothing is written before you agree.

| Stage | What you do | What you get |
|---|---|---|
| Frame | Describe the idea and who it is for | A one-line summary of what the folder already holds |
| Doc set | Confirm or change the recommended docs | The 7 core docs, plus the optional ones the project needs |
| Each doc | Talk each point through: discuss it, brainstorm it, or pick from options | A recommendation with its reason whenever a choice is ready |
| Each doc | Hear what does not fit, and keep or drop it | A push-back with its reason, such as an adjective where a goal needs a number, until you decide |
| Each doc | Agree on the doc's key points | The doc, written and marked `drafted` |
| Each doc | Approve it, or ask for changes | The mark becomes `approved` |
| Close | Read the summary | Each doc's status, and the questions you still own |

The docs come in order: PROPOSAL → PHILOSOPHY → DESIGNS → GOALS → FEATURES → ROADMAP → README. Each one builds on the ones before it, so you never answer the same question twice. The design comes right after the philosophy, because the design guides the features.

**Choosing the mode.** `/what-we-build` alone reads the folder and picks the mode. An argument picks it for you: `new` or `resume`.

| The folder holds | The skill |
|---|---|
| No founding docs, or docs without marks | starts a new project, building on what it finds |
| Docs with marks, not all approved | resumes |
| Something that disagrees with your request | asks you |

### F2 — Resume ✅

A session can stop at any point and pick up in a later sitting. Each drafted doc carries a mark on its first line, invisible when rendered:

```markdown
<!-- what-we-build: drafted 2026-10-13 -->
```

The mark becomes `approved` when you approve the doc, and goes back to `drafted` whenever the doc is edited again. `/what-we-build resume` reads the marks, tells you where the session stopped, and continues at the first doc that is not approved.

## Getting the docs

### F3 — The doc set ✅

The skill knows 14 kinds of document: 7 core and 7 optional. Two optional docs, TODO and CHANGELOG, are recommended for every project and start when you agree on the doc set, so a finding or a change has a home from the start. The other five join only when the project needs them.

| Kind | Docs |
|---|---|
| Core | PROPOSAL, PHILOSOPHY, DESIGNS, GOALS, FEATURES, ROADMAP, README |
| Optional, recommended for every project | TODO, CHANGELOG |
| Optional, when the project needs them | UIUX, GLOSSARY, CONTRIBUTING, SECURITY, RUNBOOK |

For each kind, the skill carries a guide. The agent reads it before it starts that doc, so the questions, the push-back and the doc's form fit that doc. It also maps other common names to the set, for example a PRD to FEATURES, or an ARCHITECTURE.md to DESIGNS.

### F4 — Wording rules ✅

The docs come out in plain, precise English, so a reader finds a fact fast and understands it the first time.

| Rule | What you see in the docs |
|---|---|
| One name per thing | A word means the same thing in every doc |
| Short sentences | One point per sentence, with conditions first |
| Numbers with sources | A number instead of an adjective, and a source for every number that states a fact |
| Shared status marks | ✅ 🚧 🟨 ⬜ ❌ mean the same in every doc |

Each doc also has its own form:

- GOALS is a short intro and two tables: goals that pass or fail, and benchmarks tracked against a reference.
- FEATURES opens with a TL;DR: an outline of every capability, by group. The details follow in the same order, written to scan, with each feature's own decisions under it and a table of what happens when something fails.
- DESIGNS opens with the few principles the design is built around. Each principle asks a question of every new requirement and lists the decisions it drives, each with the option it beat. Open design questions wait in TODO, then in ROADMAP.
- PHILOSOPHY is where the project thinks: a few questions the project takes a stance on, each argued in full and tested against books and papers, with room below for reflections. The skill asks you those questions first, each stance comes from your answer, and then the skill goes deeper with sources.

## Later, if needed

| Idea | Note |
|---|---|
| Place one fact | `/what-we-build place "<fact>"` runs the placement test on one new fact and edits the doc that owns it |
| Wording rules in other languages | One file per language, written in that language, not translated |

## Not planned

| Not this | Why |
|---|---|
| Starting on its own | A session needs the user's full attention, so it starts when the user types it. |
| Drafting without a conversation | Text nobody decided is the problem the skill exists to solve. |
| A fixed questionnaire or template | Fixed questions fill forms. Decisions come from a conversation. |
| More docs than the project needs | Optional docs join only when they have a job, because only a doc with a job gets kept true. |
| Choosing how a product should feel | That is the user's call. The skill records the user's words when they bring them. |
| User manuals (tutorials, how-to guides, API and command references) | They answer other questions, after the founding docs exist. |
| Agent instruction files (AGENTS.md, CLAUDE.md) | They hold the commands and rules for the code, which comes after the founding docs. Claude Code's `/init` writes one from the code. |
| Decision records (ADRs) | DESIGNS.md holds the decisions that span the project, under the principles that drive them, and FEATURES.md holds each feature's own decisions, each with the option it beat and its reason. |
| Standard texts (LICENSE, CODE_OF_CONDUCT) | They need a choice of a standard text, not a discussion. |
| Scripts that check the docs, such as links or blank lines | The skill's job is the conversation. The agent keeps links and blank lines right while it writes. |
