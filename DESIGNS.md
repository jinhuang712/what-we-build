# Designs

What goes in is a project folder and a conversation with the user. What comes out is a set of Markdown docs that hold the project's context. In between is the skill: Markdown instructions that an agent reads.

what-we-build is designed around 6 guidelines:

1. **A short core with detail on demand:** `SKILL.md` holds only what the agent always needs and points to the guides.
2. **The docs are the state:** with git beside them, they hold where the work stopped.
3. **No dependencies:** the skill is Markdown only.
4. **Our own words over borrowed text:** methods from other guides are rewritten and never copied.
5. **Examples the reader knows:** an example comes from this repo or from the stable ideas of a well-known tool.
6. **Trust the model:** a guide says what a doc is for and leaves the method to the model.

## 1. A short core with detail on demand

The agent reads `SKILL.md` in full each time the skill starts, so it holds only what the agent always needs. Each doc's guide waits in `references/` until a step points to it. `SKILL.md` stays within a line limit. The cost is that a step must name its guide, or the agent never reads it.

**Ask:** does the agent always need this, or only the step that writes one doc?

- **Decisions:** [001: One skill holds every start](specs/decisions/001-one-skill-for-every-start.md) and [005: One guide file per kind of doc](specs/decisions/005-one-guide-per-kind-of-doc.md)

## 2. The docs are the state

Each point goes into its doc as soon as the user agrees it, and a point still open goes to `TODO.md`. So the docs hold everything decided, and neither a mark nor a separate file records where the work stopped. Git keeps each doc's history, which shows what changed in the project after a doc was last touched. The cost is that a doc can stand half written while its open points wait in `TODO.md`.

**Ask:** does this need a file other than the docs to remember it?

- **Decisions:** [008: A resume with nothing to draft looks for drift](specs/decisions/008-resume-looks-for-drift.md) and [024: Approval lives in the conversation](specs/decisions/024-approval-lives-in-the-conversation.md)

## 3. No dependencies

The skill is Markdown only, so it works anywhere an agent can read files. The cost is that nothing checks the docs by machine.

**Ask:** does this add anything that must be installed or run?

- **Decisions:** [016: A skill and no plugin](specs/decisions/016-a-skill-and-no-plugin.md)

## 4. Our own words over borrowed text

The rules take methods from other writing guides and rewrite them for this skill. The sources are named in the decisions, and no passage is copied. The cost is that a reader cannot check a rule against its source line by line.

**Ask:** is any passage copied from somewhere else?

- **Decisions:** [004: Our own skill over jig's `vision-elicitation`](specs/decisions/004-our-own-skill-over-vision-elicitation.md) and [006: Three ideas from mattpocock/skills over the whole guide](specs/decisions/006-three-ideas-from-mattpocock-skills.md)

## 5. Examples the reader knows

An example comes from this repo or from the stable ideas of a well-known tool, such as the sessions and hooks of Claude Code. Both readers know Claude Code: the user works in it, and the agent that reads the skill is a Claude model. An example never names a command, a flag or text from another project, since those change or would be borrowed. An invented example is the fallback when neither source fits. The cost is that an example can age when the tool renames an idea.

**Ask:** does an example rest on a detail the tool may change?

- **Decisions:** [027: Examples come from a tool the reader knows](specs/decisions/027-examples-from-a-known-tool.md)

## 6. Trust the model

A guide says what a doc is for and what goes wrong. It leaves the method to the model, because a model told every step stops using its judgment. One run followed a guide's "table: pain → what the project does" to the letter, and the user rejected the tables. The cost is that two runs may write the same doc differently.

**Ask:** does this teach the model something it already knows?

- **Decisions:** [026: The skill says what the agent must do, not each step](specs/decisions/026-the-skill-says-what-not-how.md), [028: A guide says what its doc's core idea is and is not](specs/decisions/028-a-guide-says-what-its-core-idea-is-and-is-not.md), [029: A guide is written in tagged lines](specs/decisions/029-a-guide-is-written-in-tagged-lines.md) and [031: The skill leaves the form of the talk open](specs/decisions/031-the-skill-leaves-the-form-of-the-talk-open.md)
