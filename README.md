# gov-communication-skills

Agent skills and supporting knowledge for designing and reviewing UK government customer communications.

The first use case is DVLA Drivers Medical. The skills and generic knowledge are written so that any government service can use them. Nothing in them should depend on Drivers Medical.

Nothing here is legal advice, and nothing here is an official GOV.UK or DVLA publication.

## How the repository is organised

There are 3 kinds of knowledge, 1 layer of skills that apply them, and 1 layer of tests.

- `knowledge/content-design/`: GOV.UK content design and writing guidance, true for any service
- `knowledge/privacy/`: privacy-aware communication principles under UK GDPR, true for any service
- `services/<service>/`: what is true for one service only, including its policy decisions
- `skills/`: skills that draft or review a communication by applying the knowledge above
- `evals/`: worked examples that test whether the skills behave correctly

Each directory has a README that sets out what belongs there and what does not.

## How the layers depend on each other

Knowledge flows one way: generic knowledge, then service knowledge, then skills.

- generic knowledge never refers to a service
- service knowledge can refer to generic knowledge, and can narrow it, but must say so when it does
- skills load generic knowledge always, and service knowledge only when told which service they are working on
- evals can use any layer

If a skill only works for one service, it is not generic. It belongs with that service, or the service-specific part belongs in `services/`.

## Working here

Read `CLAUDE.md` before adding or changing anything. It covers how knowledge is added, where it goes, and what to do when a position is not known.

No build step, no package manager, no framework. Everything is Markdown.
