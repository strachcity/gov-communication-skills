# Pattern: We're waiting on someone else

Moment 3 in `../moments.md`. Draft, last revised 6 October 2026.

Lines starting with ">" are quotes. Lines starting with "Interpretation:" are ours. "How to use the baseline copy" in `../moments.md` explains the 2 kinds of placeholder.

## Purpose

To tell the customer their case depends on another person or organisation. It says whether they need to do anything, and when they'll hear next.

## Trigger

The service asks a third party for information or action and cannot continue until it arrives, or passes the case to another organisation for its next stage. The service context names the event and the third party.

## Customer situation

Nothing seems to be happening, and they don't know why. They may think the delay is their fault, or that their case has been lost.

## Customer questions

- what's happening while I wait?
- is it something I've done?
- do I need to do anything?
- how long will it take?
- will you tell me when something changes?

## Core information

Every version of this message says:

- the service is waiting for information or action from someone else
- whether the customer needs to do anything. Usually they don't, so say "You do not need to do anything now"
- when the customer will hear next

Interpretation: commit to when the service will next update the customer, not to when the third party will reply. The service controls the first and not the second. If the service hasn't confirmed an update commitment, keep it as a placeholder and flag it. Don't leave the line out.

## Optional information

Each of these needs a confirmed service decision. Without one, leave it out and flag it.

- who the service is waiting on
- what the service has asked for
- an expected timescale
- what the service will do if there's no reply, like chasing
- whether the customer can help, like by prompting the third party

## Placeholders

From the service context:

| Placeholder | What the service context supplies |
|---|---|
| [service name] | the name customers know the service by |
| [case] | the customer's word for their case |
| [who we've asked] | how the third party can be described, in each channel. See "Describing the third party" |
| [what we've asked for] | only if the service has confirmed it can be described |
| [next stage] | for variant E, what the other organisation will do |
| [update commitment] | how often or when the service updates customers while waiting |
| [timescale] | the expected wait, only if the service has a confirmed one |
| [if no reply] | what the service will do, as confirmed by a policy decision |
| [how you can help] | only if the service wants the customer to act |
| [tracking URL] | a full GOV.UK web address |
| [contact details] | how to get help, in the A to Z format, like "Telephone: 0300 000 0000" with opening times on separate lines |
| [sender] | who the message is from |
| [letter greeting] | from the service's letter template |

Filled for each message:

| Placeholder | Value |
|---|---|
| ((first name)) ((last name)) | the customer's full name, or the named contact's |
| ((reference)) | the case reference |
| ((update date)) | worked out from [update commitment] |
| ((third party name)) | only if the service has decided to name the third party, and the name changes from case to case |
| ((date)) | the date of the letter |

### Describing the third party

[who we've asked] can be written at different levels. Each level is a disclosure decision for the service, and can differ by channel:

- not described at all: "someone else"
- a general description: "another organisation"
- a role, like "the person you named on your [case]"
- a name, which may change from case to case: ((third party name))

Interpretation: the least revealing level that still lets the customer understand and act is the starting point. It's not a decision. If there's no confirmed decision, flag it.

## Variants

### A. Waiting has started

Use the baseline copy below.

### B. Still waiting

The service is still waiting after the first message. This was moment 16 (see "Changes to the moments" in `../moments.md`).

Only send it if there's something new to say, like a new update date, that the service has chased, or that the customer can now help. Don't repeat variant A.

```
We're still waiting for information we need from [who we've asked] before we can continue with your [case].

[We contacted them again on ((date chased)).]

You do not need to do anything now. We'll update you by ((update date)).
```

### C. What we were waiting for has arrived

The service has what it was waiting for. Close the loop the first message opened: say what happens next, and whether the customer needs to do anything.

```
We've received the information we were waiting for from [who we've asked]. We'll [next step] by [timescale].

You do not need to do anything now.
```

### D. The third party cannot help, so the customer needs to act

Use "We need something from you", variant B. Start with what's changed, then the request. Don't blame the third party unless the service has decided it can.

### E. Passed to someone else for the next stage

Another organisation is doing the next stage of the case itself, like an inspection or an assessment, rather than sending information back. Replace the first line with:

```
Your [case] has been passed to [who we've asked], who will [next stage].
```

Say whether they'll contact the customer directly, if the service context confirms it. If not, flag it.

### Not this pattern

- the service is waiting on the customer: use "We need something from you"
- the service's own work is taking longer: use the delay modifier on the relevant moment

## Modifiers that apply

- **delay:** the wait is longer than the customer was told. Say so, say they don't need to do anything if that's true, and give a new update date. See "Modifiers" in `../moments.md`

## Common failure modes

- naming the third party, or what was asked for, without a confirmed decision
- making the customer think the delay is theirs
- blaming the third party, like "your [who we've asked] has not replied", without a confirmed decision. That can also disclose information about the third party
- no next update, so the customer phones to ask
- a timescale that depends on the third party, presented as the service's commitment
- a "still waiting" message with nothing new in it
- promising to chase when the service hasn't confirmed it does

## Privacy and policy checkpoints

Check these with `privacy-aware-communications`. Don't decide them here.

- **who:** can the third party be described, and at what level, in each channel? Naming some third parties, like a health professional, can reveal special category information
- **whose information:** the description can reveal information about someone other than the customer, like a person they care for. Treat that as carefully as the customer's own
- **what:** can what was asked for be described, in each channel?
- **the third party's information:** telling the customer the third party hasn't replied is information about the third party too
- **what the customer already knows:** if the customer named or chose the third party, describing them may reveal less. That's still a decision for the service
- **chasing and no reply:** what happens if there's no reply is a policy decision. A communication judgement doesn't settle it. Don't infer it
- **channel:** describing the third party in a text is higher risk. The lower-risk option says only that the case is waiting and points to a more secure route. Check the channel's risk heuristics

## Baseline copy

Leave out any line for something the service doesn't have, like a tracking route. Don't force every part into every channel.

### Email

```
Subject: [Service name]: update on your [case]

Dear ((first name)) ((last name))

We're waiting for information we need from [who we've asked] before we can continue with your [case].

You do not need to do anything now.

Your reference number is ((reference)).

What happens next

We'll update you by ((update date)), or sooner if we get what we need.

[Optional: If we do not hear from them by ((date)), we'll [if no reply].]

You can check the progress of your [case] at [tracking URL]

If you need help, contact us:
[contact details]

[Sender]
```

### Text message

With an update date:

```
Your [case] is waiting for information from someone else. You do not need to do anything. We'll update you by ((update date)).
```

With a tracking route instead:

```
Your [case] is waiting for information from someone else. You do not need to do anything. Track it: [tracking URL]
```

As a pointer, if the service sends the detail by email or letter, or has decided texts must say less:

```
We've sent you [an email / a letter] about your [case]. You do not need to do anything now.
```

Interpretation: these versions don't describe the third party, following the text message risk heuristics in `privacy-aware-communications`. A service can say more in a text only with a confirmed decision. Both the date and the web address would usually go over 160 characters, so choose one.

See "Text messages" in `../moments.md` for counting characters and sender IDs.

### Letter

```
Reference: ((reference))
((date))

We're waiting for information about your [case]

[letter greeting]

We're waiting for information we need from [who we've asked] before we can continue with your [case].

You do not need to do anything now.

What happens next

We'll write to you again by ((update date)), or sooner if we get what we need.

[Optional: If we do not hear from them by ((date)), we'll [if no reply].]

Check progress or get help

You can check the progress of your [case] at [short tracking URL].

If you need help, contact us:
[contact details]

Have your reference number ready.

[Sender]
```

The main sources don't cover how to greet or sign off a letter. Use the service's letter template, and flag it if there isn't one.

### Status page, behind sign-in

```
Status: Waiting for information

We're waiting for information we need from [who we've asked].

You do not need to do anything now.

We'll update you by ((update date)).
```

## Evidence

- **status:** seen in 2 services. No main source describes this need directly. Adapted for 3 invented services. Not yet tested with users
- **HM Passport Office**, "How we communicate with customers" (published): tells customers when "we send an email to their digital referee asking them to complete the referee section of the application", when "the referee has completed the application", and when "we reject their referee and need a new one"
- **unpublished design work in one service:** the moment occurs. No detail is recorded

### Tested against the evidence

Interpretation, from adapting this pattern back to each source:

- both services tell the customer when the wait starts and when it ends. That supports variant C as part of this pattern
- a published service names the role of a third party the customer chose. That added the "what the customer already knows" checkpoint
- when the third party can't be used, a published service asks the customer for someone else. That's variant D, handing over to "We need something from you"
- "no action needed" and "you need to act" need sharply different wording, so they're separate variants
- the evidence doesn't say what services do if the third party never replies. [if no reply] stays a policy placeholder

### Adapted for invented services

Interpretation, from adapting this pattern for a permit, a benefit and a registration service on 6 October 2026:

- a channel-specific disclosure decision mapped cleanly onto the levels for describing the third party
- one service passed the case to another organisation for the next stage, rather than waiting for information. Variant E was added
- one service named a different organisation for each case. ((third party name)) was added
- a third party linked to a person the customer cares for could reveal that person's health information. The "whose information" checkpoint was added
- a service recorded chasing as a communication judgement. The checkpoint now says that doesn't settle a policy question
