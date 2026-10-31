# TODO.md

TODO.md tracks what is open: issues found, discussions to hold, tasks to do and ideas to keep. Each item has a priority, a type and a time, so a reader sees what matters first and how old it is.

**Owns:** the open items, each with enough context and evidence to act on.

**Leaves out:** work with a milestone (ROADMAP) and what is already decided (`specs/decisions/`).

**Add when** the doc set is agreed, for every project, so a finding has a home the moment it comes up.

## Guidelines

- **Delete an item when it is handled,** in the change that handles it. History lives in git.
- **Delete its evidence files too.**
- **Move an item to ROADMAP** once it has a milestone.

## Priority

| Tag | Means |
|---|---|
| `P0` | Something is broken or blocked now. Do it first. |
| `P1` | Important. Do it in the current milestone. |
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
| `blocks` | What waits for this item. |
| `related` | Links to FEATURES, specs, decisions or other items. |

Use the fields an item needs. Leave out the rest.

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
