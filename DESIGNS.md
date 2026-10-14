<!-- what-we-build: drafted 2026-10-14 -->

# Designs

How what-we-build is built, and why. What goes in is a project folder and a conversation with the user. What comes out is a set of Markdown docs, each with a mark that says drafted or approved. In between is the skill: Markdown instructions that an agent reads. What the skill does for the user is in [FEATURES.md](FEATURES.md).

## Principles

Each principle names the choice, what it costs, and how to check that it holds.

### Context

- **Short core, detail on demand.** `SKILL.md` holds what every session needs. The doc guides and the wording rules wait in reference files until a step points to them. Cost: a step must name its reference, or the agent never reads it. Holds as: `SKILL.md` stays within the limit in GOALS.md G6, and each step that needs a reference names its path.

### State

- **The docs are the state.** A mark on each doc's first line over a separate state file. Cost: points agreed for a doc that is not drafted yet are lost when the sitting ends. Holds as: no file but the docs records where a session stopped.

### Portability

- **No dependencies.** The skill is Markdown only. Cost: nothing checks the docs by machine. Holds as: `skills/what-we-build/` holds only Markdown files.

### Words

- **Our own words over borrowed text.** The wording rules take methods from controlled languages such as ASD-STE100, and from other writing guides, and rewrite them for this skill. Cost: a reader cannot check a rule against its source line by line. Holds as: the sources are named, in `references/wording.md` and in the decisions below, and no passage is copied from them.
- **Made-up examples over real projects.** Each example in the skill is invented for it, or taken from this repo. Cost: an example carries no proof that it worked somewhere. Holds as: no example in `skills/` names or quotes another project.

### Checks

- **Readers check the docs, not scripts.** Cost: a broken link, a missing blank line or a wrong fact stays until a reader catches it. Holds as: every goal measured on this repo is measured by a reader who did not write the change ([GOALS.md](GOALS.md)).

### Testing

- **Test by use first.** Real sessions come before prepared test prompts, and the prompts follow from what the sessions show ([ROADMAP.md](ROADMAP.md) → M3). Cost: evidence comes slowly, one session at a time. Holds as: each rule in `SKILL.md` that a session taught names the failure that taught it.
- **The repo is its own first example.** Its docs follow the skill. Cost: every rule change means checking this repo's docs again. Holds as: every core doc in this repo carries a what-we-build mark.

## Decision: one skill with its modes over a skill per mode — 2026-10-12

The modes share the roles, the rules and the wording, and a user should not need to know which skill to call.

## Decision: manual start over automatic loading — 2026-10-12

The skill sets `disable-model-invocation: true`, because a session starts only when the user types the command (reason: FEATURES.md → Not planned).

## Decision: the plugin manifest at the repo root over a plugin-only layout — 2026-10-12

The repo then installs as a plugin, and also works when its skill folder is linked into `~/.claude/skills`. Install steps are in [README.md](README.md).

## Decision: our own skill over jig's `vision-elicitation` — 2026-10-12

jig's `vision-elicitation` (ramboz/jig, MIT) runs a fixed 13-section questionnaire after jig's own scaffold and fills two templates. It has no doc set, no push-back, no goals with numbers and no manual start. Its per-section fill marks gave the idea for the doc marks. The format here is our own.

## Decision: one guide file per kind of doc over one shared reference — 2026-10-13

Each guide holds everything about its doc, over one shared reference and notes in `SKILL.md`. A step works on one doc, and reading all 17 guides cost about 700 lines each time. `SKILL.md` then keeps only the flow.

## Decision: three ideas from mattpocock/skills over the whole guide — 2026-10-13

Only three ideas in the writing guidance of mattpocock/skills (MIT) matched a failure a session had shown:

- State the target instead of the ban.
- Treat a doc that restates the code as a cache.
- Record only decisions that are hard to reverse, surprising and a real trade-off.

## Decision: DESIGNS third, before GOALS and FEATURES — 2026-10-14

The design comes right after the philosophy, because the design guides the features. In a real session on 2026-10-14, the platform and the language were settled long before any feature was listed, and the user moved DESIGNS ahead of GOALS.

| Option | For | Against |
|---|---|---|
| **DESIGNS third** | The philosophy's stances turn into how the project is built while they are fresh, and the features are then written within that design. | A number the design needs stays open until GOALS sets it. |
| DESIGNS fifth, after FEATURES | Every feature and every number is known before the design starts. | The features are written without the design that shapes them. |

## Open questions

- How to evaluate the skill: which test prompts, and what a good session looks like in numbers. (ROADMAP.md → M3.)
