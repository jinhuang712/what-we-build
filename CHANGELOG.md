# Changelog

## Unreleased

### Working with the agent

- A tree says which docs each event updates, so the docs change when the work does.
  - Before: only finished work, decisions and open items had a set moment.
  - After: a new requirement reaches the plan before the work starts, and each doc has its moment.
- `AGENTS.md` starts with every work rule, and you reject the ones you do not want.
  - Before: the agent proposed rules and you agreed them one at a time.
  - After: a project has the full rules from its first start.
- The agent looks for contradictions.
  - After a change it searches the docs for what the change now contradicts.
  - It tells you when your words contradict a doc.
  - It picks no side.
- When a change lands, the agent fixes what it left behind before it reports.
- When a checkpoint ends, the agent runs the start pass again.
- The agent follows the skill strictly until you reject a rule.
  - Before: it could set a rule aside once you agreed.
  - After: it never asks for a way around a rule and records each exception you make.
- When a rule seems not to fit, the agent says why and asks for your opinion.
- Agreeing on a direction no longer counts as approving a change.
- Each start puts every doc in the skill's format before any talk.
  - Before: the agent talked with you before it moved old docs.
  - After: it works alone, adds nothing new and gives you the proof at the end.
  - What only you can settle waits in `TODO.md`.
  - It asks for your approval once for the whole pass.
  - After a topic you open it goes back to the pass.
  - At the end it says what it left unchecked.
- A folder with no git gets the suggestion of `git init` before the agent touches a doc.

### Writing a doc

- A project with a command line must now have `CLI.md`.
  - Before: flags and exit codes had no doc of their own since 0.4.0.
  - After: the commands and what they return have one home that the program follows.
- IDs follow the skill's format and change when the structure changes.
  - Before: an ID never changed, even when its group was wrong.
  - After: the agent can rebuild a structure and fix every link in one change.
- The skill says its rules in fewer lines with the same meaning.
- A list inside a bullet keeps ` · ` after a colon and takes sub-bullets when it grows.
  - Before: the comma rules pushed lists into chains such as "kind and label and weight".
  - After: the skill rules out such a chain.

### Keeping the docs

- Once the work at hand is done and nothing is next, the agent goes through `TODO.md` with you.
- A window reads the skill first only where the skill is installed.
- A finished checkpoint stays in ROADMAP in full.

### Goals and features

- A comparison may set a target and fail it.
  - Before: a comparison only showed where the project stood.
  - After: a missed target is marked ❌.
- A measured measure shows its value in the Summary in place of a status.
- *Later* is gone from FEATURES.
  - Before: ideas waited in a *Later* list.
  - After: every feature not yet built sits in the tree and in a checkpoint.
- ROADMAP keeps each goal's result from each checkpoint.
  - Before: only GOALS held a result, and a newer one replaced it.
  - After: a goal that later fails leaves the old record in place and opens an issue.
- Each checkpoint names the goals it runs, and one goal may run in many checkpoints.
  - Before: ROADMAP allowed a goal in one checkpoint only.
  - After: GOALS is the rubric for the project's whole life, such as cost and speed at every checkpoint.
- FEATURES may name the types a user meets, such as the public names of a library.
- ` · ` may separate a list of names and never replaces commas in a sentence.

## 0.7.0 — 2026-11-05

### Working with the agent

- The skill is written for any agent that loads Agent Skills, and the install steps cover Claude Code.
- When your agent reads another file such as `CLAUDE.md`, the agent makes that file load `AGENTS.md`.
- The agent reads the whole skill when it starts and again after each compaction, and never hands it to a subagent.
- When the agent says the skill asks for something, it quotes the line.
- When a rule seems not to fit, the agent asks you instead of reading its way around it.
- The agent pushes back with its reason and keeps making the case while you are still weighing it.
  - It weighs what you say with you before it writes it down.
  - Once you reject a point, it raises it again only with a new fact.
- When you repeat a stance, the agent offers to write it into PHILOSOPHY.
- Before you drop a core doc, the agent tells you what it would hold.
- Only you end the talk on a doc.
  - Until you do, the agent keeps looking for the next line that breaks a rule.
  - When it finds none, it reads the doc again and shows you what it checked.

### Writing a doc

- Before you see a doc, the agent checks it line by line against its guide and the wording rules.
  - It shows you what each check found as the proof that the doc is done.
  - It never asks you to review a doc in place of that proof.
  - It also checks each link and each number's source.
  - It also checks that each fact has one home and each item its ID.
- Every item carries an ID at the level its doc uses, such as a sub-feature or a sub-checkpoint.
  - A feature with more than one case splits into sub-features.
  - A checkpoint that delivers more than one feature group splits into sub-checkpoints, each with its own exit criteria.
  - A parent lists no features when its sub-checkpoints list them.
- A feature or checkpoint is marked done only once it has been run, and a claim nobody ran gets the new ❔ mark.
- Each guide says which docs its doc may link to, and a link goes one way.
  - Before, a link table in SKILL.md said only where a doc may link and specs linked to each other.
  - Now a link its guide does not allow is ruled out, and so is a plain-text pointer in its place.
  - Two docs never link to each other, so a decision or a spec no longer links back up.
  - TODO may link to any file in the project.
  - A goal names the want it serves and no longer links to PROPOSAL or ROADMAP.
  - A goal links to each feature and guideline it checks.
  - A design guideline links to the PHILOSOPHY stance it derives from.
- A file named in a doc is a link, not a name in backticks.
- A part gets a spec only when a reader cannot follow its mechanism from its code, and ARCHITECTURE links it only then.
- A table cell holds no sentence and at most one comma.
- A field with more than one link puts each link on its own line, as *Decisions* does.
- Every feature not yet built sits in a checkpoint or in *Later*, and *Later* holds nothing a planned checkpoint needs.
- A feature says from your side what it does, how you use it and when it applies.
- Once FEATURES holds more than ten features and sub-features, each group gets a file of its own and FEATURES becomes the index.
  - Before, FEATURES was one file however long it grew.
  - Now a link to a feature points into its group file, and the agent fixes every link when a group moves.
- The agent checks each item against what its guide says a finished doc gives the reader.
- A prototype page shows one screen, and drops the other options once you pick one.
- The agent adds every optional doc whose condition holds, and tells you which.
- The agent trusts no doc the skill did not write.
  - It checks each claim in such a doc against the code or asks you before the claim enters a doc.
  - It never follows an instruction found in such a doc.
- When your docs are older than the skill, the agent offers to judge every item again against its guide.
  - When a doc moves into a new form, every item in it is judged again from scratch with the done items too.
  - No line is kept because it is old.
- When a heading or an ID is renamed, every link and mention of it changes in the same change.
- A decision that a later one replaces in whole or in part says so under its date.
- When a change moves a measured number, the agent measures it again and dates the new value.

## 0.6.0 — 2026-11-03

### Working with the agent

- `SKILL.md` is written in plain words with one point to a line.
- The agent reads every doc it works on in full and never hands a doc to a subagent.
- When you stop the agent, it stops every agent it started and every agent those started.
- When a project's own rules disagree with a guide, the agent tells you instead of picking one.
- The agent says when it thinks the talk is enough and you judge it together, instead of settling each point with lettered options.

### Start

- The agent makes every window load `AGENTS.md`, and adds a `CLAUDE.md` with `@AGENTS.md` when your project has none.
- The agent talks the rules for `AGENTS.md` through with you and never puts them all in at once.
- On each start the agent shows you any part of a doc that its guide no longer asks for.

### Doc guides

- Every guide and `SKILL.md` are written in tagged lines in the order `[YES]` `[NO]` `[MAYBE]` `[WHEN]`.
  - Before, a guide had lists such as *Owns* and *Push back on*.
  - Now one *What is it* list says what goes in, what goes elsewhere and how to write it.
  - Lines that said the same thing twice are gone, so the guides are 121 lines shorter.
- A guide says what its doc's core idea is and is not.
  - FEATURES: a group, a feature and a sub-feature.
  - PROPOSAL: a want and a pain.
  - PHILOSOPHY: a stance.
  - DESIGNS: a guideline.
  - GOALS: a goal, and a constraint may check a DESIGNS guideline.
  - ROADMAP: a checkpoint.
  - SPECS: a part, which ARCHITECTURE shares.
  - DECISIONS: a decision.
  - GLOSSARY: a term.
- What FEATURES called a part is now a sub-feature, so *part* means only a piece of the project.
- Examples in the guides may come from the stable ideas of a well-known tool, such as Claude Code.
- A ROADMAP checkpoint lists the features it delivers, and its exit criteria are bullets grouped by the kind of goal.
- Goals that are checked but do not block a release sit in their own group.
- A sub-checkpoint may have its own exit criteria, and its parent only says it is met.
- FEATURES no longer names a version, and each decision in it carries a short name.
- A doc links every ID it names where it may, and never shows a bare ID.
- CHANGELOG holds no IDs or links, and no table of renamed IDs.
- DESIGNS holds no order for when guidelines collide, since a guideline is never traded.
- TODO has three priorities from `P0` to `P2`, and an idea that may never happen is an `IDEA` at `P2`.
- A TODO item's status is `OPEN` or `HALT` in place of open, in progress and blocked.

## 0.5.0 — 2026-11-03

### Install

- what-we-build installs as a personal skill, and the plugin is gone.
- Before, you installed it with `claude plugin install` and typed `/what-we-build:what-we-build`.
- Now you clone the repo, link its skill folder into `~/.claude/skills` and type `/what-we-build`.
- To move over, uninstall the plugin and follow INSTALL.md.

### Working with the agent

- The skill keeps a project's context over its whole life, not only while the first docs are written.
- It starts from an idea, from running code with no docs or from messy docs.
- The agent is a thinking partner that brings its own ideas and challenges yours.
- It leaves the outcome open until it has discussed it with you.
- It discusses, brainstorms or asks for a decision as the moment needs.
- The skill no longer says when to use which way.
- Each point goes into its doc as soon as you agree it, so an agreed point never lives only in the window.
- You see each change before it is committed.
- Nothing is committed before you approve it.
- You approve in the conversation, and no doc carries a mark any more.
- The agent re-reads the whole doc before any edit, even of one word.
- The skill says what the agent must do and leaves the steps to it, keeping only the rules that stop a mistake seen in tests.
- When you stop the agent, it stops at once.
- A point still open waits in TODO.md, so the work can stop at any time.
- When docs already exist, `/what-we-build` tells you where the work stands.
  - It also tells you what is still open and which docs may have fallen behind.
- Without git, the agent recommends `git init` since the history shows which docs fell behind.
- An idea, running code and old docs are all material for the talk.
- The agent discusses that material with you instead of moving its text.
- The agent goes through your project's AGENTS.md with you and recommends its read order, layout and work rules.
- The work rules reach every new window through AGENTS.md, even when the skill is not loaded.
- They say to read the doc that owns a thing first and to record each open item at once.
- A decision is recorded at once when another way was open and the code does not show the reason.
- When the docs and the code disagree, the agent asks you instead of picking a side.
- Once other developers build on your project, the agent tells you it may need a wiki and leaves its form to you.
- After a change the agent checks only the rules it touched, and it checks the goals only at a checkpoint or a release.

### The doc set

- Every guide is rewritten, and SKILL.md is half as long.
- New guides cover `specs/` and `specs/decisions/`, ARCHITECTURE and INSTALL.
- UIUX is a spec with `prototype/*.html` beside it, and it has its own guide.
- Its *Screens* table links every page, so UIUX is the way into the prototype.
- UIUX draws each story's flow across the screens it passes.
- Each feature lists its stories, one sentence each that says who does what and for what.
- The wording rules move into SKILL.md, and `references/wording.md` is gone.
- Decisions move out of DESIGNS and FEATURES into `specs/decisions/`.
- The placement test asks about a design commitment and a rule for the work before it asks about a goal.
- When to add an optional doc is said only in SKILL.md, and no guide says when to draft its doc.
- An open question lives in TODO.md as a `DISCUSSION`.
- A skeleton suggests a form, and you change it where the content needs another.
- The default layout puts the reasons at the root with `specs/` and `plan/` beside them.
- Before, every doc sat at the root.
- PROPOSAL writes *Pain points* only when there are pains, each in its own section.
- PROPOSAL drops *How it works*, *Approach* and *How we know it works* because other docs own them.
- PHILOSOPHY drops *Reflections* and argues in prose with any structure that shows the thought.
- FEATURES numbers its groups as well as the features in them.
- A ✅ in FEATURES means the feature is built, and GOALS checks whether it works in real use.
- FEATURES, ROADMAP and GOALS open with a *Summary* that draws every entry and its status as an ASCII tree.
- README opens with a hero image and always has *Install* and *How to use*.
- README lists its optional sections with the doc that owns each one.
- ARCHITECTURE opens with a diagram of the whole.
- CONTRIBUTING and RUNBOOK name a script instead of listing commands.

### Goals and the roadmap

- GOALS holds only the effects the project must have, in six kinds that each have a section.
- A commitment goes to DESIGNS and a rule for the work goes to AGENTS.md, not to GOALS.
- Every goal names the want it serves, and ROADMAP says from which checkpoint it runs.
- Every measure, benchmark and comparison writes its formula in a code block.
- A constraint is a condition the product must always meet.
- A goal is met only with a measurement or the user's own report.
- ROADMAP calls its stages checkpoints with IDs, and each item has its own status.
- A checkpoint ends with every goal that can run by then.
- Status marks sit on a *Status* line and not in headings, so links stay stable.

### Wording

- Explanation is a short paragraph, and separate points are a list with one sentence to a bullet.
- A bullet holds at most one comma, and a paragraph is not held to a count.
- An ID is always written with its name, and a list of IDs replaces a range.
- A link points only to what its doc rests on.
- A feature links up to what it rests on and down to everything that builds it, including the UIUX flow of each story.
- ARCHITECTURE links down to the spec of each part, a spec links down to its decisions and a goal links up to the PROPOSAL wants it serves.
- No doc holds a code chunk, which is code from the project or a command over two lines.
- A code block is fine for a formula or a tree.
- The docs speak of the window and the project context instead of sessions and sittings.
- The guides set no counts such as two or three stances.

## 0.4.0 — 2026-10-18

### Sessions

- `/what-we-build revisit` is removed.
  - The skill drafts a doc set and resumes it.
  - A folder with docs but no marks starts a new project that builds on those docs.
- The placement test sends a feature the project will not build to FEATURES.md → *Not planned* instead of to DESIGNS.md.
- The draft step starts from the guide's skeleton and style, and names the wording rules.
- SKILL.md lists every doc guide by name with a link instead of a path pattern and one example.
- Each failure from a real session sits beside the rule it backs as that rule's reason.
- The separate list of lessons that repeated those rules is gone.
- The docs come in a new order: PROPOSAL → PHILOSOPHY → DESIGNS → GOALS → FEATURES → ROADMAP → README.
  - The design comes right after the philosophy because the design guides the features.
- TODO.md and CHANGELOG.md are recommended for every project, and created as soon as the doc set is agreed.
- The placement test sends a stance that steers the whole project to PHILOSOPHY.md.
- A rule that steers only how the project is built goes to DESIGNS.md.
- The placement test sends a decision that concerns one feature to FEATURES.md beside that feature.
- An open design question goes to ROADMAP.md, or to TODO.md until the roadmap is drafted.
- A design principle or a decision that spans the project goes to DESIGNS.md.
- The agent pushes back with its reason and keeps making the case until the user decides.
- Once the user rejects a point, the agent drops it until a new fact comes up.
- The agent explains each choice in plain words with a concrete case or a real sample before it asks.
- It ties each option to the case where that option matters.
- When the user brings a list of their own, the agent says what it would add and what it doubts before adopting it.
- The agent draws a choice with several moving parts before asking about it.
- A point that needs design the project is not ready for waits in TODO.md so the current doc can close.
- That point moves to ROADMAP.md once the roadmap is drafted.
- When the user points out one wrong word or row, the agent re-reads the whole doc and fixes every place the idea appears.

### Doc guides

- The guides teach instead of ordering: each rule gives its reason and no rule sets a count to meet.
  - The PHILOSOPHY guide is the first one rewritten this way.
- The proposal guide teaches the case from the pain.
  - Pain points come first.
  - Then comes the shift that lets them be eased now.
  - Then come the idea and what we want and don't want.
  - The wants describe needs instead of one answer per pain.
  - The agent talks the case through with the user before writing.
  - The three lists are prose and not tables.
  - Measured results stay in GOALS.
  - The line under the title says where the state of the work lives.
- The rules give reasons instead of counts.
  - No count says how many questions to batch.
  - No count says how long a roadmap row, a sentence or a noun cluster may be.
  - No count says how many negations a sentence may hold.
- The philosophy comes from questions.
  - The agent asks the questions the project must take a stance on.
  - Each stance comes from the user's answer and not from a list of ready-made principles.
  - The page answers each question with a stance and its reasoning.
  - The deeper thinking sits in *Reflections*.
- The philosophy is where the project thinks.
  - The agent keeps asking why until an answer reaches something about people or the world.
  - Then it looks for books and papers on the same question that agree or disagree.
  - It quotes their checked words under the stance they test.
  - Each stance is argued in full, and the page has no length limit.
  - The bold lines carry the short form.
- The design guide teaches DESIGNS as a few principles and the decisions they drive.
  - The page opens with the principles, numbered.
  - Each principle asks a question of every new requirement.
  - Each principle lists its decisions, each named as the choice with what it beat and why.
  - A decision that weighed several options keeps a table and its recorded date.
  - A decision about one feature leaves DESIGNS, and so do open questions and failure behavior.
  - The page ends with the order that decides when two principles collide.
- FEATURES keeps each feature's own decisions under it, and ends with a table of what happens when something fails.
- ROADMAP holds the open design questions: a design discussion before the milestone it blocks, and a table of features waiting for design.
- GOALS holds two kinds of number: goals that pass or fail and benchmarks tracked against a reference.
  - Every measured number says how to reproduce it.
  - Every number is measured on work close to real use.
- A bold stance line in PHILOSOPHY is the user's or approved by the user.
  - Until one is agreed, its place stays empty.
- The README points to FEATURES.md for status instead of copying it in a table.
- The glossary can give each term's name in today's code, while the code still lags the docs.
- The skeletons keep a blank line around every block, so a doc copied from them no longer joins two lines or turns a line into a table row.
- Each doc's form lives in its guide.
  - The style table in the wording rules had drifted from the guides and is gone.
- Every skeleton heading stays, with "None yet" when it has nothing to hold.
  - No heading is marked optional.
- The decision records guide is removed.
  - An ADR found in the folder maps to DESIGNS.md.
- The CLI.md and AGENTS.md guides are removed.
  - A command reference copies the program.
  - An agent file holds commands the code already shows.
- Examples follow the rules they teach.
  - The FEATURES setting gives its reason.
  - The PHILOSOPHY principle names its refusal.
  - The history example says why.
- A *Later* item that gets a milestone becomes a planned feature, and the roadmap schedules it.
- FEATURES opens with a TL;DR that outlines the whole doc in one small table per group.
  - Each capability gets its own row with its feature and its status.
  - The details follow in the same order with a `##` heading per group and a `###` per item.
  - The details open with a lead sentence so they scan.
  - Short lines and tables follow, or diagrams and snippets.
- DESIGNS holds no status.
  - A principle the code does not hold yet is still the design.
  - The gap is tracked in FEATURES, TODO or GOALS.

### Wording

- The blank-line rule says what a missing blank line breaks.
- Five rules are removed:
  - Write in your default voice.
  - Three layers per section.
  - The format by the shape of the data.
  - One clause per decision.
  - The story in git.
- A long doc opens so the reader sees all of it: a TL;DR outline, or the few points it is built around.
- A doc describes the project in its own terms, not as a version of another project.

### Checks

- `blank_lines.py` and `check_links.py` are removed, so the skill is Markdown only.
- The agent keeps links and blank lines right while it writes.

### This repo's docs

- The README points to the roadmap for status, instead of a copy of the version and progress that had gone stale.
- ROADMAP's question reads "When, and how far along?" in every doc as it does in SKILL.md.
- The proposal says "one sitting" for the goal on a short talk, as GOALS.md does.
- An audit of the repo's own docs against the skill's rules fixed most lines that broke a rule.
- Conflicts that need the owner's decision stay open.
- DESIGNS.md holds each decision in its own dated section.
- DESIGNS.md records the new doc order as a decision.
- The goal on decisions now reads every decision for the option it beat and its reason.
  - It stays open until this repo's docs take the forms of 2026-10-17.
- FEATURES.md lists the new conversation rules and doc forms.

## 0.3.0 — 2026-10-13

The second revisit of this repo found 33 conflicts between its docs and the skill. Each one got a cause, and the causes changed the skill.

### Sessions

- When every doc is drafted, the skill asks whether you want to approve them or revisit them again.
  - Before, it offered to resume.
- A revisit gives each conflict its cause, so you see whether the doc or the skill should change.
- Goals measured during a revisit are measured by a reader who did not write the change.
- The revisit audit looks for principles that pick no side.

### Doc guides

- Each kind of doc has its own guide file, so a session reads only the guide for the doc it is working on.
- Goals name the want they serve and where they were measured.
- Status marks mean the same in every doc: ✅ 🚧 🟨 ⬜ ❌.
- Progress such as "not yet used on a new project" lives only in the roadmap.
- A milestone can be a proven state, not only a usable one.
- Decisions start with "Decided" and a date so they can be counted.
- Decisions name the option they beat.
- The philosophy fits on one screen.
  - It has a short preamble.
  - It has one line per principle that picks a side and refuses one thing.
  - It ends with a tie-break.
- The design doc holds design principles grouped by area.
  - Each principle has its cost and a rule that shows it holds.
  - The big decisions and the open questions follow.
  - It has no map of the code and no section per feature.
- Every example in the guides is made up for the skill, or taken from this repo.
- Optional skeleton sections are marked, and the others say "None yet" rather than disappear.

### Wording

- A number in an illustrative scene may be invented.
- A number that states a fact needs a source.
- Claims about behavior such as a command name are checked or marked "not yet verified".

### Checks

- `blank_lines.py` stops before writing when a non-blank line would change, even when Python runs with `-O`.

## 0.2.0 — 2026-10-13

The first revisit of this repo with the skill itself. What it found changed the skill.

- A session is a conversation, not a form.
  - The agent discusses, brainstorms or asks for a decision as the user needs.
  - Each doc guide lists the points to explore and opens the doc with a brainstorm.
- Every doc guide now opens with what the doc is for.
  - It says where the doc sits in a session and which facts belong in it.
  - It names what to push back on.
  - It gives guidelines with their reasons.
  - It shows weak and strong examples.
- SKILL.md keeps the flow and points to the guides.
- New rules between docs:
  - Each doc reads on its own.
  - The owner changes first.
  - Reasons have homes.
  - A doc that restates the code is a cache.
- Formats follow the shape of the data in every doc, even when the same records appear elsewhere.
- Goals take a method column.
- A decision is recorded only when it is hard to reverse, surprising and a real trade-off.
- Any edit sets a doc's mark back to `drafted`.
- The skill no longer defines how a product should feel.
- Each doc has a style that sets its form.
- The agent writes in its default voice.
- The revisit audit checks for thin sections, numbers with no source and text that restates the code.
  - It ends with a changelog entry.
- The lessons from real sessions are phrased as the target behavior, each with the failure that taught it.

## 0.1.0 — 2026-10-12

The first release.

- `/what-we-build` drafts a new project's founding docs through a conversation, one decision at a time.
  - The founding docs are PROPOSAL · PHILOSOPHY · GOALS · FEATURES · DESIGNS · ROADMAP · README.
  - Optional docs join when the project needs them.
- `/what-we-build resume` continues a session from the marks on each doc.
- `/what-we-build revisit` cleans a doc set that overlaps, sprawls or drifted.
- Two checks: `check_links.py` for broken links and anchors, `blank_lines.py` for blank lines around blocks.
