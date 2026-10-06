# No service context

Tests that the skill helps establish a service context without blocking the draft, and invents nothing.

- **skill:** government-communication
- **task:** draft
- **channel:** not given
- **service context:** none

## Prompt

I work on a government service that issues licences. Can you write the message we send when someone's application arrives?

## A correct response must

- identify the "We've received it" pattern, variant A
- either ask a small number of questions, or give a draft with placeholders and ask the questions alongside it
- if it drafts, use placeholders for the service name, reference, next step, timescale, tracking route, contact route and sender
- say which channels it chose and why, or ask
- list what needs a service decision, including whether the date of receipt has legal significance
- offer to turn the answers into a service context the user can keep

## A correct response must not

- invent a timescale, a reference format, a web address or a sender name
- ask the user to fill in a whole service context before giving any help
- name a real government service or department
