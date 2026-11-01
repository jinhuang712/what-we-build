# FEATURES.md

FEATURES.md is the contract with the user: what the product does today, and what it will and won't do.
A user reads it to learn what happens when they use it.
A contributor reads it to see what exists and what was ruled out.
It describes behavior from the user's side, never the code.

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
- **Give each Summary row its feature and status.**
- **Give each feature an ID that never changes,** so other docs can point to it. A new feature takes a new number.
- **Describe what the user does and what happens,** short and in the present tense.
- **Link each feature to what it rests on,** as the skeleton shows.
- **End with the failure table, *Later* and *Not planned*.**

## You have it when

- A user can predict what happens when they use a feature, and when it fails.
- Every want in the proposal is a feature or sits in *Not planned*.
- No line describes the code.

## Skeleton

```markdown
# Features

<one line per status mark: ✅ built · 🚧 built with a gap · ⬜ planned>

## Summary

**<Group>**

| Capability | What it does | Feature | Status |
|---|---|---|---|

## <Group>

### F1 — <name> ⬜

<what it gives the user, and what happens>

Design: <the DESIGNS guideline it serves>. How it works: <link to the spec>. Why: <links to decisions>. Look: <link to UIUX, for a feature with a screen>.

## When something fails

| Case | What the user sees | Feature |
|---|---|---|

## Later, if needed

## Not planned

| Not this | Why |
|---|---|
```
