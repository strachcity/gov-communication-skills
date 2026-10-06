# Eval results

## Round 4: 6 October 2026

The 3 `privacy-aware-communications` cases, rerun once each after "default positions" were renamed "risk heuristics" and the expectations reworded to match. Marked by the agent that wrote the skills. No runs without the skill.

| Case | Result |
|---|---|
| privacy 01: sender name reveals health | 9 of 9 |
| privacy 02: medical email, no decision recorded | 8 of 9 |
| privacy 03: medical messages, confirmed decision | 7 of 7 |
| **Total** | **24 of 25** |

### What the runs showed

- every run described heuristics as risks with a lower-risk option, marked "needs confirmation", and never as the organisation's policy
- every run separated quoted source rules, like the phishing rules, from heuristics
- **privacy 02:** asked "Is it OK?", the response opened "Not as it stands", which is a verdict on whether the email can be sent. The skill's boundaries now say not to answer yes or no, and to lead with what the message reveals and what needs a decision

### Limits

As round 3: 1 run each, not marked blind, no comparison without the skill.

## Round 3: 6 October 2026

The 5 new cases for `case-communication-patterns` and `government-communication`, each run once with the skills. To save usage, there were no runs without the skills, and the agent that wrote the skills marked the results, as in round 1.

| Case | Result |
|---|---|
| case-communication-patterns 01: map a case journey | 8 of 8 |
| case-communication-patterns 02: draft a generic message | 6 of 6 |
| case-communication-patterns 03: adapt the waiting pattern with a partial service context | 9 of 9 |
| government-communication 01: no service context | 9 of 9 |
| government-communication 02: service context from published documentation | 9 of 9 |
| **Total** | **41 of 41** |

### What the runs showed

- every run used only confirmed facts. Unconfirmed decisions and facts from published content became placeholders, with the candidate values listed
- every run kept the third party and sensitive evidence out of text messages, and committed to the service's update date rather than the third party's reply
- one run found that what's needed can change from case to case. The pattern now allows ((what we need)) for each message
- the lists of what needs a service decision were long, up to 17 items. The front door now puts the items that would change the draft most first
- one expectation in government-communication 02 conflicted with the skill's rule to use only confirmed facts. The expectation was reworded

### Before these runs

The patterns and front door were adapted for 3 invented services, a permit, a benefit and a registration service. That found 36 problems, which were fixed before the evals ran. Each pattern's evidence section records what changed.

### Limits

- 1 run each, so this doesn't show how consistent the skills are
- not marked blind, and no comparison without the skills
- the checks were written by the same agent that wrote the skills

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
