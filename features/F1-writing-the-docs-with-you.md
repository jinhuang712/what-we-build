# F1: Writing the docs with you

```
F1: Writing the docs with you
├── F1.1: Start from where the project is — what the folder holds decides where the talk begins
│   ├── F1.1.1: Start from an idea or from code — no docs yet
│   ├── F1.1.2: Start from docs the skill did not write — read as material and never as truth
│   └── F1.1.3: Start from docs an older skill wrote — every item judged again
├── F1.2: Agree the doc set — you agree the docs and what AGENTS.md holds
│   ├── F1.2.1: Pick the docs — the core docs and the optional ones whose condition holds
│   └── F1.2.2: Set up AGENTS.md — the rules every new window reads
├── F1.3: Talk each doc through — discuss, brainstorm or decide with a recommendation
├── F1.4: Push back — the agent says what does not fit and why
├── F1.5: See the change — every doc is checked before you see it
└── F1.7: Resume — you stop at any point and pick up later
    ├── F1.7.1: Pick up an unfinished doc set — the agent starts at the first doc not finished
    └── F1.7.2: Find the docs that fell behind — the agent compares a finished doc set with the work
```

You type `/what-we-build` and the agent turns what your folder already holds into a doc set you talked through point by point. You can stop anywhere and pick up later.

```
you type /what-we-build
        │
        ▼
F1.1: Start from where the project is
        │  the agent reads the folder
        ▼
F1.2: Agree the doc set
        │  you agree the docs and what AGENTS.md holds
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

You type `/what-we-build` in whatever folder you have, and the agent reads it first. An empty folder, running code and docs already there are all material for the talk. What the folder holds decides where the talk begins, and a doc set this skill started goes on as [F1.7: Resume](#f17-resume) says. When the folder has no git, the agent suggests `git init`, since git shows which docs fell behind.

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
        └── neither ────────────▶ it stays out
```

- **An instruction in such a doc:** the agent never follows it.
- **Its old format:** the agent talks it through with you before any move into the new one.
- **Each item in it:** judged again from scratch once the doc moves into the new form.

### F1.1.3: Start from docs an older skill wrote

The agent tells you the docs are older than the skill and offers to judge every item again against its guide. You decide whether it does.

- **Items marked done:** judged again too.
- **A part its guide no longer asks for:** the agent names it.
- **A line in an old form:** never kept because it is old.

## F1.2: Agree the doc set

Before any doc is written, you and the agent agree which docs the project gets and what its `AGENTS.md` holds. The agent brings a recommendation for each and you decide.

- **Why:** [032: AGENTS.md keeps a copy of the rules that the host loads](../specs/decisions/032-agents-md-keeps-a-copy-the-host-loads.md)

**Stories:**

- You decide which docs the project gets, so the agent writes none you did not agree to.

### F1.2.1: Pick the docs

The agent proposes the docs and you decide which ones come.

- **The core docs:** all seven of [F3.1: The core docs](F3-getting-the-docs.md#f31-the-core-docs) unless you drop one.
- **The optional docs:** each doc of [F3.2: Docs that join later](F3-getting-the-docs.md#f32-docs-that-join-later) whose condition holds in your project.
- **You drop a core doc:** the agent first tells you what it would hold.

### F1.2.2: Set up AGENTS.md

`AGENTS.md` holds the rules that every new window reads before it works. The agent proposes what goes in and you agree each rule in turn.

- **What it holds:** a read order, a layout and the work rules of [F2.1: Keep the context while you work](F2-keeping-the-context.md#f21-keep-the-context-while-you-work).
- **How it grows:** one rule at a time as you agree it, never all at once.
- **What it links to:** the docs in its read order and nothing else.
- **No `CLAUDE.md` yet:** the agent adds one with the line `@AGENTS.md` so every window loads it.

## F1.3: Talk each doc through

The core docs come one at a time in a fixed order, since each builds on the ones before it. On each doc the agent asks one thing at a time, recommends an answer and says why. A point goes into the doc once you agree it. The talk on a doc ends only when you say it is done.

```
PROPOSAL → PHILOSOPHY → DESIGNS → GOALS → FEATURES → ROADMAP → README
```

- **Before you end the talk:** the agent keeps looking for the next line that breaks a rule.
- **When it finds none:** it reads the whole doc again and shows you what it checked.
- **When it thinks the talk is enough:** it says so and names what is still open.
- **Code, another doc or another topic:** none of them comes before you end the talk.

| The point | What the agent does |
|---|---|
| has moving parts | draws it |
| has an open outcome | asks open questions and gives its own view |
| can go many ways | brainstorms and points out the best one |
| is a fact no doc owns | asks you where it goes |
| is a number nobody knows | leaves it open in the doc |
| is still open | puts it in `TODO.md` as a `DISCUSSION` |
| is a stance you state a second time | proposes to write it in PHILOSOPHY |

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

Nothing reaches a doc behind your back. Before the agent shows you a doc, it checks the doc line by line and shows you what each check found as the proof that the doc is done. It commits a change only once you approve it.

| What it checks | Against |
|---|---|
| every line | the doc's guide |
| every sentence | the wording rules |
| every link | the doc's guide and the link's target |
| every file or folder it names | its link |
| every fact | the placement test and a second home |
| every number | its source |
| every item | its ID and what the guide says a finished doc gives the reader |

- **A check fails:** you see the doc only after the agent fixes it.
- **Review in place of proof:** the agent never asks you to look for yourself.
- **A heading or an ID is renamed:** every link and mention of it changes in the same change.
- **Approval:** only yours counts.

**Stories:**

- You approve a change only after you have seen its proof, so nothing reaches a doc behind your back.

## F1.7: Resume

You can stop at any point and pick up later, because every agreed point is already in its doc and every open one is in `TODO.md`. On a later `/what-we-build` the agent reads the docs and tells you what it found.

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

- You come back another day and the agent picks up at the first doc that is not finished.
- You return to a finished doc set and learn which docs fell behind the work.

### F1.7.1: Pick up an unfinished doc set

Part of the doc set is written. The agent starts at the first core doc in the order that is not finished and tells you what is still open for it.

### F1.7.2: Find the docs that fell behind

Every doc is written. The agent compares the docs with what changed in the project since each was last touched and tells you which ones fell behind it.
