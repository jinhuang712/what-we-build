# FEATURES.md

FEATURES.md is the contract with the user: what the product does today, and what it will and won't do. A user reads it to learn what happens when they use it. A contributor reads it to see what exists and what was ruled out. It describes behavior from the user's side, never the code.

It comes fifth in the doc order: each feature delivers a want from the proposal within the design that DESIGNS sets.

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
- A *Not planned* item with no reason.

## Guidelines

- **Open with a Summary,** an ASCII tree in a code block of every feature by group with its status and a short description.
- **Number the groups too,** so F1 is a group and F1.1 a feature in it.
- **Split a feature that does several things** into parts such as F1.1.1.
- **Give each feature an ID that never changes,** so other docs can point to it.
- **Give a new feature a new number.**
- **Describe what the user does and what happens,** short and in the present tense.
- **Link each feature to its design guideline,** and down to its spec and its decisions.
- **End with what happens when something fails,** then *Later* and *Not planned*.

## You have it when

- A user can predict what happens when they use a feature, and when it fails.
- Every want in the proposal is a feature or sits in *Not planned*.
- No line describes the code.

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

- **Design:** <the DESIGNS guideline it serves>
- **How it works:** <a link to its spec>
- **Why:** <links to its decisions>

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
