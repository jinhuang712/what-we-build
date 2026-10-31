# README.md

The README is the front door. A visitor reads it to decide, in about thirty seconds, whether the project is for them, and then to start using it. It summarizes the other docs at pitch level and points to them.

It comes last, because it sums up the approved docs.

**Owns:** the tagline, a short description, what it does, a taste of it working, install, first use, the commands, the known limits, and links to every other doc.

**Leaves out:** detail any other doc owns.

**Push back on:** a fact written only in the README, and a copy of another doc's detail.

## Guidelines

- **Lead with the one constraint that sets the project apart.**
- **Show real output before the install steps.**
- **Say what it does in a few bullets,** and link to the doc that holds the detail.
- **Give install steps as commands that can be copied.**
- **Put a warning up front** when the tool is unofficial or risks an account.
- **Link to the status.** Do not copy it.

## You have it when

- A visitor can decide in thirty seconds whether the project is for them.
- A user can install and run it without asking anyone.
- Nothing is written only here.

## Skeleton

```markdown
# <Name>

> <tagline>

<what it is, and the one constraint that sets it apart>

## What it does
- <a capability, in a line>

## A taste
<real output of one command>

## Install
<commands that can be copied>

## First use
<the first steps, numbered>

## Commands
<a table: to do this, run this. Exit codes if they matter>

## Good to know
<the known limits, each in a line>

## Docs

| Doc | Answers |
|---|---|
| [FEATURES.md](FEATURES.md) | <the question it answers> |

## License
```
