# Promotion added to a service message

Tests that adding promotion to a case message is flagged as possible direct marketing, without deciding it.

- **skill:** privacy-aware-communications
- **task:** review
- **channel:** email
- **service context:** none

## Prompt

Can you check this email from a privacy point of view? Our marketing team asked us to add the last paragraph.

## Input

```
Subject: We've received your application

Dear Jo Patel

We've received your application for a parking permit. Your reference is PP-204816. We'll make a decision by 30 October 2026.

You do not need to do anything now.

Did you know you can also join our paid leisure centre membership? Sign up today and get your first month free at https://www.example-leisure.co.uk/join

Parking Permits Team
```

## A correct response must

- identify the first part as a service message, citing the ICO's description of acknowledgement messages
- flag that the last paragraph may make the whole message direct marketing, quoting the ICO that a service message with direct marketing elements is considered direct marketing
- flag that promoting a paid-for service is generally direct marketing, citing the ICO
- say PECR and UK GDPR direct marketing rules may then apply, and list the questions for the DPO, like consent and the right to object
- flag the link to a site outside GOV.UK, citing the Service Manual
- suggest removing the promotion, or sending it separately under the right rules, as options

## A correct response must not

- decide that the email is lawful or unlawful
- state a lawful basis
