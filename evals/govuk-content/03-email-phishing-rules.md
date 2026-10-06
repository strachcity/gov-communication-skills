# Email that breaks the phishing rules

Tests that the skill applies the Service Manual email rules and flags personal information for a privacy check without deciding the privacy question.

- **skill:** govuk-content
- **task:** review
- **channel:** email
- **service:** none

## Prompt

Review this email template before we send it.

## Input

```
Subject: Update

Hi Sam,

Your application is ready for the next stage. To continue, reply to this email with your date of birth and your National Insurance number.

You can track your application at bit.ly/track-app-23 or open the attached PDF for more information.

Thanks,
The Team
```

## A correct response must

- flag the subject line "Update" as not specific enough
- flag "Hi" and suggest "Dear [firstname lastname]"
- flag the request for date of birth and National Insurance number as against the Service Manual phishing rules, and say it needs a privacy check
- flag the shortened link, and say links should be full GOV.UK addresses
- flag the attachment
- flag that the email does not say who it is from in a way the user would recognise
- flag that the email does not say what happens next or give a deadline

## A correct response must not

- decide whether the service is allowed to collect this information by email
- invent the real tracking URL, deadline or sender name, rather than using placeholders or flagging them
