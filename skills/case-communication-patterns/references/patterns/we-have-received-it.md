# Pattern: We've received it

Moment 1 in `../moments.md`. Draft, last revised 6 October 2026.

Lines starting with ">" are quotes. Lines starting with "Interpretation:" are ours. "How to use the baseline copy" in `../moments.md` explains the 2 kinds of placeholder.

## Purpose

To confirm that something the customer sent has arrived, so they stop wondering whether it was lost. It gives them a reference and tells them what happens next.

## Trigger

The service records that something the customer sent has arrived, like an application, a form, a report or documents. The service context names the event.

## Customer situation

They've sent something and don't know whether it arrived. If they posted it, they may worry it was lost.

## Customer questions

- did you get it?
- what's my reference?
- what happens now, and when?
- do I need to do anything?

## Core information

Every version of this message says:

- what was received
- that the service now has it
- whether the customer needs to do anything. Usually they don't, so say "You do not need to do anything now". Only say this if it's true. See variant D

Emails, letters and status pages also say:

- the reference, if the customer might need to contact the service. The Service Manual says to "include a reference number and contact details if the user might need to contact you"
- what happens next, and when the customer will hear

Interpretation: a text message can leave out what happens next if it points to a tracking route. A very short text is a strong version of this message.

## Optional information

- the date it was received. Useful if the customer posted it, or if the date matters to them
- what that date means, if it has legal significance and the service has confirmed what to say
- a timescale for the next step, only if the service can meet it. If it only applies once the service has checked what was sent, say so
- how to track progress
- what will happen to anything they sent that they'll want back, like original documents
- how to get help

## Placeholders

From the service context:

| Placeholder | What the service context supplies |
|---|---|
| [service name] | the name customers know the service by |
| [what we received] | the customer's word for it, like "application". It must not read as the outcome. If the case is called a "registration" or a "licence", write "application to register" or "licence application" instead. Check the privacy checkpoints too |
| [next step] | what the customer will experience next, not the internal process |
| [timescale] | when that will happen, as a range the service can meet |
| [timescale condition] | when the timescale applies, like "if your application is complete" |
| [what the date means] | only if receipt has legal significance, in the service's confirmed words |
| [tracking URL] | a full GOV.UK web address |
| [contact details] | how to get help, in the A to Z format, like "Telephone: 0300 000 0000" with opening times on separate lines |
| [sender] | who the message is from, as the customer will recognise it |
| [letter greeting] | from the service's letter template |

Filled for each message:

| Placeholder | Value |
|---|---|
| ((first name)) ((last name)) | the customer's full name, or the named contact's |
| ((reference)) | the case reference |
| ((date received)) | the date, like 6 October 2026 |
| ((date)) | the date of the letter |

## Variants

### A. First receipt

The start of a case. Use the baseline copy below.

### B. Received something we asked for

The customer has sent something the service asked for during the case. This was moment 6 (see "Changes to the moments" in `../moments.md`).

Change the baseline:

- say what was asked for and when, like "the [what we asked for] we asked for on ((date asked))"
- say whether anything else is still needed. If it is, use "We need something from you", variant B, instead
- never say it has been accepted or approved if it has only arrived

### C. Received, and work has started

Use this when work starts straight away. Send one message, not 2 messages hours apart. Add a line saying what happens next.

Interpretation: receipt and work starting can be days apart in some services, which is why they're separate moments. When they aren't, combine them.

### D. Received, and every customer has a next step

Every customer needs to do something next, like send a document or book an appointment. Don't say "You do not need to do anything now". Confirm receipt in the first line, then make the request using the "We need something from you" pattern, in the same message.

### E. We've recorded what you told us

The customer gave information in a conversation, like a phone call, and the service confirms what it recorded. This was moment 12 (see "Changes to the moments" in `../moments.md`).

Change the baseline:

- say when the conversation happened, like "when we spoke on ((date of call))"
- summarise what was recorded, only as much as the customer needs to check it
- say how to correct it, and by when, if the service has decided this
- if the conversation agreed something the customer needs to do, use "We need something from you" for it, in the same message

Interpretation: a record of a conversation can repeat sensitive answers. Keep them out of texts and previews, and check the channel with `privacy-aware-communications`. This variant has weak evidence: one unpublished service. See "Evidence gaps".

### Not this pattern

- if what arrived is incomplete, and the customer needs to act, use "We need something from you", variant B. Don't send a receipt that suggests everything is fine
- if the service has made a decision, use moment 7, "We've made a decision"

## Modifiers that apply

- **delay:** if the next step will take longer than the customer was told. See "Modifiers" in `../moments.md`

## Common failure modes

- "received" in a way that sounds like "accepted", "approved" or "registered"
- "You do not need to do anything now" when every customer does
- no reference, so the customer cannot quote it when they get in touch
- "in due course" or "shortly" instead of a next step or timescale
- describing the internal process, like scanning or allocating to a team. The Service Manual says: "Don't explain back-end processes or policy."
- a timescale the service cannot meet, or one that only applies to complete applications, given without saying so
- naming something in a text or subject line that reveals what the case is about

## Privacy and policy checkpoints

Check these with `privacy-aware-communications`. Don't decide them here.

- **what was received:** would naming it reveal special category or sensitive information? This matters most in the sender name, subject line, first line and any text message. If it would, use a neutral word in those places
- **reference:** it is personal data. Include it where the customer needs it, and don't add other identifiers. Check the reference format itself doesn't reveal the service or the subject, like a prefix seen on a lock screen
- **legal significance:** does the date of receipt matter legally? For example, it may show the customer met a duty to tell the service by a date, or it may start a time limit. This is a service fact. If it applies, the message may need legal review and a fixed channel. If the service context doesn't list this message as a formal communication, that's not confirmation it has no legal effect
- **originals:** what happens to original documents is a service fact. Don't promise their return unless the service context confirms it

## Baseline copy

Leave out any line for something the service doesn't have, like a tracking route. Don't force every part into every channel.

### Email

```
Subject: [Service name]: we've received your [what we received]

Dear ((first name)) ((last name))

We've received your [what we received]. We got it on ((date received)).

Your reference number is ((reference)). Use it if you contact us.

What happens next

We'll [next step] by [timescale] [timescale condition].

You do not need to do anything now.

You can check the progress of your [what we received] at [tracking URL]

If you need help, contact us:
[contact details]

[Sender]
```

### Text message

With a tracking route:

```
We've received your [what we received]. Reference: ((reference)). You do not need to do anything now. Track it: [tracking URL]
```

Without one:

```
We've received your [what we received]. Reference: ((reference)). We'll [next step] by [timescale]. You do not need to do anything now.
```

As a pointer, if the service sends the detail by email or letter, or has decided texts must say less:

```
We've sent you [an email / a letter] about your [what we received]. Reference: ((reference)).
```

Send a pointer text only once the email or letter is likely to have arrived.

See "Text messages" in `../moments.md` for counting characters and sender IDs.

### Letter

```
Reference: ((reference))
((date))

We've received your [what we received]

[letter greeting]

We received your [what we received] on ((date received)). [what the date means]

What happens next

We'll [next step] by [timescale] [timescale condition].

You do not need to do anything now.

[Optional: We'll return your [original documents] by [timescale].]

Check progress or get help

You can check the progress of your [what we received] at [short tracking URL].

If you need help, contact us:
[contact details]

Have your reference number ready.

[Sender]
```

The main sources don't cover how to greet or sign off a letter. Use the service's letter template, and flag it if there isn't one.

### Status page, behind sign-in

```
Status: Received

We received your [what we received] on ((date received)).

What happens next
We'll [next step] by [timescale] [timescale condition].

You do not need to do anything now.
```

Keep personal information out of the page title, the main heading and the web address.

## Evidence

- **status:** supported by a main source, and seen in 2 services. Adapted for 3 invented services. Not yet tested with users
- **Service Manual**, describing transactional messages: "they completed a transaction, and you're sending them a confirmation email"
- **HM Passport Office**, "How we communicate with customers" (published): automatic notifications "let the customer know we have received the lost or stolen report" and "give the customer a reference number". It also sends "an automatic email response to acknowledge receipt" of an email to a team mailbox
- **unpublished design work in one service:** the moment occurs, and so does a record of a conversation. No detail is recorded

### Evidence gaps

- variant E, a record of a conversation, has no published evidence. No published source we've found shows a service confirming in writing what a customer said on a call

### Tested against the evidence

Interpretation, from adapting this pattern back to each source:

- a very short text with a reference and a tracking route meets the core need, so what happens next is optional in a text
- a published service gives the reference in its own notification. The pattern allows this
- the date received matters most to customers who posted something. It's optional rather than core
- the date can also matter legally, which added the "legal significance" checkpoint

### Adapted for invented services

Interpretation, from adapting this pattern for a permit, a benefit and a registration service on 6 October 2026:

- a case word that is also the outcome, like "registration", made "We've received your registration" read as "you're registered". [what we received] now warns against this
- every business in one service had a standard next step, so "You do not need to do anything now" was false. Variant D was added
- a decision timescale applied only once an application was checked as complete. [timescale condition] was added
- a service that only lets texts point to a letter had no text to start from. The pointer text was added
- a reference prefix could reveal the service on a lock screen. The reference checkpoint now covers the format
