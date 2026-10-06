# Vague status message

Tests that the skill improves a vague status message without adding facts it was not given.

- **skill:** govuk-content
- **task:** review
- **channel:** email
- **service:** none

## Prompt

This is the email we send when someone's application is being looked at. Can you check it?

## Input

```
Your application is currently with our medical team and will be processed in due course.
```

## A correct response must

- flag that the status is vague and does not say what is happening
- flag the passive "will be processed"
- flag that there is no next step for the reader
- flag that "in due course" gives no timescale
- flag that it does not answer the reader's likely question, like when they will hear back
- use placeholders, like [timescale], for facts it was not given
- use the "Confused / Uncertain?" column to say the real timescale and next step need confirming
- flag that mentioning a medical team may need a privacy check, without deciding the question

## A correct response must not

- say why the application is waiting, like "we are waiting for your doctor to reply"
- invent a timescale, like "within 6 weeks"
- remove the reference to the medical team without flagging why
