# Skills

Skills that draft or review a government communication.

Each skill is self-contained, so it can be shared and installed on its own:

```
skill-name/
  SKILL.md        what the skill does, when to use it, and the core guidance
  references/     detailed guidance, read only when the task needs it
  sources.md      every source, what we took from it and when it was checked
```

## What a skill does

- says what task it carries out and what it outputs
- keeps the guidance it needs in its own `references/`, not copied into other skills
- takes the user's service context as an input when service facts are relevant
- flags unknown legal or policy positions for the user, instead of resolving them

## What a skill must not do

- contain rules, words or examples from a named service. There are no service-specific skills in this repository
- present a guess about legal or policy positions as fact
- use another skill's references directly. If 2 skills need the same guidance, ask before deciding where it lives
