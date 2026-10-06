# Plan

How we get from an empty structure to working skills for drafting and reviewing government communications.

The first skills cover 4 channels:

- web pages in prototypes
- emails
- text messages
- letters

The first service is DVLA Drivers Medical.

This file is a working plan, not guidance. Delete or archive it once the first skills are built.

Sources reviewed on 6 October 2026.

## 1. Source review

Each source is rated for how much we should rely on it, what we take from it and where it goes.

### GOV.UK content and publishing guidance

https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/

- **authority:** primary. This is the GOV.UK standard
- **what it covers:** writing guidelines (user needs, clear language, structure, tone, titles, summaries, links, change notes), the A to Z style guide and the technical A to Z
- **take:** almost all of it, one rule per entry, quoted
- **goes to:** `knowledge/content-design/`
- **caveats:**
  - the site is in public beta, so links may move
  - the guidance is written for GOV.UK web pages, so some parts (summaries, change notes, titles for search) do not apply to emails, texts or letters, and each entry must say which channels it applies to
  - the guidance pages use en dashes themselves, so "no dashes" is your house rule for this repository, not a GOV.UK rule

Useful finding: the must, need to and can distinction is written down in "Use clear language", under "Make requirements clear". Your style check prompt says it isn't a literal A to Z entry, which is right, but it does have a citable source. "Should" as a recommendation is not defined there, so that part stays a convention.

### GOV.UK Service Manual

- "Planning and writing text messages and emails": https://www.gov.uk/service-manual/design/sending-emails-and-text-messages
- "Writing for user interfaces": https://www.gov.uk/service-manual/design/writing-for-user-interfaces

**Authority:** primary for services.

**Take:**

- channel choice, transactional and subscription messages
- personalising messages, being concise, giving clear instructions
- the phishing rules
- microcopy for prototype pages

**Goes to:**

- writing rules go to `knowledge/content-design/`
- the phishing and "too sensitive to send" rules also go to `knowledge/privacy/`

**Caveats:**

- **the email and text page is old:** it was last updated on 3 October 2017, before UK GDPR applied
- **one statement needs checking:** "You don't need to ask permission to send transactional messages" is a data protection claim, so it goes in as "needs confirmation", not as fact
- **its examples don't all follow its own advice:** for example, it says to sign off with "Regards" and uses an unexplained acronym, so the examples aren't templates
- **there's no letters page:** I checked 2 likely addresses and both were not found

### GOV.UK Design System

https://design-system.service.gov.uk/

- **authority:** primary for prototype web pages
- **take:** the wording guidance inside components and patterns, like question pages, error messages, check answers and confirmation pages
- **goes to:** `knowledge/content-design/`, as web page entries
- **caveat:** take wording guidance only, not markup, since DTx-experiments already holds the markup

### GOV.UK Notify guidance

https://www.notifications.service.gov.uk/using-notify/guidance

- **authority:** primary for what emails, texts and letters can technically contain, if the service sends through Notify
- **take:** formatting (emails can have headings, bullets, inset text and numbered steps, letters can have headings, bullets, numbered steps and page breaks, neither can have bold or italics), links and URLs, personalisation, text message sender names, the letter specification
- **goes to:** `knowledge/content-design/`, as channel entries
- **caveat:** whether Drivers Medical sends through GOV.UK Notify is a service fact we don't know yet

### Inclusive language

https://www.gov.uk/government/publications/inclusive-communication/inclusive-language-words-to-use-and-avoid-when-writing-about-disability

- **authority:** primary
- **goes to:** `knowledge/content-design/`
- **caveat:** this matters a lot for Drivers Medical, where every customer has a health condition or disability

### NHS digital service manual content guide

https://service-manual.nhs.uk/content

- **authority:** secondary. It's good, well-researched guidance, but it's the NHS's, not GOV.UK's
- **what it covers:** health literacy, voice and tone, the A to Z of NHS health writing, writing NHS messages (updated August 2026), numbers, punctuation, formatting and inclusive content
- **take:**
  - the health literacy evidence
  - the per-channel advice for emails, texts and letters
  - trust and phishing advice
  - writing to someone who has a carer
  - plain names for conditions
- **goes to:** a separate area, `knowledge/content-design/nhs/`, loaded only when a service chooses to adopt it (see decision 1)

**Caveats:**

- **it isn't a rulebook:** it says it is "a guide, not a rulebook", and defers to the GOV.UK A to Z for anything it doesn't cover
- **it conflicts with GOV.UK in places:** see section 3
- **its own example messages break its own advice:** for example, a letter says "within 30 days of the date of this letter", starts with "Please complete", and has a question as a heading. They're useful as eval inputs, not as models

### The govuk-style-writer skill (uploaded)

**Authority:** secondary. It's a summary of other sources, so every rule must be checked against its source before we use it.

**What's strong, and worth reusing as design ideas rather than content:**

- it works out the channel, reader and context before writing
- it lists what must never change, like eligibility, deadlines, amounts, legal duties and consequences
- it ends with a "Check before publishing" list of things to confirm
- it has a section on sensitive and difficult messages
- it has per-channel advice for letters, emails and texts

**Where it doesn't fit our architecture:**

- **it mixes layers:** generic GOV.UK rules, other organisations' guides and department rules sit in one file, which is the mixing this repository is designed to avoid
- **"the domain guide wins" happens automatically:** here, a service has to choose to adopt a guide, and record that it has
- **most of it is out of scope:** justice, HMRC, Home Office, functional standards and Welsh
- **some claims cite no source:** a few things I couldn't trace to a source, like "Dear" being "also safer for government generally". In fact the service manual does support "Dear" for emails, so that one can be cited properly

**Checked against the source and correct:**

- negative contractions
- the use of "one"
- must, need to and can
- Notify formatting for emails and letters

**What we'll do with it:** use it as a checklist of topics and as a reference for how the skills should work. We won't copy its text.

**Open question:** who wrote it, and can we reuse its structure?

### DTx-experiments `drivers-medical/DESIGN.md`

- **authority:** prototype design judgement for Drivers Medical, not confirmed DVLA policy
- **take:**
  - internal terms customers must never see
  - waits shown as a range with a reason
  - never a countdown or a percentage complete
  - who holds the case, in words customers recognise
  - the decision language open question
- **goes to:** `services/drivers-medical/`, as "needs confirmation" with DVLA policy named as owner
- **caveat:** these came from prototype work and research, not from a recorded policy decision

### Not used

- **govuk-design-guide:** it's about GOV.UK website templates, not writing, and has no licence file
- **prompt-to-page:** it only hosts installers, the app is proprietary, and its guidance comes from the GOV.UK Design System, which we use directly

### Privacy sources, not yet reviewed in depth

These are the sources the privacy work will need. I've confirmed they're reachable but haven't read them for content yet.

- ICO guidance on special category data: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/
- ICO guide to data security: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/security/a-guide-to-data-security/
- UK GDPR Article 9, and the Data Protection Act 2018 Schedule 1
- the Government Security Classifications policy, for what can go by email
- the NHS England "Messaging best practice" guidance, which the NHS content guide refers to for governance and channel choice. It's an example from health, not a rule for DVLA

## 2. Decisions needed

These change what gets built. I've made a recommendation for each.

### Decision 1: how to treat the NHS content guide

**Recommendation:** keep it as separate generic knowledge in `knowledge/content-design/nhs/`. Drivers Medical adopts individual entries by recorded decision, not the whole guide.

The reasons:

- DVLA is a GOV.UK service, so GOV.UK style is the default
- Drivers Medical customers are writing and reading about their health and their GP, so some NHS advice clearly helps
- adopting the whole guide would bring in things like numerals for "one", which contradict GOV.UK with no gain for DVLA customers

### Decision 2: what happens when sources conflict

**Recommendation:**

- GOV.UK is the default
- a service can depart from it only through a recorded service decision
- the skill flags any conflict it meets rather than picking a side

This is the opposite of the uploaded skill, where the domain guide wins automatically.

### Decision 3: which channels are in scope

**Recommendation:** in scope are web pages in prototypes, emails, text messages and letters.

Out of scope for now:

- NHS App messages
- phone and IVR scripts
- web chat
- Welsh

### Decision 4: how many skills

**Recommendation:** 2 skills, each taking the channel as an input.

- **`review-communication`:** your style check prompt turned into a skill. It outputs your 6-column table, adds privacy and service findings to the same table, and uses "Confused / Uncertain?" for anything needing confirmation
- **`draft-communication`:** works out the context, drafts for the channel, then runs the same checks as the review and ends with "Check before publishing"

That's better than 1 skill per channel, because the rules are mostly shared and a fix should only happen once.

### Decision 5: Welsh

**Recommendation:** out of scope for the first version, but record it as an open question for Drivers Medical.

DVLA is based in Swansea and probably has Welsh language duties, but we don't know what they require for these communications.

## 3. Conflicts found so far

Each one gets recorded in the relevant knowledge entry, citing both sources.

| Topic | GOV.UK | NHS | Proposed handling |
|---|---|---|---|
| The number one | "one" in prose | numerals for all numbers | GOV.UK by default |
| "Should" | not defined in GOV.UK guidance | avoid, can sound patronising | GOV.UK by default, flag "should" for checking |
| Bold in letters | GOV.UK Notify letters cannot have bold | letters can have bold | depends on how the service sends letters, which is a service fact |
| Greeting in texts | not needed | start with the person's name | open question for each service |
| Email sign-off | the service manual example uses "Regards" | "Yours sincerely" | flag, there's no GOV.UK rule |
| Links in messages | only GOV.UK domain links | NHS.UK or GOV.UK | GOV.UK by default |

## 4. What to build

### `knowledge/content-design/`

Each entry says which channels it applies to.

These are grouped for planning only. Each one is a separate file.

**Writing:**

- `meet-user-needs.md`
- `plain-english.md`
- `active-voice.md`
- `modal-verbs.md`
- `contractions.md`
- `tone.md`
- `inclusive-language.md`

**Structure:**

- `front-loading.md`
- `headings.md`
- `bullet-lists.md`
- `numbered-steps.md`
- `links.md`

**Style:**

- `numbers.md`
- `dates-and-times.md`
- `money.md`
- `capitalisation.md`
- `punctuation.md`
- `words-to-avoid.md`

**Web pages only:**

- `titles.md`
- `summaries.md`
- `question-pages.md`
- `error-messages.md`
- `check-answers.md`
- `confirmation-pages.md`

**Channels:**

- `channel-email.md`
- `channel-text-message.md`
- `channel-letter.md`
- `channel-web-page.md`

**Accessibility:**

- `accessibility.md`

### `knowledge/content-design/nhs/`

Only the entries Drivers Medical might adopt:

- `health-literacy.md`
- `naming-conditions.md`
- `writing-to-people-with-carers.md`
- `trust-and-phishing.md`

### `knowledge/privacy/`

Every entry starts as "needs confirmation", with the data protection officer (DPO) as owner.

- `special-category-data.md`
- `what-a-message-can-reveal.md`: including what the sender name, subject line or envelope reveals on its own
- `channel-email.md`
- `channel-text-message.md`
- `channel-letter.md`
- `channel-web-page.md`
- `requests-for-personal-information.md`
- `third-parties-and-carers.md`
- `transactional-and-subscription-messages.md`

### `services/drivers-medical/`

- `vocabulary.md`: customer-facing words, and internal words never to use
- `waits-and-timescales.md`
- `decision-language.md`: open question
- `channels.md`: which channels the service uses and how it sends them. Unknown
- `legal-basis.md`: open question, owned by the DVLA DPO
- `adopted-guidance.md`: which NHS entries the service has adopted, and departures from GOV.UK
- `open-questions.md`

### `skills/`

- `review-communication/SKILL.md`
- `draft-communication/SKILL.md`

### `evals/`

1 folder per skill. Each case is a short Markdown file with input, channel, service, must do and must not do.

The first cases:

- a GOV.UK web page passage with known style errors
- a passage with nothing wrong, to check nothing gets flagged
- the NHS address-check letter from the content guide, which breaks several rules
- a text message whose sender name reveals a health condition
- a Drivers Medical letter reviewed without service knowledge, to check no service rules have leaked into the generic skill
- the same letter reviewed with service knowledge
- a draft request where the legal position is unknown, to check the skill flags it rather than guessing

Running the evals is manual for now: run the skill on each case and check it against the case's list. Only add tooling if that becomes painful.

## 5. Build order

Each step is small enough to review on its own.

1. Agree decisions 1 to 5.
2. Add the content design entries a review needs first: plain English, active voice, modal verbs, contractions, punctuation, words to avoid, numbers, and dates and times.
3. Build `review-communication` for web pages only, with 3 evals.
4. Add the email, text message and letter channel entries, and widen the review skill and its evals to cover them.
5. Add the privacy entries, marked "needs confirmation", with 2 privacy evals.
6. Add Drivers Medical service knowledge from DTx-experiments, all marked "needs confirmation", with the leak test eval.
7. Build `draft-communication`, reusing the same knowledge and evals.
8. Add the NHS entries Drivers Medical adopts, if decision 1 says so.

Step 3 gives you a working review skill early. It's also the version of your style check prompt that cites real sources.

## 6. Open questions

| Question | Who could answer |
|---|---|
| Does Drivers Medical send emails, texts and letters through GOV.UK Notify? | DVLA service team |
| Which channels does Drivers Medical use now, and which are planned? | DVLA service team |
| Can a text message or email mention that it is about a medical case at all, including in the sender name or subject line? | DVLA DPO |
| What is the lawful basis for processing health data in Drivers Medical, and does it limit channels? | DVLA DPO, legal |
| Does DVLA say a decision is made at first notification? | DVLA policy |
| What do DVLA's Welsh language duties require for these communications? | DVLA Welsh language team |
| Who wrote the govuk-style-writer skill, and can we reuse its structure? | you |
| Is "You don't need to ask permission to send transactional messages" still correct under UK GDPR and the Privacy and Electronic Communications Regulations (PECR)? | DPO, or ICO guidance |
