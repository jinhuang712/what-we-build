# Wording

The docs are read to decide and to build. Every rule below serves one of those two needs. The rules borrow methods from controlled languages for technical writing, such as ASD-STE100 Simplified Technical English, in our own words.

## Words

- One name per thing, and one thing per name. When two words compete, pick one and record it in `GLOSSARY.md` if the project has one.
- Use the names the project already uses. Do not invent labels the reader has never seen.
- When you must coin a name, make it short and clear.
- Spell out an abbreviation the first time, then use one form.
- Explain a term the first time a reader is likely to meet it.
- Use a verb for an action, not a noun phrase. "The app indexes the files", not "The app performs indexing of the files".
- Prefer a one-word verb to a phrasal verb.
- Keep noun clusters to three words. Break longer ones with prepositions.
- Write "for example" and "that is", not "e.g." and "i.e.".
- Never end a list with "etc." Name every item or give the count.
- No slang, buzzwords or words that only add emphasis (very, really, simply, just, robust, seamless).
- Use "must", "can" and "will". When something is uncertain, say what is uncertain once. Do not spread "might" and "should" through the text.

## Sentences

- Short sentences, one point each. About 20 words for a step, 25 for a description.
- Conditions first: "When the index is missing, the app rebuilds it."
- Active voice, so the reader knows who does what.
- At most one negation per sentence. No double negatives.
- Keep articles and "that". Do not drop words to save space.
- No semicolons. Write two sentences.
- When a pronoun could point to two things, repeat the noun. Follow "this" with a noun.
- Use connecting words to show how sentences relate: because, so, then, but.
- Write steps the reader must take as commands.
- Put required actions in the main text, not in parentheses or notes.

## Paragraphs and sections

- One topic per paragraph. Short paragraphs.
- Put the answer first. When a section is long, open it with a one-sentence summary.
- One idea per line in lists. A list item holds one point, not three sentences.
- Never nest lists. Split the topic or use a table.

## Format by the shape of the data

| Shape | Format |
|---|---|
| Records with two or more attributes | a table, one row per record |
| A few things compared on the same attributes | a table |
| Commands, config, code, output | a code block, copied exactly |
| Names, paths, keys, values in a sentence | backticks |
| Steps in order | a numbered list |
| Three or more parallel items with one attribute | a list |
| Reasoning | sentences |

Keep one blank line before and after every heading, list, table and code fence.

## Numbers

- A number beats an adjective. "Under 50 ms" beats "fast".
- Give units and the method: "≤ 50 ms per query, measured by the benchmark script on the full data set".
- Dates as `YYYY-MM-DD`. Versions exact.
- Never invent a number. When the number is not known, say so and leave the item open.

## History

- Keep a decision's history as one clause: what, why, when. `Decided 2026-10-12: SQLite FTS5, because it ships with the OS and indexes 1.4 GB in 13 s.`
- Remove logs of what was checked, mockup rounds, who asked, and stories of what failed. Git keeps them.
- A changed decision replaces the old one: `Lowered to macOS 14.5 on 2026-10-12 (was 26)`.

## Voice by doc

| Doc | Voice |
|---|---|
| PROPOSAL | a technical pitch: short, punchy, persuasive, with real numbers |
| PHILOSOPHY | reflective: plain words, a few lines that stay with the reader |
| GOALS | cold: a measure and a status |
| FEATURES | precise, present tense, from the user's side |
| DESIGNS | technical, decisions as dated clauses |
| ROADMAP | a status board |
| README | welcoming and direct |
