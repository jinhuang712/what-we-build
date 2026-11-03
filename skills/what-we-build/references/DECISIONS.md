# specs/decisions/

The decisions folder records the forks the project took:

- What we chose.
- What we did not choose.
- Why.

It keeps the reason alive after the people who knew it have moved on. One decision is one short file. DESIGNS, FEATURES and the specs link to it instead of retelling it.

**Owns:**

- Each decision.
- Its alternatives.
- What it costs.

A decision about the whole design and a decision about one feature live in the same folder.

**Leaves out:**

- How the chosen thing works (`specs/`).
- What the user sees (FEATURES).
- What changed in a release (CHANGELOG).

## Decision

A decision needs all three of its [YES] lines.

- [YES] a fork where another way was open.
- [YES] a choice someone may later want to undo.
- [YES] a reason the code does not show.
- [NO] a change that only says what changed, which CHANGELOG holds.
- [NO] a commitment every design must meet, which DESIGNS holds.

## Guidelines

- **Keep the title to the choice in one line,** such as "Settings live in JSON files instead of a settings screen".
- **Put the reason in the file, not the title.**
- **Keep a file short and numbered,** so the folder lists the decisions in order.

## You have it when

- A reader can tell what was chosen and what was not without asking.
- The reason is one the code cannot show.

## Skeleton

```markdown
# NNN. <the choice, as a statement>

Decided: YYYY-MM-DD

## The problem

<what forced a choice>

## The choice

<what we chose>

## Not chosen

<each alternative, and why not>

## Consequences

<what it costs, and what follows from it>
```
