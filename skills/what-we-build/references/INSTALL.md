# INSTALL.md

INSTALL.md holds everything about installing beyond the one line in the README. A user reads it when that line is not enough.

## What it holds

Point anything a [NO] line rules out to its home, or push back when it has none.

- [YES] what must be in place first.
- [YES] every way to install it.
- [YES] how to check that it worked.
- [YES] how to update it and how to remove it.
- [YES] what to do when the install fails.
- [NO] how to use it, which README and FEATURES hold.
- [NO] how to deploy a service, which RUNBOOK holds.
- [NO] how to set up for development, which CONTRIBUTING holds.
- [NO] a step that does not work as written.
- [NO] a command longer than two lines instead of a script.
- [NO] a way to install that nobody has tried.

## How to write it

- [YES] put the most common way first.
- [YES] end each way with how to check that it worked.

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
