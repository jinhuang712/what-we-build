# DESIGNS.md

DESIGNS.md is the design the project intends: the few principles it is built around, and the decisions that follow from each. Its reader is a developer about to change the code, or about to propose something new, who needs the rules that hold everywhere and the reasons behind choices that would otherwise look strange. It is not a tour of the code, and it is not a spec. The code shows what exists and how it works. This doc keeps what the code cannot say.

It comes third in a session, right after the philosophy, because the design guides the features. It turns the philosophy's stances and the proposal's approach into the way the project is built. GOALS and FEATURES come after it, so a number this doc needs stays open until GOALS sets it. A fact belongs here when it is a principle, or a decision that spans the project.

**Owns:** one paragraph on what goes in and what comes out; the principles, numbered at the top, one sentence each; under each principle, the question it asks of a new requirement and the decisions it drives; and the order that decides when two principles pull apart.

**Leaves out:** user-visible behavior, and what a caller sees when something fails (FEATURES); a decision that concerns one feature, and examples of a feature at work (FEATURES, beside that feature); whether a principle is built yet (FEATURES, TODO, GOALS); open design questions (TODO, then ROADMAP); a map of the code, a table of the stack, install steps (README) and license text (LICENSE). The code, the manifests and the lockfile already hold these, and a copy goes stale.

**Push back on:** a principle that reads like a feature, a principle every team would sign, a principle that drives a single decision, a decision with no real alternative, a decision about one feature, a walkthrough posing as design, a status note, and a date nobody recorded.

## What a principle is

A design principle sits between the other docs. It is not a belief about the world, which PHILOSOPHY holds. It is not a number that passes or fails, which GOALS holds. It is not a pitch, which PROPOSAL makes. It is a rule of thumb the team reaches for when a new requirement arrives: a sense of how this project is built, firm enough to settle real cases.

So a principle earns its place by the decisions it drives. "Every payment can be retried safely" settles how charges are keyed, how the ledger is written and how a retry runs. A line that drives only one choice is that choice: write it as a decision under the principle it serves. A line that names something the user gets, such as "customers get a reminder before the due date", is a feature, and it goes in FEATURES.md. In one session, the user read a draft and found it wordy, with principles that sounded like features. The page improved once each principle had to show the decisions it drove.

A project usually has only a handful of principles, because each one is broad. Under them sit many decisions, because each principle shows up in many places. The page reads from large to small: the principles at the top, the decisions under each, and the features in FEATURES.md below that.

## A principle asks a question

Each principle carries one question, which a reader asks of a new requirement: **Ask:** "can this run twice without charging twice?" The question is what makes a principle useful months later, when someone proposes a feature nobody foresaw. The reader asks the question, and the answer says whether the feature fits, or what it must do to fit.

Ask the question when a new requirement arrives. Do not walk back through the basic features to test each one against every principle. A basic feature exists because the product needs it, and asking whether it fits a principle only creates doubt where there was none. In one session, the agent asked whether a basic feature fit the minimalism principle, and the user found the question strange: the feature was basic enough that nobody would remove it.

## How a principle takes shape

Here is one design, for a made-up invoicing app, as it moves through a session.

**The user's list.** The user says: "The design is about three things. Keep it simple, never charge anyone twice, and send reminders." The agent does not write the list down as it is. It says what it would change, and why:

- "Send reminders" is something the customer gets. It is a feature, and it waits for FEATURES.md.
- "Never charge anyone twice" is a promise to the customer. The agent asks what it means for the build. "A network call can fail at any point, so any step may run again." The principle becomes: every payment can be retried safely.
- "Keep it simple" is a line every team would sign. The agent asks what it rules out. "No background workers we have to babysit. Everything runs inside the web app." Now it is a choice that a reader can test: everything runs in the web app's process.
- The agent adds one. The user mentioned customers in two currencies, and nothing on the list covers money. They agree on a third principle: an amount is always exact, stored in the smallest unit of its currency.

**From principle to decisions.** The agent takes "every payment can be retried safely" and asks where it shows up. Each answer becomes a decision, and each names the option it beat:

- **Each charge carries a key, and the payment provider refuses a second charge with the same key.** Instead of checking for an earlier charge before charging, because two requests can both check before either charges. Mature payment systems key their charges the same way.
- **The ledger only appends.** Instead of updating a balance, because a step that runs twice then shows as two rows that can be matched, not as a silent double.
- **A retry reuses the key of the charge it retries.** Instead of starting a new charge, because a new key would make the retry a second payment.

The principle drives several decisions, which is how the agent knows it is a principle. Before choosing the key design, the agent looks at how mature payment systems handle retries, and the first decision says what it found. A design that repeats a known answer is easier to trust, and one that departs from it should say why.

**The question it asks.** Months later, someone proposes "pay from the link in the email". The reader asks the principle's question: can this run twice without charging twice? The link must then carry the key of the invoice's charge. The feature fits, and the principle told the team how.

**When two collide.** Everything runs in the web app's process, but a charge whose answer never arrived must be checked again later, and only a background job does that. The page ends with the order that decides such a case: payments that can be retried safely, then exact amounts, then one process. The check runs as a job, and the page says what it costs.

## Guidelines

- **Open with the principles, numbered, one sentence each.** A reader sees the whole design at a glance, and every later section hangs on one of them. DESIGNS is built around its principles, so it opens with them ([wording.md](wording.md) → Sections), and it needs no TL;DR table as well.
- **Give each principle its own section,** in the opening's order: a lead that says why it holds and what it costs, the **Ask:** line, then its decisions. The cost is what tempts the next developer to undo the principle, so naming it is the warning.
- **Write each decision as the choice, what it was chosen instead of, and why.** The heading names the choice, so the decision reads in a line and can be linked. Then two short lines: **Instead of:** the real alternative it beat, and **Why:** the reason. A decision with no real alternative is obvious, and it stays out, because a record of every small choice buries the few that matter.
- **Give a decision that weighed several options a table and its date.** A table with the columns Option, For and Against shows the trade-off, and the date says when it was made. Date only the decisions whose date was recorded when they were made. A date added later to fit the form claims a history nobody wrote down.
- **Keep decisions at the size of the project.** A decision that concerns one feature, such as when a late payment is refunded, goes beside that feature in FEATURES.md, where a developer reads its behavior. So do examples of a feature at work. In one session, the user moved the feature decisions out of DESIGNS, and asked to keep only the decisions that span the project.
- **Leave the decisions unnumbered.** Numbers belong to the docs whose items other docs track, such as features and milestones. A decision is found by its principle and its name.
- **Link the reason when a decision only carries out a product decision,** such as a manual start: `(reason: PROPOSAL.md → What we don't want)`. DESIGNS comes before FEATURES, so the proposal is where that stance already lives. The reason has one home.
- **End with the order that decides when two principles pull apart.** Without it, each side of an argument quotes the principle it likes. Name the principle each step stands for.
- **Write the design you intend, and say so at the top.** A principle is the design before the code exists, and while the code still falls short of it. The opening says that the page describes the intended design, and that FEATURES.md says what is built. Whether a principle holds today lives where status lives: a 🚧 or ⬜ feature in FEATURES.md, a defect in TODO.md, or an unmet check in GOALS.md. A "not yet" note here is a second home, and it goes stale when the code catches up. In one session, the user approved a design and then asked whether its core was already built.
- **Send open questions out of DESIGNS.** A design question that is not answered yet goes to TODO.md while the roadmap is not written, and into ROADMAP.md once it is: a design discussion before the milestone that needs it, or a feature waiting for design. A guess written as a decision gets built on.

## Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "**Keep it simple.**" | "**Everything runs in the web app's process.** Ask: does this need a process we would have to run and watch?" | A choice a reader can test, with its question |
| "**Customers get a reminder before the due date.**" as a principle | Move it to FEATURES.md. | A feature, not a principle |
| A principle with one decision under it | Write the decision under the principle it serves. | A principle drives many decisions |
| "**We use PostgreSQL.**" | "**PostgreSQL** — Instead of: MongoDB. Why: every report joins invoices to customers." | The option it beat, and the reason |
| A section on how a late payment is refunded | Move it beside the payments feature in FEATURES.md. | A feature decision lives with its feature |
| "**The ledger only appends.** Not yet: refunds still edit the row." | The decision stays as it is. The refund's edit goes in TODO.md as a defect. | The design here, the gap where status lives |
| Every decision dated today, after the fact | Only the decisions whose date was recorded carry one. | A history that happened |

## Explore

**Discuss to open:** ask what the user believes the design is about, in their own words. When they offer a list, say what you would add and what you doubt before you adopt any of it. A list from the user is where the discussion starts, not where it ends: in one session, the agent took the user's list of principles as given, and the user asked it to think along instead.

1. What goes in, and what comes out? Say it in one paragraph.
2. Which few principles is the project built around? For each one: is it a choice a reader can test, or a feature, or a premise every team shares?
3. For each principle: where does it show up? List the decisions it drives. One that drives a single decision becomes a decision under another principle.
4. For each decision: what was the real alternative, and why did this choice win? For a hard choice, list the real options before picking one, so the reason has something to beat, and look at how mature projects solved the same problem. Draw the flow when the design has several moving parts, so the user sees what the choice changes.
5. What question does each principle ask of a new requirement?
6. When two principles pull apart, which one wins?
7. Which decisions concern one feature? They move to FEATURES.md, beside it. Which questions are still open? They go to TODO.md, and later to ROADMAP.md.

## Skeleton

```markdown
# Designs

<one paragraph: what goes in, what comes out, and the shape of the thing in between>

<Name> is designed around <N> principles:

1. **<principle>.** <one sentence>
2. **<principle>.** <one sentence>

<one short paragraph: each principle asks a question of every new requirement, then lists the decisions that follow from it. This page is the design we intend. What is built is in FEATURES.md, and open questions are in ROADMAP.md.>

## 1. <principle>

<the lead: what the principle means, why it holds, and what it costs>

**Ask:** <the question this principle asks of a new requirement>

### <the decision, named as the choice>

- **Instead of:** <the real alternative it beat>
- **Why:** <the reason>

### <a decision that weighed several options> — <YYYY-MM-DD, when it was recorded>

<why it won, in a sentence or two>

| Option | For | Against |
|---|---|---|
| **<the chosen option>** (chosen) | <for> | <against> |
| <another option> | <for> | <against> |

## 2. <principle>

...

## When principles collide

1. **<what wins first>.** <the principle it stands for, and why>
2. **<what wins next>.** <the principle it stands for, and why>
```

## Style

One paragraph, the numbered principles, and a line on how the page reads. Then one section per principle, each with its lead, its question and its decisions, and the collision order last. Each decision is a heading and two short lines, or a short table when it weighed several options. No status, no open questions, no section per feature, and no map of the code.

## Done when

Every principle is a choice a reader can test, carries its question, and drives several decisions. Every decision names the real alternative it beat and its reason, and only the decisions whose date was recorded carry one. No decision concerns a single feature, nothing walks through a feature, nothing says whether a principle is built yet, no open question is left on the page, and the collision order is there.
