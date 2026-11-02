# 016. A skill and no plugin

Decided: 2026-11-03

## The problem

The repo shipped a plugin manifest so the skill could install with `claude plugin install`. The plugin held one skill and no hooks, agents or servers. Installed that way the command became `/what-we-build:what-we-build`, while every doc called it `/what-we-build`. Each release also had to set the same version in two manifest files.

## The choice

what-we-build is a personal skill only. A user clones the repo and links its skill folder into `~/.claude/skills`, and types `/what-we-build`. The manifest in `.claude-plugin/` is removed, and a release is a git tag.

## Not chosen

- Keeping the plugin beside the skill: the long command name and the two version fields stay for a channel that gives nothing the linked folder lacks.
- The plugin as the main way with the skill in INSTALL: every use pays the long command name.

## Consequences

Nobody finds the skill through a plugin marketplace. A user who installed the plugin uninstalls it and links the folder instead. It replaces 003: The plugin manifest sits at the repo root.
