# README.md

The README is the front door. A visitor reads it in about thirty seconds to decide whether the project is for them. Then they read it to start using it. It summarizes the other docs at pitch level and points to them.

It comes last, because it sums up the approved docs.

## What is it

Point anything a [NO] line rules out to its home, or push back when it has none.

- [YES]   open with a hero image and the tagline.
- [YES]   what it is, and what it does in a few bullets.
- [YES]   how to install it in one line.
- [YES]   lead with the one constraint that sets the project apart.
- [YES]   show how to use it with the first real task from start to result.
- [YES]   emoji where they carry meaning, such as a mark beside each capability.
- [YES]   color on the page through the hero and the diagrams, with badges and callouts.
- [YES]   link each doc once in *Docs*, and copy no status.
- [YES]   link INSTALL from *Install* too so whoever changes the one line finds the rest.
- [NO]    detail another doc owns, even as a copy.
- [NO]    a fact written only in the README.
- [NO]    emoji as decoration on every line.
- [NO]    an optional section with no owner doc behind it.
- [MAYBE] an architecture diagram that sums up `specs/ARCHITECTURE.md`, which you recommend.

## Optional sections

Add a section only when the project needs it. Each one summarizes its owner doc.

| Section | Add when | Owner |
|---|---|---|
| Architecture | recommended with `specs/ARCHITECTURE.md` | `specs/ARCHITECTURE.md` |
| Demo | a screenshot or recording that shows it faster than words | — |
| Why | a reason not obvious from what it is | PROPOSAL |
| Examples | a real case that teaches faster than the rules | FEATURES |
| Configuration | settings a user will change | FEATURES |
| How it compares | questions on how it differs from a known tool | PROPOSAL |
| FAQ | the same questions again and again | the doc that owns each answer |
| Known limits | a limit to know before trying it | FEATURES |
| Contributing | a `CONTRIBUTING.md` | CONTRIBUTING |
| Acknowledgements | work it builds on | `specs/decisions/` |

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

- <a mark> **<a capability>:** <what it does, in a line>

## Install

<one line>

<a link to INSTALL.md, when there is one>

## How to use

<the first real task, from start to result>

## Architecture

<the diagram from specs/ARCHITECTURE.md>

## Docs

<a link to every other doc>

## License
```
