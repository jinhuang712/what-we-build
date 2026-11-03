# specs/UIUX.md

UIUX.md explains how the product looks and moves. The screens are how the stories in FEATURES are carried out, so each story becomes a flow here, drawn across the screens it passes. A designer or a developer reads it before touching the interface. It is also the way into `prototype/`, because every screen links to its page there.

It is a spec in `specs/`.

## What it holds

Point anything a [NO] line rules out to its home, or push back when it has none.

- [YES]   the rules the interface follows, each with its reason.
- [YES]   every screen and its page in `prototype/`.
- [YES]   the drawn flow of each story across the screens.
- [YES]   the states, how urgent each one looks and which may interrupt the user.
- [YES]   the colors, type and motion that carry meaning.
- [YES]   the keyboard and accessibility.
- [NO]    what the user does and why, which FEATURES holds.
- [NO]    the guidelines the design must meet, which DESIGNS holds.
- [NO]    the forks behind a screen, which `specs/decisions/` holds.
- [NO]    the numbers for sizes and timing, which live in the code.
- [NO]    a story in FEATURES with no flow here.
- [NO]    a flow that is only described and not drawn.
- [NO]    a screen with no page in `prototype/` or a page with no screen here.
- [NO]    a second index of the pages, such as `prototype/index.html`.
- [NO]    a rule with no reason, since it is broken the first time it gets in the way.

## How to write it

- [YES]   list the screens in a table with a link to each page, so this doc is the prototype's navigation.
- [YES]   draw each flow as an ASCII diagram with the screens it passes in order and where it can fail.
- [YES]   link each flow up to its story in FEATURES and to each page it passes.
- [YES]   rank the states by urgency so a minor state never looks like an error.
- [YES]   name the code that holds the numbers instead of copying them.
- [WHEN]  a screen changes: change its page in the same change.

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
