# 035. A feature of this skill is ✅ once the skill covers it

Decided: 2026-11-04

## The problem

The FEATURES guide now marks a feature ✅ only once it is built and has been run. A program's feature can be run on the spot. A feature of this skill is a way an agent behaves, and whether an agent really behaves that way shows only when it runs on a real project. So this repo's FEATURES could not tell which of its marks the new rule allows.

## The choice

In this repo a feature is ✅ once `SKILL.md` or a guide holds the rule that asks for it. The mark says which ground the skill tries to cover and not that an agent always follows it. Whether it works is left to the goals and shown in ROADMAP, as before. A ✅ still needs its proof: the line in the skill that asks for the feature.

## Not chosen

- A ✅ only once a real session shows an agent doing it: the sessions read so far cover too few features to say which ones an agent follows.
- A ✅ only once a new project proves it: that is what ROADMAP measures, and FEATURES would copy its progress.

## Consequences

The project's rule differs from the guide here, and the user chose it. A feature whose text claims more than the skill asks for is cut back to what the skill says.
