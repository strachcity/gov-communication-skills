# Pattern: Your case has moved on

Moment 2 in `../moments.md`. Draft, last revised 6 October 2026.

Lines starting with ">" are quotes. Lines starting with "Interpretation:" are ours. "How to use the baseline copy" in `../moments.md` explains the 2 kinds of placeholder.

This pattern merges 2 earlier moments, "Work has started" and "Something has changed". See "Changes to the moments" in `../moments.md`. It's deliberately narrow.

## Purpose

To tell the customer their case has reached a stage that changes what they can expect, when they'd otherwise wonder whether anything is happening.

## When to send it

Send it only if at least one of these is true:

- it changes when the customer will hear next, or what happens next
- the service has told customers it will update them at this stage
- there's been a long gap since the last message, and the customer is likely to get in touch to ask

Otherwise, no message is needed. See "No message needed" in `../moments.md`.

The Service Manual says:

> Only send email or text messages when it meets a user need.

And that transactional messages:

> reassure the user that the service is working as they expect it to. They reduce anxiety and stop users contacting your service needlessly.

## Trigger

A stage of the case starts or finishes, like work starting after a queue, or a check finishing. The service context names the stages that customers are told about.

## Customer situation

They know the service has their case, but haven't heard anything for a while.

## Customer questions

- is anything happening?
- what happens now, and when?
- do I need to do anything?

## Core information

Every version of this message says:

- what has changed, in terms of what it means for the customer, not the service's process
- what happens next, and when
- whether they need to do anything. Usually they don't

## Optional information

- how to track progress
- the reference

## Placeholders

From the service context:

| Placeholder | What the service context supplies |
|---|---|
| [service name] | the name customers know the service by |
| [case] | the customer's word for their case |
| [what's changed] | the change, in customer terms, as the service has confirmed it can be described |
| [next step] | what happens next, from the customer's view |
| [timescale] | when, only if the service can meet it |
| [tracking URL] | a full GOV.UK web address |
| [sender] | who the message is from |

Filled for each message:

| Placeholder | Value |
|---|---|
| ((first name)) ((last name)) | the customer's full name |
| ((reference)) | the case reference |

## Variants

### A. Work has started

Work starts after a gap since the customer was told it was received. If work starts straight away, use "We've received it", variant C, instead.

```
We've started working on your [case]. We'll [next step] by [timescale].
```

### B. A stage is complete

A stage that the customer knows about has finished. Say what happens next. Never imply the outcome.

```
We've finished [what's changed]. Next, we'll [next step] by [timescale].
```

### Not this pattern

- a wait for someone else has ended: use "We're waiting on someone else", variant C
- the case has an outcome: use "We've made a decision"
- the customer needs to act: use "We need something from you"
- the case moved between teams, and nothing changes for the customer: no message is needed

## Modifiers that apply

- **delay:** if the next step will take longer than the customer was told

## Common failure modes

- naming internal teams, stages or checks the customer doesn't know about. The Service Manual says: "Don't explain back-end processes or policy."
- an update with no meaning, like "Your application has progressed"
- implying the outcome, like a finished check read as approval
- sending updates so often that the customer stops reading them
- revealing a check the service shouldn't disclose, like a fraud or security check

## Privacy and policy checkpoints

Check these with `privacy-aware-communications`. Don't decide them here.

- **naming the stage:** could the name of the stage reveal something sensitive, like a medical assessment or a fraud check? Naming it is high risk in texts and previews
- **checks:** whether a check can be mentioned at all is a service decision. One published service tells its staff not to mention identity or fraud concerns in letters
- **kind of message:** a progress update the customer didn't ask for may be an optional service update. Whether customers can stop them is a service decision. See `kinds-of-message.md` in `privacy-aware-communications`

## Baseline copy

Leave out any line for something the service doesn't have.

### Email

```
Subject: [Service name]: update on your [case]

Dear ((first name)) ((last name))

[What's changed, as in variant A or B.]

You do not need to do anything now.

Your reference number is ((reference)).

You can check the progress of your [case] at [tracking URL]

[Sender]
```

### Text message

```
[Service name]: we've started working on your [case]. We'll [next step] by [timescale]. You do not need to do anything.
```

### Status page, behind sign-in

```
Status: [stage name, as customers know it]

[What's changed.]

What happens next
We'll [next step] by [timescale].
```

Interpretation: a status page may be enough on its own for this moment, without an email or text. That's a service decision.

## Evidence

- **status:** seen in 2 services, counting both earlier moments. The need is supported by the Service Manual's description of transactional messages. Not yet tested with users
- **Service Manual**, "Planning and writing text messages and emails": the quotes under "When to send it"
- **HM Passport Office**, "How we communicate with customers" (published): tells customers when "we have finished automatic identity checks". Its staff must not add "anything in the letter about Public Protection concerns such as identity or fraud"
- **unpublished design work in one service:** both "work has started" and a change of stage occur. No detail is recorded

### Why the 2 moments were merged

Interpretation, 6 October 2026:

- "Work has started" had evidence from 1 unpublished service. Its message differed from "We've received it" only when there's a gap between receipt and work starting
- most of the evidence for "Something has changed" was a wait ending, which is now part of "We're waiting on someone else"
- what's left of both is the same message: the case has reached a stage that changes what the customer can expect
- the "When to send it" test keeps it narrow, so it doesn't become a reason to send updates about internal steps

### Evidence gaps

- no published source shows a "work has started" message
- the only published evidence for a stage finishing is one service's identity check message

### Adapted for invented services

Interpretation, from adapting this pattern for a permit, a benefit and a registration service on 6 October 2026. See `evals/results.md`.
