# 025. A feature status says built, and GOALS says whether it works

Decided: 2026-11-03

## The problem

FEATURES used two meanings for its marks. Starting from running code and keeping the context while you work were never run on a new project and were marked ✅. Resume and the wiki hint were marked 🚧 for the same reason. For a skill, a feature is built once the skill says it, and it works only once an agent follows it on a real project. ROADMAP and GOALS already track that second part, through CP3: First real use and goals such as O2: Context survives compaction.

## The choice

A ✅ in FEATURES means the feature is built. Whether it works in real use is checked by the goals and shown in ROADMAP. A 🚧 is kept for a gap in what is built, named beside the mark. A failed goal sends the feature it covers back to 🚧 with that gap named.

## Not chosen

- 🚧 on every feature not yet run on a new project: almost every feature would carry it, and FEATURES would copy the progress that ROADMAP holds.
- Leaving the two meanings mixed: a reader could not tell from a mark what had been proven.

## Consequences

F1.7: Resume and F2.2: A wiki when others build on it move to ✅. The FEATURES guide says what each mark means.
