# Plan

How we get from an empty structure to working skills for drafting and reviewing government communications.

This file is a working plan, not guidance. Archive it once the first skills are built.

Sources reviewed on 6 October 2026.

## Scope

The first skills cover 4 channels:

- web pages in prototypes
- emails
- text messages
- letters

The first service is DVLA Drivers Medical.

Out of scope for now:

- NHS guidance, which will become its own service-specific skill later
- NHS App messages, phone scripts and web chat
- Welsh

## 1. Main sources

These 3 sources are the basis for all generic knowledge. Every entry in `knowledge/content-design/` cites at least one of them.

### GOV.UK content and publishing guidance

https://guidance.publishing.service.gov.uk/

- **what it is:** how to write for GOV.UK, including the writing guidelines, the A to Z style guide and the technical A to Z
- **what we take:** plain English, tone, active voice, must and need to, contractions, structure, headings, lists, links, titles, and the A to Z rules for numbers, dates, punctuation, capitals and words to avoid
- **applies to:** all 4 channels for language and style, and web pages for titles, summaries and page structure
- **why it applies beyond web pages:** the Service Manual says emails and text messages should "Follow the Government Digital Service (GDS) style guide"
- **caveats:** the site is in public beta, so links may move. It's written for GOV.UK content pages, not service pages, emails or letters, so each entry says which channels it applies to

### GOV.UK Service Manual

https://www.gov.uk/service-manual

The pages we use:

- "Planning and writing text messages and emails": https://www.gov.uk/service-manual/design/sending-emails-and-text-messages
- "Writing for user interfaces": https://www.gov.uk/service-manual/design/writing-for-user-interfaces

What it covers:

- **for emails and text messages:** when to send them, transactional and subscription messages, choosing a channel, protecting users from phishing, personalising messages, being concise and giving clear instructions
- **for prototype web pages:** wording for service pages, like headings, buttons and short instructions

What it applies to:

- emails, text messages and prototype web pages
- it has no page on letters

Caveats:

- the email and text message page was last updated in 2017, before UK GDPR applied
- its examples don't always follow its own advice, so we won't use them as templates

### GOV.UK Notify guidance

https://www.notifications.service.gov.uk/using-notify

**What it covers:** what an email, text message or letter can technically contain if it's sent through GOV.UK Notify.

**What we take:**

- formatting: what each channel can and can't include, and that none of them can use bold or italics
- links and URLs
- personalisation and optional content
- text message sender IDs
- the letter specification

**Applies to:** emails, text messages and letters.

**Caveat:** it's only binding if the service sends through GOV.UK Notify. We don't know yet whether Drivers Medical does.

## 2. What each source covers, by channel

This shows where each piece of knowledge comes from. A dash means no main source covers it.

| Topic | Web page | Email | Text message | Letter |
|---|---|---|---|---|
| Plain English, tone, style | Publishing | Publishing | Publishing | Publishing |
| Structure, headings, lists | Publishing | Publishing, Notify | - | Publishing, Notify |
| Links | Publishing | Service Manual, Notify | Service Manual, Notify | Notify |
| Titles and summaries | Publishing | none | none | none |
| Wording on service pages | Service Manual | none | none | none |
| Components and patterns | - | none | none | none |
| When to send, choosing a channel | none | Service Manual | Service Manual | - |
| Greeting, sender, sign-off | none | Service Manual, Notify | Service Manual, Notify | - |
| Phishing protection | none | Service Manual | Service Manual | - |
| Formatting limits | none | Notify | - | Notify |
| Message length | none | none | - | Notify |
| What is too sensitive to send | - | Service Manual (one line) | Service Manual (one line) | - |

"None" means the topic doesn't apply to that channel.

## 3. Gaps the main sources don't fill

There are 4 gaps. Each needs a supporting source or a decision. Supporting sources are used only for their gap, and their entries say so.

### Gap 1: components and patterns for prototype pages

The Service Manual covers wording, but question pages, error messages, check answers and confirmation pages are documented in the GOV.UK Design System.

**Proposal:** add the GOV.UK Design System as a supporting source for prototype web pages only: https://design-system.service.gov.uk/

### Gap 2: how to write a letter

None of the 3 sources covers greetings, sign-offs, where the reference number goes, deadlines as dates or letter headings. Notify only covers what a letter can technically contain.

**Proposal:** use your colleague's govuk-style-writer skill as the supporting source for letter conventions only. This is the case where it's necessary. Entries based on it are marked "needs confirmation" and name it as the source.

### Gap 3: privacy and special category data

The Service Manual says only that some information is "too sensitive to be sent by email or text", and to ask your information assurance team. None of the 3 sources covers the law.

**Proposal:** use the legislation and ICO guidance as supporting sources for `knowledge/privacy/` only. Every entry is marked "needs confirmation", with the data protection officer (DPO) as owner.

- UK GDPR Article 9 and the Data Protection Act 2018, Schedule 1
- ICO guidance on special category data: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/
- ICO guide to data security: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/security/a-guide-to-data-security/

### Gap 4: text message length and formatting

Notify's formatting page lists what emails and letters can include, but not text messages. Notify's pricing page should cover the 160-character limit for one text message and how some characters count twice. The address I tried returned "not found".

**Proposal:** find the current Notify pages for both before writing `channel-text-message.md`. If Notify doesn't cover them, record them as open questions.

## 4. Where the main sources disagree

Each one gets recorded in the relevant entry, citing both sources, and the skills flag it rather than picking a side.

| Topic | Service Manual | Notify | Proposed handling |
|---|---|---|---|
| Link text in emails | spell out URLs in full | link text is fine in emails the recipient expects, or with more than 2 links | full URLs by default, and flag link text for checking |
| Short URLs | avoid redirects | a short URL from GDS or your IT team is fine | flag, because a short URL is a redirect |
| Which sites to link to | only the GOV.UK domain | no rule | GOV.UK only, and flag any other domain |

## 5. Decisions

### Already decided

- **main sources:** GOV.UK publishing guidance, the Service Manual and GOV.UK Notify
- **NHS guidance:** excluded for now, and a future service-specific skill
- **your colleague's skill:** can be reused, but only where the main sources have a gap

### Recommended, waiting for you to confirm

- **supporting sources:** the 3 for gaps 1 to 3 above, each used only for its gap
- **conflicts:** GOV.UK is the default. A service can only depart from it through a recorded decision, and the skills flag any conflict they meet
- **skills:** 2 skills, review and draft, each taking the channel as an input. The review uses your 6-column table
- **Welsh:** out of scope for the first version, and recorded as an open question for DVLA

## 6. What to build

Each file below names its source. "Publishing" means the GOV.UK publishing guidance.

### `knowledge/content-design/`

Language and style, all channels:

- `plain-english.md`: Publishing
- `active-voice.md`: Publishing
- `modal-verbs.md`: Publishing, "Use clear language", the section "Make requirements clear"
- `contractions.md`: Publishing
- `tone.md`: Publishing
- `numbers.md`: Publishing
- `dates-and-times.md`: Publishing
- `money.md`: Publishing
- `capitalisation.md`: Publishing
- `punctuation.md`: Publishing
- `words-to-avoid.md`: Publishing

Structure:

- `front-loading.md`: Publishing
- `headings.md`: Publishing, Notify
- `bullet-lists.md`: Publishing, Notify
- `numbered-steps.md`: Publishing, Notify
- `links.md`: Publishing, Service Manual, Notify

Web pages:

- `titles.md`: Publishing
- `summaries.md`: Publishing
- `service-page-wording.md`: Service Manual
- `question-pages.md`: Design System (gap 1)
- `error-messages.md`: Design System (gap 1)
- `check-answers.md`: Design System (gap 1)
- `confirmation-pages.md`: Design System (gap 1)

Channels:

- `channel-email.md`: Service Manual, Notify
- `channel-text-message.md`: Service Manual, Notify
- `channel-letter.md`: Notify, and your colleague's skill (gap 2)
- `channel-web-page.md`: Publishing, Service Manual
- `when-to-send-messages.md`: Service Manual
- `phishing-protection.md`: Service Manual

### `knowledge/privacy/`

All from gap 3, all "needs confirmation":

- `special-category-data.md`
- `what-a-message-can-reveal.md`: including what the sender name, subject line or envelope reveals on its own
- `channel-email.md`
- `channel-text-message.md`
- `channel-letter.md`
- `channel-web-page.md`
- `requests-for-personal-information.md`
- `third-parties-and-carers.md`
- `transactional-and-subscription-messages.md`: starts from the Service Manual's claim that you don't need permission to send transactional messages, which needs checking against UK GDPR and the Privacy and Electronic Communications Regulations (PECR)

### `services/drivers-medical/`

Taken from DTx-experiments `drivers-medical/DESIGN.md`, all marked "needs confirmation" with DVLA policy as owner:

- `vocabulary.md`: words customers recognise, and internal terms never to use
- `waits-and-timescales.md`
- `decision-language.md`: open question
- `channels.md`: which channels the service uses, and whether it sends through Notify. Unknown
- `legal-basis.md`: open question, owned by the DVLA DPO
- `departures-from-guidance.md`: any recorded decisions to depart from GOV.UK
- `open-questions.md`

### `skills/`

- `review-communication/SKILL.md`: your style check prompt turned into a skill. It outputs the 6-column table. Privacy and service findings go in the same table, with "Confused / Uncertain?" used for anything needing confirmation
- `draft-communication/SKILL.md`: works out the context, drafts for the channel, runs the same checks as the review, and ends with "Check before publishing"

### `evals/`

1 folder per skill. Each case is a short Markdown file with the input, channel, service, what the skill must do and what it must not do.

The first cases:

- a web page passage with known style errors
- a passage with nothing wrong, to check nothing gets flagged
- an email that breaks the Service Manual's phishing rules
- a text message whose sender name reveals a health condition
- a Drivers Medical letter reviewed without service knowledge, to check no service rules leak into the generic skill
- the same letter reviewed with service knowledge
- a draft request where the legal position is unknown, to check the skill flags it rather than guessing

Running the evals is manual for now. Only add tooling if that becomes painful.

## 7. Build order

Each step is small enough to review on its own.

1. Confirm the recommended decisions in section 5.
2. Add the first content design entries: plain English, active voice, modal verbs, contractions, punctuation, words to avoid, numbers, and dates and times.
3. Build `review-communication` for web pages only, with 3 evals.
4. Add the email, text message and letter entries, and widen the review skill and its evals to cover them.
5. Add the privacy entries, marked "needs confirmation", with 2 privacy evals.
6. Add Drivers Medical service knowledge, with the leak test eval.
7. Build `draft-communication`, reusing the same knowledge and evals.

## 8. Open questions

| Question | Who could answer |
|---|---|
| Does Drivers Medical send emails, texts and letters through GOV.UK Notify? | DVLA service team |
| Which channels does Drivers Medical use now, and which are planned? | DVLA service team |
| Can a text message or email mention that it is about a medical case at all, including in the sender name or subject line? | DVLA DPO |
| What is the lawful basis for processing health data in Drivers Medical, and does it limit channels? | DVLA DPO, legal |
| Does DVLA say a decision is made at first notification? | DVLA policy |
| What do DVLA's Welsh language duties require for these communications? | DVLA Welsh language team |
| Is "You don't need to ask permission to send transactional messages" still correct under UK GDPR and PECR? | DPO, or ICO guidance |

## 9. Reviewed and not used

- **NHS digital service manual content guide:** excluded for now. It's good guidance, and it becomes a source when the NHS service-specific skill is built
- **govuk-design-guide:** it's about GOV.UK website templates, not writing
- **prompt-to-page:** it only hosts app installers, and the app is proprietary
