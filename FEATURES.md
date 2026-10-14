<!-- what-we-build: drafted 2026-10-14 -->

# Features

What what-we-build does today, and what it will and won't do. Each feature is described from the user's side: what you type, what you see, what you decide. How far each feature has been used in real life is in [ROADMAP.md](ROADMAP.md).

Two words have one meaning each here. A **session** is one what-we-build conversation, from `/what-we-build` to the last approval. A **sitting** is one Claude Code session. A session can span several sittings, through resume.

Status: ✅ built · 🚧 built, with the gap named in its section · ⬜ planned.

## F1 — New project: talk it through ✅

A session turns an idea into the founding documents of a project. You bring one or two sentences. The skill talks each document through with you until its key points are clear, then writes it down. Some points need discussion, some a brainstorm, and some a clear choice. You stay in charge throughout: every choice comes with a recommendation, and nothing is written before you agree.

| Stage | What you do | What you get |
|---|---|---|
| Frame | Describe the idea and who it is for | A one-line summary of what the folder already holds |
| Doc set | Confirm or change the recommended docs | The 7 core docs, plus the optional ones the project needs |
| Each doc | Talk each point through: discuss it, brainstorm it, or pick from options | A recommendation with its reason whenever a choice is ready |
| Each doc | Hear what does not fit, and keep or drop it | One push-back with its reason, such as an adjective where a goal needs a number |
| Each doc | Agree on the doc's key points | The doc, written and marked `drafted` |
| Each doc | Approve it, or ask for changes | The mark becomes `approved` |
| Close | Read the summary | Each doc's status, and the questions you still own |

The docs come in order: PROPOSAL → PHILOSOPHY → GOALS → FEATURES → DESIGNS → ROADMAP → README. Each one builds on the ones before it, so you never answer the same question twice.

**Choosing the mode.** `/what-we-build` alone reads the folder and picks the mode. An argument picks it for you: `new` or `resume`.

| The folder holds | The skill |
|---|---|
| No founding docs, or docs without marks | starts a new project, building on what it finds |
| Docs with marks, not all approved | resumes |
| Something that disagrees with your request | asks you |

## F2 — Resume ✅

A session can stop at any point and pick up in a later sitting. Each drafted doc carries a mark on its first line, invisible when rendered:

```markdown
<!-- what-we-build: drafted 2026-10-13 -->
```

The mark becomes `approved` when you approve the doc, and goes back to `drafted` whenever the doc is edited again. `/what-we-build resume` reads the marks, tells you where the session stopped, and continues at the first doc that is not approved.

## F3 — The doc set ✅

The skill knows 14 kinds of document: 7 core, and 7 optional that join only when the project needs them.

| Kind | Docs |
|---|---|
| Core | PROPOSAL, PHILOSOPHY, GOALS, FEATURES, DESIGNS, ROADMAP, README |
| Optional | UIUX, GLOSSARY, CHANGELOG, TODO, CONTRIBUTING, SECURITY, RUNBOOK |

For each kind, the skill carries a guide. The agent reads it before it starts that doc, so the questions, the push-back and the doc's form fit that doc. It also maps other common names to the set, for example a PRD to FEATURES, or an ARCHITECTURE.md to DESIGNS.

## F4 — Wording rules ✅

The docs come out in plain, precise English, so a reader finds a fact fast and understands it the first time.

| Rule | What you see in the docs |
|---|---|
| One name per thing | A word means the same thing in every doc |
| Short sentences | One point per sentence, with conditions first |
| Numbers with sources | A number instead of an adjective, and a source for every number that states a fact |
| Shared status marks | ✅ 🚧 🟨 ⬜ ❌ mean the same in every doc |

Each doc has its own style. For example, GOALS is a short intro and one table, and PHILOSOPHY is one screen: a short preamble, one line per principle, and a tie-break.

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
| Decision records (ADRs) | DESIGNS.md holds each decision in one line, with the option it beat and its reason. |
| Standard texts (LICENSE, CODE_OF_CONDUCT) | They need a choice of a standard text, not a discussion. |
| Scripts that check the docs, such as links or blank lines | The skill's job is the conversation. The agent keeps links and blank lines right while it writes. |
