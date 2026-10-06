# Decision and certificate on the same day

Tests combining the decision with "What you applied for is on its way", and flagging an email attachment.

- **skill:** case-communication-patterns
- **task:** adapt
- **channel:** email
- **service context:** an invented registration service, below

## Prompt

When we accept a registration, we email the certificate as a PDF the same day. Draft that email.

## Service context

```
Service: Register as a childminding assistant (invented)
Customer word for the case: application to register
Outcome word: "registered". Status: confirmed
Certificate: emailed as a PDF attachment. Status: confirmed
Duty: registered assistants must tell us about any change of address within 14 days. Status: needs confirmation. Owner: registration manager
Feedback survey: none
```

## A correct response must

- send one email, with the outcome first, then the certificate
- flag that a PDF attachment conflicts with the Service Manual's advice to avoid attachments, and offer a link behind sign-in as the lower-risk option
- include the change of address duty as an optional section, flagged as needing confirmation
- flag "must" in the duty, because the context doesn't say it's a legal requirement
- say whether this is the end of the process, or flag it

## A correct response must not

- send 2 separate emails for the decision and the certificate
- add a feedback request
