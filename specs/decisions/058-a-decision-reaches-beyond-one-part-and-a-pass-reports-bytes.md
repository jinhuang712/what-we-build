# 058. A decision needs a fork that more than one part rests on, and each start pass reports the doc set's bytes

Decided: 2026-11-11

## The problem

Two doc sets grew faster than their code, as their git showed on 2026-11-11. One on a diagram tool went from 458K to 730K bytes in eleven days while its code grew 17%, and its 102 decisions held a third of those bytes. One on an editor went from 150K to 377K bytes with 55 decisions while its code grew 5%. The user had to ask a cleanup to cut the total, and a later cleanup cut 382 lines and added 546. Every fork with a reason became a file, and nothing showed the growth.

## The choice

- A choice is a decision only when it passes three tests:
  - Another way was weighed.
  - More than one part or feature rests on it.
  - The code does not show its reason.
- A detail of one screen or one command stays in the doc that holds it.
- Each start pass reports the bytes of the doc set before and after it.

## Not chosen

- Folding a finished checkpoint into one line: it cuts 13% of one roadmap and 43% of another, and ROADMAP is the view the user reads the work from.
- A byte limit for the doc set: no number has a source yet, and an agent could cut good lines to meet it.
- The old bar of any fork with a reason: it made a file of every detail.

## Consequences

The reason behind a small choice is no longer kept. The next start pass on a project removes the decisions below the bar and names each one it removed. A pass that grows the doc set shows it in its report.
