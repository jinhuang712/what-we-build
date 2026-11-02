# README.md

The README is the front door.
A visitor reads it in about thirty seconds to decide whether the project is for them.
Then they read it to start using it.
It summarizes the other docs at pitch level and points to them.

It comes last, because it sums up the approved docs.

**Owns:**

- The hero image and the tagline.
- What it is.
- What it does.
- How to install it in one line.
- How to use it.
- Links to every other doc.

**Leaves out:**

- Detail any other doc owns.

**Push back on:**

- A fact written only in the README.
- A copy of another doc's detail.
- A README with no hero image.
- Emoji used as decoration on every line.
- An optional section with no owner doc behind it.

## Guidelines

- **Open with a hero image.** It shows what the project is before a word is read.
- **Lead with the one constraint that sets the project apart.**
- **Say what it does in a few bullets,** and link to the doc that holds the detail.
- **Install in one line,** and link to INSTALL.md for the rest.
- **Show how to use it with the first real task,** from start to result.
- **Recommend an architecture diagram** that sums up `specs/ARCHITECTURE.md`.
- **Use emoji where they carry meaning,** such as a mark beside each capability.
- **Give the page color** through the hero and the diagrams, with badges and callouts.
- **Link to the status.** Do not copy it.

## Optional sections

Add a section only when the project needs it.
Each one summarizes its owner doc and links to it.

| Section | Add when | Owner |
|---|---|---|
| Architecture | Recommended for a project with more than one part | `specs/ARCHITECTURE.md` |
| Demo | A screenshot or a recording shows it faster than words | — |
| Why | The reason is not obvious from what it is | PROPOSAL |
| Examples | A real case teaches faster than the rules | FEATURES |
| Configuration | It has settings a user will change | FEATURES |
| How it compares | Users will ask how it differs from a known tool | PROPOSAL |
| FAQ | The same questions keep coming | The doc that owns each answer |
| Known limits | A user should know a limit before trying it | FEATURES |
| Status | The project is not yet stable | ROADMAP |
| Contributing | Outsiders can help | CONTRIBUTING |
| Acknowledgements | It builds on others' work | `specs/decisions/` |

## You have it when

- A visitor can decide in thirty seconds whether the project is for them.
- A user can install it and finish a first task without asking anyone.
- Nothing is written only here.

## Skeleton

```markdown
# <Name>

![<Name>](<path to the hero image>)

> <tagline>

<what it is, and what sets it apart>

## What it does
- <a mark> <a capability, in a line>

## Install
<one line, then a link to INSTALL.md>

## How to use
<the first real task, from start to result>

## Architecture
<the diagram from specs/ARCHITECTURE.md, and a link to it>

## Docs

| Doc | Answers |
|---|---|
| [FEATURES.md](FEATURES.md) | <the question it answers> |

## License
```
