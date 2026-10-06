# Channels

What each channel can expose, and risk heuristics for each.

Last checked: 6 October 2026

Lines starting with ">" are quoted from the source. Lines starting with "Interpretation:" are ours. Every risk heuristic is our interpretation of the sources. It describes a risk, not an organisation's policy. It stays "needs confirmation" until an organisation's DPO or information assurance team confirms a position.

Each heuristic is marked:

- **high risk:** a confirmed service position is needed before including it
- **raised risk:** include it only if the person needs it, and say why

Rules quoted from a source, like the Service Manual's phishing rules, are not heuristics. They're stated as the source states them.

## Contents

- Rules for every channel
- Text messages
- Emails
- Letters
- Phone calls and voicemail
- Web pages and status trackers
- Choosing a channel

## Rules for every channel

From the Service Manual, "Planning and writing text messages and emails":

> Some information is too sensitive to be sent by email or text. You should consider this and discuss anything you're not sure about with your information assurance team.

When contacting users, the same page says "you must":

> leave out sensitive information, like bank details

> avoid making requests for personal information, like a user's date of birth

> only send links which point to the GOV.UK domain

From the ICO (see `principles.md`, "Security"): showing who receives a message can itself disclose confidential information.

Interpretation, for every channel:

- treat what is visible before opening (sender, subject, preview, envelope) as revealed to anyone who sees the device or the post
- treat inference the same as stating it. A sender name naming a medical team reveals health information as surely as naming a condition
- the reference number is personal data, because it identifies the person's case. It's usually needed, so include it, but do not add other identifiers

## Text messages

From GOV.UK Notify, "Security features":

> Text messages cannot provide end-to-end encryption.

> Text messages are stored and processed in: the UK and Ireland; the country where the recipient's phone is; the phone's country of origin (for international numbers)

Risk heuristics (interpretation):

- **high risk:** special category information, or wording that lets it be inferred, in the sender ID, the message or any link
- **raised risk:** case detail beyond what the person needs to act. The lower-risk option is to say there's an update and point to a more secure route, like signing in, an email or a call

From the Service Manual's phishing rules: avoid requests for personal information, and only link to the GOV.UK domain, with web addresses in full.

Reasoning: a text has no end-to-end encryption, often shows on a lock screen, and may be read on a shared phone. A phone number can also be out of date.

## Emails

From GOV.UK Notify, "Security features":

> We always try to encrypt emails using TLS 1.2, 1.1 or 1.0. If the recipient's mail server does not support TLS, we will send the email without protection.

> Email cannot provide end-to-end encryption.

From the Service Manual, emails must also "avoid sending attachments" and "include the user's first name and surname in the body of the email to make phishing more difficult".

Risk heuristics (interpretation):

- **high risk:** special category information, or wording that lets it be inferred, in the sender name, subject line or first line, because these show in previews
- **high risk:** special category information in the body
- **raised risk:** anything in the body the person doesn't need for this message

From the Service Manual: avoid attachments.

## Letters

From GOV.UK Notify, "Letter pricing": letters are sent in "C5 size envelopes with an address window".

From HM Passport Office, "Data protection: caseworker guidance", a published example of a department applying the accuracy principle:

> check the customer data and correct it if it is wrong (this will make sure any letters, emails or documents are sent to the correct address)

Risk heuristics (interpretation):

- **high risk:** anything beyond the name and address visible through the window or on the envelope, including a return address that reveals what the letter is about
- **raised risk:** detail the person doesn't need. A letter can carry more than a text or email, but others in the household may open post
- **raised risk:** sending anything sensitive without checking the address is current

The Service Manual letters page also says there "might also be a security or legislative reason for sending a letter", for example "sensitive information that you wouldn't want to put in an email".

## Phone calls and voicemail

From HM Passport Office, "Data protection: caseworker guidance":

> do not leave personal customer data or special category data as a message on an answerphone

From HMRC's "Information disclosure guide", IDG30230:

> When speaking on the telephone you must take every step to ensure that you do not disclose any HMRC information until you are wholly satisfied that the person you are speaking to is the person they claim to be.

Interpretation: 2 departments' published guidance apply the security principle in the same way. That supports the principle, but it is still each department's own policy.

Risk heuristics (interpretation):

- **high risk:** anything about the case in a voicemail. The lower-risk option says who is calling, a reference if needed, and how to call back
- **high risk:** discussing the case on a call before checking the person's identity. See `disclosure.md`

## Web pages and status trackers

From the Service Manual, "Collecting personal information from users":

> avoid putting personally identifiable information into page titles or H1s

From "Writing for user interfaces":

> Do not include personal information (like a user's name or date of birth) in the <title> field of a URL

Risk heuristics (interpretation):

- **high risk:** case detail on a page without a sign-in

From the Service Manual: avoid personal information in page titles, headings and web addresses.

## Choosing a channel

Interpretation, drawn from the heuristics above:

- the less secure the channel, the less it should say. A text or email can say there's an update and point somewhere more secure
- where a message must carry special category information, a letter or a page behind sign-in is usually the starting point, unless a confirmed decision says otherwise
- if the less revealing version would leave the person unable to act, flag the trade-off. Do not resolve it by revealing more

## Organisation decisions

An organisation's DPO or information assurance team may confirm, tighten or relax any heuristic here. Record their decision in the service's own service context, with owner and date. The skill then applies the decision instead of the heuristic.
