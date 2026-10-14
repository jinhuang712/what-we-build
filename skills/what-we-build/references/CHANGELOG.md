# CHANGELOG.md

The changelog tells users what changed in each release, in words they understand. It is the doc people read before they upgrade.

**Owns:** one section per version with its date, grouped by area.

**Recommend it for every project, and create it when the doc set is agreed,** with an empty *Unreleased* section, so the first change has a place to land. In one session the user asked for it with the doc set, and three approved docs later the file still did not exist. A fact belongs here when it shipped in a release.

## Guidelines

- **Write from the user's side:** what they can now do, or what no longer breaks.
- **Keep an *Unreleased* section** and fill it in the change that does the work, so release day needs no archaeology.

| Weak | Strong |
|---|---|
| "Refactored the export module." | "Exports now keep your column order." |
