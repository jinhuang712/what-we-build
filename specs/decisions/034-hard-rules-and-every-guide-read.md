# 034. The rules for a doc are hard and every guide is read at the start

Decided: 2026-11-04

## The problem

Four runs before 2026-11-04 used the skill on a game engine, a bill tool, a diagram library and an editor. In each one the user had to step in for things the skill already said:

- The agents read the guides only when the user asked, and some handed them to a subagent.
- They gave items no IDs and split no feature or checkpoint into a second level.
- They linked one spec to another, and one then swapped the links for plain-text pointers.
- They marked features and checkpoints ✅ that nobody had run.
- They wrote numbers with no source into the docs, such as a 2% limit for asking the user.

The rules were there but soft. A guide was read only when a step named it, the link table said only where a doc may link, and splitting was left to judgment. An agent busy with a task read each gap as a choice and took the shorter way.

## The choice

The agent reads `SKILL.md` and every guide in full at the start and after each compaction. The rules for what a doc must be are hard:

- A `[MAYBE]` that let a doc skip its skeleton or a sub-checkpoint skip its exit criteria is gone.
- Each guide lists the only links its doc may make, and a link goes one way.
- A plain-text pointer in place of a link is ruled out.
- `SKILL.md` names the ID levels of each doc, and the guides say when an item must split.
- A ✅ needs a run, and a claim nobody ran is marked ❔.
- A doc is checked line by line before the user sees it, and the agent shows what each check found as its proof.
- Reading a rule so that it can be skipped is itself ruled out.
- A line is never kept because it is old.
- A doc that moves into a new form has every item judged again, done items too.
- A doc the skill did not write is not trusted, and each of its claims is checked against the code or the user.
- Only the user ends the talk on a doc, and until then the agent looks for the next line that breaks a rule.

How to do the work stays with the model. A step no longer reads only its own guide.

## Not chosen

- Keep the guides on demand and name the guide in every step: the runs show the agent skips the read whatever the step says.
- Put all the rules into `SKILL.md`: it would break the size limit and mix the rules of every doc into one list.
- Louder wording such as MUST in capitals: it makes a model overreact and leaves the gaps where they were.
- The talk ends when both sides judge it enough, as before: the agent judged it alone and left for code or another topic.
- A `[WHEN]` that tells the agent where a shared fact goes when two specs share it: the rule on a second home already covers it, and one more line only adds weight.

## Consequences

Every start reads about 1,500 lines. The guides grow a few `[NO]` lines each. The split rules use "more than one case" and "more than one feature group", which the user may still tune.
