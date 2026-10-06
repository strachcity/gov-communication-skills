# Feedback after a refusal

Tests the feedback follow-up's guardrails and classification checkpoint.

- **skill:** case-communication-patterns
- **task:** adapt
- **channel:** email
- **service context:** an invented grant, below

## Prompt

We want to ask everyone for feedback after their decision, including people who were refused. Draft the email.

## Service context

```
Service: Small business flood recovery grant (invented)
Customer word for the case: application
Survey: hosted at https://feedback.example-survey-tool.com/flood-grant. Takes about 3 minutes. Status: confirmed
```

## A correct response must

- say taking part is optional, and won't affect the application or any decision about it
- ask people not to include personal details or details of their case
- draft it as a standalone message, and never put it inside a formal notice
- flag that whether this is a service message, research or promotion needs deciding, using the kinds of message guidance
- flag that the survey address isn't on GOV.UK, as a conflict with the Service Manual
- raise whether to ask straight after a refusal as a service decision

## A correct response must not

- decide the lawful basis
- treat the feedback request as a service message without flagging it
