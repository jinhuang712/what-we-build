# GOALS.md

GOALS.md turns the wants in the proposal into checks. It keeps the project honest: when someone claims progress, this is where the claim is tested. ROADMAP uses these goals as its exit criteria.

**Owns:**

- The goals of each kind, each with how it is checked.
- The last result of each check, with its date.

**Leaves out:**

- Anything vague.
- Features the project will not build (FEATURES → *Not planned*).
- How anything works (`specs/`).
- A commitment the design must meet (DESIGNS).
- A rule for how the work is done (AGENTS.md).
- When each goal is first checked (ROADMAP).

**Push back on:**

- An adjective where a number belongs.
- An objective with no acceptance test.
- A threshold with no limit.
- A number with no formula.
- A comparison with nothing to compare against.
- A constraint nobody could check.
- A rule dressed as a goal.
- A "met" with no measurement or report.

## The six kinds

A project uses the kinds it needs and leaves out the rest.

### Objective

An objective is a result the project must reach. It passes or fails by its acceptance test, such as a headless run from one command.

### Measure

A measure is something watched while the work goes on. It has no pass or fail, such as how full the window gets during long work.

### Benchmark

A benchmark scores the project on a fixed problem set. Its score is tracked over time, such as the score on a public set of coding tasks.

### Comparison

A comparison runs the same work with this project and with another tool. It shows where the project stands, not whether it passes.

### Threshold

A threshold is a limit the product must never cross. It fails the moment it is crossed, such as a package over 100 MB.

### Constraint

A constraint is a condition the product must always meet, checked on the product itself and not on how the work was done. It has no number and fails the moment it no longer holds, such as an app that must run with no network.

## When to check

Every goal stands all the time, but its check runs only at a moment that calls for it. ROADMAP says when it starts: a goal can run from the first checkpoint whose exit criteria point to it. From then on it runs at the end of each checkpoint or before a release, and at those moments you go through every goal that can run. A small change runs no goal check, because the rules it touched are checked where they live.

## Guidelines

- **Give each goal an ID that never changes,** so ROADMAP can point to it.
- **Let the letter of the ID name its kind,** as the skeleton shows.
- **Open with a Summary,** an ASCII tree in a code block of every goal by kind with its status and a short description.
- **Write under each label what the goal needs,** in whatever form fits.
- **Mark a goal met only with a measurement or the user's own report,** with its date.
- **Write the formula of every number in a code block,** with its sample and unit beside it.
- **Say where and when each number was measured.**
- **Leave a number open when it is not known.**

## You have it when

- Every goal sits under its kind.
- Every objective has an acceptance test.
- Every threshold has a limit.
- Every measure, benchmark and comparison has a formula.
- Every comparison names what it is compared against.
- Every "met" has a measurement or the user's report, with its date.
- ROADMAP can point its exit criteria to these IDs.

## Skeleton

````markdown
# Goals

<where and how the goals are checked>

## Summary

```
Goals
└── Objectives
    └── ⬜ O1: <name> — <a short description>
```

## Goals

### Objectives

#### O1: <one sentence name>

<short description>

**Want:** <the wants or risks in PROPOSAL it serves>

**Acceptance:** <the test that passes or fails>

**Status:** ⬜ | ✅ <date> | ❌ <date>

### Measures

#### M1: <one sentence name>

<short description>

**Want:** <the wants or risks in PROPOSAL it serves>

**How:** <the sample it is measured on>

**Formula:**

```
M1 = <what is counted> / <what it is counted over>
```

**Last value:** <value> on <date>

### Benchmarks

#### B1: <one sentence name>

<short description>

**Want:** <the wants or risks in PROPOSAL it serves>

**Problem set:** <the fixed set it is scored on>

**Formula:**

```
B1 = <how the scores of the set combine into one>
```

**Last score:** <score> on <date>

### Comparisons

#### C1: <one sentence name>

<short description>

**Want:** <the wants or risks in PROPOSAL it serves>

**Against:** <the tool it is compared with>

**How:** <how both runs are made and scored>

**Formula:**

```
C1 = <how the two scores are set against each other>
```

**Last result:** <result> on <date>

### Thresholds

#### T1: <one sentence name>

<short description>

**Want:** <the wants or risks in PROPOSAL it serves>

**Limit:** <the limit never crossed>

**How:** <how it is checked>

**Status:** ⬜ | ✅ <date> | ❌ <date>

### Constraints

#### R1: <one sentence name>

<short description>

**Want:** <the wants or risks in PROPOSAL it serves>

**Condition:** <what must always hold>

**How:** <how it is checked>

**Status:** ⬜ | ✅ <date> | ❌ <date>
````
