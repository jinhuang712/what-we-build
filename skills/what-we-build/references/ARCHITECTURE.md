# specs/ARCHITECTURE.md

ARCHITECTURE.md is the map of the whole project. A new contributor reads it first to learn what the parts are and where to look. It stays at the macro level. How each part works inside goes in that part's own spec. A part is what the [SPECS](SPECS.md) guide calls one.

## What it holds

Point anything a [NO] line rules out to its home, or push back when it has none.

- [YES]   the parts and what each one does.
- [YES]   how the parts connect, with a diagram.
- [YES]   where each part lives in the code.
- [NO]    how a part works inside, which its spec in `specs/` holds.
- [NO]    the guidelines the design must meet, which DESIGNS holds.
- [NO]    the forks behind the shape, which `specs/decisions/` holds.
- [NO]    what the user sees, which FEATURES holds.
- [NO]    a map that lists files instead of parts.

## How to write it

- [YES]   always open with a diagram of the whole so the reader sees the shape before the words.
- [YES]   name each part by what it does.
- [YES]   name each part's folder rather than its files, because folders change less often.
- [NO]    a part named for how it is built, such as *utils*.

## You have it when

- It opens with a diagram of the whole.
- A new contributor knows where to look for any change.
- Every part in the code is on the map.
- Nothing in it explains how a part works inside.

## Skeleton

```markdown
# Architecture

<what the project does, in one paragraph>

<a diagram of the parts and how they connect>

## <Part>

<what it does, in a few lines>

<the folder it lives in>
```
