# Ports and downloads

The downloadable zips, and the Microsoft 365 Copilot version of the plugin. All of them are built from `skills/`, which stays the only source. Nothing here edits it, and a port never forks it.

| File | What it is |
|---|---|
| `build.py` | builds every zip into `ports/dist/`, which git ignores |
| `core.md` | the only hand-written port text: the front door compressed to fit Copilot's 8,000-character Instructions box. Placeholders in double braces are filled at build time |
| `core.reviewed` | a hash of what `core.md` summarises, from when it was last checked |
| `testing.md` | how to test the Copilot port |

## Why there is a build script

Hand-made zips go stale and are easy to get wrong, like a skill missing its references or a folder nested twice. The script has no dependencies.

## Building

```
python3 ports/build.py            build into ports/dist/
python3 ports/build.py --check    validate only, write nothing
```

You don't need to run it to publish. The `Publish downloads` GitHub Action runs it on every push to `main` that changes a skill, and attaches the zips to the `downloads` release. The README and `docs/install.html` link there, and both hold the install steps. Change them together.

## What it builds

| Zip | For |
|---|---|
| `gov-communication-skills-plugin.zip` | Claude: Customize, then Plugins, then upload. The plugin folder, its manifest, every skill and the licence |
| `gov-communication-skills-<skill>.zip` | Claude: Customize, then Skills, then upload. One skill, with its folder at the root |
| `gov-communication-skills-copilot.zip` | Microsoft 365 Copilot |

The Copilot zip opens to files named for what to do with them:

```
0 Read me first.txt
1 Paste into Instructions.txt
2 Upload these 4 skills/                                  one zip per skill
3 No Skills option - upload these as knowledge instead/   one text file per skill
Licence.txt
```

The zip has no folder inside it. Windows Extract All and the Mac's Archive Utility each make one named after the zip, so an inner folder would nest a second copy.

Each Copilot skill is the skill folder unchanged, with the licence credit added to the end of each Markdown file. Each knowledge file is a skill's `SKILL.md`, then its reference files, each headed with its path, so "read `references/moments.md`" still makes sense. The instructions tell Copilot how to find them, so don't rename the files.

## Copilot limits

The build fails if any of these is broken:

- the instructions are over 8,000 characters
- there are more than 8 skills, or more than 20 knowledge files
- a `SKILL.md` is over 20,000 characters, or a description over 1,024

Microsoft publishes the 8,000-character instructions limit for Agent Builder. The others follow the policymemo port, which was built against Agent Builder. They need confirming against Microsoft's guidance.

## When the front door changes

`core.md` summarises `skills/government-communication/SKILL.md` and each skill's description. If either changes, the build stops with exit code 2, and so does the Action. Read the change, update `core.md` to match, then run:

```
python3 ports/build.py --accept
```

A change to any other part of a skill flows into the zips on the next build, with nothing to review.

## Adding another surface

Gemini and ChatGPT aren't built yet. A new surface needs its own section in `build.py` and its own test runs. It never needs a change to `skills/`.
