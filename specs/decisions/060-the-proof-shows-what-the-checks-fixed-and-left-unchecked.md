# 060. The proof shows what the checks fixed and what they left unchecked

Decided: 2026-11-11

## The problem

Before the user saw a doc, the agent listed what each check found line by line as the proof that the doc was done. On a diagram tool and an editor from 2026-11-07 to 2026-11-08 these proofs grew into long reports that the users called a mess. The lines that mattered sat among checks that had found nothing.

## The choice

- The proof holds what the checks fixed and what they left unchecked.
- A check that found nothing is not listed.

## Not chosen

- Every check line by line: the user reads past what was fine to find what changed.
- No proof: the user would have to look for the problems again.

## Consequences

The report is shorter. It shows which checks changed something or did not run, and it no longer shows each check that passed.
