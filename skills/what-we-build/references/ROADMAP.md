# ROADMAP.md

ROADMAP.md answers "when?" and "how far along?". It breaks the work into checkpoints, each a usable or proven state of the project. It shows where the work stands. It schedules features and does not describe them.

**Owns:**

- Checkpoints in order.
- Their tasks and progress.
- Exit criteria that point to GOALS.

**Leaves out:**

- Feature behavior and the *Later* list (FEATURES).
- Open questions (TODO).
- Their answers once decided (`specs/decisions/`).
- Release notes (CHANGELOG).

**Push back on:**

- A checkpoint nobody could use.
- Exit criteria that restate goals instead of pointing to them.
- A checkpoint that starts building before its design is decided.

## Guidelines

- **Open with a Summary,** an ASCII tree in a code block of every checkpoint and its items with their status.
- **Keep the first checkpoint small enough to finish soon.**
- **Point exit criteria to GOALS.**

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
