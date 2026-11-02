# Install

You need [Claude Code](https://docs.claude.com/en/docs/claude-code/overview).

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

| What you see | What to do |
|---|---|
| The command is not found | Restart Claude Code and type it again |
| The skill folder is empty | Check the clone path in the `ln -s` line |
