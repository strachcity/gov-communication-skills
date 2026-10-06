# Pattern: We need something from you

Moment 5 in `../moments.md`. Draft, last revised 6 October 2026.

Lines starting with ">" are quotes. Lines starting with "Interpretation:" are ours. "How to use the baseline copy" in `../moments.md` explains the 2 kinds of placeholder.

## Purpose

To get the customer to provide something the case cannot progress without. It tells them exactly what, how, by when, and what happens if they don't.

## Trigger

The service cannot continue until the customer provides information, evidence or a replacement, or takes an action, like calling or booking. The service context names the event.

## Customer situation

Their case has stopped until they act. They may not know why, what counts, or how to provide it.

## Customer questions

- what exactly do you need?
- how do I give it to you?
- by when?
- what happens if I don't, or can't?
- what happens after I've done it?
- is this message genuine?

## Core information

The Service Manual says to:

> make it clear what you need the user to do and include any deadlines

> say what will happen if they don't do what you're asking

> explain what you'll do next and when they'll hear from you

So every full version of this message says:

- exactly what is needed, specific enough to act on
- how to provide it
- the deadline, as a date, if there is one. Use "on or before ((deadline))"
- what happens if they don't, if there's a consequence
- what happens after the service gets it
- the reference, so they can include it

Interpretation: state the consequence in the first request, not only in a final reminder. The Service Manual asks for it in every request, and a customer who learns of it late has less time to act.

## Optional information

- why it's needed, only where it helps the customer act or provide the right thing. Don't explain policy
- more than one way to provide it
- what to do if they cannot provide it
- how to get help

## Placeholders

From the service context:

| Placeholder | What the service context supplies |
|---|---|
| [service name] | the name customers know the service by |
| [case] | the customer's word for their case, like "application" |
| [what we need] | specific enough to act on. Check the privacy checkpoints first. If it changes from case to case, write it as ((what we need)), filled for each message |
| [short description] | a neutral description for a text, subject line or first line |
| [how to provide it] | each route, like an upload page, a postal address or a phone call |
| [upload URL] | a full GOV.UK web address, if there's an upload route |
| [deadline rule] | how the deadline is worked out, like "14 days from the date of the request". Turned into a date for each message |
| [consequence] | what happens if they don't act, as the service has confirmed it |
| [next step] | what happens after the service gets it |
| [timescale] | when that will happen |
| [contact details] | how to get help, in the A to Z format, like "Telephone: 0300 000 0000" with opening times on separate lines |
| [sender] | who the message is from |
| [letter greeting] | from the service's letter template |

Filled for each message:

| Placeholder | Value |
|---|---|
| ((first name)) ((last name)) | the customer's full name, or the named contact's |
| ((reference)) | the case reference |
| ((deadline)) | the date, worked out from [deadline rule] |
| ((date)) | the date of the letter |

## Variants

### A. First request

Use the baseline copy below.

### B. Request after another event

Something has just happened, like something sent was incomplete, someone else couldn't help, or a decision needs a follow-up action. Start with one sentence saying what happened, then make the request. Don't explain the process behind it.

### C. Replacement needed

Something the customer sent or chose can't be used. Say what can't be used, and what's needed instead, at the level of detail the customer needs to get it right. Don't imply fault unless the service has decided to.

### D. No deadline

Only use this when the service context confirms there's no deadline. If the deadline just isn't known yet, keep ((deadline)) and flag it.

Replace the deadline line with the reason to act, like "We cannot continue with your [case] until we get this." If the service has confirmed what happens while it waits, use that as the consequence.

### E. Formal or legal consequence

The request has legal effect, or not acting has a legal consequence. The service context must say so. Flag it for legal review. The channel and some wording may be fixed by law, and "must" may be correct here.

### F. More than one thing needed

List each thing as a bullet or numbered step. Say whether they can send them separately.

### G. An action, not something to send

The customer needs to call, book or confirm something, rather than send it. Change the headings and verbs to match, like "How to give us your details" and "Call us on or before ((deadline))". If they need to call, say what to have ready.

## Modifiers that apply

- **reminder:** the same request again, after no reply. Start with "We asked you on ((date asked)) to [action]." Keep the same deadline, if there is one, unless the service has changed it
- **final reminder:** the last request before the consequence. Put the deadline and the consequence first. Don't introduce a consequence that wasn't in the earlier messages without flagging it

See "Modifiers" in `../moments.md`.

## Common failure modes

- a vague request, like "send us further information"
- a vague subject line, like "we need something from you"
- asking the customer to reply with personal information by email or text. The Service Manual says to "avoid making requests for personal information, like a user's date of birth"
- a deadline written as a period, like "within 14 days", instead of a date
- the consequence only appearing in the final reminder
- "must" for something that isn't a legal requirement. GOV.UK guidance uses "must" for legal requirements and "need to" for others
- not saying what happens after they've done it
- a text message that tries to carry the whole request
- no route for people who cannot provide what's asked

## Privacy and policy checkpoints

Check these with `privacy-aware-communications`. Don't decide them here.

- **what is needed:** could describing it reveal special category or sensitive information, like the kind of evidence implying a health condition? If so, keep it out of texts, sender names, subject lines and first lines
- **return route:** is each route secure enough for what's being sent? Don't ask for sensitive information, like bank details, by reply email or text. A route that every customer can't use, like email for customers who get letters, needs an alternative
- **is it genuine:** requests for personal or financial information are what scams look like. Say how the customer can check the request is genuine, like calling a number they can find on GOV.UK. How to do this is a service decision
- **consequence:** the consequence must come from the service context. Never infer it
- **deadline rule:** if the service gives a rule rather than a date, check whether it's calendar or working days, and what date the request counts from, especially for a letter
- **legal effect:** is the request a formal notice? This is a service fact
- **must or need to:** depends on whether there's a legal requirement. If the service context doesn't say, use "need to" and flag it

## Baseline copy

Leave out any line for something the service doesn't have. Don't force every part into every channel.

### Email

```
Subject: [Service name]: you need to send us [short description]

Dear ((first name)) ((last name))

You need to send us [what we need] so we can continue with your [case].

Send it on or before ((deadline)).

Your reference number is ((reference)).

What to send

[what we need, as a list if there's more than one thing]

How to send it

[how to provide it]. Include your reference number.

If you do not send it

[consequence]

What happens next

When we get it, we'll [next step] by [timescale].

If you cannot send it, or you need help, contact us:
[contact details]

[Sender]
```

If [short description] would reveal something sensitive in the subject line, use "[Service name]: action needed on your [case]".

### Text message

A pointer, when what's needed is sensitive or needs explaining:

```
You need to send us something for your [case] by ((deadline)). We've [emailed you / sent you a letter] with details. Reference: ((reference))
```

Self-contained, when what's needed and how to send it are short and not sensitive:

```
You need to send us [short description] for your [case] on or before ((deadline)). Send it at [upload URL]
```

Send a pointer text only once the email or letter is likely to have arrived. Interpretation: avoid sending a text and an email at the same moment unless the text adds something. The Service Manual says to avoid it "unless there's a very good reason".

See "Text messages" in `../moments.md` for counting characters and sender IDs.

### Letter

```
Reference: ((reference))
((date))

You need to send us [short description]

[letter greeting]

We need [what we need] so we can continue with your [case].

Send it on or before ((deadline)).

What to send

[what we need, as a list if there's more than one thing]

How to send it

[how to provide it]. Include your reference number: ((reference)).

If you do not send it

[consequence]

What happens next

When we get it, we'll [next step] by [timescale].

If you cannot send it, or you need help, contact us:
[contact details]

[Sender]
```

The main sources don't cover how to greet or sign off a letter. Use the service's letter template, and flag it if there isn't one.

### Status page, behind sign-in

```
Status: Action needed

You need to send us [what we need].

Send it on or before ((deadline)).

[Button or link: Send [short description]]

If you do not send it
[consequence]
```

Put the action at the top of the page, above any case history.

## Evidence

- **status:** supported by a main source, and seen in 2 services. Adapted for 3 invented services. Not yet tested with users
- **Service Manual**, "Planning and writing text messages and emails": the 3 quotes under "Core information"
- **HM Passport Office**, "How we communicate with customers" (published): "When customers do not send us the documents we need, we will send them automatic reminders through text message or email. If a customer still does not send us their documents, we will withdraw their application." It also sends automated messages when "we need a new photo" and when "it is time to send in their documents (for example, after the digital referee completes their section)"
- **unpublished design work in one service:** the moment occurs. No detail is recorded

### Tested against the evidence

Interpretation, from adapting this pattern back to each source:

- a published service asks for a replacement when something sent can't be used. The first draft had no variant for this, so variant C was added
- a published service asks for documents after another step finishes. Variant B covers it
- a published service's reminders lead to withdrawal. That supports stating the consequence early, and the final reminder modifier
- a request text can be self-contained when the ask isn't sensitive, so there are 2 text versions
- customers may need a choice of return routes, so [how to provide it] allows more than one
- renewal reminders also looked like this pattern, but they don't block a live case. They stay with moment 9, "You need to act before a date"

### Adapted for invented services

Interpretation, from adapting this pattern for a permit, a benefit and a registration service on 6 October 2026:

- one service collects details by phone only, which fought the "send" wording in 5 places. Variant G was added, and [how to send it] became [how to provide it]
- a request for bank details needs a way to check it's genuine. The "is it genuine" checkpoint was added
- one service gave a deadline rule, not a date. [deadline rule] and its checkpoint were added
- "no deadline" and "deadline not known yet" were being confused. Variant D now separates them
- the deadline sat in different places in the email and letter. It now comes straight after the first line in both
- the subject line "we need something from you" was too vague, so it now names what's needed, with a neutral fallback
