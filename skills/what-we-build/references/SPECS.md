# specs/

The specs folder explains how each part of the project works, like a technical design written for readers outside the team. A spec reads like a short paper: prose that explains, with ASCII diagrams where several parts talk to each other. A reader who has not seen the code can follow how the part works.

**Owns:** the mechanism of one part of the project, one file per part.

**Leaves out:** what the user sees (FEATURES), the guidelines the design must meet (DESIGNS), and the forks behind it (`specs/decisions/`).

**UIUX is a spec too.** A project with a visual interface keeps `specs/UIUX.md`, which explains how the product looks and moves, and `prototype/*.html`, the final screens. Change them together. Options weighed on the way are process files, and they stay out.

**Add when** a part has a mechanism worth explaining. A spec and the code guide each other: a spec drafted first guides the code, and a better implementation updates the spec. When they disagree, tell the user and let them decide.

## You have it when

- A reader who has not seen the code can follow how the part works.
- It agrees with the code, or the user knows where it does not.
- For UIUX, the pages in `prototype/` show what the rules describe.

## Skeleton

```markdown
# <Part>

<what the part does and why it exists, in a paragraph>

<the mechanism, in prose, with a diagram>
```
