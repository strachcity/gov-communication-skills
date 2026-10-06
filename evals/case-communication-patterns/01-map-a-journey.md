# Map a case journey to moments

Tests that the skill maps service events to generic moments without moving service detail into the moments.

- **skill:** case-communication-patterns
- **task:** plan
- **service:** an invented licensing service

## Prompt

Here's our case journey. Which messages do we need?

## Input

```
1. Customer posts an application form.
2. The form is scanned and a case is created, usually 3 days later.
3. A caseworker reviews it and writes to the customer's employer for a reference.
4. If the employer doesn't reply in 4 weeks, the caseworker sends a reminder to the employer.
5. The case moves to a senior caseworker for sign-off.
6. A decision letter is sent.
```

## A correct response must

- map step 1 to moment 1 and step 3 to moment 3
- map step 4 to variant B of moment 3 (still waiting), or say whether the customer needs to know
- say step 5 needs no customer message
- map step 6 to moment 8, and flag whether the letter has legal effect as a question for the service
- keep "employer" as the service's value for [who we've asked], not as part of the moment

## A correct response must not

- invent timescales not in the input
- decide whether the employer can be named in a text or email
- create a new generic moment for an employer reference
