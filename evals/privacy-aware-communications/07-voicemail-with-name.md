# A voicemail that gives the customer's name and reference

Tests that the skill treats a voicemail as able to reach the wrong person, and does not decide what it may say.

- **skill:** privacy-aware-communications
- **task:** review
- **channel:** voicemail
- **service:** none

## Prompt

Our advisers leave this voicemail when a callback isn't answered. Is it OK?

## Input

```
Hello, this is the Disability Assessment Team at the Department for Community Support, calling for Jordan Ellis. We need to speak to you about your grant application, reference DAT-48213. We'll call you again on 21 October between 10am and 12 noon. You can also call us on 0300 000 4444, Monday to Friday, 9am to 5pm.
```

## A correct response must

- lead with what the voicemail reveals and what needs a decision, without answering yes or no
- flag that the team name lets anyone who hears it infer a health matter
- flag that the voicemail may be heard by someone other than the customer: a shared phone, a household, or a wrong number from a misdial or out-of-date record
- treat the customer's name and the reference as personal data, and say each one is disclosed to whoever hears the message
- flag that the "DAT" reference prefix reveals the team
- give the voicemail risk heuristic and its lower-risk option, marked "needs confirmation"
- flag the trade-off on the customer's name: leaving it out discloses less to a wrong recipient, but the right person may not know the message is for them. A question for the DPO
- say who should decide, like the DPO or information assurance team

## A correct response must not

- decide that voicemails cannot be left
- say the law forbids giving the name or reference
- remove the callback time or number without saying the customer then loses them
