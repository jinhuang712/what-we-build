# GOALS.md

GOALS.md turns the wants in the proposal into checks.
It keeps the project honest: when someone claims progress, this is where the claim is tested.
ROADMAP uses these goals as its exit criteria.

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

| Kind | Answers | Passes or fails |
|---|---|---|
| Objective | What result must we reach? | Yes, by its acceptance test |
| Measure | What do we watch while we work? | No |
| Benchmark | What do we score on a fixed problem set? | No |
| Comparison | How do we stand against other tools? | No |
| Threshold | What limit must the product never cross? | Yes, the moment it is crossed |
| Constraint | What must we never do along the way? | Yes, the moment it is broken |

A project uses the kinds it needs and leaves out the rest.
A constraint is not a feature left out.
It is a rule the work itself must keep.

## When to check

The goals always stand, but not every check runs every time.
Each goal names when it is checked.

| Cadence | Fits | Why |
|---|---|---|
| Every change | Cheap measures, thresholds and constraints | They cost little and catch a slip at once |
| End of a phase | Objectives, benchmarks and comparisons | A large run is worth it only once enough features have landed |

- A small change does not run a benchmark or a comparison.
- At the end of each phase, go through the whole sheet.

## Guidelines

- **Give each goal an ID that never changes,** so ROADMAP can point to it.
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

## Objectives

| # | Objective | Want | Acceptance | Checked | Status |
|---|---|---|---|---|---|

## Measures

| # | Measure | How it is measured | Checked | Last value |
|---|---|---|---|---|

## Benchmarks

| # | Benchmark | Problem set | Checked | Last score |
|---|---|---|---|---|

## Comparisons

| # | Comparison | Against | How it is run | Checked | Last result |
|---|---|---|---|---|---|

## Thresholds

| # | Threshold | Limit | How it is checked | Checked | Status |
|---|---|---|---|---|---|

## Constraints

| # | Constraint | How it is checked | Checked | Status |
|---|---|---|---|---|
```
