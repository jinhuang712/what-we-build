# F2: Keeping the context

```
F2: Keeping the context
├── F2.1: Keep the context while you work — the agent reads the owning doc first and records at once
└── F2.2: A wiki when others build on it — the agent tells you when the project may need one
```

Once the docs are written, they stay true while the work goes on in later windows. The rules that keep them true live in the project's `AGENTS.md`, so they reach a window that never loaded the skill.

- **Stance:** [What should a project manage?](../PHILOSOPHY.md#what-should-a-project-manage)

## F2.1: Keep the context while you work

In every window the agent works from the docs and writes back into them at once. The skill starts only when you type `/what-we-build`, so these rules live in the project's `AGENTS.md` and the agent reads them whenever its window is new.

| When | What the agent does |
|---|---|
| its window is new or was compacted | reads SKILL.md and every guide in full and then each doc in the read order |
| it needs to know where things stand | scans `TODO.md` · `ROADMAP.md` · `GOALS.md` |
| it is about to change something | reads the doc that owns it first |
| it works on a doc | reads and writes the doc itself and never hands it to a subagent |
| the work needs the code | may hand the code to a subagent |
| it makes a choice the DECISIONS guide counts as one | writes the decision at once |
| something cannot be done now | adds it to `TODO.md` at once |
| the docs and the code disagree | tells you and lets you decide |
| a change is done | updates `CHANGELOG.md` and the feature's status in the same change |
| a todo is done | deletes it in the same change |
| it changes something | checks only what it touched against the rules |
| a checkpoint ends or a release is near | checks the goals |
| you stop it | stops at once with every agent it started and every agent those started |

- **Design:** [DESIGNS 2: The docs are the state](../DESIGNS.md#2-the-docs-are-the-state)
- **Why:**
  - [002: The skill starts only by hand](../specs/decisions/002-manual-start.md)
  - [030: The main window reads and writes the docs](../specs/decisions/030-the-main-window-reads-and-writes-the-docs.md)

**Stories:**

- An agent in a new window reads the docs in the read order, so it knows the project before it works.
- The agent reads each doc itself before a rewrite, so it learns the project instead of passing it to a subagent.
- You find the open items and the decisions written down at once, so nothing lives only in the window.

## F2.2: A wiki when others build on it

When other developers start to build on your project, often with their own agents, the source alone leaves them guessing how to use it. The agent tells you then that the project may need a wiki. What the wiki holds and where it lives is your call, and the skill gives it no guide.

- **Why:** [023: The skill points to a wiki and leaves its form to the project](../specs/decisions/023-the-skill-points-to-a-wiki.md)

**Stories:**

- You hear at the right time that the project may need a wiki, so the developers who build on it do not have to read the source.
