# ROADMAP.md

ROADMAP.md answers "when?" and "how far along?". It breaks the work into milestones, each a usable or proven state of the project, and shows where the work stands. It schedules features. It does not describe them.

**Owns:** milestones in order, their tasks and progress, exit criteria that point to GOALS, and the design questions still open.

**Leaves out:** feature behavior and the *Later* list (FEATURES), the answers to design questions once decided (`specs/decisions/`), and release notes (CHANGELOG).

**Push back on:** a milestone nobody could use, exit criteria that restate goals instead of pointing to them, and a milestone that starts building before its design is decided.

## Guidelines

- **Keep the first milestone small enough to finish soon.**
- **Put an open design question before the milestone it blocks.**
- **Point exit criteria to GOALS.**

## Skeleton

```markdown
# Roadmap

**Current milestone:** M1. <one line>

## Overview

| Milestone | Delivers | Features | Status |
|---|---|---|---|

## M1 — <name> ⬜

| ID | What it delivers | Note |
|---|---|---|

**Exit criteria:** <GOALS ids>

## Waiting for design
```
