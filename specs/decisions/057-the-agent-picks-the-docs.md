# 057. The agent picks the docs a project needs

Decided: 2026-11-09

## The problem

Every project got all seven core docs. In a run on a script of about 200 lines the agent proposed PROPOSAL, PHILOSOPHY, DESIGNS and five decisions. The user cut most of them as too much, since the user had stated no stance for PHILOSOPHY to hold.

## The choice

The agent picks the docs the project needs and the user decides. The core docs are where most projects start, and the agent says what each doc it proposes would hold. How many docs fit depends on how complex the project is, which no rule can set.

## Not chosen

- A doc only once the user agreed a fact for it: it reads as vague, and a project's needs show before its facts do.
- Ask the questions of the seven core docs and build only the answered ones: too complex for what it settles.
- Keep all seven: a small project carries empty docs or invented ones.

## Consequences

A small project gets fewer docs. The agent may also leave out a doc a project needs, and only the user's decision catches that.
