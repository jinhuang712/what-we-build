# CLI.md

CLI.md is the contract of the command line: what a person or a program may call and what comes back. The program follows it, so a command can stand here before its code exists. It says what `--help` cannot: what is only planned, and what a script may rely on.

It comes right after FEATURES, since each command is how a user reaches a feature.

## What is it

Point anything a [NO] line rules out to its home, or push back when it has none.

- [YES]   every command and flag with its status.
- [YES]   who calls each command: a person, a script or both.
- [YES]   what each command prints, with stdout and stderr apart.
- [YES]   each failure of a command with its exit code.
- [YES]   every exit code and what it means.
- [YES]   every output format a script relies on.
- [YES]   the environment variables the commands read.
- [YES]   a short example for each command with what it prints.
- [NO]    what a feature does for the user, which FEATURES holds.
- [NO]    what the project will not build, which FEATURES lists under *Not planned*.
- [NO]    how a command works inside, which `specs/` holds.
- [NO]    why a command has its shape, which `specs/decisions/` holds.
- [NO]    how to install it, which INSTALL holds.
- [NO]    a pasted `--help` or a generated reference, since that copies the program.
- [NO]    a link to another doc, since FEATURES links to CLI.
- [WHEN]  a command or what it returns changes: change CLI.md in the same change.

## Command

- [YES]   a name a person or a program calls, such as `notes search`.
- [YES]   say what a call prints and how it fails, such as *`notes search <text>` prints one line per note and exits 1 when the notes folder cannot be read*.
- [NO]    a flag, which sits under its command.
- [NO]    a script only the project's developers run, which CONTRIBUTING holds.
- [WHEN]  several commands share a flag: list it once under *Global flags*.

## You have it when

- A script's author can call every command and handle every failure without reading the code.
- A reader can tell what is built from what is planned.
- It agrees with the program, or the user knows where it does not.

## Skeleton

```markdown
# CLI

<who calls it: a person, a script or both>

Status: ✅ built · ⬜ planned

## Commands

### <command>

**Status:** ⬜

<how to call it, in one line>

| Flag | Means | Default |
|---|---|---|
| <flag> | <what it changes> | <its default> |

**Called by:** <a person, a script or both>

**Prints:** <what goes to stdout and what goes to stderr>

**Fails:** <each failure and its exit code>

**Example:** <a short call and what it prints>

## Global flags

| Flag | Means | Default |
|---|---|---|
| <flag> | <what it changes> | <its default> |

## Exit codes

| Code | Means |
|---|---|
| <code> | <what happened> |

## Output formats

<each format a script relies on>

## Environment

| Variable | Means | Default |
|---|---|---|
| <name> | <what it changes> | <its default> |
```
