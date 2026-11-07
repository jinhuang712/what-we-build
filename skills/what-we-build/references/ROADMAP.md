# ROADMAP.md

ROADMAP.md answers "when?" and "how far along?". It breaks the work into checkpoints, each a usable or proven state of the project. It shows where the work stands. It schedules features and does not describe them.

## What is it

Point anything a [NO] line rules out to its home, or push back when it has none.

- [YES]   checkpoints in order.
- [YES]   their tasks and progress.
- [YES]   exit criteria that point to GOALS.
- [YES]   let each checkpoint name the goals it runs, such as cost and speed at every checkpoint.
- [YES]   record each goal's result and date beside it once the checkpoint runs it.
- [YES]   open with a Summary, an ASCII tree in a code block of every checkpoint and its items with their status.
- [YES]   keep the first checkpoint small enough to finish soon.
- [YES]   a heading for each checkpoint and each sub-checkpoint, with its status on a **Status:** line below it.
- [YES]   split a checkpoint that delivers more than one feature group into sub-checkpoints.
- [YES]   exit criteria of its own for each sub-checkpoint.
- [YES]   a **Delivers:** list in each checkpoint with each feature it delivers, linked.
- [YES]   every feature not yet built in a checkpoint.
- [YES]   a last checkpoint for the features that wait for a need.
- [YES]   link an open question of a checkpoint to its TODO item.
- [YES]   exit criteria as bullets grouped by the kind of goal, one goal to a bullet.
- [YES]   a group headed *Do not hold the release* for goals that are checked but do not block it.
- [NO]    feature behavior, which FEATURES holds.
- [NO]    open questions, which TODO holds.
- [NO]    their answers once decided, which `specs/decisions/` holds.
- [NO]    release notes, which CHANGELOG holds.
- [NO]    a finished checkpoint folded into a summary.
- [NO]    a checkpoint that starts building before its design is decided.
- [NO]    a sub-checkpoint's goal repeated in its parent, since a parent's exit criteria say only that its sub-checkpoints are met.
- [NO]    a recorded result rewritten after the checkpoint ends.
- [NO]    a link to any doc but GOALS, FEATURES and TODO.
- [WHEN]  its sub-checkpoints list what they deliver: the parent lists none.
- [WHEN]  a goal fails after a checkpoint met it: keep the checkpoint's record and add an `ISSUE` to `TODO.md`.

## Checkpoint

- [YES]   a state someone can use or a claim it proves, such as *a session survives a restart*.
- [NO]    a bag of tasks, such as *bugs found last week*.
- [NO]    a date or a version alone.
- [MAYBE] a release, when it ships what the checkpoint delivers.

## You have it when

- A reader knows what comes next and what done means for it.
- Every checkpoint's exit criteria point to GOALS.
- Every finished checkpoint shows each goal's result and date.

## Skeleton

````markdown
# Roadmap

**Current checkpoint:** <a link to it>. <where the work stands>

## Summary

```
Roadmap
└── ⬜ CP1: <name> — <what it delivers>
    └── ⬜ CP1.1: <an item>
```

## CP1: <name>

**Status:** ⬜

<where it stands>

**Delivers:**

- <a feature ID with its name, linked to FEATURES>

**Exit criteria:**

- **Sub-checkpoints**
  - <a sub-checkpoint ID with its name, linked> is met.
- **Do not hold the release**
  - <a goal ID with its name, linked>: <mark, result and date once it runs>

### CP1.1: <name>

**Status:** ⬜

<what it does>

**Exit criteria:**

- **Objectives**
  - <a goal ID with its name, linked>: <mark, result and date once it runs>
- **Benchmarks**
  - <a goal ID with its name, linked>: <mark, result and date once it runs>
````
