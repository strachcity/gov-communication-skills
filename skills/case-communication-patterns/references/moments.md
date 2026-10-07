# Moments

Draft, last revised 6 October 2026. Every moment here is a proposal.

Every moment has a pattern, in `patterns/`:

1. We've received it: `patterns/we-have-received-it.md`
2. Your case has moved on: `patterns/your-case-has-moved-on.md`
3. We're waiting on someone else: `patterns/we-are-waiting-on-someone-else.md`
4. We'll contact you: `patterns/we-will-contact-you.md`
5. We need something from you: `patterns/we-need-something-from-you.md`
6. We couldn't reach you: `patterns/we-could-not-reach-you.md`
7. We've made a decision: `patterns/we-have-made-a-decision.md`
8. What you applied for is on its way: `patterns/what-you-applied-for-is-on-its-way.md`
9. You need to act before a date: `patterns/you-need-to-act-before-a-date.md`

There's one follow-up, "Ask for feedback": `patterns/ask-for-feedback.md`.

## How to read this file

### Evidence status

Each moment has one status:

- **proposed:** suggested, with no evidence recorded yet
- **seen in 1 service**
- **seen in 2 or more services**
- **supported by a main source:** a GOV.UK main source describes the need, as well as at least one service showing it
- **tested with users**

A moment's status only changes when new evidence is added to its pattern file.

Lines starting with ">" are quotes. Lines starting with "Interpretation:" are ours.

## Message anatomy

Every message for a moment contains these parts, in this order. Leave out any part that doesn't apply.

1. What has happened, as a headline or first line.
2. Who it's for: a greeting with the customer's full name, for emails and letters.
3. The reference.
4. What happens next, and when.
5. What the customer needs to do and by when, or that they don't need to do anything.
6. What happens if they don't act, if they need to.
7. How to check progress or get help.
8. Who it's from.

Parts 4 to 6 come from the Service Manual, which says to:

> make it clear what you need the user to do and include any deadlines

> say what will happen if they don't do what you're asking

> explain what you'll do next and when they'll hear from you - if you won't be contacting them again, make it clear that it's the end of the process

## How to use the baseline copy

Each pattern has baseline copy for each channel. It uses 2 kinds of placeholder:

- **[square brackets]:** a service fact, filled once from the service context, like [sender] or [tracking URL]. Descriptive facts the user gives you can be used as they are. Decisions, like timescales and consequences, need to be confirmed. See "2 kinds of fact" in the `government-communication` skill's `references/service-context.md`
- **((double brackets)):** a value filled for each message when it's sent, like ((reference)) or ((deadline)). GOV.UK Notify uses this format for personalisation. These are not gaps in the service context

### Optional copy

Optional copy is always a whole block, never part of a sentence:

- a placeholder inside a sentence must always have a value. If a part of a sentence might not apply, rewrite it as a separate block
- an optional block starts with a line like `[If there's a cost:]` and ends with `[End if]`. Everything between is complete sentences or a heading and its content
- where a sentence has alternatives, like "an email" or "a letter", it uses one placeholder, like [what we sent], which always gets a value
- the only exception is the "[Service name]: " prefix on texts, which is kept or removed whole

When drafting for a service, resolve every block. Keep it and remove the marker lines if the condition applies. Remove the whole block if it doesn't. If it's unknown, leave the block out of the draft and list it for the service. A draft should never contain `[If ...:]` or `[End if]`.

A service fact can be a rule, like "20 working days after we receive a complete application". Turn it into a date for each message, and flag what the rule counts from and whether it's calendar or working days. If the rule itself isn't confirmed, list the rule as needing a decision, not the date.

When adapting a pattern:

- leave out a line only when the service context confirms the service doesn't have that thing, like a tracking route. If the fact is just unknown, keep the placeholder and flag it
- don't draft for a channel the service doesn't use, or only plans to use, unless the user asks
- if the service context records how it chooses channels, like "letters only if there's no email address", draft the main channel and say which customers get the alternative
- send one channel for each moment unless there's a reason to send 2. The Service Manual says to avoid sending an email and a text message at the same time "unless there's a very good reason". A letter followed by a pointer text counts as one message with a pointer. Updating a status page doesn't count as a second message
- check the channel can arrive in time. A letter can't announce a call tomorrow. If no channel the service uses can arrive in time, flag it
- if the customer's word for their case is also an outcome, like "registration" or "licence", don't let it read as the outcome. Write "application to register" or "licence application" where it would
- if the service context maps a case state to a moment, treat it as a starting point. If the pattern doesn't fit, say so

### Combining moments

Sometimes 2 moments happen at once, like a decision and the thing being issued, or a receipt and a request. Send one message:

1. Lead with the moment that matters most to the customer, usually the outcome or the action.
2. Then give the other moment's core information.
3. Keep each moment's checkpoints.

### Pointer messages

When the detail goes by email or letter, or the service has decided texts must say less, a text can point to it. The patterns use these 2 generic pointers:

```
We've sent you [an email / a letter] about your [case].
```

```
Please contact us about your [case]. [how to get in touch]
```

Send a pointer only once the email or letter is likely to have arrived. A pointer that only says "contact us" from an unrecognised sender looks like a scam. Say how to check it's genuine where the service has decided how.

### Text messages

- count characters using the service's real reference format and the longest likely values, like the longest date. Over 160 counts as more than one text. In this repository, `evals/text-message-lengths.py` checks every baseline with long values
- use straight apostrophes and quote marks. This is a technical precaution, not a GOV.UK writing rule. Notify's text message pricing page says non-standard characters cut the limit to 70. It lists "single and double quotation marks" and "dashes" as standard, but doesn't say whether that includes curly ones. A test message through Notify would settle it
- the text baselines start with "[Service name]: ". Leave it out if the sender ID already names the service
- if the sender ID doesn't name the service, like "GOVUK", and the service name would reveal something sensitive on a lock screen, there's a trade-off: an anonymous text looks like a scam, and a named one reveals the service. That's a decision for the service. Flag it, and don't resolve it by revealing more
- if the service has a language duty, like Welsh, each version needs its own count. Welsh accented letters cut the limit to 70

## When the customer is an organisation

Some services deal with businesses or other organisations. The message goes to a named contact, who may not own the case.

- greet the named contact by name in emails, as the Service Manual asks
- name the organisation in the first line, like "We've received the application for ((business name))"
- write "your [case]" only if the contact is the person responsible for it. Otherwise write "the [case] for ((organisation name))"
- the named contact may have left. A bounced email or returned letter may mean a new person needs to be found, and whether they have authority to act is a service decision
- a sole trader may work from home. Their business address, opening hours or inspection dates can reveal where they live and when they're in. Treat these as personal data
- information about a limited company is generally not personal data, but information about an identifiable sole trader, partner, director or employee can be. The named contact's name and email address are personal data. See "Information about businesses and organisations" in `privacy-aware-communications`

## Failure modes for every moment

These apply to all moments, so they aren't repeated below.

- explaining the service's process instead of what it means for the customer. The Service Manual says: "Don't explain back-end processes or policy."
- a status with no next step or timescale (interpretation, from parts 4 and 5 of the anatomy)
- inventing a timescale the service can't meet (interpretation)
- saying more than the channel should carry. Check with `privacy-aware-communications`

## Questions for every service

For each moment a service uses, it needs to answer:

- what triggers it in the service
- which channels it uses
- the timescales it can commit to
- whether the message has legal effect, like a formal notice
- what the message can reveal, in each channel

## Moments

Pick the moment from the customer's situation, not the service's event. Each pattern file has the full detail: customer questions, variants, checkpoints and evidence.

| Moment | Customer situation | Customer action | Not to be confused with | Status |
|---|---|---|---|---|
| 1. We've received it | they've sent something and don't know if it arrived | usually no | 2, which says work has started. Something sent later in the case, and a record of a conversation, are variants of this moment | supported by a main source, and seen in 2 services |
| 2. Your case has moved on | they know the service has their case, but haven't heard for a while | usually no | 1, which confirms arrival, and variant C of 3, where a wait has ended. Send only if it passes the pattern's "When to send it" test | seen in 2 services |
| 3. We're waiting on someone else | their case depends on someone outside the service | usually no, sometimes yes | 5, where the service is waiting on the customer | seen in 2 services |
| 4. We'll contact you | the service has arranged a call, appointment, interview or visit | sometimes, like being available | 6, where contact was attempted and failed | supported by a main source, and seen in 2 services |
| 5. We need something from you | the case can't move until the customer does something | yes | 3, where the service is waiting on someone else | supported by a main source, and seen in 2 services |
| 6. We couldn't reach you | the service tried to contact them and couldn't, or a message couldn't be delivered | often | 5, a written request with no missed contact. The customer didn't expect the contact and may suspect a scam | seen in 2 services |
| 7. We've made a decision | the case has an outcome, or has closed without one | depends on the outcome | 2, a stage finishing with no outcome yet | seen in 2 services |
| 8. What you applied for is on its way | they know the outcome, and are waiting for the thing itself | sometimes, like signing it when it arrives | 7, the decision itself. Actions after a decision use 5 or 9 | seen in 2 services |
| 9. You need to act before a date | something is due, like a renewal, outside a live case | yes | 5, a request during a live case | supported by a main source, and seen in 2 services |

## Modifiers

A modifier changes how a moment's message is written, without being a moment of its own.

### Reminder

The same message again, after the customer hasn't acted or before something planned.

- start by saying what was said before, and when, like "We asked you on [date] to..."
- keep the same deadline, if there is one, unless the service has changed it
- applies to: 4 (we'll contact you), 5 (we need something from you), 8 (what you applied for is on its way, variant C), 9 (you need to act before a date)

### Final reminder

The last reminder before a consequence.

- put the deadline and the consequence first
- don't introduce a consequence that wasn't in the earlier messages without flagging it
- applies to: 5, 6, 9

### Delay

Something is taking longer than the customer was told.

- say there's a delay
- say whether the customer needs to do anything. Interpretation: this matters most, because the customer may think the delay is theirs
- give a new expectation, as a date where possible
- explain the cause only if the service has decided it can be disclosed
- applies to: any moment that gave the customer a timescale, most often 1, 2, 3, 4, 7 and 8
- evidence: unpublished prototype work only

## Follow-ups

A follow-up is a separate kind of message that follows, or is attached to, a moment. It doesn't tell the customer anything about their case.

### Ask for feedback

- **follows:** 7 (a decision, including a case closed without one), 8 (delivery), or a completed interaction, like a call
- **pattern:** `patterns/ask-for-feedback.md`
- **status:** supported by a main source, the Service Manual's "Measuring user satisfaction"
- **kind of message:** not assumed to be a service message. See `kinds-of-message.md` in `privacy-aware-communications`

## No message needed

Some internal events don't change anything for the customer, like a case moving between teams. They need no message.

Evidence: unpublished prototype work. Status: seen in 1 service.

## Gaps

Points a service needs that no moment covers yet. Add them here in generic words, with the date. Do not name the service.

None open.
