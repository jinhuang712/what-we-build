# CLI.md

CLI.md is the reference for every command: what it does, its flags, its output and its exit codes. Scripts and people both depend on it, so it must match the program exactly.

**Owns:** every command and flag, with a mark for built or planned, exit codes, output formats, and examples.

**Add when** the project has a command-line interface. Draft it right after FEATURES.md, because each command is how a user reaches a feature. A fact belongs here when it is about a command, a flag or an exit code.

## Guidelines

- **Mark each command and flag** as built or planned, so nobody scripts against a flag that doesn't exist.
- **Show an example per command,** with its output.
- **Say what happens on failure,** and with which exit code. Scripts depend on it.

| Weak | Strong |
|---|---|
| "`search` finds notes." | "`notes search <text>` prints one line per note, best match first. Exits 1 when the notes folder can't be read." |

## Explore

Who calls each command, a person or a script? What does it print? What does it do on failure? Which flags are needed now, and which can wait?
