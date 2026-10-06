# Moments

Draft, last revised 6 October 2026. Every moment here is a proposal.

Patterns written so far, in `patterns/`:

- 1. We've received it: `patterns/we-have-received-it.md`
- 3. We're waiting on someone else: `patterns/we-are-waiting-on-someone-else.md`
- 5. We need something from you: `patterns/we-need-something-from-you.md`

There are 12 moments and 3 modifiers. "Changes to the moments" at the end says how they changed from the first draft.

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
- **includes:** variant B, "We've received what you sent", which was moment 6

### 2. Work has started

- **customer situation:** they've been told it arrived, but nothing seems to be happening
- **customer questions:** is anyone working on it? When will I hear?
- **should establish:** someone has started, what happens next and when, whether they need to do anything
- **customer action:** no
- **failure modes:** naming internal roles or teams the customer doesn't know (interpretation)
- **privacy or policy questions:** whether naming who holds the case reveals something sensitive
- **not to be confused with:** 1, which only confirms arrival
- **evidence:**
  - unpublished prototype work: observed
- **status:** seen in 1 service

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

### 4. Something has changed

- **customer situation:** their case has moved on, often after a wait
- **customer questions:** what changed? What happens now?
- **should establish:** what changed, what happens next and when, whether they need to do anything
- **customer action:** usually no
- **failure modes:** an update that says something happened but not what it means for them (interpretation)
- **privacy or policy questions:** whether the update reveals anything about a third party
- **not to be confused with:** 8, which is a decision, and variant C of 3, where a wait has ended
- **evidence:**
  - unpublished prototype work: observed
  - HM Passport Office: tells customers when "the referee has completed the application" and when "we have finished automatic identity checks"
- **status:** seen in 2 or more services
- **evidence note:** most of the evidence first recorded here was a wait ending, which is now variant C of 3. This moment may only cover changes not tied to a wait. Check before writing its pattern

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

### 6. We'll contact you

- **customer situation:** the service plans to call or contact them
- **customer questions:** when? Is it genuine? What should I have ready?
- **should establish:** when and how contact will happen, how to recognise it's genuine, what to have ready, what to do if the time doesn't work
- **customer action:** sometimes, like being available
- **failure modes:** no way to tell the contact is genuine, so the customer ignores it (interpretation)
- **privacy or policy questions:** what can be said on the call before identity is checked
- **not to be confused with:** 7, where contact was attempted and failed. A reminder of planned contact uses the reminder modifier
- **evidence:**
  - unpublished prototype work: observed
- **status:** seen in 2 or more services, counting the reminder evidence
- **includes:** reminders of planned contact, using the reminder modifier. This was moment 8, whose evidence was: unpublished prototype work, observed; HM Passport Office: "We send automated SMS text messages to customers to remind them they have booked a counter appointment."

### 7. We couldn't reach you

- **customer situation:** the service tried to contact them and couldn't
- **customer questions:** who was it? Was it important? What do I do now?
- **should establish:** who tried, that it was genuine, what to do now and by when, what happens if they don't respond
- **customer action:** yes
- **failure modes:** leaving case detail on a voicemail or unsecured message (see privacy below)
- **privacy or policy questions:** what can go in a voicemail or text. HM Passport Office guidance says not to leave personal or special category data on an answerphone
- **not to be confused with:** 5, a written request for something
- **evidence:**
  - unpublished prototype work: observed
  - HM Passport Office: when there's no answer, staff "leave a voicemail to confirm you will call again in 2 hours", and after 3 attempts send a letter
- **status:** seen in 2 or more services

### 8. We've made a decision

- **customer situation:** the case has an outcome
- **customer questions:** what's the outcome? What does it mean for me? Can I challenge it?
- **should establish:** the outcome, what it means, what happens next, how to challenge it if they can
- **customer action:** depends on the outcome
- **failure modes:** burying the outcome under background (interpretation)
- **privacy or policy questions:** whether the decision is a formal notice, which channel it must use, and what decision language the service can use
- **not to be confused with:** 4, a progress update
- **evidence:**
  - unpublished prototype work: observed
  - HM Passport Office: sends an automated message "to tell them we have approved their application"
- **status:** seen in 2 or more services

### 9. What happens after the decision

- **customer situation:** the decision is made and something follows from it
- **customer questions:** what will arrive, and when? Do I need to do anything?
- **should establish:** what happens next, when, anything they need to do
- **customer action:** sometimes
- **failure modes:** ending contact without saying the case is finished (interpretation, from the Service Manual's "make it clear that it's the end of the process")
- **privacy or policy questions:** none known
- **not to be confused with:** 10, a future deadline
- **evidence:**
  - unpublished prototype work: observed
  - HM Passport Office: "We will send customers an automatic message reminding them to sign their new passport when they receive it."
- **status:** seen in 2 or more services

### 10. You need to act before a date

- **customer situation:** something is due, like a renewal
- **customer questions:** what's due? By when? How do I do it?
- **should establish:** what's due, the date, how to do it, what happens if they don't
- **customer action:** yes
- **failure modes:** a deadline written as a period rather than a date (interpretation)
- **privacy or policy questions:** none known
- **not to be confused with:** 5, a request during a live case
- **evidence:**
  - unpublished prototype work: observed
  - HM Passport Office: sends texts "to remind them their passport (or their child's passport) is due to expire"
  - Service Manual, describing transactional messages: "they paid for an annual service a year ago, and you're reminding them that it's about to expire"
- **status:** supported by a main source

### 11. We're closing your case

- **customer situation:** the case is ending without the outcome they applied for, for example because they didn't reply
- **customer questions:** why? Can I restart it?
- **should establish:** that the case is closing, why, what they can do now
- **customer action:** sometimes
- **failure modes:** closing without warning first (interpretation)
- **privacy or policy questions:** the rules for withdrawing or closing a case
- **not to be confused with:** 8, a decision on the case
- **evidence:**
  - HM Passport Office: "If we do not get a reply to an email or letter we have sent to a customer who has a live application with us, we will follow the withdrawn application guidance."
- **status:** seen in 1 service

### 12. Here's a record of what we discussed

- **customer situation:** they've had a conversation with the service
- **customer questions:** what did we agree? What happens now?
- **should establish:** when the conversation happened, what was asked and answered, what happens next
- **customer action:** sometimes, like correcting the record
- **failure modes:** none recorded yet
- **privacy or policy questions:** the record may repeat sensitive answers, which limits the channel
- **not to be confused with:** variant B of 1, which confirms something sent in writing
- **evidence:**
  - unpublished prototype work: observed
- **status:** seen in 1 service

## Modifiers

A modifier changes how a moment's message is written, without being a moment of its own. Agreed on 6 October 2026, from writing the first 3 patterns.

### Reminder

The same message again, after the customer hasn't acted or before something planned.

- start by saying what was said before, and when, like "We asked you on [date] to..."
- keep the same deadline, if there is one, unless the service has changed it
- applies to: 5 (we need something from you), 6 (we'll contact you), 10 (you need to act before a date)

### Final reminder

The last reminder before a consequence.

- put the deadline and the consequence first
- don't introduce a consequence that wasn't in the earlier messages without flagging it
- applies to: 5, 10

### Delay

Something is taking longer than the customer was told.

- say there's a delay
- say whether the customer needs to do anything. Interpretation: this matters most, because the customer may think the delay is theirs
- give a new expectation, as a date where possible
- explain the cause only if the service has decided it can be disclosed
- applies to: any moment that gave the customer a timescale, most often 1, 2 and 3
- was moment 15. Its evidence was unpublished prototype work only

## Changes to the moments

Agreed on 6 October 2026, after writing the first 3 patterns. There were 16 moments, and now there are 12, with 3 modifiers.

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
