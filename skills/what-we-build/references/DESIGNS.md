# DESIGNS.md

DESIGNS.md holds the project's design guidelines: the few hard commitments the whole design is built around.
Its reader is a developer about to change the code or propose something new.
A guideline is concrete and not up for negotiation.
A reader can check any design against it and name the one it breaks.

It comes third in a session, right after the philosophy.
The design guides the features, so it comes before them.

**Owns:**

- The guidelines, numbered and one line each.
- Under each: why it holds and what it costs.
- Under each: the question it asks of a new requirement.
- Under each: links to its decisions and specs.

**Leaves out:**

- The choices made to meet a guideline (`specs/decisions/`).
- How the thing works (`specs/`).
- What the user sees (FEATURES).
- Whether it is built yet (ROADMAP).
- Open questions (TODO).

**Push back on:**

- A guideline every team would sign ("keep it simple").
- A guideline that reads like a feature.
- A guideline that is really a mechanism.

## Guidelines

- **Open with the numbered guidelines, one line each.** A reader then sees the whole design at a glance.
- **State each one as a commitment a reader can test.** "Every payment can be retried safely" is testable. "Payments are reliable" is not.
- **Give each a short section** on why it holds and what it costs.
- **End each section with an Ask: line** and links to its decisions and specs.

## You have it when

- A reader can check a new design against the guidelines and name the one it breaks.
- Every guideline names its cost and has an **Ask:** line.
- Nothing in it is a mechanism or a feature.

## Skeleton

```markdown
# Designs

<one paragraph: what goes in and out, and the shape between>

<Name> is designed around <N> guidelines:

1. **<guideline>.** <one line>

## 1. <guideline>

<why it holds, and what it costs>

**Ask:** <the question it asks of a new requirement>

- **Decisions:** <links to specs/decisions/>
- **How it works:** <links to specs/>
```
