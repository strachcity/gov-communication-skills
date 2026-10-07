# Follow-up: Ask for feedback

A follow-up, not a moment. See "Follow-ups" in `../moments.md`. Draft, last revised 6 October 2026.

Lines starting with ">" are quotes. Lines starting with "Interpretation:" are ours. "How to use the baseline copy" in `../moments.md` explains the 2 kinds of placeholder.

## Why it's a follow-up

Asking for feedback doesn't tell the customer anything about their case. It follows another moment, like a decision, or is attached to it. It's also a different kind of message, with its own privacy questions.

## Purpose

To invite the customer to say what they thought of the service, in a way that's clearly optional and can't affect their case.

## When to send it

The Service Manual says:

> You must allow users to tell you what they think of your service once they've finished using it.

> Sometimes the end of a transaction is not the end of a user's experience with the service.

> to measure satisfaction with the whole service, make sure you have a way to collect feedback at the very end of a user's involvement with it (the 'end point').

> For example, for users claiming Carer's Allowance, you could set up a system where you email them when they get a decision.

> Services often have many different end points for users. Make sure there's a way to collect feedback at all of them.

Interpretation: the end points are the places this follow-up can go:

- after a decision
- after a case closes without a decision
- after what was applied for has been delivered
- after a completed interaction, like a call or an appointment

## Customer questions

- what are you asking, and why?
- how long will it take?
- do I have to?
- will it affect my case?
- who will see what I say?

## Core information

Every version says:

- what's being asked, and why
- how long it takes
- that it's optional
- that it won't affect their case or any decision
- how to take part

Interpretation: say "it will not affect your [case]" in plain words. A customer waiting on a decision, or thinking about challenging one, may worry that a bad review counts against them.

## Optional information

- what the service does with feedback
- how to stop being asked, if the service offers it
- how to give feedback another way, like by phone

## Placeholders

From the service context:

| Placeholder | What the service context supplies |
|---|---|
| [service name] | the name customers know the service by |
| [case] | the customer's word for their case |
| [what it won't affect] | anything else the customer might worry it affects, like a later inspection or a rating by another organisation, as the service has confirmed |
| [how long] | how long the survey takes, tested, not estimated |
| [survey URL] | a full web address. See the checkpoints on the domain |
| [other ways] | another way to give feedback, like phone or post |
| [how to take part] | for letters, a full sentence, like how to use a reply form and prepaid envelope, or a phone number |
| [what we do with it] | only if the service has confirmed it |
| [how to stop] | only if the service offers it |
| [sender] | who the message is from |

Filled for each message:

| Placeholder | Value |
|---|---|
| ((first name)) ((last name)) | the customer's full name |

## Variants

### A. After a decision

Send it separately from the decision, or after it in its own clearly separate section. Never put it in a formal notice.

Interpretation: asking for feedback straight after a refusal can feel careless. When to ask, and whether to ask after every outcome, is a service decision.

### B. After a case closes without a decision

The Service Manual says services should try to get feedback from users who drop out, "as they'll likely have important insights". Be careful with tone: the case may have closed because the customer didn't reply.

### C. After delivery

After what was applied for has arrived, at the end of the process. If the decision and delivery happen together, ask once, after both.

Interpretation: if another organisation continues the customer's journey, like an inspection after registration, this may not be the end of their experience. Say what the feedback is about.

### D. After a completed interaction

After a call, appointment or visit. For phone or face-to-face support, the Service Manual mentions a survey by phone, using interactive voice response (IVR), or "a follow-up survey by post".

## Common failure modes

- not saying it's optional, or that it won't affect the case
- inviting free text that encourages the customer to describe their case, health or circumstances
- a feedback request inside a formal notice or a refusal
- asking so often that customers stop reading messages from the service
- a survey link that looks like phishing, because it isn't on GOV.UK
- adding promotion, which can turn the message into direct marketing

## Privacy and policy checkpoints

Check these with `privacy-aware-communications`. Don't decide them here.

- **kind of message:** is this a service message, research or promotion? Don't assume it's a service message. The ICO page on direct marketing in the public sector doesn't cover feedback requests. See `kinds-of-message.md`
- **lawful basis:** what lawful basis supports processing the person's data to send it, and to collect their answers? This is for the DPO
- **objections and preferences:** can the customer stop these requests, and does the service have to? This is for the DPO
- **free text:** don't invite sensitive case details by default. If the research needs them, the research design must support it, and the DPO should confirm
- **survey domain:** the Service Manual says emails and texts should "only send links which point to the GOV.UK domain". Many survey tools use other domains. This is a conflict to flag, not to resolve
- **survey supplier:** if a supplier runs the survey, they may process the customer's data. Flag it for the DPO
- **channel and timing:** a text late at night, or straight after bad news, is a judgement for the service. Use the channel the customer uses. For customers who don't use email or texts, the Service Manual mentions a survey by post or by phone

## Baseline copy

Leave out any line for something the service doesn't have.

### Email

```
Subject: [Service name]: tell us what you thought

Dear ((first name)) ((last name))

We'd like to know what you thought of [service name], so we can improve it.

It takes about [how long]. It's optional, and it will not affect your [case] or any decision about it.

[If there's something else the customer might worry it affects:]
It will not affect [what it won't affect] either.
[End if]

Please do not include personal details or details of your [case].

Give feedback: [survey URL]

[If there are other ways to give feedback:]
You can also give feedback [other ways].
[End if]

[Sender]
```

Interpretation: "please" is fine here. This is a request the customer can say no to, not an instruction.

The letter has no reference on purpose. Linking feedback to a case is a privacy question for the DPO, not a default.

### Text message

```sms
[Service name]: tell us what you thought. It's optional, takes [how long] and will not affect your [case]: [survey URL]
```

With a long service name and web address, this goes over 160 characters. Leave out the service name if the sender ID gives it.

### Letter

For customers who don't use email or a phone:

```
Tell us what you thought of [service name]

[letter greeting]

We'd like to know what you thought of [service name], so we can improve it.

It takes about [how long]. It's optional, and it will not affect your [case] or any decision about it.

[how to take part]

[Sender]
```

### As a section at the end of another message

Only where the service decides this is appropriate, and never in a formal notice:

```
Tell us what you thought

It takes about [how long]. It's optional, and it will not affect your [case]: [survey URL]
```

## Evidence

- **status:** supported by a main source. Not yet tested with users
- **Service Manual**, "Measuring user satisfaction": the quotes under "When to send it", and its points about users who drop out and about assisted digital support
- **Service Manual**, "Planning and writing text messages and emails": the rule on GOV.UK links
- **ICO**, "Direct marketing and the public sector": doesn't cover feedback requests. See `kinds-of-message.md`

### Evidence gaps

- no published source we've found says whether a public sector feedback request is a service message
- no published source shows how services word a feedback invitation
