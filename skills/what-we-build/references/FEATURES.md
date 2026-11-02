# FEATURES.md

FEATURES.md is the contract with the user: what the product does today, and what it will and won't do. A user reads it to learn what happens when they use it. A contributor reads it to see what exists and what was ruled out. It describes behavior from the user's side, never the code.

It comes fifth in a session: each feature delivers a want from the proposal within the design that DESIGNS sets.

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

- **Open with a Summary,** an outline of every capability by group.
- **Give each feature an ID that never changes,** so other docs can point to it.
- **Give a new feature a new number.**
- **Describe what the user does and what happens,** short and in the present tense.
- **Link each feature to what it rests on,** such as its design guideline and its decisions.
- **End with what happens when something fails,** then *Later* and *Not planned*.

## You have it when

- A user can predict what happens when they use a feature, and when it fails.
- Every want in the proposal is a feature or sits in *Not planned*.
- No line describes the code.

## Skeleton

```markdown
# Features

<what the status marks mean: ✅ built · 🚧 built with a gap · ⬜ planned>

## Summary

<every capability by group, with its feature and status>

## <Group>

### F1: <name>

**Status:** ⬜

<what it gives the user, and what happens>

- **Design:** <the DESIGNS guideline it serves>
- **How it works:** <a link to its spec>
- **Why:** <links to its decisions>

## When something fails

<each failure, what the user sees and the feature it belongs to>

## Later, if needed

<ideas that may come, and what would bring them>

## Not planned

- **<not this>:** <why>
```
