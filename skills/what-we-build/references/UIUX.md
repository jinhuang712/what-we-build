# specs/UIUX.md

UIUX.md explains how the product looks and moves. The screens are how the stories in FEATURES are carried out, so each story becomes a flow here, drawn across the screens it passes. A designer or a developer reads it before touching the interface. It is also the way into `prototype/`, because every screen links to its page there.

It is a spec in `specs/`, drafted right after FEATURES, since it shapes how the features look.

**Owns:**

- The rules the interface follows, each with its reason.
- Every screen and its page in `prototype/`.
- The flow of each story across the screens, drawn.
- The states, how urgent each one looks and which may interrupt the user.
- The colors, type and motion that carry meaning.
- The keyboard and accessibility.

**Leaves out:**

- What the user does and why (FEATURES).
- The guidelines the design must meet (DESIGNS).
- The forks behind a screen (`specs/decisions/`).
- The numbers for sizes and timing, which live in the code.

**Push back on:**

- A story in FEATURES with no flow here.
- A flow that is only described and not drawn.
- A screen with no page in `prototype/`, or a page with no screen here.
- A second index of the pages, such as `prototype/index.html`.
- A rule with no reason.

## Guidelines

- **List the screens in a table with a link to each page,** so this doc is the prototype's navigation.
- **Draw each flow as an ASCII diagram,** with the screens it passes in order and where it can fail.
- **Link each flow up to its story in FEATURES** and to each page it passes.
- **Rank the states by urgency,** so a minor state never looks like an error.
- **Write each rule with its reason,** because a rule without one is broken the first time it gets in the way.
- **Name the code that holds the numbers** instead of copying them.
- **Change a screen and its page together.**

## You have it when

- A reader can open every page in `prototype/` from here.
- Every story in FEATURES has a drawn flow.
- Every page in `prototype/` shows what its screen says.

## Skeleton

````markdown
# UIUX

<how the product should feel to use, in a paragraph>

## Principles

- **<a rule>,** <its reason>.

## Screens

| Screen | What it is for | Page | Features |
|---|---|---|---|
| <name> | <its job> | <a link to prototype/name.html> | <the features it serves> |

## Flows

### <the story, in a few words>

<a link to the story in FEATURES>

```
<screen> ──<action>──▶ <screen> ──<action>──▶ <screen>
                           │
                           └──<failure>──▶ <what the user sees>
```

## States

| State | How urgent | May interrupt |
|---|---|---|
| <state> | <rank> | <yes or no> |

## Visual language

<the colors, type and motion that carry meaning, and the code that holds their numbers>

## Access

<the keyboard and accessibility>
````
