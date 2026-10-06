# Pattern: We couldn't reach you

Moment 6 in `../moments.md`. Draft, last revised 6 October 2026.

Lines starting with ">" are quotes. Lines starting with "Interpretation:" are ours. "How to use the baseline copy" in `../moments.md` explains the 2 kinds of placeholder.

## Purpose

To tell the customer the service tried to contact them and couldn't, that the contact was genuine, and what happens now.

## Trigger

A call isn't answered, or a message can't be delivered, like an email that bounces or a letter that's returned. The service context names the event and what the service does next.

## Customer situation

They may have a missed call from a number they don't know, or no idea anyone tried to contact them. They may suspect a scam. If they didn't know the service needed them, they may worry something is wrong.

## Customer questions

- who was it?
- is it genuine?
- was it important?
- do I need to do anything, and by when?
- what happens if I don't?

## Core information

Every version of this message says:

- who tried to contact them, in a way they'll recognise
- what happens next: the service will try again, or the customer needs to get in touch
- if the customer needs to act, how, and by when

Emails, letters and status pages also say:

- how the customer can check the contact is genuine
- what happens if they don't get in touch, if the service has confirmed it
- the reference

Interpretation: a voicemail or text should not say why the service called. Saying it's genuine and how to get back in touch is enough.

## Optional information

- when the service will try again
- when the customer can call back, like opening times
- a direct route to the right person or team, if the general helpline can't help

## Placeholders

From the service context:

| Placeholder | What the service context supplies |
|---|---|
| [service name] | the name customers know the service by. Check it doesn't reveal something sensitive when heard on a voicemail |
| [caller name] | how the caller introduces themselves on a voicemail. Usually the service name. If that's sensitive, a neutral name, only if the service has decided one |
| [case] | the customer's word for their case |
| [retry plan] | when and how the service will try again, as the service has confirmed it |
| [how to get in touch] | the route to use, with when it's open. If only a general helpline exists, say what to tell them, like the reference |
| [how to check it's genuine] | like "find our number on GOV.UK", as the service has decided |
| [consequence] | what happens if they don't get in touch, as the service has confirmed it |
| [deadline rule] | how the deadline to get in touch is worked out |
| [sender] | who the message is from |
| [letter greeting] | from the service's letter template |

Filled for each message:

| Placeholder | Value |
|---|---|
| ((first name)) ((last name)) | the customer's full name |
| ((reference)) | the case reference |
| ((caller first name)) | if the service gives the caller's first name |
| ((time of next attempt)) | if the service will call again at a set time |
| ((deadline)) | the date to get in touch by |
| ((date)) | the date of the letter |
| ((dates of attempts)) | when the service tried, if the service includes this |

## Variants

### A. We'll try again

A first missed call. The service will call again. Say when, if it can.

If the service hasn't decided whether it tries again, don't choose between A and B. Keep [retry plan] as a placeholder and flag it.

### B. Please get in touch

The service has stopped trying, and needs the customer to contact it. Use the structure of "We need something from you", variant G, for the action: how to get in touch, by when, and what happens if they don't.

### C. A message couldn't be delivered

An email bounced, a text failed or a letter came back. Use a different channel the service holds. Ask the customer to check or update their contact details, without saying which details failed in a way that reveals them to someone else.

If the service has no other channel, say so. A banner on a status page behind sign-in may be the only route, and the customer may never see it. Flag this for the service.

For an organisation, a failed message often means the named contact has left. See "When the customer is an organisation" in `../moments.md`.

Interpretation: when a message fails, the details on file may belong to someone else now. Say less in the new message, not more.

### Not this pattern

- the service is asking for something in writing, with no missed contact: use "We need something from you"
- a call or appointment is being arranged: use "We'll contact you"

## Modifiers that apply

- **final reminder:** if the customer still hasn't got in touch and there's a confirmed consequence. See "Modifiers" in `../moments.md`

## Common failure modes

- saying why the service called in a voicemail or text
- "please call us" with no way to check it's genuine, so it reads like a scam
- sending the customer to a general helpline that can't help with this
- a number to call back that the customer can't verify
- no deadline or consequence, when there is one
- a consequence in the final letter that earlier attempts never mentioned

## Privacy and policy checkpoints

Check these with `privacy-aware-communications`. Don't decide them here.

- **voicemail:** anything about the case in a voicemail is high risk, because others may hear it. The lower-risk version says who called and how to get back in touch
- **service name:** could the name of the service reveal something sensitive when heard on a voicemail or seen on a lock screen?
- **identity on the call back:** the service needs to check the caller's identity before discussing the case. How is a service decision
- **when to call:** when the service calls, and how many times, is a service decision. Don't infer it
- **failed delivery:** contact details that fail may now reach someone else. Check before using another channel
- **consequence:** what happens if the customer doesn't get in touch must come from the service context

## Baseline copy

Leave out any line for something the service doesn't have.

### Voicemail

Call scripts are out of scope, but a voicemail is a message, so this is the lowest-risk baseline:

```
Hello, this is [caller name] calling for ((first name)) ((last name)). We need to speak to you. [We'll call you again at ((time of next attempt)).] You can also call us on [direct number], [opening times]. Thank you.
```

Interpretation: don't give the case reference or the reason for the call. Whether to give the caller's first name is a service decision.

### Text message

```
[Service name] tried to call you today. We need to speak to you about your [case]. [We'll call again at ((time of next attempt)). / Call us on [direct number], [opening times].]
```

### Email

```
Subject: [Service name]: we tried to call you

Dear ((first name)) ((last name))

We tried to call you about your [case] but could not reach you.

Your reference number is ((reference)).

What you need to do

[Call / Contact] us [on or before ((deadline))]:
[how to get in touch]

To check this email is genuine, [how to check it's genuine].

If you do not get in touch

[consequence]

[Sender]
```

### Letter

```
Reference: ((reference))
((date))

We need to speak to you about your [case]

[letter greeting]

We tried to contact you about your [case], but could not reach you.

Contact us [on or before ((deadline))]:
[how to get in touch]

Have your reference number ready.

To check this letter is genuine, [how to check it's genuine].

If you do not contact us

[consequence]

[Sender]
```

The main sources don't cover how to greet or sign off a letter. Use the service's letter template, and flag it if there isn't one.

## Evidence

- **status:** seen in 2 services. No main source describes this need. Not yet tested with users
- **HM Passport Office**, "How we communicate with customers" (published):
  - after a missed call, staff "leave a voicemail to confirm you will call again in 2 hours", making no more than 3 calls in 24 hours, then send a letter
  - its voicemail says "I need to speak with you directly, so please do not contact our helpline, as they will not be able to advise you"
  - its third voicemail says the service will send a letter or email, and "You may need to check your spam or junk email folder"
  - if an email returns an "undeliverable message", staff "must contact the customer (or referee) by phone to confirm their email address"
  - "If you cannot identify a customer, you must not tell them: an application exists"
- **unpublished design work in one service:** the moment occurs. No detail is recorded

The call times and number of attempts are one service's policy. They're evidence that services set these rules, not rules for other services.

### Evidence gaps

- no published source shows a text or email sent after a missed call
- the evidence for variant C comes from one published service only

### Adapted for invented services

Interpretation, from adapting this pattern for a permit, a benefit and a registration service on 6 October 2026:

- one service's name would reveal a sensitive subject on a voicemail. [caller name] was added, with the trade-off flagged in `../moments.md`
- one service hadn't decided whether it tries again. The pattern now says not to choose between A and B
- the email assumed a deadline. It's now optional
- one service only had a general helpline. [how to get in touch] now covers that
- one service had only email and a status page, so variant C had no other channel. The pattern now says to flag this
- for a business, a bounced email often meant the named contact had left
