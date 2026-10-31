# DESIGNS.md

DESIGNS.md holds the project's design guidelines: the few hard commitments the whole design is built around. Its reader is a developer about to change the code or propose something new. A guideline is concrete and not up for negotiation, so a reader can check any design against it and name the one it breaks.

It comes third in a session, right after the philosophy, because the design guides the features.

**Owns:** the guidelines, numbered, one line each. Under each: why it holds, what it costs, the question it asks of a new requirement, and links to its decisions and specs.

**Leaves out:** the choices made to meet a guideline (`specs/decisions/`), how the thing works (`specs/`), what the user sees (FEATURES), whether it is built yet, and open questions.

**Push back on:** a guideline every team would sign ("keep it simple"), one that reads like a feature, and one that is really a mechanism.

## Guidelines

- **Open with the guidelines, numbered, one line each,** so a reader sees the whole design at a glance.
- **State each one as a commitment a reader can test.** "Every payment can be retried safely" is testable. "Payments are reliable" is not.
- **Give each a short section:** why it holds and what it costs, an **Ask:** line, and links to its decisions and specs.

## You have it when

- A reader can check a new design against the guidelines and name the one it breaks.
- Every guideline names its cost and has an **Ask:** line.
- Nothing in it is a mechanism or a feature.

## Skeleton

```markdown
# Designs

<one paragraph: what goes in, what comes out, and the shape between>

<Name> is designed around <N> guidelines:

1. **<guideline>.** <one line>

## 1. <guideline>

<why it holds, and what it costs>

**Ask:** <the question it asks of a new requirement>

- **Decisions:** <links to specs/decisions/>
- **How it works:** <links to specs/>
```
