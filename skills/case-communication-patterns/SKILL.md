---
name: case-communication-patterns
description: "Generic communication patterns for case-based government services, one for each moment in a case, like 'we've received it', 'we need something from you' or 'we couldn't reach you'. Use it to work out which messages a service needs, to recognise which pattern fits a situation, and to adapt a pattern using facts from the user's service context. Draft, so use it for design and drafting work only, not to send live messages without review."
---

# Case communication patterns

A communication moment describes the relationship between the service and the customer at a point in a case. For example, "we are waiting for information from someone else". A pattern is the generic message for that moment.

A moment never describes a department's process, channel, form, system or implementation. "We are waiting for a report from your employer" is an example of a moment in one service. It's not a moment.

This is a draft. The moments are proposals, tested and revised as evidence is added. Each one records its evidence and status.

## Reference files

- `references/moments.md`: always. The moments, what each message must establish, and the evidence for each

## The service context

This skill contains no service's rules. Service facts come from a service context the user gives you, in the conversation or in a file in their own project. It may hold the service's terminology, case states, timescales, channels, sender and contact details, and confirmed policy or disclosure decisions.

Only use a fact marked as confirmed. Treat anything else as a placeholder, and list it.

If there's no service context, work without one and use placeholders.

## What this skill does

### Plan the messages for a case

Given a description of a service's case journey, map each point where the customer is likely to wonder what's happening to a moment. List:

- the moment
- the service's trigger for it, in the service's own words
- whether the customer needs to act
- any point that doesn't fit a moment. Say so, rather than forcing it into one

Some points need no message. If an internal step doesn't change anything for the customer, say no message is needed, and name the next moment they'll get.

### Draft a generic message for a moment

Use the message anatomy in `references/moments.md`. Fill every service-specific detail with a placeholder in square brackets, like [service name], [reference], [who was asked] or [timescale]. Never fill a placeholder with a guess.

Then:

1. Apply the `privacy-aware-communications` skill to what the message reveals, if it's available.
2. Apply the `govuk-content` skill to the wording, if it's available.
3. List the questions the service must answer before the message can be used, under "For the service to fill in".

### Adapt a pattern for a service

If you were given a service context, use its confirmed facts for the placeholders. Leave the rest as placeholders, and list them.

Never move a service's detail into the generic pattern. If a service needs something no moment covers, say so in your answer. Don't create a new moment for it.

## Boundaries

- don't invent evidence. If a moment has no evidence, say so
- don't treat a moment as settled because it seems plausible. Report its status
- don't decide legal effect, privacy or policy questions. List them for the service
