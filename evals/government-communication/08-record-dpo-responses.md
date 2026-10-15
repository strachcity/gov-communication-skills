# Recording a data protection team's responses in the service context

Tests that responses to a decision paper are recorded at the strength they were given: clear decisions as decisions, steers as steers, deferrals and disagreements as open.

- **skill:** government-communication
- **task:** create or update a service context
- **channel:** none
- **service context:** an invented grant, with the responses below

## Prompt

Our data protection team went through the decision paper at the meeting on 7 October 2026. Here are their responses. Update our service context with what they decided, so the drafts use it.

## Input

```
Service: Specialist Mobility Grant (invented)
Organisation: Department for Community Support (invented)

| No. | Decision needed | What we proposed | Decision | Comments |
| 1 | Email sign-off | Sign off as "Disability Assessment Team" | Use the department name, not the team | RK: use the department name. PL: agree. Keep subject lines generic too |
| 2 | Reference in texts | Give the reference in the first text | Can use the reference. No "DAT" prefix | RK: only where the customer needs to quote it. PL: is a unique reference safe to send by text? Ask the security team |
| 3 | Is "review" neutral in texts? | Yes | Not decided. Avoid "review" where possible, let's learn first | RK: "your application" instead. PL: be as generic as possible |
| 4 | Naming the provider that books assessments | Name it in emails only. Share the customer's phone number with it to arrange the assessment. Please confirm the basis for sharing | "Our provider", keep it generic. Sam Okafor can give the current wording | RK: I think we already say "our provider"? |
| 5 | Voicemails | Say the department name and the customer's name | All good, as long as no name and no more information | RK: is the reference new each time? PL: risk of a misdial, so keep it generic if voicemails are allowed at all |
| 6 | Links in emails | GOV.UK links in full | Links in emails when appropriate. Goes through the cyber team. Never in texts | PL: what is the department's current policy on links? |
| 7 | Asking for medical evidence by email | Say what we need in the email body | Not for the first release, until the journey is worked through | RK: further discussion needed |
```

## A correct response must

- record 1 as a confirmed policy decision, with the meeting date, and ask for the decision owner's role, because initials alone do not say who has authority
- record 2 as a decision with an open condition: the security team's view on sending a reference by text is still needed
- record 3 as not decided. The steer to avoid "review" can shape wording, but it is recorded as needing confirmation, not as a policy decision
- record 4 as a decision for the wording "our provider", and keep sharing the customer's contact details with the provider as a separate open question, because the response does not cover it
- flag that 5 is ambiguous: "all good" reads as approval, but the condition "no name" contradicts the proposal. Ask which is meant before drafting voicemails
- record 6 as conditional on a cyber team review, and record the open question about the department's own link policy
- record 7 as deferred, with "further discussion" as an open question, not a decision against
- say which drafts each recorded decision changes

## A correct response must not

- record "be as generic as possible" as a confirmed rule
- treat a reviewer's question, like whether a reference is safe to send, as a decision
- record Sam Okafor as the owner of decision 4, because they were named as a source of wording, not as the decision maker
- add any of these decisions to the plugin's generic guidance
