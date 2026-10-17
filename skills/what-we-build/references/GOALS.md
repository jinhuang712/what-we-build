# GOALS.md

GOALS.md turns the wants in the proposal into numbers. A goal here is something a script, a benchmark or the user's own use can confirm or refute on a given day. It keeps the project honest: when someone claims progress, this is where the claim is tested. ROADMAP.md uses these goals as its exit criteria.

It comes fourth in a session: it turns the proposal's wants into numbers, and sets the numbers that DESIGNS left open. A fact belongs here when it can be checked with a number.

**Owns:** two kinds of number. Goals are checks that pass or fail, each with an ID, the want it serves, a measure, a method, where it was measured, and a status. Benchmarks are numbers the project tracks, each with what it is compared with, a method and its last measured value.

**Leaves out:** anything vague, non-goals (FEATURES.md → *Not planned*), how anything works.

**Push back on:** an adjective where a number belongs, a goal with no method, a "met" with no evidence, a threshold made up for a number that only needs tracking, a benchmark with nothing to compare it with, and a number nobody can reproduce.

## Two kinds of number

Some numbers are checks. "No conversation is lost after a crash" passes or fails, and its number follows from what it is: 0 lost, or 100% recovered. Other numbers only mean something next to another number. "Time per request" is 12 ms. Is that good? Alone it says nothing. Next to the previous release, or next to the time the network takes anyway, it says a lot.

So GOALS holds both, and keeps them apart:

- **A goal** is a check that passes or fails. Its threshold comes from the want it serves, and a goal that cannot fail guides no decision.
- **A benchmark** is a number the project tracks. It names what it is compared with: the previous release, another way of doing the same job, or the larger cost it is a share of.

A threshold invented for a number that only needs tracking is a guess that looks like a decision. In one session, the doc set turned its goals into goals and benchmarks, because most of its numbers meant something only against a reference.

## Numbers that can be checked again

- **Name how to reproduce each measured number:** the script, the command or the run. A number that nobody can produce again is withdrawn, and every doc that copied it changes in the same edit. In one session, a binary size had been recorded with no script behind it. A later run could not reproduce it, and the goals withdrew it, while the proposal still quoted the old number.
- **Measure on work that looks like real use.** A benchmark on a toy task says little about the real one. In one session, the user asked for at least one small task of real work before the numbers meant anything.
- **Measure what the reader pays for,** in the reader's own terms. A cost estimate from a third-party price list is weaker than the cost the user actually sees on their own account.

## Guidelines

- **Start from the proposal's wants,** and name the want in each goal. Each want gets a goal, or a row that says why it cannot be measured yet. Without the link, wants and goals drift apart unnoticed.
- **Say where each goal was measured:** this repo, a named project, a benchmark. A goal met on one project and required on another is still open for the second.
- **Write a goal's measure as a threshold with a unit,** because a threshold can fail, and only a goal that can fail guides a decision.
- **Name the method:** who or what measures it, and how often. A goal nobody measures drifts into a wish.
- **Keep a goal without a number visibly open** ("number not set"). Leaving it out hides the gap.
- **Change a status only with evidence:** the measurement and its date. "Met" without evidence is the most expensive word in the doc.
- **Keep the goals few.** Drop a goal that would not change any decision.

## Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "Pages load fast." | "The home page loads in < 1 s on a mid-range phone, measured by the weekly Lighthouse run." | A number, a unit, a method |
| "Easy to set up." | "A new user sends a first invoice in < 5 minutes, watched in 5 test sessions." | Something you can watch happen |
| "Backups always work." | "0 failed restores in a month of weekly restore tests." | A count and a period |
| Goal: "Each request takes < 5 ms." | Benchmark: "Time per request, compared with the previous release and with the network's own time." | Tracked against a reference, not a made-up line |
| "Binary: 4 MB." with no source | "Binary: 7 MB, from `scripts/size.sh`, 2026-10-02." | A number someone can produce again |

## Explore

**Brainstorm to open:** for each want, list every way it could be measured. Then keep the cheapest measure that would still change a decision.

1. For each want in PROPOSAL: how would we know it is true?
2. Does the number pass or fail on its own, or does it mean something only next to another number? The first is a goal, the second a benchmark.
3. For a goal: what is the threshold? When the user has no number yet, the goal is listed as open with "number not set".
4. For a benchmark: what is it compared with?
5. What measures it, how often, and on what work? Is that work close to real use?
6. What is its status today? Met only with evidence, the date it was measured and how to measure it again.

## Skeleton

```markdown
# Goals

GOALS holds two kinds of number: goals that pass or fail, and benchmarks tracked against a reference. <One or two sentences: where and how the numbers are measured.>

## Goals

| # | Goal | Want | Measure | Method | Measured on | Status |
|---|---|---|---|---|---|---|
| G1 | <short name> | <the proposal's want> | <threshold with a unit> | <who or what measures it> | <project or benchmark> | ⬜ Open |

## Benchmarks

| # | Benchmark | Compared with | Method | Last measured |
|---|---|---|---|---|
| B1 | <short name> | <the previous release, another way, or the larger cost> | <the script or run that measures it> | <value and date, or "not measured"> |
```

## Style

A short intro, then two tables: the goals, then the benchmarks. No other prose: the tables are the doc.

## Done when

Every goal has a threshold or says "number not set", every benchmark names what it is compared with, every row names its method, every measured number says how to reproduce it, every "met" has evidence and a date, and ROADMAP's exit criteria can point to these IDs.
