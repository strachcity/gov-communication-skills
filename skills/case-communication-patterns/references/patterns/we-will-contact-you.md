# Pattern: We'll contact you

Moment 4 in `../moments.md`. Draft, last revised 6 October 2026.

Lines starting with ">" are quotes. Lines starting with "Interpretation:" are ours. "How to use the baseline copy" in `../moments.md` explains the 2 kinds of placeholder.

## Purpose

To tell the customer about contact the service has planned, like a call, an appointment, an interview or a visit. It says when, how to recognise it's genuine, what to have ready, and how to change it.

## Trigger

The service arranges or books contact with the customer. The service context names the kinds of contact it uses.

## Customer situation

They need to be available, or go somewhere, at a set time. They may not know what it's for, or whether a call from an unknown number is genuine.

## Customer questions

- when, and how?
- what's it for?
- is it genuine?
- what should I have ready?
- what if the time doesn't work?
- what if I miss it?

## Core information

Every version of this message says:

- what kind of contact it is, like a call or an appointment
- when, as a date and time, or a time window
- for an appointment or visit, where

Emails, letters and status pages also say:

- how to recognise the contact is genuine
- what to have ready, if anything
- how to change or cancel it
- the reference

## Optional information

- what the contact is for, at the level the service has decided is safe
- how long it will take
- how to ask for support, like an interpreter, if the service offers it
- what happens if they miss it, if the service has confirmed it

## Placeholders

From the service context:

| Placeholder | What the service context supplies |
|---|---|
| [service name] | the name customers know the service by |
| [case] | the customer's word for their case |
| [kind of contact] | like "call", "appointment" or "visit" |
| [purpose] | what the contact is for, only at the level the service has confirmed |
| [what to have ready] | documents, information or anything else |
| [how to recognise it] | like the number the call will come from, or that the caller will give a reference |
| [how to change it] | the route, and any deadline for changing |
| [support available] | only if the service offers it |
| [missed consequence] | only if the service has confirmed it |
| [contact details] | how to get help, in the A to Z format |
| [sender] | who the message is from |
| [letter greeting] | from the service's letter template |

Filled for each message:

| Placeholder | Value |
|---|---|
| ((first name)) ((last name)) | the customer's full name |
| ((reference)) | the case reference |
| ((date and time)) | the date, and the time or time window, like "between 1pm and 3pm" |
| ((place)) | for an appointment or visit |
| ((date)) | the date of the letter |

## Variants

### A. A call is planned

Give the date and a time window. Say what number the call will come from, if the service has decided to.

### B. An appointment is booked

Confirm the date, time and place. The Service Manual's example of a transactional message confirms a booking in one text.

### C. A visit is planned

Someone from the service will visit the customer's home or premises. Say how to recognise them, like identification they'll show. This is core information for a visit, in every channel, because it protects the customer from someone pretending to be from the service.

```
[Service name]: we'll visit you on ((date and time)). Our officer will show [how to recognise it]. To change it, [how to change it].
```

With a long service name and a time window, this is close to 160 characters. Count it with real values.

### D. Contact is coming, but not at a set time

The service will contact the customer within a period, without a set time. Give the period as dates. Say how the contact will happen, and how to recognise it.

### Not this pattern

- another organisation will contact the customer, as part of passing the case on: use "We're waiting on someone else", variant E
- the contact already failed: use "We couldn't reach you"
- the customer needs to book or call: use "We need something from you", variant G

## Modifiers that apply

- **reminder:** before the contact, the same message again, shorter. This was moment 8 (see "Changes to the moments" in `../moments.md`)
- **delay:** if the contact has to move

## Common failure modes

- no way to check the contact is genuine, so the customer ignores the call or refuses the visit
- a time window too vague to plan around
- no way to change the time
- the purpose of an appointment, or its place, revealing something sensitive in a text or on an envelope
- not saying what to have ready, so the contact has to be repeated

## Privacy and policy checkpoints

Check these with `privacy-aware-communications`. Don't decide them here.

- **purpose and place:** could the purpose of the contact, or the place, reveal special category information, like a clinic address? This is high risk in texts, previews and envelopes
- **how to recognise it:** what the service tells customers to expect is a service decision. Publishing a caller number helps customers, but scammers can copy it
- **identity on the call:** the service needs to check the customer's identity before discussing the case. How is a service decision
- **when to call:** when the service can call is a service decision
- **arriving in time:** check the message can arrive before the contact. A letter can't announce a call tomorrow. If no channel the service uses can arrive in time, flag it
- **missed contact:** the consequence of missing it must come from the service context
- **kind of message:** a booking confirmation the customer asked for is a service message. Reminders the customer can opt out of may be optional service updates. See `kinds-of-message.md` in `privacy-aware-communications`

## Baseline copy

Leave out any line for something the service doesn't have.

### Text message

```
[Service name]: we'll call you on ((date and time)) about your [case]. To change this, [how to change it].
```

For an appointment:

```
[Service name]: your appointment is on ((date and time)) at ((place)). To change it, [how to change it].
```

### Email

```
Subject: [Service name]: your [kind of contact] on ((date and time))

Dear ((first name)) ((last name))

We'll [call you / see you / visit you] on ((date and time)) [at ((place))] about your [case].

Your reference number is ((reference)).

What to have ready

[what to have ready]

How to know it's us

[how to recognise it]

If the time does not work

[how to change it]

[If the service offers support:]
If you need support, like an interpreter, [support available].

[Sender]
```

### Letter

```
Reference: ((reference))
((date))

Your [kind of contact] on ((date and time))

[letter greeting]

We'll [call you / see you / visit you] on ((date and time)) [at ((place))] about your [case].

What to have ready

[what to have ready]

How to know it's us

[how to recognise it]

If the time does not work

[how to change it]

[If the service has confirmed it:]
If you miss it

[missed consequence]

If you need help, contact us:
[contact details]

[Sender]
```

The main sources don't cover how to greet or sign off a letter. Use the service's letter template, and flag it if there isn't one.

### Status page, behind sign-in

```
[Kind of contact]: ((date and time))

[Place: ((place))]

What to have ready
[what to have ready]

[Link: Change or cancel]
```

## Evidence

- **status:** supported by a main source, and seen in 2 services. Not yet tested with users
- **Service Manual**, "Planning and writing text messages and emails", its example of a transactional message: "Dial-a-Ride: Your vehicle will arrive in approximately [number of minutes] at [time of day] on [date]. Your driver today is [driver name]."
- **HM Passport Office**, "How we communicate with customers" (published): "We send automated SMS text messages to customers to remind them they have booked a counter appointment. We only do this if they have asked us during the application process." Its staff "must only phone a customer between the hours of 9am and 8pm", and must check whether the customer has said when they're not available
- **unpublished design work in one service:** the moment occurs. No detail is recorded

The call hours are one service's policy, not a rule for other services. That a published service sends appointment reminders only on request supports the "kind of message" checkpoint.

### Evidence gaps

- no published source shows a message telling a customer a call is planned
- no published source covers home or premises visits

### Adapted for invented services

Interpretation, from adapting this pattern for a permit, a benefit and a registration service on 6 October 2026:

- one service only uses letters and pointer texts, so nothing could announce a call the next day. The "arriving in time" checkpoint was added
- the visit variant had no text, and the text left out how to recognise the officer. Both are fixed
- the letter had a [missed consequence] placeholder but no line for it
- when another organisation will make the contact, the hand-off belongs in "We're waiting on someone else", variant E
