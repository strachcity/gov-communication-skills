# gov-communication-skills

Agent skills and supporting knowledge for designing and reviewing UK government customer communications.

It works for any government service. The same plugin is used by every service, with no bespoke skill for each one. You tell it about your service, and it adapts generic case communication patterns using your service's facts.

Nothing here is legal advice, and nothing here is an official GOV.UK publication.

## What it does

Government services repeatedly write the same kinds of case communication. The plugin holds generic patterns for them, and adapts each one using your service's facts.

```mermaid
flowchart LR
    P["Reusable patterns<br/>one for each shared moment"] --> R
    S["Service facts<br/>from your service context"] --> R
    G["Guardrails<br/>GOV.UK content and privacy checks"] --> R
    R["Ready-to-review communications<br/>a draft for each channel, plus open decisions"]
```

It doesn't invent your policy. Anything your service hasn't decided is listed for a person to decide.

## Install

[![Download the skills (zip)](https://img.shields.io/badge/Download_the_skills-zip-0f7a52?style=for-the-badge)](https://github.com/strachcity/gov-communication-skills/releases/download/downloads/gov-communication-skills-plugin.zip)

There are 3 ways to use it. Pick the one that fits the tool you have.

### Add it as a plugin

This repository is a plugin marketplace, so it stays up to date.

In claude.ai, Cowork or the Claude desktop app:

1. Go to Customize, then Plugins.
2. Select Add, then Add marketplace.
3. Enter `strachcity/gov-communication-skills`.
4. Install "GOV.UK communication skills".

A plugin added on claude.ai is also available in Claude Code when you sign in with the same account.

In Claude Code on its own, run:

```
/plugin marketplace add strachcity/gov-communication-skills
/plugin install gov-communication-skills@gov-communication-skills
```

To try it from a local copy instead:

```
claude --plugin-dir path/to/gov-communication-skills
```

### Download the skills as a zip

Use this if you can't add a marketplace, or want a copy to share.

1. [Download the plugin (zip)](https://github.com/strachcity/gov-communication-skills/releases/download/downloads/gov-communication-skills-plugin.zip).
2. In Claude, go to Customize, then Plugins, then upload the zip. Don't unzip it first.

If your plan has Skills but not Plugins, upload these one at a time under Customize, then Skills:

- [government-communication](https://github.com/strachcity/gov-communication-skills/releases/download/downloads/gov-communication-skills-government-communication.zip)
- [case-communication-patterns](https://github.com/strachcity/gov-communication-skills/releases/download/downloads/gov-communication-skills-case-communication-patterns.zip)
- [privacy-aware-communications](https://github.com/strachcity/gov-communication-skills/releases/download/downloads/gov-communication-skills-privacy-aware-communications.zip)
- [govuk-content](https://github.com/strachcity/gov-communication-skills/releases/download/downloads/gov-communication-skills-govuk-content.zip)

Upload all 4. The front door uses the other 3.

A download doesn't update itself. Download it again to get changes.

### Use it in Microsoft 365 Copilot

1. [Download the Copilot version (zip)](https://github.com/strachcity/gov-communication-skills/releases/download/downloads/gov-communication-skills-copilot.zip), and extract it. On Windows, right-click it and choose Extract All. On a Mac, double-click it.
2. In Copilot Chat, select Create agent. If it opens a chat with the agent builder, select Skip or Configure.
3. Open "1 Paste into Instructions.txt", copy everything in it, and paste it into the Instructions box.
4. Under Skills, upload each zip in "2 Upload these 4 skills", one at a time. Don't unzip or rename them.
5. If there's no Skills option, upload the 4 files in "3 No Skills option - upload these as knowledge instead" under Knowledge instead.
6. Select Create.

The Copilot version hasn't been tested yet. See `ports/testing.md`.

### Using it

Claude uses the skills when a task fits, or you can ask for one by name, like "use govuk-content to review this email".

## Using it for your service

1. Install the plugin.
2. Tell it about your service, or point it to your service's documentation.
3. It creates a service context, or reads the one you already have.
4. It finds the generic case communication pattern that fits your request.
5. It adapts the pattern using your service's confirmed facts.
6. It runs privacy and policy checks.
7. It applies GOV.UK content guidance.
8. It returns a first draft, and lists anything that still needs a decision from your service.

The service context holds your service's facts and decisions, like its terminology, case states, timescales, channels, sender details and confirmed policy or disclosure decisions. Keep it in your own project, not in this repository. `ARCHITECTURE.md` describes what it can contain.

## How the repository is organised

- `skills/`: one folder per skill. Each skill holds its own guidance in `references/` and lists its sources in `sources.md`
- `evals/`: worked examples that test whether the skills behave correctly, one folder per skill. They use invented services only
- `ports/`: builds the downloads and the Microsoft 365 Copilot version from `skills/`. See `ports/README.md`

There's no folder for any named service. Each directory has a README that sets out what belongs there and what does not.

## Skills

| Skill | What it does | Status |
|---|---|---|
| `government-communication` | the front door. Helps you create a service context, then uses the other skills to draft or review a whole communication | draft, evals run once, see `evals/results.md` |
| `case-communication-patterns` | the 9 moments case-based services share, a substantially written pattern for each, a feedback follow-up, and how to recognise and adapt them | draft. Every pattern adapted for 3 invented services, evals run once, see `evals/results.md` |
| `privacy-aware-communications` | lists what a message reveals in each channel, applies confirmed decisions, flags the rest, and drafts the communications part of a DPIA | tested, see `evals/results.md` |
| `govuk-content` | drafts and reviews content against GOV.UK guidance, and flags privacy and policy questions without answering them | tested, see `evals/results.md` |

## Rules that keep it service-agnostic

- no skill refers to a named service, or uses a named service's words
- service facts come from the user's service context, at the point of use
- a service context can narrow generic guidance, but must say so and give a reason
- nothing from a service context is added to the plugin without a recorded decision and a generic source

## Working here

Read `CLAUDE.md` before adding or changing anything. It covers how knowledge is added, where it goes, and what to do when a position is not known. `ARCHITECTURE.md` explains what we are building and how the parts fit. `PLAN.md` has the build plan.

No build step to use it, no package manager, no framework. Everything is Markdown, except 2 small scripts:

- `python3 evals/text-message-lengths.py` checks every text message baseline fits in one text
- `python3 ports/build.py` builds the downloads. A GitHub Action runs it for you when a skill changes

## Licence

This work is licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). The full text is in `LICENSE`.

Copyright 2026 strachcity and contributors.

You can:

- use it in your service, team or department
- copy, publish and share it
- edit, adapt and build on it

As long as you credit it. Use this statement, or link to it:

> Contains material from gov-communication-skills (https://github.com/strachcity/gov-communication-skills), licensed under the Open Government Licence v3.0.

Some files quote GOV.UK guidance and other public sector information. That material stays under its own licence, usually the Open Government Licence v3.0 too. Each skill's `sources.md` says where it came from.
