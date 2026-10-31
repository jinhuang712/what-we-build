# decisions/

The decisions folder records the forks the project took: what we chose, what we did not choose, and why. It keeps the reason alive after the people who knew it have moved on. One decision is one short file, so DESIGNS, FEATURES and the specs can link to it instead of retelling it.

**Owns:** each decision, its alternatives, and what it costs. A decision about the whole design and a decision about one feature live in the same folder.

**Leaves out:** how the chosen thing works (`specs/`), what the user sees (FEATURES), and what changed in a release (CHANGELOG).

**Add when** the project takes its first real fork. Create `decisions/README.md` with the format and an index, and add a file for each decision after that. A project of any size has them, so the folder starts early.

## Guidelines

- **Write a decision when three answers are yes.** Was another way open? Might someone later want to undo this? Does the code, or FEATURES, fail to show the reason? A change that only says what changed belongs in CHANGELOG. A function name never gets a file.
- **Keep a file under one page.** It says the problem, the choice, the alternatives and the cost, and leaves the history to git.
- **Never reuse a number, and never rewrite a decision.** When a later decision replaces it, the old file stays and its status points to the new one.
- **Link both ways.** DESIGNS, FEATURES and the specs link to the decisions behind them. The index lists every decision.
- **Date the decision.** The date is its identity, and tells a reader how old the reason is.

| Weak | Strong |
|---|---|
| Title: "We use a queue" | Title: "A busy Session queues messages instead of refusing them" |
| A file for renaming a function | No file: the rename is in CHANGELOG |

The title is the choice in one line, and the reason goes in the file under *The problem*.

## Explore

What did we choose, what else was possible, and what would make someone want to undo it?

## Skeleton

```markdown
# NNN. <the choice, as a statement>

Decided: YYYY-MM-DD    Status: current | superseded by NNN

## The problem
<the force or limit, in a sentence or two>

## The choice
<what we chose>

## Not chosen
- <an alternative>: <why not>

## Consequences
<what it makes easy, and what it makes hard>
```

The index in `decisions/README.md` is a table: number, date, the choice.

## Style

Plain words, short. One line per alternative. The title states the choice, so the index reads as a list of the project's stands.

## Done when

Every file has all four sections and a date, no number repeats, every replaced decision points to its replacement, and the index lists every file.
