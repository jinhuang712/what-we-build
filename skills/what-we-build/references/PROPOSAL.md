# PROPOSAL.md

The proposal is where the project begins: the case for why it should exist at all. It names the pain, the change in the world that lets the pain be eased now, and the idea that answers it. A reader finishes it knowing whether the project is worth building. Engineers, a future contributor, and the user six months from now all read it to remember why.

It comes first in a session, because every other doc builds on the pain it names. A fact belongs here when it explains why the project should exist at all.

**Owns:** the pain points, the shift, the one idea that makes the project different, what we want, a sample of it working, what we don't want, who it is for, the approach, the risks, how we will know it works.

**Leaves out:** exact behavior (FEATURES), the checks and their measured results (GOALS, though it may quote the headline checks), progress (ROADMAP), and the index of the project's own docs (README). When the project's idea is itself a set of documents, as for a docs tool, that set belongs in *The idea*.

**Push back on:** a case that opens with the solution, a pain point with no example, a want that serves no pain, a "don't want" with no reason, and a section of measured results.

## Why the case starts from the pain

A proposal persuades the way a doctor does: by naming what hurts before offering the cure. A reader who recognizes the pain wants to hear the answer. A reader handed the answer first has to take the problem on trust, and most will not. So the case has a spine, and every section hangs on it:

- **Pain points.** What hurts today, each with a moment or a number that proves it.
- **What we want.** What the reader needs instead, as needs, not one fix per pain.
- **What we don't want.** What the project refuses to become, each with its reason.

The idea is the one sentence that answers the pains. It is easy to find once the pains are clear, and easy to get wrong before. The shift, the sample, the approach and the risks all serve the spine. The shift comes right after the pains and says why they can be eased now: the reader has just recognized the pain, and now hears what changed. The sample shows a want coming true, and the risks say where the case is weak.

An agent with a good idea in mind is tempted to pitch it at once: the idea, its features, the evidence that it works. The pitch sounds strong, and it skips the part the reader needed most. In one session, the agent presented a polished case for the project, and the user stopped it: "what are the pain points? what do we really want? what do we not want?" The case only came together once it was built in that order.

## Talk the case through before writing it

The proposal is an argument, and an argument is tested by saying it out loud. Before any line goes into the file, make the case in the conversation: present it to the user as you would to someone deciding whether to fund it, starting from the pain. The user hears where it is weak, what it overstates, and what it leaves out. That is cheap to fix in a conversation, and expensive once a finished-looking draft exists.

In one session, the agent opened with an audit of the old proposal and a drafted *shift* table. The user set both aside: "before writing down anything, lets run the discussion again. you as the presenter, tell me, why?" The discussion that followed changed the pains, the wants and the order of the case.

## Here is a case taking shape

A made-up expenses app, as its proposal moves through a session.

**The pain, first try.** The user says: "Expenses are painful." True, and it persuades nobody, because it names no moment. The agent asks when it hurts most. "The end of every month. I sit for an evening matching receipts to card lines by hand." Now the pain has a moment, and anyone who has spent that evening recognizes it.

**More pains.** The agent and the user list them quickly, without judging: receipts get lost, the company's categories change every quarter, a trip abroad doubles the work. Then they pick the ones that hurt most, and find a real example for each. The others stay in the list as support, or drop out.

**The wants.** The agent asks what the user needs instead, and the answers come as needs, not as one fix per pain. "I want the month done for me, and to be asked only about what the app cannot place" eases the evening of matching, the lost receipts and the trip abroad at once. A want that serves no pain, such as "a dark theme", is a feature looking for a reason, and it waits for FEATURES.

**The don't-wants.** The user says the app must never become a form to fill in. The agent asks why. "A form gets answered, not thought about. I want to look at a month, not type into it." The reason goes with the refusal, so the next person who proposes a form hears it.

**The idea.** With the pains and wants on the table, the idea is what ties them together: "Your card already knows what you spent, so the app starts from the card, not from the receipt." It fits in one sentence. If it needed a paragraph, it would still be several ideas.

**Then the file.** Only now does the agent write, and the draft holds no surprises, because the user has heard every line of the argument already.

## Pains, wants and don't-wants are prose

A pain is a small story: a moment, what goes wrong, and what it costs. A table cell squeezes it to a label, and the label persuades nobody. The same holds for a want, which needs its "because", and for a refusal, which needs its reason. So the three lists are written as numbered or bulleted prose, one bold line each, then the sentences that make it real.

The wants describe needs. They do not answer the pains one by one. A need often eases several pains at once, and a list that pairs each want with one pain reads like a checklist, while the proposal is a pitch. The reader should still find every pain eased somewhere in the wants, and every want should serve a pain.

Tables still fit where the content is a comparison: the shift, as before and after, and the risks, each with what reduces it. In one session, the agent followed the old skeleton and wrote all three lists as tables. The user rejected them, and the prose version was the one approved.

## Numbers are examples, not results

A number in a pain point is evidence of the pain: "matching one month of receipts takes three hours". It makes the moment concrete, and it belongs here.

Measured results of the project itself do not. A table of how the first build scored against its rivals looks persuasive, but it answers "how far along are we?", which ROADMAP and GOALS own. Results change with each run, so a copy here goes stale, and the proposal starts to read like a status report. In one session, the agent added a section of benchmark results, and the user had it removed. The pain points that used the same test kept their numbers, written to stand alone. A copied result also goes stale where nobody looks: in another doc set, the proposal kept a binary size after the goals had withdrawn it as not reproducible.

## Say that it is the target

The proposal describes what the project will be. A reader who meets it after some code exists can take the target for the state of the code. So the line under the title says where the state lives: what is built is in FEATURES.md, and where the work stands is in ROADMAP.md. In one session, the user approved the docs and then asked whether the core of the design was already built.

## Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "Developers struggle with documentation." | "You ask your agent for a README and a roadmap. Ninety seconds later you have 2,000 confident words about decisions you never made." | A scene the reader has lived |
| A pitch that opens with the idea and its features | The case that opens with the pain, then the shift, then the idea and what we want and don't want | The pain before the cure |
| Pain: "Expenses are painful." | Pain: "Every month ends with an evening of matching receipts to card lines by hand." | A concrete moment |
| Wants as a table: "Matching \| Automatic" | "**The month is done for you.** The app matches each receipt to its card line, and asks only about the ones it cannot place." | A need with its because, in prose |
| Each want ending "This answers pain 2" | Wants written as needs, each easing whichever pains it eases | A pitch, not a checklist |
| Don't want: "Bloat." | Don't want: "A form to fill in. A form gets answered, not thought about." | A named thing, with its reason |
| A section of benchmark scores | The scores stay in GOALS. A pain keeps the one number that proves it | Evidence of the pain, not a status report |

## Explore

Build the case in the order of its spine, and talk it through before writing.

1. What hurts today? Brainstorm the pains together, as many as come. Then pick the ones that hurt most, and find a moment or a number for each.
2. Describe the moment the pain happens, as a scene the reader has lived. This becomes the hook.
3. What changed in the world that lets these pains be eased now?
4. What does the reader need instead? Write the needs, and check that each pain is eased by some need.
5. What must this project never become? Ask for the reason of each.
6. What is the one idea that answers the pains? Keep asking until it fits in a sentence.
7. Present the whole case to the user, starting from the pain, and let the user test it. Agree on it before writing.
8. Show it working: one concrete example of the product in use, such as a conversation, a command and its output, or a screen.
9. Who is it for? Who is the first user?
10. What is the approach, in one line per choice: platform, language, core model, what it builds on?
11. What could make it fail, and what reduces each risk?

## Skeleton

```markdown
# <Name> — Proposal

> <tagline>

Proposed <YYYY-MM-DD>. This is what the project will be: what is built is in FEATURES.md, and where the work stands is in ROADMAP.md.

## In short

<the hook: a scene the reader knows>

**<the one-line answer>**

## Pain points

1. **<the pain, one line>.** <the moment, or the number, that proves it>

<one sentence on what the pains lead to, when they share a root>

## The shift

| Before | Now |
|---|---|
| <how it was> | <what changed> |

## The idea

**<one sentence>.** <a few sentences on what it means>

## What we want

- **<what the reader needs>.** <how, in a sentence or two>

## How it works

<one concrete sample, a few lines; link FEATURES.md>

## What we don't want

- **<what the project refuses to become>.** <the reason>.

For the full list, see FEATURES.md → Not planned.

## Who it is for

## Approach

## Risks

| Risk | What reduces it |
|---|---|
| <risk> | <mitigation> |

## How we know it works

<the headline checks; link GOALS.md>
```

## Style

Short sections, each opening with its point. The pains, wants and don't-wants are prose with a bold line each. Tables are for comparisons: the shift and the risks. Numbers are real, and they prove a pain or name a check. The proposal argues, so every section should make the case stronger.

## Done when

The hook names a moment the reader has lived. The case runs from the pain, and the user heard it before it was written. The idea fits in one sentence. The sample shows the product instead of describing it. Every pain has an example and is eased by some want, every want serves a pain, and every "don't want" has a reason. No section reports measured results, and the line under the title says where the state of the work lives. A stranger could repeat the pitch after one reading.
