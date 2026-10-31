# FEATURES.md

FEATURES.md is the contract with the user: what the product does today, and what it will and won't do. A user reads it to learn what happens when they press a key or run a command. A contributor reads it to see what exists and what was ruled out. It describes behavior from the user's side, never the code.

It comes fifth in a session: each feature delivers a want from the proposal within the design that DESIGNS sets.

**Owns:** each feature's behavior from the user's side, its status, what the user sees when something fails, the *Later* list, and the *Not planned* list with reasons.

**Leaves out:** how a feature works inside (`specs/`), the choices behind it (`decisions/`), type names and code paths, layout and motion (UIUX), and schedule (ROADMAP).

**Push back on:** a long feature that needs a spec instead, a setting with no reason, and a *Not planned* item with no reason.

## Guidelines

- **Open with a TL;DR,** an outline of every capability by group, each row with its feature and status (✅ built, 🚧 built with a gap, ⬜ planned).
- **Give each feature an ID that never changes,** so other docs can point to it. A new feature takes a new number.
- **Describe what the user does and what happens,** in the present tense, short. Link each feature to what it rests on: the guideline in DESIGNS, the spec, the decisions, and UIUX when it has a screen.
- **End with the failure table, *Later* and *Not planned*,** each *Not planned* item with its reason.

## Skeleton

```markdown
# Features

<one line per status mark: ✅ built · 🚧 built with a gap · ⬜ planned>

## TL;DR

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
