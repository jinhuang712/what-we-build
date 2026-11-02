# FEATURES.md

FEATURES.md is the contract with the user: what the product does today, and what it will and won't do. A user reads it to learn what happens when they use it. A contributor reads it to see what exists and what was ruled out. It describes behavior from the user's side, never the code.

It comes fifth in the doc order: each feature delivers a want from the proposal within the design that DESIGNS sets. It holds every capability the project needs, so it is the bridge between the design, the build and the progress. Each feature links up to what it rests on and down to everything that builds it.

**Owns:**

- Each feature's behavior from the user's side.
- Each feature's status.
- What the user sees when something fails.
- The *Later* list.
- The *Not planned* list, with reasons.

**Leaves out:**

- How a feature works inside (`specs/`).
- The choices behind it (`specs/decisions/`).
- Type names and code paths.
- Layout and motion (`specs/UIUX.md`).
- Schedule (ROADMAP).

**Push back on:**

- A long feature that needs a spec instead.
- A setting with no reason.
- A feature that cannot reach what builds it.
- A *Not planned* item with no reason.

## Guidelines

- **Open with a Summary,** an ASCII tree in a code block of every feature by group with its status and a short description.
- **Number the groups too,** so F1 is a group and F1.1 a feature in it.
- **Split a feature that does several things** into parts such as F1.1.1.
- **Give each feature an ID that never changes,** so other docs can point to it.
- **Give a new feature a new number.**
- **Describe what the user does and what happens,** short and in the present tense.
- **Link a feature up to the design guidelines it rests on,** and to a PHILOSOPHY stance only when the stance forces it.
- **Link a feature down to everything that builds it:** its UIUX section, its prototype page, its specs and its decisions.
- **Leave the checkpoint to ROADMAP,** which links to the features it delivers.
- **End with what happens when something fails,** then *Later* and *Not planned*.

## You have it when

- A user can predict what happens when they use a feature, and when it fails.
- Every want in the proposal is a feature or sits in *Not planned*.
- No line describes the code.
- A reader can reach each feature's reason and its build from the feature.

## Skeleton

````markdown
# Features

<what the status marks mean: ✅ built · 🚧 built with a gap · ⬜ planned>

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
- **Looks like:** <its section in specs/UIUX.md and its page in prototype/>
- **How it works:** <its specs>
- **Why:** <its decisions>

#### F1.1.1: <name>

**Status:** ⬜

<what this part does>

## When something fails

<each failure, what the user sees and the feature it belongs to>

## Later, if needed

<ideas that may come, and what would bring them>

## Not planned

- **<not this>:** <why>
````
