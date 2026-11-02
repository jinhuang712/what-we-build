<!-- what-we-build: approved 2026-11-02 -->

# Goals

Each goal ties to a want or a risk in [PROPOSAL.md](PROPOSAL.md). A goal met on one project stays open for another until it is checked there. A status changes only with a check and its date. For goals checked on this repo, the reader who checks did not write the change. The docs were rewritten after 2026-10-13, so every result from that day waits for a new check.

## Objectives

| # | Objective | Want | Acceptance | Checked | Status |
|---|---|---|---|---|---|
| G1 | One sitting | Risk: the user wants the docs and not the talk | A new project's 7 core docs are drafted and approved in 1 sitting | end of phase | ⬜ |
| G11 | Context survives compaction | Context that outlives the session | After a compaction the agent names the current task and the latest decisions from the docs alone | end of phase | ⬜ |

## Measures

| # | Measure | How it is measured | Checked | Last value |
|---|---|---|---|---|
| G12 | Reads before it changes | Share of changes in sampled sittings made after reading the owning doc | end of phase | not measured |
| G13 | Sentences over the comma rule | Sentences outside tables with two or more commas in the core docs except PHILOSOPHY | every change | 5 on 2026-11-02 and 34 at v0.4.0 |
| G14 | Length of the core docs | `wc -l` over the 7 core docs | every change | 693 on 2026-11-02 and 614 at v0.4.0 |

## Benchmarks

| # | Benchmark | Problem set | Checked | Last score |
|---|---|---|---|---|
| G15 | Session quality | Three realistic project prompts (ROADMAP M3.1) scored against G2–G5 | end of phase | not run |

## Comparisons

| # | Comparison | Against | How it is run | Checked | Last result |
|---|---|---|---|---|---|
| G16 | With and without the skill | The same agent without the skill | The G15 prompts run both ways and scored the same way | end of phase | not run |

## Thresholds

| # | Threshold | Limit | How it is checked | Checked | Status |
|---|---|---|---|---|---|
| G2 | One home per fact | 0 facts written out in full in two docs | An independent audit lists every such fact | end of phase | ⬜ last not met 2026-10-13 with 8 facts |
| G3 | Goals that can be checked | 0 goals without a check | Read GOALS.md row by row | every change | ⬜ last met 2026-10-13 |
| G4 | Decisions with reasons | 0 decisions without what was not chosen and why | Read every file in `specs/decisions/` | every change | ⬜ |
| G6 | A short skill | `SKILL.md` ≤ 500 lines | `wc -l skills/what-we-build/SKILL.md` | every change | ⬜ 207 lines on 2026-11-02 by the author |
| G7 | Links that work | 0 broken relative links and anchors | A reader follows every relative link and anchor | every change | ⬜ last met 2026-10-13 |
| G8 | Manual start only | 0 automatic starts | Watch sittings for a load without `/what-we-build` | end of phase | ⬜ |
| G9 | Guidelines that can be tested | 0 guidelines a reader cannot test | A reader names a design that each DESIGNS guideline rejects | end of phase | ⬜ |

## Constraints

| # | Constraint | How it is checked | Checked | Status |
|---|---|---|---|---|
| G5 | No draft before agreement and no commit before approval | Read the session for each doc's first write and its commit | every change | ⬜ last not met 2026-10-13 |
| G17 | No dependencies ([DESIGNS 3](DESIGNS.md#3-no-dependencies)) | `skills/what-we-build/` holds only Markdown files | every change | ⬜ |
| G18 | Our own words ([DESIGNS 4](DESIGNS.md#4-our-own-words-over-borrowed-text)) | No passage in `skills/` is copied from a source | every change | ⬜ |
| G19 | Made-up examples ([DESIGNS 5](DESIGNS.md#5-made-up-examples-over-real-projects)) | No example in `skills/` names or quotes another project | every change | ⬜ |
| G20 | No code chunks in docs | No doc in this repo pastes code or a command longer than two lines | every change | ⬜ |

G10 was retired on 2026-11-02 and its number is not reused.
