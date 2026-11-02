# Install

You need [Claude Code](https://docs.claude.com/en/docs/claude-code/overview).

## As a plugin

```sh
claude plugin marketplace add jinhuang712/what-we-build
claude plugin install what-we-build@what-we-build
```

Start a new Claude Code session. Type `/what-we-build:what-we-build` to check that it loaded (not yet verified with this plugin).

## As a personal skill

```sh
git clone https://github.com/jinhuang712/what-we-build.git ~/dev/skills/what-we-build
ln -s ~/dev/skills/what-we-build/skills/what-we-build ~/.claude/skills/what-we-build
```

Start a new Claude Code session. Type `/what-we-build` to check that it loaded.

## Update

- **As a plugin:** `claude plugin update what-we-build@what-we-build`
- **As a personal skill:** `git -C ~/dev/skills/what-we-build pull`

## Remove

- **As a plugin:** `claude plugin uninstall what-we-build@what-we-build`
- **As a personal skill:** `rm ~/.claude/skills/what-we-build` and then delete the clone

## When it fails

| What you see | What to do |
|---|---|
| The command is not found | Start a new Claude Code session and type it again |
| The plugin is not found | Check the marketplace with `claude plugin marketplace list` |
| The skill folder is empty | Check the clone path in the `ln -s` line |
