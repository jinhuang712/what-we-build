# PROPOSAL.md

The proposal is where the project begins: the case for why it should exist at all. It names the change in the world that makes the project necessary, the pain that change causes, and the idea that answers it. A reader finishes it knowing whether the project is worth building. Engineers, a future contributor, and the user six months from now all read it to remember why.

It comes first in a session, because every other doc builds on the pain it names. A fact belongs here when it explains why the project should exist at all.

**Owns:** the shift, the pain points, the one idea that makes the project different, what we want, a sample of it working, what we don't want, who it is for, the approach, the risks, how we will know it works.

**Leaves out:** exact behavior (FEATURES), the full list of checks (GOALS, though it may quote the headline ones), progress (ROADMAP), and the index of the project's own docs (README). When the project's idea is itself a set of documents, as for a docs tool, that set belongs in *The idea*.

**Push back on:** a pain point with no example, a want that answers no pain, and a "don't want" with no reason.

## Guidelines

- **Open with a scene the reader has lived,** not with a definition. A reader who recognizes the moment of pain keeps reading. A reader handed a category ("a documentation framework") decides from the label.
- **Give every pain point an example or a number.** "Expenses are painful" persuades nobody. "Every month ends with an evening of matching receipts by hand" persuades anyone who has spent that evening.
- **State the idea in one sentence.** If the idea needs a paragraph, it is not one idea yet. Keep asking until it fits.
- **Answer every pain with a want.** A want that answers no pain is a feature looking for a reason.
- **Show the product working,** with one concrete sample: a conversation, a command and its output, a screen. A sample convinces where a description only claims.
- **Give every "don't want" a reason.** A refusal without a reason gets reopened by the next person who did not hear it.
- **Keep the stances short here.** The proposal states what the project refuses to become. The full list of excluded items, with reasons, lives in FEATURES.md → *Not planned*.

## Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "Developers struggle with documentation." | "You ask your agent for a README and a roadmap. Ninety seconds later you have 2,000 confident words about decisions you never made." | A scene the reader has lived |
| Pain: "Expenses are painful." | Pain: "Every month ends with an evening of matching receipts to card lines by hand." | A concrete moment |
| Don't want: "Bloat." | Don't want: "A form to fill in. Templates produce answers, not decisions." | A named thing, with its reason |

## Explore

**Brainstorm to open:** list the pains together, as many as come, as fast as they come. Then pick the three that hurt most, and find a real example for each.

1. What changed in the world that makes this project necessary now?
2. What hurts today? Ask for each pain point with a concrete example or a number.
3. Describe the moment the pain happens, as a scene the reader has lived. (This becomes the hook.)
4. What is the one idea that makes this different? Say it in one sentence.
5. For each pain: what should happen instead?
6. Show it working: one concrete example of the product in use (a conversation, a command and its output, a screen).
7. What must this project never become? Ask for the reason of each.
8. Who is it for? Who is the first user?
9. What is the approach, in one line per choice: platform, language, core model, what it builds on?
10. What could make it fail, and what reduces each risk?

## Skeleton

```markdown
# <Name> — Proposal

> <tagline>

Proposed <YYYY-MM-DD>. For what is built today, see ROADMAP.md.

## In short            (the hook: a scene the reader knows, then the one-line answer)
## The shift            (a before/after table)
## Pain points          (numbered, one bold line each, with an example)
## The idea             (one bold sentence; a table or diagram only if it helps)
## What we want         (table: pain → what the project does)
## How it works         (one concrete sample, a few lines, link FEATURES.md)
## What we don't want   (table of a few stances; link FEATURES.md → Not planned for the full list)
## Who it is for
## Approach
## Risks                (table: risk → mitigation)
## How we know it works (link GOALS.md)
```

## Style

Short sections, each opening with its point. Tables for comparisons. Real numbers. The proposal argues, so every section should make the case stronger.

## Done when

The hook names a moment the reader has lived. The idea fits in one sentence. The sample shows the product instead of describing it. Every pain has an example, every want answers a pain, and every "don't want" has a reason. A stranger could repeat the pitch in two sentences.
