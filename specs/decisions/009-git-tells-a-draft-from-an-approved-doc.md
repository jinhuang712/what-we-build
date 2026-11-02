# 009. Git tells a draft from an approved doc

Decided: 2026-11-02

## The problem

Each doc carried a mark on its first line saying drafted or approved, and any edit set it back to drafted. A doc is committed only once it is approved, so the mark repeated what git already held. Keeping both cost a fresh approval of the whole doc for a change of one number, such as a line count in GOALS.

## The choice

No doc carries a mark. A commit records the user's approval, so a committed doc is approved and an uncommitted change is a draft. A resume reads `git status` for where the work stopped and each doc's last commit for drift.

## Not chosen

- A mark only on a new doc: the approval would still have two homes until the first commit.
- A mark that a measured value does not reset: it patches the cost and keeps the second home.
- No approval at all: the agent would commit drafts the user never agreed to.

## Consequences

A commit now means approval, so the agent never commits a doc the user has not approved. A project without git cannot tell a draft from an approved doc.
