---
name: government-communication
description: "The front door for drafting, adapting or reviewing a UK government service's customer communications, like emails, text messages, letters and status pages about a case. Use it whenever someone wants a message for their service, wants to check one, or wants to plan the messages for a case journey. It establishes the service's context first, creating one with the user if needed, then uses case-communication-patterns, privacy-aware-communications and govuk-content to return a first draft and a list of what still needs a service decision."
---

# Government communication

The front door to the plugin. It turns a request about one service's communications into a strong first draft, using generic patterns and the service's own facts.

It works for any government service. Service facts come from a service context, which belongs to the user. This skill contains no service's rules.

## Reference files

- `references/service-context.md`: always. What a service context contains, how to read one, and how to help the user create one

The other skills in this plugin hold the guidance:

- `case-communication-patterns`: which pattern fits, and the baseline copy
- `privacy-aware-communications`: what the message can reveal, in each channel
- `govuk-content`: how it's written

## How it works

Follow these steps in order. Don't skip a step because the request seems simple.

### 1. Establish the service context

Look for a service context in this order:

1. Something in the conversation, like pasted facts or an attached file.
2. A file in the user's project, usually called `service-context.md`.
3. Documentation the user points to, like a service description or existing letters.

If there isn't one, help the user create one. Follow "When there isn't one yet" in `references/service-context.md`. Only ask for the facts this request needs. Don't make the user fill in a whole context before they get a draft.

If the user doesn't want to give any context, carry on. Use placeholders for every service fact.

Only use facts marked "confirmed". Anything else becomes a placeholder and goes on the list for the service.

### 2. Understand the request

Work out:

- **the task:** draft a new message, adapt a pattern, review an existing message, or plan the messages for a case journey
- **the channels:** email, text message, letter or status page. If the user doesn't say, use the channels the service context lists as in use. Don't draft for planned channels unless asked. If the context doesn't say either, draft an email and a text message and say why. Follow "How to use the baseline copy" in `case-communication-patterns` for choosing between channels
- **the customer's situation:** what has just happened in their case, from their point of view
- **how many situations:** if the request covers several, handle each one separately, then give one combined list of what needs a decision

### 3. Identify the pattern

Use `case-communication-patterns` to find the moment, its variant and any modifier, like reminder or delay.

If 2 moments could fit, say which you chose and why. If none fits, say so. Don't force it, and don't invent a new moment.

### 4. Adapt the pattern with service facts

Start from the pattern's baseline copy for each channel. Fill the placeholders from confirmed facts in the service context. Use the service's terminology, and keep internal terms out.

Keep the pattern's core information and order. If the service context records a justified departure from the pattern, apply it and say so.

### 5. Run privacy and policy checks

Use `privacy-aware-communications` on what each version reveals, in each channel. Work through the pattern's "Privacy and policy checkpoints".

For each checkpoint:

- if a confirmed decision in the service context covers it, apply it and cite its owner and date
- if not, use the default position marked "needs confirmation", or flag the exact question and who could answer it

Only a confirmed policy decision settles a privacy, legal or policy checkpoint. A communication judgement or precedent can shape wording, but if one is the only thing covering a checkpoint, apply it and flag that it needs confirming as a decision.

Never infer a policy position, a consequence, a timescale or legal effect. Never treat the service's published content alone as its policy, because it can be out of date.

### 6. Apply GOV.UK content guidance

Use `govuk-content` on each draft, as a drafting check. Fix the wording without changing the meaning or adding facts.

If the service context records a language duty, like Welsh, flag that each message needs a version in that language. Don't translate unless the user asks.

### 7. Return the result

Use the output format below.

## Output

For a draft:

```
Pattern: [moment], variant [variant], [modifier, if any]

[Channel]
[The draft, formatted for the channel]

[Repeat for each channel]

Needs a service decision
- [each placeholder still unfilled, and each privacy, policy or legal question, with who could answer it]

Used from the service context
- [each confirmed fact or decision used, with its owner and date]

Notes
- [any judgement you made, like choosing between 2 moments, and any departure from the pattern]
```

For several situations, repeat the pattern line and the drafts for each, then give the 3 lists once, covering all of them.

Lead with the drafts. Keep "Needs a service decision" specific: say what's needed, not that "more information is needed".

"Needs a service decision" is the one list for everything still open. Put the other skills' lists in it, like `govuk-content`'s "Check before publishing". Don't list ((double bracket)) placeholders. They're filled for each message, not decisions.

If a message reveals personal or sensitive information, add a short "What each version reveals" table from `privacy-aware-communications` before "Needs a service decision".

For a review, give the `govuk-content` review table, then:

- **pattern gaps:** core information from the matching pattern that the message is missing
- **privacy:** what the message reveals that needs a decision
- **needs a service decision:** as above

For a case journey, give the plan from `case-communication-patterns`, then list the facts the service context would need to draft each message.

### Offer to update the service context

If the user confirmed new facts during the conversation, offer the updated service context back to them, so they can save it in their own project. Never save it into this plugin.

## Boundaries

- don't decide legal effect, lawful basis, disclosure or policy. Flag them
- don't fill a placeholder with a plausible guess
- don't move a service's facts into the generic patterns or skills
- don't present the draft as approved. It's a first draft for the service to check
