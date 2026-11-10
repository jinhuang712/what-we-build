# 022. Stories live in FEATURES and their flows in UIUX

Decided: 2026-11-03

## The problem

A user story says who does what and for what. It is the thread from a feature to the screens that carry it out, and the docs had no place for it. FEATURES spoke of one "you", so a feature used by two kinds of people could not say who does what. UIUX had only a short paragraph in the specs guide, so a feature had no flow to link to, and nothing led a reader into the pages in `prototype/`.

## The choice

Each feature in FEATURES lists its stories, one sentence each that says who does what and for what. Each story links down to its flow in `specs/UIUX.md`. UIUX draws every flow as an ASCII diagram of the screens it passes, since the interface is how a flow is carried out. Its *Screens* table links each screen to its page in `prototype/`, so UIUX is the prototype's navigation. UIUX gets its own guide again. A feature now reaches its pages through the flows of its stories.

## Not chosen

- The template "As a … I want … so that …": every story would read the same, and the reason would copy a want that PROPOSAL already holds.
- Stories at the top of each flow in UIUX: a project without an interface has stories too and no UIUX to hold them.
- A separate doc for stories: the stories and the features would become two lists that drift apart.
- An index page in `prototype/`: the pages would have two ways in, and one would fall behind.
- A tree of the screens: a tree sits in a code block, where its links cannot be followed.

## Consequences

The FEATURES guide gains stories, the specs guide points to the new UIUX guide and the link table in SKILL.md gains a row for UIUX. A reader can follow a want to a feature, a story, a flow and a page without a search.
