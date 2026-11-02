# CHANGELOG.md

The changelog tells users what changed in each release, in words they understand. It is the doc people read before they upgrade.

**Owns:**

- One section per version with its date, grouped by area.

**Add when** the doc set is agreed, in every project. Start it with an empty *Unreleased* section so the first change has a place to land. Fill it in the change that does the work.

## Guidelines

- **Write from the user's side:** what they can now do, or what no longer breaks.
- **Give a break a before and after.**

## You have it when

- A user can tell from it whether to upgrade, and what to change when they do.
- Every break has a before and an after.
- The *Unreleased* section holds the changes not yet released.

## Skeleton

```markdown
# Changelog

## Unreleased

## <X.Y.Z> — <YYYY-MM-DD>

### <area>

<what changed, from the user's side>
```
