# The documents

This file is the guide to each document. Read a doc's entry before you start it. Each entry follows the same order:

| Part | What it gives you |
|---|---|
| Description | what the doc is for, who reads it, where it sits in a session, and which facts belong in it |
| Owns and leaves out | its boundaries, so facts land in one place |
| Push back on | the mistakes this doc invites, to name when the user makes them |
| Guidelines | how to write it well, each with its reason |
| Weak and strong | examples of the same content, written badly and well |
| Explore | the points to talk through with the user, and a brainstorm to open the doc |
| Skeleton | the headings to start from |
| Style | the doc's form |
| Done when | the signs that the doc is ready for approval |

## Contents

- Core: [PROPOSAL](#proposalmd) · [PHILOSOPHY](#philosophymd) · [GOALS](#goalsmd) · [FEATURES](#featuresmd) · [DESIGNS](#designsmd) · [ROADMAP](#roadmapmd) · [README](#readmemd)
- Optional: [UIUX](#uiuxmd) · [CLI](#climd) · [GLOSSARY](#glossarymd) · [AGENTS](#agentsmd) · [CHANGELOG](#changelogmd) · [TODO](#todomd) · [CONTRIBUTING](#contributingmd) · [SECURITY](#securitymd) · [RUNBOOK](#runbookmd) · [Decision records](#decision-records)
- [Other names you may meet](#other-names-you-may-meet)
- [Not covered](#not-covered)

---

## PROPOSAL.md

The proposal is where the project begins: the case for why it should exist at all. It names the change in the world that makes the project necessary, the pain that change causes, and the idea that answers it. A reader finishes it knowing whether the project is worth building. Engineers, a future contributor, and the user six months from now all read it to remember why.

It comes first in a session, because every other doc builds on the pain it names. A fact belongs here when it explains why the project should exist at all.

**Owns:** the shift, the pain points, the one idea that makes the project different, what we want, a sample of it working, what we don't want, who it is for, the approach, the risks, how we will know it works.

**Leaves out:** exact behavior (FEATURES), the full list of checks (GOALS, though it may quote the headline ones), status (ROADMAP), the list of docs (README).

**Push back on:** a pain point with no example, a want that answers no pain, and a "don't want" with no reason.

### Guidelines

- **Open with a scene the reader has lived,** not with a definition. A reader who recognizes the moment of pain keeps reading. A reader handed a category ("a documentation framework") decides from the label.
- **Give every pain point an example or a number.** "Context switching is hard" persuades nobody. "Every switch starts with: what was this one doing?" persuades anyone who has felt it.
- **State the idea in one sentence.** If the idea needs a paragraph, it is not one idea yet. Keep asking until it fits.
- **Answer every pain with a want.** A want that answers no pain is a feature looking for a reason.
- **Show the product working,** with one concrete sample: a conversation, a command and its output, a screen. A sample convinces where a description only claims.
- **Give every "don't want" a reason.** A refusal without a reason gets reopened by the next person who did not hear it.
- **Keep the stances short here.** The proposal states what the project refuses to become. The full list of excluded items, with reasons, lives in FEATURES.md → *Not planned*.

### Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "Developers struggle with documentation." | "You ask your agent for a README and a roadmap. Ninety seconds later you have 2,000 confident words about decisions you never made." | A scene the reader has lived |
| Pain: "Context switching is hard." | Pain: "Every switch into a session starts with the same question: what was this one doing?" | A concrete moment |
| Don't want: "Bloat." | Don't want: "A form to fill in. Templates produce answers, not decisions." | A named thing, with its reason |

### Explore

Talk these points through in the way that fits: discuss, brainstorm or decide.

**Brainstorm to open:** list the pains together, as many as come, as fast as they come. Then pick the three that hurt most, and find a real example for each.

1. What changed in the world that makes this project necessary now?
2. What hurts today? Ask for each pain point with a concrete example or a number.
3. Describe the moment the pain happens, as a scene the reader has lived. (This becomes the hook.)
4. What is the one idea that makes this different? Say it in one sentence.
5. For each pain: what should happen instead?
6. Show it working: one concrete example of the product in use (a conversation, a command and its output, a screen).
7. What must this project never become? Ask for the reason of each.
8. Who is it for? Who is the first user?
9. What is the approach, in one line per choice: platform, language, core model, what it builds on?
10. What could make it fail, and what reduces each risk?

### Skeleton

```markdown
# <Name> — Proposal

> <tagline>

Proposed <YYYY-MM-DD>. For what is built today, see ROADMAP.md.

## In short            (the hook: a scene the reader knows, then the one-line answer)
## The shift            (a before/after table)
## Pain points          (numbered, one bold line each, with an example)
## The idea             (one bold sentence; a table or diagram only if it helps)
## What we want         (table: pain → what the project does)
## How it works         (one concrete sample, a few lines, link FEATURES.md)
## What we don't want   (table of a few stances; link FEATURES.md → Not planned for the full list)
## Who it is for
## Approach
## Risks                (table: risk → mitigation)
## How we know it works (link GOALS.md)
```

### Style

Short sections, each opening with its point. Tables for comparisons. Real numbers. The proposal argues, so every section should make the case stronger.

### Done when

The hook names a moment the reader has lived. The idea fits in one sentence. The sample shows the product instead of describing it. Every pain has an example, every want answers a pain, and every "don't want" has a reason. A stranger could repeat the pitch in two sentences.

---

## PHILOSOPHY.md

The philosophy is the project's reasoning, written down so it outlasts the people who had it. It says what the project values and how that value shapes every choice. The other docs refer to it when a decision is hard: a feature is checked against its principles, and a change against its test. It is also the one doc that may teach: a reader should come away seeing the problem differently.

It comes second in a session: it draws its principles from the pain and the wants in the proposal. A fact belongs here when it is a reason that applies to many things.

**Owns:** what the core value means, three to five principles, the evidence behind them where it exists, and the test that every change must pass.

**Leaves out:** any feature, setting, screen part or technology. A principle that names a feature belongs in FEATURES, UIUX or DESIGNS.

**Push back on:** a principle that names a feature or a screen part, and a principle that would reject nothing.

### Guidelines

- **Start from the one value the project protects:** attention, trust, speed, privacy. Principles that serve no shared value read as a list of opinions.
- **Write each principle so it can reject a real, tempting feature.** A principle that rejects nothing gives no guidance when a decision is hard.
- **Name no feature, setting or screen part.** "No badges that show counts" is a screen rule for UIUX. The principle behind it ("attention is the scarce resource") is the part that belongs here.
- **Explain each principle in a short paragraph:** the belief, then why it holds. A one-line principle gets agreed with and then ignored.
- **Cite evidence only when the user knows the source, or you can verify it.** An invented citation destroys the trust the page exists to build.
- **End with the test for every change:** a few yes-or-no questions that other docs and contributors can apply.
- **Leave out how the product should feel.** That is the user's call. Record their words only when they bring them.

### Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "Sessions come first." | "Attention is the scarce resource. Information waits at the edge, and only what needs the user comes forward." | A value, not a model choice |
| "No badges that show counts." | Move it to UIUX.md. Keep the value behind it here. | A screen rule is not a principle |
| "Be simple." | "The default is the product. Each choice handed to the user is a cost." | Says what to give up |

### Explore

Talk these points through in the way that fits: discuss, brainstorm or decide. This doc usually needs the most discussion.

**Brainstorm to open:** list every belief the user holds about the problem, however small. Then keep the few that would reject a real, tempting feature.

1. What is the one value the project protects?
2. What does that value mean here, in the user's own words?
3. Which beliefs follow from it? Draft three to five, then test each one: name a tempting feature it would reject.
4. Is there research or a known idea behind the principles? Use it only when the source is known.
5. What questions should every proposed change answer?

### Skeleton

```markdown
# Philosophy

<two or three short paragraphs: what changed, what is scarce, why this project exists>

## What <the value> means
## Principles
### 1. <principle>          (a short paragraph each)
## Evidence                 (optional table: rule → source)
## The test for every change
```

### Style

Short prose, one section per principle, then the test. Paragraphs, not bullet lists: a principle needs its reasoning beside it.

### Done when

No line names a feature, each principle can reject something real, and the test is the last section, because other docs point to it.

---

## GOALS.md

GOALS.md turns the wants in the proposal into checks. A goal here is something a script, a benchmark or the user's own use can confirm or refute on a given day. It keeps the project honest: when someone claims progress, this is where the claim is tested. ROADMAP.md uses these goals as its exit criteria.

It comes third in a session: it turns the proposal's wants into numbers. A fact belongs here when it can be checked with a number.

**Owns:** goals as checks, each with an ID, a measure with a number, a method and a status.

**Leaves out:** anything vague, non-goals (FEATURES → *Not planned*), how anything works.

**Push back on:** an adjective where a number belongs, a goal with no method, and a "met" with no evidence.

### Guidelines

- **Start from the proposal's wants.** Each want gets a goal, or a note on why it cannot be measured yet.
- **Write the measure as a threshold with a unit,** because "fast" can't fail, and a goal that can't fail can't guide a decision.
- **Name the method:** who or what measures it, and how often. A goal nobody measures drifts into a wish.
- **Keep a goal without a number visibly open** ("number not set"). Leaving it out hides the gap.
- **Change a status only with evidence:** the measurement and its date. "Met" without evidence is the most expensive word in the doc.
- **Keep the goals few.** Drop a goal that would not change any decision.

### Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "Search is fast." | "A query takes < 50 ms while typing, measured by the benchmark on real history." | A number, a unit, a method |
| "Easy to set up." | "A new user makes it look right in < 1 minute, without editing a file." | Something you can watch happen |
| "Never miss a notification." | "0 missed in a week of daily use, counted by the author." | A count and a period |

### Explore

Talk these points through in the way that fits: discuss, brainstorm or decide.

**Brainstorm to open:** for each want, list every way it could be measured. Then keep the cheapest measure that would still change a decision.

1. For each want in PROPOSAL: how would we know it is true?
2. What number, measured how? Who or what measures it, and how often?
3. What is the threshold? When the user has no number yet, the goal is listed as open with "number not set".
4. What is its status today? Met only with evidence and the date it was measured.

### Skeleton

```markdown
# Goals

Each goal is a check with a number. <One or two sentences: where and how the goals are measured.>

| # | Goal | Measure | Method | Status |
|---|---|---|---|---|
| G1 | <short name> | <threshold with a unit> | <who or what measures it> | ⬜ Open |
```

### Style

A short intro, then one table of checks: ID, goal, measure, method, status. No other prose: the table is the doc.

### Done when

Every row has a number or says "number not set", every row names its method, every "met" has evidence and a date, and ROADMAP's exit criteria can point to these IDs.

---

## FEATURES.md

FEATURES.md is the contract with the user: what the product does today, and what it will and won't do. A user reads it to learn exactly what happens when they press a key or run a command. A contributor reads it before building, to see what exists and what was ruled out. It describes behavior from the user's side, never the code.

It comes fourth in a session: each feature delivers a want from the proposal, and the proposal's stances become its *Not planned* list. A fact belongs here when the user can see it or do it.

**Owns:** each feature's behavior from the user's side (keys, commands, settings, config keys, files the user sees), its status, the *Later* list, and the *Not planned* list with reasons.

**Leaves out:** type names, code paths, module names, algorithms and design reasons (all DESIGNS), layout and motion (UIUX), schedule (ROADMAP).

**Push back on:** type names or algorithms in a feature, a setting with no reason, and a *Not planned* item with no reason.

### Guidelines

- **Give each feature an ID and a status** (✅ built, 🚧 built with a gap, ⬜ planned), so other docs can point to it and a reader knows what to trust.
- **Open each feature with a short description** of what it gives the user. Then the behavior.
- **Describe what the user does and what happens, in the present tense.** A reader should be able to predict the result before trying it.
- **State the defaults, and every setting with its key.** Each setting needs a reason, because a setting is a decision handed back to the user.
- **Name the gap** on every 🚧 feature, so nobody mistakes "built" for "finished".
- **Give every *Not planned* item a reason.** This list is where people look before proposing something, and a reason stops the same proposal from coming back.
- **Describe behavior, not code.** "⌘K searches every agent's past conversations" belongs here. "An FTS5 index with BM25 ranking" belongs in DESIGNS.

### Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "Smart search across agents." | "⌘K searches every agent's past conversations. Enter on a result opens that session, or resumes it when it is closed." | What the user does, and what happens |
| "Uses an FTS5 index with BM25 ranking." | Move it to DESIGNS.md. | Implementation, not behavior |
| "Configurable notifications." | "Only *needs you* sends a notification. Setting: `agents.notify`, on by default." | The default and the one setting |

### Explore

Talk these points through in the way that fits: discuss, brainstorm or decide.

**Brainstorm to open:** for each want, list everything the product could do about it. Then sort the list into now, later and never.

1. From each want in PROPOSAL: which features deliver it? Give each an ID (F1, F2, ...).
2. For each feature: what does the user do, and what happens? What are the defaults?
3. Which settings does it need? Recommend none. Each setting needs a reason.
4. What is its status: built, built with a gap, or planned?
5. What is deliberately left for later?
6. What will the project never do? Turn the stances in PROPOSAL into concrete items, each with a reason.

### Skeleton

```markdown
# Features

<one line per status mark: ✅ built · 🚧 built with a gap · ⬜ planned>

## F1 — <name> ⬜
<a short description: what it gives the user>
<behavior, as short lines or a table>
Settings: <none, or each with its key>
Gap: <for 🚧 only>

## Later, if needed   (table: idea → note)
## Not planned        (table: not this → why)
```

### Style

One section per feature, present tense, from the user's side. Tables for keys, commands and settings.

### Done when

Every want in PROPOSAL maps to a feature or to *Not planned*, every 🚧 names its gap, and no line describes the code.

---

## DESIGNS.md

DESIGNS.md explains how the project is built, and why it is built that way. Its reader is a developer about to change the code: they need the structure, the rules that hold everywhere, and the reasons behind choices that would otherwise look strange. It is not a tour of the code. The code shows what exists. This doc keeps what the code cannot say.

It comes fifth in a session: it explains how the features are built, and links each feature it implements. A fact belongs here when it is about code, files, processes or a decision.

**Owns:** design principles, tech stack, structure and module boundaries, data model, file formats, interfaces between parts, testing, distribution, licensing, and every decision worth recording, with its reason and date.

**Leaves out:** user-visible behavior. Each section that matches a feature opens with "Behavior: FEATURES.md → Fn" and then holds only implementation.

**Push back on:** a decision with no reason, a principle that is really a product decision, and text that restates the code.

### Guidelines

- **Write design principles in concrete words.** "Local only: no server, all state in files" beats "privacy-first", because a concrete principle says what it forbids.
- **Keep product decisions out of the principles.** A design principle says how it is built. When it says what the user gets ("starts only by hand"), it is a feature: it goes in FEATURES.md.
- **Record a decision when it is hard to reverse, surprising without context, and the result of a real trade-off.** Leave the obvious ones to the code. A record of every small choice buries the few that matter.
- **Give each recorded decision one clause:** what, why, and the date (`Decided 2026-09-27: SQLite FTS5, because ...`). The reason is what stops the next developer from undoing it.
- **Name the type or file that owns each mechanism,** so a reader can find it, instead of restating what the code does. A restated mechanism goes stale the day the code changes.
- **Keep what looking cannot find:** the constraint, the convention, the trap. These are the lines that save a developer a day.
- **Mark open questions as open.** A guess written as a decision gets built on.

### Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "Privacy-first." | "Local only: no server, no account, all state in files on the device." | Says what it forbids |
| "We use SQLite." | "Decided 2026-09-27: SQLite FTS5, because it ships with the OS and indexed 1.4 GB of transcripts in 12.6 s." | A reason and a date |
| "`SearchIndex` opens the database, reads each file from its stored offset, parses each line, ..." (a page) | "`SearchIndex` owns all database access, on one serial queue, so the control socket can search off the main thread." | The constraint, not a walkthrough |

### Explore

Talk these points through in the way that fits: discuss, brainstorm or decide.

**Brainstorm to open:** for each hard choice, list two or three real alternatives before picking one, so the reason has something to beat.

1. Which design principles hold everywhere? Ask what each one forbids.
2. Stack: language, platform, frameworks, storage, build. One decision at a time, with the alternatives and the reason.
3. Structure: which parts exist, and what may each one depend on?
4. Data: what is stored, where, in what format? What survives a restart?
5. Interfaces: between parts, and to the outside (APIs, files, protocols).
6. Testing: what is tested how, and what does "fast enough" or "cheap enough" mean? (Link GOALS.)
7. What is still undecided? Record it as an open question, not a guess.

### Skeleton

```markdown
# Designs

How <name> is built and why. Behavior is in FEATURES.md.

## Design principles      (bold name, what it means, what it forbids)
## Tech stack             (table: layer → choice, with decisions below)
## Structure              (parts and allowed dependencies)
## Data model
## <one section per feature area>   (opens with "Behavior: FEATURES.md → Fn")
## Testing
## Distribution
## Licensing and references
## Open questions
```

### Style

Sections per area, each opening with what it covers. Decisions as dated clauses. Tables for stacks and formats.

### Done when

Every recorded decision has a reason and a date, every feature area links its F-number, and nothing restates behavior or the code.

---

## ROADMAP.md

ROADMAP.md answers "when?" and "how far along?". It breaks the work into milestones, each a usable state of the project, and shows where the work stands. A reader checks it to see what comes next and whether a milestone is done. It schedules features. It does not describe them.

It comes sixth in a session: it schedules the features into milestones, and its exit criteria point to the goals. A fact belongs here when it is about when, or about status.

**Owns:** milestones in order, their tasks with IDs, status, and exit criteria that point to GOALS.

**Leaves out:** feature behavior, the *Later* list (FEATURES), release notes (CHANGELOG).

**Push back on:** a milestone nobody could use, exit criteria that restate goals instead of pointing to them, and build logs in task rows.

### Guidelines

- **Make each milestone a usable state,** not a pile of tasks. "Sessions survive quitting" can be used. "Polish" cannot.
- **Make the first milestone small enough to finish soon.** A first milestone that drags makes the whole plan look unreal.
- **Point exit criteria at goal IDs** instead of restating them, so the measure lives in one place.
- **Give tasks IDs** (M1.1) that branches and commits can use, so the work traces back to the plan.
- **Keep one row per task, about 20 words.** Logs of how a task was built and checked belong in git.

### Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "M2: Polish." | "M2 Sessions survive quitting. Exit: GOALS.md G3." | A usable state, and a checkable exit |
| "M1.3 Built 2026-10-07 after three mockups. Checked headless at every size ..." | "M1.3 Smooth scrolling (engine patch 0005)." | One row, no log |

### Explore

Talk these points through in the way that fits: discuss, brainstorm or decide.

**Brainstorm to open:** list the versions of the project someone could use every day, from the smallest up. Then pick the smallest one as the first milestone.

1. What is the smallest version that is useful every day? That is the first milestone.
2. What comes next, and what does each milestone depend on?
3. For each milestone: which goals must be met to call it done?
4. Which tasks make up each milestone?

### Skeleton

```markdown
# Roadmap

**Current milestone:** M1. <one line>

## Overview   (table: milestone → delivers → features → depends on → status)

## M1 — <name> ⬜
| ID | What it delivers | Note |
|---|---|---|
**Exit criteria:** GOALS.md G1 and G3.

## Later
See FEATURES.md → Later, if needed.
```

### Style

A status board: one overview table, then one table per milestone.

### Done when

Every milestone has exit criteria tied to goals, and the first milestone is small enough to finish soon.

---

## README.md

The README is the front door. A visitor reads it to decide, in about thirty seconds, whether the project is for them, and then to start using it. It summarizes the other docs at pitch level and points to them. It should never be the only place a fact is written down.

It comes last in a session, because it sums up the approved docs. Beyond install and first use, it holds no fact of its own: everything else is a summary with a link.

**Owns:** the tagline, a short description that leads with what sets the project apart, what it does, install, first use, known limits, and links to every other doc.

**Leaves out:** detail any other doc owns. It summarizes and links.

**Push back on:** a fact written only in the README, and a copy of another doc's detail.

### Guidelines

- **Lead with the one constraint that sets the project apart.** "It writes no document until you agree on its key points" tells a visitor more than "a flexible documentation tool".
- **Say what it does in a few bullets,** then link to the doc that holds the detail.
- **Use a table when the content is records,** such as the docs with the question each answers, or situations with the command for each.
- **Give the install steps exactly,** as commands that can be copied.
- **List the known limits** a new user must know before starting. Hiding them costs more trust than stating them.
- **Draft it last,** from the approved docs, so it summarizes decisions that already exist.

### Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "A powerful, flexible documentation framework." | "It writes no document until you have agreed on its key points." | The one constraint, not a category |
| A copy of the full feature list | Four bullets, then a link to FEATURES.md | A summary, not a copy |

### Explore

Usually nothing new: draft it from the approved docs. Then ask:

1. Which install methods exist now?
2. Which limits must a new user know before they start?

### Skeleton

```markdown
# <Name>

> <tagline>

<one or two sentences: what it is, and the constraint that sets it apart>

## What it does        (a few bullets)
## Install
## Use                 (or: When to reach for it, as a table)
## Known limits
## Documents           (a link to every other doc)
## License
```

### Style

One description, then bullets and tables. Commands in code blocks.

### Done when

A stranger can install and use the project from the README alone, and every other doc is linked.

---

## UIUX.md

UIUX.md describes how the product looks and moves: where each kind of information lives on screen, how loud each state is, and which colors and motions carry meaning. A designer or developer reads it before touching the interface, to keep the screens consistent.

**Owns:** layout, states and how loud each one is, color, type, motion, keyboard, accessibility. Rules, not measurements: name the code type that holds the numbers.

**Leaves out:** behavior (FEATURES), implementation (DESIGNS).

**Add when** the project has a visual interface. Draft it right after FEATURES.md, because it shapes how the features look. A fact belongs here when it is about how the product looks or moves.

### Guidelines

- **Write each rule with its reason,** because a rule without one gets broken the first time it is inconvenient.
- **Give each state a loudness,** and say which one may interrupt the user.
- **Name the type that holds the numbers** (sizes, durations, colors) instead of copying them.

| Weak | Strong |
|---|---|
| "Cards are 72 pt tall with 12 pt padding." | "Card sizes live in `SessionCardLayout`. A card that waits for the user grows one line." |

### Explore

Where does each kind of information live on screen? Which state may interrupt the user? Which colors carry meaning? What moves, and what never moves?

---

## CLI.md

CLI.md is the reference for every command: what it does, its flags, its output and its exit codes. Scripts and people both depend on it, so it must match the program exactly.

**Owns:** every command and flag, with a mark for built or planned, exit codes, output formats, and examples.

**Add when** the project has a command-line interface. Draft it right after FEATURES.md, because each command is how a user reaches a feature. A fact belongs here when it is about a command, a flag or an exit code.

### Guidelines

- **Mark each command and flag** as built or planned, so nobody scripts against a flag that doesn't exist.
- **Show an example per command,** with its output.
- **Say what happens on failure,** and with which exit code. Scripts depend on it.

| Weak | Strong |
|---|---|
| "`search` finds notes." | "`notes search <text>` prints one line per note, best match first. Exits 1 when the index can't be read." |

### Explore

Who calls each command, a person or a script? What does it print? What does it do on failure? Which flags are needed now, and which can wait?

---

## GLOSSARY.md

The glossary fixes the project's words: one name per thing, each with a one-line meaning. It stops two words from naming one thing, which is how docs and code start to disagree.

**Owns:** the project's terms, and the one name chosen for each thing.

**Add when** the domain has its own terms, or two words compete for one thing. Start it with the first doc, and add terms as they appear.

### Guidelines

- **Pick one name and record the losing synonyms,** so search still finds them.
- **Define each term in one line,** in plain words.

| Weak | Strong |
|---|---|
| Tab, pane, session and terminal used for one thing | "**Session:** one shell and its agent. (Not: tab, terminal.)" |

### Explore

When two words name one thing, which one do we keep?

---

## AGENTS.md

AGENTS.md is the instruction file for coding agents working in the repo. Many tools read it, and `CLAUDE.md` can link to it, so the rules live once. It covers what an agent cannot learn by looking: commands that must pass, rules to follow, and what never to touch.

**Owns:** commands to build, test and lint, the rules agents must follow, which doc to read first, and the guardrails.

**Add when** coding agents will work in the repo. Draft it near the end of a session, once the build commands and the rules are known.

### Guidelines

- **Give each rule its reason in a clause,** so an agent can apply it to cases the rule does not name.
- **Write the target behavior,** and keep a prohibition only for a hard guardrail. A ban puts the forbidden thing in the agent's mind.
- **Point to the placement test** for where new facts go.

| Weak | Strong |
|---|---|
| "Don't break the build." | "Run `make test` and `make lint` before you call work done. Report failures with their output." |

### Explore

Which commands must pass before work is done? What must an agent never touch? Where do new facts go?

---

## CHANGELOG.md

The changelog tells users what changed in each release, in words they understand. It is the doc people read before they upgrade.

**Owns:** one section per version with its date, grouped by area.

**Add when** the project ships releases. Start it with the first release. A fact belongs here when it shipped in a release.

### Guidelines

- **Write from the user's side:** what they can now do, or what no longer breaks.
- **Keep an *Unreleased* section** and fill it in the change that does the work, so release day needs no archaeology.

| Weak | Strong |
|---|---|
| "Refactored the index module." | "Search results now appear while you type." |

---

## TODO.md

TODO.md holds small fixes found in review that have no milestone yet, so they don't get lost.

**Owns:** short items, each with enough context to act on.

**Add when** small findings would otherwise get lost. Move an item to ROADMAP once it has a milestone.

| Weak | Strong |
|---|---|
| "Fix motion thing." | "`SessionCard.swift` animates a state change even when Reduce Motion is on. Gate it on `Motion.isReduced`." |

---

## CONTRIBUTING.md

CONTRIBUTING.md tells outside contributors how to help: how to set up, how work flows, and what must pass. GitHub links it from issues and pull requests.

**Owns:** setup, workflow (branches, commits, reviews), required checks, where to ask.

**Add when** the project is public and accepts contributions. Draft it at the end of a session, with AGENTS.md, once the workflow is known.

### Guidelines

- **State the bar for a change,** so contributors know before they invest. For example: a change needs a failure seen in real use.
- **List the checks that must pass,** as commands.

---

## SECURITY.md

SECURITY.md tells people how to report a vulnerability safely. GitHub shows it as the project's security policy.

**Owns:** where to report, what to include, which versions are supported, what happens next.

**Add when** the project is public. Draft it at the end of a session.

---

## RUNBOOK.md

RUNBOOK.md is for the person keeping a service running: how to deploy, roll back and respond to each alert. It is read under pressure, so each procedure is short and exact.

**Owns:** deploy, rollback, monitoring, each alert and its response, who is on call.

**Add when** the project is a service someone must keep running. Draft it after DESIGNS.md, once the service's parts are known.

| Weak | Strong |
|---|---|
| "Check the logs if something breaks." | "Alert `queue-lag > 5 min`: run `kubectl rollout restart deploy/worker`. If lag stays after 10 minutes, page the on-call." |

---

## Decision records

A decision record holds one decision in its own file, when DESIGNS.md has too many to read. It is the ADR (architecture decision record) format.

**Owns:** one decision per file (`docs/decisions/0001-<slug>.md`): the context, the decision and its reason, in one to three sentences. Add the alternatives or consequences only when they are not obvious.

**Add when** DESIGNS.md holds so many decisions that it becomes hard to read. Keep each decision's one-line summary in DESIGNS.md, with a link to its record.

### Guidelines

- **Record only decisions that pass the bar:** hard to reverse, surprising without context, and a real trade-off.
- **Keep it to one paragraph** unless the alternatives are worth remembering.

---

## Other names you may meet

| Name | Where it fits here |
|---|---|
| PRD, product spec | FEATURES.md, with the pains and wants in PROPOSAL.md |
| Vision document | PROPOSAL.md and PHILOSOPHY.md |
| PR/FAQ (working backwards) | a style for PROPOSAL.md: write it as the launch announcement |
| ARCHITECTURE.md, design doc, tech spec | DESIGNS.md |
| ADR | a decision record, summarized in DESIGNS.md |
| RFC | a proposal for one change. Its outcome lands in DESIGNS.md or a decision record |
| OKRs, success metrics | GOALS.md |
| Non-goals | FEATURES.md → Not planned, and the stances in PROPOSAL.md |
| Backlog | ROADMAP.md for scheduled work, TODO.md for small items |

## Not covered

- **User manuals:** tutorials, how-to guides and API references for end users. They answer different questions (the Diátaxis framework sorts them). Write them after the founding docs exist.
- **Standard texts:** `LICENSE` and `CODE_OF_CONDUCT.md`. Use a standard text, such as an OSI-approved license or the Contributor Covenant. They need a choice, not a discussion.
