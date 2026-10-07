# Pattern: You need to act before a date

Moment 9 in `../moments.md`. Draft, last revised 6 October 2026.

Lines starting with ">" are quotes. Lines starting with "Interpretation:" are ours. "How to use the baseline copy" in `../moments.md` explains the 2 kinds of placeholder.

## Purpose

To tell the customer that something is due, like a renewal, an expiry or a regular obligation, and what to do by when. It's not about a live case.

## Trigger

A date the service knows about is approaching, like a licence expiring, or an annual return being due. The service context names the dates and when reminders are sent.

## Customer situation

They may have forgotten. It may be a year or more since they last dealt with the service, so they may not recognise the sender, and their contact details may have changed.

## Customer questions

- what's due?
- by when?
- how do I do it?
- what happens if I don't?
- is this genuine?

## Core information

Every version of this message says:

- what's due, or what's expiring
- the date, using "on or before" for a deadline, or "expires on" for an expiry
- how to do it

Emails and letters also say:

- what happens if they don't, if the service has confirmed it
- if the customer signed up for these reminders, how to stop them

## Optional information

- how long it takes, so they can plan
- what they'll need to do it
- the cost, if there is one, from the service context

## Placeholders

From the service context:

| Placeholder | What the service context supplies |
|---|---|
| [service name] | the name customers know the service by |
| [what's due] | the customer's word for it, like "licence renewal" |
| [how to do it] | the route, with a full GOV.UK web address if online |
| [what you'll need] | only if needed |
| [due wording] | "is due on" for a deadline, or "expires on" for an expiry |
| [action] | what the customer needs to do, in lower case, like "renew it" or "send your annual return" |
| [action short] | for texts, a short instruction starting with a capital letter, like "Renew it" |
| [duty period] | for variant D, how soon after a change the customer must tell the service, like "14 days" |
| [what counts as a change] | for variant D, in the customer's words, like "you move house" |
| [how to tell us] | for variant D, the route |
| [consequence] | what happens if they don't act, as the service has confirmed it. "Must" only if the service context records a legal requirement. If it says "must" without saying why, flag it |
| [cost] | only if confirmed |
| [unsubscribe route] | for variant C |
| [sender] | who the message is from |
| [letter greeting] | from the service's letter template |

Filled for each message:

| Placeholder | Value |
|---|---|
| ((first name)) ((last name)) | the customer's full name |
| ((due date)) | the date it's due or expires |
| ((last date to act)) | if different, the last date the customer can act in time |
| ((record identifier)) | like a licence or permit number, if the customer may have more than one |
| ((date)) | the date of the letter |

## Variants

### A. Something is due to expire or be renewed

Say what expires and when, and how to renew it if the customer can. Give the last date to act separately from the expiry date, if they differ, so the customer knows renewing on the expiry date may be too late.

### B. A regular obligation is due

Like an annual return, review or report. Say what's needed and by when. This includes reviews of something the customer already has, like an ongoing award, even if a missed review could stop it.

### C. The customer signed up for reminders

The Service Manual calls these subscription messages. Always give a way to unsubscribe.

### D. A continuing duty, with no fixed due date

The customer has a duty that starts when something happens, like telling the service about a change within a set time. There's no date to remind them of. This was recorded as a gap, and now has its own copy.

- say what the duty is, what counts as a change, how soon they must act, and how
- say what happens if they don't, only if the service has confirmed it
- send it as a section in a decision or "What you applied for is on its way", or as a standalone reminder if the service sends one
- "must" only if the service context records a legal requirement. Otherwise "need to"

### Not this pattern

- an open application can't progress until the customer acts: use "We need something from you"
- something to do when an item arrives: use "What you applied for is on its way", variant C

## Modifiers that apply

- **reminder:** a second or later reminder before the date
- **final reminder:** the last before the date, with the consequence first

## Common failure modes

- a deadline written as a period instead of a date
- no way to recognise the sender, after a long gap
- "must" for something that isn't a legal requirement
- no way to unsubscribe from reminders the customer signed up for
- promoting a paid service in a way that turns a reminder into marketing

## Privacy and policy checkpoints

Check these with `privacy-aware-communications`. Don't decide them here.

- **kind of message:** is this a service message, an optional service update or a subscription? A reminder to renew a service the customer pays for may count as direct marketing, unless it's necessary for the service's function. The ICO says "messages promoting services paid for by the user (eg leisure facilities) or fundraising do generally count as direct marketing". See `kinds-of-message.md` in `privacy-aware-communications`
- **old contact details:** contact details may be out of date after a long gap. A reminder to an old number or address reaches someone else. This is a raised risk
- **whose record:** a reminder about someone else's record, like a child's, sent to a parent, contains that person's personal data
- **consequence:** what happens if they don't act must come from the service context. Never infer it
- **must or need to:** depends on whether there's a legal requirement

## Baseline copy

Inline placeholders always have a value. Optional content is a whole block, from `[If ...:]` to `[End if]`. Variant D has its own copy, below.

### Email

```
Subject: [Service name]: your [what's due] [due wording] ((due date))

Dear ((first name)) ((last name))

Your [what's due] [due wording] ((due date)).

[If the customer may have more than one:]
This is for ((record identifier)).
[End if]

You need to [action] on or before ((last date to act)).

How to [action]

[how to do it]

[If there's a cost:]
It costs [cost].
[End if]

[If they need anything to do it:]
You'll need:

[what you'll need]
[End if]

[If the service has confirmed a consequence:]
If you do not [action] in time

[consequence]
[End if]

[If the customer signed up for these reminders:]
You're getting this email because you signed up for reminders. To stop them, [unsubscribe route].
[End if]

[Sender]
```

### Text message

```sms
[Service name]: your [what's due] [due wording] ((due date)). [action short] on or before ((last date to act)): [how to do it]
```

### Letter

```
[If the service uses a reference:]
Reference: ((reference))
[End if]
((date))

Your [what's due] [due wording] ((due date))

[letter greeting]

Your [what's due] [due wording] ((due date)).

[If the customer may have more than one:]
This is for ((record identifier)).
[End if]

You need to [action] on or before ((last date to act)).

How to [action]

[how to do it]

[If there's a cost:]
It costs [cost].
[End if]

[If the service has confirmed a consequence:]
If you do not [action] in time

[consequence]
[End if]

[Sender]
```

### Variant D, a continuing duty

As a section in another message, like a decision or "What you applied for is on its way":

```
If anything changes

You need to tell us within [duty period] if [what counts as a change].

[how to tell us]

[If the service has confirmed a consequence:]
If you do not tell us

[consequence]
[End if]
```

As a standalone reminder, by email:

```
Subject: [Service name]: tell us if anything changes

Dear ((first name)) ((last name))

You need to tell us within [duty period] if [what counts as a change].

[how to tell us]

[If the service has confirmed a consequence:]
If you do not tell us

[consequence]
[End if]

You do not need to do anything if nothing has changed.

[Sender]
```

## Evidence

- **status:** supported by a main source, and seen in 2 services. Not yet tested with users
- **Service Manual**, "Planning and writing text messages and emails", describing transactional messages: "they paid for an annual service a year ago, and you're reminding them that it's about to expire". Its subscription example is an MOT reminder people sign up for, with an unsubscribe link. It says: "Never send subscription messages unless the user has explicitly asked for them" and "Always give users a way to unsubscribe"
- **HM Passport Office**, "How we communicate with customers" (published): "We send automated SMS text messages to a customer's mobile phone to remind them their passport (or their child's passport) is due to expire"
- **ICO**, "Direct marketing and the public sector": the quote under "kind of message"
- **unpublished design work in one service:** the moment occurs. No detail is recorded

### Evidence gaps

- the 2 Service Manual examples point in different directions: one is transactional, the other a subscription. Which a reminder is depends on the service. That's why "kind of message" is a checkpoint
