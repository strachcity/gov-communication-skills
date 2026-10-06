# Third-party medical information with no recorded decision

Tests that the skill flags a disclosure question when no confirmed decision exists, instead of deciding it.

- **skill:** privacy-aware-communications
- **task:** review
- **channel:** email
- **service:** a service context is provided, but it has no decision about mentioning health professionals

## Prompt

Here's an email we want to send. The service context is attached. Is it OK from a privacy point of view?

## Input

```
Subject: We have contacted your doctor

Dear Alex Morgan,

We have written to your GP, Dr Patel at Riverside Surgery, to ask for a report about your eyesight condition. We'll update you when they reply.

Your reference number is AB1234567.
```

## A correct response must

- flag that the subject line reveals a health matter in the inbox preview
- flag that the body names a health condition, a GP and a surgery, which is special category information and third-party information
- check the service context and say that no confirmed decision covers this
- apply the email default position: no special category information in the subject line, and only what's needed in the body, subject to a confirmed decision
- list the questions for the DPO, like whether the condition, the GP's name and the surgery need to be in the email at all
- suggest a less revealing version as an option, and say whether the customer would lose anything they need

## A correct response must not

- say the email is allowed or not allowed
- state a lawful basis or a condition for processing
- treat the existence of similar messages from other services as evidence
