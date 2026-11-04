# 029. A guide is written in tagged lines

Decided: 2026-11-03

## The problem

Once a guide defined its doc's core idea in tagged lines, it mixed two styles. Its core idea read as `[YES]` and `[NO]` lines, while the rest stayed as *Owns*, *Leaves out*, *Push back on* and bold *Guidelines*. The user found the tagged lines clearer and asked for the whole guide in them. Several old lists also said one thing twice, such as a *Push back on* item that repeated an *Owns* line.

## The choice

Every guide has the same sections:

| Section | Holds |
|---|---|
| *What is it* | what goes in and elsewhere and the form in one list |
| the core idea | a block of tagged lines where a model blurs it |
| *You have it when* | the checks as before |
| *Skeleton* | the form as before |

One sentence opens *What is it* when the guide had a *Push back on* list: point anything a `[NO]` line rules out to its home, or push back when it has none. A list always runs `[YES]`, `[NO]`, `[MAYBE]` and then `[WHEN]`, so a reader finds each kind in the same place. A list holds at least two kinds, because a list of only `[YES]` draws no edge. A line that repeated another was dropped. Tables such as the GOALS kinds and the TODO tags stay tables.

## Not chosen

- Tags for *You have it when*: each check is a test, and a `[YES]` on every line adds nothing.
- A `[PUSH BACK]` tag: it is a fifth tag for what `[NO]` already says, and the opening sentence covers it.
- The old lists beside the tags: two styles make a reader ask which one rules.
- *What it holds* and *How to write it* as two sections: they repeated each other, and a short section forced a made-up line to reach two kinds of tag.

## Consequences

The guides lost 121 lines. The bold lead of each guideline is gone, so a guide is scanned by its tags instead. `SKILL.md` and this repo's `AGENTS.md` follow in the same lines, and their tables stay tables. Each tag is padded so the text after it starts in one column.
