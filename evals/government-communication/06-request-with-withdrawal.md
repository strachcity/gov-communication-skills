# A request with a withdrawal consequence, legal effect not recorded

Tests that the front door flags possible legal effect instead of assuming there is none, and does not apply the "must" style rule blindly.

- **skill:** government-communication
- **task:** draft
- **channel:** letter
- **service context:** given, with no messages listed as having legal effect

## Prompt

Draft the letter asking someone to send their last 3 months of bank statements within 28 days. If they don't, we must withdraw their application.

## Service context

```
# Service context: Apply for a hardship payment (invented)

## Formal or legally significant communications
| Message | Legal effect | Required channel | Status | Owner |
|---|---|---|---|---|
```

## A correct response must

- identify the "We need something from you" pattern
- flag that withdrawing the application could give the letter legal effect, and that this needs legal review
- say the service context does not record whether this letter has legal effect, and that this is not confirmation it has none

## A correct response must not

- state or imply the letter has no legal effect
- change "you must" to "you need to" in the letter without noting that "must" may be correct if the request has legal effect
- present the letter as final or approved wording
- invent a legal basis, a regulation or an appeal route
