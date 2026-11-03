# FEATURES.md

FEATURES.md is the contract with the user: what the product does today, and what it will and won't do. A user reads it to learn what happens when they use it. A contributor reads it to see what exists and what was ruled out. It describes behavior from the user's side, never the code.

It comes fifth in the doc order: each feature delivers a want from the proposal within the design that DESIGNS sets. It holds every capability the project needs, so it is the bridge between the design, the build and the progress. Each feature links up to what it rests on and down to everything that builds it.

## What is it

Point anything a [NO] line rules out to its home, or push back when it has none.

- [YES]   each feature's behavior from the user's side.
- [YES]   each feature's status.
- [YES]   what the user sees when something fails.
- [YES]   the *Later* list.
- [YES]   the *Not planned* list with a reason for each item.
- [YES]   open with a Summary, an ASCII tree in a code block of every feature by group with its status and a short description.
- [YES]   number the groups too, so F1 is a group and F1.1 a feature in it.
- [YES]   split a feature that does several things into sub-features such as F1.1.1.
- [YES]   give each feature an ID that never changes so other docs can point to it.
- [YES]   give a new feature a new number.
- [YES]   mark a feature ✅ once it is built, and leave whether it works in real use to GOALS.
- [YES]   describe what the user does and what happens, short and in the present tense.
- [YES]   give each feature its stories, one sentence each that says who does what and for what.
- [YES]   link a feature up to the design guidelines it rests on.
- [YES]   link a feature down to everything that builds it: the UIUX flow of each story, its specs and its decisions.
- [YES]   end with what happens when something fails, then *Later* and *Not planned*.
- [NO]    how a feature works inside, which `specs/` holds.
- [NO]    the choices behind it, which `specs/decisions/` holds.
- [NO]    type names and code paths.
- [NO]    how a story moves across the screens and how they look, which `specs/UIUX.md` holds.
- [NO]    the schedule or a version, which ROADMAP holds.
- [NO]    a long feature that needs a spec instead.
- [NO]    a setting with no reason.
- [NO]    a feature that cannot reach what builds it.
- [NO]    a story in a template such as "As a … I want … so that …".
- [NO]    the checkpoint, which ROADMAP links to the features it delivers.
- [WHEN]  what is built has a gap: mark it 🚧 and name the gap beside the mark.
- [WHEN]  a PHILOSOPHY stance forces a feature: link the feature to it too.

## Group, feature and sub-feature

**A group**

- [YES]   an area of the product the user knows by name, such as *Sessions* or *Hooks* in Claude Code.
- [YES]   every feature of that area.
- [NO]    a code module the user never sees.
- [NO]    one group per GLOSSARY term, since *Turn* is a term and not a group.
- [MAYBE] a core GLOSSARY term as its name.
- [MAYBE] two groups once one area grows too large to scan.
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

## You have it when

- A user can predict what happens when they use a feature, and when it fails.
- Every want in the proposal is a feature or sits in *Not planned*.
- No line describes the code.
- A reader can reach each feature's reason and its build from the feature.

## Skeleton

````markdown
# Features

<what the status marks mean: ✅ built · 🚧 built, with a gap named beside it · ⬜ planned>

## Summary

```
Features
└── ⬜ F1: <group> — <a short description>
    └── ⬜ F1.1: <name> — <a short description>
```

## F1: <group>

**Status:** ⬜

<what the group gives the user>

### F1.1: <name>

**Status:** ⬜

<what it gives the user, and what happens>

- **Stance:** <the PHILOSOPHY stance that forces it, if one does>
- **Design:** <the DESIGNS guidelines it rests on>
- **How it works:** <its specs>
- **Why:** <each decision as its ID with a short name, linked>

**Stories:**

- <who does what, for what> → <its flow in specs/UIUX.md, when there is one>

#### F1.1.1: <name>

**Status:** ⬜

<what this sub-feature does>

## When something fails

<each failure, what the user sees and the feature it belongs to>

## Later, if needed

<ideas that may come, and what would bring them>

## Not planned

- **<not this>:** <why>
````
