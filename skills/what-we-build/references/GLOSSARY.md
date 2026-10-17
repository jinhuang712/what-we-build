# GLOSSARY.md

The glossary fixes the project's words: one name per thing, each with a one-line meaning. It stops two words from naming one thing, which is how docs and code start to disagree.

**Owns:** the project's terms, and the one name chosen for each thing.

**Add when** the domain has its own terms, or two words compete for one thing. Start it with the first doc, and add terms as they appear.

## Guidelines

- **Pick one name and record the losing synonyms,** so search still finds them.
- **Define each term in one line,** in plain words.
- **Give the name in today's code when it differs.** The docs often settle a name before the code is renamed. A column with the name the code uses today lets a reader of the code find the thing, and it lists what a rename still has to change. Once the code catches up, the cell names the same thing the term does. In one session, the glossary carried such a column through a rename of the core types.

| Weak | Strong |
|---|---|
| Account, user, member and customer used for one thing | "**Member:** a person in a workspace. (Not: user, account, customer.)" |
| "**Member:** a person in a workspace." while the code still says `User` | The same line, with "In code today: the `User` model" in its own column |

## Explore

When two words name one thing, which one do we keep?
