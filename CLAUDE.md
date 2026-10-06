# CLAUDE.md

This repository holds agent skills and supporting knowledge for UK government customer communications. Read `README.md` for the layout. This file covers how knowledge is added and the rules that keep the layers apart.

## Where things go

Ask one question first: would this still be true for a different government service?

- yes, and it comes from GOV.UK publishing guidance: `knowledge/content-design/`
- yes, and it is about personal data, channels or special category data: `knowledge/privacy/`
- no, it is true for one service only: `services/<service>/`
- it describes how to carry out a drafting or review task: `skills/`
- it is a worked example with an expected result: `evals/`

If you are not sure which, put it in the service folder and say why in the entry. Something wrongly kept specific does little harm. Something wrongly made generic changes the output for every service.

Do not create a new top-level directory without asking.

## Service policy must not be silently promoted

Service-specific policy must never be moved, copied or rephrased into generic knowledge or a generic skill without an explicit, recorded decision.

This includes doing it by accident. Watch for:

- a generic rule worded from one service's example, like a rule about "medical conditions" in content design guidance
- a skill that hardcodes a service's vocabulary, channels, timescales or decisions
- an eval for a generic skill that only passes if the skill knows a service's policy
- a service decision restated as "best practice" because it seemed sensible

A service rule can become generic only when:

1. A generic source supports it, like the GOV.UK style guide, the ICO or the legislation itself.
2. The generic entry cites that source, not the service.
3. The change is made in its own commit, and the commit message says what was promoted and why.

Until then it stays in the service folder, even if it looks universal.

## Flag unknown positions, never infer them

If a legal or policy position is not known, say so. Do not fill the gap with a plausible guess.

This applies to knowledge entries, skill instructions and skill output alike.

- record an unknown position as an open question, with who could answer it if you know
- in skill output, flag the point for the user to check instead of choosing an answer
- never treat "this is common practice" or "other services do this" as evidence of a legal or policy position
- never infer a service's policy from its published content alone, because published content can be out of date or wrong
- if two sources disagree, record both and flag the conflict

A flagged gap is a useful result. A confident wrong answer about data protection or a licensing decision can harm a real person.

## How to add a knowledge entry

One topic per file, in Markdown, named for the topic in lower case with hyphens, like `modal-verbs.md`.

Start each entry with these lines:

```
Source: <URL or document name>
Last checked: <date, like 6 October 2026>
Status: confirmed | needs confirmation | open question
Owner: <person or role who can confirm it, if known>
```

Then write the entry.

- quote or closely follow the source, and link to it
- keep what the source says separate from your interpretation of it
- add a short example of right and wrong where it helps
- if a summary drifts from its source, the source wins and the summary is wrong until fixed

Content design entries cite at least one of the 3 main sources:

- GOV.UK content and publishing guidance: https://guidance.publishing.service.gov.uk/
- the GOV.UK Service Manual: https://www.gov.uk/service-manual
- GOV.UK Notify guidance: https://www.notifications.service.gov.uk/using-notify

A supporting source can be used only where the main sources have a gap. The entry names the gap and is marked "needs confirmation". `PLAN.md` lists the agreed supporting sources.

The publishing guidance site is in public beta, so check links still work and update them if pages move.

Privacy entries cite the legislation, ICO guidance or a named internal decision. They are not legal advice. Anything that would change what a real communication contains needs confirming with the service's data protection officer or legal team, and its status should say so until it is.

Service entries also start with a `Kind:` line:

- `policy decision`: made by someone with authority, so say who and when
- `communication judgement`: a design decision based on research or experience
- `precedent`: wording that was approved or rejected, with the reason if known
- `hypothesis`: from prototypes or workshops, not yet tested or agreed

Never present a hypothesis or judgement as a policy decision.

## This repository is public

Never commit real communications, case details, personal data or internal policy correspondence.

Keep raw source material in `_source-material/`, which git ignores. Only add extracts that have been anonymised and cleared for publication.

## How to add a skill

One folder per skill in `skills/`, with a `SKILL.md` inside.

- the skill names which knowledge it loads, by path
- the skill does not copy knowledge into itself, so there is one place to fix it
- a generic skill takes the service as an input and contains no service rules
- add at least one eval in `evals/` before calling a skill ready

## Writing style for this repository

Everything here follows the guidance it holds.

- plain English, sentences under 25 words where possible
- British English
- bullets start lower case and have no full stop
- numbered steps are full sentences
- no em dashes or en dashes

## Keep it small

No build tooling, package manager, framework or schema validator. Add structure only when a real problem needs it, and say what the problem was.
