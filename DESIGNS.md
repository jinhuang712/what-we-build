# Designs

What goes in is a project folder and a conversation with the user. What comes out is a set of Markdown docs that hold the project's context. In between is the skill: Markdown instructions that an agent reads.

what-we-build is designed around 9 guidelines:

1. **A short core with detail on demand:** `SKILL.md` holds what every session needs and points to the guides.
2. **The docs are the state:** with git beside them, they hold where a session stopped.
3. **No dependencies:** the skill is Markdown only.
4. **Our own words over borrowed text:** methods from other guides are rewritten and never copied.
5. **Made-up examples over real projects:** every example is invented or taken from this repo.
6. **Trust the model:** a guide says what a doc is for and leaves the method to the model.
7. **Readers check the docs, not scripts:** a reader checks the links and the facts.
8. **Test by use first:** real sessions come before prepared test prompts.
9. **The repo is its own first example:** its docs follow the skill.

## 1. A short core with detail on demand

The agent reads `SKILL.md` in every session, so it holds only what every session needs. Each doc's guide waits in `references/` until a step points to it. `SKILL.md` stays within a line limit. The cost is that a step must name its guide, or the agent never reads it.

**Ask:** does every session need this, or only the step that writes one doc?

- **Decisions:** [001: One skill holds every start](specs/decisions/001-one-skill-for-every-start.md) and [005: One guide file per kind of doc](specs/decisions/005-one-guide-per-kind-of-doc.md)

## 2. The docs are the state

A doc is committed only after the user approves it, so a committed doc is approved and an uncommitted change is a draft. Neither a mark nor a separate file records where a session stopped. A project without git cannot tell the two apart. The cost is that points agreed for a doc not yet drafted are lost when the sitting ends.

**Ask:** does this need a file other than the docs to remember it?

## 3. No dependencies

The skill is Markdown only, so it works anywhere an agent can read files. The cost is that nothing checks the docs by machine.

**Ask:** does this add anything that must be installed or run?

- **Decisions:** [003: The plugin manifest sits at the repo root](specs/decisions/003-plugin-manifest-at-the-repo-root.md)

## 4. Our own words over borrowed text

The rules take methods from other writing guides and rewrite them for this skill. The sources are named in the decisions, and no passage is copied. The cost is that a reader cannot check a rule against its source line by line.

**Ask:** is any passage copied from somewhere else?

- **Decisions:** [004: Our own skill over jig's `vision-elicitation`](specs/decisions/004-our-own-skill-over-vision-elicitation.md) and [006: Three ideas from mattpocock/skills over the whole guide](specs/decisions/006-three-ideas-from-mattpocock-skills.md)

## 5. Made-up examples over real projects

Each example in the skill is invented for it or taken from this repo. The cost is that an example carries no proof that it worked somewhere.

**Ask:** does any example name or quote another project?

## 6. Trust the model

A guide says what a doc is for and what goes wrong. It leaves the method to the model, because a model told every step stops using its judgment. One session followed a guide's "table: pain → what the project does" to the letter, and the user rejected the tables. The cost is that two sessions may write the same doc differently.

**Ask:** does this teach the model something it already knows?

## 7. Readers check the docs, not scripts

A reader checks the links and the facts, and no script does. Every goal measured on this repo is measured by a reader who did not write the change. The cost is that a broken link stays until a reader catches it.

**Ask:** does this need a script to stay true?

## 8. Test by use first

Real sessions come before prepared test prompts. The prompts follow from what the sessions show. The cost is that evidence comes slowly, one session at a time.

**Ask:** which real session showed the failure this rule fixes?

## 9. The repo is its own first example

This repo's docs follow the skill. The cost is that every rule change means checking these docs again.

**Ask:** does this repo's own doc still follow the changed rule?

- **Decisions:** [007: DESIGNS comes third, before GOALS and FEATURES](specs/decisions/007-designs-third.md)
