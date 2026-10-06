# Content with nothing to change

Tests that the skill leaves good content alone.

- **skill:** govuk-content
- **task:** review
- **channel:** web content page
- **service:** none

## Prompt

Style check this please.

## Input

```
You need to renew your permit every 3 years.

It costs £50 to renew. You'll get your new permit within 15 working days.

You'll need:

- your permit number
- a debit or credit card

Renew your permit online.

If you cannot renew online, call the Permits Office.

Telephone: 0300 123 4567
Monday to Friday, 9am to 5pm
```

## A correct response must

- say in one line that nothing needs to change, with no table

## A correct response must not

- add rows that only confirm something is already correct
- flag "You'll", which is a positive contraction and allowed
- flag "need to", which is correct for an administrative requirement
- suggest changes based on a house rule that is not in the GOV.UK guidance
