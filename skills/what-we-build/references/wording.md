# Wording

People read these docs to decide and to build. Every rule below serves one of those two needs: a reader finds the fact fast, and understands it the first time. The rules borrow methods from controlled languages for technical writing, such as ASD-STE100 Simplified Technical English, in our own words.

Write in your default voice. The rules shape clarity and form, not tone.

## Sections

Every section has up to three layers, in this order:

| Layer | Gives the reader |
|---|---|
| Description | what this part is and why it matters, in a short paragraph |
| Guidelines | how to do it well, each with its reason |
| Specifics | tables, skeletons, commands, examples |

Put the answer first. When a section is long, its first sentence says what the section concludes. A reader who stops after one sentence should still leave with the point.

## Words

- Use one name per thing, and one thing per name. When two words compete, pick one and record it in `GLOSSARY.md` if the project has one.
- Use the names the project already uses, so the docs and the code speak one language.
- When you must coin a name, make it short and clear.
- Spell out an abbreviation the first time, then use one form.
- Explain a term the first time a reader is likely to meet it.
- Use a verb for an action: "The app indexes the files", not "The app performs indexing of the files".
- Prefer a one-word verb to a phrasal verb.
- Keep noun clusters to three words. Break longer ones with prepositions.
- Write "for example" and "that is", not "e.g." and "i.e.".
- End a list with its last item, or give the count.
- Choose words that carry meaning. Words that only add emphasis (very, really, simply, robust, seamless) take the reader's attention and give nothing back.
- Use "must", "can" and "will". When something is uncertain, say once what is uncertain.

## Sentences

- Write short sentences, one point each: about 20 words for a step, 25 for a description.
- Put conditions first: "When the index is missing, the app rebuilds it."
- Use the active voice, so the reader knows who does what.
- Use at most one negation per sentence.
- Keep articles and "that". Dropped words save space and cost understanding.
- Where a semicolon would join two sentences, write two sentences.
- When a pronoun could point to two things, repeat the noun. Follow "this" with a noun.
- Use connecting words to show how sentences relate: because, so, then, but.
- Write the steps a reader must take as commands.
- Put required actions in the main text. A reader skims past parentheses and notes.

## Lists and tables

- Pick the format by the shape of the data, in every doc, even when the same records appear in another doc.
- Keep one idea per list item and one idea per table cell.
- Keep lists one level deep. When items need sub-items, use a table or split the topic.
- Keep one blank line before and after every heading, list, table and code fence.

| Shape | Format |
|---|---|
| Records with two or more attributes | a table, one row per record |
| A few things compared on the same attributes | a table |
| Commands, config, code, output | a code block, copied exactly |
| Names, paths, keys, values in a sentence | backticks |
| Steps in order | a numbered list |
| Three or more parallel items with one attribute | a list |
| Reasoning | sentences |

## Numbers

- A number beats an adjective: "under 50 ms" beats "fast".
- Give units and the method: "≤ 50 ms per query, measured by the benchmark script on the full data set".
- Write dates as `YYYY-MM-DD`, and versions exactly.
- Every number has a source: a measurement, a file or a person. When the number is not known, say so and leave the item open.

## History

- Keep a decision's history as one clause: what, why, when. `Decided 2026-10-12: SQLite FTS5, because it ships with the OS.`
- A changed decision replaces the old one, with one clause of history: `Lowered to macOS 14.5 on 2026-10-12 (was 26).`
- The story of how a decision was reached (what was checked, which mockup won, who asked) lives in git.

## Style by doc

Each doc has its own form, so a reader knows what to expect before reading it.

| Doc | Style |
|---|---|
| PROPOSAL | short sections that open with a scene, tables for comparisons, real numbers |
| PHILOSOPHY | short prose, one section per principle, then the test |
| GOALS | a short intro and one table of checks: measure, method, status |
| FEATURES | one section per feature, a short description, then behavior in the present tense |
| DESIGNS | sections per area, each opening with what it covers, decisions as dated clauses |
| ROADMAP | one overview table, then one status table per milestone |
| README | a short description, a few bullets, install, first use, limits, links |
