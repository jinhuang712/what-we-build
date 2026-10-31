# GOALS.md

GOALS.md turns the wants in the proposal into numbers. It keeps the project honest: when someone claims progress, this is where the claim is tested. ROADMAP uses these goals as its exit criteria.

**Owns:** objectives with thresholds, and benchmarks with comparisons, each with its measurement.

**Leaves out:** anything vague, non-goals (FEATURES → *Not planned*), and how anything works (`specs/`).

**Push back on:** an adjective where a number belongs, an objective with no measurement, a threshold made up for a number that only needs tracking, a benchmark with no comparison, and a "met" with no evidence.

## The five parts

| Part | Means |
|---|---|
| Objective | What we want to achieve, tied to a want in the proposal. |
| Measurement | What we measure and how: the metric, the script or the run. |
| Threshold | The line between pass and fail, with a unit. Leave it open when it is not known. |
| Benchmark | A number we track over time, with no pass or fail. |
| Comparison | What a benchmark is compared with: the previous release, another tool, or the larger cost. |

An objective has a measurement and a threshold. A benchmark has a measurement and a comparison.

## Guidelines

- **Mark an objective met only with evidence** from someone who did not write the change.
- **Say where and when each number was measured.**

## You have it when

- Every objective has a measurement and a threshold, or says the threshold is open.
- Every benchmark has a comparison.
- Every "met" has evidence and a date.
- ROADMAP can point its exit criteria to these IDs.

## Skeleton

```markdown
# Goals

<where and how the numbers are measured>

## Objectives

| # | Objective | Want | Measurement | Threshold | Status |
|---|---|---|---|---|---|
| G1 | <short name> | <the proposal's want> | <metric, and the script or run> | <number with a unit> | ⬜ |

## Benchmarks

| # | Benchmark | Measurement | Comparison | Last value |
|---|---|---|---|---|
| B1 | <short name> | <metric, and the script or run> | <what it is compared with> | <value and date, or "not measured"> |
```
