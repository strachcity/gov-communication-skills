# A service with a Welsh language duty

Tests that a language duty is flagged, not translated, and that texts are counted with Welsh in mind.

- **skill:** government-communication
- **task:** draft
- **channel:** email and text message
- **service context:** an invented grant, below

## Prompt

Draft the email and text we send when we've received a grant application.

## Service context

```
Service: Community hall repair grant (invented)
Customer word for the case: grant application
Sender: Community Hall Grants
Text sender ID: HallGrants
Reference format: CHG-123456
Tracking: https://www.gov.uk/check-community-hall-grant
Next step: we aim to make a decision within 8 weeks. Status: needs confirmation
Constraint: we must offer every message in Welsh. Source: our Welsh language scheme. Status: confirmed
```

## A correct response must

- use "We've received it", variant A
- use the sender, sender ID, reference format and tracking address as given
- keep the 8-week timescale as a placeholder, and flag it as needing confirmation
- flag that each message needs a Welsh version
- say that Welsh accented letters can cut a text's limit to 70 characters, and that the Welsh version needs its own count
- leave the service name prefix out of the text, because the sender ID names the service

## A correct response must not

- translate the messages into Welsh without being asked
- present the 8 weeks as a commitment
