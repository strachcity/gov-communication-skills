# Services

Knowledge that is true for one service only. One folder per service.

## What belongs here

- the service's vocabulary, and the internal terms customers should never see
- policy and legal decisions the service has made, with who made them and when
- the service's channels and what each one is used for
- known open questions the service has not resolved
- places where the service deliberately departs from, or narrows, generic guidance, with the reason

## What does not belong here

- generic content design or privacy guidance, even if this service is where it was first noticed

A service rule never moves into a generic skill without an explicit, recorded decision. See `CLAUDE.md`.

## Service layer for communication moments

To tailor the generic moments in `skills/communication-moments/` to a service, add a `moments.md` file to the service folder with one row per moment the service uses:

| Moment | Trigger in this service | Channels | Values for the placeholders | Status | Open questions |
|---|---|---|---|---|---|
| 3. We're waiting on someone else | [the service's own event] | [for example email and text] | [who was asked]: [value]. [timescale]: [value] | confirmed or needs confirmation | [anything not yet decided] |

- only values marked "confirmed" are used in drafts
- a service's detail never moves into the generic moments. If a service needs something no moment covers, add it to "Gaps" in `skills/communication-moments/references/moments.md`
