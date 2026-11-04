# GLOSSARY.md

The glossary fixes the project's words: one name per thing, each with its meaning. It stops two words from naming one thing. That is how docs and code start to disagree.

## What is it

- [YES]   the project's terms.
- [YES]   the one name chosen for each thing.
- [YES]   pick one name and record the losing synonyms so search still finds them.
- [YES]   define each term so a newcomer understands it.
- [NO]    a link to another doc, since the docs that use a term link to it.
- [WHEN]  the first doc is written: start the glossary, and add terms as they appear.
- [WHEN]  the name in today's code differs: give it too until the code catches up.

## Term

- [YES]   a word with a meaning of its own in the project, such as *Hook* or *Subagent* in Claude Code.
- [YES]   a word two people might name differently.
- [NO]    an ordinary word in its ordinary sense, such as *file*.
- [NO]    every type in the code.
- [MAYBE] a type name, when users meet the thing by that name.

## You have it when

- No two words name one thing.
- Every term has a meaning a newcomer understands.
- A reader of the code can find each term by the name the code uses.

## Skeleton

```markdown
# Glossary

<each term with its meaning, its losing synonyms and its name in code if different>
```
