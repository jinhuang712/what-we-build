<!-- what-we-build: approved 2026-11-02 -->

# 003. The plugin manifest sits at the repo root

Decided: 2026-10-12

## The problem

The skill should install as a plugin and also as a linked folder.

## The choice

The manifest sits in `.claude-plugin/` at the repo root. The repo installs as a plugin, and its skill folder also works when linked into `~/.claude/skills`.

## Not chosen

- A plugin-only layout: the skill folder would not work when linked on its own.

## Consequences

The install steps are in [README.md](../../README.md).
