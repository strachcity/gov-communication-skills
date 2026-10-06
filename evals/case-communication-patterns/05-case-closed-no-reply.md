# Case closed without a decision

Tests variant D of the decision pattern, with an unconfirmed closure rule.

- **skill:** case-communication-patterns
- **task:** adapt
- **channel:** email
- **service context:** an invented home energy scheme, below

## Prompt

The customer didn't reply to our last 2 requests, so we're closing their application. Draft the email.

## Service context

```
Service: Home energy upgrade scheme (invented)
Customer word for the case: application
Closing rule: applications are closed if the customer doesn't reply within 28 days of a final reminder. Status: needs confirmation. Owner: scheme manager
Reapplying: customers can apply again at any time. Status: confirmed
Contact: Telephone: 0300 000 4444, Monday to Friday, 9am to 5pm. Status: confirmed
```

## A correct response must

- use "We've made a decision", variant D
- say the application is closed and why, in the first sentences
- say they can apply again
- flag that the closing rule needs confirming before the email is used
- flag whether closing can be challenged, as a question for the service
- check that the earlier requests said the application could be closed

## A correct response must not

- present the closure as a refusal on the merits
- invent what happens to anything the customer sent or paid
