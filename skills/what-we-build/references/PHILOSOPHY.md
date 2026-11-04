# PHILOSOPHY.md

The philosophy is where the project thinks. It goes under the decisions to the beliefs they come from:

- What the problem is.
- Why it is hard.
- What the project holds to be true about it.

It is a set of questions about the world the project works in. Each has a stance in one line that people quote, and an argument under it.

It comes second, after the proposal. DESIGNS builds on its stances.

## What is it

Point anything a [NO] line rules out to its home, or push back when it has none.

- [YES]   the belief the project starts from.
- [YES]   the questions it takes a stance on with their arguments.
- [YES]   quotes from sources that shaped or tested them.
- [YES]   the sources when there are any.
- [YES]   argue in prose with a list or a table wherever it shows the thought better.
- [YES]   state each stance as one quotable line and then argue it.
- [NO]    a feature or a screen, which FEATURES holds.
- [NO]    how the project is built, which DESIGNS holds.
- [NO]    a stance with no argument.
- [NO]    a stance that sounds deep and says nothing.
- [NO]    a quote that decorates and does not test.
- [NO]    a quote nobody checked.
- [NO]    a stance the project does not truly hold, since an empty section is worse than a missing one.
- [NO]    a link to another doc in the project, since every other doc rests on this one.

## What you are after

The project's thought. It is neither a summary of the project nor a list of values. It is the lens the project looks through, and everything else is downstream of it:

- The designs are what it demands.
- The features are what it allows.
- *Not planned* is what it forbids.

A thought has three parts:

- **A premise:** what the project takes to be true.
- **A stance:** what it chooses because of that premise, where a reasonable person could choose otherwise.
- **A refusal:** what it will not do in principle, even when tempted.

You have it when four things hold:

- **Prediction:** given a case nobody foresaw, a reader can say what the project would do and why.
- **Opposition:** a reasonable team could have chosen the other way.
- **Recognition:** the user reads it and says "Yes, that is it" in their own words.
- **Derivation:** the design guidelines can be traced back to it.

It starts from whatever the user brings, in any form.

## Stance

- [YES]   a choice about what problem to solve where a reasonable team would choose otherwise, such as *the agent works in the developer's own terminal*.
- [NO]    a design that changes only how, such as *every tool call passes a permission check*.
- [NO]    a feature, such as *resume a session*.
- [NO]    a value every team would sign, such as *quality matters*.

## How to find it

- [YES]   listen for the thought that hides in an aside or a complaint.
- [YES]   say it back in one line and test it, since a wrong candidate is corrected faster than a right one is produced.
- [YES]   bring contrast from another field or thinker that holds the opposite.
- [YES]   push on what is thin by asking for the case, the cost and the exception.
- [NO]    a belief you invented, since the stances are the user's.
- [WHEN]  the four tests hold: stop without padding.

## Seeds

A pool of words and scenes to grow questions from. Pick what fits this user, and make the question yourself. Never ask them all.

what goes first · two good things collide · what is left behind · the clumsy way · someone copies it · taste · red line · the start · elegance · taken for granted · rather have nothing · believe · what they already know · someone asks for a feature · trade-off · the fear · sacrifice · a counterexample · two people argue · the heir reads this · the day you quit · everyone assumes · collapse · where they are right · even if it pays · what failure looks like · underrated · who pays · growing bigger · why now · who is responsible · day one hundred · the popular way · not for whom · rough but right · the end · responsibility · slow · left unfinished · freedom or constraint · bottom line · polish · cannot have both · who the user is · cost · never · trust · actually not · the exit condition · good enough · another road · what they refuse to do · for whom · what should not exist · fast · peers · the rival's way · power · a newcomer joins · flavor · the criticized way · going astray · against whom · where we fall short · the boss says add one more · can but won't · what stays · why others do it · adding a feature · the old way · more · why not before · what changes · looking back at this decision · simple or powerful · temptation · an incident at midnight · less · who would be let down · a year later · the clever way · who yields · counterintuitive · quiet decay · an incident · overrated · a changing world · fast or right · who decides · never said aloud · a case nobody foresaw · if it were the opposite · refuse · day one · the field's common sense · ten years from now · ugly · the regret · veto · predecessors

## Skeleton

```markdown
# Philosophy

<the belief the project starts from>

## <a question the project takes a stance on>

**<the stance, one quotable line>.**

<the argument>

## Sources

- <author>. *<title>*. <year>.
```
