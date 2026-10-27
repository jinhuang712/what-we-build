# README.md

The README is the front door. A visitor reads it to decide, in about thirty seconds, whether the project is for them, and then to start using it. It summarizes the other docs at pitch level and points to them. It should never be the only place a fact is written down.

It comes last in a session, because it sums up the approved docs. Beyond install and first use, it holds no fact of its own: everything else is a summary with a link.

**Owns:** the tagline, a short description that leads with what sets the project apart, what it does, install, first use, and links to every other doc.

**Leaves out:** detail any other doc owns. It summarizes and links.

**Push back on:** a fact written only in the README, and a copy of another doc's detail.

## Guidelines

- **Lead with the one constraint that sets the project apart.** "It writes no document until you agree on its key points" tells a visitor more than "a flexible documentation tool".
- **Say what it does in a few bullets,** then link to the doc that holds the detail.
- **Point to the status instead of copying it.** A table of what is done copies the marks in FEATURES.md, and the copy drifts the first time a feature changes. In one doc set, a check found the README's status table disagreeing with FEATURES.md on several rows. Link FEATURES.md for what is built.
- **Use a table when the content is records,** such as the docs with the question each answers, or situations with the command for each.
- **Give the install steps exactly,** as commands that can be copied.
- **Leave the known limits out unless the user asks for them.** Each limit already has a home: a gap in FEATURES.md, a number in GOALS.md, a plan in ROADMAP.md. A README section would be a second home, and it goes stale. When the user wants one, keep it to what a new user must know before starting.
- **Draft it last,** from the approved docs, so it summarizes decisions that already exist.

## Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "A powerful, flexible documentation framework." | "It writes no document until you have agreed on its key points." | The one constraint, not a category |
| A copy of the full feature list | Four bullets, then a link to FEATURES.md | A summary, not a copy |
| A "Feature status" table with done and planned for each area | "What is built: FEATURES.md" | The status stays in one home |

## Explore

Usually nothing new: draft it from the approved docs. Then ask:

1. Which install methods exist now?
2. Which limits must a new user know before they start?

## Skeleton

```markdown
# <Name>

> <tagline>

<one or two sentences: what it is, and the constraint that sets it apart>

## What it does        (a few bullets)

## Install

## Use                 (or: When to reach for it, as a table)

## Documents           (a link to every other doc)

## License
```

## Style

One description, then bullets and tables. Commands in code blocks.

## Done when

A stranger can install and use the project from the README alone, and every other doc is linked.
