# 015. Feature groups take numbers

Decided: 2026-11-03

## The problem

FEATURES grouped its features under headings with no ID, and the features inside were numbered in the order they were added. A group could not be pointed to, and F5 sat between F2 and F3 because it came later and joined the middle group. Two features were the groups under another name: F1 Start and talk each doc through and F3 The doc set.

## The choice

Each group is a feature with an ID, and the features in it are its parts. Writing the docs with you is F1, Keeping the context is F2 and Getting the docs is F3. The old F1 and F3 merge into their groups, so their parts keep their IDs. Resume becomes F1.7, Keep the context while you work becomes F2.1 and Wording rules becomes F3.5.

## Not chosen

- Keeping the numbers and the order: a group stays without an ID, and the order keeps reading as a mistake.
- Keeping the old F1 and F3 as a third level such as F1.1.1: the same idea would sit at two levels and the IDs grow deep.

## Consequences

This breaks the rule that a feature ID never changes, once and for all three moved features. The links to them in FEATURES, ROADMAP and TODO move in the same change. From here on a new feature takes the next number inside its group.
