# PROPOSAL.md

The proposal is where the project begins: the case for why it should exist. It says what gap the project fills and why now. It gives the idea that fills the gap. A reader finishes it knowing whether the project is worth building.

It comes first, because every other doc builds on the reason it gives.

## What it holds

Point anything a [NO] line rules out to its home, or push back when it has none.

- [YES]   why the project should exist.
- [YES]   why now.
- [YES]   the idea.
- [YES]   what we want and what we don't want.
- [YES]   who it is for.
- [YES]   the risks.
- [NO]    how it is built, which DESIGNS holds.
- [NO]    exact behavior, which FEATURES holds.
- [NO]    the numbers, which GOALS holds.
- [NO]    progress, which ROADMAP holds.
- [NO]    the index of docs, which README holds.
- [NO]    a case that opens with the solution.
- [NO]    a reason with no example.
- [NO]    a "don't want" with no reason.

## Want and pain

**A want**

- [YES]   what someone needs in their own words, such as *pick up yesterday's work where it stopped*.
- [YES]   a reason it serves, from *Why it should exist*.
- [NO]    a feature, such as *resume a session*.
- [NO]    a number, which GOALS holds.
- [MAYBE] several features that meet it, which FEATURES works out.
- [WHEN]  the project already has code: the want comes from the pain, not from what the code does.

**A pain**

- [YES]   a moment someone hits with the sample or number that proves it, such as *a long session forgets what was decided*.
- [NO]    the lack of a solution, such as *there is no memory file*.

## How to write it

- [YES]   start from what the user brings in whatever form it takes.
- [YES]   give each pain its own section with the moment, number or sample that proves it.
- [YES]   argue the case so that every section makes it stronger.
- [WHEN]  something changed: write *Why now*, and leave it out otherwise.

## You have it when

- A stranger can say after one reading why the project should exist.
- Every want traces to the reason the project exists.
- The user recognizes the case as their own.

## Skeleton

```markdown
# <Name> — Proposal

> <tagline>

## In short

<a scene the reader knows, then the one-line answer>

## Why it should exist

<the reason in the user's own form, shown with an example>

### Pain points

<when the project eases a pain>

#### <the pain>

<the moment, number or sample that proves it>

## Why now

<what changed that makes it possible or urgent. Leave it out when nothing did>

## The idea

<the idea in one sentence, then what it means>

## What we want

- **<what someone needs>:** <how the project meets it>

## What we don't want

- **<what the project refuses to become>:** <why>

## Who it is for

<the people, and what each gets>

## Risks

<each risk, and what reduces it>
```
