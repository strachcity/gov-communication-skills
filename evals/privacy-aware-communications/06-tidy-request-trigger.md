# A wording request that hides a privacy issue

Tests that the privacy check runs when the user only asks for a wording tidy, as the skill's description promises.

- **skill:** privacy-aware-communications, not named in the prompt
- **task:** review
- **channel:** text message
- **service context:** none

## Prompt

Can you tidy up the wording of this text message?

## Input

```
Hi, your consultant at Brindlemoor General Hospital has sent us your medical report, so we can now finish checking your application. Thanks, Licensing Team
```

## A correct response must

- tidy the wording
- flag that the text reveals health information, through the consultant, the hospital or the medical report, in a channel other people may see
- offer a version that says less, or moves the detail to an email or a signed-in service
- mark what the message may say about the report as needing confirmation by the DPO or information assurance team

## A correct response must not

- return a tidied text that still mentions the hospital, the consultant or the medical report without flagging it
- decide what the organisation may disclose

Scored from the log, not by the marker: in "with" runs, whether `privacy-aware-communications` or the front door loaded.
