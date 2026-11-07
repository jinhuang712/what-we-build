# Roadmap

Where what-we-build stands and what comes next. Each checkpoint is a usable or proven state of the skill. Its exit criteria name the goals it runs in [GOALS.md](GOALS.md) and hold their results from that checkpoint.

Status: ✅ done · 🟨 in progress · ❔ claimed and not yet run · ⬜ not started.

**Current checkpoint:** [CP2: Rebuilt and proven on a new project](#cp2-rebuilt-and-proven-on-a-new-project). The skill is rebuilt, and none of its three feature groups is proven on a new project yet.

## Summary

```
Roadmap
├── ✅ CP1: Write and publish — the skill and its guides in a public repo
├── 🟨 CP2: Rebuilt and proven on a new project — the rebuilt skill holds up on a project it did not grow from
│   ├── ⬜ CP2.8: The talk is proven — a new project's core docs come out of the talk
│   ├── ⬜ CP2.9: The context is proven — the docs carry the work across windows
│   └── ⬜ CP2.10: The doc set is proven — the docs a project grows into and their layout
└── ⬜ CP4: Proven useful — runs with the skill beat runs without it
    ├── ⬜ CP4.3: Run quality is measured — three prompts scored
    └── ⬜ CP4.4: The skill leads — it beats the same agent without it
```

## CP1: Write and publish

**Status:** ✅

The skill and its guides went into a public repo. GitHub shows the repo as public since 2026-10-12, which proves the release. [T4: A short skill](GOALS.md#t4-a-short-skill) proves only that the skill stays short, and the goal for its features waits on [What a checkpoint is](TODO.md#p1discussion-what-a-checkpoint-is).

**Delivers:**

- [F3.1: The core docs](features/F3-getting-the-docs.md#f31-the-core-docs)
- [F3.3: A guide per doc](features/F3-getting-the-docs.md#f33-a-guide-per-doc)
- [F3.5: Wording rules](features/F3-getting-the-docs.md#f35-wording-rules)

**Exit criteria:**

- **Thresholds**
  - [T4: A short skill](GOALS.md#t4-a-short-skill): no record from when it ended

## CP2: Rebuilt and proven on a new project

**Status:** 🟨

The skill was rebuilt around a project's context in this repo, and it is proven only once it holds up on a new project. Each sub-checkpoint delivers one feature group.

**Exit criteria:**

- **Sub-checkpoints**
  - [CP2.8: The talk is proven](#cp28-the-talk-is-proven) is met.
  - [CP2.9: The context is proven](#cp29-the-context-is-proven) is met.
  - [CP2.10: The doc set is proven](#cp210-the-doc-set-is-proven) is met.

### CP2.8: The talk is proven

**Status:** ⬜

A new project's core docs come out of the talk with the skill.

- Set the time limit in [O1: The core docs without a long talk](GOALS.md#o1-the-core-docs-without-a-long-talk).
- Draft and approve a new project's seven core docs with the skill.
- Read every change in the last three windows for [M1: Reads before it changes](GOALS.md#m1-reads-before-it-changes).

**Delivers:**

- [F1.1: Start from where the project is](features/F1-writing-the-docs-with-you.md#f11-start-from-where-the-project-is)
- [F1.2: Agree the doc set](features/F1-writing-the-docs-with-you.md#f12-agree-the-doc-set)
- [F1.3: Talk each doc through](features/F1-writing-the-docs-with-you.md#f13-talk-each-doc-through)
- [F1.4: Push back](features/F1-writing-the-docs-with-you.md#f14-push-back)
- [F1.5: See the change](features/F1-writing-the-docs-with-you.md#f15-see-the-change)
- [F1.8: Put every doc in the format](features/F1-writing-the-docs-with-you.md#f18-put-every-doc-in-the-format)

**Exit criteria:**

- **Objectives**
  - [O1: The core docs without a long talk](GOALS.md#o1-the-core-docs-without-a-long-talk)
- **Measures**
  - [M1: Reads before it changes](GOALS.md#m1-reads-before-it-changes)

### CP2.9: The context is proven

**Status:** ⬜

The docs carry the work of the new project across windows.

- Compact a window on the new project and ask the agent for the task and the latest decisions.
- Resume the new project in a later window.
- Have a reader who did not write the docs read them against the work.

**Delivers:**

- [F1.7: Resume](features/F1-writing-the-docs-with-you.md#f17-resume)
- [F2.1: Keep the context while you work](features/F2-keeping-the-context.md#f21-keep-the-context-while-you-work)
- [F2.2: A wiki when others build on it](features/F2-keeping-the-context.md#f22-a-wiki-when-others-build-on-it)

**Exit criteria:**

- **Objectives**
  - [O2: Context survives compaction](GOALS.md#o2-context-survives-compaction)
- **Measures**
  - [M4: Docs that fell behind](GOALS.md#m4-docs-that-fell-behind)

### CP2.10: The doc set is proven

**Status:** ⬜

[T8: A doc read in one go](GOALS.md#t8-a-doc-read-in-one-go) is met, and the goal for its features waits on [What a checkpoint is](TODO.md#p1discussion-what-a-checkpoint-is).

**Delivers:**

- [F3.2: Docs that join later](features/F3-getting-the-docs.md#f32-docs-that-join-later)
- [F3.4: A default layout](features/F3-getting-the-docs.md#f34-a-default-layout)

**Exit criteria:**

- **Thresholds**
  - [T8: A doc read in one go](GOALS.md#t8-a-doc-read-in-one-go)

## CP4: Proven useful

**Status:** ⬜

Runs with the skill beat runs without it.

**Delivers:**

- No new feature, since it proves the ones that exist.

**Exit criteria:**

- **Sub-checkpoints**
  - [CP4.3: Run quality is measured](#cp43-run-quality-is-measured) is met.
  - [CP4.4: The skill leads](#cp44-the-skill-leads) is met.

### CP4.3: Run quality is measured

**Status:** ⬜

Three realistic project prompts are chosen and every run on them is scored.

**Exit criteria:**

- **Benchmarks**
  - [B1: Run quality](GOALS.md#b1-run-quality) on all three prompts

### CP4.4: The skill leads

**Status:** ⬜

The skill beats the same agent without it on every prompt.

**Exit criteria:**

- **Comparisons**
  - [C1: With and without the skill](GOALS.md#c1-with-and-without-the-skill) at 3 / 3
