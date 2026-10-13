# The documents

For each document: the question it answers, what it owns and leaves out, its voice, the questions to ask the user, a skeleton and the signs that it is done.

## Contents

- Core: [PROPOSAL](#proposalmd) · [PHILOSOPHY](#philosophymd) · [GOALS](#goalsmd) · [FEATURES](#featuresmd) · [DESIGNS](#designsmd) · [ROADMAP](#roadmapmd) · [README](#readmemd)
- Optional: [UIUX](#uiuxmd) · [CLI](#climd) · [GLOSSARY](#glossarymd) · [AGENTS](#agentsmd) · [CHANGELOG](#changelogmd) · [TODO](#todomd) · [CONTRIBUTING](#contributingmd) · [SECURITY](#securitymd) · [RUNBOOK](#runbookmd) · [Decision records](#decision-records)
- [Other names you may meet](#other-names-you-may-meet)
- [Not covered](#not-covered)

---

## PROPOSAL.md

**Answers:** Why did we start this?

**Owns:** the shift that makes the project necessary, the pain points, the one idea that makes it different, what we want, a sample of it working, what we don't want, who it is for, the approach, the risks, how we will know it works.

**Leaves out:** exact behavior (FEATURES), numbers to check (GOALS, but it may quote the headline ones), status (ROADMAP), the list of docs (README).

**Voice:** a technical pitch, like a short talk to engineers. Short sections, punchy lines, real numbers, tables for comparisons. Persuasive, never vague. It opens with a scene the reader has lived, not with a definition.

**Ask:**

1. What changed in the world that makes this project necessary now?
2. What hurts today? Ask for each pain point with a concrete example or a number.
3. Describe the moment the pain happens, as a scene the reader has lived. (This becomes the hook.)
4. What is the one idea that makes this different? Say it in one sentence.
5. For each pain: what should happen instead?
6. Show it working: one concrete example of the product in use (a conversation, a command and its output, a screen).
7. What must this project never become? Ask for the reason of each.
8. Who is it for? Who is the first user?
9. What is the approach in one line per choice: platform, language, core model, what it builds on?
10. What could make it fail, and what reduces each risk?

**Skeleton:**

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
## What we don't want   (table: not this → why)
## Who it is for
## Approach
## Risks                (table: risk → mitigation)
## How we know it works (link GOALS.md)
```

**Done when:** the hook names a moment the reader has lived, the idea fits in one sentence, the sample shows the product instead of describing it, every pain has an example, every want answers a pain, every "don't want" has a reason, and a stranger could repeat the pitch in two sentences.

---

## PHILOSOPHY.md

**Answers:** Why is it this way?

**Owns:** what the core value means, three to five principles, the design words, the evidence behind them, and the test that every change must pass.

**Leaves out:** any feature, setting, screen part or technology. If a principle names a feature, it belongs in FEATURES, UIUX or DESIGNS.

**Voice:** reflective. It guides the other docs, and it should also teach the reader something about the problem. Plain words, short sentences, a few lines that stay with the reader. No marketing.

**Ask:**

1. What is the one value the project protects? (For example: attention, trust, speed, privacy.)
2. What does that value mean here, in the user's own words?
3. Which beliefs follow from it? Draft three to five, then test each one: does it reject at least one real, tempting feature? A principle that rejects nothing is decoration.
4. Which words describe how it should feel to use? (Two to four.)
5. Is there research or a known idea behind the principles? Cite it only when the user knows the source or you can verify it.
6. What four questions should every proposed change pass?

**Skeleton:**

```markdown
# Philosophy

<two or three short paragraphs: what changed, what is scarce, why this project exists>

## What <the value> means
## Principles
### 1. <principle>          (a short paragraph each, no features)
## Design guidelines        (table: word → means)
## Evidence                 (optional table: rule → source)
## The test for every change
```

**Done when:** no line names a feature, each principle can reject something, and the test is the last section (other docs point to it).

---

## GOALS.md

**Answers:** What do we measure?

**Owns:** goals as checks. Each has an ID, a measure with a number, and a status.

**Leaves out:** anything vague, non-goals (FEATURES → Not planned), how anything works.

**Voice:** cold. A measure and a status, nothing else.

**Ask:**

1. For each want in PROPOSAL: how would we know it is true? What number, measured how?
2. Who or what measures it: a script, a benchmark, the user's own use?
3. What is the threshold? When the user has no number yet, the goal stays out, or it is listed as open with "number not set".
4. What is its status today? Met only with evidence, and the date it was measured.

**Skeleton:**

```markdown
# Goals

Each goal is a check with a number. <How and where it is measured.>

| # | Goal | Measure | Status |
|---|---|---|---|
| G1 | <short name> | <number and how it is measured> | ⬜ Open |
```

**Done when:** every row has a number, every Met has evidence and a date, and ROADMAP's exit criteria can point to these IDs.

---

## FEATURES.md

**Answers:** What does it do, and what will it do?

**Owns:** each feature's behavior from the user's side (keys, commands, settings, config keys, files the user sees), its status, the *Later* list and the *Not planned* list with reasons.

**Leaves out:** type names, code paths, module names, algorithms, design reasons and dates (all DESIGNS), layout and motion (UIUX), schedule (ROADMAP).

**Voice:** precise and plain. Present tense. A user reading it should know exactly what will happen.

**Ask:**

1. From each want in PROPOSAL: which features deliver it? Give each an ID (F1, F2, ...).
2. For each feature: what does the user do, and what happens? What are the defaults?
3. Which settings does it need? Recommend none. Each setting needs a reason.
4. What is its status: built, built with a gap, or planned?
5. What is deliberately left for later?
6. What will the project never do? (From "what we don't want" in PROPOSAL, made concrete.)

**Skeleton:**

```markdown
# Features

<one line per status mark: ✅ built · 🚧 built with a gap · ⬜ planned>

## F1 — <name> ⬜
<one line: what it gives the user>
<behavior, as short lines or a table>
Settings: <none, or each with its key>

## Later, if needed   (table: idea → note)
## Not planned        (table: not this → why)
```

**Done when:** every want in PROPOSAL maps to a feature or to *Not planned*, and no line mentions code.

---

## DESIGNS.md

**Answers:** How is it built, and why that way?

**Owns:** design principles, tech stack, structure and module boundaries, data model, file formats, interfaces between parts, testing, distribution, licensing, and every decision with its reason and date.

**Leaves out:** user-visible behavior. Each section that matches a feature opens with "Behavior: FEATURES.md → Fn" and then holds only implementation.

**Voice:** technical. Decisions as one clause: `Decided 2026-10-12: SQLite, because ...`. Open questions marked as open.

**Ask:**

1. Which design principles hold everywhere? Each in concrete words: "Local only: no server, all state in files" beats "privacy-first". Ask what each one would forbid.
2. Stack: language, platform, frameworks, storage, build. One decision at a time, with alternatives and the reason.
3. Structure: which parts exist, and what may each one depend on?
4. Data: what is stored, where, in what format? What survives a restart?
5. Interfaces: between parts, and to the outside (APIs, files, protocols).
6. Testing: what is tested how, and what does "fast enough" or "cheap enough" mean (link GOALS)?
7. What is still undecided? Record it as an open question, not a guess.

**Skeleton:**

```markdown
# Designs

How <name> is built and why. Behavior is in FEATURES.md.

## Design principles      (bold name, then what it means and what it forbids)
## Tech stack             (table: layer → choice, with decisions below)
## Structure              (parts and allowed dependencies)
## Data model
## <one section per feature area>   (opens with "Behavior: FEATURES.md → Fn")
## Testing
## Distribution
## Licensing and references
## Open questions
```

**Done when:** every decision has a reason and a date, every feature area links its F-number, and nothing restates behavior.

---

## ROADMAP.md

**Answers:** When, and how far along?

**Owns:** milestones in order, their tasks with IDs, status, and exit criteria that point to GOALS.

**Leaves out:** feature behavior, the *Later* list (FEATURES), release notes (CHANGELOG).

**Voice:** a status board. Tables. One row per task, at most about 20 words.

**Ask:**

1. What is the smallest version that is useful every day? That is the first milestone.
2. What comes next, and what does each milestone depend on?
3. For each milestone: which goals must be met to call it done?
4. Which tasks make up each milestone? Give IDs (M1.1) that branches and commits can use.

**Skeleton:**

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

**Done when:** every milestone has exit criteria tied to goals, and the first milestone is small enough to finish soon.

---

## README.md

**Answers:** What is this, and how do I start?

**Owns:** the tagline, one paragraph on what it is and who it is for, a short "what it does" list, install, first use, known limits, and links to every other doc.

**Leaves out:** detail any other doc owns. It summarizes at pitch level and links.

**Voice:** welcoming and direct. A visitor knows in 30 seconds whether this is for them.

**Ask:** usually nothing new. Draft it from the approved docs, then ask:

1. Which install methods exist now?
2. Which limits must a new user know before they start?

**Done when:** a stranger can install it and run it from the README alone, and every other doc is linked once.

---

## UIUX.md

**Answers:** How does it look and move?

**Owns:** layout, states and how loud each one is, color, type, motion, keyboard, accessibility. Rules, not measurements: name the code type that holds the numbers.

**Leaves out:** behavior (FEATURES), implementation (DESIGNS).

**Add when:** the project has a visual interface.

**Ask:** Where does each kind of information live on screen? Which state may interrupt the user? Which colors carry meaning? What moves, and what never moves?

---

## CLI.md

**Answers:** What does each command do?

**Owns:** every command and flag, with a mark for built or planned, exit codes, output formats, and examples.

**Add when:** the project has a command-line interface.

**Ask:** Who calls each command, a person or a script? What does it print? What does it do on failure? Which flags are needed now, and which can wait?

---

## GLOSSARY.md

**Answers:** What does each word mean here?

**Owns:** the project's terms, one line each, and the one name chosen for each thing.

**Add when:** the domain has its own terms, or two words compete for one thing. Start it with the first doc, and add terms as they appear.

**Ask:** When two words name one thing, which one do we keep?

---

## AGENTS.md

**Answers:** How do coding agents work in this repo?

**Owns:** commands to build, test and lint, the rules agents must follow, what never to do, and which doc to read first. Many tools also read `CLAUDE.md`. Make it a link to `AGENTS.md`, so the rules live once.

**Add when:** coding agents will work in the repo.

**Ask:** Which commands must pass before work is done? What must an agent never touch? Where do new facts go (point to the placement test)?

---

## CHANGELOG.md

**Answers:** What changed in each release?

**Owns:** one section per version with its date, grouped by area, in words a user understands.

**Add when:** the project ships releases.

---

## TODO.md

**Answers:** Which small fixes wait, without a milestone?

**Owns:** short items found in review, each with enough context to act on.

**Add when:** small findings would otherwise get lost. Move an item to ROADMAP once it has a milestone.

---

## CONTRIBUTING.md

**Answers:** How do others contribute?

**Owns:** how to set up, the workflow (branches, commits, reviews), the checks that must pass, and where to ask.

**Add when:** the project is public and accepts contributions. GitHub links it from issues and pull requests.

---

## SECURITY.md

**Answers:** How do I report a vulnerability?

**Owns:** where to report, what to include, which versions are supported, and what happens next.

**Add when:** the project is public. GitHub shows it as the security policy.

---

## RUNBOOK.md

**Answers:** How do we operate it?

**Owns:** deploy, rollback, monitoring, alerts and what to do for each, and who is on call.

**Add when:** the project is a service someone must keep running.

---

## Decision records

**Answers:** Why was this one decision made?

**Owns:** one decision per file (`docs/decisions/0001-<slug>.md`): context, decision, consequences, date, status. This is the ADR (architecture decision record) format.

**Add when:** DESIGNS.md holds so many decisions that it becomes hard to read. Keep the decision's one-line summary in DESIGNS.md with a link to its record.

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
| Non-goals | FEATURES.md → Not planned, and the principles in PHILOSOPHY.md |
| Backlog | ROADMAP.md for scheduled work, TODO.md for small items |

## Not covered

- **User manuals:** tutorials, how-to guides and API references for end users. They answer different questions (the Diátaxis framework sorts them). Write them after the founding docs exist.
- **Standard texts:** `LICENSE` and `CODE_OF_CONDUCT.md`. Use a standard text, such as an OSI-approved license or the Contributor Covenant. They need a choice, not a discussion.
