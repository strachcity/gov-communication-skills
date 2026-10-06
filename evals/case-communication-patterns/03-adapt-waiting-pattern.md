# Adapt the waiting pattern with a partial service context

Tests that the skill adapts a pattern using only confirmed facts, and flags the rest.

- **skill:** case-communication-patterns
- **task:** adapt
- **channel:** email and text message
- **service context:** an invented permit service, below

## Prompt

We've asked someone else for information about a customer's permit application. Draft the email and text message.

## Service context

```
Service: Apply for a market trader permit (invented)
Customer word for the case: application
Tracking: https://www.gov.uk/check-market-permit-application
Sender: Market Permits Service

Kind: policy decision
Topic: update timescale
Decision: We update customers at least every 15 working days while waiting.
Status: confirmed
Owner: Head of service

Kind: hypothesis
Topic: naming the third party
Decision: Emails can say "the local council".
Status: needs confirmation
Owner: Data protection officer
```

## A correct response must

- use the "We're waiting on someone else" pattern, variant A
- say the customer does not need to do anything now
- give a next update based on the confirmed 15 working days
- leave the third party undescribed, or use the least revealing level, and flag that naming "the local council" needs confirmation by the data protection officer
- keep the text message free of any description of the third party
- list what happens if there's no reply as a question for the service

## A correct response must not

- use "the local council" as if it were confirmed
- invent what the service will do if there's no reply
- promise when the third party will reply
