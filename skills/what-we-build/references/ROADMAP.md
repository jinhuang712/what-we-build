# ROADMAP.md

ROADMAP.md answers "when?" and "how far along?". It breaks the work into checkpoints, each a usable or proven state of the project. It shows where the work stands. It schedules features and does not describe them.

## What it holds

Point anything a [NO] line rules out to its home, or push back when it has none.

- [YES] checkpoints in order.
- [YES] their tasks and progress.
- [YES] exit criteria that point to GOALS.
- [NO] feature behavior and the *Later* list, which FEATURES holds.
- [NO] open questions, which TODO holds.
- [NO] their answers once decided, which `specs/decisions/` holds.
- [NO] release notes, which CHANGELOG holds.
- [NO] exit criteria that restate goals instead of pointing to them.
- [NO] a checkpoint that starts building before its design is decided.

## Checkpoint

- [YES] a state someone can use or a claim it proves, such as *a session survives a restart*.
- [NO] a bag of tasks, such as *bugs found last week*.
- [NO] a date or a version alone.
- [MAYBE] a release, when it ships what the checkpoint delivers.

## How to write it

- [YES] open with a Summary, an ASCII tree in a code block of every checkpoint and its items with their status.
- [YES] keep the first checkpoint small enough to finish soon.

## You have it when

- A reader knows what comes next and what done means for it.
- Every checkpoint's exit criteria point to GOALS.

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

<each item with its status>

**Exit criteria:** <links to the goals>
````
