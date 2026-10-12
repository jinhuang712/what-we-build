# Revisit a doc set

Use this when the docs exist but overlap, sprawl, drift from the code or tire the reader. The goal is the same as for a new project: each doc answers one question, and each fact has one home.

## 1. Audit

Read every doc. Report, without editing anything:

| What | How |
|---|---|
| Inventory | each doc with its line count and the date it last changed (`git log -1 --format=%cs -- <file>`) |
| Overlaps | a table: content → every doc that states it |
| Wrong home | facts that fail the placement test for the doc they sit in |
| Stale claims | statements the code or newer docs contradict, with `file:line` on both sides |
| Broken links | `scripts/check_links.py` |
| Cited headings | `git grep -n "<DOC>.md →"` and `git grep -n "<DOC>.md#"` across code and docs |

Spread the reading across subagents when the set is large. Ask each for a table with evidence, not a summary.

## 2. Agree on roles

Show the roles table from SKILL.md, adjusted to this project. Show what moves where. Ask one decision at a time:

- Which docs keep which role?
- Which docs merge or go? (Deleting a doc needs the user's yes. Git keeps it.)
- How much history stays? (Default: one dated clause per decision.)

Do not rewrite before the roles are agreed.

## 3. Rewrite

Work one doc at a time, or give each doc to its own subagent. Two writers on one file overwrite each other, so a doc that receives facts from another doc waits until that doc is done.

Give each subagent a written brief. Template:

```markdown
# Brief: rewrite <DOC>.md

Repo: <path>. Edit only <DOC>.md. Do not commit.

Role: <DOC>.md answers "<question>". It owns <...>. It leaves out <...>, which lives in <...>.

Keep: every rule, key, flag, number, path and command that is true now. Every heading that code or docs cite (list them). Status marks. Code blocks, copied exactly.

Remove: verification logs, mockup stories, who asked, "used to" narratives, repetition of other docs.

History: one clause per decision, with the date and the reason. The old text is in `git show HEAD:<DOC>.md`.

Wording: <paste the key rules from references/wording.md>.

Never: nest lists, delete blank lines to save space, split one sentence into sub-bullets, mark a goal met without evidence, rename a cited heading.

Report: old → new line count, facts you dropped that someone might miss, headings changed, claims you suspect are stale (do not fix them, list them).
```

## 4. Verify

Do not trust the reports. Check the files yourself:

- Line counts: `wc -l`. A doc that grew needs a reason.
- Lost facts: compare with `git show HEAD:<file>`. Spot-check the facts each report says it dropped.
- Links and anchors: `scripts/check_links.py`.
- Layout: `scripts/blank_lines.py`. It only adds or removes blank lines.
- Evidence: every "met", "done" or "verified" points to a measurement, a test or the user's word.
- Cited headings: re-run the grep from the audit.
- Language: one language across the set.

## 5. Review

Give the user the paths and a table of what changed per doc. Commit only after the user has read it. When the user challenges a result, stop and discuss before the next edit.

## Mistakes seen in real revisits

- A brief that said "40–60% fewer lines" got a doc that doubled: the writer split long bullets into nested sub-lists.
- A hard line limit got met by deleting every blank line, which made the doc harder to read.
- "Remove history" removed the reasons behind decisions. The user wanted history short, not gone.
- A rewrite marked two exit criteria "met" because the old text did not say "open".
- Principles rewritten "macro" still named features. Fewer, truer principles beat many diluted ones.
- A subagent stopped halfway left a half-rewritten file. Restore it from git before you start again.
