# Renewal reminder for a paid licence

Tests the act-before-a-date pattern with an expiry, a fee and a possible direct marketing question.

- **skill:** case-communication-patterns
- **task:** adapt
- **channel:** email and text message
- **service context:** an invented licence, below

## Prompt

Draft the renewal reminder we send 8 weeks before a licence expires.

## Service context

```
Service: Mobile food stall licence (invented)
Licence length: 12 months. Status: confirmed
Renewal fee: £95. Status: confirmed
Renewals: must be received at least 10 working days before expiry to avoid a gap. Status: confirmed
Trading without a licence: an offence. Status: confirmed. Owner: legal team
How to renew: https://www.gov.uk/renew-mobile-food-stall-licence. Status: confirmed
Text sender ID: StallLicence. Status: confirmed
```

## A correct response must

- say "expires on" with the expiry date, and give the last date to renew separately
- include the fee
- use "must" or say it's an offence only because the context confirms it's a legal matter
- flag whether a reminder to renew a paid licence could be direct marketing, as a question for the DPO
- flag that contact details may be out of date after a year
- leave out the service name prefix in the text, because the sender ID names the service, or explain the choice

## A correct response must not

- imply renewing on the expiry date is in time
- decide whether the reminder is direct marketing
