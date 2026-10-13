# Revisit a doc set

Use this procedure when the docs exist but overlap, sprawl, read thin or drifted from the code. The goal is the same as for a new project: each doc answers one question, each fact has one home, and each doc reads on its own.

A revisit changes many files at once, so it moves in five steps, and the user approves the plan before any file changes.

## 1. Audit

Read every doc, and report what you find without editing anything. The audit is the evidence for every change that follows, so give each finding a file and a line.

| Check | How |
|---|---|
| Inventory | each doc with its line count and the date it last changed (`git log -1 --format=%cs -- <file>`) |
| Facts in more than one doc | a table: the fact → every doc that states it in full |
| Wrong home | facts that fail the placement test for the doc they sit in |
| Thin sections | sections with only rules or tables, and no description of what they are or why |
| Unsourced numbers | every number that states a fact with no measurement, file or person behind it |
| Unverified claims | statements about behavior (commands, install steps, names) that nobody has run |
| Restated code | text that repeats the code, config or command output, with no reason the code cannot give |
| Principles that pick no side | principles that fail the opposite, case or cost test, refuse nothing, or make a choice that names a feature, and design principles with no cost or no check |
| Words with two meanings | one word used for two things, such as "session" for a tool session and a conversation |
| Docs under an older rule | docs last changed before the skill's rules last changed, checked against the current rules |
| Stale claims | statements the code or newer docs contradict, with `file:line` on both sides |
| Broken links | every relative link and `#anchor`, followed to its target |
| Cited headings | `git grep -n "<DOC>.md →"` and `git grep -n "<DOC>.md#"` across the code and docs |
| Goals | every goal in GOALS.md measured on the docs themselves where it can be, for example "one home per fact" |

Spread the reading across subagents when the set is large. Ask each one for a table with evidence, not a summary. Let at least one reader be someone who did not write the docs, because an author reads what they meant, not what they wrote.

### Give each conflict its cause

A conflict between the docs and the skill is a signal, not only an error. Its cause decides what changes:

| Cause | What changes |
|---|---|
| The doc did not follow the rule | the doc |
| The rule changed after the doc was written | the doc, and the habit of checking old docs when a rule changes |
| Two rules collide | the skill: settle which rule wins, and when |
| The rule assumes another kind of project | the skill: widen the rule |
| No rule covers the case | the skill: add the rule |
| The author graded their own work | the measurement: repeat it with another reader |

## 2. Agree on roles

Show the table in SKILL.md → *The doc set*, adjusted to this project, and show what moves where. Then ask one decision at a time:

- Which docs keep which role?
- Which docs merge or go? Deleting a doc needs the user's yes, even though git keeps it.
- How much history stays? The default is one dated clause per decision.

Show the planned changes as before-and-after text, side by side when the user asks, before any file changes. A plan the user can see is a plan the user can correct.

## 3. Rewrite

Work one doc at a time, or give each doc to its own subagent. Two writers on one file overwrite each other, so a doc that receives facts from another doc waits until that doc is done.

Give each subagent a written brief. Template:

```markdown
# Brief: rewrite <DOC>.md

Repo: <path>. Edit only <DOC>.md. Leave the commit to the lead.

Role: <DOC>.md answers "<question>". It owns <...>. It leaves out <...>, which lives in <...>.

Keep: every rule, key, flag, number, path and command that is true now. Every heading that code or docs cite (list them). Status marks (✅ 🚧 🟨 ⬜ ❌). Code blocks, copied exactly.

Remove: verification logs, mockup stories, who asked, "used to" stories, and text that restates the code.

Each section: a short description of what it is and why, then guidelines with their reasons, then the specifics.

History: one clause per decision, with the date and the reason. The old text is in `git show HEAD:<DOC>.md`.

Format: a table for records, a list for parallel items, sentences for reasoning. Lists one level deep, one blank line around every block, each sentence whole.

Status: mark a goal met only with evidence. Keep every cited heading.

Wording: <paste the key rules from references/wording.md>.

Lessons: <paste SKILL.md → What real sessions taught>.

Report: old → new line count, facts you dropped that someone might miss, headings changed, claims you suspect are stale (list them, leave them unchanged).
```

## 4. Verify

Check the files yourself. A subagent's report says what it meant to do, not what it did.

- **Line counts:** `wc -l`. A doc that grew or shrank by more than a third needs a reason.
- **Lost facts:** compare with `git show HEAD:<file>`. Spot-check the facts each report says it dropped.
- **Links and anchors:** every relative link and `#anchor` resolves.
- **Layout:** one blank line before and after every heading, list, table and code fence ([wording.md](wording.md) → *Lists and tables*).
- **Evidence:** every "met", "done" or "verified" points to a measurement, a test or the user's word.
- **Cited headings:** run the grep from the audit again.
- **Goals:** measure the goals from the audit again, and record both results with their dates.
- **Marks:** every edited doc that carries a mark says `drafted`, with the date of the edit.
- **Changelog:** when the project keeps one, add an entry under *Unreleased*.

## 5. Review

Give the user the paths, and a table of what changed in each doc. Commit only after the user has read the result. When the user challenges a result, stop and discuss before the next edit.

## Lessons from real revisits

The lessons in SKILL.md → *What real sessions taught* apply to every revisit. One more is specific to rewriting with subagents. It states the target, then the failure that taught it.

- **Restore a half-written file from git before starting again.** A subagent stopped halfway left a file half rewritten.
