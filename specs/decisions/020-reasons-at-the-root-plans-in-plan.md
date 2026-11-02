# 020. The reasons sit at the root, and the plan sits in `plan/`

Decided: 2026-10-31

## The problem

Every doc sat at the root. In the repos built with the skill, such as gotato, pdf-cli and calm, the docs had grown a different shape by themselves. The reasons changed slowly and needed the user's approval, the specs moved with the code, and the goals, the roadmap and the todo list changed every few days.

## The choice

By default the reasons and the contract sit at the root, `specs/` holds how each part works with `specs/decisions/` under it, and `plan/` holds GOALS, ROADMAP and TODO with `plan/evidence/` for the files TODO points to. The layout follows how fast each doc changes. Where the docs live stays the user's choice, and a doc keeps its name wherever it sits.

## Not chosen

- Every doc at the root: the slow reasons and the fast plan sit side by side, and the root grows with every optional doc.

## Consequences

A project can keep every doc at the root, as this repo does, and say so in its `AGENTS.md`. The TODO guide points its evidence files to `plan/evidence/`.
