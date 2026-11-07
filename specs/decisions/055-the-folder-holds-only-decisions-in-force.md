# 055. The decisions folder holds only decisions in force

Decided: 2026-11-08

## The problem

A replaced decision stayed with a line that named its successor, so the folder only grew. This repo reached 54 files, 13 of them replaced in whole or in part, and a project on a diagram tool reached 99. A reader had to work out which parts still held.

## The choice

The folder holds only the decisions in force, and git keeps the rest. A replaced decision is deleted or rewritten, and two on one topic merge.

## Not chosen

- A line that names the later decision: the file count never falls, and the reader must combine two files.
- An archive folder: it is a second copy of what git already holds.
- Renumbering after a delete: it breaks links and gains nothing, so numbers keep their gaps.

## Consequences

The path that led to a decision is only in git. Each decision's *Not chosen* has to carry the reasons worth keeping.
