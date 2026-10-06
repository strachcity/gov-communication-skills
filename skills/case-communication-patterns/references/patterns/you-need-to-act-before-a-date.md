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
| [consequence] | what happens if they don't act, as the service has confirmed it. "Must" only if there's a legal requirement |
| [cost] | only if confirmed |
| [unsubscribe route] | for variant D |
| [sender] | who the message is from |
| [letter greeting] | from the service's letter template |

Filled for each message:

| Placeholder | Value |
|---|---|
| ((first name)) ((last name)) | the customer's full name |
| ((due date)) | the date |
| ((what it's for)) | like a vehicle or a property, if the customer has more than one |
| ((date)) | the date of the letter |

## Variants

### A. A renewal is due

Say what's due, the date, and how to renew.

### B. Something is expiring

There may be nothing to renew. Say what's expiring and when, and what happens after.

### C. A regular obligation is due

Like an annual return or report. Say what's needed and by when.

### D. The customer signed up for reminders

The Service Manual calls these subscription messages. Always give a way to unsubscribe.

### Not this pattern

- the case can't progress until the customer acts: use "We need something from you"
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

Leave out any line for something the service doesn't have.

### Email

```
Subject: [Service name]: your [what's due] is due on ((due date))

Dear ((first name)) ((last name))

Your [what's due] [for ((what it's for))] is due on ((due date)).

How to [renew / do it]

[how to do it]

[You'll need:
[what you'll need]]

If you do not [renew / do it] on or before ((due date))

[consequence]

[For variant D:]
You're getting this email because you signed up for reminders. To stop them, [unsubscribe route].

[Sender]
```

### Text message

```
[Service name]: your [what's due] is due on ((due date)). [Renew / Do it] at [how to do it]
```

### Letter

```
((date))

Your [what's due] is due on ((due date))

[letter greeting]

Your [what's due] [for ((what it's for))] is due on ((due date)).

How to [renew / do it]

[how to do it]

If you do not [renew / do it] on or before ((due date))

[consequence]

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

### Adapted for invented services

Interpretation, from adapting this pattern for a permit, a benefit and a registration service on 6 October 2026. See `evals/results.md`.
