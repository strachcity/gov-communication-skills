# Plan

What's next, and the decisions about sources that the skills rely on. `ARCHITECTURE.md` describes the design, and takes precedence where the 2 differ. Git history records what's been done.

Last updated 7 October 2026.

## State of play

- `govuk-content` and `privacy-aware-communications` are tested, with blind-marked evals
- `case-communication-patterns` has 9 moments, 3 modifiers and 1 follow-up. Every one has a pattern, adapted for 3 invented services, with evals run once
- `government-communication`, the front door, exists in draft with its own evals, run once
- no pattern is marked "tested with users"

## Next steps

1. Test with a new team. Give the plugin to someone outside this work, with only the README. Ask them to set up a service context and draft messages for their own service. Record where they got stuck, and fix the instructions rather than adding rules.
2. Run the blind evaluation for the patterns and the front door. Run each eval once with the skills and once without, marked by a separate agent that can't tell which is which. Rerun only the cases that fail or look inconsistent.
3. Test the patterns with users. A test pack can be written then.

## Running evals without wasting usage

Each eval run loads several skills, so a full round is expensive.

- after changing a skill, run only that skill's evals, once
- run the comparison without the skills only for a release or a major change
- record the result in `evals/results.md`, replacing the earlier result for that case

## Scope

The skills cover 4 channels: web pages in prototypes, emails, text messages and letters.

Out of scope for now:

- NHS guidance. A service that needs it can bring it in its own service context
- NHS App messages, phone scripts and web chat
- Welsh

## Supporting sources

The main sources are listed in `CLAUDE.md`. A supporting source is used only for its gap, and its entries are marked "needs confirmation".

| Gap | Supporting source |
|---|---|
| Components and patterns for prototype pages | GOV.UK Design System, for prototype pages only: https://design-system.service.gov.uk/ |
| Greeting and sign-off in letters, and sign-off in emails | a colleague's govuk-style-writer skill |
| Privacy law | UK GDPR, the Data Protection Act 2018 and ICO guidance, for the privacy skill only |
| Text message formatting | Notify covers length, on its pricing page, but not formatting. The skills treat text messages as plain text and mark that as interpretation |

The ICO says some of its guidance is under review following the Data (Use and Access) Act. Keep privacy entries' "last checked" dates up to date, and check again before any real use.

Where sources disagree, see "Known conflicts between sources" in `skills/govuk-content/references/channels.md`.

## Reviewed and not used

- **NHS digital service manual content guide:** an NHS service can bring it into its own service context
- **govuk-design-guide:** it's about GOV.UK website templates, not writing
- **prompt-to-page:** it only hosts app installers, and the app is proprietary

## Open questions

None at the moment. Each service's own open questions belong in its service context.
