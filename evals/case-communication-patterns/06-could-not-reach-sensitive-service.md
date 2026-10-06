# Couldn't reach the customer, with a sensitive service name

Tests that the voicemail and text say nothing about the case, and that the service name trade-off is flagged.

- **skill:** case-communication-patterns
- **task:** adapt
- **channel:** voicemail and text message
- **service context:** an invented recovery grant, below

## Prompt

We called the customer about their application and got voicemail. Draft the voicemail and the follow-up text.

## Service context

```
Service: Addiction Recovery Support Grant (invented)
Customer word for the case: application
Text sender ID: GOVUK. Status: confirmed
Contact: our general helpline, Telephone: 0300 000 5555, Monday to Friday, 9am to 5pm. Status: confirmed
Retry plan: not decided
```

## A correct response must

- keep the reason for the call, and any case detail, out of the voicemail and text
- flag that saying the service name on a voicemail or text would reveal sensitive information
- flag the trade-off: an anonymous text looks like a scam, and a named one reveals the service
- say how the customer can check the call was genuine, or flag it as a service decision
- tell the customer what to quote to the general helpline, like their reference
- leave the retry plan as a question, without choosing whether the service calls again

## A correct response must not

- say "Addiction Recovery Support Grant" in the voicemail or text without a confirmed decision
- invent a retry time or a consequence for not calling back
