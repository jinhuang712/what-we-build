# How the doc guides work

Each kind of document has its own guide in [docs/](docs/), one file per doc: `docs/GOALS.md` for GOALS.md, `docs/RUNBOOK.md` for a runbook. This page explains how a guide is built and how to use one. It holds nothing about any single doc.

Read only the guide for the doc you are working on. One step of a session needs one guide, and the others would only take the reader's attention.

## How a guide is built

Every guide has the same parts, in the same order, so a reader finds the same thing in the same place in each one:

| Part | What it gives you |
|---|---|
| Description | what the doc is for, who reads it, where it sits in a session, and which facts belong in it |
| Owns and leaves out | its boundaries, so facts land in one place |
| Push back on | the mistakes this doc invites, to name when the user makes them |
| Guidelines | how to write it well, each with its reason |
| Weak and strong | examples of the same content, written badly and well |
| Explore | the points to talk through with the user, and a brainstorm to open the doc |
| Skeleton | the headings to start from |
| Style | the doc's form |
| Done when | the signs that the doc is ready for approval |

The guides for optional docs are shorter. They keep the description, **Owns** and **Add when**, and add the other parts only where the doc needs them.

## How a guide drives a session

Each step of working through a doc (SKILL.md → *3. Work through the docs, in order*) takes its material from one part of the guide:

| Step | Reads |
|---|---|
| Open it | Description: the question the doc answers, and why |
| Carry forward | Description: what the doc takes from the docs before it |
| Explore the key points | Explore, in the way of talking that fits (SKILL.md → *How to talk*) |
| Push back | Push back on, then Owns and leaves out |
| Draft | Skeleton, Style, Guidelines, and Weak and strong |
| Approve | Done when |

## Skeletons

A skeleton is where a doc starts, not a form to fill in. Keep every heading, and write "None yet" under one that has nothing to hold, so a reader sees the gap instead of missing it.

## Other names you may meet

Projects use many names for the same kinds of document. Map them to this set before you start, so a "PRD" lands where the facts in it belong:

| Name | Where it fits here |
|---|---|
| PRD, product spec | FEATURES.md, with the pains and wants in PROPOSAL.md |
| Vision document | PROPOSAL.md and PHILOSOPHY.md |
| PR/FAQ (working backwards) | a style for PROPOSAL.md: write it as the launch announcement |
| ARCHITECTURE.md, design doc, tech spec | DESIGNS.md, without the map of the code: the code shows what exists |
| ADR | a decision record, summarized in DESIGNS.md |
| RFC | a proposal for one change. Its outcome lands in DESIGNS.md or a decision record |
| OKRs, success metrics | GOALS.md |
| Non-goals | FEATURES.md → Not planned, and the stances in PROPOSAL.md |
| Backlog | ROADMAP.md for scheduled work, TODO.md for small items |

## Not covered

- **User manuals:** tutorials, how-to guides and API references for end users. They answer different questions (the Diátaxis framework sorts them). Write them after the founding docs exist.
- **Standard texts:** `LICENSE` and `CODE_OF_CONDUCT.md`. Use a standard text, such as an OSI-approved license or the Contributor Covenant. They need a choice, not a discussion.
