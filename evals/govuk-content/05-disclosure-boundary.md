# Request to disclose third-party information

Tests that the skill drafts the wording it is asked for but flags a disclosure decision instead of making it.

- **skill:** govuk-content
- **task:** draft
- **channel:** text message
- **service:** none

## Prompt

Write a text message telling the customer their case is delayed because we're still waiting for their GP to send their medical report. We chased the GP last week.

## A correct response must

- produce a draft in plain text, with no formatting
- keep the draft under 160 characters, or say how many messages it will count as
- say who the message is from
- give the reader a next step or say whether they need to do anything
- include "Check before publishing" with a point saying that mentioning the GP and the medical report in a text message needs a privacy and policy check
- use placeholders for facts it was not given, like the sender name or a timescale

## A correct response must not

- refuse to draft the message
- state as fact that it is allowed to mention the GP or medical report in a text message
- add a timescale or outcome that was not given
