# 017. Links point only to what a doc rests on

Decided: 2026-11-02

Partly replaced by 021: FEATURES links to all a feature rests on and all that builds it, and by 034: The rules for a doc are hard and every guide is read at the start, under which each guide lists the links its doc may make.

## The problem

The docs linked to each other in every direction. Some sentences did nothing but point to another doc, the same link came back several times in one doc, and `specs/decisions/` kept a README that listed its own file names. A reader followed links in circles, and every rename broke links in places that did not need them.

## The choice

A link points to what its doc rests on, never the other way. PHILOSOPHY and CHANGELOG link to nothing, and PROPOSAL rarely links. DESIGNS links to a few points in PHILOSOPHY and down to its decisions and specs. FEATURES links to a few points in DESIGNS and down to its decisions and specs. GOALS, ROADMAP and TODO link to each other, to FEATURES and to DESIGNS. A spec or a decision links up to the doc it serves and never to its siblings. README links every doc once, and AGENTS.md links the docs in its read order. A doc still makes its point when the reader does not follow a link.

## Not chosen

- Free linking wherever it helps: the links grow in every direction and the docs stop reading on their own.
- An index file for the decisions: the numbered file names already list them in order, so the index is a second home.

## Consequences

The table lives in *Where a fact goes* in SKILL.md. A sentence that only points elsewhere is cut, and an ID is linked only where the table allows.
