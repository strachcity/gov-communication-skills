---
name: communication-moments
description: "Draft model of the communication moments that case-based government services share, like 'we've received it', 'we need something from you' or 'we couldn't reach you'. Use it to plan which messages a service needs, and to draft a service-agnostic message for a moment that a service layer can then tailor. Draft, so use it for design and drafting work only, not to send live messages without review."
---

# Communication moments

A communication moment describes the relationship between the service and the customer at a point in a case. For example, "we are waiting for information from someone else".

A moment never describes a department's process, channel, form, system or implementation. "We are waiting for your GP to return a D4" belongs to one service. It's an example of a moment, not a moment.

This is a draft model. The moments are proposals, tested and revised as evidence is added. Each one records its evidence and status.

## Reference files

- `references/moments.md`: always. The moments, what each message must establish, and the evidence for each

## What this skill does

### Plan the messages for a case

Given a description of a service's case journey, map each point where the customer is likely to wonder what's happening to a moment. List:

- the moment
- the service's trigger for it, in the service's own words
- whether the customer needs to act
- any point that doesn't fit a moment. Say so, rather than forcing it into one

Some points need no message. If an internal step doesn't change anything for the customer, say no message is needed, and name the next moment they'll get.

### Draft a service-agnostic message for a moment

Use the message anatomy in `references/moments.md`. Fill every service-specific detail with a placeholder in square brackets, like [service name], [reference], [who was asked] or [timescale]. Never fill a placeholder with a guess.

Then:

1. Apply the `govuk-content` skill to the wording, if it's available.
2. Apply the `privacy-aware-communications` skill to what the message reveals, if it's available.
3. List the questions a service layer must answer before the message can be used, under "For the service to fill in".

### Apply a service layer

If you were given a service layer (see `services/README.md`), use its values for the placeholders. Only use values marked as confirmed. Leave the rest as placeholders, and list them.

Never move a service's detail into the generic moment. If a service needs something no moment covers, record it as a gap.

## Boundaries

- don't invent evidence. If a moment has no evidence from a service, say so
- don't treat a moment as settled because it seems plausible. Report its status
- don't decide legal effect, privacy or policy questions. List them for the service
