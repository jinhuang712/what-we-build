# INSTALL.md

INSTALL.md holds everything about installing beyond the one line in the README. A user reads it when that line is not enough.

**Owns:**

- What must be in place first.
- Every way to install it.
- How to check that it worked.
- How to update it and how to remove it.
- What to do when the install fails.

**Leaves out:**

- How to use it (README and FEATURES).
- How to deploy a service (RUNBOOK).
- How to set up for development (CONTRIBUTING).

**Push back on:**

- A step that does not work as written.
- A command longer than two lines instead of a script.
- A way to install that nobody has tried.

**Add when** the one line in the README is not the whole story.

## Guidelines

- **Put the most common way first.**
- **End each way with how to check that it worked.**

## You have it when

- A user on any supported setup can install it without asking anyone.
- Every way ends with a check.

## Skeleton

```markdown
# Install

<what must be in place first>

## <Way>

<the steps, then how to check that it worked>

## Update

## Remove

## When it fails

<what the user sees, and what to do>
```
