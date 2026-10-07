# Testing the Copilot port

Results go in `evals/results.md`, in their own table for Copilot.

## Why the Claude results don't transfer

A port changes 3 things at once: the model, the core rules (compressed into `core.md`), and how skill text arrives (Copilot skills or knowledge files). A failure on Copilot can come from any of the 3.

## Order

Run these in order. Each stage is cheap and stops a wasted run at the next.

1. Install check. Follow "Use it in Microsoft 365 Copilot" in the README exactly, from the download onwards. Record anything confusing, whether the instructions saved whole, and whether skills, knowledge upload, both or neither were available.
2. Smoke test. In a fresh chat, ask for a message with no service context. Check that it drafts with placeholders, asks at most 1 question at a time, guesses no timescale or policy, and uses British English with no em dashes.
3. Skill reach. The core rules are in the instructions, so the smoke test can't show whether the skills are read. Run cases whose pass depends on a reference file:
   - `evals/case-communication-patterns/03-adapt-waiting-pattern.md`, which needs a pattern file
   - `evals/privacy-aware-communications/02-third-party-medical-no-decision.md`, which needs `references/disclosure.md`
   - `evals/govuk-content/01-web-page-style-errors.md`, which needs `references/style-a-to-z.md`

   Run each on an agent with the skills or knowledge files, and on one built from the instructions alone. If the runs don't differ, the skills aren't being reached.
4. Front door. Run `evals/government-communication/01-no-service-context.md` and `02-context-from-documentation.md` as written, changing only the surface.

## Recording

For each run, record the surface, the version and build date from `0 Read me first.txt`, and whether skills or knowledge files were present.

A failure that also happens on Claude belongs to the skills. A failure that happens only on Copilot belongs to `core.md` or `build.py`, and is fixed there, never by editing `skills/` to suit a port.
