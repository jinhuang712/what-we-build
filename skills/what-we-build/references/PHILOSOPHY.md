# PHILOSOPHY.md

The philosophy says how the project sees its problem. It is a set of questions the project has to take a stance on, each answered in one line that people remember and quote, with the thinking behind it. The stances steer the whole project: the goals, the features, the design, the roadmap and what the README claims. A reader turns to it when a decision is close, and settles a real case with one answer.

It comes second in a session, after the proposal. The proposal says why the project should exist. The philosophy says how the project sees the problem, and DESIGNS, which comes next, builds on its stances. A fact belongs here when it is a stance that steers the whole project, not only how it is built.

**Owns:** the belief the project starts from, in a short preamble; the questions the project takes a stance on, each with its answer; a tie-break for when two answers collide; and *Reflections*, the deeper thinking and side insights from the conversation.

**Leaves out:** any feature the product has, any setting or screen part, and how the project is built. A stance that steers only how the project is built is a design principle, and it goes in DESIGNS.md. The full list of what will not be built, with the reasons, lives in FEATURES.md → *Not planned*.

**Push back on:** a stance no team would answer differently ("quality matters"), a stance that steers only the build, a stance that names a feature or a screen part, and questions and answers longer than one screen.

## Guidelines

- **Ask before you write.** The stances come from the user's answers to questions. A list of ready-made principles is the lazy path: each line looks right, and none of them steers anything. One session offered more than 30 candidate lines over 9 rounds before it asked the user what they believed. The user kept one, called the rest design rules, and the page took shape only once it was built on questions such as "What is reading?"
- **Ask about the domain, not the product.** "What is a budget?" or "Why do people stop tracking their money?" has an answer that steers everything. "Should the app send reminders?" has an answer that is a feature.
- **Answer each question with one quotable line, then the thinking behind it.** The line is what people quote in a review. The few sentences after it say why the stance is true, in the user's terms.
- **Test each answer two ways.** Opposite: a sensible team could answer the same question differently. Reach: the answer steers more than the build, such as a goal, a feature or a README claim. An answer that fails the opposite test is a premise, and it goes in the preamble. An answer that steers only the build goes in DESIGNS.md.
- **Add a refusal when it sharpens the stance:** "No red warnings for a missed day: the next entry picks up where the last one ended." A refusal shows what the stance costs.
- **Add a tie-break.** Say which answer wins when two collide. Without one, each side of an argument quotes the line it likes.
- **Keep the questions and answers to one screen,** so they get read before a decision instead of after it.
- **Keep the thinking in *Reflections*.** The conversation behind a philosophy wanders, and its side insights are worth keeping: a doubt, an analogy, a thought still forming. *Reflections* holds them below the answers, with no length limit, so the answers stay short.
- **Cite evidence only when the user knows the source, or you can verify it.** An invented citation destroys the trust the page exists to build.
- **Leave out how the product should feel.** That is the user's call. Record their words only when they bring them.

## Weak and strong

| Weak | Strong | What changed |
|---|---|---|
| "**Simplicity over power.**" written before any question was asked | "Why do people stop tracking their money? **They stop when it scolds them.** A late entry is normal, not a failure." | A stance from the user's answer, not from a list |
| "**Sync every hour.**" | Move it to DESIGNS.md. It steers only how the app is built. | A design rule is not a stance |
| "Users can export their data as CSV." | Move it to FEATURES.md. Keep the stance behind it here: "Whose data is it? **The user's, in a file they can open anywhere.**" | A feature is not a stance |
| "People are busy." | Move it to the preamble. Every team would agree, so it settles nothing. | A premise, not a stance |

## Explore

This doc usually needs the most discussion. Discuss it: ask, listen and test. Offer no stances before the user has answered.

1. What is true about the world that this project answers? This becomes the preamble.
2. Which questions must the project take a stance on? Propose a few, such as "What is <the core thing>?", "Why is <the problem> hard?", "How does <our user> differ from <the usual one>?", "What makes a <tool of this kind> good?" and "How much should it do?" Invite the user to add, cut and reword them. The user's own questions count most.
3. Ask one question at a time, and let the user answer in their own words. Reflect back what you heard, test the weak spots, and offer another angle. When the user asks for your answer, give it as an answer to that question, with its reason, not as a list of lines.
4. Turn each answer into one quotable line, and check the line with the user.
5. Test each line for opposite and reach.
6. When two answers collide, which one wins?
7. Which thoughts from the conversation are worth keeping in *Reflections*?

## Skeleton

```markdown
# Philosophy

<one to three sentences: what is true about the world, and what this project does about it>

## <a question the project takes a stance on>

**<the stance, one quotable line>.** <why it is true, in a few sentences>. <optional refusal>: <its alternative>.

## <next question>

...

When two answers collide, <which wins>, then <which>.

## Reflections

<the deeper thinking from the conversation: side insights, doubts, thoughts still forming>
```

## Style

A short preamble, then one section per question: the question as the heading, a bold stance as its first line, and a few sentences of reasoning. Then the tie-break, and *Reflections* last. The questions and answers fit on one screen. *Reflections* has no length limit. A stance gets quoted on its own, so each answer must make sense without the others.

## Done when

Each stance answers a question the user agreed on, comes from the user's answer, passes the opposite and reach tests, and names no feature the product has. The tie-break is there, and the questions and answers fit on one screen.
