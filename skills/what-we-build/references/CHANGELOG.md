# CHANGELOG.md

The changelog tells users what changed in each release, in words they understand. It is the doc people read before they upgrade.

**Owns:** one section per version with its date, grouped by area.

**Add when** the doc set is agreed, for every project, with an empty *Unreleased* section so the first change has a place to land. Fill it in the change that does the work.

## Guidelines

- **Write from the user's side:** what they can now do, or what no longer breaks.
- **Give a break a before and after.**

## Skeleton

```markdown
# Changelog

## Unreleased

## <X.Y.Z> — <YYYY-MM-DD>

### Added
- <what the user can now do>

### Changed
- <what behaves differently, with before and after>

### Fixed
- <what no longer breaks>
```
