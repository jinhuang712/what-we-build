# CHANGELOG.md

The changelog tells users what changed in each release, in words they understand. It is the doc people read before they upgrade.

## What is it

- [YES]   one section per version with its date, grouped by area.
- [YES]   write from the user's side: what they can now do or what no longer breaks.
- [WHEN]  the project starts: give it an empty *Unreleased* section so the first change has a place to land.
- [WHEN]  a change does the work: fill its entry in that same change.
- [WHEN]  a change breaks something: give it a before and an after.

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
