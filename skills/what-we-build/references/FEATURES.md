# FEATURES.md

FEATURES.md is the contract with the user: what the product does today, and what it will and won't do. A user reads it to learn exactly what happens when they press a key or run a command. A contributor reads it before building, to see what exists and what was ruled out. It describes behavior from the user's side, never the code.

It comes fourth in a session: each feature delivers a want from the proposal, and the proposal's stances become its *Not planned* list. A fact belongs here when the user can see it or do it.

**Owns:** each feature's behavior from the user's side (keys, commands, settings, config keys, files the user sees), its status, the *Later* list, and the *Not planned* list with reasons.

**Leaves out:** type names, code paths, module names, algorithms and design reasons (all DESIGNS), layout and motion (UIUX), schedule (ROADMAP).

**Push back on:** type names or algorithms in a feature, a setting with no reason, and a *Not planned* item with no reason.

## Guidelines

- **Give each feature an ID and a status** (✅ built, 🚧 built with a gap, ⬜ planned), so other docs can point to it and a reader knows what to trust.
- **Open each feature with a short description** of what it gives the user. Then the behavior.
- **Describe what the user does and what happens, in the present tense.** A reader should be able to predict the result before trying it.
- **State the defaults, and every setting with its key.** Each setting needs a reason, because a setting is a decision handed back to the user.
- **Name the gap** on every 🚧 feature, so nobody mistakes "built" for "finished".
- **Give every *Not planned* item a reason.** This list is where people look before proposing something, and a reason stops the same proposal from coming back.
- **Move an item out of *Later* once it has a milestone.** It becomes a ⬜ planned feature here, and ROADMAP.md schedules it, so *Later* only holds what is not yet scheduled.
- **Keep progress out.** "Not yet used in real life" is progress, and it lives in ROADMAP.md. A 🚧 gap names what the feature lacks.
- **Describe behavior, not code.** "An invoice goes out on the first of each month" belongs here. "A cron job reads the `invoices` table at 00:00 UTC" belongs in DESIGNS.

## Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "Smart invoicing." | "An invoice goes out on the first of each month. When a payment fails, the app tries again after 3 days, then emails the customer." | What happens, and when |
| "Uses a cron job and a retry queue." | Move it to DESIGNS.md. | Implementation, not behavior |
| "Configurable reminders." | "One reminder, 3 days before the due date. Setting: `reminders.enabled`, on by default, because a customer who pays by standing order may not want reminders." | The default, and the one setting with its reason |

## Explore

**Brainstorm to open:** for each want, list everything the product could do about it. Then sort the list into now, later and never.

1. From each want in PROPOSAL: which features deliver it? Give each an ID (F1, F2, ...).
2. For each feature: what does the user do, and what happens? What are the defaults?
3. Which settings does it need? Recommend none. Each setting needs a reason.
4. What is its status: built, built with a gap, or planned?
5. What is deliberately left for later?
6. What will the project never do? Turn the stances in PROPOSAL into concrete items, each with a reason.

## Skeleton

```markdown
# Features

<one line per status mark: ✅ built · 🚧 built with a gap · ⬜ planned>

## F1 — <name> ⬜

<a short description: what it gives the user>

<behavior, as short lines or a table>

Settings: <none, or each with its key and reason>

Gap: <for 🚧 only>

## Later, if needed   (table: idea → note)

## Not planned        (table: not this → why)
```

## Style

One section per feature, present tense, from the user's side. Tables for keys, commands and settings.

## Done when

Every want in PROPOSAL maps to a feature or to *Not planned*, every 🚧 names its gap, and no line describes the code.
