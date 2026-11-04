# TODO.md

TODO.md tracks what is open:

- Issues found.
- Discussions to hold.
- Tasks to do.
- Ideas to keep.

Each item has a priority, a type and a time. A reader sees what matters first and how old it is.

## What is it

- [YES]   the open items, each with enough context and evidence to act on.
- [YES]   link an item to any file it needs, since an open item may sit anywhere.
- [NO]    work with a checkpoint, which ROADMAP holds.
- [NO]    what is already decided, which `specs/decisions/` holds.
- [WHEN]  a change handles an item: delete the item and its evidence files in that change, since git keeps the history.
- [WHEN]  an item gets a checkpoint: move it to ROADMAP.

## Priority

| Tag | Means |
|---|---|
| `P0` | broken or blocked now and done first |
| `P1` | done before the current checkpoint |
| `P2` | worth doing with no deadline |

## Type

| Tag | Means |
|---|---|
| `ISSUE` | something wrong |
| `DISCUSSION` | a decision needed |
| `TASK` | known work with a clear end |
| `IDEA` | a maybe kept so it is not lost |

## Fields

| Field | Holds |
|---|---|
| `description` | what happens and what should happen |
| `created` / `updated` | dates as `YYYY-MM-DD` |
| `status` | `OPEN` when ready or `HALT` when it waits on what `next` names |
| `found` | where and how it was found |
| `branch` | the branch or worktree of the work |
| `evidence` | links to files in `plan/evidence/` such as logs or screenshots |
| `next` | the next step |
| `blocks` | what waits for this item |
| `related` | links to related docs or items |

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
- status: OPEN
- found: <where, and how>
- evidence: <link to a file in plan/evidence/>
- next: <the next step>

### [P1][DISCUSSION] <the question>

- description: <why it is open>
- created: YYYY-MM-DD
- blocks: <what waits for the answer>
```
