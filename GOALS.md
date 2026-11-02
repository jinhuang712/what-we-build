# Goals

Each goal is an effect the skill must have, tied to a want or a risk in the proposal. A goal met on one project stays open for another until it is checked there, and a status changes only with a check and its date. For goals checked on this repo, the reader who checks did not write the change unless the status says "by the author".

## Summary

```
Goals
├── Objectives
│   ├── ⬜ O1: One sitting — the 7 core docs of a new project agreed in 1 sitting
│   └── ⬜ O2: Context survives compaction — after a compaction the agent knows the task from the docs alone
├── Measures
│   ├── M1: Reads before it changes — not measured yet
│   └── M4: Docs that fell behind — not measured yet
├── Benchmarks
│   └── B1: Session quality — not run yet
├── Comparisons
│   └── C1: With and without the skill — not run yet
└── Thresholds
    ├── ✅ T4: A short skill — SKILL.md within 500 lines
    └── ✅ T8: A doc read in one go — every doc within one Claude Code read
```

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

**Want:** an agent that reads before it works.

**How:** every change in the 3 latest sittings at the checkpoint, read for whether the owning doc was read first.

**Formula:**

```
M1 (%) = 100 × changes made after reading the owning doc / all changes in the sample
```

**Checked:** each checkpoint.

**Last value:** not measured.

#### M4: Docs that fell behind

At a checkpoint the docs still say what the project is.

**Want:** the risk that the docs fall behind the work.

**How:** a reader who did not write the change reads the whole doc set against the work.

**Formula:**

```
M4 (claims) = claims in the whole doc set that the work now contradicts
```

**Checked:** each checkpoint.

**Last value:** not measured.

### Benchmarks

#### B1: Session quality

Sessions with the skill are scored on a fixed set of prompts.

**Want:** the wants and risks in the proposal that only a real session shows.

**Problem set:** the three realistic project prompts of [CP4: Proven useful](ROADMAP.md#cp4-proven-useful).

**Scored on:** a reader who did not run the session checks each of these:

- Every fact has one home.
- Every goal has a check.
- Every decision says what was not chosen and why.
- No doc was drafted before its key points were agreed or committed before it was approved.
- A reader who did not write a doc can retell its main points after one read.
- The user recognizes each doc as what was decided.
- Each doc's content came from the talk and not from the blanks of a skeleton.
- Each doc has a job in that project.

**Formula:**

```
run score = checks passed / 8
B1 = mean of the 3 run scores
```

**Checked:** each checkpoint.

**Last score:** not run.

### Comparisons

#### C1: With and without the skill

The skill earns its place only if it beats the same agent without it.

**Want:** the risk that the skill is only a faster way to get confident text.

**Against:** the same agent without the skill.

**How:** the prompts of [B1: Session quality](#b1-session-quality) run both ways and scored the same way.

**Formula:**

```
lead = run score with the skill − run score without it, for each prompt
C1 = prompts with a lead above 0 / 3, with the mean lead
```

**Checked:** each checkpoint.

**Last result:** not run.

### Thresholds

#### T4: A short skill

`SKILL.md` is read in every session, so it stays short enough to read in full.

**Want:** the risk that the skill itself grows too long.

**Limit:** `SKILL.md` ≤ 500 lines.

**How:** `wc -l skills/what-we-build/SKILL.md`

**Checked:** each checkpoint.

**Status:** ✅ 195 lines on 2026-11-02 by the author.

#### T8: A doc read in one go

The agent re-reads a whole doc before any edit, so one read must return all of it.

**Want:** docs a person can read.

**Limit:** every doc within 25000 tokens and 2000 lines, the default limits of one Claude Code read.

**How:** `wc -l` for lines, and a read that returns the whole file without a cut.

**Checked:** each checkpoint.

**Status:** ✅ 2026-11-02 by the author, with the largest doc CHANGELOG at about 4000 tokens.
