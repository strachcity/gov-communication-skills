# gov-communication-skills

Agent skills and supporting knowledge for designing and reviewing UK government customer communications.

The first use case is DVLA Drivers Medical. The generic skills are written so that any government service can use them. Nothing in them should depend on Drivers Medical.

Nothing here is legal advice, and nothing here is an official GOV.UK or DVLA publication.

## How the repository is organised

- `skills/`: one folder per skill. Each generic skill holds its own guidance in `references/` and lists its sources in `sources.md`
- `services/<service>/`: what is true for one service only, including its policy decisions
- `evals/`: worked examples that test whether the skills behave correctly, one folder per skill

Each directory has a README that sets out what belongs there and what does not.

## Skills

| Skill | What it does | Status |
|---|---|---|
| `govuk-content` | drafts and reviews content against GOV.UK guidance, and flags privacy and policy questions without answering them | first version, not yet tested |
| `privacy-aware-communications` | spots privacy issues, applies recorded service decisions, and flags anything not decided | planned |
| `government-communication` | combines the other skills with service knowledge to draft or review a whole communication | planned |

## How the layers depend on each other

- generic skills never refer to a service
- service knowledge can narrow generic guidance, but must say so when it does
- generic skills load service knowledge only when told which service they are working on
- evals can use any layer

If a skill only works for one service, it is not generic. It belongs with that service, or the service-specific part belongs in `services/`.

## Working here

Read `CLAUDE.md` before adding or changing anything. It covers how knowledge is added, where it goes, and what to do when a position is not known. `PLAN.md` has the build plan.

No build step, no package manager, no framework. Everything is Markdown.
