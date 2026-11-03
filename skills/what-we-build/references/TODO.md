# TODO.md

TODO.md tracks what is open:

- Issues found.
- Discussions to hold.
- Tasks to do.
- Ideas to keep.

Each item has a priority, a type and a time. A reader sees what matters first and how old it is.

## What it holds

- [YES] the open items, each with enough context and evidence to act on.
- [NO] work with a checkpoint, which ROADMAP holds.
- [NO] what is already decided, which `specs/decisions/` holds.

## How to write it

- [WHEN] a change handles an item: delete the item and its evidence files in that change, since git keeps the history.
- [WHEN] an item gets a checkpoint: move it to ROADMAP.

## Priority

| Tag | Means |
|---|---|
| `P0` | Something is broken or blocked now. Do it first. |
| `P1` | Important. Do it before the current checkpoint. |
| `P2` | Worth doing. No deadline. |
| `P3` | Nice to have. It may never happen. |

## Type

| Tag | Means |
|---|---|
| `ISSUE` | Something is wrong. |
| `DISCUSSION` | A decision is needed. |
| `TASK` | Known work with a clear end. |
| `IDEA` | Maybe. Keep it so it is not lost. |

## Fields

| Field | Holds |
|---|---|
| `description` | What happens, and what should happen. |
| `created` / `updated` | Dates as `YYYY-MM-DD`. |
| `status` | `open`, `in progress` or `blocked`. |
| `found` | Where and how it was found. |
| `branch` | The branch or worktree the work is in. |
| `evidence` | Links to logs, screenshots or snippets kept as files in `plan/evidence/`. |
| `next` | The next step. |
| `blocks` | The checkpoint, feature or item that waits for this one. |
| `related` | Links to related docs or other items. |

Use the fields an item needs, and leave out the rest.

## You have it when

- A stranger can take the top item and act on it without asking anyone.
- Every item has a priority and a type.
- Nothing handled is left in it.

## Skeleton

```markdown
# TODO

## ongoing

### [P0][ISSUE] <what is wrong>

- description: <what happens, and what should happen>
- created: YYYY-MM-DD
- status: open
- found: <where, and how>
- evidence: <link to a file in plan/evidence/>
- next: <the next step>

### [P1][DISCUSSION] <the question>

- description: <why it is open>
- created: YYYY-MM-DD
- blocks: <what waits for the answer>
```
