# Sender name that reveals health information

Tests that the skill looks at what is visible before a message is opened, not just the message body.

- **skill:** privacy-aware-communications
- **task:** disclosure inventory
- **channel:** text message
- **service:** none

## Prompt

Can you check this text message for privacy issues?

## Input

```
Sender ID: MedicalTeam

We have received your form. Your reference is AB1234567. You do not need to do anything now. Track your case at https://www.gov.uk/track-your-case
```

## A correct response must

- produce a disclosure inventory table
- flag that the sender ID "MedicalTeam" lets anyone who sees the phone infer a health matter, citing the ICO point that receiving a message can itself reveal information
- treat the reference number as personal data, but accept it as needed for the message
- apply the text message default position and mark it "needs confirmation"
- say who should confirm it, like the DPO or information assurance team

## A correct response must not

- decide that the sender ID is unlawful
- invent an organisation's policy on sender IDs
- flag the GOV.UK link as a problem
