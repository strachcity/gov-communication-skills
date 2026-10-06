# gov-communication-skills

Agent skills and supporting knowledge for designing and reviewing UK government customer communications.

The first use case is DVLA Drivers Medical. The generic skills are written so that any government service can use them. Nothing in them should depend on Drivers Medical.

Nothing here is legal advice, and nothing here is an official GOV.UK or DVLA publication.

## Install

This repository is a Claude Code plugin. In Claude Code, run:

```
/plugin marketplace add strachcity/gov-communication-skills
/plugin install gov-communication-skills@gov-communication-skills
```

To try it from a local copy instead:

```
claude --plugin-dir path/to/gov-communication-skills
```

The plugin adds 3 skills. Claude uses them when a task fits, or you can ask for one by name, like "use govuk-content to review this email".

## How the repository is organised

- `skills/`: one folder per skill. Each generic skill holds its own guidance in `references/` and lists its sources in `sources.md`
- `services/<service>/`: what is true for one service only, including its policy decisions
- `evals/`: worked examples that test whether the skills behave correctly, one folder per skill

Each directory has a README that sets out what belongs there and what does not.

## Skills

| Skill | What it does | Status |
|---|---|---|
| `govuk-content` | drafts and reviews content against GOV.UK guidance, and flags privacy and policy questions without answering them | tested, see `evals/results.md` |
| `communication-moments` | the moments every case-based service shares, what each message must establish, and the evidence for each | draft, evals written but not run |
| `privacy-aware-communications` | lists what a message reveals in each channel, applies confirmed decisions, flags the rest, and drafts the communications part of a DPIA | tested, see `evals/results.md` |
| `government-communication` | combines the other skills with service knowledge to draft or review a whole communication | planned |

## How the layers depend on each other

- generic skills never refer to a service
- service knowledge can narrow generic guidance, but must say so when it does
- generic skills load service knowledge only when told which service they are working on
- evals can use any layer

If a skill only works for one service, it is not generic. It belongs with that service, or the service-specific part belongs in `services/`.

## Working here

Read `CLAUDE.md` before adding or changing anything. It covers how knowledge is added, where it goes, and what to do when a position is not known. `ARCHITECTURE.md` explains what we are building and how the parts fit. `PLAN.md` has the build plan.

No build step, no package manager, no framework. Everything is Markdown.
