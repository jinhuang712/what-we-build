# Philosophy

A project manages one thing: its context.

The context is what the people and the agent worked out together. It is made in discussion, and it is both the process and the result of that discussion. It has to be kept over the whole life of the project, from the first idea to the last release. Everything this skill writes down is a part of it.

## What should a project manage?

**Its context, over the whole life of the project.**

When a project built with an agent drifts, its context failed first, in one of these ways:

- **It does not record:** what it keeps has no fixed shape and no home.
- **It patches:** a doc edited again and again ends up unreadable to people and agents alike.
- **It loses the thread:** a compacted window takes the decisions with it.
- **It does not read:** the doc was right, and the code went its own way.
- **It works from git alone:** the log says what changed and never whether it was right.
- **It scatters:** one fact sits in several places, and unrelated things pile together.

All of these are one failure. The context was lost, or could not be found, or was not read, and the work drifted. So the thing to manage is the context, and the skill is built around that.

Two meanings of "context" must be kept apart. The window is what a model can hold at one time. It fills up, it is compacted, and it is lost. The project context is what the people and the agent have decided, and it has to outlive every window.

## Where does it live?

**In docs, with one home for each fact. Not in the window, and not in git.**

The window is the wrong home. It is lost when it is compacted, and models grow less reliable as the input grows (Chroma, 2025). A project that lives in the window is gone with it.

Git is the wrong home too. It holds what changed and says nothing of why. It can tell an agent where the work stopped, and it cannot tell it where the work should go.

Docs survive both. They fail in two ways, and the skill is built against both. The first is that a fact has several homes, so they disagree. The second is that a doc has no known shape, so it has to be guessed at. So each doc answers one question, each fact has one home, and every doc has a skeleton.

No doc holds code. A spec that holds code has two copies of it, one to read and one to run. The copy made by hand breaks. The doc names the thing, says why, and links to it.

## How is it carried from one window to the next?

**Writing and reading are one chain, and the chain breaks at its weakest link.**

To write, the agent must be willing to write. It must know where the fact goes, and how to write it. Then it writes, and the user confirms, and only then does the text count as part of the context.

To read, the agent must know where to look and how to read what it finds. It must understand it the same way each time, and only then can it act on it.

If one link is missing, the others do not help. A doc in the right place is no use to an agent that does not know to read it before it acts. Most of the failures above are failures of reading: the doc was there, and nobody went to it. So the skill fixes the places, gives every doc a known shape, and tells the agent where to start.

## What does a model do with a rule?

**It follows a hard rule and reads a soft one as a choice.**

A model busy with a task takes the shorter way. A rule that leaves room is read as leave to skip it, and the runs that shaped this skill skipped every such rule until the user stepped in. A rule works only when no reading of it lets the model skip it: a plain yes or no, with its cases named. What a rule leaves open is how to do the work, since a model told every step stops using its judgment.

## Why keep the docs up?

**A doc that fell behind misleads more than a missing one, since the agent believes what it reads.**

An agent reads the docs before it works and takes them as true. A missing doc makes it ask. A doc that fell behind makes it build the wrong thing with confidence, and the user finds out only when the code comes back. So writing the docs once is not enough. The change that does the work updates the doc that owns it, and at each checkpoint the docs are read against the work.

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

The goals and the roadmap are the plan. The plan is the process looking forward, and the decisions and the changelog are the process looking back. TODO is the process at this moment.

The two halves cannot be separated cleanly, and they should not be. A decision is the output of a discussion, and it is also the trace of that discussion. Keeping one keeps the other. The static half and the dynamic half together are the context.

Each half fails without the other. A result with no process says what is, and not why, so the next person undoes it without knowing. A process with no result is a diary. With both, an agent in a new window can answer three questions without asking anyone: what are we building, why this way, and where are we now.

## Sources

Each source is paraphrased here, not quoted.

- Kelly Hong, Anton Troynikov and Jeff Huber. *Context Rot: How Increasing Input Tokens Impacts LLM Performance*. 2025. [trychroma.com/research/context-rot](https://trychroma.com/research/context-rot)
