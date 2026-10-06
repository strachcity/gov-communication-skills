# Service context

What a service context contains, how to read one, and how to help a user create one.

Last revised 6 October 2026.

A service context holds one service's facts and decisions. It belongs to the user. It lives in their own project, or in the conversation, never in this plugin.

## Contents

- What it can contain
- How each fact is recorded
- Template
- Reading a service context
- When there isn't one yet
- Which facts each pattern needs

## What it can contain

Every section is optional. A missing fact stays a placeholder in the draft.

- **about the service:** what it does, in a sentence or 2
- **users:** who the customers are, and anything that affects how they read messages
- **terminology:** the words customers know, and internal terms to keep out
- **case states:** the states a case moves through, and what the customer sees
- **timescales:** the ones the service can commit to
- **channels:** which channels the service uses, and for what
- **sender and contact information:** the sender name, text message sender ID, contact routes and opening times
- **tracking routes:** where the customer can check progress
- **formal or legally significant communications:** which messages have legal effect
- **decisions:** confirmed policy or disclosure decisions
- **constraints:** like a template tool, a character limit or a Welsh language duty
- **departures from the generic patterns:** with the reason
- **open questions:** with who could answer each

## How each fact is recorded

Each fact or decision records:

- **status:** confirmed, needs confirmation or open question
- **source:** a document, meeting or person
- **owner:** who can confirm it, if known
- **last checked:** a date

A decision also records its kind:

- **policy decision:** made by someone with authority, so it says who and when
- **communication judgement:** a design decision based on research or experience
- **precedent:** wording that was approved or rejected, with the reason if known
- **hypothesis:** from prototypes or workshops, not yet tested or agreed

Only confirmed facts are used in drafts. A hypothesis or judgement is never treated as a policy decision, even if it's marked confirmed. Say so if you see one marked that way.

## Template

Give the user this template, filled in with what you know. Leave out sections with nothing in them.

```
# Service context: [service name]

Last updated: [date]
Owner: [role]

## About the service

[What it does, in a sentence or 2.]

## Users

[Who they are, and anything that affects how they read messages.]

## Facts

| Fact | Value | Status | Source | Owner | Last checked |
|---|---|---|---|---|---|
| Customer word for the case | application | confirmed | service team | product manager | 6 October 2026 |
| Reference format | [example] | | | | |
| Sender name | | | | | |
| Text message sender ID | | | | | |
| Contact route | | | | | |
| Tracking route | | | | | |
| Channels used | | | | | |

## Terminology

| Customers say | Internal term to avoid | Status |
|---|---|---|

## Case states

| State | What the customer sees | Moment | Status |
|---|---|---|---|

## Timescales

| What | Timescale | Status | Source | Owner |
|---|---|---|---|---|

## Formal or legally significant communications

| Message | Legal effect | Required channel | Status | Owner |
|---|---|---|---|---|

## Decisions

Kind: policy decision | communication judgement | precedent | hypothesis
Topic: [what it covers]
Decision: [the decision, in its owner's words where possible]
Source: [document, meeting or person]
Owner: [role]
Date: [date made]
Status: confirmed | needs confirmation | open question

## Constraints

- [constraint, with its source]

## Departures from the generic patterns

| Pattern | Departure | Reason | Status |
|---|---|---|---|

## Open questions

| Question | Who could answer |
|---|---|
```

## Reading a service context

- use only facts marked "confirmed"
- if 2 facts conflict, use neither. Flag both
- if a fact has no status, treat it as "needs confirmation"
- if a fact is out of date or its source is unclear, use it only if confirmed, and mention the date

## When there isn't one yet

### 1. Start from the request

Find the pattern the request needs, then ask only for the facts in its placeholder table. See "Which facts each pattern needs" below.

Ask a few questions at a time, starting with the ones that change the draft most. Always offer the option to carry on with placeholders.

Good first questions:

- what's the service called, and what do customers call their case?
- which channels do you send messages through?
- who are the messages from, and how can customers get help?
- is there anything you've already decided about what messages can say?

### 2. Read documentation the user points to

Take facts from it, and record the document as the source.

Mark everything taken from documentation as "needs confirmation", unless the user confirms it. Published content can be out of date or wrong, so it's never treated as the service's policy on its own.

Don't infer a policy, disclosure decision, consequence or legal effect from documentation. Record it as an open question.

If 2 documents disagree, record both and flag the conflict.

### 3. Draft the service context

Use the template. Fill in only what you were told or read, with each fact's status and source.

### 4. List the open questions

Include every placeholder the draft still needs, and every privacy or policy checkpoint without a confirmed decision. Say who could answer each, if you can tell.

### 5. Offer it back

Give the user the service context to save in their own project, like `service-context.md`. Say it's theirs to keep and update. It's never added to this plugin.

## Which facts each pattern needs

| Pattern | Facts |
|---|---|
| We've received it | customer word for what was received, reference format, next step and timescale, tracking route, contact route, sender, whether receipt has legal significance |
| We're waiting on someone else | customer word for the case, how the third party can be described in each channel, when the service will next update the customer, what happens if there's no reply, tracking route, contact route, sender |
| We need something from you | what's needed and a neutral description of it, return routes, deadline, consequence of not acting, whether there's a legal requirement, next step after receipt, contact route, sender |

The full placeholder table is in each pattern file in `case-communication-patterns`.
