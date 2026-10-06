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

There are 9 moments, 3 modifiers and 1 follow-up. "Changes to the moments" at the end says how they changed from the first draft.

## How to read this file

### Evidence status

Each moment has one status:

- **proposed:** suggested, with no evidence recorded yet
- **seen in 1 service**
- **seen in 2 or more services**
- **supported by a main source:** a GOV.UK main source describes the need, as well as at least one service showing it
- **tested with users**

A moment's status only changes when new evidence is added here.

### Evidence sources

- **unpublished prototype work:** "observed in unpublished prototype work". This is one service's own design work, not a published source. It shows that a moment occurs, so no detail is recorded and the service is not named
- **HM Passport Office:** "How we communicate with customers", caseworker guidance, published on GOV.UK: https://www.gov.uk/government/publications/how-we-communicate-with-customers/how-we-communicate-with-customers-accessible-version
- **Service Manual:** "Planning and writing text messages and emails": https://www.gov.uk/service-manual/design/sending-emails-and-text-messages

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

- **[square brackets]:** a service fact, filled once from the service context, like [sender] or [tracking URL]. Only use confirmed facts
- **((double brackets)):** a value filled for each message when it's sent, like ((reference)) or ((deadline)). GOV.UK Notify uses this format for personalisation. These are not gaps in the service context

When adapting a pattern:

- leave out any line for something the service doesn't have, like a tracking route
- don't draft for a channel the service doesn't use, or only plans to use, unless the user asks
- if the service context records how it chooses channels, like "letters only if there's no email address", draft the main channel and say which customers get the alternative
- send one channel for each moment unless there's a reason to send 2. The Service Manual says to avoid sending an email and a text message at the same time "unless there's a very good reason"

### Text messages

- count characters using the service's real reference format and the longest likely values, like the longest date. Over 160 counts as more than one text
- use straight apostrophes and quote marks. This is a technical precaution, not a GOV.UK writing rule. Notify's text message pricing page says non-standard characters cut the limit to 70, but doesn't say whether curly apostrophes are standard. A test message through Notify would settle it
- if the sender ID doesn't name the service, like "GOVUK", start the text with the service name, like "[Service name]: ". Check the name itself doesn't reveal something sensitive on a lock screen
- if the service has a language duty, like Welsh, each version needs its own count. Welsh accented letters cut the limit to 70

## When the customer is an organisation

Some services deal with businesses or other organisations. The message goes to a named contact, who may not own the case.

- greet the named contact by name in emails, as the Service Manual asks
- name the organisation in the first line, like "We've received the application for ((business name))"
- write "your [case]" only if the contact is the person responsible for it. Otherwise use the organisation's name
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

Each moment's pattern file holds its full evidence. The entries for 1, 3 and 5 keep their original detail.

### 1. We've received it

- **customer situation:** they've sent something and don't know if it arrived
- **customer questions:** did you get it? What's my reference? What happens now?
- **should establish:** it arrived, the reference, what happens next and when, whether they need to do anything
- **customer action:** usually no
- **failure modes:** no reference, so the customer can't quote it when they call (interpretation)
- **privacy or policy questions:** whether the message should say what was received, if that reveals the subject of the case
- **not to be confused with:** 2, which says work has started. Something sent later in the case is variant B of this moment
- **evidence:**
  - unpublished prototype work: observed
  - HM Passport Office: "If a customer sends an email to an examination team mailbox, we will send them an automatic email response to acknowledge receipt of the email."
  - Service Manual, describing transactional messages: "they completed a transaction, and you're sending them a confirmation email"
- **status:** supported by a main source
- **includes:** variant B, "We've received what you sent", which was moment 6, and variant E, a record of a conversation, which was moment 12

### 2. Your case has moved on

- **customer situation:** they know the service has their case, but haven't heard for a while
- **should establish:** what has changed for them, what happens next and when, whether they need to do anything
- **customer action:** usually no
- **not to be confused with:** 1, which confirms arrival, and variant C of 3, where a wait has ended. Send only if it passes the pattern's "When to send it" test
- **pattern:** `patterns/your-case-has-moved-on.md`, which has the evidence, variants and checkpoints
- **status:** seen in 2 services, counting both earlier moments
- **includes:** "Work has started" and "Something has changed", which were moments 2 and 4

### 3. We're waiting on someone else

- **customer situation:** their case depends on someone outside the service
- **customer questions:** what's happening while I wait? Is it my fault? Do I need to do anything?
- **should establish:** the service is waiting on someone else, roughly how long, whether the customer needs to do anything, what happens if there's no reply
- **customer action:** usually no, sometimes yes
- **failure modes:** making the customer think the delay is theirs (interpretation)
- **privacy or policy questions:** whether to say who the service is waiting on. Naming them can reveal sensitive information
- **not to be confused with:** 5, where the service is waiting on the customer
- **evidence:**
  - unpublished prototype work: observed
  - HM Passport Office: tells customers when "we send an email to their digital referee asking them to complete the referee section of the application"
- **status:** seen in 2 or more services
- **includes:** variant B, "We're still waiting", which was moment 16, and variant C, when the wait ends

### 4. We'll contact you

- **customer situation:** the service has arranged a call, appointment, interview or visit
- **should establish:** when, where or how, how to recognise it's genuine, what to have ready, how to change it
- **customer action:** sometimes, like being available
- **not to be confused with:** 6, where contact was attempted and failed
- **pattern:** `patterns/we-will-contact-you.md`, which has the evidence, variants and checkpoints
- **status:** supported by a main source, and seen in 2 services
- **includes:** reminders of planned contact, using the reminder modifier, which was moment 8

### 5. We need something from you

- **customer situation:** the case can't move until the customer does something
- **customer questions:** what do you need? How do I send it? By when? What if I can't?
- **should establish:** exactly what's needed, how to provide it, the deadline, what happens if they don't, how to get help
- **customer action:** yes
- **failure modes:** asking for personal information in an email or text. The Service Manual says to "avoid making requests for personal information"
- **privacy or policy questions:** how the customer can send it securely, and what the consequence of not acting is
- **not to be confused with:** 3, where the service is waiting on someone else
- **evidence:**
  - unpublished prototype work: observed
  - HM Passport Office: "When customers do not send us the documents we need, we will send them automatic reminders through text message or email." It also tells customers when "we need a new photo"
  - Service Manual: "make it clear what you need the user to do and include any deadlines"
- **status:** supported by a main source

### 6. We couldn't reach you

- **customer situation:** the service tried to contact them and couldn't, or a message couldn't be delivered
- **should establish:** who tried, that it was genuine, what happens now, what to do and by when
- **customer action:** often
- **not to be confused with:** 5, a written request with no missed contact
- **pattern:** `patterns/we-could-not-reach-you.md`, which has the evidence, variants and checkpoints
- **status:** seen in 2 services

### 7. We've made a decision

- **customer situation:** the case has an outcome, or has closed without one
- **should establish:** the outcome first, what it means, what happens next or that it's the end, how to challenge it if they can
- **customer action:** depends on the outcome
- **not to be confused with:** 2, a stage finishing with no outcome yet
- **pattern:** `patterns/we-have-made-a-decision.md`, which has the evidence, variants and checkpoints
- **status:** seen in 2 services
- **includes:** "We're closing your case", which was moment 11, as variant D

### 8. What you applied for is on its way

- **customer situation:** they know the outcome, and are waiting for the thing itself
- **should establish:** what's been sent or issued, when to expect it, what to do if it doesn't arrive, whether it's the end of the process
- **customer action:** sometimes, like signing it when it arrives
- **not to be confused with:** 7, the decision itself
- **pattern:** `patterns/what-you-applied-for-is-on-its-way.md`, which has the evidence, variants and checkpoints
- **status:** seen in 2 services
- **was:** "What happens after the decision", moment 9, narrowed to what's issued, sent or made available

### 9. You need to act before a date

- **customer situation:** something is due, like a renewal, outside a live case
- **should establish:** what's due, the date, how to do it, what happens if they don't
- **customer action:** yes
- **not to be confused with:** 5, a request during a live case
- **pattern:** `patterns/you-need-to-act-before-a-date.md`, which has the evidence, variants and checkpoints
- **status:** supported by a main source, and seen in 2 services
- **was:** moment 10

## Modifiers

A modifier changes how a moment's message is written, without being a moment of its own. Agreed on 6 October 2026, from writing the first 3 patterns.

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
- was moment 15. Its evidence was unpublished prototype work only

## Follow-ups

A follow-up is a separate kind of message that follows, or is attached to, a moment. It doesn't tell the customer anything about their case.

### Ask for feedback

- **follows:** 7 (a decision, including a case closed without one), 8 (delivery), or a completed interaction, like a call
- **pattern:** `patterns/ask-for-feedback.md`
- **status:** supported by a main source, the Service Manual's "Measuring user satisfaction"
- **kind of message:** not assumed to be a service message. See `kinds-of-message.md` in `privacy-aware-communications`

## Changes to the moments

### Round 2: writing the remaining patterns

Made on 6 October 2026, while writing patterns for every moment. There were 12 moments, and now there are 9, with 3 modifiers and 1 follow-up.

| Was | Now | Reason |
|---|---|---|
| 2. Work has started | merged into 2, "Your case has moved on" | evidence from 1 unpublished service. It differs from "We've received it" only when there's a gap before work starts |
| 4. Something has changed | merged into 2, "Your case has moved on" | most of its evidence was a wait ending, now variant C of 3. What's left is the same message as "Work has started" |
| 6. We'll contact you | 4 | renumbered. Now covers appointments and visits too |
| 7. We couldn't reach you | 6 | renumbered |
| 8. We've made a decision | 7 | renumbered |
| 9. What happens after the decision | 8, "What you applied for is on its way" | narrowed. Actions after a decision use 5 or 9 |
| 10. You need to act before a date | 9 | renumbered |
| 11. We're closing your case | variant D of 7 | the message has the same shape as a decision: what happened, why, what it means, what you can do. Evidence from 1 published service |
| 12. Here's a record of what we discussed | variant E of 1 | it confirms what the service recorded, like a receipt. Evidence from 1 unpublished service |
| none | follow-up: "Ask for feedback" | a different kind of message that follows a moment, not a case state |

Kept, after testing whether to merge:

- 9 is kept separate from 5. It doesn't block a live case, can be a subscription, and has its own direct marketing question
- 6 is kept separate from 5. The customer didn't expect the contact and may suspect a scam, which changes the message
- 8 is kept separate from 7. Published evidence shows services send separate messages for issuing and delivery

### Round 1: after the first 3 patterns

Agreed on 6 October 2026, after writing the first 3 patterns. There were 16 moments, and then 12, with 3 modifiers. The numbers in this table are from before round 2.

| Was | Now | Reason |
|---|---|---|
| 6. We've received what you sent | variant B of 1 | the message is the same receipt, with "is anything else needed" added |
| 7. We'll contact you | 6 | renumbered |
| 8. Reminder | the reminder modifier, applied to 6 | a reminder repeats another moment's message. It's not a separate customer situation |
| 9 to 14 | 7 to 12 | renumbered |
| 15. There's a delay | the delay modifier | a delay can happen in several moments, and its content is the same in each |
| 16. We're still waiting | variant B of 3 | it continues the same situation, and only makes sense after 3 |

Also from the patterns:

- 4 is kept, but its evidence needs checking, because most of it was a wait ending
- 10 is kept separate from 5. It doesn't block a live case, but it shares the reminder modifier
- something the customer sent can't be used, and a replacement is needed: this is variant C of 5

## No message needed

Some internal events don't change anything for the customer, like a case moving between teams. They need no message.

Evidence: unpublished prototype work. Status: seen in 1 service.

## Gaps

Points a service needs that no moment covers yet. Add them here in generic words, with the date. Do not name the service.

None recorded yet.
