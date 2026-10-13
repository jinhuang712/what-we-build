# Changelog

## 0.2.0 — 2026-10-13

The first revisit of this repo with the skill itself. What it found changed the skill.

- A session is a conversation, not a form. The agent discusses, brainstorms or asks for a decision, depending on where the user is. Each doc guide's *Ask* becomes *Explore*, with a brainstorm prompt.
- Every doc guide now opens with what the doc is for, where it sits in a session and which facts belong in it. It names what to push back on, gives guidelines with their reasons, and shows weak and strong examples. SKILL.md keeps the flow and points to the guides.
- New rules between docs: each doc reads on its own, the owner changes first, reasons have homes, and a doc that restates the code is a cache.
- Formats follow the shape of the data in every doc, even when the same records appear elsewhere.
- Goals take a method column, and a decision is recorded only when it is hard to reverse, surprising and a real trade-off.
- Any edit sets a doc's mark back to `drafted`.
- The skill no longer defines how a product should feel. Each doc has a style, meaning its form, and the agent writes in its default voice.
- The revisit audit checks for thin sections, numbers with no source, and text that restates the code. It ends with a changelog entry.
- The lessons from real sessions are phrased as the target behavior, each with the failure that taught it.

## 0.1.0 — 2026-10-12

The first release.

- `/what-we-build` drafts a new project's founding docs through a conversation, one decision at a time: PROPOSAL, PHILOSOPHY, GOALS, FEATURES, DESIGNS, ROADMAP and README, plus optional docs when the project needs them.
- `/what-we-build resume` continues a session from the marks on each doc.
- `/what-we-build revisit` cleans a doc set that overlaps, sprawls or drifted.
- Two checks: `check_links.py` for broken links and anchors, `blank_lines.py` for blank lines around blocks.
