# Designs

What goes in is a project folder and a conversation with the user. What comes out is a set of Markdown docs that hold the project's context. In between is the skill: Markdown instructions that an agent reads.

what-we-build is designed around 4 guidelines:

1. **A short core with detail beside it:** [SKILL.md](skills/what-we-build/SKILL.md) holds only what the agent always needs, and the agent reads every guide with it.
2. **The docs are the state:** with git beside them, they hold where the work stopped.
3. **Examples the reader knows:** an example comes from this repo or from the stable ideas of a well-known tool.
4. **Hard rules for the doc, the method left to the model:** a guide fixes what a doc must and must not be and leaves how to work to the model.

## 1. A short core with detail beside it

The agent reads [SKILL.md](skills/what-we-build/SKILL.md) and every guide in full each time the skill starts and after each compaction. A guide left for a step to point to was never read in the runs before 2026-11-04. [SKILL.md](skills/what-we-build/SKILL.md) still holds only what the agent always needs and stays within a size limit, so the detail sits in the guides. The cost is the whole skill read at every start, about 60000 bytes on 2026-11-04.

**Ask:** is this needed for every doc, or only for one?

- **Stance:** [How is it carried from one window to the next?](PHILOSOPHY.md#how-is-it-carried-from-one-window-to-the-next)
- **Decisions:**
  - [001: One skill holds every start](specs/decisions/001-one-skill-for-every-start.md)
  - [005: One guide file per kind of doc](specs/decisions/005-one-guide-per-kind-of-doc.md)
  - [034: The rules for a doc are hard and every guide is read at the start](specs/decisions/034-hard-rules-and-every-guide-read.md)
- **How it works:**
  - [The core](specs/ARCHITECTURE.md#the-core)
  - [The guides](specs/ARCHITECTURE.md#the-guides)

## 2. The docs are the state

Each point goes into its doc as soon as the user agrees it, and a point still open goes to `TODO.md`. So the docs hold everything decided, and neither a mark nor a separate file records where the work stopped. Git keeps each doc's history, which shows what changed in the project after a doc was last touched. The cost is that a doc can stand half written while its open points wait in `TODO.md`.

**Ask:** does this need a file other than the docs to remember it?

- **Stance:** [Where does it live?](PHILOSOPHY.md#where-does-it-live)
- **Decisions:**
  - [008: A resume with nothing to draft looks for drift](specs/decisions/008-resume-looks-for-drift.md)
  - [024: Approval lives in the conversation](specs/decisions/024-approval-lives-in-the-conversation.md)

## 3. Examples the reader knows

An example comes from this repo or from the stable ideas of a well-known tool, such as the sessions and hooks of Claude Code. Claude Code is where this skill was built and tested, and a user of another coding agent knows the same ideas. An example never names a command, a flag or text from another project, since those change or would be borrowed. An invented example is the fallback when neither source fits. The cost is that an example can age when the tool renames an idea.

**Ask:** does an example rest on a detail the tool may change?

- **Stance:** [How is it carried from one window to the next?](PHILOSOPHY.md#how-is-it-carried-from-one-window-to-the-next)

## 4. Hard rules for the doc, the method left to the model

A guide says what a doc must and must not be, in rules that leave no way around them. A rule that leaves room is read as a choice, and an agent busy with a task takes the shorter way. In the runs before 2026-11-04 the agents skipped such rules until the user stepped in. How to do the work stays with the model, because a model told every step stops using its judgment. One run followed a guide's "table: pain → what the project does" to the letter, and the user rejected the tables. The cost is a longer list of `[NO]` lines in each guide.

**Ask:** does this fix what the doc must be, or does it teach the model a method?

- **Stance:** [What does a model do with a rule?](PHILOSOPHY.md#what-does-a-model-do-with-a-rule)
- **Decisions:**
  - [028: A guide says what its doc's core idea is and is not](specs/decisions/028-a-guide-says-what-its-core-idea-is-and-is-not.md)
  - [029: A guide is written in tagged lines](specs/decisions/029-a-guide-is-written-in-tagged-lines.md)
  - [031: The skill leaves the form of the talk open](specs/decisions/031-the-skill-leaves-the-form-of-the-talk-open.md)
  - [034: The rules for a doc are hard and every guide is read at the start](specs/decisions/034-hard-rules-and-every-guide-read.md)
