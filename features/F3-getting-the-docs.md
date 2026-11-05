# F3: Getting the docs

```
F3: Getting the docs
├── F3.1: The core docs — the seven docs every project gets
├── F3.2: Docs that join later — the recommended docs and the ones a project grows into
├── F3.3: A guide per doc — what each doc owns and what it leaves out
├── F3.4: A default layout — the reasons at the root with specs/ and plan/ beside them
└── F3.5: Wording rules — short bullets and one name per thing
```

A project gets the docs it needs and no more, and the agent writes each one by its guide.

- **Design:** [DESIGNS 1: A short core with detail beside it](../DESIGNS.md#1-a-short-core-with-detail-beside-it)
- **Why:** [005: One guide file per kind of doc](../specs/decisions/005-one-guide-per-kind-of-doc.md)

## F3.1: The core docs

Every project gets seven core docs, and each answers one question.

| Doc | Answers |
|---|---|
| PROPOSAL | Why did we start this? |
| PHILOSOPHY | Why is it this way? |
| DESIGNS | What must the design always satisfy? |
| GOALS | What do we check, and when? |
| FEATURES | What does it do, and what will it do? |
| ROADMAP | When, and how far along? |
| README | What is this, and how do I start? |

**Stories:**

- You get the seven docs every project needs, so the reasons and the contract are written down.

## F3.2: Docs that join later

Three docs are recommended from the start, so a finding, a change or a choice has a home at once. The others join only when their condition holds in the project.

| Doc | Joins when |
|---|---|
| TODO | recommended from the start |
| CHANGELOG | recommended from the start |
| `specs/decisions/` | recommended from the start |
| `specs/` | a part whose working needs explaining |
| ARCHITECTURE | more than one part worth a spec |
| UIUX | a visual interface with prototype pages beside it |
| GLOSSARY | terms of its own or two words for one thing |
| INSTALL | more than one install line |
| CONTRIBUTING | a public project open to contributions |
| SECURITY | a way to report a vulnerability |
| RUNBOOK | a service someone keeps running |

**Stories:**

- You add an optional doc only when the project needs it, so you keep no doc without a job.

## F3.3: A guide per doc

Each kind of doc has a guide. The agent reads SKILL.md and every guide in full itself before it touches a doc and again after each compaction. When it says the skill asks for something, it quotes the line.

- **Something the guide rules out:** the agent names the doc that holds it.
- **A rule that seems not to fit:** the agent says why and asks for your opinion.
- **A rule you reject:** the agent writes the exception as a decision.
- **A form other than the skeleton:** only when you reject the skeleton.

| A guide holds | What it settles |
|---|---|
| tagged lines | what goes in and elsewhere and how to write it |
| what its core idea is and is not | where a model tends to blur the doc |
| the docs its doc may link to | which links are allowed |
| *You have it when* | what a finished doc gives the reader |
| a skeleton | the form the doc starts from |

- **Why:**
  - [034: The rules for a doc are hard and every guide is read at the start](../specs/decisions/034-hard-rules-and-every-guide-read.md)
  - [040: A rule holds unless the user rejects it](../specs/decisions/040-a-rule-holds-unless-the-user-rejects-it.md)

**Stories:**

- The agent reads every guide before it touches a doc, so each doc holds only what it owns.
- You ask why a doc must look a certain way and get the line that says so.

## F3.4: A default layout

You choose where the docs live, and each doc keeps its name wherever it sits. You also decide with the agent whether `AGENTS.md` records the layout. Unless you choose otherwise, the agent suggests this one.

```
<project>/
├── PROPOSAL.md … README.md   the reasons and the contract
├── features/                 one file per group past ten features and sub-features
├── specs/                    how each part works
│   └── decisions/            the choices and the ways not taken
└── plan/                     GOALS, ROADMAP and TODO
    └── evidence/             the files that TODO items point to
```

- **Why:** [020: The reasons sit at the root, and the plan sits in plan/](../specs/decisions/020-reasons-at-the-root-plans-in-plan.md)

**Stories:**

- You keep the default layout or choose your own, and each doc keeps its name wherever it sits.

## F3.5: Wording rules

The docs come out in plain and precise English, so a reader finds a fact fast and understands it the first time. The same rules hold in every doc.

| What | How it is written |
|---|---|
| an explanation | a short paragraph with the answer first |
| separate points | a list with one sentence per bullet and at most one comma |
| a thing | one name everywhere |
| an ID | always with its name like "T4: A short skill" |
| a file or an ID another doc holds | a link wherever the doc's guide allows |
| a number | its source or left open |
| a date | `YYYY-MM-DD` |
| a status | the same marks in every doc |
| code | a script named in place of pasted code |

**Stories:**

- A reader finds a fact on the first read, because every doc uses the same plain wording.
