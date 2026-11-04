# Install

You need git and a coding agent that loads Agent Skills. The steps below are for [Claude Code](https://docs.claude.com/en/docs/claude-code/overview), the only agent tried so far.

## Clone and link

```sh
git clone https://github.com/jinhuang712/what-we-build.git ~/dev/skills/what-we-build
ln -s ~/dev/skills/what-we-build/skills/what-we-build ~/.claude/skills/what-we-build
```

Restart Claude Code. Type `/what-we-build` to check that it loaded.

## Update

`git -C ~/dev/skills/what-we-build pull`

## Remove

`rm ~/.claude/skills/what-we-build` and then delete the clone.

## When it fails

- **The command is not found:** restart Claude Code and type it again.
- **The skill folder is empty:** check the clone path in the `ln -s` line.
- **`ln` says No such file or directory:** run `mkdir -p ~/.claude/skills` and run the `ln -s` line again.
