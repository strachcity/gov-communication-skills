# Pattern: What you applied for is on its way

Moment 8 in `../moments.md`. Draft, last revised 6 October 2026.

Lines starting with ">" are quotes. Lines starting with "Interpretation:" are ours. "How to use the baseline copy" in `../moments.md` explains the 2 kinds of placeholder.

This was moment 9, "What happens after the decision". It has been narrowed to what's issued, sent or made available after a decision. Actions after a decision use "We need something from you" or "You need to act before a date".

## Purpose

To tell the customer that what they applied for has been issued, sent or made available, when to expect it, and what to do if it doesn't arrive.

## Trigger

The service issues, sends or makes available what the customer applied for, or returns something they sent. The service context names the event.

## Customer situation

They know the outcome, and are waiting for the thing itself, like a document, a licence, a payment or a card. They may need it by a date.

## Customer questions

- when will it arrive?
- how will it arrive?
- what if it doesn't arrive?
- do I need to do anything when it arrives?
- is this the end of my case?

## Core information

Every version of this message says:

- what has been issued or sent
- how and when it will arrive, or where to collect or download it
- what to do if it doesn't arrive by a date

Emails and letters also say:

- anything the customer needs to do when it arrives
- whether this is the end of the process. The Service Manual says "if you won't be contacting them again, make it clear that it's the end of the process"

## Optional information

- how to track delivery
- what to check when it arrives
- what will happen to anything the customer sent, like original documents

## Placeholders

From the service context:

| Placeholder | What the service context supplies |
|---|---|
| [service name] | the name customers know the service by |
| [what we've issued] | the customer's word for it |
| [how it's sent] | like post, courier, email or a download |
| [arrival timescale] | how long it usually takes, only if the service can meet it |
| [if it does not arrive] | what to do, and when, as the service has confirmed it |
| [what to do when it arrives] | like sign it or activate it, only if needed |
| [collection or download details] | for variant B |
| [ongoing duties] | only if the customer has a continuing duty, like telling the service about changes. See variant D of "You need to act before a date" |
| [when the next reminder comes] | a full sentence, like "We'll remind you before it expires." |
| [contact details] | how to get help, in the A to Z format |
| [sender] | who the message is from |
| [letter greeting] | from the service's letter template |

Filled for each message:

| Placeholder | Value |
|---|---|
| ((first name)) ((last name)) | the customer's full name |
| ((reference)) | the case reference |
| ((date sent)) | the date it was sent |
| ((arrive by)) | the date it should arrive by, from [arrival timescale] |
| ((tracking number)) | only if the service sends one |

## Variants

### A. It's been sent

Use the baseline copy.

### B. It's ready to collect or download

Say where and how, and any deadline for collecting it. For a download, give the full GOV.UK web address, never an attachment.

### E. Sent by email

The document itself is sent by email. Replace "should arrive by" with what's attached or linked. The Service Manual says emails should "avoid sending attachments". Flag this conflict for the service. The lower-risk option is a link to download it behind sign-in.

### C. Something to do when it arrives

The customer needs to do something with it, like sign it. Say so clearly in the first message, and in a reminder if the service sends one.

### D. Returning what the customer sent

The service is returning documents or items the customer sent. Say what's being returned and how.

### Not this pattern

- the decision itself: use "We've made a decision". If the decision and the issue happen together, combine them, with the outcome first. See "Combining moments" in `../moments.md`
- something the customer needs to do before a date, unrelated to delivery: use "You need to act before a date"

## Modifiers that apply

- **delay:** if it will arrive later than the customer was told
- **reminder:** for variant C, if the service reminds the customer what to do

## Common failure modes

- no date for when to expect it, so the customer can't tell when it's late
- no route if it doesn't arrive
- not saying whether this is the end of the process
- sending a link to download something sensitive in an email or text. Downloads should be behind sign-in
- the envelope or parcel revealing what's inside

## Privacy and policy checkpoints

Check these with `privacy-aware-communications`. Don't decide them here.

- **outside the envelope:** could the envelope, parcel or return address reveal what's inside, or something sensitive? This is high risk
- **valuable items in the post:** identity documents or payment cards in the post may attract theft. How they're sent is a service decision
- **address:** check the address is current before sending. An item sent to an old address reaches someone else
- **lost items:** what happens if it's lost, and whether there's a charge, must come from the service context
- **downloads:** case documents should be behind sign-in, not attached or linked openly
- **attachments:** sending the document as an email attachment conflicts with the Service Manual's advice to avoid attachments. Flag it

## Baseline copy

Leave out any line for something the service doesn't have.

### Email

```
Subject: [Service name]: your [what we've issued] is on its way

Dear ((first name)) ((last name))

We sent your [what we've issued] by [how it's sent] on ((date sent)). It should arrive by ((arrive by)).

Your reference number is ((reference)).

[If there's something to do when it arrives:]
When it arrives

[what to do when it arrives]
[End if]

If it has not arrived by ((arrive by))

[if it does not arrive]

[If this is the end of the process, and no reminders follow:]
This is the last message we'll send you about this [case].
[End if]

[If reminders follow, like for a renewal:]
[when the next reminder comes]
[End if]

[If there's a continuing duty:]
If anything changes

[ongoing duties]
[End if]

[Sender]
```

### Text message

```sms
[Service name]: we sent your [what we've issued] on ((date sent)). It should arrive by ((arrive by)). If it has not arrived by then, [if it does not arrive, in a few words].
```

### Letter

Interpretation: if the item itself is sent by post, a separate letter is often not needed. That's a service decision.

```
Reference: ((reference))
((date))

Your [what we've issued] is on its way

[letter greeting]

We sent your [what we've issued] by [how it's sent] on ((date sent)). It should arrive by ((arrive by)).

If it has not arrived by ((arrive by)), [if it does not arrive].

[Sender]
```

### Status page, behind sign-in

```
Status: Sent

We sent your [what we've issued] on ((date sent)). It should arrive by ((arrive by)).

If it has not arrived by then
[if it does not arrive]
```

## Evidence

- **status:** seen in 2 services. A main source supports saying when it's the end of the process. Not yet tested with users
- **Service Manual**, "Planning and writing text messages and emails": "if you won't be contacting them again, make it clear that it's the end of the process"
- **HM Passport Office**, "How we communicate with customers" (published): sends messages "to tell them when they can expect to receive their new passport", "telling them their passport will be with them soon", and "reminding them to sign their new passport when they receive it". It says "We will stop sending automatic messages when we have sent the customer their new passport"
- **unpublished design work in one service:** the moment occurs. No detail is recorded

### Evidence gaps

- no published source shows what services tell customers to do if something doesn't arrive
- no published source covers collection or download

### Adapted for invented services

Interpretation, from adapting this pattern for a permit, a benefit and a registration service on 6 October 2026:

- 2 services sent the document by email on the day of the decision. "Should arrive by" didn't fit, and the attachment conflict wasn't raised. Variant E and the attachment checkpoint were added, with a pointer to combining with the decision
- "This is the last message" was wrong where a renewal reminder follows
- one service had a standing duty to report changes. An optional "If anything changes" section was added
