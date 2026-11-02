# 014. Summaries are ASCII trees

Decided: 2026-11-02 and 2026-11-03

## The problem

FEATURES, ROADMAP and GOALS each hold many entries in groups and parts, such as a feature with its sub-features or a checkpoint with its items. A reader needs to see all of them at once before reading any section. A summary written as flat text or a table hid how the entries nest, and a summary is only as good as the names it gives each entry.

## The choice

Each of the three docs opens with a summary drawn as an ASCII tree in a code block. Each line gives an entry's status, its ID with its name and a short description. An entry may have parts with IDs such as F1.1 or CP2.1.

## Not chosen

- No summary: a reader would have to scroll through every section to see the whole.
- A table: it flattens the nesting and forces every row into the same shape.
- A nested Markdown list with each ID as a link: the links work, but the nesting is hard to see in plain text and the lines read as prose.

## Consequences

The IDs in a summary are not links, because a code block shows text only. A reader finds a section by its name in the heading below.
