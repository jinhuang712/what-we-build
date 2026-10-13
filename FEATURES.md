<!-- what-we-build: drafted 2026-10-13 -->

# Features

What what-we-build does today, and what it will and won't do. Each feature is described from the user's side: what you type, what you see, what you decide.

Status: ✅ built · 🚧 built, with the gap named in its section · ⬜ planned.

## F1 — New project: talk it through 🚧

A session turns an idea into the founding documents of a project. You bring one or two sentences. The skill talks each document through with you until its key points are clear, then writes it down. Some points need discussion, some a brainstorm, and some a clear choice. You stay in charge throughout: every choice comes with a recommendation, and nothing is written before you agree.

| Stage | What you do | What you get |
|---|---|---|
| Frame | Describe the idea and who it is for | A one-line summary of what the folder already holds |
| Doc set | Confirm or change the recommended docs | The 7 core docs, plus the optional ones the project needs |
| Each doc | Talk each point through: discuss it, brainstorm it, or pick from options | A recommendation with its reason whenever a choice is ready |
| Each doc | Agree on the doc's key points | The doc, written and marked `drafted` |
| Each doc | Approve it, or ask for changes | The mark becomes `approved` |
| Close | Read the summary | Each doc's status, and the questions you still own |

The docs come in order: PROPOSAL → PHILOSOPHY → GOALS → FEATURES → DESIGNS → ROADMAP → README. Each one builds on the ones before it, so you never answer the same question twice.

Gap: not yet used on a new project.

## F2 — Resume 🚧

A session can stop at any point and pick up later. Each drafted doc carries a mark on its first line, invisible when rendered:

```markdown
<!-- what-we-build: drafted 2026-10-13 -->
```

The mark becomes `approved` when you approve the doc, and goes back to `drafted` whenever the doc is edited again. `/what-we-build resume` reads the marks, tells you where the session stopped, and continues at the first doc that is not approved.

Gap: not yet used on a new project.

## F3 — Revisit 🚧

`/what-we-build revisit` cleans up a doc set that overlaps, sprawls, reads thin or drifted from the code. It audits every doc, agrees each doc's role with you, rewrites, checks the result against the old version, and shows you the changes before anything is committed.

| Stage | What you get |
|---|---|
| Audit | Tables of facts written in more than one place, thin sections, numbers with no source, and stale claims |
| Roles | Each doc's question and boundaries, for you to confirm |
| Rewrite | The docs, rewritten one at a time |
| Verify | Lost facts, broken links and unsupported "met" claims, checked |
| Review | The changes, for you to read before any commit |

Gap: run once, on this repo (2026-10-13). Not yet run on another project.

## F4 — The doc set ✅

The skill knows 17 kinds of document: 7 core, and 10 optional that join only when the project needs them.

| Kind | Docs |
|---|---|
| Core | PROPOSAL, PHILOSOPHY, GOALS, FEATURES, DESIGNS, ROADMAP, README |
| Optional | UIUX, CLI, GLOSSARY, AGENTS, CHANGELOG, TODO, CONTRIBUTING, SECURITY, RUNBOOK, decision records |

For each kind, the skill carries a guide: what the doc is for, where it sits in a session, which facts belong in it, what to push back on, guidelines with their reasons, weak and strong examples, the points to explore, a skeleton and the signs that it is done. It also maps other common names to the set, for example a PRD to FEATURES, or an ARCHITECTURE.md to DESIGNS.

## F5 — Wording rules ✅

The skill writes plain, precise English, so a reader finds a fact fast and understands it the first time.

- Each section opens with what it is and why it matters, then guidelines, then the specifics.
- One name per thing, short sentences, conditions first, active voice.
- A table for records, a list for parallel items, sentences for reasoning.
- Numbers instead of adjectives, each with a source.
- History as one dated clause per decision.

Each doc has its own style. For example, GOALS is a short intro and one table, and PHILOSOPHY is short prose with one section per principle.

## F6 — Checks ✅

Two scripts check a doc set. Both run on Python's standard library, with nothing to install.

| Command | What it does |
|---|---|
| `python3 scripts/check_links.py FILE.md ...` | Reports relative links and `#anchors` that do not resolve. Exits 1 when one is broken. |
| `python3 scripts/blank_lines.py FILE.md ...` | Puts one blank line around headings, tables, lists and code fences. Stops when any other line would change. |

## Later, if needed

| Idea | Note |
|---|---|
| Place one fact | `/what-we-build place "<fact>"` runs the placement test on one new fact and edits the doc that owns it |
| Evals | Test prompts run with and without the skill, scored, to show what it changes |
| Wording rules in other languages | One file per language, written in that language, not translated |

## Not planned

| Not this | Why |
|---|---|
| Starting on its own | A session needs the user's full attention, so it starts when the user types it. |
| Drafting without a conversation | Text nobody decided is the problem the skill exists to solve. |
| A fixed questionnaire or template | Fixed questions fill forms. Decisions come from a conversation. |
| More docs than the project needs | Optional docs join only when they have a job. A doc with no job is a doc nobody keeps true. |
| Choosing how a product should feel | That is the user's call. The skill records the user's words when they bring them. |
| User manuals (tutorials, how-to guides, API references) | They answer other questions, after the founding docs exist. |
| Standard texts (LICENSE, CODE_OF_CONDUCT) | They need a choice of a standard text, not a discussion. |
