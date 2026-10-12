<!-- what-we-build: drafted 2026-10-12 -->

# Features

Status: ✅ built · 🚧 built, with the gap named in its section · ⬜ planned.

## F1 — New project: talk it through 🚧

The user types `/what-we-build` in a project folder. The skill turns the user's idea into the founding docs through a conversation.

| Step | What happens |
|---|---|
| Frame | The skill asks for the idea in one or two sentences and who it is for. It reports what the folder already holds. |
| Doc set | It recommends the 7 core docs plus the optional ones that fit. The user confirms. |
| Each doc | It names the doc and its question, carries forward what earlier docs settled, asks the key questions one decision at a time with a recommendation, pushes back once on what does not fit, drafts the file, and asks for approval. |
| Close | It runs the checks and lists each doc with its status and the questions the user still owns. |

Order: PROPOSAL → PHILOSOPHY → GOALS → FEATURES → DESIGNS → ROADMAP → README. Optional docs join where they fit.

Gap: not yet used on a real project.

## F2 — Resume 🚧

Each drafted doc carries a mark on its first line: `<!-- what-we-build: drafted YYYY-MM-DD -->`, which becomes `approved` when the user approves. `/what-we-build resume` reads the marks, reports where the session stopped, and continues at the first doc that is not approved.

Gap: not yet used on a real project.

## F3 — Revisit 🚧

`/what-we-build revisit` cleans a doc set that overlaps, sprawls or drifted: audit, agree on roles with the user, rewrite, verify against the old version, and let the user review before anything is committed.

Gap: the procedure was used by hand on one project before the skill existed. It has not run as the skill.

## F4 — The doc set ✅

| Kind | Docs |
|---|---|
| Core | PROPOSAL, PHILOSOPHY, GOALS, FEATURES, DESIGNS, ROADMAP, README |
| Optional | UIUX, CLI, GLOSSARY, AGENTS, CHANGELOG, TODO, CONTRIBUTING, SECURITY, RUNBOOK, decision records |

For each doc the skill knows the question it answers, what it owns and leaves out, its voice, the questions to ask, a skeleton and the signs that it is done. It maps other common names to the set: PRD, vision document, PR/FAQ, ARCHITECTURE.md, ADR, RFC, OKRs, non-goals, backlog.

## F5 — Wording rules ✅

Plain, precise English: one name per thing, short sentences, conditions first, active voice, format by the shape of the data, numbers instead of adjectives, and history as one dated clause. Each doc has its own voice.

## F6 — Checks ✅

| Command | What it does |
|---|---|
| `python3 scripts/check_links.py FILE.md ...` | Reports relative links and `#anchors` that do not resolve. Exits 1 when one is broken. |
| `python3 scripts/blank_lines.py FILE.md ...` | Puts one blank line around headings, tables, lists and code fences. Stops when any other line would change. |

## Later, if needed

| Idea | Note |
|---|---|
| Place one fact | `/what-we-build place "<fact>"`: run the placement test on one new fact and edit the doc that owns it |
| Evals | Test prompts run with and without the skill, scored, to show what it changes |
| Wording rules in other languages | One file per language, written in that language, not translated |

## Not planned

| Not this | Why |
|---|---|
| Starting on its own | A session takes the user's attention. It starts on purpose. |
| Drafting without a conversation | Text nobody decided is the problem the skill exists to solve. |
| User manuals (tutorials, how-to guides, API references) | They answer other questions, after the founding docs exist. |
| Standard texts (LICENSE, CODE_OF_CONDUCT) | They need a choice of a standard text, not a discussion. |
