# 026. The skill says what the agent must do, not each step

Decided: 2026-11-03

## The problem

A test on three repos showed the agent moving old docs into the new format without a talk. The skill had grown a branch for each start, a numbered loop for each change and steps for each resume. The agent followed the branches and skipped the talk, and no list of steps could cover every project and every user.

## The choice

The skill keeps what the agent would not do unasked: the stance it talks from, the home of each fact, the docs and their guides, and the rules that stop a mistake we have seen. It drops the steps a capable model takes on its own, such as how to find where the work stopped, and leaves the form of the talk to the model and the user. It rests on DESIGNS 6: Hard rules for the doc, the method left to the model.

## Not chosen

- A procedure for each start: it cannot be complete, and it turns the talk into a form.
- Cutting every rule that reads like a step: "Re-read the whole doc before any edit" stops patch writing, which the model does unasked.

## Consequences

The *Start* table, the approval loop and the resume steps are gone. A resume no longer names the first unfinished doc, as 024: Approval lives in the conversation did, and the agent only tells the user where the work stands. A new rule from a test goes in only when the model failed on what to do.
