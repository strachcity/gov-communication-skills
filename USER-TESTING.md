# User testing the patterns

A test pack for a user researcher. It tests the first 3 patterns with people, starting with "We're waiting on someone else", where privacy and the customer's need pull hardest against each other.

Written 6 October 2026. No testing has been done yet. Until it has, every pattern's evidence status stays below "tested with users".

## What we want to learn

1. Can people understand a "waiting" message that doesn't say who the service is waiting on?
2. Does saying more about the third party change what people understand or do?
3. Do people understand that they don't need to do anything?
4. Do people think the delay is their fault?
5. Do people trust a short text message enough to act on it, or do they suspect it's a scam?
6. Do people read "We've received it" as "approved"?
7. In "We need something from you", do people notice the deadline and the consequence?

## Hypotheses

- a "waiting" message that commits to a next update date reduces the urge to phone, whether or not it names the third party
- the least revealing description ("someone else") is understood, but makes some people think the delay is theirs
- describing the third party by role helps understanding, but people worry about what the message reveals on a shared phone
- people don't confuse "received" with "approved" when the message says what happens next
- stating the consequence in the first request means more people act before the deadline

These are ours. They're there to be disproved.

## Who to test with

- 8 to 12 people per round, from the public
- people who have recently applied for something, or waited on a decision, from any public service
- include people who:
  - share a phone or a computer with others
  - rarely use email
  - use a screen reader or screen magnifier
  - have low confidence reading English
  - are under stress, like waiting on a decision that matters to them

Don't recruit from one service's customers only. The patterns are generic, so test them with an invented service.

## Method

Moderated sessions, about 30 minutes each, in person or remote.

Test understanding, not preference. Ask people what the message means and what they'd do, before asking what they think of it.

1. Set the scene with the scenario below.
2. Show one message at a time, on the device it would arrive on.
3. Ask the comprehension questions before any opinion questions.
4. Rotate the order of the versions between participants.
5. At the end, show the versions side by side and ask which they'd want, and why.

## Scenario

Use an invented service:

> You applied for a permit to sell food from a stall at your local market. You applied online 3 weeks ago. You've just received this message.

## Stimuli

The messages are filled from the baseline copy. Each version changes one thing.

### Waiting, text message

Version A, the third party not described:

```
Your application is waiting for information from someone else. You do not need to do anything. We'll update you by 27 October 2026.
```

Version B, described as another organisation:

```
Your application is waiting for information from another organisation. You do not need to do anything. We'll update you by 27 October 2026.
```

Version C, no update date:

```
Your application is waiting for information from someone else. You do not need to do anything. Track it: https://www.gov.uk/check-market-permit
```

### Waiting, email

Version D, the third party described by role:

```
Subject: Market permits: update on your application

Dear Sam Taylor

We're waiting for information we need from the council's environmental health team before we can continue with your application.

You do not need to do anything now.

Your reference number is MKT-204816.

What happens next

We'll update you by 27 October 2026, or sooner if we get what we need.

You can check the progress of your application at https://www.gov.uk/check-market-permit

If you need help, call 0300 000 1234, Monday to Friday, 9am to 5pm.

Market Permits Service
```

Version E: the same email, with "someone else" instead of "the council's environmental health team".

### Received, text message

```
We've received your application. Reference: MKT-204816. You do not need to do anything now. Track it: https://www.gov.uk/check-market-permit
```

### Need something, email

Use the "We need something from you" baseline email, asking for proof of address on or before a date, with the consequence that the application will be closed.

## Questions

After each message:

- in your own words, what is this message telling you?
- what's happening with your application?
- do you need to do anything? What?
- why do you think it's taking this long?
- when will you next hear something?
- what would you do after reading this?
- if this arrived on a phone you share, would you be comfortable with someone else seeing it?

For text messages:

- who do you think sent this?
- would you trust it? What would you check?

For the received message:

- has your application been approved?

For the request:

- what do you need to send, and by when?
- what happens if you don't?

## What to record

- for each version: whether the person correctly said what's happening, whether they need to act, and when they'll hear next
- whether they said they'd phone the service
- whether they thought the delay was their fault
- whether they suspected the text was a scam, and why
- anything they found worrying to have on a shared device

## Using the results

- record findings in generic words in the evidence section of each pattern, with the date and the number of participants
- a pattern only moves to "tested with users" when its core information has been tested in at least one round
- if a finding changes the baseline copy, change it in its own commit, and say what was tested
- never commit participants' names, recordings, notes or anything that could identify them. This repository is public
- if a finding is about one service's users rather than the pattern, it belongs in that service's own context, not here
