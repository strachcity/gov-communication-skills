# Channels

What each channel can expose, and a default position for each.

Last checked: 6 October 2026

Lines starting with ">" are quoted from the source. Lines starting with "Interpretation:" are ours. Every default position is our interpretation of the sources. Each one stays "needs confirmation" until an organisation's DPO or information assurance team confirms or replaces it.

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

Default position (interpretation):

- no special category information, and nothing that allows it to be inferred, in the sender ID, the message or any link
- no case detail beyond what the person needs to act. Say there's an update, and point to a more secure route, like signing in, an email or a call
- no requests for personal information
- full GOV.UK web addresses only

Reasoning: a text has no end-to-end encryption, often shows on a lock screen, and may be read on a shared phone. A phone number can also be out of date.

## Emails

From GOV.UK Notify, "Security features":

> We always try to encrypt emails using TLS 1.2, 1.1 or 1.0. If the recipient's mail server does not support TLS, we will send the email without protection.

> Email cannot provide end-to-end encryption.

From the Service Manual, emails must also "avoid sending attachments" and "include the user's first name and surname in the body of the email to make phishing more difficult".

Default position (interpretation):

- no special category information, or anything that allows it to be inferred, in the sender name, subject line or first line, because these show in previews
- in the body, only what the person needs for this message. Special category information needs a confirmed decision before it goes in the body
- no attachments

## Letters

From GOV.UK Notify, "Letter pricing": letters are sent in "C5 size envelopes with an address window".

From HM Passport Office, "Data protection: caseworker guidance", a published example of a department applying the accuracy principle:

> check the customer data and correct it if it is wrong (this will make sure any letters, emails or documents are sent to the correct address)

Default position (interpretation):

- nothing beyond the name and address visible through the window or on the envelope, including the return address
- a letter can carry more detail than a text or email, but only what the person needs. Others in the household may open post
- check the address is current before sending anything sensitive

The Service Manual letters page also says there "might also be a security or legislative reason for sending a letter", for example "sensitive information that you wouldn't want to put in an email".

## Phone calls and voicemail

From HM Passport Office, "Data protection: caseworker guidance":

> do not leave personal customer data or special category data as a message on an answerphone

From HMRC's "Information disclosure guide", IDG30230:

> When speaking on the telephone you must take every step to ensure that you do not disclose any HMRC information until you are wholly satisfied that the person you are speaking to is the person they claim to be.

Interpretation: 2 departments' published guidance apply the security principle in the same way. That supports the principle, but it is still each department's own policy.

Default position (interpretation):

- a voicemail says who is calling, a reference if needed, and how to call back. Nothing about the case
- verify identity before discussing anything on a call. See `disclosure.md`

## Web pages and status trackers

From the Service Manual, "Collecting personal information from users":

> avoid putting personally identifiable information into page titles or H1s

From "Writing for user interfaces":

> Do not include personal information (like a user's name or date of birth) in the <title> field of a URL

Default position (interpretation):

- case detail goes behind a sign-in
- no personal information in page titles, headings or web addresses

## Choosing a channel

Interpretation, drawn from the defaults above:

- the less secure the channel, the less it should say. A text or email can say there's an update and point somewhere more secure
- where a message must carry special category information, a letter or a page behind sign-in is usually the starting point, unless a confirmed decision says otherwise
- if the less revealing version would leave the person unable to act, flag the trade-off. Do not resolve it by revealing more

## Organisation decisions

An organisation's DPO or information assurance team may confirm, tighten or relax any default here. Record their decision in the service pack, with owner and date. The skill then applies the decision instead of the default.
