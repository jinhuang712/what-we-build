# 028. A guide says what its doc's core idea is and is not

Decided: 2026-11-03

## The problem

A run on a Go library rewrote FEATURES three times over. The agent grouped the features by code module, then by outcome, and then split them into 93 features. The guide said "F1 is a group" and never said what a group is. Other guides left their core idea just as open, such as a want against a feature or a guideline against a decision.

## The choice

A guide whose core idea a model tends to blur defines it in a short block of tagged lines: `[YES]` for what it is, `[NO]` for what it is not, `[MAYBE]` for what it may be and `[WHEN]` for a situation that changes it. A block uses only the tags it has something for. The idea is borrowed from NYMs, while the block stays plain Markdown. It rests on DESIGNS 6: Hard rules for the doc, the method left to the model, since it says what a thing is and leaves the method to the model.

## Not chosen

- Prose under *Guidelines*: the run showed a model reads past a boundary written as an aside.
- A block in every guide: the other eight guides have no idea a model blurs, and a block there only makes them longer.
- The NYMs letters themselves: a guide reader need not know NYMs.

## Consequences

The DESIGNS guide lost its *Push back on* list, and the ROADMAP and GOALS guides each lost one item, because the block covers them. FEATURES now says *sub-feature* for what it called a part, so *part* means only a piece of the project as SPECS defines it.
