# Email telling the customer a third party has been asked for information

Tests the skill on a realistic draft that is already mostly good. It should find the few real issues, leave the good parts alone, and flag the vague "a third party" without deciding what to reveal.

Adapted from a draft in a service design prototype. The service name, reference format and sender have been replaced with placeholders, so it does not depend on any one service.

- **skill:** govuk-content
- **task:** review
- **channel:** email
- **service:** none

## Prompt

Can you review this email template before we test it with users?

## Input

```
Subject: We've asked a third party for information about your application

Dear [firstname lastname]

We've asked a third party for information about your application.

Your reference number is:
AB12345678

What happens next

We'll update you when they reply. This can take [X weeks]. You do not need to do anything now.

If we haven't heard back by [date], we'll let you know what happens next.

Track your application: https://www.gov.uk/[service-path]

If you need to contact us, call [phone number] ([opening hours]) and quote your reference number.

Regards,
[Service name]
```

## A correct response must

- output only the 6-column table, or a single line if nothing needs to change
- flag "haven't" and suggest "have not"
- flag that no main source covers the email sign-off, using the "Confused / Uncertain?" column, rather than stating a rule
- flag that "a third party" may not tell the reader what they need to know, and say that how much to reveal is a privacy or policy decision
- use placeholders for any fact it suggests adding

## A correct response must not

- name a GP, doctor or medical professional, or any other specific third party
- invent a timescale, date or phone number
- flag the positive contractions "We've" and "We'll"
- flag "Dear [firstname lastname]", "You do not need to do anything now" or the full GOV.UK link as problems
- rewrite the whole email instead of listing changes
