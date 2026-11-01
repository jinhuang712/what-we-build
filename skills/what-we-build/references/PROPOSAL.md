# PROPOSAL.md

The proposal is where the project begins: the case for why it should exist.
It says what gap the project fills and why now.
It gives the idea that fills the gap.
A reader finishes it knowing whether the project is worth building.

It comes first, because every other doc builds on the reason it gives.

**Owns:**

- Why the project should exist.
- Why now.
- The idea.
- What we want.
- What we don't want.
- Who it is for.
- The risks.

**Leaves out:**

- How it is built (DESIGNS).
- Exact behavior (FEATURES).
- The numbers (GOALS).
- Progress (ROADMAP).
- The index of docs (README).

**Push back on:**

- A case that opens with the solution.
- A reason with no example.
- A want that serves no reason.
- A "don't want" with no reason.

## Guidelines

- **Start from what the user brings.** It can take any form.
- **When the project eases a pain, list each pain** with the moment or number that proves it.
- **Show the reason** with a moment, a number or a sample.
- **Argue the case.** Every section should make it stronger.
- **Write *Why now* only when something changed.**

## You have it when

- A stranger can say after one reading why the project should exist.
- Every want traces to the reason the project exists.
- The user recognizes the case as their own.

## Skeleton

```markdown
# <Name> — Proposal

> <tagline>

## In short
<a scene the reader knows, then the one-line answer>

## Why it should exist
<the reason in the user's own form, shown with an example>

### Pain points
<when the project eases a pain>
1. **<the pain, one line>.** <the moment or number that proves it>

## Why now
<what changed that makes it possible or urgent. Leave it out when nothing did>

## The idea
**<one sentence>.** <what it means>

## What we want
- **<what someone needs>.** <how the project meets it>

## What we don't want
- **<what the project refuses to become>.** <the reason>

## Who it is for
<the people, and what each gets>

## Risks
| Risk | What reduces it |
|---|---|
| <risk> | <mitigation> |
```
