# CLAUDE.md

This repository holds agent skills and supporting knowledge for UK government customer communications. Read `README.md` for the layout and `ARCHITECTURE.md` for the design. This file covers how knowledge is added and the rules that keep the layers apart.

## This repository is service-agnostic

The plugin must work for any government service without changes.

- do not create, propose or require skills, folders or packs for named services
- do not use a named service's words in pattern names, skill text, examples or the architecture
- service facts come from the user's service context, supplied at the point of use or kept in their own project. See "The service context" in `ARCHITECTURE.md`
- the plugin can help a user create a service context, but never stores one here

## Where things go

Ask one question first: would this still be true for a different government service?

- yes, and it comes from GOV.UK content guidance: `skills/govuk-content/references/`
- yes, and it is about personal data, channels or special category data: `skills/privacy-aware-communications/references/`
- yes, and it is a moment or pattern that case-based services share: `skills/case-communication-patterns/references/`
- no, it is true for one service only: not in this repository. It belongs in that service's own service context
- it describes how to carry out a drafting or review task: the skill's `SKILL.md`
- it is a worked example with an expected result: `evals/<skill>/`, using an invented service

If you are not sure, leave it out and record the question. Something wrongly kept out does little harm. Something wrongly made generic changes the output for every service.

Do not create a new top-level directory without asking.

## Service policy must not be silently promoted

Service-specific policy must never be moved, copied or rephrased into generic knowledge or a generic skill without an explicit, recorded decision.

This includes doing it by accident. Watch for:

- a generic rule or pattern worded from one service's example, like a rule about "medical conditions" in content design guidance
- a skill that hardcodes a service's vocabulary, channels, timescales or decisions
- an eval for a generic skill that only passes if the skill knows a service's policy
- a service decision restated as "best practice" because it seemed sensible

A service rule can become generic only when:

1. A generic source supports it, like the GOV.UK style guide, the ICO or the legislation itself.
2. The generic entry cites that source, not the service.
3. The change is made in its own commit, and the commit message says what was promoted and why.

Until then it stays in that service's own context, outside this repository, even if it looks universal.

Patterns seen across services are evidence for a moment, recorded as described under "Evidence and provenance" in `ARCHITECTURE.md`. A published source is cited by name. Unpublished work only shows that a moment occurs, and the service is not named.

## Flag unknown positions, never infer them

If a legal or policy position is not known, say so. Do not fill the gap with a plausible guess.

This applies to knowledge entries, skill instructions and skill output alike.

- record an unknown position as an open question, with who could answer it if you know
- in skill output, flag the point for the user to check instead of choosing an answer
- never treat "this is common practice" or "other services do this" as evidence of a legal or policy position
- never infer a service's policy from its published content alone, because published content can be out of date or wrong
- if two sources disagree, record both and flag the conflict

A flagged gap is a useful result. A confident wrong answer about data protection or a licensing decision can harm a real person.

## How to add guidance to a skill

Each generic skill keeps its guidance in a small number of reference files in `references/`, grouped by when the agent needs them. The core principles needed for most tasks go in `SKILL.md` itself.

- quote or closely follow the source. Mark quotes with ">" and our own reading with "Interpretation:"
- add every source to the skill's `sources.md`, with its address, what we took from it, which file uses it and the date checked
- add a short example of right and wrong where it helps
- if a summary drifts from its source, the source wins and the summary is wrong until fixed
- if the guidance is silent, say so. Do not invent a rule

Content guidance cites at least one of the 3 main sources:

- GOV.UK content and publishing guidance: https://guidance.publishing.service.gov.uk/
- the GOV.UK Service Manual: https://www.gov.uk/service-manual
- GOV.UK Notify guidance: https://www.notifications.service.gov.uk/using-notify

A supporting source can be used only where the main sources have a gap. Say which gap it fills, and that it needs confirmation. `PLAN.md` lists the agreed supporting sources.

Web guidance can move or change. Check source addresses and dates when a skill is materially updated, or when a link fails.

Privacy guidance cites the legislation, ICO guidance, GOV.UK guidance, or a department's published guidance. It is not legal advice. Risk heuristics derived from these sources describe a risk, not a policy. They are marked as interpretation and "needs confirmation" until the organisation's data protection officer confirms a position.

## Service context

Service facts are never added here. The format a service context follows, and the kinds of fact it records (policy decision, communication judgement, precedent, hypothesis), are set out under "The service context" in `ARCHITECTURE.md`.

Never present a hypothesis or judgement as a policy decision.

Evals that need service facts use an invented service, written into the eval case.

## This repository is public

Use only publicly available sources. Never commit real communications, case details, personal data, internal documents or internal policy correspondence.

Unpublished material, like workshop outputs, can inform thinking but is never a source. If you need to look at it locally, keep it in `_source-material/`, which git ignores.

## How to add a skill

One folder per skill in `skills/`, following `skills/README.md`.

- `SKILL.md` starts with a `name` and a `description`. The description says what the skill does and when to use it
- keep `SKILL.md` under 500 lines, and say when to read each reference file
- a skill takes the service context as an input and contains no service rules
- add evals in `evals/<skill>/` before calling a skill ready

## Writing style for this repository

Everything here follows the guidance it holds.

- plain English, sentences under 25 words where possible
- British English
- bullets start lower case and have no full stop
- numbered steps are full sentences
- no em dashes or en dashes, except inside exact quotes from a source

## Keep it small

No build tooling, package manager, framework or schema validator. Add structure only when a real problem needs it, and say what the problem was.
