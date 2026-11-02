# GOALS.md

GOALS.md turns the wants in the proposal into checks. It keeps the project honest: when someone claims progress, this is where the claim is tested. ROADMAP uses these goals as its exit criteria.

**Owns:**

- The goals of each kind, each with how it is checked.
- When each goal is checked.
- The last result of each check, with its date.

**Leaves out:**

- Anything vague.
- Features the project will not build (FEATURES → *Not planned*).
- How anything works (`specs/`).
- The commitment behind a constraint (DESIGNS), which the constraint links to.

**Push back on:**

- An adjective where a number belongs.
- An objective with no acceptance test.
- A threshold with no limit.
- A comparison with nothing to compare against.
- A constraint nobody could check.
- A "met" with no evidence.

## The six kinds

A project uses the kinds it needs and leaves out the rest.

### Objective

An objective is a result the project must reach. It passes or fails by its acceptance test, such as a headless run from one command.

### Measure

A measure is something watched while the work goes on. It has no pass or fail, such as how full the window gets in a long sitting.

### Benchmark

A benchmark scores the project on a fixed problem set. Its score is tracked over time, such as the score on a public set of coding tasks.

### Comparison

A comparison runs the same work with this project and with another tool. It shows where the project stands, not whether it passes.

### Threshold

A threshold is a limit the product must never cross. It fails the moment it is crossed, such as a package over 100 MB.

### Constraint

A constraint is a rule the work itself must keep, not a feature left out. It fails the moment it is broken, such as a dependency outside the standard library.

## When to check

Every goal stands all the time, but its check runs only at a moment that calls for it. A check is worth its cost once enough has landed, such as at the end of a checkpoint or before a release. At each checkpoint, go through the whole sheet. A small change runs no goal check, because the rules it touched are checked where they live.

## Guidelines

- **Give each goal an ID that never changes,** so ROADMAP can point to it.
- **Let the letter of the ID name its kind,** as the skeleton shows.
- **Open with a Summary,** a tree of every goal by kind with its status and a short description.
- **Write under each label what the goal needs,** in whatever form fits.
- **Mark a goal met only with evidence** from someone who did not write the change.
- **Say where and when each number was measured.**
- **Leave a number open when it is not known.**

## You have it when

- Every goal sits under its kind and names when it is checked.
- Every objective has an acceptance test.
- Every threshold has a limit.
- Every comparison names what it is compared against.
- Every "met" has evidence and a date.
- ROADMAP can point its exit criteria to these IDs.

## Skeleton

```markdown
# Goals

<where and how the goals are checked>

## Summary

**Objectives**

- ⬜ [O1: <name>](#o1-one-sentence-name): <a short description>

## Goals

### Objectives

#### O1: <one sentence name>

<short description>

**Want:** <the wants or risks in PROPOSAL it serves>

**Acceptance:** <the test that passes or fails>

**Checked:** <each checkpoint or a release, and how>

**Status:** ⬜ | ✅ <date> | ❌ <date>

### Measures

#### M1: <one sentence name>

<short description>

**How:** <how it is measured>

**Checked:** <each checkpoint or a release>

**Last value:** <value> on <date>

### Benchmarks

#### B1: <one sentence name>

<short description>

**Problem set:** <the fixed set it is scored on>

**Checked:** <each checkpoint or a release>

**Last score:** <score> on <date>

### Comparisons

#### C1: <one sentence name>

<short description>

**Against:** <the tool it is compared with>

**How:** <how both runs are made and scored>

**Checked:** <each checkpoint or a release>

**Last result:** <result> on <date>

### Thresholds

#### T1: <one sentence name>

<short description>

**Limit:** <the limit never crossed>

**How:** <how it is checked>

**Checked:** <each checkpoint or a release>

**Status:** ⬜ | ✅ <date> | ❌ <date>

### Constraints

#### R1: <one sentence name>

<short description>

**Rule:** <the commitment in DESIGNS, as a link>

**How:** <how it is checked>

**Checked:** <each checkpoint or a release>

**Status:** ⬜ | ✅ <date> | ❌ <date>
```
