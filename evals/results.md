# Eval results

## Round 2: 6 October 2026

9 cases, each run 3 times with the skill and 3 times without, so 54 runs. A separate agent marked each case. It saw the 6 responses shuffled and relabelled, so it could not tell which used the skill.

| Case | With skill (3 runs) | Without skill (3 runs) |
|---|---|---|
| govuk-content 01: web page with style errors | 17, 18, 17 of 18 | 14, 13, 13 of 18 |
| govuk-content 02: nothing to change | 5, 5, 5 of 5 | 3, 3, 3 of 5 |
| govuk-content 03: email that breaks phishing rules | 9, 9, 9 of 9 | 7, 7, 7 of 9 |
| govuk-content 04: vague status message | 11, 11, 11 of 11 | 9, 9, 10 of 11 |
| govuk-content 05: request to mention the GP in a text | 10, 10, 10 of 10 | 7, 7, 7 of 10 |
| govuk-content 06: third-party update email | 9, 10, 10 of 10 | 5, 5, 5 of 10 |
| privacy 01: sender name reveals health | 8, 8, 8 of 8 | 4, 4, 4 of 8 |
| privacy 02: medical email, no decision recorded | 9, 9, 9 of 9 | 6, 8, 6 of 9 |
| privacy 03: medical messages, confirmed decision | 7, 7, 7 of 7 | 6, 5, 5 of 7 |
| **Total** | **258 of 261 (99%)** | **182 of 261 (70%)** |

### What the skills got wrong

- **govuk-content 01, 2 runs:** raised "should" in the reason column but not the "Confused / Uncertain?" column
- **govuk-content 06, 1 run:** suggested "your doctor" as an example of a clearer third party, which names a medical professional

### What the model got wrong without the skills

- it got GOV.UK rules wrong, like saying "can't" is acceptable and "Hi" is fine in emails
- it ignored the requested formats: no review table, no disclosure inventory, no "needs confirmation" status
- it made the disclosure decision itself, by leaving the GP out of a message it was asked to draft
- it stated policy as fact, like "We will never ask you to send your National Insurance number by email"
- it cited no sources for privacy points

### Limits

- the checks are written by the same people who wrote the skills, so they test what we expected, not everything that matters
- the markers did not read the skills' sources, so checks about sources were judged from what each response cited
- time and token costs were only recorded in round 1: about 15 seconds and 13,600 tokens more per run with the skill

## Round 1: 6 October 2026

8 cases, 1 run each, marked by the same agent that wrote the skills. With the skill: 76 of 76 checks. Without: 60 of 76. Round 2 replaces this.
