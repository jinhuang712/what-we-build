# specs/ARCHITECTURE.md

ARCHITECTURE.md is the map of the whole project. A new contributor reads it first to learn what the parts are and where to look. It stays at the macro level. How each part works inside goes in that part's own spec.

**Owns:**

- The parts, and what each one does.
- How the parts connect, with a diagram.
- Where each part lives in the code.

**Leaves out:**

- How a part works inside (its spec in `specs/`).
- The guidelines the design must meet (DESIGNS).
- The forks behind the shape (`specs/decisions/`).
- What the user sees (FEATURES).

**Push back on:**

- A part explained in detail that needs its own spec.
- A map that lists files instead of parts.
- A map with no diagram.

**Add when** the project has more than one part worth a spec.

## Guidelines

- **Always open with a diagram of the whole,** so the reader sees the shape before the words.
- **Name each part by what it does.**
- **Name each part's folder rather than its files,** because folders change less often.

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
