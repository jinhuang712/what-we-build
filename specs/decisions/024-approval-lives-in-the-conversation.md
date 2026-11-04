# 024. Approval lives in the conversation

Decided: 2026-11-03

Partly replaced by 026: The skill says what the agent must do, not each step, under which a resume no longer names the first doc not finished.

## The problem

Decision 009: Git tells a draft from an approved doc made a commit mean approval, so an uncommitted change was a draft and a resume read `git status` to find where the work stopped. Since 019: Agreed points go in at once, a doc holds only what the user has agreed, so there is no draft left for git to tell apart. The extra meaning only added a rule, and it misread any uncommitted change in the folder as a doc waiting for approval.

## The choice

The user approves in the conversation, and a commit only saves what was approved. A point still open goes to `TODO.md` as a `DISCUSSION`. A resume finds where the work stopped from the first doc in the order that is not written yet or still has an open question. Git keeps each doc's history for the drift report. This replaces 009: Git tells a draft from an approved doc.

## Not chosen

- Keeping a commit as the mark of approval: every doc already holds only agreed points, so the mark repeats what the conversation settled.
- A mark on each doc: the approval would have a second home, as before 009: Git tells a draft from an approved doc.

## Consequences

The *Start* table no longer looks at uncommitted changes. A project without git loses only the drift report, so the agent still recommends `git init`.
