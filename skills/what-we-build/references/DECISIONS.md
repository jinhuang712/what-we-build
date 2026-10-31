# specs/decisions/

The decisions folder records the forks the project took: what we chose, what we did not choose, and why. It keeps the reason alive after the people who knew it have moved on. One decision is one short file, so DESIGNS, FEATURES and the specs link to it instead of retelling it.

**Owns:** each decision, its alternatives, and what it costs. A decision about the whole design and a decision about one feature live in the same folder.

**Leaves out:** how the chosen thing works (`specs/`), what the user sees (FEATURES), and what changed in a release (CHANGELOG).

## Guidelines

- **Write a decision when another way was open, someone may later want to undo the choice, and the code does not show the reason.** A change that only says what changed belongs in CHANGELOG.
- **Keep the title to the choice, in one line,** such as "A busy Session queues messages instead of refusing them". The reason goes in the file.
- **Keep a file under one page,** and keep an index in `specs/decisions/README.md`.

## You have it when

- A reader can tell what was chosen and what was not without asking.
- The reason is one the code cannot show.
- The index lists every decision.

## Skeleton

```markdown
# NNN. <the choice, as a statement>

Decided: YYYY-MM-DD

## The problem
## The choice
## Not chosen
- <an alternative>: <why not>
## Consequences
```
