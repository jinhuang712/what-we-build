# specs/

The specs folder explains how each part of the project works, like a technical design written for readers outside the team. A spec reads like a short paper: prose that explains, with ASCII diagrams where several parts talk to each other. A reader who has not seen the code can follow how the part works.

## What is it

A spec and the code guide each other.

- [YES]   the mechanism of one part of the project in a file of its own.
- [NO]    what the user sees, which FEATURES holds.
- [NO]    the guidelines the design must meet, which DESIGNS holds.
- [NO]    the forks behind it, which `specs/decisions/` holds.
- [NO]    the options weighed on the way, since they are process files.
- [WHEN]  the project has a visual interface: it keeps `specs/UIUX.md` with the final screens in `prototype/*.html`, as the [UIUX](UIUX.md) guide says.
- [WHEN]  a spec is drafted first: it guides the code.
- [WHEN]  a better implementation lands: it updates the spec.
- [WHEN]  they disagree: tell the user and let them decide.

## Part

- [YES]   a piece of the project with a mechanism of its own, such as *the permission check* or *compaction* in Claude Code.
- [YES]   one spec file.
- [NO]    a feature, since one part can serve many features and one feature can use many parts.
- [NO]    a single code file.
- [MAYBE] the same name as a FEATURES group, as *Hooks* can be both.
- [WHEN]  a part grows too large for a short paper: it splits into specs of its own.

## You have it when

- A reader who has not seen the code can follow how the part works.
- It agrees with the code, or the user knows where it does not.

## Skeleton

```markdown
# <Part>

<what the part does and why it exists, in a paragraph>

<the mechanism in prose, with a diagram>
```
