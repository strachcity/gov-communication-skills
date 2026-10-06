# Pattern: We've made a decision

Moment 7 in `../moments.md`. Draft, last revised 6 October 2026.

Lines starting with ">" are quotes. Lines starting with "Interpretation:" are ours. "How to use the baseline copy" in `../moments.md` explains the 2 kinds of placeholder.

## Purpose

To tell the customer the outcome of their case, what it means for them, and what they can do next. It also covers a case that ends without a decision on its merits, like an application treated as withdrawn.

## Trigger

The service makes a decision on the case, or closes it without one. The service context names the event and the possible outcomes.

## Customer situation

They've been waiting for this, sometimes for a long time. The outcome may matter a great deal to them. If it's not what they wanted, they may be upset, and need to know quickly what they can do.

## Customer questions

- what's the outcome?
- what does it mean for me?
- what happens now, and when?
- why was this decided?
- can I challenge it, and by when?
- is this the end of my case?

## Core information

Every full version of this message says:

- the outcome, first, in plain words
- what it means for the customer
- what happens next, or that this is the end of the process
- what they can do if they disagree, if a route exists and the service has confirmed it
- the reference

The Service Manual says to:

> explain what you'll do next and when they'll hear from you - if you won't be contacting them again, make it clear that it's the end of the process

Interpretation: put the outcome in the first sentence, even when it's not what the customer wanted. Background and reasons come after it.

## Optional information

Each needs confirmation from the service context. Some may be required by law for a particular service, which is a service fact.

- the reasons for the decision
- the date the decision takes effect
- conditions attached to the outcome
- the date of the decision, if it matters for a challenge deadline
- where to get independent help or advice

## Placeholders

From the service context:

| Placeholder | What the service context supplies |
|---|---|
| [service name] | the name customers know the service by |
| [case] | the customer's word for their case |
| [outcome] | the service's confirmed wording for each possible outcome, like "approved" or "refused". Never choose decision words for the service |
| [what it means] | what the outcome means for the customer, in the service's confirmed words |
| [next step] | what happens next, or [end of process] |
| [challenge route] | how to challenge the decision, if there is one, like a review or an appeal |
| [challenge deadline rule] | how the deadline for a challenge is worked out |
| [reasons] | only if the service has confirmed how reasons are given |
| [restart route] | for variant D, how to apply again or restart, if the service allows it |
| [contact details] | how to get help, in the A to Z format |
| [sender] | who the message is from |
| [letter greeting] | from the service's letter template |

Filled for each message:

| Placeholder | Value |
|---|---|
| ((first name)) ((last name)) | the customer's full name, or the named contact's |
| ((reference)) | the case reference |
| ((decision date)) | the date of the decision |
| ((challenge deadline)) | the date, worked out from [challenge deadline rule] |
| ((reasons for this case)) | the reasons, if the service gives them for each case |
| ((date)) | the date of the letter |

## Variants

### A. The customer gets what they asked for

Use the baseline copy. Say what happens next, like what they'll receive. If something will be sent or issued later, the follow-up uses "What you applied for is on its way".

### B. The customer doesn't get what they asked for

State the outcome in the first sentence. Don't open with "Unfortunately" or an apology, then bury the outcome. Give the reasons in plain words, if the service gives them. Put the challenge route and its deadline straight after the reasons.

Interpretation: this is the version most likely to need a letter or a page behind sign-in, and the least suited to a self-contained text. See the checkpoints.

### C. Part of what they asked for, or with conditions

Say what they've got, then what they haven't, then the conditions. Keep each in its own short paragraph or list.

### D. Closed without a decision

The case ends without a decision on its merits, for example because the customer didn't reply, asked to stop, or no longer needs it. This was moment 11 (see "Changes to the moments" in `../moments.md`).

- say the case is closed, and why, in one sentence
- say what this means, like whether anything they paid or sent is returned. Only from the service context
- say what they can do now, like apply again, if the service allows it
- never present it as a refusal on the merits

Interpretation: if the case was closed because the customer didn't reply, the earlier requests should have said this could happen. If they didn't, flag it. See the final reminder modifier.

### E. Decision with an action

The customer needs to do something because of the decision, like pay, confirm or send something. Give the outcome first, then use "We need something from you" for the action, in the same message.

### F. Formal notice

The decision has legal effect, or the law sets how it's given. The service context must say so. Flag it for legal review. The channel, the wording and what must be included may be fixed by law. Don't adapt the wording of a formal notice without that review.

### Not this pattern

- a stage of the case has finished but there's no outcome yet: use "Your case has moved on"
- what was decided is being sent or issued: use "What you applied for is on its way"

## Modifiers that apply

- **delay:** if the decision is later than the customer was told, before the decision is made. See "Modifiers" in `../moments.md`

## Common failure modes

- the outcome buried below background, reasons or an apology
- decision words the service hasn't confirmed, like "approved" when the legal outcome is something else
- reasons in legal or policy language the customer can't act on. The Service Manual letters page says research found legal jargon especially confusing
- a challenge deadline written as a period, like "within 1 month", instead of a date
- no route for someone who disagrees, when one exists
- not saying whether this is the end of the process
- a text or email that arrives before the formal notice it refers to
- adding a feedback request or promotion to a formal notice

## Privacy and policy checkpoints

Check these with `privacy-aware-communications`. Don't decide them here.

- **legal effect:** is this decision a formal notice? What must it contain, and which channel must it use? This is a service fact. A message missing from the service context's list of formal communications is not confirmation it has none
- **decision words:** the outcome must use the service's confirmed wording. Never infer it from published content
- **reasons:** whether and how reasons are given is a service decision. Reasons can reveal special category information, or information about a third party
- **challenge route:** the route, who can use it, and the deadline must come from the service context. Never infer them
- **preview and lock screen:** an outcome in a subject line, first line or text can reveal sensitive information. Refusals are high risk in previews
- **who receives it:** if someone acts for the customer, who gets the decision is a service decision
- **pointer texts:** if a text points to a formal notice, send it only after the notice is likely to have arrived

## Baseline copy

Leave out any line for something the service doesn't have. A formal notice may need different wording entirely.

### Letter

```
Reference: ((reference))
((date))

[Outcome headline, like "Your [case] has been [outcome]"]

[letter greeting]

We've [outcome] your [case]. [what it means]

[Reasons, if given:]
Why we made this decision

((reasons for this case))

What happens next

[next step]

[If there's a challenge route:]
If you disagree with this decision

You can [challenge route]. You need to do this on or before ((challenge deadline)).

If you need help, contact us:
[contact details]

[Sender]
```

The main sources don't cover how to greet or sign off a letter. Use the service's letter template, and flag it if there isn't one.

### Email

```
Subject: [Service name]: we've made a decision on your [case]

Dear ((first name)) ((last name))

We've [outcome] your [case]. [what it means]

Your reference number is ((reference)).

[Reasons, if given:]
Why we made this decision

((reasons for this case))

What happens next

[next step]

[If there's a challenge route:]
If you disagree with this decision

You can [challenge route]. You need to do this on or before ((challenge deadline)).

If you need help, contact us:
[contact details]

[Sender]
```

Interpretation: the subject line says a decision has been made, not what it is. The outcome stays out of previews unless the service decides otherwise.

### Text message

A pointer, by default:

```
We've made a decision on your [case]. We've [emailed you / sent you a letter] with details. Reference: ((reference))
```

Self-contained, only for an outcome the service has decided can go in a text, and never for a formal notice:

```
Your [case] has been [outcome]. [next step, in a few words]. Reference: ((reference))
```

### Status page, behind sign-in

```
Status: [outcome]

We've [outcome] your [case]. [what it means]

What happens next
[next step]

If you disagree
You can [challenge route] on or before ((challenge deadline)).
```

### Variant D, closed without a decision, email body

```
We've closed your [case] because [reason for closing].

[What this means, like what happens to anything you paid or sent.]

If you still want to [what they applied for], you can [restart route].

Your reference number is ((reference)).
```

## Evidence

- **status:** seen in 2 services. A main source supports saying when it's the end of the process. Not yet tested with users
- **Service Manual**, "Planning and writing text messages and emails": the quote under "Core information"
- **Service Manual**, "Writing effective letters": research found legal jargon especially confusing, and there "might also be a security or legislative reason for sending a letter"
- **HM Passport Office**, "How we communicate with customers" (published): sends an automated message "to tell them we have approved their application". For closure: "If a customer still does not send us their documents, we will withdraw their application", and "If there is no response to the Contact letter, you must deal with the application using the Withdrawing passport applications guidance"
- **unpublished design work in one service:** the moment occurs. No detail is recorded

### Evidence gaps

- no published source we've found shows how a government service words a refusal, or its reasons, in a customer message
- no published source shows how services word a challenge route in a message
- the closure evidence comes from one published service only

### Adapted for invented services

Interpretation, from adapting this pattern for a permit, a benefit and a registration service on 6 October 2026. See `evals/results.md`.
