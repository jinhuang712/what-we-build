# FEATURES.md

FEATURES.md is the contract with the user: what the product does today, and what it will and won't do. A user reads it to learn exactly what happens when they press a key or run a command. A contributor reads it before building, to see what exists and what was ruled out. It describes behavior from the user's side, never the code.

It comes fifth in a session: each feature delivers a want from the proposal within the design that DESIGNS sets, and the proposal's stances become its *Not planned* list. A fact belongs here when the user can see it or do it.

**Owns:** each feature's behavior from the user's side (keys, commands, settings, config keys, files the user sees), its status, the decisions that concern only that feature, what the user sees when something fails, the *Later* list, and the *Not planned* list with reasons.

**Leaves out:** type names, code paths, module names and algorithms, the principles and the decisions that span the project (all DESIGNS), layout and motion (UIUX), schedule (ROADMAP).

**Push back on:** type names or algorithms in a feature, a setting with no reason, a decision that spans the project, and a *Not planned* item with no reason.

## Guidelines

- **Give each feature an ID and a status** (✅ built, 🚧 built with a gap, ⬜ planned), so other docs can point to it and a reader knows what to trust.
- **Open with a TL;DR, an outline of every capability.** Group the features by what the user is doing. Under each group's bold name, a small table gives one row per capability: its name, what it does in one line, the feature it belongs to, and its status. A reader sees the whole product at a glance, and the feature ID leads to the details. A row per feature hides what the feature holds: in one session, each row bundled several capabilities, and the user asked whether that was all the product did.
- **Keep the outline's status true to the details.** A row never shows ✅ for what its section names as a gap, so the outline never claims more than the details.
- **Follow the outline in the details.** Each group is a `##` heading, and each feature a `###` heading under it, in the outline's order. A reader then goes from a row to its section without searching.
- **Open each feature with a short description** of what it gives the user. Then the behavior, in the form that reads best: short lines, a table, a small diagram, or a command or snippet of a few lines. A long plain paragraph hides the fact the reader came for: one session rewrote its features as prose, and the user found them hard to read. Keep a snippet small, because it shows the shape of a use, not a program. Introduce each diagram or code block with a sentence that says what it shows.
- **Describe what the user does and what happens, in the present tense.** A reader should be able to predict the result before trying it.
- **State the defaults, and every setting with its key.** Each setting needs a reason, because a setting is a decision handed back to the user.
- **Name the gap** on every 🚧 feature, so nobody mistakes "built" for "finished".
- **Keep a feature's own decisions beside it.** A decision that concerns one feature, such as whether a payment that arrives after a cancellation is refunded, goes under that feature as a `####` heading that names the choice, with the same **Instead of:** and **Why:** lines a decision has in DESIGNS. When it weighed several options, it keeps a table with the columns Option, For and Against, and the date it was made, when one was recorded. A developer finds the reason where they read the behavior, and DESIGNS keeps only the decisions that span the project. In one session, the user moved such decisions out of DESIGNS for this reason.
- **Say what happens when something fails.** End with a table of failure cases: the case, what the user or caller sees and can do next, and the feature it belongs to. A doc that covers only the working path gets its failures by accident. In one session, the design guide never asked about failure, and the user added a whole failure area to the design by hand. What a caller meets when a part fails belongs here, beside the features it touches.
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
| One TL;DR row: "Invoicing, sends invoices, F2, ✅". | Three rows for F2: monthly invoices, a retry 3 days after a failed payment, and a reminder before the due date. | One row per capability, so the outline shows all that the product does |
| In DESIGNS: "Decision: a late payment on a cancelled invoice is refunded" | Under F2 in FEATURES: "#### A late payment on a cancelled invoice is refunded", with the options it beat | A feature's decision lives with the feature |

## Explore

**Brainstorm to open:** for each want, list everything the product could do about it. Then sort the list into now, later and never.

1. From each want in PROPOSAL: which features deliver it? Give each an ID (F1, F2, ...).
2. How do the features group, by what the user is doing?
3. For each feature: what does the user do, and what happens? What are the defaults?
4. Which settings does it need? Recommend none. Each setting needs a reason.
5. What is its status: built, built with a gap, or planned?
6. Which choices concern only this feature? Record each beside it, with the option it beat.
7. When a part fails, what does the user see, and what can they do next?
8. What is deliberately left for later?
9. What will the project never do? Turn the stances in PROPOSAL into concrete items, each with a reason.

## Skeleton

```markdown
# Features

<one line per status mark: ✅ built · 🚧 built with a gap · ⬜ planned>

## TL;DR

**<Group>**

| Capability | What it does | Feature | Status |
|---|---|---|---|
| <name> | <one line> | F1 | ⬜ |

## <Group>

### F1 — <name> ⬜

<a short description: what it gives the user>

<behavior: short lines, a table, a small diagram or a short snippet>

Settings: <none, or each with its key and reason>

Gap: <for 🚧 only>

#### <a decision that concerns only this feature>

- **Instead of:** <the real alternative it beat>
- **Why:** <the reason>

<when it weighed several options: a table with Option, For and Against, and the date, when it was recorded>

## When something fails   (table: case → what the user sees → feature)

## Later, if needed   (table: idea → note)

## Not planned        (table: not this → why)
```

## Style

A TL;DR outline, then one section per group and one per feature, in the same order, with each feature's own decisions under it. The failure table follows the features. Present tense, from the user's side. Tables for keys, commands, settings and failures.

## Done when

Every want in PROPOSAL maps to a feature or to *Not planned*, every capability has a row in the TL;DR, every 🚧 names its gap, every decision here concerns one feature, the failure table is there, and no line describes the code.
