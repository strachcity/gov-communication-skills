# Decision: not what the customer asked for

Tests the decision pattern for an unwelcome outcome with a 2-stage challenge route.

- **skill:** case-communication-patterns
- **task:** adapt
- **channel:** letter and text message
- **service context:** an invented hardship grant, below

## Prompt

Draft the letter and text for when a hardship grant is not awarded. Here's our service context.

## Service context

```
Service: Emergency hardship grant (invented)
Customer word for the case: application
Outcome words: "awarded" or "not awarded". Status: confirmed. Owner: policy team
Reasons: given in every decision letter. Status: confirmed
Challenge route: ask for a review within 1 month of the decision date. If still unhappy, appeal to an independent tribunal. Status: confirmed. Owner: legal team
Decision letter: a formal notice, by post. Status: confirmed. Owner: legal team
Texts: sender ID "GOVUK". Texts may only say a letter has been sent. Status: confirmed. Owner: information assurance lead
Contact: Telephone: 0300 000 3333, Monday to Friday, 9am to 5pm. Status: confirmed
```

## A correct response must

- give the outcome in the first sentence of the letter, using "not awarded", in a sentence that reads correctly
- include a reasons section, using a per-case placeholder for the reasons
- give the challenge route as 2 steps, with the deadline as a date placeholder and the decision date shown
- flag what the 1 month counts from, and whether it's calendar months, if the context doesn't settle it
- flag the letter as a formal notice needing legal review
- keep the text to a pointer that doesn't reveal the outcome, and send it after the letter is likely to have arrived
- flag the trade-off of a GOVUK sender ID with no service name

## A correct response must not

- open with "Unfortunately" or an apology before the outcome
- use outcome words the service hasn't confirmed, like "refused" or "rejected"
- add a feedback request to the letter
