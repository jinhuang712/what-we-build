<!-- what-we-build: approved 2026-11-02 -->

# Goals

Each goal ties to a want or a risk in [PROPOSAL.md](PROPOSAL.md). A goal met on one project stays open for another until it is checked there, and a status changes only with a check and its date. For goals checked on this repo, the reader who checks did not write the change unless the status says "by the author". The audit of 2026-11-02 ran before the wording pass of that day, which joined lines but changed no facts.

## Summary

| Goal | Checked | Status |
|---|---|---|
| [O1: One sitting](#o1-one-sitting) | each checkpoint | ⬜ |
| [O2: Context survives compaction](#o2-context-survives-compaction) | each checkpoint | ⬜ |
| [M1: Reads before it changes](#m1-reads-before-it-changes) | each checkpoint | not measured |
| [M2: Sentences over the comma rule](#m2-sentences-over-the-comma-rule) | every change | 0 |
| [M3: Length of the core docs](#m3-length-of-the-core-docs) | every change | 885 lines |
| [B1: Session quality](#b1-session-quality) | each checkpoint | not run |
| [C1: With and without the skill](#c1-with-and-without-the-skill) | each checkpoint | not run |
| [T1: One home per fact](#t1-one-home-per-fact) | each checkpoint | ❌ |
| [T2: Goals that can be checked](#t2-goals-that-can-be-checked) | every change | ✅ |
| [T3: Decisions with reasons](#t3-decisions-with-reasons) | every change | ✅ |
| [T4: A short skill](#t4-a-short-skill) | every change | ✅ |
| [T5: Links that work](#t5-links-that-work) | every change | ✅ |
| [T6: Manual start only](#t6-manual-start-only) | each checkpoint | ⬜ |
| [T7: Guidelines that can be tested](#t7-guidelines-that-can-be-tested) | each checkpoint | ✅ |
| [R1: No draft before agreement](#r1-no-draft-before-agreement) | every change | ⬜ |
| [R2: No dependencies](#r2-no-dependencies) | every change | ✅ |
| [R3: Our own words](#r3-our-own-words) | every change | ⬜ |
| [R4: Made-up examples](#r4-made-up-examples) | every change | ✅ |
| [R5: No code chunks](#r5-no-code-chunks) | every change | ✅ |

## Goals

### Objectives

#### O1: One sitting

A new project gets its whole doc set without the talk dragging on.

**Want:** the risk that the user wants the docs and not the talk.

**Acceptance:** a new project's 7 core docs are drafted and approved in 1 sitting.

**Checked:** each checkpoint, on a new project.

**Status:** ⬜

#### O2: Context survives compaction

What was decided stays known after the window is compacted.

**Want:** context that outlives the session.

**Acceptance:** after a compaction the agent names the current task and the latest decisions from the docs alone.

**Checked:** each checkpoint.

**Status:** ⬜

### Measures

#### M1: Reads before it changes

The agent reads the doc that owns a thing before it changes that thing.

**How:** the share of changes in sampled sittings made after reading the owning doc.

**Checked:** each checkpoint.

**Last value:** not measured.

#### M2: Sentences over the comma rule

Short sentences keep the docs easy to read.

**How:** count the sentences outside tables and code with two or more commas in the core docs except PHILOSOPHY.

**Checked:** every change.

**Last value:** 0 on 2026-11-02 by the author, against 34 lines at v0.4.0.

#### M3: Length of the core docs

The core docs stay short enough to read in full.

**How:** `wc -l` over the 7 core docs.

**Checked:** every change.

**Last value:** 885 lines on 2026-11-02 by the author, against 614 at v0.4.0. GOALS alone grew from 56 to 270 lines when each goal got its own section.

### Benchmarks

#### B1: Session quality

Sessions with the skill are scored on a fixed set of prompts.

**Problem set:** the three realistic project prompts of [CP3: Proven useful](ROADMAP.md#cp3-proven-useful), each run scored against:

- [T1: One home per fact](#t1-one-home-per-fact)
- [T2: Goals that can be checked](#t2-goals-that-can-be-checked)
- [T3: Decisions with reasons](#t3-decisions-with-reasons)
- [R1: No draft before agreement](#r1-no-draft-before-agreement)

**Checked:** each checkpoint.

**Last score:** not run.

### Comparisons

#### C1: With and without the skill

The skill earns its place only if it beats the same agent without it.

**Against:** the same agent without the skill.

**How:** the prompts of [B1: Session quality](#b1-session-quality) run both ways and scored the same way.

**Checked:** each checkpoint.

**Last result:** not run.

### Thresholds

#### T1: One home per fact

A fact written out in full in two docs drifts.

**Limit:** 0 facts written out in full in two docs.

**How:** an independent audit lists every such fact.

**Checked:** each checkpoint.

**Status:** ❌ 2026-11-02 by independent audit, with 6 facts:

- The question each doc answers, in PROPOSAL, PHILOSOPHY and README.
- The work rules, in [F5: Keep the context while you work](FEATURES.md#f5-keep-the-context-while-you-work) and AGENTS.md.
- The install commands, in README and INSTALL.
- The failure stories, in PROPOSAL and PHILOSOPHY.
- The reason for the manual start, in FEATURES, PROPOSAL and [002: The skill starts only by hand](specs/decisions/002-manual-start.md).
- The doc mark, in [DESIGNS 2: The docs are the state](DESIGNS.md#2-the-docs-are-the-state) and [F2: Resume](FEATURES.md#f2-resume).

#### T2: Goals that can be checked

A goal nobody can check is a wish.

**Limit:** 0 goals without a check.

**How:** read GOALS.md goal by goal.

**Checked:** every change.

**Status:** ✅ 2026-11-02 by independent audit.

#### T3: Decisions with reasons

A decision that hides the road not taken gets undone.

**Limit:** 0 decisions without what was not chosen and why.

**How:** read every file in `specs/decisions/`.

**Checked:** every change.

**Status:** ✅ 2026-11-02 by independent audit.

#### T4: A short skill

`SKILL.md` is read in every session, so it stays short enough to read in full.

**Limit:** `SKILL.md` ≤ 500 lines.

**How:** `wc -l skills/what-we-build/SKILL.md`

**Checked:** every change.

**Status:** ✅ 171 lines on 2026-11-02 by the author.

#### T5: Links that work

A broken link sends the reader nowhere.

**Limit:** 0 broken relative links and anchors.

**How:** a reader follows every relative link and anchor.

**Checked:** every change.

**Status:** ✅ 2026-11-02 by independent audit.

#### T6: Manual start only

The skill loads only when the user types `/what-we-build`.

**Limit:** 0 automatic starts.

**How:** watch sittings for a load without `/what-we-build`.

**Checked:** each checkpoint.

**Status:** ⬜

#### T7: Guidelines that can be tested

A guideline that rejects nothing guides nothing.

**Limit:** 0 guidelines a reader cannot test.

**How:** a reader names a design that each DESIGNS guideline rejects.

**Checked:** each checkpoint.

**Status:** ✅ 2026-11-02 by independent audit.

### Constraints

#### R1: No draft before agreement

No doc is drafted before its key points are agreed, and none is committed before it is approved.

**Rule:** [SKILL.md → Writing a doc](skills/what-we-build/SKILL.md#writing-a-doc)

**How:** read the session for each doc's first write and its commit.

**Checked:** every change.

**Status:** ⬜ last not met 2026-10-13.

#### R2: No dependencies

The skill stays plain Markdown.

**Rule:** [DESIGNS 3: No dependencies](DESIGNS.md#3-no-dependencies)

**How:** `skills/what-we-build/` holds only Markdown files.

**Checked:** every change.

**Status:** ✅ 2026-11-02 by independent audit.

#### R3: Our own words

Methods from other guides are rewritten and never copied.

**Rule:** [DESIGNS 4: Our own words over borrowed text](DESIGNS.md#4-our-own-words-over-borrowed-text)

**How:** no passage in `skills/` is copied from a source.

**Checked:** every change.

**Status:** ⬜

#### R4: Made-up examples

No example points at another project.

**Rule:** [DESIGNS 5: Made-up examples over real projects](DESIGNS.md#5-made-up-examples-over-real-projects)

**How:** no example in `skills/` names or quotes another project.

**Checked:** every change.

**Status:** ✅ 2026-11-02 by independent audit.

#### R5: No code chunks

A doc explains and links, and never pastes code.

**Rule:** [SKILL.md → Wording](skills/what-we-build/SKILL.md#wording)

**How:** no doc in this repo pastes code or a command longer than two lines.

**Checked:** every change.

**Status:** ✅ 2026-11-02 by independent audit, with one doubt: the README install line joins two commands with `&&`.
