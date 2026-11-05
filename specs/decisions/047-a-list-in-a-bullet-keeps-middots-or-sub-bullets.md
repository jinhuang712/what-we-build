# 047. A list in a bullet keeps middots after a colon or moves to sub-bullets

Decided: 2026-11-05

## The problem

A bullet holds at most one comma, and ` · ` may not stand in for commas in a sentence. In a run on a diagram tool the agent met both rules by replacing 58 middots with "and", which gave lines such as "kind and label and weight and arrowheads". The rules passed and the lines got harder to read.

## The choice

A list after a colon keeps ` · ` between its items. A list that outgrows one line takes a sub-bullet per item. "And" repeated in place of commas or ` · ` is ruled out.

## Not chosen

- Drop the comma rule for lists: bullets would again hold several points behind a list of commas.
- Allow ` · ` anywhere: it would stand in for commas in plain sentences, which is why the rule exists.
- Sub-bullets for every list: a short list of names would take five lines.

## Consequences

SKILL.md gives three lines of its budget to this. A list in the middle of a sentence still has to be reworded or moved after a colon.
