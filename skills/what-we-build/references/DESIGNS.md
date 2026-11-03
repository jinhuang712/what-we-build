# DESIGNS.md

DESIGNS.md holds the project's design guidelines: the few hard commitments the whole design is built around. Its reader is a developer about to change the code or propose something new. A guideline is concrete and not up for negotiation. A reader can check any design against it and name the one it breaks.

It comes third in the doc order, right after the philosophy. The design guides the features, so it comes before them.

## What it holds

Point anything a [NO] line rules out to its home, or push back when it has none.

- [YES]   the guidelines in a numbered list.
- [YES]   why each holds and what it costs.
- [YES]   the question each asks of a new requirement.
- [YES]   links from each to its decisions and specs.
- [NO]    the choices made to meet a guideline, which `specs/decisions/` holds.
- [NO]    how the thing works, which `specs/` holds.
- [NO]    whether it is built yet, which ROADMAP holds.
- [NO]    open questions, which TODO holds.

## Guideline

- [YES]   a commitment a reader can check a design against, such as *an action that cannot be undone asks the user first*.
- [NO]    a stance about what problem to solve, which PHILOSOPHY holds.
- [NO]    a choice between options that a decision records, such as *settings live in JSON files*.
- [NO]    a mechanism, such as *a hook runs before each tool call*.
- [NO]    a feature, such as *resume a session*.
- [NO]    a value every team would sign, such as *keep it simple*.

## How to write it

- [YES]   open with the numbered guidelines so a reader sees the whole design at a glance.
- [YES]   give each a short section on why it holds and what it costs.
- [YES]   give each the question it asks of a new requirement.
- [NO]    a guideline with its cost left out.

## You have it when

- A reader can check a new design against the guidelines and name the one it breaks.
- Every guideline names its cost and the question it asks.
- Nothing in it is a mechanism or a feature.

## Skeleton

```markdown
# Designs

<one paragraph: what goes in and out, and the shape between>

<Name> is designed around <N> guidelines:

1. **<guideline>:** <its gist>

## 1. <guideline>

<why it holds, and what it costs>

**Ask:** <the question it asks of a new requirement>

- **Decisions:** <links to specs/decisions/>
- **How it works:** <links to specs/>
```
