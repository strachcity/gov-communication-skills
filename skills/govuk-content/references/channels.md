# Channels

What changes for each channel: web content pages, service pages in prototypes, emails, text messages and letters.

Last checked: 6 October 2026

Lines starting with ">" are quoted from the source. Lines starting with "Interpretation:" are ours. Every source is listed in `../sources.md`.

## Contents

- Rules for every channel
- Web content pages
- Service pages in prototypes
- Emails
- Text messages
- Letters
- Known conflicts between sources
- Gaps

## Rules for every channel

The writing guidelines and A to Z apply to every channel:

- the Service Manual says emails and text messages should "Follow the Government Digital Service (GDS) style guide and write clearly using clear language"
- the Service Manual letters page says "You can adapt the writing standards that apply to digital content"

From "Planning and writing text messages and emails" (Service Manual), which covers emails and texts:

> Don't explain back-end processes or policy. Give the user just enough information so they know what to do next

The same page says to:

- make it clear what you need the user to do, and include any deadlines
- say what will happen if they don't do what you're asking
- explain what you'll do next and when they'll hear from you, and if you won't contact them again, make it clear that it's the end of the process

Interpretation: the letters page asks for the same things (the action, and "what happens next if the user does not do the action"), so treat these 3 as the standard for every message.

If the service sends through GOV.UK Notify, its formatting rules apply:

> You cannot use bold, italics, underlined text, different typefaces or fonts. This is because they can make it harder for people to read what you've written.

Interpretation: if you do not know whether the service uses Notify, follow the Notify rules anyway and flag it. They are stricter, so the content will work either way.

## Web content pages

These are pages like GOV.UK guidance, rather than steps in a service.

Structure, from "Clear structure":

> Put the most important information first.

- headings: descriptive, front-loaded, active where possible, and the content should still make sense with them removed
- headings should not be questions, because "they're hard to frontload and users want answers, not questions"
- the page title is the H1, so content uses H2, H3 and H4
- a start button goes under a heading that relates to its task, like "Apply online"
- no footnotes
- do not repeat the summary in the first paragraph

Titles, from "Clear titles" and the A to Z:

- 65 characters or less, including spaces
- unique, clear and descriptive, front-loaded and using the words people search for
- a colon can break up a longer title
- no dashes, slashes or full stop at the end, and not a question
- use the active verb ("Submit") if the page is for doing something, and the present participle ("Submitting") if it's guidance about doing something elsewhere
- do not include the content type, like "guidance"

Summaries, from "Summaries":

- 160 characters or less, including spaces
- end with a full stop
- active, including a verb
- do not mention the content type or repeat the title

Links, from "Add links":

- links go in body text, not in titles, summaries or subheadings
- put links where they're useful, not in a list at the bottom
- avoid anchor links where possible

Change notes, from "Change notes": a substantive change to a published page may need a change note. Interpretation: this does not apply to prototypes.

## Service pages in prototypes

These are the pages of a transaction, like questions, check answers and confirmation pages.

Source: "Writing for user interfaces" (Service Manual).

> So start with less.

> If you find yourself having to explain how the user interface works, that's a sign something has gone wrong.

- short sentences, one idea per sentence, important words first
- "now" is usually not needed, like "apply" rather than "apply now"
- headings can be questions on service pages
- every input still needs a question directly associated with it, for screen readers
- one H1 per page, describing what the page does
- the page title follows the format "Where do you live? - Register to vote - GOV.UK"
- if the service is speaking, the user is "you" and the service is "we". If the user is speaking, use "I", "me" or "my"
- headings and input labels are sentence case with no full stop. Other text is in full sentences with a full stop
- avoid acronyms inside the transaction. If you use one, spell it out on each page

Tone:

> Be approachable and helpful, but not overly familiar. Remember that it's government 'speaking'.

- say "sorry" only if something serious has gone wrong, like the service stopping
- no "sorry" in validation error messages
- usually no "please" or "thank you", like "Application complete" rather than "Thank you for your application"
- no humour in error messages

> If people do not notice your copy, you're probably doing it right. Aim to be boring.

Accessibility: do not rely on shape, size, colour or location, like "click the green button" or "use the menu on the left".

Personal information:

> Do not include personal information (like a user's name or date of birth) in the <title> field of a URL

"Collecting personal information from users" also says to avoid personal information in page titles or H1s. Interpretation: flag it if a prototype puts personal information in a heading or title.

Gap: question pages, error messages, check answers and confirmation pages are documented in the GOV.UK Design System, which this skill doesn't cover yet. Flag anything that depends on a component pattern.

## Emails

Source: "Planning and writing text messages and emails" (Service Manual), unless stated.

When to send:

- "Always consider whether you can send an email or text message instead of a letter."
- some information is too sensitive to send by email or text. Interpretation: flag this for a privacy check, do not decide it
- only send messages that meet a user need, like transactional messages (about something the user has done) or subscription messages (that the user asked for)
- never send subscription messages unless the user asked for them, and always give a way to unsubscribe

Writing:

- say who the message is from. The service name may mean more than the department name
- tailor the subject line, like "visa application" rather than "application". Subject lines are often shortened
- start with "Dear [firstname lastname]", not "Hi"
- include a reference number and contact details if the user might need to contact you
- keep it short, and say only one important thing in each message
- put the most important information in the first sentence, so it shows in the preview
- no jargon or acronyms without explanation

Protecting users from spam and phishing. The page says "you must":

> leave out sensitive information, like bank details

> avoid making requests for personal information, like a user's date of birth

> only send links which point to the GOV.UK domain

> spell out any web addresses (URLs) in full to show the user where links are going

> avoid including redirects in any links - for example, tracking

> avoid sending attachments with emails

> include the user's first name and surname in the body of the email to make phishing more difficult

Formatting, from Notify "Formatting":

- emails can include bullet points, headings, horizontal lines, inset text and numbered steps
- no bold, italics or underlining
- headings and subheadings in sentence case. The first subheading must come after a heading

Links, from Notify "Links and URLs":

- write the URL in full, and Notify turns it into a link
- link text may be useful for long URLs, unsubscribe links, or emails with more than 2 links
- "If the recipient is not expecting to receive an email from you, we recommend using the URL instead of link text."
- never use "click here", "click link", "this link" or "more"
- do not use a third-party link shortening service

There's a conflict between these link rules. See "Known conflicts".

## Text messages

Source: "Planning and writing text messages and emails" (Service Manual), unless stated.

The when-to-send, writing and phishing rules for emails also apply to text messages, except:

- you don't need to start with "Dear" or "Hi"
- the attachment rule doesn't apply

Avoid sending text messages late at night if you can. Avoid sending an email and a text message at the same time unless there's a very good reason.

Length, from Notify "Text message pricing":

- a message over 160 characters, including spaces, counts as more than one message
- a message with non-standard characters, like Welsh accented letters, counts as more than one message after 70 characters

Interpretation: count characters and flag any message over 160, or over 70 if it has non-standard characters.

Sender, from Notify "Text message sender ID": the sender ID tells users who the message is from. The default is "GOVUK".

Formatting: Notify says you cannot use Markdown to add link text to a text message. Notify's formatting page lists options for emails and letters only. Interpretation: write text messages as plain text, using line breaks rather than headings or bullets, and write links as full URLs.

## Letters

Source: "Writing effective letters" (Service Manual), unless stated.

When to send a letter. The page says it's probably better to send a letter if:

- users need a hard copy
- the letter is formatted in a way you can't make accessible in an email
- research shows your users expect or prefer letters

There might also be a security or legal reason for a letter. Otherwise, if the message is short and simple, send a text or email.

Structure:

> start with user needs - know what you want the user to do when they get the letter and leave out any information that isn't directly relevant to that task

> put the most important information at the top - this includes explaining what the letter's about and any action a user needs to take

Important information includes:

- any reference or phone numbers the user needs
- a brief summary of why the user is getting the letter, perhaps as a headline, like "You need to renew your licence"
- where relevant, what happens next if the user does not do what the letter asks

Tone:

> There's no reason to strike a more formal tone in a letter, despite the perception that they should be more formal than digital content.

The page says research found legal jargon especially confusing, and that users find short letters easier to follow than long ones.

Links: "Use short URLs where possible". This conflicts with the email and text message rule. See "Known conflicts".

Accessibility: think about font sizes, and do not rely on colour alone.

Formatting, from Notify "Formatting":

- letters can include bullet points, headings, numbered steps and page breaks
- no bold, italics or underlining
- you cannot use Markdown link text in a letter

Size, from Notify "Letter specification" and "Letter pricing": A4 portrait, 10 pages or less (5 double-sided sheets), sent in a C5 envelope with an address window.

Interpretation: anything printed in the address window area can be seen from outside the envelope. Flag any content placed there for a privacy check.

Gap: none of the main sources covers how to greet the reader or sign off a letter. Follow the template or service the user names, and flag it if there isn't one.

## Known conflicts between sources

Give both positions and flag the conflict. Do not pick one silently.

| Topic | One source | Another source | Default |
|---|---|---|---|
| Headings as questions | "Clear structure": headings should not be questions | "Writing for user interfaces": headings can be questions on service pages | no questions on content pages, questions allowed on service pages |
| Link text in emails | Service Manual: spell out web addresses in full | Notify: link text is fine for expected emails or more than 2 links | full addresses, and flag link text |
| Short addresses | Service Manual (emails and texts): avoid redirects | Service Manual (letters) and Notify: short addresses are fine | full addresses in emails and texts, short ones allowed in letters |
| Which sites to link to | Service Manual (emails and texts): only GOV.UK | "Add links": other sites are allowed in some circumstances | GOV.UK only in emails and texts, and flag any other site |

## Gaps

No main source covers these yet. Flag them when they come up:

- greetings and sign-offs in letters
- sign-offs in emails
- component and pattern wording for service pages, which is in the GOV.UK Design System
