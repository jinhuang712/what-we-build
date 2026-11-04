# 030. The main window reads and writes the docs

Decided: 2026-11-03

Partly replaced by 038: Two guidelines leave DESIGNS, under which No dependencies is no longer a guideline.

## The problem

A run on a Go library loaded the skill and sent the whole rewrite to subagents. They rewrote every doc while the main window read none of them in full. It reported only bytes and lines, and it later rebuilt FEATURES from a copy that had lost parts of the compaction design. The docs changed, but the window and the user learned nothing about the project. That defeats the skill, whose context is what the agent and the user work out together. A global rule that lists deep reading as a subagent job pushed the agent this way.

## The choice

The main window reads each doc it works on in full and writes it with the user. A subagent never reads or writes a doc, and that includes checking a doc against the code. A subagent may still read the code. The rule sits in *While you work*, so it reaches the project's `AGENTS.md`.

## Not chosen

- Subagents check the docs after the main window reads them: the user chose to keep every doc task in the main window.
- A hook that blocks a subagent from writing Markdown: it is a dependency and breaks DESIGNS 3: No dependencies.
- A proof of reading such as quoting the doc first: the user did not want the rules to grow thick.

## Consequences

A large rewrite is slower, since one window reads every doc. A global rule that sends deep reading to subagents now conflicts with the skill, so the user may narrow it to code.
