# GOALS.md

GOALS.md turns the wants in the proposal into numbers. A goal here is something a script, a benchmark or the user's own use can confirm or refute on a given day. It keeps the project honest: when someone claims progress, this is where the claim is tested. ROADMAP uses these goals as its exit criteria.

**Owns:** goals that pass or fail, and benchmarks tracked against a reference, each with its method.

**Leaves out:** anything vague, non-goals (FEATURES → *Not planned*), and how anything works (`specs/`).

**Push back on:** an adjective where a number belongs, a goal with no method, a "met" with no evidence, and a benchmark with nothing to compare it with.

## Guidelines

- **Give a goal a threshold and a method.** Leave the number open when it is not known.
- **Give a benchmark what it is compared with.** A number alone means nothing.
- **Mark a goal met only with evidence** from someone who did not write the change.

## Skeleton

```markdown
# Goals

<where and how the numbers are measured>

## Goals

| # | Goal | Want | Measure | Method | Status |
|---|---|---|---|---|---|

## Benchmarks

| # | Benchmark | Compared with | Method | Last measured |
|---|---|---|---|---|
```
