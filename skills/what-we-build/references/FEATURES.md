# FEATURES.md

FEATURES.md is the contract with the user: what the product does today, and what it will and won't do. A user reads it to learn what happens when they use it. A contributor reads it to see what exists and what was ruled out. It describes behavior from the user's side, never the code.

It comes fifth in the doc order: each feature delivers a want from the proposal within the design that DESIGNS sets. It holds every capability the project needs, so it is the bridge between the design, the build and the progress. Each feature links up to what it rests on and down to everything that builds it.

## What is it

Point anything a [NO] line rules out to its home, or push back when it has none.

- [YES]   each feature's behavior from the user's side.
- [YES]   each feature's status.
- [YES]   open with a Summary, an ASCII tree in a code block of every item with its status and what it is in a few words.
- [YES]   number the groups too, so F1 is a group and F1.1 a feature in it.
- [YES]   split a feature with more than one case into sub-features such as F1.1.1.
- [YES]   give each feature an ID in the format of the skill's *IDs* table so other docs can point to it.
- [YES]   give a new feature a new number.
- [YES]   mark a feature ✅ once it is built and you have run it.
- [YES]   leave whether it works in real use to GOALS.
- [YES]   give each feature its stories, one sentence each that says who does what and for what.
- [YES]   link a feature up to the design guidelines it rests on.
- [YES]   link a feature down to everything that builds it: the UIUX flow of each story, its specs and its decisions.
- [NO]    how a feature works inside, which `specs/` holds.
- [NO]    the choices behind it, which `specs/decisions/` holds.
- [NO]    type names and code paths the user never meets.
- [NO]    how a story moves across the screens and how they look, which `specs/UIUX.md` holds.
- [NO]    the schedule or a version, which ROADMAP holds.
- [NO]    a setting with no reason.
- [NO]    a feature that cannot reach what builds it.
- [NO]    a story in a template such as "As a … I want … so that …".
- [NO]    the checkpoint, which ROADMAP links to the features it delivers.
- [NO]    a link to GOALS or ROADMAP, since they link to FEATURES.
- [WHEN]  what is built has a gap: mark it 🚧 and name the gap beside the mark.
- [WHEN]  a PHILOSOPHY stance forces a feature: link the feature to it too.
- [WHEN]  an idea may come later: give it a ⬜ in the tree.
- [WHEN]  a feature is ruled out: list it in *Not planned* with its reason.
- [WHEN]  FEATURES holds more than ten features and sub-features: give each group a file of its own and keep FEATURES.md as the index.

## Group, feature and sub-feature

**A group**

- [YES]   an area of the product the user knows by name, such as *Sessions* or *Hooks* in Claude Code.
- [YES]   every feature of that area.
- [NO]    a code module the user never sees.
- [NO]    one group per GLOSSARY term, since *Turn* is a term and not a group.
- [MAYBE] a core GLOSSARY term as its name.
- [WHEN]  the area has specs and decisions: they show what the group must hold.
- [WHEN]  it has none yet: PROPOSAL and DESIGNS show it.

**A feature**

- [YES]   one thing the user does or meets in its group, such as *Resume a session*.
- [YES]   stories of its own.
- [NO]    a case of another feature.
- [MAYBE] a group of its own once it gathers features of its own, as *Subagents* may grow out of *Tools*.

**A sub-feature**

- [YES]   one case of a feature, such as *Continue the latest session* under *Resume a session*.
- [NO]    a thing the user does on its own.

**`<description>`**

Each group, feature and sub-feature has one in the skeleton. It answers the reader's questions from the user's side.

- [YES]   what it does for the user and what they end up with.
- [YES]   how the user uses it step by step.
- [YES]   when it applies, when it does not and when it fails.
- [YES]   open with a paragraph.
- [NO]    who uses it and what they gain, which its stories hold.
- [NO]    how as the way it works inside, which `specs/` holds.
- [NO]    an answer made up for a question that does not apply.
- [NO]    steps, cases or separate points written out in a paragraph.
- [NO]    a **Description** header.
- [MAYBE] where the user meets it, such as a command or a screen.
- [WHEN]  the user meets a number or a limit: give it.

## The index and the group files

- [YES]   the index holds the status legend and the Summary of every item with its status.
- [YES]   the index holds *Not planned*.
- [YES]   a group file opens with a tree of its own items.
- [YES]   a group file holds its features.
- [YES]   name a group file after its group, such as `features/F1-sessions.md`.
- [YES]   link each group in the index to its file.
- [NO]    a status in a group file, since the index holds it.
- [NO]    a link from a group file to the index.
- [WHEN]  a group moves into a file: fix every link to its features.

## You have it when

- A user can predict what happens when they use a feature, and when it fails.
- Every want in the proposal is a feature or sits in *Not planned*.
- No line describes the code.
- A reader can reach each feature's reason and its build from the feature.

## Skeleton

````markdown
# Features

<what the status marks mean: ✅ built · 🚧 built, with a gap named beside it · ❔ claimed and not yet run · ⬜ planned>

## Summary

```
Features
└── ⬜ F1: <group> — <what it is in a few words>
    └── ⬜ F1.1: <name> — <what it is in a few words>
```

## F1: <group>

**Status:** ⬜

<description>

### F1.1: <name>

**Status:** ⬜

<description>

- **Stance:** <the PHILOSOPHY stance that forces it, if one does>
- **Design:** <the DESIGNS guidelines it rests on>
- **How it works:** <its specs>
- **Why:** <each decision as its ID with a short name, linked>

**Stories:**

- <who does what, for what> → <its flow in specs/UIUX.md, when there is one>

#### F1.1.1: <name>

**Status:** ⬜

<description>

## Not planned

- **<not this>:** <why>
````

The index, once the groups have files of their own:

````markdown
# Features

<what the status marks mean>

## Summary

```
Features
└── ⬜ F1: <group> — <what it is in a few words>
    └── ⬜ F1.1: <name> — <what it is in a few words>
```

## Groups

- [F1: <group>](features/F1-<group>.md)

## Not planned

- **<not this>:** <why>
````

A group file:

````markdown
# F1: <group>

```
F1: <group>
└── F1.1: <name> — <what it is in a few words>
```

<description>

## F1.1: <name>

<description>

- **Stance:** <the PHILOSOPHY stance that forces it, if one does>
- **Design:** <the DESIGNS guidelines it rests on>
- **How it works:** <its specs>
- **Why:** <each decision as its ID with a short name, linked>

**Stories:**

- <who does what, for what> → <its flow in specs/UIUX.md, when there is one>
````
