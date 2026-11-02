# Changelog

## Unreleased

### Sessions

- The skill manages a project's context over its whole life, not only its founding docs.
- The skill starts from an idea, from running code with no docs or from messy docs.
- A working protocol takes every doc through one loop from discussion to commit.
- No doc is committed before the user approves it.
- The agent re-reads the whole doc before any edit, even of one word.
- Before it changes a fact, the agent reads the doc that owns it.
- A decision is written down when it is made.
- A finding that cannot be handled now goes to TODO.md at once.
- When the docs and the code disagree, the agent asks the user instead of picking a side.
- The agent goes through the project's AGENTS.md with the user and decides with them what it holds.
- The agent leaves the outcome open until it has discussed it with the user.
- The agent recommends that the project's AGENTS.md hold the work rules, so they reach every sitting.
- The agent tracks where the project stands by scanning TODO, ROADMAP and GOALS.
- After a change the agent checks only the rules it touched, and it checks the goals only at a checkpoint or a release.
- When every change is committed, a resume reports where the project stands and what may have drifted since each doc's last commit.
- A commit records the user's approval, so no doc carries a mark any more.
- A link points only to what its doc rests on, and PHILOSOPHY and CHANGELOG link to nothing.
- FEATURES, ROADMAP and GOALS open with a summary tree that gives each entry its status and a short description.
- A feature that does several things splits into parts such as F1.1.
- Each roadmap item has its own status.
- A threshold keeps every doc within one Claude Code read, in place of the count of core doc lines.
- The agent is a thinking partner that brings its own ideas and challenges the user's.
- No doc holds a code chunk.
- The default layout puts the reasons at the root.
- `specs/` holds how each part works, and `plan/` holds the goals, the roadmap and the todo list.
- Before, every doc sat at the root.
- SKILL.md is half as long, without the session stories.
- The wording rules move into SKILL.md, and `references/wording.md` is gone.

### Doc guides

- Every guide is rewritten.
- New guides: `specs/`, `specs/decisions/` and `specs/ARCHITECTURE.md`.
- The UIUX guide is gone, because UIUX is now a spec.
- Decisions move out of DESIGNS and FEATURES into `specs/decisions/`.
- PHILOSOPHY drops *Reflections* and the tie-break.
- An open question lives in TODO.md as a `DISCUSSION`, and ROADMAP no longer holds one or a *Waiting for design* list.
- PROPOSAL no longer assumes a pain: *Pain points* sits under *Why it should exist* and is written only when there are pains.
- PROPOSAL gives each pain its own section, in whatever shape shows its evidence.
- FEATURES opens with *Summary* instead of *TL;DR*.
- GOALS holds six kinds of goal, each in its own section.
- GOALS holds only the effects the skill must have, and each rule lives in its own home.
- Each goal says when it is checked, at a checkpoint or a release.
- Every measure, benchmark and comparison writes its formula in a code block.
- A constraint is a condition the product must always meet, and a rule for how the work is done stays out of GOALS.
- Every goal in the skeleton names the want it serves.
- GOALS opens with a Summary, and each goal has its own section with an ID that names its kind.
- This repo's goals take the new IDs, so G6 is now T4 and G2 is a check in B1: Session quality.
- ROADMAP calls its stages checkpoints, with IDs such as CP2, so they no longer clash with the measures.
- An ID is always a link with its name, and a list of IDs replaces a range.
- Status marks move out of headings into a *Status* line, so links to a feature or a checkpoint stay stable.
- A skeleton suggests a form, and the writer changes it where the content needs another.
- Explanation is written in short paragraphs, with good use of tables, lists and diagrams.
- A paragraph is one block and a bullet is one sentence, so sentences are no longer stacked one to a line.
- SKILL.md explains each step in short paragraphs instead of a list of rules, and lists every guide in two tables.
- The guides set no counts, such as two or three stances or a page per decision.
- A CHANGELOG groups its entries by area, as its guide always said.
- CONTRIBUTING and RUNBOOK name a script instead of listing commands.
- README opens with a hero image and always has *Install* and *How to use*.
- README lists its optional sections, each with when to add it and the doc that owns it.
- ARCHITECTURE always opens with a diagram of the whole.
- New guide: INSTALL.md, for everything beyond the README's one install line.
- A command longer than two lines belongs in a script.
- PROPOSAL drops *How it works*, *Approach* and *How we know it works*, which FEATURES, DESIGNS and GOALS own.

## 0.4.0 — 2026-10-18

### Sessions

- `/what-we-build revisit` is removed. The skill drafts a doc set and resumes it. A folder with docs but no marks starts a new project that builds on those docs.
- The placement test sends a feature the project will not build to FEATURES.md → *Not planned*, as the rule on reasons already said, instead of to DESIGNS.md.
- The draft step starts from the guide's skeleton and style, and names the wording rules.
- SKILL.md lists every doc guide by name, with a link, instead of a path pattern and one example.
- Each failure from a real session sits beside the rule it backs, as that rule's reason. The separate list of lessons, which repeated those rules, is gone.
- The docs come in a new order: PROPOSAL → PHILOSOPHY → DESIGNS → GOALS → FEATURES → ROADMAP → README. The design comes right after the philosophy, because the design guides the features.
- TODO.md and CHANGELOG.md are recommended for every project, and created as soon as the doc set is agreed.
- The placement test sends a stance that steers the whole project to PHILOSOPHY.md. A rule that steers only how the project is built goes to DESIGNS.md.
- The placement test sends a decision that concerns one feature to FEATURES.md, beside that feature, and an open design question to ROADMAP.md, or to TODO.md until the roadmap is drafted. A fact goes to DESIGNS.md when it is a design principle, or a decision that spans the project.
- The agent pushes back with its reason and keeps making the case until the user decides, instead of once. Once the user rejects a point, the agent drops it, and raises it again only with a new fact.
- The agent explains each choice in plain words, with a concrete case or a real sample, before asking, and ties each option to the case where it matters.
- When the user brings a list of their own, the agent says what it would add and what it doubts before adopting it.
- The agent draws a choice with several moving parts before asking about it, and parks a point that needs design the project is not ready for in TODO.md, so the current doc can close. The point moves to ROADMAP.md once that doc is drafted.
- When the user points out one wrong word or row, the agent re-reads the whole doc and fixes every place the idea appears.

### Doc guides

- The guides teach instead of ordering: each rule gives its reason, and no rule sets a count to meet. The PHILOSOPHY guide is the first rewritten this way.
- The proposal guide teaches the case from the pain: pain points first, then the shift that lets them be eased now, the idea, and what we want and don't want. The wants describe needs, not one answer per pain. The agent talks the case through with the user before writing. The three lists are prose, not tables, measured results stay in GOALS, and the line under the title says where the state of the work lives.
- The rules give reasons instead of counts: how many questions to batch, how long a roadmap row, a sentence or a noun cluster may be, and how many negations a sentence may hold.
- The philosophy comes from questions. The agent asks the questions the project must take a stance on, and each stance comes from the user's answer, not from a list of ready-made principles. The page answers each question with a stance and its reasoning, then holds the deeper thinking in *Reflections*.
- The philosophy is where the project thinks. The agent keeps asking why until an answer reaches something about people or the world. Then it looks for books and papers on the same question, both those that agree and those that disagree, and quotes their checked words under the stance they test. Each stance is argued in full, and the page has no length limit: the bold lines carry the short form.
- The design guide teaches DESIGNS as a few principles and the decisions they drive. The page opens with the principles, numbered. Each principle asks a question of every new requirement, and lists its decisions, each named as the choice, with what it was chosen instead of and why. A decision that weighed several options keeps a table and its recorded date. A decision about one feature, open questions and failure behavior leave DESIGNS. The page ends with the order that decides when two principles collide.
- FEATURES keeps each feature's own decisions under it, and ends with a table of what happens when something fails.
- ROADMAP holds the open design questions: a design discussion before the milestone it blocks, and a table of features waiting for design.
- GOALS holds two kinds of number: goals that pass or fail, and benchmarks tracked against a reference. Every measured number says how to reproduce it, and is measured on work close to real use.
- A bold stance line in PHILOSOPHY is the user's or approved by the user. Until one is agreed, its place stays empty.
- The README points to FEATURES.md for status instead of copying it in a table.
- The glossary can give each term's name in today's code, while the code still lags the docs.
- The skeletons keep a blank line around every block, so a doc copied from them no longer joins two lines or turns a line into a table row.
- Each doc's form lives in its guide. The style table in the wording rules, which had drifted from the guides, is gone.
- Every skeleton heading stays, with "None yet" when it has nothing to hold. No heading is marked optional.
- The decision records guide is removed. An ADR found in the folder maps to DESIGNS.md.
- The CLI.md and AGENTS.md guides are removed. A command reference copies the program, and an agent file holds commands the code already shows.
- Examples follow the rules they teach: the FEATURES setting gives its reason, the PHILOSOPHY principle names its refusal, and the history example says why.
- A *Later* item that gets a milestone becomes a planned feature, and the roadmap schedules it.
- FEATURES opens with a TL;DR: an outline of the whole doc, one small table per group. It gives each capability its own row, with its feature and its status. The details follow in the same order, a `##` heading per group and a `###` per item, and are written to scan: a lead sentence, then short lines, tables, small diagrams or short snippets.
- DESIGNS holds no status. A principle the code does not hold yet is still the design, and the gap is tracked in FEATURES, TODO or GOALS.

### Wording

- The blank-line rule says what a missing blank line breaks.
- Five rules are removed: write in your default voice, three layers per section, the format by the shape of the data, one clause per decision, and the story in git.
- A long doc opens so the reader sees all of it: a TL;DR outline, or the few points it is built around.
- A doc describes the project in its own terms, not as a version of another project.

### Checks

- `blank_lines.py` and `check_links.py` are removed, so the skill is Markdown only. The agent keeps links and blank lines right while it writes.

### This repo's docs

- The README points to the roadmap for status, instead of a copy of the version and progress that had gone stale.
- ROADMAP's question reads "When, and how far along?" in every doc, as in SKILL.md.
- The proposal says "one sitting" for goal G1, as GOALS.md does.
- An audit of the repo's own docs against the skill's rules fixed most lines that broke a rule. Conflicts that need the owner's decision stay open.
- DESIGNS.md holds each decision in its own dated section, and records the new doc order as a decision. Goal G4 now reads every decision for the option it beat and its reason, and stays open until this repo's docs take the forms of 2026-10-17 (ROADMAP.md → M2.5).
- FEATURES.md lists the new conversation rules and doc forms.

## 0.3.0 — 2026-10-13

The second revisit of this repo found 33 conflicts between its docs and the skill. Each one got a cause, and the causes changed the skill.

### Sessions

- When every doc is drafted, as after a revisit, the skill asks whether you want to approve them or revisit them again, instead of offering to resume.
- A revisit gives each conflict its cause, so you see whether the doc or the skill should change.
- Goals measured during a revisit are measured by a reader who did not write the change.
- The revisit audit looks for principles that pick no side.

### Doc guides

- Each kind of doc has its own guide file, so a session reads only the guide for the doc it is working on.
- Goals name the want they serve and where they were measured.
- Status marks mean the same in every doc: ✅ 🚧 🟨 ⬜ ❌.
- Progress, such as "not yet used on a new project", lives only in the roadmap.
- A milestone can be a proven state, not only a usable one.
- Decisions start with "Decided" and a date, so they can be counted, and name the option they beat.
- The philosophy fits on one screen: a short preamble, one line per principle that picks a side and refuses one thing, and a tie-break.
- The design doc holds design principles grouped by area, each with its cost and a rule that shows it holds, then the big decisions and the open questions. It has no map of the code and no section per feature.
- Every example in the guides is made up for the skill, or taken from this repo.
- Optional skeleton sections are marked, and the others say "None yet" rather than disappear.

### Wording

- A number in an illustrative scene may be invented. A number that states a fact needs a source.
- Claims about behavior, such as a command name, are checked or marked "not yet verified".

### Checks

- `blank_lines.py` stops before writing when a non-blank line would change, even when Python runs with `-O`.

## 0.2.0 — 2026-10-13

The first revisit of this repo with the skill itself. What it found changed the skill.

- A session is a conversation, not a form. The agent discusses, brainstorms or asks for a decision, depending on where the user is. Each doc guide lists the points to explore, with a brainstorm to open the doc.
- Every doc guide now opens with what the doc is for, where it sits in a session and which facts belong in it. It names what to push back on, gives guidelines with their reasons, and shows weak and strong examples. SKILL.md keeps the flow and points to the guides.
- New rules between docs: each doc reads on its own, the owner changes first, reasons have homes, and a doc that restates the code is a cache.
- Formats follow the shape of the data in every doc, even when the same records appear elsewhere.
- Goals take a method column, and a decision is recorded only when it is hard to reverse, surprising and a real trade-off.
- Any edit sets a doc's mark back to `drafted`.
- The skill no longer defines how a product should feel. Each doc has a style, meaning its form, and the agent writes in its default voice.
- The revisit audit checks for thin sections, numbers with no source, and text that restates the code. It ends with a changelog entry.
- The lessons from real sessions are phrased as the target behavior, each with the failure that taught it.

## 0.1.0 — 2026-10-12

The first release.

- `/what-we-build` drafts a new project's founding docs through a conversation, one decision at a time: PROPOSAL, PHILOSOPHY, GOALS, FEATURES, DESIGNS, ROADMAP and README, plus optional docs when the project needs them.
- `/what-we-build resume` continues a session from the marks on each doc.
- `/what-we-build revisit` cleans a doc set that overlaps, sprawls or drifted.
- Two checks: `check_links.py` for broken links and anchors, `blank_lines.py` for blank lines around blocks.
