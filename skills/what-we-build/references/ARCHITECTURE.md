# specs/ARCHITECTURE.md

ARCHITECTURE.md is the map of the whole project.
A new contributor reads it first to learn what the parts are and where to look.
It stays at the macro level.
How each part works inside goes in that part's own spec.

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
- A part that has a spec but no link to it.

**Add when** the project has more than one part worth a spec.

## Guidelines

- **Open with one diagram of the whole.** The reader sees the shape before the words.
- **Name each part by what it does,** and link to its spec.
- **Name the folder each part lives in, not the files.** Folders change less often.

## You have it when

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

Lives in: `<folder>`. How it works: <link to its spec>.
```
