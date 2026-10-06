---
name: privacy-aware-communications
description: Check what a government customer communication reveals about a person, in each channel, against UK GDPR, ICO guidance and published government guidance. Produces a disclosure inventory, flags privacy questions with who should answer them, and can draft the communications part of a data protection impact assessment (DPIA) for DPO review. Use this whenever a letter, email, text message, voicemail or web page involves personal information, health or other sensitive information, a third party, or a choice of channel, even if the user only asks for a content review. It never decides a lawful basis or what an organisation may disclose.
---

# Privacy-aware communications

Helps you see what a communication reveals about a person, and whether the channel is suitable for it.

This skill is not legal advice. It applies published guidance and flags questions. Decisions about lawful basis, disclosure and acceptable risk belong to the organisation's data protection officer (DPO) and information assurance team.

## Sources

Use only public sources:

- UK GDPR and the Data Protection Act 2018
- ICO guidance
- GOV.UK guidance, including the Service Manual, the Service Standard, GOV.UK Notify and the Government Security Classifications
- departments' published guidance, as examples of how accountable organisations apply the law

Never use unpublished practice, workshop notes or "how we usually do it" as a source. `sources.md` lists every source and when it was checked.

The ICO says some of its guidance is under review following the Data (Use and Access) Act. Check `sources.md` dates before relying on anything.

## Reference files

- `references/principles.md`: always. The legal principles that bear on communications, quoted from the source
- `references/channels.md`: always. What each channel can expose, and a default position for each, derived from the sources
- `references/disclosure.md`: when a communication would tell someone something about a person, including the person themselves on a call, or a third party
- `references/dpia.md`: when asked for a DPIA, or for a privacy assessment of a set of messages

## What this skill does

### 1. Build a disclosure inventory

For each message and each channel, list what it reveals. Include what's visible before the message is opened:

- the sender name or sender ID
- the email subject line and preview
- anything visible through an envelope window or on the envelope
- the fact that the person received the message at all

Then list what the body reveals:

- identifiers, like names and references
- facts about the person's case
- special category information, like health, or anything that lets someone infer it
- information about a third party, or the fact that a third party is involved

Output the inventory as a table:

| Message | Channel | Visible before opening | Revealed in the message | Special category, or allows inference? | Position | Status |
|---|---|---|---|---|---|---|

### 2. Check it against the principles and the channel defaults

Use `references/principles.md` and `references/channels.md`. For each item, ask:

- is it needed for the purpose of this message? (data minimisation)
- is this channel secure enough for it, given the channel default? (security)
- could it reach the wrong person, like an out-of-date number or address? (accuracy and security)
- does it reveal or allow someone to infer special category information?

### 3. Apply confirmed decisions, flag the rest

If you were given a service pack, look for a decision that covers the item. Only apply it if its status is "confirmed", and cite its owner and date.

Otherwise, record the channel default as the position and mark it "needs confirmation". If the default doesn't settle it, flag the exact question and who should answer it, usually the DPO or information assurance team.

## Boundaries

Never decide:

- the lawful basis, or the condition for processing special category data
- whether an organisation may disclose something to a particular person
- whether a risk is acceptable
- whether a DPIA is legally required for a particular processing activity

Never infer an organisation's position from its published messages or practice. Two organisations doing the same thing is not evidence that it is required or lawful.

When the guidance is silent, say so. Do not invent a rule.

## Working with other skills

- `govuk-content` makes the wording clear. This skill decides nothing about wording, except where wording reveals information
- if a less revealing version would leave the customer without something they need, say so. It's a trade-off for the service to decide, not a reason to reveal more

## How you write to the user

Follow the same plain English rules as the content you check:

- short sentences, lead with the point
- no em dashes or en dashes
- bullets start lower case and have no full stop
- say clearly what is a quote, what is your interpretation, and what is a question for someone else
