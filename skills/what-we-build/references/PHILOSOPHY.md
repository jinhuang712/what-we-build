# PHILOSOPHY.md

The philosophy is where the project thinks. Every other doc records what was decided. This one goes under the decisions, to the beliefs they come from: what the problem is, why it is hard, and what the project holds to be true about it. It is a set of questions about the world the project works in. Each is answered with a stance in one line that people quote, and under the line is the argument that makes it true.

It comes second in a session, after the proposal. The proposal says why the project should exist. The philosophy says how the project sees the problem, and DESIGNS, which comes next, builds on its stances. A fact belongs here when it is a stance that steers the whole project, not only how it is built.

**Owns:** the belief the project starts from, in a preamble; the questions the project takes a stance on, each with its answer and the argument behind it; quotes from the books, papers and people that shaped or tested the answers; a tie-break for when two answers collide; *Reflections*, the thinking still in motion; and the sources.

**Leaves out:** any feature the product has, any setting or screen part, and how the project is built. A stance that steers only how the project is built is a design principle, and it goes in DESIGNS.md. The full list of what will not be built, with the reasons, lives in FEATURES.md → *Not planned*.

**Push back on:** a stance with no argument under it; a quote that decorates a stance and does not test it; a stance no team would answer differently ("quality matters"); a stance that steers only the build; a stance that names a feature or a screen part; and a quote nobody checked.

## Why a philosophy needs depth

A stance is used in cases nobody foresaw. Months later, someone proposes a feature, and a reader opens the philosophy to see whether it fits. A slogan cannot answer, because a slogan says what the project believes and not why. Two people read "keep it simple" and reach opposite verdicts. The argument under a stance is what carries it into a new case: the reader follows the reasoning, and sees where the new case lands.

So the depth is not ornament. A deep stance has three parts:

- **The reason.** Why the stance is true, traced down to something about the world, about people or about the problem. A reason that stops at "users like it" has not reached the bottom yet, and the next section shows how to get there.
- **The cost.** What the project gives up by holding it. A stance that costs nothing is a premise that every team shares, and it settles nothing.
- **The other side.** What a thoughtful person who disagrees would say, and the project's answer to it. A stance that has met its strongest objection is one a reader can trust.

Depth also lets the other docs stay short. DESIGNS, GOALS and FEATURES record decisions in a line or a row, because the thinking behind them already lives here.

## Ask why, and keep asking

The main tool of this doc is one word: why. A well-known saying holds that if you ask why five times, you reach the truth of almost anything. Toyota's factories made it a method: when something goes wrong, ask why it happened, then ask why about that answer, and keep going. The first answer names a symptom. An answer a few levels down names a cause, something true that the rest follows from.

A philosophy works the same way. The user's first answer to a question is usually true and shallow, because it is the answer anyone would give. Each why moves it one level down: from what happens, to why it happens, to what about people or the world makes it happen. A stance written at the first level reads like every other team's. A stance written at the bottom is the project's own.

The five in the saying is a way of speaking, not a count. Some answers reach the bottom sooner, and some need more rounds. Stop when the answer reaches something about people or the world that no longer depends on the product, and another why would only repeat it. Ask the whys in the flow of the conversation, and reflect back what you heard before the next one, so that it feels like thinking together, not like an interrogation. The user's answer is the next step down, not yours.

## How a stance gets deeper

Depth is found in conversation, not added at the end. Here is one stance, for a made-up budget app, as it moves through a session.

**The question.** "Why do people stop tracking their money?"

**The first answer.** The user says: "They forget, and then catching up is too much work." Written down as is, the line would be "Make tracking easy". Every budget app would sign it, so it fails the opposite test. The answer is a start, not a stance.

**Why is catching up too much work,** when a week of spending takes ten minutes to enter? "When I open the app after a week, it shows everything I missed in red. I feel bad, and I close it." People do not stop because tracking is hard. They stop because coming back hurts.

**Why does the red make you close it?** "It feels like a report card, and I failed it."

**Why does failing end it,** when a bad grade makes some people try harder? "Because it is about money. I already feel judged about money, and the app adds one more judgment."

**Why does money feel like a judgment?** "Because how you handle money feels like a verdict on who you are." This answer no longer depends on the app. It is about people, and one more why would only say it again. The draft line becomes "They stop when it scolds them", and its reason is now at the bottom: money already feels like a verdict, so the app must never add one.

**A source that agrees.** The agent looks for others who thought about the same question. The question is about habits and lapses, not about budget apps, so the search goes to research on habits. Suppose a study finds that one missed day barely slows a habit, while the feeling of having broken a streak often ends it. That gives the stance a reason below the user's own experience: the damage comes from the feeling, not from the gap. The agent brings back the study's own words, and the user reads them.

**A source that disagrees.** The agent then looks for the other side, because a stance is only as strong as its answer to its best objection. Suppose a writer on personal finance argues that a visible record of failure keeps people honest, and that hiding it is flattery. The objection is serious. The user's answer is that the record stays, but the color of failure goes: a missed day shows as missing, not as wrong. The stance is now sharper than before, and it states its cost: the app gives up the push that shame gives some people.

**The stance.** The page records:

> **Why do people stop tracking their money? They stop when it scolds them.**
>
> A missed week is normal. What ends the habit is the moment of coming back and being shown a wall of red, because how people handle money already feels like a verdict on who they are. So the app keeps an honest record and never paints it as failure: a gap is a gap. Some people are pushed by shame, and this app gives that up on purpose. No red warnings for a missed day: the next entry picks up where the last one ended.

Under it go the two quotes, the one that agrees and the one that disagrees. The user's doubt, whether some people do want the streak, goes into *Reflections*, because it is still open.

Look at what happened. Each why came from the agent, and each answer from the user. The line took shape early, and its reason only at the bottom. The sources did not supply the stance. They tested it, gave it a deeper reason, and forced it to state its cost.

## What sources do

Most questions a project asks have been asked before, in another field. "What is a diagram?", "Why do people settle?" and "What makes a tool easy to learn?" have each been studied by philosophers, psychologists, designers and economists. Their work is a second conversation partner, one that thought about the question for years.

A source can do three things for a stance:

- **Give it a deeper reason.** The user's experience says what happens. A study or a classic often says why.
- **Name its cost.** A thinker who disagrees shows what the stance gives up, and that is often the more useful source.
- **Turn it.** Sometimes a source changes the answer. A complaint about tiring work can become a stance about cost once a classic on why people settle for "good enough" enters the conversation. The user decides whether the stance turns.

A source cannot do the user's thinking. A stance borrowed from a book, with no answer from the user under it, is a ready-made principle with a citation, and it steers no more than one without.

The search follows the question, not the product. A budget app's question about lapses leads to habit research, not to other budget apps. Look for the classics of the field the question belongs to, and look for both sides.

**Why quote the original words.** A paraphrase is the agent's reading of the source. The original lets the reader weigh the thinker directly, and often holds a phrase better than any summary. So the page quotes, under the stance each quote supports, as a blockquote with "— author, *title*, year" below it. A quote in another language keeps the original, with a translation under it. The user's own words count as a source too, quoted with the date, when they say it best.

**Why whole sentences.** A quote cut to a few words loses the thinking that made it worth quoting, and the reader cannot tell what the thinker meant. One session cut its quotes to fragments, and the user called the page "way too brief". Keep whole sentences, and cut with `…` only the clauses that carry nothing.

**Why every quote is checked.** The page exists so that a reader trusts its reasoning, and one invented quote breaks that trust for the whole page. A quote is checked against the work itself, or against more than one copy when the work is out of reach. *Sources* says how each was checked. A quote that could not be checked is left out.

## Style

The page is long where the thinking is long, and it still reads fast, because each part has one job.

- **The preamble** states the belief the project starts from: a premise most people would accept, and what the project does about it.
- **The bold lines** are the short form. A reader in a hurry reads only them and knows every stance. Each one must make sense alone, because it gets quoted alone.
- **The argument under each line** is for the reader who must apply the stance to a new case. It holds the reason, the cost, the answer to the other side, a refusal when one sharpens the stance, and the quotes.
- **The tie-break** says which answer wins when two collide. Without it, each side of an argument quotes the line it likes.
- ***Reflections*** holds what is not settled: a doubt, a tension between two sources, an analogy, a stance that may need another look, and how the stances changed and why. A philosophy that records its open questions is more honest than one that looks finished.
- ***Sources*** lists each work, with one line on how the quotes were checked.

Deep thinking still uses plain words. Depth comes from the ideas, and the wording rules hold here as everywhere.

How the product should feel is the user's call. Record the user's words about it only when the user brings them.

## Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "**Simplicity over power.**" written before any question was asked | "Why do people stop tracking their money? **They stop when it scolds them.**" | A stance from the user's answer, not from a list |
| "**They stop when it scolds them.** A late entry is normal." and nothing more | The same line, then the reason, the cost and the answer to the other side | A stance that is argued, not only stated |
| A quote that says the stance again in grander words | A quote from a source that disagrees, and the page's answer to it | A source that tests the stance |
| A quote cut to four words | The whole sentence, with `…` where a clause carried nothing | A quote a reader can weigh |
| "**Sync every hour.**" | Move it to DESIGNS.md. It steers only how the app is built. | A design rule is not a stance |
| "Users can export their data as CSV." | Move it to FEATURES.md. Keep the stance behind it here: "Whose data is it? **The user's, in a file they can open anywhere.**" | A feature is not a stance |
| "People are busy." | Move it to the preamble. Every team would agree, so it settles nothing. | A premise, not a stance |

## Explore

This doc needs the most discussion, and the stances come from the user. A list of ready-made principles is the lazy path: each line looks right, and none of them steers anything. One session offered more than 30 candidate lines over 9 rounds before it asked the user what they believed. The user kept one, called the rest design rules, and the page took shape only once it was built on questions such as "What is reading?"

1. What is true about the world that this project answers? This becomes the preamble.
2. Which questions must the project take a stance on? Ask about the world, not the product: "What is a budget?" has an answer that steers everything, and "Should the app send reminders?" has an answer that is a feature. Propose a few, such as "What is <the core thing>?", "Why is <the problem> hard?", "How does <our user> differ from <the usual one>?" and "What makes a <tool of this kind> good?" The user's own questions count most.
3. Take one question at a time. Let the user answer in their own words, reflect back what you heard, and keep asking why until the answer reaches something about the world (see [Ask why, and keep asking](#ask-why-and-keep-asking)).
4. Bring in the sources, on both sides, as in [How a stance gets deeper](#how-a-stance-gets-deeper). Show the user their words, and ask whether the stance changes.
5. Find the one quotable line, and check it with the user.
6. Test the line two ways. Opposite: a sensible team could answer the same question differently. A line that fails is a premise, and it goes in the preamble. Reach: the line steers more than the build, such as a goal, a feature or a README claim. A line that steers only the build goes in DESIGNS.md.
7. When two answers collide, which one wins?
8. What is still open, or still forming? It goes in *Reflections*.

## Skeleton

```markdown
# Philosophy

<the belief the project starts from: what is true about the world, and what this project does about it>

> <a quote that grounds the belief>
>
> — <author>, *<title>*, <year>

## <a question the project takes a stance on>

**<the stance, one quotable line>.**

<the argument: the reason, the cost, and the answer to the other side>. <optional refusal>: <its alternative>.

> <a quote that supports or tests the stance>
>
> — <author>, *<title>*, <year>

## <next question>

...

When two answers collide, <which wins>, then <which>.

## Reflections

<the thinking still in motion: doubts, tensions between sources, analogies, and how the stances changed and why>

## Sources

<one line on how the quotes were checked>

- <author>. *<title>*. <year>.
```

## Done when

Each stance answers a question the user agreed on, comes from the user's answer, passes the opposite and reach tests, and names no feature the product has. Each stance carries its reason, its cost and its answer to the other side, and has been tested against sources the user has seen. Every quote is checked and listed in *Sources*. The tie-break is there.
