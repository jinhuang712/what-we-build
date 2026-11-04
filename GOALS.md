# Goals

Each goal is an effect the skill must have, tied to a want or a risk in the proposal. The thresholds are checked on this repo. The other goals are checked on real runs of the skill on a new project, and a goal met on one project stays open for another until it is checked there. A status changes only with a check and its date.

## Summary

```
Goals
├── Objectives
│   ├── ⬜ O1: The core docs without a long talk — the 7 core docs of a new project agreed within a time limit
│   └── ⬜ O2: Context survives compaction — questions answered before a compaction are still answered right after it
├── Measures
│   ├── ⬜ M1: Reads before it changes — the share of changes made after reading the owning doc
│   └── ⬜ M4: Docs that fell behind — claims in the doc set that the work contradicts
├── Benchmarks
│   └── ⬜ B1: Run quality — 8 checks on 3 project prompts
├── Comparisons
│   └── ⬜ C1: With and without the skill — the prompts of B1: Run quality with and without the skill
└── Thresholds
    ├── ✅ T4: A short skill — the body of SKILL.md under 5000 tokens
    └── ✅ T8: A doc read in one go — every doc within the 25000 tokens of one Claude Code read
```

## Goals

### Objectives

#### O1: The core docs without a long talk

A new project gets its whole doc set without the talk dragging on.

**Want:** the risk that the user wants the docs and not the talk.

**Checks:** [F1.3: Talk each doc through](features/F1-writing-the-docs-with-you.md#f13-talk-each-doc-through)

**Acceptance:** a new project's 7 core docs are drafted and approved within N hours of talk. N stays open while [The time limit for O1: The core docs without a long talk](TODO.md#p1discussion-the-time-limit-for-o1-the-core-docs-without-a-long-talk) is open.

**Status:** ⬜

#### O2: Context survives compaction

What was decided stays known after the window is compacted.

**Want:** context that outlives the window.

**Checks:**

- [F2.1: Keep the context while you work](features/F2-keeping-the-context.md#f21-keep-the-context-while-you-work)
- [DESIGNS 2: The docs are the state](DESIGNS.md#2-the-docs-are-the-state)

**Acceptance:** after N rounds of work in a real run, compact the window and ask the agent questions that were answered before it. One wrong answer fails. N stays open while [How to evaluate the skill](TODO.md#p2discussion-how-to-evaluate-the-skill) is open.

**Status:** ⬜

### Measures

#### M1: Reads before it changes

The agent reads the doc that owns a thing before it changes that thing.

**Want:** an agent that reads before it works.

**Checks:** [F2.1: Keep the context while you work](features/F2-keeping-the-context.md#f21-keep-the-context-while-you-work)

**How:** every change in the last 3 windows of work before the checkpoint, each read for whether the owning doc was read first.

**Formula:**

```
M1 (%) = 100 × changes made after reading the owning doc / all changes in the sample
```

**Last value:** not measured.

#### M4: Docs that fell behind

At a checkpoint the docs still say what the project is.

**Want:** the risk that the docs fall behind the work.

**Checks:**

- [F1.7.2: Find the docs that fell behind](features/F1-writing-the-docs-with-you.md#f172-find-the-docs-that-fell-behind)
- [DESIGNS 2: The docs are the state](DESIGNS.md#2-the-docs-are-the-state)

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

**Checks:**

- [F1: Writing the docs with you](features/F1-writing-the-docs-with-you.md)
- [F3: Getting the docs](features/F3-getting-the-docs.md)

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

**Checks:**

- [F1: Writing the docs with you](features/F1-writing-the-docs-with-you.md)
- [F2: Keeping the context](features/F2-keeping-the-context.md)
- [F3: Getting the docs](features/F3-getting-the-docs.md)

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

[SKILL.md](skills/what-we-build/SKILL.md) is read each time the skill starts, so it stays short enough to read in full.

**Want:** the risk that the skill itself grows too long.

**Checks:** [DESIGNS 1: A short core with detail beside it](DESIGNS.md#1-a-short-core-with-detail-beside-it)

**Limit:** the body of [SKILL.md](skills/what-we-build/SKILL.md) under 5000 tokens, the size [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) gives for a skill's instructions.

**How:** estimate the tokens of the body as its bytes divided by 3. A token of English text holds more than 3 bytes, so the estimate errs high.

**Status:** ✅ about 4685 tokens from 14057 bytes on 2026-11-05.

#### T8: A doc read in one go

The agent re-reads a whole doc before any edit, so one read must return all of it.

**Want:** docs a person can read.

**Checks:** [F2.1: Keep the context while you work](features/F2-keeping-the-context.md#f21-keep-the-context-while-you-work)

**Limit:** every doc within 25000 tokens, the default limit of one read that the [Claude Code docs](https://code.claude.com/docs/en/env-vars) give.

**How:** a doc under 25000 bytes passes, since it never has more tokens than bytes. A larger doc passes when one Claude Code read with no offset returns all of it.

**Status:** ✅ 2026-11-05, with every doc under 25000 bytes and CHANGELOG.md the largest at 24790 bytes.
