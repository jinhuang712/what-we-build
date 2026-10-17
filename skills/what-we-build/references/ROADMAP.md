# ROADMAP.md

ROADMAP.md answers "when?" and "how far along?". It breaks the work into milestones, each a usable or proven state of the project, and shows where the work stands. A reader checks it to see what comes next and whether a milestone is done. It schedules features. It does not describe them.

It comes sixth in a session: it schedules the features into milestones, and its exit criteria point to the goals. A fact belongs here when it is about when, or about progress.

**Owns:** milestones in order, their tasks with IDs, progress (including "not yet used in real life"), exit criteria that point to GOALS, and the design questions still open: a design discussion before the milestone it blocks, and the features waiting for design.

**Leaves out:** feature behavior, the *Later* list (FEATURES), the answers to design questions once decided (DESIGNS, or FEATURES for one feature), release notes (CHANGELOG).

**Push back on:** a milestone nobody could use, exit criteria that restate goals instead of pointing to them, build logs in task rows, and a milestone that starts building before the design it needs is decided.

## Guidelines

- **Make each milestone a usable or proven state,** not a pile of tasks. "Users can sign up and pay" can be used. "Beats working without the tool on goals G2–G5" can be proven. "Polish" is neither.
- **Make the first milestone small enough to finish soon.** A first milestone that drags makes the whole plan look unreal.
- **Point exit criteria at goal IDs** instead of restating them, so the measure lives in one place.
- **Give tasks IDs** (M1.1) that branches and commits can use, so the work traces back to the plan.
- **Keep one row per task, short enough to scan down the table.** Logs of how a task was built and checked belong in git.
- **Schedule the open design questions.** A question that blocks a milestone gets a design discussion right before it, with its own exit: the user approves the decisions, which then move to DESIGNS, or to FEATURES when they concern one feature. A feature that needs a design before it can get a milestone waits in a *Waiting for design* table, with what it depends on and when it will be discussed. Each open question then has one home, beside the work it blocks, and the current milestone can close without it. In one session, the user parked every feature that still needed design in the roadmap, to finish the current phase first.

## Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "M2: Polish." | "M2 Users can sign up and pay. Exit: GOALS.md G3." | A usable state, and a checkable exit |
| "M1.3 Built 2026-10-07 after three mockups. Checked on every screen size ..." | "M1.3 Sign-up form." | One row, no log |

## Explore

**Brainstorm to open:** list the versions of the project someone could use every day, from the smallest up. Then pick the smallest one as the first milestone.

1. What is the smallest version that is useful every day? That is the first milestone.
2. What comes next, and what does each milestone depend on?
3. For each milestone: which goals must be met to call it done?
4. Which tasks make up each milestone?
5. Which design questions must be answered before a milestone starts? Which features still need a design before they can be scheduled? Bring in the open questions parked in TODO.md.

## Skeleton

```markdown
# Roadmap

**Current milestone:** M1. <one line>

## Overview   (table: milestone → delivers → features → depends on → status)

## M1 — <name> ⬜

| ID | What it delivers | Note |
|---|---|---|

**Exit criteria:** GOALS.md G1 and G3.

## Design discussion before M2 ⬜

| ID | Question | Note |
|---|---|---|
| D2.1 | <a design question that blocks M2> | |

**Exit criteria:** the user approves the decisions.

## M2 — <name> ⬜

...

## Waiting for design   (table: feature → depends on → discussed)

## Later

See FEATURES.md → Later, if needed.
```

## Style

A status board: one overview table, then one table per milestone, with a design discussion before a milestone that needs one. The features waiting for design come after the milestones, before *Later*.

## Done when

Every milestone has exit criteria tied to goals, the first milestone is small enough to finish soon, and every open design question sits before the milestone it blocks or in *Waiting for design*.
