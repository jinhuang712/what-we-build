<!-- what-we-build: drafted 2026-10-13 -->

# Designs

How what-we-build is built, and why. What goes in is a project folder and a conversation with the user. What comes out is a set of Markdown docs, each with a mark that says drafted or approved. In between is the skill: Markdown instructions that an agent reads, and two Python scripts that check the docs. What the skill does for the user is in [FEATURES.md](FEATURES.md).

## Principles

Each principle names the choice, what it costs, and how to check that it holds.

### Context

- **Short core, detail on demand.** `SKILL.md` holds what every session needs. The doc guides, the wording rules and the revisit procedure wait in reference files until a step points to them. Cost: a step must name its reference, or the agent never reads it. Holds as: `SKILL.md` stays within the limit in GOALS.md G6, and each step that needs a reference names its path.

### State

- **The docs are the state.** A mark on each doc's first line over a separate state file. Cost: points agreed for a doc that is not drafted yet are lost when the sitting ends. Holds as: no file but the docs records progress.

### Portability

- **No dependencies.** Markdown and Python's standard library. Cost: the checks read Markdown with regular expressions instead of a parser. Holds as: the scripts import only the standard library.

### Words

- **Our own words over borrowed text.** The wording rules take methods from controlled languages such as ASD-STE100, and from other writing guides, and rewrite them for this skill. Cost: a reader cannot check a rule against its source line by line. Holds as: the sources are named, in `references/wording.md` and in the decisions below, and no passage is copied from them.
- **Made-up examples over real projects.** Each example in the skill is invented for it, or taken from this repo. Cost: an example carries no proof that it worked somewhere. Holds as: no example in `skills/` names or quotes another project.

### Checks

- **Scripts check form, readers check meaning.** The scripts check links and blank lines, not facts. Cost: a wrong fact passes every script. Holds as: a revisit ends with a reader who did not write the change checking the claims and the goals ([SKILL.md](skills/what-we-build/SKILL.md) → Revisit, step 4).
- **Repair layout, never content.** Cost: `blank_lines.py` stops on a file it could almost fix. Holds as: after a run, `git diff` shows changes to blank lines only.

### Testing

- **Test by use first.** Real sessions come before prepared test prompts, and the prompts follow from what the sessions show ([ROADMAP.md](ROADMAP.md) → M3). Cost: evidence comes slowly, one session at a time. Holds as: each lesson in `SKILL.md` names the failure that taught it.
- **The repo is its own first example.** Its docs follow the skill. Cost: every rule change means checking this repo's docs again. Holds as: every core doc in this repo carries a what-we-build mark.

## Decisions

- Decided 2026-10-12: one skill with three modes over three skills, because the modes share the roles, the rules and the wording, and a user should not need to know which skill to call.
- Decided 2026-10-12: `disable-model-invocation: true` over automatic loading, because a session starts only when the user types the command (reason: FEATURES.md → Not planned).
- Decided 2026-10-12: the plugin manifest at the repo root over a plugin-only layout, because the repo then installs as a plugin and also works when its skill folder is linked into `~/.claude/skills`. Install steps are in [README.md](README.md).
- Decided 2026-10-12: our own skill over jig's `vision-elicitation` (ramboz/jig, MIT), because that skill runs a fixed 13-section questionnaire after jig's own scaffold and fills two templates, with no doc set, no push-back, no goals with numbers and no manual start. Its per-section fill marks gave the idea for the doc marks. The format here is our own.
- Decided 2026-10-13: one guide file per kind of doc, holding everything about that doc, over one shared reference and notes in `SKILL.md`, because a step works on one doc, reading all 17 guides cost about 700 lines each time, and `SKILL.md` then keeps only the flow.
- Decided 2026-10-13: three ideas from the writing guidance of mattpocock/skills (MIT) over the whole guide, because only these three matched a failure a session had shown: state the target instead of the ban, treat a doc that restates the code as a cache, and record only decisions that are hard to reverse, surprising and a real trade-off.

## Open questions

- How to evaluate the skill: which test prompts, and what a good session looks like in numbers. (ROADMAP.md → M3.)
