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

## 1. Four kinds of knowledge

Every piece of knowledge in this repository is one of these. Keeping them apart is the point of the structure.

| Kind | Example | Where it lives |
|---|---|---|
| GOV.UK content guidance | "Put the most important information at the top." | generic, in the content skill |
| Privacy principle | "Do not request personal information in an email or text message." | generic, in the privacy skill |
| Service policy decision | "We can tell the licence holder we have asked their GP for information in circumstances X and Y." | service folder |
| Service communication judgement | "When a case is waiting on a GP, say so, because otherwise people phone to ask." | service folder |

Service knowledge also records where it came from, because a prototype is not a policy:

- **policy decision:** made by someone with authority, with their name or role and the date
- **communication judgement:** a design decision based on research or experience
- **precedent:** wording that was approved or rejected, with the reason if known
- **hypothesis:** an idea from prototypes or workshops that hasn't been tested or agreed

## 2. Skills

There are 3 skills. Each of the first 2 owns one kind of generic knowledge. The third combines them with service knowledge.

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

Combines the other 2 skills with service knowledge, to draft or review a whole communication. Each step happens in order.

1. Work out what the communication is for.
2. Work out what the customer needs to understand and do.
3. List the facts that are known.
4. Run a privacy check if the communication involves personal or sensitive information.
5. Apply any service policy that covers the issue, or flag it if none does.
6. Apply the service's communication judgements.
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
- **caveats:** the site is in public beta, so links may move

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

**Caveat:** it only applies if the service sends through Notify. We don't know yet whether Drivers Medical does.

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
| Text message formatting and length | find the current Notify pages. If Notify doesn't cover them, record them as open questions |

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

There's one structural choice to make. Everything else follows from it.

### Option 1: knowledge inside each skill (recommended)

Each generic skill holds its own reference files. Service knowledge stays outside, as data.

```
skills/
  govuk-content/
    SKILL.md
    references/
    sources.md
  privacy-aware-communications/
    SKILL.md
    references/
    sources.md
  government-communication/
    SKILL.md
services/
  drivers-medical/
evals/
```

Why I'd choose this:

- **each skill works on its own:** it can be shared as a single file, the way your colleague shared theirs, which doesn't work if it points to a separate `knowledge/` folder
- **the boundary is built in:** privacy knowledge can only be used through the privacy skill
- **you can test each layer alone:** this matches the build order below

### Option 2: keep the current shared `knowledge/` folder

All skills read from one shared knowledge folder.

- it's simpler if many skills need the same knowledge
- the skills can't be shared on their own

### Reference files

Either way, I'd use fewer, larger reference files than the plan had before:

- **the core:** the principles an agent needs in most tasks go in `SKILL.md` itself
- **the rest:** a small number of reference files hold guidance that's only needed sometimes, like the A to Z rules, or the rules for one channel
- **sources:** each skill has a `sources.md` listing every source with its title, address, date checked and what we took from it
- **marking interpretation:** in every file, text marked as our interpretation is kept separate from what a source says

About 30 tiny files would be harder for an agent to reason with than about 6 well-organised ones.

## 8. Source material for Drivers Medical

The most useful material for the service layer is real:

- existing communications
- wording that was debated
- written answers from data protection or policy
- any DVLA correspondence standards

**This repository is public.** Real communications, case details or internal policy emails must never be committed.

I'd handle source material like this:

- keep raw material in a local folder that git ignores, like `_source-material/`
- add only extracts that have been anonymised and cleared for publication, recorded in `services/drivers-medical/` with their kind and source
- if that's too restrictive, make the repository private before adding anything sensitive

When extracts are added, the job is to classify them, not to merge them into rules straight away:

| Source | Kind |
|---|---|
| DTx-experiments `DESIGN.md` | communication judgement or hypothesis |
| GOV.UK guidance | generic content guidance |
| ICO or data protection guidance | generic privacy principle |
| A policy email | service policy decision |
| An approved customer letter | precedent |
| A prototype | hypothesis |

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
- a Drivers Medical status message with the policy question taken out. For example, "Your application is currently with our medical team and will be processed in due course." The skill should flag the vague status, the passive voice, the missing next step, the unclear timescale and the likely unanswered question
- the same message, testing the boundary: the skill must not decide to say "your GP hasn't replied", because that's a disclosure and policy question

For `privacy-aware-communications`:

- a text message whose sender name reveals a health condition
- a draft that discloses third-party medical information where no policy decision exists, so the skill must flag it rather than decide
- the same draft where a recorded policy decision does exist, so the skill must apply and cite it

For `government-communication`:

- a Drivers Medical letter without service knowledge, to check no service rules leak into the generic skills
- the same letter with service knowledge

Running the evals is manual for now. Only add tooling if that becomes painful.

## 10. Build order

The rhythm for each step is: take a source, extract the principles, test them against examples, refine, then add the next source.

1. Choose an option for where things live (section 7), and restructure the folders if needed.
2. Build `govuk-content`, using the main sources only.
3. Test it with the 5 evals, including Drivers Medical examples with the policy questions taken out. Refine.
4. Build `privacy-aware-communications`, with every entry marked "needs confirmation". Test it with its 3 evals.
5. Add Drivers Medical as a service. Classify the source material, starting with `DESIGN.md`, rather than turning it into rules.
6. Build `government-communication`, with the leak test eval.

## 11. Open questions

| Question | Who could answer |
|---|---|
| Does Drivers Medical send emails, texts and letters through GOV.UK Notify? | DVLA service team |
| Which channels does Drivers Medical use now, and which are planned? | DVLA service team |
| Can a text message or email mention that it is about a medical case at all, including in the sender name or subject line? | DVLA DPO |
| What is the lawful basis for processing health data in Drivers Medical, and does it limit channels? | DVLA DPO, legal |
| In what circumstances can DVLA tell a customer it is waiting for their GP? | DVLA policy, DPO |
| Does DVLA say a decision is made at first notification? | DVLA policy |
| What do DVLA's Welsh language duties require for these communications? | DVLA Welsh language team |
| Is "You don't need to ask permission to send transactional messages" still correct under UK GDPR and PECR? | DPO, or ICO guidance |
| Should this repository stay public once service material is added? | you |

## 12. Reviewed and not used

- **NHS digital service manual content guide:** excluded for now. It becomes a source when the NHS service-specific skill is built
- **govuk-design-guide:** it's about GOV.UK website templates, not writing
- **prompt-to-page:** it only hosts app installers, and the app is proprietary
