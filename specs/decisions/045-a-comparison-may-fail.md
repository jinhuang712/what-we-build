# 045. A comparison may set a target and fail it

Decided: 2026-11-05

## The problem

The GOALS guide said a comparison shows where a project stands and has no pass or fail. Real projects use comparisons as gates. In a run on a diagram tool the user wanted to beat the rival and to improve wherever it lost, and this repo's own roadmap needs one comparison to reach 3 of 3.

## The choice

A comparison may set a target. It fails when the project misses that target, and a missed target is marked ❌.

## Not chosen

- Keep comparisons without a result: a project then hides a real gate under the wrong kind.
- Move such checks to thresholds: a threshold limits the product alone and has no rival.

## Consequences

A comparison with a target and one without now share a kind. A lost comparison can hold a checkpoint open.
