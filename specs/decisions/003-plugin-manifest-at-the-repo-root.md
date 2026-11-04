# 003. The plugin manifest sits at the repo root

Decided: 2026-10-12

Replaced by 016: A skill and no plugin.

## The problem

The skill should install as a plugin and also as a linked folder.

## The choice

The manifest sits in `.claude-plugin/` at the repo root. The repo installs as a plugin, and its skill folder also works when linked into `~/.claude/skills`.

## Not chosen

- A plugin-only layout: the skill folder would not work when linked on its own.

## Consequences

Both ways to install must keep working, and INSTALL.md describes each.
