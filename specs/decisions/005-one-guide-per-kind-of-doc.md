# 005. One guide file per kind of doc

Decided: 2026-10-13

## The problem

A step works on one doc, but the rules for every doc sat in one shared reference. Reading all of it cost about 700 lines each time.

## The choice

Each kind of doc has its own guide in `references/`.

## Not chosen

- One shared reference with notes in `SKILL.md`: every step read the rules of every doc.

## Consequences

`SKILL.md` keeps only the flow and points to the guide a step needs.
