# Wording

People read these docs to decide and to build. Every rule below serves one of those two needs: a reader finds the fact fast, and understands it the first time. The rules borrow methods from controlled languages for technical writing, such as ASD-STE100 Simplified Technical English, in our own words.

## Sections

Put the answer first. When a section is long, its first sentence says what the section concludes. A reader who stops after one sentence should still leave with the point.

Open a long doc so the reader sees all of it at a glance. The opening is either a TL;DR outline of its groups and items, or the few points the doc is built around, numbered, one sentence each. Then each group or point gets its own section, in the same order. A reader who knows the shape of a doc finds a fact in it without reading the rest. Which opening fits depends on the doc: an inventory such as FEATURES.md reads best as an outline, and a doc built on a few ideas, such as DESIGNS.md, reads best as its points. One session's user preferred "we are built around these points" to a TL;DR table for the design.

## Words

- Use one name per thing, and one thing per name. When two words compete, pick one and record it in `GLOSSARY.md` if the project has one.
- Use the names the project already uses, so the docs and the code speak one language.
- Describe the project in its own terms, not as a version of another project ("X for Y", "an X-like tool"). The comparison borrows the other project's meaning, including the parts you do not mean, and it ages with that project.
- When you must coin a name, make it short and clear.
- Spell out an abbreviation the first time, then use one form.
- Explain a term the first time a reader is likely to meet it.
- Use a verb for an action: "The app sends the invoices", not "The app performs the sending of the invoices".
- Prefer a one-word verb to a phrasal verb.
- Break a long noun cluster with prepositions, because the reader must untangle a stack of nouns to find the thing: "the export of reports for the tax year", not "the tax year report export".
- Write "for example" and "that is", not "e.g." and "i.e.".
- End a list with its last item, or give the count.
- Choose words that carry meaning. Words that only add emphasis (very, really, simply, robust, seamless) take the reader's attention and give nothing back.
- Use "must", "can" and "will". When something is uncertain, say once what is uncertain.

## Sentences

- Write short sentences, one point each. A reader takes in a short sentence at one pass, and reads a long one twice.
- Put conditions first: "When a payment fails, the app tries again after 3 days."
- Use the active voice, so the reader knows who does what.
- Avoid stacking negations. Each one makes the reader flip the meaning, and two flips are easy to get wrong: "Do every required step", not "Do not skip a step that is not optional".
- Keep articles and "that". Dropped words save space and cost understanding.
- Where a semicolon would join two sentences, write two sentences.
- When a pronoun could point to two things, repeat the noun. Follow "this" with a noun.
- Use connecting words to show how sentences relate: because, so, then, but.
- Write the steps a reader must take as commands.
- Put required actions in the main text. A reader skims past parentheses and notes.

## Lists and tables

- Keep one idea per list item and one idea per table cell.
- Keep lists one level deep. When items need sub-items, use a table or split the topic.
- Keep one blank line before and after every heading, list, table and code fence. Without it, a paragraph right after a list joins the last item, and one right after a table becomes a table row.

## Status marks

Use one set of marks across every doc, so a mark means the same thing wherever it appears.

| Mark | Means | Used in |
|---|---|---|
| ✅ | built, done, or met | FEATURES, ROADMAP, GOALS |
| 🚧 | built, with a gap named beside it | FEATURES |
| 🟨 | in progress | ROADMAP |
| ⬜ | planned, not started, or not yet measured | FEATURES, ROADMAP, GOALS |
| ❌ | measured and not met | GOALS |

## Numbers

- A number beats an adjective: "under 50 ms" beats "fast".
- Give units and the method: "≤ 50 ms per query, measured by the benchmark script on the full data set".
- Write dates as `YYYY-MM-DD`, and versions exactly.
- Every number that states a fact has a source: a measurement, a file or a person. When the number is not known, say so and leave the item open.
- A number inside an illustrative scene, told to "you", may be invented, because the scene asks the reader to imagine, not to believe. Keep it plausible, and keep it out of any sentence that states a fact.

## Style by doc

Each doc has its own form, so a reader knows what to expect before reading it. The form is in the *Style* section of the doc's guide, next to this file.
