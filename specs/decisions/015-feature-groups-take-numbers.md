# 015. Feature groups take numbers

Decided: 2026-11-03

## The problem

FEATURES grouped its features under headings with no ID, and the features inside were numbered in the order they were added. A group could not be pointed to. F5: Keep the context while you work sat between F2: Resume and F3: The doc set, because it came later and joined the middle group. Two features were the groups under another name: F1: Start and talk each doc through and F3: The doc set.

## The choice

Each group is a feature with an ID, and the features in it are its parts. The groups become F1: Writing the docs with you, F2: Keeping the context and F3: Getting the docs. The two old features that were the groups under another name fold into them, so their parts keep their IDs. F2: Resume becomes F1.7: Resume, F5: Keep the context while you work becomes F2.1: Keep the context while you work and F4: Wording rules becomes F3.5: Wording rules.

## Not chosen

- Keeping the numbers and the order: a group stays without an ID, and the order keeps reading as a mistake.
- Keeping the two old features as a third level under their groups: the same idea would sit at two levels and the IDs would grow deep.

## Consequences

This breaks the rule that a feature ID never changes, for the three features that moved. The links to them in FEATURES, ROADMAP and TODO move in the same change. From here on a new feature takes the next number inside its group.
