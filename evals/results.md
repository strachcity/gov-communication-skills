# Eval results

The latest result for each case. When a case is rerun, replace its row. Git history has the earlier rounds.

Last updated 15 October 2026.

## govuk-content and privacy-aware-communications

Run 3 times with the skill and 3 times without, marked blind by a separate agent, except where noted.

| Case | With skill | Without skill |
|---|---|---|
| govuk-content 01: web page with style errors | 17, 18, 17 of 18 | 14, 13, 13 of 18 |
| govuk-content 02: nothing to change | 5, 5, 5 of 5 | 3, 3, 3 of 5 |
| govuk-content 03: email that breaks phishing rules | 9, 9, 9 of 9 | 7, 7, 7 of 9 |
| govuk-content 04: vague status message | 11, 11, 11 of 11 | 9, 9, 10 of 11 |
| govuk-content 05: request to mention the GP in a text | 10, 10, 10 of 10 | 7, 7, 7 of 10 |
| govuk-content 06: third-party update email | 9, 10, 10 of 10 | 5, 5, 5 of 10 |
| privacy 01: sender name reveals health | 9 of 9, once | 4, 4, 4 of 8 |
| privacy 02: medical email, no decision recorded | 9 of 9, once | 6, 8, 6 of 9 |
| privacy 03: medical messages, confirmed decision | 7 of 7, once | 6, 5, 5 of 7 |
| privacy 04: promotion added to a service message | 8 of 8, once | not run |
| privacy 05: a judgement marked "confirmed", and a spoken DPO claim | 7 of 7, once | 3, 3, 3 of 7 |
| privacy 06: a wording request that hides a privacy issue | 6 of 6, once | 5, 5, 4 of 6 |
| privacy 07: a voicemail with the customer's name and reference | 11 of 11, once | not run |
| privacy 08: a text that names the provider booking an appointment | 10 of 10, once | not run |

All 8 privacy cases were rerun once on 15 October 2026. Privacy 02 was run again after its missing service context was added, after the lower-risk drafting change, marked blind by a separate agent. The "without skill" column is from earlier rounds, before the skill changed.

Privacy 05 and 06 were written by someone who didn't write the skills.

## case-communication-patterns and government-communication

Run once each, with the skills only. Cases 04 to 11 and the 2 reruns were marked by a separate agent that didn't read the skills. The exceptions are case-communication-patterns 01 to 03 and government-communication 01, from an independent round at `1db3111`. It ran each 3 times with the skills and 3 times without, marked blind by a separate agent. The figures after "Without" are the runs without the skills.

| Case | Result |
|---|---|
| case-communication-patterns 01: map a case journey | 7, 7, 7 of 8. Without: 4, 3, 4 |
| case-communication-patterns 02: draft a generic message | 6, 5, 6 of 6. Without: 3, 3, 3 |
| case-communication-patterns 03: adapt the waiting pattern | 9, 9, 9 of 9. Without: 6, 7, 6 |
| case-communication-patterns 04: decision, not awarded | 9 of 10 |
| case-communication-patterns 05: case closed without a decision | 8 of 8 |
| case-communication-patterns 06: couldn't reach the customer, sensitive service name | 7 of 8 |
| case-communication-patterns 07: a visit at short notice | 6 of 7 |
| case-communication-patterns 08: decision and certificate together | 7 of 7 |
| case-communication-patterns 09: renewal reminder for a paid licence | 8 of 8 |
| case-communication-patterns 10: when to send a progress update | 6 of 6 |
| case-communication-patterns 11: feedback after a refusal | 7 of 8 |
| government-communication 01: no service context | 9 of 9. Without, at `1db3111`: 3, 3, 3 |
| government-communication 02: service context from documentation | 9 of 9 |
| government-communication 03: an organisation as the customer | 9 of 9 |
| government-communication 04: a Welsh language duty | 8 of 8 |
| government-communication 05: no questions, "the usual timescales" | 8 of 8. Without, at `1db3111`: 5, 5, 5 |
| government-communication 06: a request with a withdrawal consequence, legal effect not recorded | 7 of 7. Without, at `1db3111`: 4, 4, 4 |
| government-communication 07: undecided disclosures, and a request for the more revealing wording | 11 of 11 |
| government-communication 08: recording a data protection team's responses | 11 of 12 |
| government-communication 09: an email sent alongside a formal notice | 10 of 11 |

All 9 government-communication cases were rerun once on 15 October 2026. Case 08 was run again after `service-context.md` said how to record responses, after the lower-risk drafting change, with the skills only, marked blind by a separate agent. The figures after "Without" are from the independent round at `1db3111`. The checks for 05 and 06 were written by someone who didn't write the skills.

## Watch in the next run

- government-communication 08: after `service-context.md` said how to record responses, the rerun scored 11 of 12. It missed the open question about sharing contact details with the provider, but the case input never said they were shared. The input now says so. Rerun it
- government-communication 09: said "this decision" could be misread, but didn't say plainly that a request to book is not a decision
- government-communication 03: passed, but never used the words "personal data" for the contact's name and email address
- privacy 08: gave the less revealing text as the draft, without its own "needs confirmation" label
- case-communication-patterns 04: the draft used only confirmed outcome words, but the response's own notes said "refused"
- case-communication-patterns 07: the visit date was written in, not left as a per-message value

## Limits

- government-communication 07 to 09 and privacy 07 and 08 come from a data protection team's review of real drafts made with the skills. The service is not named, and the cases use an invented one
- the 15 October round ran each case once, not 3 times, so a single pass doesn't show the result is stable
- patterns and front door: 1 run each, no comparison without the skills, except the cases from the independent round. That round ran at `1db3111`, before the patterns and front door were revised
- the checks were written by the same people who wrote the skills, so they test what we expected, not everything that matters
