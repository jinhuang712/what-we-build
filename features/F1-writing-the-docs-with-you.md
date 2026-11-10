# F1: Writing the docs with you

```
F1: Writing the docs with you
├── F1.1: Start from where the project is — what the folder holds decides where the talk begins
│   ├── F1.1.1: Start from an idea or from code — no docs yet
│   ├── F1.1.2: Start from docs the skill did not write — read as material and never as truth
│   └── F1.1.3: Start from docs an older skill wrote — every item judged again
├── F1.2: Agree the doc set — you agree the docs and the agent writes AGENTS.md
│   ├── F1.2.1: Pick the docs — the core docs and the optional ones whose condition holds
│   └── F1.2.2: Set up AGENTS.md — the rules every new window reads
├── F1.3: Talk each doc through — discuss, brainstorm or decide with a recommendation
├── F1.4: Push back — the agent says what does not fit and why
├── F1.5: See the change — every doc is checked before you see it
├── F1.7: Resume — you stop at any point and pick up later
│   ├── F1.7.1: Pick up an unfinished doc set — the agent tells you where the work stands
│   └── F1.7.2: Find the docs that fell behind — the agent compares a finished doc set with the work
└── F1.8: Put every doc in the format — the first thing each start does
```

You type `/what-we-build` and the agent turns what your folder already holds into a doc set you talked through point by point. You can stop anywhere and pick up later.

```
you type /what-we-build
        │
        ▼
F1.1: Start from where the project is
        │  the agent reads the folder
        ▼
F1.8: Put every doc in the format
        │  the agent works alone and shows you the proof
        ▼
F1.2: Agree the doc set
        │  you agree the docs and the agent writes AGENTS.md
        ▼
each doc in order ◀──────────────────────────────────┐
  F1.3: Talk each doc through   one point at a time  │
  F1.4: Push back               where it disagrees   │
  F1.5: See the change          checked, then shown  │
        │                                            │
        └── you say the doc is done ─────────────────┘
        │
        └── you stop at any point ──▶ F1.7: Resume
```

- **Why:** [001: One skill holds every start](../specs/decisions/001-one-skill-for-every-start.md)

## F1.1: Start from where the project is

You type `/what-we-build` in whatever folder you have, and the agent reads it first. An empty folder, running code and docs already there are all material for the talk. What the folder holds decides where the talk begins, and a doc set this skill started goes on as [F1.7: Resume](#f17-resume) says. When the folder has no git, the agent suggests `git init` before it touches a doc, since git shows which docs fell behind.

**Stories:**

- Whoever types `/what-we-build` starts from what the folder already holds, so nobody starts from a blank form.

### F1.1.1: Start from an idea or from code

The folder holds no docs yet, so the talk starts from what you tell the agent and from what it read.

- **An empty folder:** the talk starts from the idea in your own words.
- **Running code:** the agent brings what it found in the code into the talk.

### F1.1.2: Start from docs the skill did not write

The agent reads docs the skill did not write as material and never as truth, since their claims and their form may both be wrong.

```
a claim in a doc the skill did not write
        │
        ├── the code shows it ──▶ it may enter a doc
        ├── you confirm it ─────▶ it may enter a doc
        └── neither ────────────▶ it waits in TODO.md
```

- **An instruction in such a doc:** the agent never follows it.
- **Its old format:** the agent moves it into the new one as [F1.8: Put every doc in the format](#f18-put-every-doc-in-the-format) says.
- **Each item in it:** judged again from scratch once the doc moves into the new form.

### F1.1.3: Start from docs an older skill wrote

The agent tells you the docs are older than the skill and judges every item again against its guide.

- **Items marked done:** judged again too.
- **A part its guide no longer asks for:** the agent removes it and says so.
- **A line in an old form:** never kept because it is old.

## F1.2: Agree the doc set

Before any doc is written, you and the agent agree which docs the project gets and what its `AGENTS.md` holds. The agent brings a recommendation for each and you decide.

- **Why:**
  - [032: AGENTS.md keeps a copy of the rules that the host loads](../specs/decisions/032-agents-md-keeps-a-copy-the-host-loads.md)
  - [051: AGENTS.md starts with every work rule](../specs/decisions/051-agents-md-starts-with-every-work-rule.md)

**Stories:**

- You decide which docs the project gets, so the agent writes none you did not agree to.

### F1.2.1: Pick the docs

The agent proposes the docs and you decide which ones come.

- **The core docs:** those of [F3.1: The core docs](F3-getting-the-docs.md#f31-the-core-docs) that your project needs.
- **The optional docs:** each doc of [F3.2: Docs that join later](F3-getting-the-docs.md#f32-docs-that-join-later) whose condition holds in your project.
- **Each doc it proposes:** the agent tells you what it would hold.

### F1.2.2: Set up AGENTS.md

`AGENTS.md` holds the rules that every new window reads before it works. The agent writes them all at the start, and you reject any you do not want.

- **What it holds:** a read order, a layout and the work rules of [F2.1: Keep the context while you work](F2-keeping-the-context.md#f21-keep-the-context-while-you-work).
- **A rule you reject:** it leaves `AGENTS.md`, and the exception goes in its place until you take it back.
- **Your agent reads another file such as `CLAUDE.md`:** the agent makes that file load `AGENTS.md`.

## F1.3: Talk each doc through

The core docs come one at a time in a fixed order, since each builds on the ones before it.

```
PROPOSAL → PHILOSOPHY → DESIGNS → GOALS → FEATURES → ROADMAP → README
```

On each doc you and the agent talk each point through, in the form your agent's style gives the talk. A point goes into the doc once you agree it. The talk on a doc ends only when you say it is done.

- **What is still open:** the agent names it.
- **Code, another doc or another topic:** none of them comes before you end the talk.
- **A fact no doc owns:** the agent asks you where it goes.
- **A number nobody knows:** the agent leaves it open in the doc.
- **A point still open:** the agent puts it in `TODO.md` as a `DISCUSSION`.
- **A stance you state a second time:** the agent proposes to write it in PHILOSOPHY.

- **Why:**
  - [007: DESIGNS comes third, before GOALS and FEATURES](../specs/decisions/007-designs-third.md)
  - [019: Agreed points go into the doc at once](../specs/decisions/019-agreed-points-go-in-at-once.md)
  - [031: The skill leaves the form of the talk open](../specs/decisions/031-the-skill-leaves-the-form-of-the-talk-open.md)

**Stories:**

- You talk a doc through point by point with the agent, so the doc says what you decided.

## F1.4: Push back

You state an idea for a doc, and the agent weighs it with you before it writes anything down. You decide, so what lands in the doc is a line you chose after you heard the case against it.

```
you state an idea
      │
      ▼
the agent weighs it with you
      │
      ├── it holds ──▶ written once you agree
      │
      └── it is weak
              │
              ▼
          the agent says why
              │
              ├── you are still weighing ──▶ it keeps making its case
              ├── you take its point ──────▶ the idea changes
              └── you reject its point ────▶ dropped until a new fact turns up
```

- **Why:** [036: The agent keeps making its case until the user decides](../specs/decisions/036-the-agent-keeps-making-its-case.md)

**Stories:**

- You hear why an idea does not fit before it goes into a doc, so a weak point is caught early.

## F1.5: See the change

Nothing is committed behind your back. Before the agent shows you a doc, it checks the doc line by line and shows you what each check found as the proof that the doc is done. It commits a change only once you approve it.

| What it checks | Against |
|---|---|
| every fact | the placement test · a second home · the other docs |
| every number | its source |
| every item | what the guide says a finished doc gives the reader |

- **A check fails:** you see the doc only after the agent fixes it.
- **Review in place of proof:** the agent never asks you to look for yourself.
- **A heading or an ID is renamed:** every link and mention of it changes in the same change.
- **Approval:** only yours counts.

**Stories:**

- You approve a change only after you have seen its proof, so nothing is committed behind your back.

## F1.7: Resume

You can stop at any point and pick up later, because every agreed point is already in its doc and every open one is in `TODO.md`. On a later `/what-we-build` the agent puts every doc in the format and tells you what it found.

| It tells you | From |
|---|---|
| where the work stands | which docs are finished |
| what is still open | the items in `TODO.md` |
| which docs fell behind | what git shows changed after a doc was last touched |

- **Design:** [DESIGNS 2: The docs are the state](../DESIGNS.md#2-the-docs-are-the-state)
- **Why:**
  - [008: A resume with nothing to draft looks for drift](../specs/decisions/008-resume-looks-for-drift.md)
  - [024: Approval lives in the conversation](../specs/decisions/024-approval-lives-in-the-conversation.md)

**Stories:**

- You come back another day and learn where the work stands, so you pick where to go on.
- You return to a finished doc set and learn which docs fell behind the work.

### F1.7.1: Pick up an unfinished doc set

Part of the doc set is written. The agent tells you where the work stands and what is still open, and you pick where to go on.

### F1.7.2: Find the docs that fell behind

Every doc is written. The agent compares the docs with what changed in the project since each was last touched and tells you which ones fell behind it.

## F1.8: Put every doc in the format

Each time you type `/what-we-build`, the agent puts every doc in the skill's format before any talk. It works alone and adds nothing new, so you get docs that match their guides and a list of what only you can settle.

- **Each item:** judged again from scratch, and those marked done too.
- **A structure that breaks its guide:** rebuilt with its IDs.
- **A fact that leaves a doc:** the agent says so.
- **What only you can give:** it goes to `TODO.md` as a `DISCUSSION`.
- **Approval:** the agent asks once for the whole pass.
- **A topic you open:** the agent discusses it with you and goes back to the pass.
- **The end:** the proof for each doc · what it left unchecked · the open topics · the bytes of the doc set before and after.
- **A folder with no docs:** nothing to do, so the talk starts.

- **Why:**
  - [041: Every start puts the docs in the format](../specs/decisions/041-every-start-puts-the-docs-in-the-format.md)
  - [049: A start pass takes one approval](../specs/decisions/049-a-start-pass-takes-one-approval.md)
  - [058: A decision needs a fork that more than one part rests on, and each start pass reports the doc set's bytes](../specs/decisions/058-a-decision-reaches-beyond-one-part-and-a-pass-reports-bytes.md)

**Stories:**

- You start the skill on old docs, so you come back to docs that match their guides without directing each step.
