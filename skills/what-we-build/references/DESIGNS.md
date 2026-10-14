# DESIGNS.md

DESIGNS.md is the design as it stands today: the choices that shape how the project is built, what each one costs, and how to check that it still holds. Its reader is a developer about to change the code, who needs the rules that hold everywhere and the reasons behind choices that would otherwise look strange. It is not a tour of the code, and it is not a spec. The code shows what exists and how it works. This doc keeps what the code cannot say.

It comes third in a session, right after the philosophy, because the design guides the features. It turns the philosophy's stances and the proposal's approach into the way the project is built. GOALS and FEATURES come after it, so a number this doc needs stays open until GOALS sets it. A fact belongs here when it is about code, files, processes or a design decision.

**Owns:** one paragraph on what goes in and what comes out; design principles grouped by area, each with its cost and a rule that shows it holds; the few big decisions, each in its own dated section with the options it beat and its reason; and the open questions.

**Leaves out:** user-visible behavior (FEATURES), a map of the code, a section per feature, a table of the stack, install steps (README) and license text (LICENSE). The code, the manifests and the lockfile already hold these, and a copy goes stale.

**Push back on:** a principle with no cost, a "Holds as" that restates the code, a feature walkthrough posing as design, and a decision with no reason or no option it beat.

## Guidelines

- **Write each principle as a choice, in concrete words.** "No personal data in logs" says what it forbids. "Privacy-first" does not.
- **Give each principle its cost.** A choice that costs nothing is not a choice. The cost is also what tempts the next developer to undo it, so naming it is the warning.
- **End each principle with "Holds as:", a rule a reviewer can check.** Name the file or type it concerns, so a reader can find it: "Holds as: only `OrderService` writes the `orders` table." A rule that restates what the code does goes stale the day the code changes.
- **Group the principles by area,** such as platform, data, failure, performance, privacy and testing, and write as many as the design has. A reader looks for the area they are about to change.
- **Say how it fails.** Name what happens when a step fails, how the caller finds out, and what the caller can do next. A design that covers only the working path gets its failures by accident: in one session the guide never asked, and the user added a whole failure area to the design.
- **Fold invariants into the principles.** "No request holds a lock across a network call" is the "Holds as" of a principle about concurrency, not a separate list.
- **Keep product decisions out of the principles.** A design principle says how the project is built. When it says what the user gets ("starts only by hand"), it is a feature, and it goes in FEATURES.md.
- **Record a decision when it is hard to reverse, surprising without context, and the result of a real trade-off.** Leave the obvious ones to the code. A record of every small choice buries the few that matter.
- **Give each decision its own section: `## Decision: <the choice> — YYYY-MM-DD`.** Several decisions can share a date, so the title names the choice. Under the heading, write what the decision needs: a few sentences, a list, or a table of the options with what speaks for and against each. The options it beat show the trade-off. The reason stops the next developer from undoing it. The fixed heading lets anyone count the decisions and link to one. A one-line decision had no room for its comparison, and one session's user asked for sections instead.
- **Link the reason when a decision only carries out a product decision,** such as a manual start: `(reason: PROPOSAL.md → What we don't want)`. DESIGNS comes before FEATURES, so the proposal is where that stance already lives. The reason has one home.
- **At the start of a project, write the design you intend.** Principles hold before the code exists, and each decision shows the option it beat, so the trade-off is visible before anything is built.
- **Mark open questions as open.** A guess written as a decision gets built on.

## Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "Privacy-first." | "**No personal data in logs.** Cost: a bug report needs the user's own steps. Holds as: the logger drops every field marked `pii`." | A choice, its cost and a check |
| "We use PostgreSQL." | `## Decision: PostgreSQL over MongoDB — 2026-09-27`, then the reason (every report joins orders to customers) and a table of both options | The options it beat, and the reason |
| "`OrderService` loads the order, checks the stock, charges the card, ..." (a page) | "**One writer per table.** Cost: a change across two tables goes through two services. Holds as: only `OrderService` writes `orders`." | The rule, not a walkthrough |
| A section per feature: "Checkout. Behavior: FEATURES.md → F3. The page calls ..." | Remove the section. Keep the choices it hid, as principles under their area. | Design, not a tour of the features |

## Explore

**Brainstorm to open:** for each hard choice, list two or three real alternatives before picking one, so the reason has something to beat.

1. What goes in, and what comes out? Say it in one paragraph.
2. Which areas does the design have: platform, data, failure, performance, privacy, testing, others?
3. In each area, which choices hold everywhere? For each one: what does it cost, and how would a reviewer see that it still holds? When it needs a number, leave the number open for GOALS.md, which comes later.
4. How does it fail? What does the caller see, and what can it do next?
5. Which choices are hard to reverse? Record each one with the options it beat.
6. What is still undecided? Record it as an open question, not a guess.

## Skeleton

```markdown
# Designs

<one paragraph: what goes in, what comes out, and the shape of the thing in between. Behavior is in FEATURES.md.>

## Principles

### <Area>

- **<choice>.** <one sentence, when the name needs it>. Cost: <what it gives up>. Holds as: <a rule a reviewer can check>.

## Decision: <X> over <Y> — YYYY-MM-DD

<why X won. Then what the decision needs: a few sentences, a list, or a table with the columns Option, For and Against.>

## Open questions
```

## Style

One paragraph, then the principles grouped by area, one list item each with its cost and its check. Then one section per decision, with the choice and the date in its heading, and the open questions last. No section per feature, and no map of the code.

## Done when

Every principle has a cost, and a "Holds as" that a reviewer can check without reading the code. Every decision has its own dated section, the options it beat and a reason. Nothing restates behavior or the code.
