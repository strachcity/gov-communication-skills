# Web page with style errors

Tests that the skill finds common GOV.UK style errors and reports them in the review table.

- **skill:** govuk-content
- **task:** review
- **channel:** web content page
- **service:** none

## Prompt

Can you do a style check on this page content?

## Input

```
Renewing your permit

Please note that permits must be renewed every 3 years; failure to do so may result in a financial penalty of £50.00.

You can renew online, by post, by phone etc. To start your renewal click here.

Your application will be processed within 10-15 working days. You'll need to utilise the reference number on your letter, eg AB123456, and send any document(s) we ask for by 2nd June, 2027.

If you can't renew online, you should contact the Permits Office.
```

## A correct response must

- output only the 6-column table, with no introduction or summary
- flag "Please note" as unnecessary
- flag the semicolon and split the sentence
- flag "financial penalty" and suggest "fine"
- flag "£50.00" and suggest "£50"
- flag "etc" and ask for the options to be listed
- flag "click here" as link text and "click" as a word
- flag the passive "will be processed"
- flag "10-15" and suggest "10 to 15"
- flag "utilise" and suggest "use"
- flag "eg" and suggest "for example"
- flag "document(s)" and suggest "documents"
- flag "2nd June, 2027" and suggest "on or before 2 June 2027"
- flag "can't" and suggest "cannot"
- use the "Confused / Uncertain?" column for "must" and "should", since the skill cannot tell whether renewal is a legal requirement or whether contacting the office is a recommendation

## A correct response must not

- add facts that are not in the input, like a real fee, timescale or phone number
- change "must" to "need to" without flagging it
- invent a URL or anchor that is not in `sources.md`
