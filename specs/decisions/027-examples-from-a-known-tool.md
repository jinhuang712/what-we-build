# 027. Examples come from a tool the reader knows

Decided: 2026-11-03

## The problem

A draft of the FEATURES guide used a notes app to show a group, a feature and a part. The user found it harder to grasp than an example from Claude Code. Both readers of the skill know Claude Code: the user works in it, and the agent is a Claude model.

## The choice

An example comes from this repo or from the stable ideas of a well-known tool, such as the sessions and hooks of Claude Code. It never names a command or a flag. It rests on [DESIGNS 5: Examples the reader knows](../../DESIGNS.md#5-examples-the-reader-knows).

## Not chosen

- Invented examples only: a reader must learn a made-up product before the point lands.
- Any real project: its details change and its text invites copying.
- An exception for each case: the rule and the guides would drift apart.

## Consequences

Old invented examples stay until their guide is next changed.
