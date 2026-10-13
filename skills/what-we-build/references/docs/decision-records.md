# Decision records

A decision record holds one decision in its own file, when DESIGNS.md has too many to read. It is the ADR (architecture decision record) format.

**Owns:** one decision per file (`docs/decisions/0001-<slug>.md`): the context, the decision with the option it beat, and its reason, in one to three sentences. Add the other alternatives or the consequences only when they are not obvious.

**Add when** DESIGNS.md holds so many decisions that it becomes hard to read. Keep each decision's one-line summary in DESIGNS.md, with a link to its record.

## Guidelines

- **Record only decisions that pass the bar:** hard to reverse, surprising without context, and a real trade-off.
- **Keep it to one paragraph** unless the alternatives are worth remembering.
