# Goals

Each goal is an effect the skill must have, tied to a want or a risk in the proposal. A goal met on one project stays open for another until it is checked there, and a status changes only with a check and its date.

## Summary

```
Goals
├── Objectives
│   ├── ⬜ O1: The core docs without a long talk — the 7 core docs of a new project agreed within a time limit
│   └── ⬜ O2: Context survives compaction — after a compaction the agent knows the task from the docs alone
├── Measures
│   ├── ⬜ M1: Reads before it changes — not measured yet
│   └── ⬜ M4: Docs that fell behind — not measured yet
├── Benchmarks
│   └── ⬜ B1: Run quality — not run yet
├── Comparisons
│   └── ⬜ C1: With and without the skill — not run yet
└── Thresholds
    ├── ✅ T4: A short skill — SKILL.md within 500 lines
    └── ✅ T8: A doc read in one go — every doc within one Claude Code read
```

## Goals

### Objectives

#### O1: The core docs without a long talk

A new project gets its whole doc set without the talk dragging on.

**Want:** the risk that the user wants the docs and not the talk.

**Acceptance:** a new project's 7 core docs are drafted and approved within N hours of talk. N stays open while [The time limit for O1: The core docs without a long talk](TODO.md#p1discussion-the-time-limit-for-o1-the-core-docs-without-a-long-talk) is open.

**Status:** ⬜

#### O2: Context survives compaction

What was decided stays known after the window is compacted.

**Want:** context that outlives the window.

**Acceptance:** after a compaction the agent names the current task and the latest decisions from the docs alone.

**Status:** ⬜

### Measures

#### M1: Reads before it changes

The agent reads the doc that owns a thing before it changes that thing.

**Want:** an agent that reads before it works.

**How:** every change in the last 3 windows of work before the checkpoint, each read for whether the owning doc was read first.

**Formula:**

```
M1 (%) = 100 × changes made after reading the owning doc / all changes in the sample
```

**Last value:** not measured.

#### M4: Docs that fell behind

At a checkpoint the docs still say what the project is.

**Want:** the risk that the docs fall behind the work.

**How:** a reader who did not write the change reads the whole doc set against the work.

**Formula:**

```
M4 (claims) = claims in the whole doc set that the work now contradicts
```

**Last value:** not measured.

### Benchmarks

#### B1: Run quality

Runs with the skill are scored on a fixed set of prompts.

**Want:** the wants and risks in the proposal that only a real run shows.

**Problem set:** three realistic project prompts, not chosen while [How to evaluate the skill](TODO.md#p2discussion-how-to-evaluate-the-skill) is open.

**Formula:**

```
run score = checks passed / 8
B1 = mean of the 3 run scores
```

A reader who did not take part in the run makes the 8 checks:

- Every fact has one home.
- Every goal has a check.
- Every decision says what was not chosen and why.
- Nothing went into a doc before it was agreed, and nothing was committed before it was approved.
- A reader who did not write a doc can retell its main points after one read.
- The user recognizes each doc as what was decided.
- Each doc's content came from the talk and not from the blanks of a skeleton.
- Each doc has a job in that project.

**Last score:** not run.

### Comparisons

#### C1: With and without the skill

The skill earns its place only if it beats the same agent without it.

**Want:** the risk that the skill is only a faster way to get confident text.

**Against:** the same agent without the skill.

**How:** the prompts of [B1: Run quality](#b1-run-quality) run both ways and are scored the same way.

**Formula:**

```
lead = run score with the skill − run score without it, for each prompt
C1 = prompts with a lead above 0 / 3, with the mean lead
```

**Last result:** not run.

### Thresholds

#### T4: A short skill

`SKILL.md` is read each time the skill starts, so it stays short enough to read in full.

**Want:** the risk that the skill itself grows too long.

**Limit:** `SKILL.md` ≤ 500 lines.

**How:** `wc -l skills/what-we-build/SKILL.md`

**Status:** ✅ 248 lines on 2026-11-04.

#### T8: A doc read in one go

The agent re-reads a whole doc before any edit, so one read must return all of it.

**Want:** docs a person can read.

**Limit:** every doc within 25000 tokens and 2000 lines, the default limits of one Claude Code read.

**How:** `wc -l` for lines and `wc -c` for bytes on every doc, since a doc never has more tokens than bytes.

**Status:** ✅ 2026-11-04, with CHANGELOG.md the longest at 392 lines and the largest at 23641 bytes.
