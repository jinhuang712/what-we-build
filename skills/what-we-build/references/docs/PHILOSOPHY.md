# PHILOSOPHY.md

The philosophy says which side the project takes when a choice is hard. A principle here is a choice, not a belief: it picks one good thing over another, and a sensible team could pick the other. The other docs turn to it when a decision is close, and a reader should be able to settle a real case with one line of it.

It comes second in a session: it turns the pain and the wants in the proposal into choices. A fact belongs here when it is a reason that applies to many things.

**Owns:** the belief the project starts from, in a short preamble; a few principles, each one line that picks a side; one thing each principle refuses, with its alternative; and a tie-break for when two principles collide.

**Leaves out:** any feature the product has (a refusal names only what it will not do, and what happens instead), any setting or screen part, and long reasoning. A principle that names a feature belongs in FEATURES, UIUX or DESIGNS. The full list of what will not be built, with the reasons, lives in FEATURES.md → *Not planned*. Long reasoning belongs in PROPOSAL.md.

**Push back on:** a belief no team would reverse ("quality matters"), a principle that names a feature or a screen part, a principle that refuses nothing, and a page longer than one screen.

## Guidelines

- **Write each principle as a choice.** "Decisions over drafts" picks a side. "Clarity" is a noun and "quality matters" is a belief: people agree with both, and then both are ignored.
- **Test each principle three ways.** Opposite: a sensible team could choose the reverse. Case: it settles a real, tempting decision that the reader can name. Cost: it shows what the project gives up. A line that fails the opposite test is a premise, and it goes in the preamble.
- **Keep each principle to one line:** "X over Y", a command, or a short saying. A line is what people remember and quote in a review.
- **Give each principle one refusal, with its alternative:** "No drafting without a conversation: agree the points, then write." The refusal shows what the principle costs. The full list, with the reasons, stays in FEATURES.md → *Not planned*, so it has one home.
- **Add a tie-break.** Say which principle wins when two collide. Without one, each side of an argument quotes the line it likes.
- **Put the belief in a short preamble:** one to three sentences on what is true about the world, which the principles answer. Longer reasoning goes in PROPOSAL.md.
- **Use the domain's words, not the product's features.** A docs tool may speak of docs and goals, as a bank may speak of money. A choice that names a feature the product has describes the feature, and it rejects nothing. The refusal is the one place a product's behavior appears: it names what the product will not do, and what happens instead.
- **Keep the page to one screen,** so it gets read before a decision instead of after it.
- **Cite evidence only when the user knows the source, or you can verify it.** An invented citation destroys the trust the page exists to build.
- **Leave out how the product should feel.** That is the user's call. Record their words only when they bring them.

## Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "Quality matters." | "**Finished over first.** No beta features: a feature ships done, or it waits." | A choice a sensible team could reverse |
| "Simplicity." | "**Fewer features over more options.** No plugin system: a needed feature goes into the core." | A side, and what it refuses |
| "Users can export their data as CSV." | Move it to FEATURES.md. Keep the choice behind it here: "**The user's data over our lock-in.** No closed format: every record leaves as a plain file." | A feature is not a principle |
| "People are busy." | Move it to the preamble. It is true for every team, so it settles nothing. | A premise, not a choice |

## Explore

This doc usually needs the most discussion.

**Brainstorm to open:** list every belief the user holds about the problem, however small. Then turn each one into a choice: what does it pick, and over what?

1. What is true about the world that this project answers? This becomes the preamble.
2. For each belief, what does it make the project choose, and over what? Write it as one line.
3. Test each line. Would a sensible team choose the opposite? Which real, tempting decision does it settle? What does it cost?
4. What does each principle refuse, and what does the project do instead?
5. When two principles collide, which one wins?

## Skeleton

```markdown
# Philosophy

<one to three sentences: what is true about the world, and what this project does about it>

- **<choice>.** <X over Y, when the name is not one already>. <one refusal>: <its alternative>.
- **<choice>.** ...

When two principles collide, <which wins>, then <which>.
```

## Style

A short preamble, then one line per principle, as a list with a bold name, then the tie-break. The whole page fits on one screen. A principle gets quoted on its own, so each line must make sense without the others.

## Done when

Each principle passes the opposite, case and cost tests, names one refusal, and makes a choice that names no feature the product has. The tie-break is there, and the page fits on one screen.
