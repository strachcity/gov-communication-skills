# Draft a service-agnostic message

Tests that the skill drafts a generic message with placeholders for every service detail.

- **skill:** communication-moments
- **task:** draft
- **channel:** email
- **service:** none

## Prompt

Draft a generic email for "we need something from you" that any service could tailor.

## A correct response must

- follow the message anatomy: what has happened, greeting, reference, what to do and by when, what happens if they don't, how to get help, who it's from
- use placeholders for every service detail, like [service name], [what we need], [deadline] and [how to send it]
- list the questions the service must answer under "For the service to fill in"
- avoid asking for personal information in the email itself

## A correct response must not

- fill any placeholder with an invented value
- name a specific department, form or system
