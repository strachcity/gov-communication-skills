# An email sent alongside a formal notice

Tests that the front door checks an email against the formal notice it accompanies, and does not invent a deadline or consequence to replace a vague one.

- **skill:** government-communication
- **task:** review
- **channel:** email
- **service context:** an invented grant, below

## Prompt

We send a formal notice by post when the customer needs to book an assessment. This email goes the same day so they can book straight away. Can you check it?

## Input

```
Subject: Book your assessment

Dear Jordan Ellis

You need to book an assessment as part of the process for the form you sent us.

We've sent a formal notice that explains this decision. You do not need to wait for it to arrive before booking your assessment.

Your reference is 48213.

How to book: [booking link]

You should this as soon as possible.

What happens next: We'll continue with your application after the assessment has taken place. If you need help, contact us.

Department for Community Support
```

## Service context

```
Service: Specialist Mobility Grant (invented)
Customer word for the case: application
Formal notice to book an assessment: has legal effect. Sent by post. Owner: Policy lead. Status: confirmed
Deadline and consequence in the notice: not recorded
Booking system address: not recorded
```

## A correct response must

- flag that asking the customer to book is not a decision, so "explains this decision" is wrong
- flag that the email must not contradict the formal notice, and ask whether it repeats the notice's deadline and consequence word for word. A question for the policy lead
- keep "as soon as possible" or a ((deadline)) placeholder until the deadline is confirmed, and list it under "Needs a service decision"
- flag that the request has no consequence for not booking, and leave it as a decision for the service
- flag that the booking link must be on GOV.UK and written in full, or the service must decide an exception, because the address is not recorded
- use "your application", the customer's word, in place of "the form you sent us" and "the process"
- fix "You should this" and add contact details
- keep the subject line and first line neutral, without naming the kind of assessment

## A correct response must not

- invent a deadline or a consequence
- say the email can replace the formal notice
- name the kind of assessment, or a provider, in the subject line
