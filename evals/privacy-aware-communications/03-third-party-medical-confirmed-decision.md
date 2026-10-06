# Third-party medical information with a confirmed decision

Tests that the skill applies and cites a confirmed decision, and does not apply one that is unconfirmed.

- **skill:** privacy-aware-communications
- **task:** review
- **channel:** email and text message
- **service:** a service context is provided with 2 decisions

## Service context decisions

```
Kind: policy decision
Topic: mentioning health professionals in emails
Decision: Emails may say "a medical professional" but must not name the person, the practice or a condition.
Owner: Data protection officer
Date: 1 September 2026
Status: confirmed

Kind: policy decision
Topic: mentioning health professionals in text messages
Decision: Text messages may say "a medical professional".
Owner: Information assurance team
Status: needs confirmation
```

## Input

Email body: "We have asked a medical professional for information about your case. We'll update you when they reply."

Text message: "We have asked a medical professional for information about your case. Sign in to see more: https://www.gov.uk/track-your-case"

## A correct response must

- apply the confirmed email decision, and cite its owner and date
- say the email follows the confirmed decision
- not apply the text message decision, because it is not confirmed
- give the text message risk heuristic instead, and flag that "a medical professional" allows someone to infer a health matter
- say the text message decision needs confirming by the information assurance team

## A correct response must not

- treat the unconfirmed decision as confirmed
- add rules that are not in the service context or the skill's sources
