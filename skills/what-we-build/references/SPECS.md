# specs/

The specs folder explains how each part of the project works, like a technical design written for readers outside the team. A spec reads like a short paper: prose that explains, with ASCII diagrams where several parts talk to each other. A reader who has not seen the code can follow how the part works.

**Owns:**

- The mechanism of one part of the project, one file per part.

**Leaves out:**

- What the user sees (FEATURES).
- The guidelines the design must meet (DESIGNS).
- The forks behind it (`specs/decisions/`).

**UIUX is a spec too.** A project with a visual interface keeps `specs/UIUX.md` with the final screens in `prototype/*.html`, and the [UIUX](UIUX.md) guide covers both. Options weighed on the way are process files, and they stay out.

A spec and the code guide each other:

- A spec drafted first guides the code.
- A better implementation updates the spec.
- When they disagree, tell the user and let them decide.

## You have it when

- A reader who has not seen the code can follow how the part works.
- It agrees with the code, or the user knows where it does not.

## Skeleton

```markdown
# <Part>

<what the part does and why it exists, in a paragraph>

<the mechanism in prose, with a diagram>
```
