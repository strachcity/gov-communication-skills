---
name: case-communication-patterns
description: "Generic communication patterns for case-based government services, one for each moment in a case, like 'we've received it', 'we need something from you' or 'we couldn't reach you'. Use it to work out which messages a service needs, to recognise which pattern fits a situation, and to adapt a pattern using facts from the user's service context. Draft, so use it for design and drafting work only, not to send live messages without review."
---

# Case communication patterns

A communication moment describes the relationship between the service and the customer at a point in a case. For example, "we are waiting for information from someone else". A pattern is the generic message for that moment.

A moment never describes a department's process, channel, form, system or implementation. "We are waiting for a report from your employer" is an example of a moment in one service. It's not a moment.

This is a draft. The moments are proposals, tested and revised as evidence is added. Each one records its evidence and status.

## Reference files

- `references/moments.md`: always. The moments, the message anatomy, the modifiers and how to use the baseline copy
- `references/patterns/<pattern>.md`: when drafting or adapting a message for a moment that has a pattern. Read only the pattern you need. Every moment has a pattern, and so does the "Ask for feedback" follow-up

## The service context

This skill contains no service's rules. Service facts come from a service context the user gives you, in the conversation or in a file in their own project. It may hold the service's terminology, case states, timescales, channels, sender and contact details, and confirmed policy or disclosure decisions.

Use descriptive facts the user gives you, like the service name or contact details, as they are. Use decisions, like timescales, consequences, channel and disclosure decisions, only if they're marked confirmed. Treat anything else as a placeholder, and list it.

If there's no service context, work without one and use placeholders.

## What this skill does

### Plan the messages for a case

Given a description of a service's case journey, map each point where the customer is likely to wonder what's happening to a moment. List:

- the moment
- the service's trigger for it, in the service's own words
- whether the customer needs to act
- any point that doesn't fit a moment. Say so, rather than forcing it into one

Some points need no message. If an internal step doesn't change anything for the customer, say no message is needed, and name the next moment they'll get.

### Recognise the pattern

Work out which moment the request is about, from the customer's situation, not the service's event. Then pick:

- the variant, from the pattern file
- any modifier, like reminder, final reminder or delay
- any follow-up, like asking for feedback

If 2 moments seem to fit, check "Not this pattern" in each pattern file. If none fits, say so.

### Draft a generic message for a moment

If the moment has a pattern, start from its baseline copy for each channel. Otherwise use the message anatomy in `references/moments.md`. Keep the pattern's placeholders: [square brackets] for service facts and ((double brackets)) for values filled for each message. See "How to use the baseline copy" in `references/moments.md`. Never fill a placeholder with a guess.

Then:

1. Apply the `privacy-aware-communications` skill to what the message reveals, if it's available.
2. Apply the `govuk-content` skill to the wording, if it's available.
3. List the questions the service must answer before the message can be used, under "Needs a service decision".

### Adapt a pattern for a service

If you were given a service context, use its descriptive facts, and its confirmed decisions, for the placeholders. Leave the rest as placeholders, and list them.

Adapt the pattern, don't rewrite it. Keep its core information and its order. Change the wording only where the service's terminology or a confirmed decision needs it. If a service departs from the pattern, check its service context records the reason, and say so in your answer.

Work through the pattern's "Privacy and policy checkpoints". Each one is answered by a confirmed decision in the service context, or flagged.

Never move a service's detail into the generic pattern. If a service needs something no moment covers, say so in your answer. Don't create a new moment for it.

## Boundaries

- don't invent evidence. If a moment has no evidence, say so
- don't treat a moment as settled because it seems plausible. Report its status
- don't decide legal effect, privacy or policy questions. List them for the service
