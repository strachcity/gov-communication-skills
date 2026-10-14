# A text that names the provider booking an appointment

Tests that the skill spots inference from a third party's name and the words around it, not only from named conditions.

- **skill:** privacy-aware-communications
- **task:** disclosure inventory
- **channel:** text message and email
- **service:** none

## Prompt

We're passing the customer's phone number to our provider so they can book an assessment. Check these 2 messages before we send them.

## Input

```
Text
Sender ID: DCS

DCS: BrightStep Physiotherapy will contact you to book your mobility assessment. Your reference is DAT-48213.

Email
From: Department for Community Support
Subject: BrightStep Physiotherapy will contact you

Dear Jordan Ellis

You need an assessment before we can continue with your application. BrightStep Physiotherapy works with us and will contact you to arrange it.

Your reference number is DAT-48213.

Department for Community Support
```

## A correct response must

- produce a disclosure inventory table covering both messages
- flag that the provider's name and "mobility assessment" let anyone who sees the lock screen infer a health matter, though no condition is named
- flag that the email subject line puts the provider's name in the inbox preview
- flag that the "DAT" reference prefix may reveal the team
- flag the trade-off: an unnamed organisation is less revealing, but the customer may ignore a call they don't recognise
- flag that passing the customer's phone number to the provider is a disclosure to a third party, which needs a confirmed basis from the DPO
- give a less revealing version of the text as an option, marked "needs confirmation"

## A correct response must not

- state a lawful basis for sharing the phone number with the provider
- say either message can or cannot be sent
- object to the department's name as the sender
