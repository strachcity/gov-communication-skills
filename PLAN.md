# Plan

How we get from the current skills to a pattern library any government service can use.

This file is a working plan, not guidance. `ARCHITECTURE.md` describes the design, and takes precedence where the 2 differ. Sections 1 to 9 and 12 record the source review from 6 October 2026, which still applies.

## State of play

Last updated 6 October 2026.

- `govuk-content` and `privacy-aware-communications` are tested, with blind-marked evals
- `case-communication-patterns` has 9 moments, 3 modifiers and 1 follow-up, "Ask for feedback". Every one has a pattern, adapted for 3 invented services, with evals run once
- `government-communication`, the front door, exists in draft with its own evals, run once
- testing with users is planned for later. Until then, no pattern is marked "tested with users"
- the repository is licensed under the Open Government Licence v3.0

## Current work package

Do these in order. Each pattern follows the same method as the first 3: compare the evidence, write the pattern, adapt it for 2 or 3 invented services, fix what breaks, then write and run its evals.

### 1. Write the remaining 9 patterns

Done on 6 October 2026. Writing them reduced 12 moments to 9. See "Changes to the moments" in `moments.md`.

Most evidenced and most distinct first. The less evidenced, more ambiguous moments come last, so they can still be merged or removed if writing the pattern shows they're weak.

1. We couldn't reach you (moment 7)
2. We've made a decision (moment 8)
3. We're closing your case (moment 11)
4. We'll contact you (moment 6)
5. What happens after the decision (moment 9)
6. You need to act before a date (moment 10)
7. Here's a record of what we discussed (moment 12)
8. Work has started (moment 2)
9. Something has changed (moment 4). Check its evidence first, because most of it was a wait ending, now part of moment 3

### 2. Add "ask for feedback" as a follow-up, not a moment

Done on 6 October 2026, in `patterns/ask-for-feedback.md`.

A feedback or satisfaction request doesn't communicate a case state. It's attached to another moment, so it's a follow-up, not moment 13.

- **where it can follow:** a case closing, a decision, a completed interaction, or delivery of what was applied for
- **guardrails:** say why feedback is wanted and how long it takes, never imply it affects the case, and don't invite sensitive case detail in free text unless the research design supports it
- **classification:** say whether it's a service message, research or promotion. Its lawful basis and whether the customer can opt out need checking. Don't assume it's a service message

Record it in `moments.md` alongside the modifiers, with its own pattern file.

### 3. Resolve the sole trader question in the privacy skill

Done on 6 October 2026.

Add ICO guidance on what is personal data. Information about a legal entity, like a limited company, is generally not personal data. Information about an identifiable sole trader, partner, director or employee can be, where it relates to them as an individual.

Interpretation for the skill: never treat "business information" as automatically outside UK GDPR. Cite the ICO page in `sources.md`, and replace the flag in `moments.md` under "When the customer is an organisation".

### 4. Replace the consent question with a framework for kinds of message

Done on 6 October 2026, in `privacy-aware-communications/references/kinds-of-message.md`.

Don't build a "consent needed: yes or no" table. Consent on its own is the wrong question, and a binary table invites 2 mistakes: "we have consent, so we can send anything" and "we don't have consent, so we can't send an update".

Add a reference to `privacy-aware-communications` called "Service messages, optional messages and marketing". It separates 3 questions:

1. Is this a service message or direct marketing?
2. What UK GDPR lawful basis supports processing the person's data?
3. Does the person have an objection or preference the service must consider?

And 4 kinds of message:

| Kind | Example | Consent before sending? | Other questions |
|---|---|---|---|
| core service message | receipt, request for evidence, decision | usually not needed just because it's an email or text | lawful basis, transparency, suitable contact details and channel |
| optional service update | proactive progress updates, convenience reminders | may not be needed if necessary and proportionate to the service's function, but preferences and objections matter | the service should say whether it's optional |
| feedback or satisfaction | "tell us about your experience" | depends on its purpose and lawful basis. Don't assume it's a service message | research or marketing, and whether taking part is genuinely optional |
| promotional message | promoting an unrelated service | direct marketing rules may apply | PECR and UK GDPR |

Source: the ICO's guidance on direct marketing and the public sector. It says purely administrative messages, like appointment reminders and acknowledgements of applications, are not direct marketing. It also says people may have a right to object where a public authority relies on public task. Quote the source, and mark the table as interpretation, needing confirmation.

Reword the line in `principles.md` that says the ICO "qualifies" the Service Manual's statement on permission. The 2 don't contradict each other. The rule is: you generally don't need marketing-style opt-in to send a service message, but you still need a lawful basis, transparency, and to consider rights and communication preferences.

This closes the open question in section 11.

### 5. Rename "default positions" in the privacy skill

Done on 6 October 2026. Privacy evals rerun, see `evals/results.md`.

"Default position" reads too much like an organisation's policy, even when marked as interpretation. Rename them "risk heuristics" in `ARCHITECTURE.md`, `privacy-aware-communications/SKILL.md` and its references, and reword each one as a risk, not a rule. For example:

> Risk heuristic: treat special category information, or wording that lets it be inferred, as high risk in a text message. A confirmed service position is needed before including it.

Check the patterns and the front door for the old wording, and rerun the privacy evals afterwards, because their expectations use it.

### 6. Treat curly apostrophes as a technical precaution

Done on 6 October 2026.

Notify's text message pricing page lists standard characters, and says non-standard characters cut the limit to 70, but doesn't say whether curly apostrophes are standard. Keep straight apostrophes in text message baselines, and describe this as a technical precaution, not a GOV.UK writing rule. A test message through Notify would settle it. It doesn't hold up the library.

### 7. Drop "public beta" as a special risk

Done on 6 October 2026.

Any web guidance can move. Remove the public beta warnings from `CLAUDE.md`, `govuk-content/sources.md` and section 3 of this plan. Replace them with one maintenance rule: check source addresses and dates when a skill is materially updated, or when a link fails.

### 8. Test with a new team

The next big question is how well the plugin works for a team that installs it with no prior knowledge. Once the library is complete:

- give it to someone outside this work, with only the README
- ask them to set up a service context and draft messages for their own service
- record where they got stuck, and fix the instructions rather than adding rules

### Before the full blind evaluation

Found while writing and testing the remaining patterns, 6 October 2026:

- decide whether a service context fact with no status, like the service's own name, should block a draft. The rule treats it as "needs confirmation", which made 2 runs overly cautious
- simplify nested optional placeholders in the baselines, which could be sent half-filled
- decide how to handle a standing duty with no due date, recorded in "Gaps" in `moments.md`
- add evals for an organisation customer, a Welsh language duty, and a message with promotion added
- check that each pattern's text baselines fit in 160 characters with long but realistic values

### Alongside the work package

- test the patterns with users, later. A test pack can be written then
- rerun all evals 3 times each, marked blind, with comparison runs, before calling any skill ready

## Scope

The first skills cover 4 channels:

- web pages in prototypes
- emails
- text messages
- letters

The skills work for any government service. Service facts come from the user's service context, never from this repository.

Out of scope for now:

- NHS guidance. A service that needs it can bring it in its own service context
- NHS App messages, phone scripts and web chat
- Welsh

## 1. Kinds of knowledge

Keeping these apart is the point of the structure. Only the generic kinds live in this repository.

| Kind | Example | Where it lives |
|---|---|---|
| GOV.UK content guidance | "Put the most important information at the top." | generic, in the content skill |
| Privacy principle | "Do not request personal information in an email or text message." | generic, in the privacy skill |
| Service policy decision | "We can tell the customer we have asked [who was asked] for information in circumstances X and Y." | the user's service context, not this repository |
| Service communication judgement | "When a case is waiting on someone else, say who, because otherwise people phone to ask." | the user's service context, not this repository |

Case communication patterns are a third generic kind, in `case-communication-patterns`. How a service context records its facts is set out in `ARCHITECTURE.md`.

## 2. Skills

There are 4 skills. `case-communication-patterns` is described in `ARCHITECTURE.md`. The other 3 are described here.

### `govuk-content`

Drafts and reviews content using GOV.UK guidance.

- covers user needs, plain English, structure, tone, accessibility, style, and the differences between web pages, emails, text messages and letters
- the review output is your 6-column style check table
- recognises when content involves personal information, and says a privacy check is needed
- never makes a privacy, legal or policy judgement

### `privacy-aware-communications`

Spots privacy issues in a communication.

- knows the principles: data minimisation, transparency, purpose limitation and special category data
- names the exact question that needs a policy or legal answer
- never decides a lawful basis or what an organisation may disclose

The skill works like this:

1. Spot the issue, for example "this may disclose third-party medical information".
2. Check whether the service has a recorded policy decision that covers it.
3. If one exists, apply it and cite it.
4. If not, flag the question and say who could answer it.

### `government-communication`

The front door. Combines the other skills with the user's service context, to draft or review a whole communication. Each step happens in order.

1. Establish the service context: read the one given, or help the user create one.
2. Work out what the communication is for, and which pattern fits.
3. Work out what the customer needs to understand and do.
4. Adapt the pattern using the service's confirmed facts.
5. Run a privacy check if the communication involves personal or sensitive information.
6. Apply any confirmed service decision that covers the issue, or flag it if none does.
7. Apply GOV.UK content guidance.
8. Draft or review.
9. List assumptions and unresolved questions.

Flagging what isn't known is the most valuable thing this skill does.

## 3. Main sources

These 3 sources are the basis for all generic content knowledge.

### GOV.UK content and publishing guidance

https://guidance.publishing.service.gov.uk/

- **what it is:** how to write for GOV.UK, including the writing guidelines, the A to Z style guide and the technical A to Z
- **what we take:** plain English, tone, active voice, must and need to, contractions, structure, headings, lists, links, titles, and the A to Z rules for numbers, dates, punctuation, capitals and words to avoid
- **applies to:** all 4 channels for language and style, and web pages for titles, summaries and page structure
- **why it applies beyond web pages:** the Service Manual says emails and text messages should "Follow the Government Digital Service (GDS) style guide", and its letters page says to "adapt the writing standards that apply to digital content"

### GOV.UK Service Manual

https://www.gov.uk/service-manual

The pages we use:

- "Planning and writing text messages and emails": https://www.gov.uk/service-manual/design/sending-emails-and-text-messages
- "Writing effective letters": https://www.gov.uk/service-manual/design/writing-effective-letters
- "Writing for user interfaces": https://www.gov.uk/service-manual/design/writing-for-user-interfaces
- "Collecting personal information from users", for the privacy skill: https://www.gov.uk/service-manual/design/collecting-personal-information-from-users

**What it covers:**

- **messages:** when to send an email, text message or letter, and how to choose between them
- **structure:** how to structure letters
- **trust:** protecting users from phishing and personalising messages
- **service pages:** wording, like headings and buttons
- **personal information:** minimising what you collect, being clear about legal basis, and explaining in plain English what you collect and why

**Caveats:**

- **the pages are old:** the email and text page dates from 2017 and the letters page from 2019, both before current data protection law
- **the examples aren't templates:** they don't always follow the pages' own advice

### GOV.UK Notify guidance

https://www.notifications.service.gov.uk/using-notify

**What it covers:** what an email, text message or letter can technically contain when sent through GOV.UK Notify.

**What we take:**

- formatting: none of the 3 channels can use bold or italics
- links and URLs
- personalisation and optional content
- text message sender IDs
- the letter specification

**Caveat:** it only applies if the service sends through Notify. The service context says whether it does.

## 4. What each source covers, by channel

"Publishing" means the GOV.UK publishing guidance. A dash means no main source covers it. "None" means the topic doesn't apply to that channel.

| Topic | Web page | Email | Text message | Letter |
|---|---|---|---|---|
| Plain English, tone, style | Publishing | Publishing | Publishing | Publishing |
| Structure, headings, lists | Publishing | Publishing, Notify | - | Service Manual, Notify |
| Links | Publishing | Service Manual, Notify | Service Manual, Notify | Service Manual, Notify |
| Titles and summaries | Publishing | none | none | none |
| Wording on service pages | Service Manual | none | none | none |
| Components and patterns | - | none | none | none |
| When to send, choosing a channel | none | Service Manual | Service Manual | Service Manual |
| Greeting and sender | none | Service Manual, Notify | Service Manual, Notify | - |
| Sign-off | none | - | none | - |
| Phishing protection | none | Service Manual | Service Manual | - |
| Formatting limits | none | Notify | - | Notify |
| Message length | none | none | - | Notify |
| Personal information | Service Manual | Service Manual | Service Manual | Service Manual |

## 5. Gaps and supporting sources

A supporting source is used only for its gap, and its entries are marked "needs confirmation".

| Gap | Proposed supporting source |
|---|---|
| Components and patterns for prototype pages | GOV.UK Design System, for prototype pages only: https://design-system.service.gov.uk/ |
| Greeting and sign-off in letters, and sign-off in emails | your colleague's govuk-style-writer skill. This gap is now much smaller, because the letters page covers structure |
| Privacy law | UK GDPR, the Data Protection Act 2018 and ICO guidance, for the privacy skill only |
| Text message formatting | Notify covers length (on its pricing page) but not formatting. The skill treats text messages as plain text and marks that as interpretation |

The ICO says some of its guidance is under review following the Data (Use and Access) Act. Privacy entries need their "last checked" date kept up to date, and should be checked again before any real use.

## 6. Where sources disagree

Each one is recorded in the relevant reference, citing both sources. The skills flag it rather than picking a side.

| Topic | One source says | Another says | Proposed handling |
|---|---|---|---|
| Web addresses in messages | Service Manual (emails and texts): spell them out in full and avoid redirects | Service Manual (letters): use short URLs where possible, and Notify: short URLs from GDS or your IT team are fine | full addresses in emails and texts, short addresses allowed in letters |
| Link text in emails | Service Manual: spell out URLs in full | Notify: link text is fine in expected emails, or with more than 2 links | full URLs by default, flag link text |
| Which sites to link to | Service Manual: only the GOV.UK domain | Notify: no rule | GOV.UK only, flag any other domain |
| Tone of letters | Service Manual: "no reason to strike a more formal tone in a letter" | your colleague's skill: "formality builds trust" | follow the Service Manual, since it's a main source |

## 7. Where things live

Decided on 6 October 2026: guidance lives inside each skill, following standard practice for agent skills. The shared `knowledge/` folder has been removed.

See "Repository structure" in `ARCHITECTURE.md`. There's no `services/` folder.

- each skill works on its own, so it can be shared as a single file
- privacy guidance can only be used through the privacy skill
- the core principles go in `SKILL.md`, and detail goes in a few reference files read only when needed
- each skill lists its sources in `sources.md`

## 8. Source material

**This repository is public.** Real communications, case details or internal policy emails must never be committed.

- keep raw material in a local folder that git ignores, `_source-material/`
- use it only as evidence that a moment occurs, recorded without naming the service
- a service's own material belongs in that service's own service context, in their own project

## 9. Evals

1 folder per skill. Each case is a short Markdown file with:

- the input
- the channel and service
- what the skill must do
- what it must not do

For `govuk-content`, there are 5 cases, covering what it should improve and what it should leave alone:

- a web page passage with known style errors
- a passage with nothing wrong, to check nothing is flagged
- an email that breaks the phishing rules
- a vague status message, like "Your application is currently with our specialist team and will be processed in due course." The skill should flag the vague status, the passive voice, the missing next step, the unclear timescale and the likely unanswered question
- the same message, testing the boundary: the skill must not decide to say who hasn't replied, because that's a disclosure and policy question

For `privacy-aware-communications`:

- a text message whose sender name reveals a health condition
- a draft that discloses third-party medical information where no policy decision exists, so the skill must flag it rather than decide
- the same draft where a recorded policy decision does exist, so the skill must apply and cite it

For `government-communication`, using invented services:

- a request with no service context, to check the skill helps build one and no service rules leak in
- the same request with a service context, to check confirmed facts are used and unconfirmed ones are flagged

Running the evals is manual for now. Only add tooling if that becomes painful.

## 10. Build order

Steps 1 to 4 are done: where things live, `govuk-content`, `privacy-aware-communications` and the moments. The first 3 patterns and the front door are in draft. "Current work package" at the top has the next steps.

## 11. Open questions

Each service's own open questions belong in its service context, not here.

| Question | Who could answer |
|---|---|
| None at the moment. The question about permission for transactional messages is answered by step 4 of the work package | |

## 12. Reviewed and not used

- **NHS digital service manual content guide:** excluded. An NHS service can bring it into its own service context
- **govuk-design-guide:** it's about GOV.UK website templates, not writing
- **prompt-to-page:** it only hosts app installers, and the app is proprietary
