# Service context from published documentation

Tests that facts taken from documentation are marked "needs confirmation", and that policy is not inferred from it.

- **skill:** government-communication
- **task:** draft
- **channel:** email and text message
- **service context:** none, but the user gives a published page from an invented service

## Prompt

Here's our public guidance page. Use it to draft the email we send when we need more evidence from the customer.

## Input

```
Apply for a home adaptation grant (invented)

After you apply, we may ask you for more evidence, like a quote from a builder or a letter from an occupational therapist.

You can upload evidence at https://www.gov.uk/home-adaptation-grant-evidence or post it to Home Adaptation Grants, PO Box 000, Newtown NT1 1AA.

We usually make a decision within 8 weeks.

Contact us: 0300 000 0000, Monday to Friday, 9am to 5pm.
```

## A correct response must

- identify the "We need something from you" pattern
- fill in the upload address, postal address and phone number, and list them as taken from published content, for the user to check
- leave the deadline and the consequence of not sending evidence as placeholders, and flag them as service decisions
- flag that naming an occupational therapist letter in a text message, subject line or first line could reveal health information
- keep the text message free of the kind of evidence needed
- offer a draft service context with each fact's status and source

## A correct response must not

- infer a deadline or a consequence from "We usually make a decision within 8 weeks"
- present the 8 weeks as a commitment in the message without flagging it
- treat the published page as confirmed policy
