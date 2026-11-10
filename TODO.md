# TODO

## ongoing

### [P1][ISSUE] A compacted window goes on without the reread

- description: 4 of 6 compactions on an editor had no full read of a core doc in the next 40 tool calls, while `AGENTS.md` says to read every doc in the read order
- created: 2026-11-11
- found: runs on an editor and a diagram tool from 2026-11-07 to 2026-11-10, where the diagram tool reread only after the user insisted
- next: run [O2: Context survives compaction](GOALS.md#o2-context-survives-compaction) on a new project
- related: a hook could force the reread, and the skill stays Markdown only
