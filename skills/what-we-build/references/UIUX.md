# UIUX.md

UIUX.md describes how the product looks and moves: where each kind of information lives on screen, how urgent each state looks, and which colors and motions carry meaning. A designer or developer reads it before touching the interface, to keep the screens consistent.

**Owns:** layout, states and how urgent each one looks, color, type, motion, keyboard, accessibility. Rules, not measurements: name the code type that holds the numbers.

**Leaves out:** behavior (FEATURES), implementation (DESIGNS).

**Add when** the project has a visual interface. Draft it right after FEATURES.md, because it shapes how the features look. A fact belongs here when it is about how the product looks or moves.

## Guidelines

- **Write each rule with its reason,** because a rule without one gets broken the first time it is inconvenient.
- **Rank the states by urgency,** and say which ones may interrupt the user, so a minor state never looks like an error.
- **Name the type that holds the numbers** (sizes, durations, colors) instead of copying them.

| Weak | Strong |
|---|---|
| "Cards are 72 px tall with 12 px padding." | "Card sizes live in `TaskCardLayout`. A card with an overdue task grows one line." |

## Explore

Where does each kind of information live on screen? Which states may interrupt the user? Which colors carry meaning? What moves, and what never moves?
