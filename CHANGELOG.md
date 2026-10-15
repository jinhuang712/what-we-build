# Changelog

## Unreleased

### Sessions

- `/what-we-build revisit` is removed. The skill drafts a doc set and resumes it. A folder with docs but no marks starts a new project that builds on those docs.
- The placement test sends a feature the project will not build to FEATURES.md → *Not planned*, as the rule on reasons already said, instead of to DESIGNS.md.
- The draft step starts from the guide's skeleton and style, and names the wording rules.
- SKILL.md lists every doc guide by name, with a link, instead of a path pattern and one example.
- Each failure from a real session sits beside the rule it backs, as that rule's reason. The separate list of lessons, which repeated those rules, is gone.
- The docs come in a new order: PROPOSAL → PHILOSOPHY → DESIGNS → GOALS → FEATURES → ROADMAP → README. The design comes right after the philosophy, because the design guides the features.
- TODO.md and CHANGELOG.md are recommended for every project, and created as soon as the doc set is agreed.
- The placement test sends a stance that steers the whole project to PHILOSOPHY.md. A rule that steers only how the project is built goes to DESIGNS.md.

### Doc guides

- The guides teach instead of ordering: each rule gives its reason, and no rule sets a count to meet. The PHILOSOPHY guide is the first rewritten this way.
- The proposal guide teaches the case from the pain: pain points, then what we want and don't want, then the idea. The agent talks the case through with the user before writing. The three lists are prose, not tables, and measured results stay in GOALS.
- The rules give reasons instead of counts: how many questions to batch, how long a roadmap row, a sentence or a noun cluster may be, and how many negations a sentence may hold.
- The philosophy comes from questions. The agent asks the questions the project must take a stance on, and each stance comes from the user's answer, not from a list of ready-made principles. The page answers each question with a stance and its reasoning, then holds the deeper thinking in *Reflections*.
- The philosophy is where the project thinks. The agent keeps asking why until an answer reaches something about people or the world. Then it looks for books and papers on the same question, both those that agree and those that disagree, and quotes their checked words under the stance they test. Each stance is argued in full, and the page has no length limit: the bold lines carry the short form.
- Each design decision gets its own section, `## Decision: <the choice> — YYYY-MM-DD`, with room for prose, a list or a table of the options.
- The design guide asks how the design fails, and lists failure among the areas.
- The skeletons keep a blank line around every block, so a doc copied from them no longer joins two lines or turns a line into a table row.
- Each doc's form lives in its guide. The style table in the wording rules, which had drifted from the guides, is gone.
- Every skeleton heading stays, with "None yet" when it has nothing to hold. No heading is marked optional.
- The decision records guide is removed. An ADR found in the folder maps to DESIGNS.md.
- The CLI.md and AGENTS.md guides are removed. A command reference copies the program, and an agent file holds commands the code already shows.
- Examples follow the rules they teach: the FEATURES setting gives its reason, the PHILOSOPHY principle names its refusal, and the history example says why.
- A *Later* item that gets a milestone becomes a planned feature, and the roadmap schedules it.
- FEATURES and DESIGNS open with a TL;DR: an outline of the whole doc, one small table per group. FEATURES gives each capability its own row, with its feature and its status. The details follow in the same order, a `##` heading per group and a `###` per item, and are written to scan: a lead sentence, then short lines, tables, small diagrams or short snippets.
- DESIGNS holds no status. A principle the code does not hold yet is still the design, and the gap is tracked in FEATURES, TODO or GOALS.

### Wording

- The blank-line rule says what a missing blank line breaks.
- Five rules are removed: write in your default voice, three layers per section, the format by the shape of the data, one clause per decision, and the story in git.

### Checks

- `blank_lines.py` and `check_links.py` are removed, so the skill is Markdown only. The agent keeps links and blank lines right while it writes.

### This repo's docs

- The README points to the roadmap for status, instead of a copy of the version and progress that had gone stale.
- ROADMAP's question reads "When, and how far along?" in every doc, as in SKILL.md.
- The proposal says "one sitting" for goal G1, as GOALS.md does.
- An audit of the repo's own docs against the skill's rules fixed most lines that broke a rule. Conflicts that need the owner's decision stay open.
- DESIGNS.md holds each decision in its own dated section, and records the new doc order as a decision. Goal G4 counts those sections, and stays open until someone measures it again.

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
