# Features

What what-we-build does today, and what it will and won't do. Each feature is described from the user's side: what you type, what you see and what you decide.

Status: ✅ built · 🚧 built, with a gap named beside it · ❔ claimed and not yet run · ⬜ planned. A ✅ says the skill holds the rule that asks for it. Whether it works on a real project is checked in ROADMAP and GOALS.

## Summary

```
Features
├── ✅ F1: Writing the docs with you — the skill starts from your folder and talks each doc through with you
│   ├── ✅ F1.1: Start from where the project is — what the folder holds decides where the talk begins
│   │   ├── ✅ F1.1.1: Start from an idea or from code — no docs yet
│   │   ├── ✅ F1.1.2: Start from docs the skill did not write — read as material and never as truth
│   │   └── ✅ F1.1.3: Start from docs an older skill wrote — every item judged again
│   ├── ✅ F1.2: Agree the doc set — you agree the docs and the agent writes AGENTS.md
│   │   ├── ✅ F1.2.1: Pick the docs — the core docs and the optional ones whose condition holds
│   │   └── ✅ F1.2.2: Set up AGENTS.md — the rules every new window reads
│   ├── ✅ F1.3: Talk each doc through — discuss, brainstorm or decide with a recommendation
│   ├── ✅ F1.4: Push back — the agent says what does not fit and why
│   ├── ✅ F1.5: See the change — every doc is checked before you see it
│   ├── ✅ F1.7: Resume — you stop at any point and pick up later
│   │   ├── ✅ F1.7.1: Pick up an unfinished doc set — the agent tells you where the work stands
│   │   └── ✅ F1.7.2: Find the docs that fell behind — the agent compares a finished doc set with the work
│   └── ✅ F1.8: Put every doc in the format — the first thing each start does
├── ✅ F2: Keeping the context — the docs stay true as the work goes on
│   ├── ✅ F2.1: Keep the context while you work — the agent reads the owning doc first and records at once
│   └── ✅ F2.2: A wiki when others build on it — the agent tells you when the project may need one
└── ✅ F3: Getting the docs — the docs a project needs, each with a guide
    ├── ✅ F3.1: The core docs — the docs most projects start with
    ├── ✅ F3.2: Docs that join later — the recommended docs and the ones a project grows into
    ├── ✅ F3.3: A guide per doc — what each doc owns and what it leaves out
    ├── ✅ F3.4: A default layout — the reasons at the root with specs/ and plan/ beside them
    └── ✅ F3.5: Wording rules — short bullets and one name per thing
```

## Groups

- [F1: Writing the docs with you](features/F1-writing-the-docs-with-you.md)
- [F2: Keeping the context](features/F2-keeping-the-context.md)
- [F3: Getting the docs](features/F3-getting-the-docs.md)

## Not planned

- **Wording rules for other languages:** the rules are written for English docs.
- **Starting on its own:** the talk needs your full attention.
- **Drafting without a conversation:** text nobody decided is the problem the skill exists to solve.
- **A fixed questionnaire or template:** fixed questions fill forms while decisions come from a conversation.
- **More docs than the project needs:** only a doc with a job gets kept true.
- **Choosing how a product should feel:** that is the user's call, and the skill records the user's words when they bring them.
- **Writing or shaping a wiki:** what it holds depends on the project, so the skill only says when one may be needed ([F2.2: A wiki when others build on it](features/F2-keeping-the-context.md#f22-a-wiki-when-others-build-on-it)).
- **A whole `AGENTS.md`:** the skill recommends only the read order, the layout and the work rules since Claude Code's `/init` writes the rest from the code.
- **Standard texts such as LICENSE:** they need a choice of a standard text, not a discussion.
- **Scripts that check the docs:** the skill is Markdown only, so a reader checks the links and the facts ([037: The skill is written for any agent](specs/decisions/037-the-skill-is-written-for-any-agent.md)).
