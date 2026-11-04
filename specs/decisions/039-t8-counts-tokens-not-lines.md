# 039. T8 counts tokens and not lines

Decided: 2026-11-04

## The problem

T8: A doc read in one go held every doc within the two default limits of one Claude Code read, 25000 tokens and 2000 lines. A line can hold any amount of text, so a count of lines says little about how much a read must return.

## The choice

T8 holds every doc within 25000 tokens. A doc under 25000 bytes passes, since it never has more tokens than bytes. A larger doc passes when one read with no offset returns all of it.

## Not chosen

- Keeping the 2000 lines beside the tokens: the user ruled out a line count as a measure for the docs.
- Lines alone: a doc of few long lines could still pass a limit it breaks in tokens.

## Consequences

No goal counts lines any more. A doc of more than 2000 short lines would pass T8 and still be cut by a read, and that case is left until a doc comes near it.
