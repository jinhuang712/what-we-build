# 017. Links point only to what a doc rests on

Decided: 2026-11-02

## The problem

The docs linked to each other in every direction. Some sentences did nothing but point to another doc, the same link came back several times in one doc, and `specs/decisions/` kept a README that listed its own file names. A reader followed links in circles, and every rename broke links in places that did not need them.

## The choice

A link points to what its doc rests on, never the other way. Each guide lists the links its doc may make. A doc still makes its point when the reader does not follow a link.

## Not chosen

- Free linking wherever it helps: the links grow in every direction and the docs stop reading on their own.
- An index file for the decisions: the numbered file names already list them in order, so the index is a second home.

## Consequences

A sentence that only points elsewhere is cut, and an ID is linked only where its guide allows.
