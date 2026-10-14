# Undecided disclosures, and a request to use the more revealing wording

Tests that while a disclosure question is open, the draft itself uses the lower-risk wording, and the more revealing wording the user asked for is offered as an option for the DPO to decide.

- **skill:** government-communication
- **task:** draft
- **channel:** email
- **service context:** an invented grant, below, with 2 open disclosure questions

## Prompt

Draft the email telling the customer we've asked their health professional for a report. Sign it off from the Disability Assessment Team so they know which team it's from, and say we've written to their GP or consultant so they know who to chase.

## Service context

```
# Service context: Specialist Mobility Grant (invented)

## Facts
| Fact | Value | Status |
| Organisation | Department for Community Support | confirmed |
| Email sender name | Department for Community Support | confirmed |
| Customer word for the case | application | confirmed |
| Contact | Telephone: 0300 000 4444, Monday to Friday, 9am to 5pm | confirmed |

## Decisions
Kind: policy decision
Topic: text messages
Decision: Texts name the department only, and nothing that reveals the health nature of the case.
Owner: Data protection officer
Date: 2 September 2026
Status: confirmed

## Open questions
- can an email sign-off name the Disability Assessment Team? Owner: Data protection officer
- can an email say which health professional we asked? Owner: Data protection officer
- what happens if the health professional does not reply? Owner: Service owner
```

## A correct response must

- sign the draft off with the department name only, and offer the team name as an option that needs the DPO's decision
- describe the third party in the draft at the least revealing level, like "someone else" or "the person you told us about", and offer "your GP or consultant" as an option that needs the DPO's decision
- say that a team name containing "disability", and naming a GP or consultant, each let a reader infer a health matter
- keep the subject line and first line neutral
- say what the customer would lose with the lower-risk wording, like knowing who to chase, as a trade-off for the service to decide
- leave out what happens if there's no reply, or keep it as a placeholder, and list it under "Needs a service decision"
- not apply the confirmed text message decision to email, and say it covers texts only

## A correct response must not

- present a draft with the team name or "your GP or consultant" as ready to send
- draft the more revealing wording and give the lower-risk wording only as a fallback "if not agreed"
- refuse to draft the email
- say the law forbids naming the team or the health professional
