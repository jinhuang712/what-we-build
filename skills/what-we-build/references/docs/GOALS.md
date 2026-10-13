# GOALS.md

GOALS.md turns the wants in the proposal into checks. A goal here is something a script, a benchmark or the user's own use can confirm or refute on a given day. It keeps the project honest: when someone claims progress, this is where the claim is tested. ROADMAP.md uses these goals as its exit criteria.

It comes third in a session: it turns the proposal's wants into numbers. A fact belongs here when it can be checked with a number.

**Owns:** goals as checks, each with an ID, the want it serves, a measure with a number, a method, where it was measured, and a status.

**Leaves out:** anything vague, non-goals (FEATURES → *Not planned*), how anything works.

**Push back on:** an adjective where a number belongs, a goal with no method, and a "met" with no evidence.

## Guidelines

- **Start from the proposal's wants,** and name the want in each row. Each want gets a goal, or a row that says why it cannot be measured yet. Without the link, wants and goals drift apart unnoticed.
- **Say where each goal was measured:** this repo, a named project, a benchmark. A goal met on one project and required on another is still open for the second.
- **Write the measure as a threshold with a unit,** because "fast" can't fail, and a goal that can't fail can't guide a decision.
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

## Explore

**Brainstorm to open:** for each want, list every way it could be measured. Then keep the cheapest measure that would still change a decision.

1. For each want in PROPOSAL: how would we know it is true?
2. What number, measured how? Who or what measures it, and how often?
3. What is the threshold? When the user has no number yet, the goal is listed as open with "number not set".
4. What is its status today? Met only with evidence and the date it was measured.

## Skeleton

```markdown
# Goals

Each goal is a check with a number. <One or two sentences: where and how the goals are measured.>

| # | Goal | Want | Measure | Method | Measured on | Status |
|---|---|---|---|---|---|---|
| G1 | <short name> | <the proposal's want> | <threshold with a unit> | <who or what measures it> | <project or benchmark> | ⬜ Open |
```

## Style

A short intro, then one table of checks: ID, goal, want, measure, method, where measured, status. No other prose: the table is the doc.

## Done when

Every row has a number or says "number not set", every row names its method, every "met" has evidence and a date, and ROADMAP's exit criteria can point to these IDs.
