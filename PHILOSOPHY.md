# Philosophy

A project manages one thing: its context.

The context is what the people and the agent worked out together. It is made in discussion, and it is both the process and the result of that discussion. It has to be kept over the whole life of the project, from the first idea to the last release. Everything this skill writes down is a part of it.

## What should a project manage?

**Its context, over the whole life of the project.**

When a project built with an agent drifts, its context failed first. It was lost, or could not be found, or was not read:

```
the context failed, so the work drifted
├── lost
│   ├── it loses the thread ······ a compacted window takes the decisions
│   └── it works from git alone ·· the log says what changed, never if it was right
├── not found
│   ├── it does not record ······· what it keeps has no fixed shape and no home
│   └── it scatters ·············· one fact in several places, unrelated things in one
└── not read
    ├── it does not read ········· the doc was right, the code went its own way
    └── it patches ··············· a doc edited again and again, unreadable to all
```

All of these are one failure, so the thing to manage is the context, and the skill is built around that.

Two meanings of "context" must be kept apart. The window is what a model can hold at one time. It fills up, it is compacted, and it is lost. The project context is what the people and the agent have decided, and it has to outlive every window.

## Where does it live?

**In docs, with one home for each fact. Not in the window, and not in git.**

| Home | Holds | Fails |
|---|---|---|
| The window | what the model holds now | lost when it is compacted |
| Git | what changed · where the work stopped | silent on why and on where the work should go |
| Docs | what was decided | a fact with several homes · a doc with no known shape |

Models also grow less reliable as the input grows (Chroma, 2025). Docs survive the window and git, and the skill is built against their own two failures. So each doc answers one question, each fact has one home, and every doc has a skeleton.

No doc holds code. A spec that holds code has two copies of it, one to read and one to run. The copy made by hand breaks. The doc names the thing, says why, and links to it.

## How is it carried from one window to the next?

**Writing and reading are one chain, and the chain breaks at its weakest link.**

```
write                        read
willing                 ┌──▶ knows where to look
  ▼                     │      ▼
knows where it goes     │    knows how to read it
  ▼                     │      ▼
knows how to write it   │    understands it the same way
  ▼                     │      ▼
writes                  │    acts on it
  ▼                     │
the user confirms ──────┘
```

Text counts as part of the context only once the user confirms it.

If one link is missing, the others do not help. A doc in the right place is no use to an agent that does not know to read it before it acts. Most of the failures above are failures of reading: the doc was there, and nobody went to it. So the skill fixes the places, gives every doc a known shape, and tells the agent where to start.

## What does a model do with a rule?

**It follows a hard rule and reads a soft one as a choice.**

A model busy with a task takes the shorter way:

```
a model busy with a task meets a rule
├── the rule leaves room ············· read as leave to skip it
├── a plain yes or no, cases named ··· followed
└── it dictates every step ··········· followed, and the model stops judging
```

The runs that shaped this skill skipped every rule that left room until the user stepped in. So a rule says what the work must be and leaves how to do it to the model.

## Why keep the docs up?

**A doc that fell behind misleads more than a missing one, since the agent believes what it reads.**

```
the agent reads a doc before it works and takes it as true
├── the doc is missing        it asks
└── the doc fell behind       it builds the wrong thing with confidence
                              └── the user finds out when the code comes back
```

So writing the docs once is not enough. The change that does the work updates the doc that owns it, and at each checkpoint the docs are read against the work.

## Who shows that the work is done?

**The agent proves it, and the user never has to look for it.**

An agent that calls a doc done and asks the user to review it hands its own check back to the user. The user then reads every line for what the agent could have found, and the doc is only as good as the user's patience that day. So a claim of done comes with its proof, which is what each check found. A claim with no proof is a failure, however good the doc may be.

## Why keep the status?

**Where the work stands is part of the context, and a status counts only once it is checked.**

An agent in a new window must know what is done before it works. Without that it rebuilds what exists or builds on what does not. The window that knew is gone, and git says only what changed. So each feature, checkpoint and goal carries a status, and a status changes only with a check and its date. A done mark nobody checked misleads more than an open one, since the next window believes it.

## What is in it?

**A result, which stands still, and a process, which moves.**

The result is what the project is. The process is why it is this way, and where it is going. A project needs both.

| Half | Docs |
|---|---|
| Result | Proposal · Philosophy · Designs · Features · Specs · README |
| Process | Decisions · TODO · Changelog · Goals · Roadmap |

```
looking back               now        looking forward, the plan
decisions · changelog ◀──  TODO  ──▶  goals · roadmap
```

The two halves cannot be separated cleanly, and they should not be. A decision is the output of a discussion, and it is also the trace of that discussion. Keeping one keeps the other. The static half and the dynamic half together are the context.

Each half fails without the other. A result with no process says what is, and not why, so the next person undoes it without knowing. A process with no result is a diary. With both, an agent in a new window can answer three questions without asking anyone: what are we building, why this way, and where are we now.

## Sources

Each source is paraphrased here, not quoted.

- Kelly Hong, Anton Troynikov and Jeff Huber. *Context Rot: How Increasing Input Tokens Impacts LLM Performance*. 2025. [trychroma.com/research/context-rot](https://trychroma.com/research/context-rot)
