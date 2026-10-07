#!/usr/bin/env python3
"""Build the downloads from skills/, .claude-plugin/ and ports/core.md.

    python3 ports/build.py             build into ports/dist/
    python3 ports/build.py --check     validate only, write nothing
    python3 ports/build.py --accept    record that core.md matches the current skills

Downloads:

    gov-communication-skills-plugin.zip    the whole plugin, for Customize > Plugins > Upload
    gov-communication-skills-<skill>.zip   one per skill, for Customize > Skills
    gov-communication-skills-copilot.zip   the Microsoft 365 Copilot port

Nothing here edits skills/. ports/dist/ is ignored by git. A GitHub Action
runs this on every push to main and publishes the zips to the "downloads"
release.

core.md is a hand-written summary of the skills. The build stops with exit
code 2 if the front door, or any skill's description, has changed since
core.md was last reviewed. Read the change, update core.md to match, then
run with --accept.
"""
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
PORTS = ROOT / "ports"
SKILLS = ROOT / "skills"
PLUGIN = ROOT / ".claude-plugin" / "plugin.json"
CORE = PORTS / "core.md"
REVIEWED = PORTS / "core.reviewed"
OUT = PORTS / "dist"

NAME = "gov-communication-skills"
REPO = "https://github.com/strachcity/gov-communication-skills"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
CREDIT = (
    "\n---\n\nContains material from gov-communication-skills "
    f"({REPO}), licensed under the Open Government Licence v3.0.\n"
)

# Order matters: the front door first. The number prefixes the knowledge file.
SKILL_ORDER = [
    "government-communication",
    "case-communication-patterns",
    "privacy-aware-communications",
    "govuk-content",
]
FRONT_DOOR = "government-communication"

# Microsoft 365 Copilot Agent Builder. The 8,000-character instructions limit
# is published by Microsoft. The others follow the policymemo port, which was
# built against Agent Builder, and need confirming against Microsoft's guidance.
INSTRUCTIONS_CHARS = 8000
SKILL_LIMIT = 8
SKILL_CHARS = 20000
DESCRIPTION_CHARS = 1024
KNOWLEDGE_LIMIT = 20
HEADROOM = 0.95

INSTRUCTIONS_FILE = "1 Paste into Instructions.txt"
SKILLS_DIR = f"2 Upload these {len(SKILL_ORDER)} skills"
KNOWLEDGE_DIR = "3 No Skills option - upload these as knowledge instead"
README_FILE = "0 Read me first.txt"

KNOWLEDGE_HOW = (
    "Each skill below is uploaded as a skill with the same name. Without skills, "
    f'your knowledge holds 4 files, "{NAME} 1 government-communication" to "{NAME} 4 '
    'govuk-content". Each file starts with the skill\'s main text, then its reference '
    'files, each headed "File: references/...". When a skill says to read a reference '
    "file, find that heading in the same knowledge file. If a file is unavailable, do "
    "the job described below and say nothing to the user about files."
)

README = """gov-communication-skills for Microsoft 365 Copilot, version {version}

Full steps, with help if something goes wrong:
{repo}#microsoft-365-copilot

In short:
1. In Copilot Chat, select Create agent. If it asks you to describe your
   agent, select Skip, or choose Configure instead of Describe.
2. In Name, enter: GOV.UK communications
3. Open "{instructions}", select everything, copy it, and paste it into the
   Instructions box. Check the last words are "Open Government Licence v3.0."
4. Under Skills, upload each of the {count} zip files in "{skills}", one at a
   time. Do not unzip them and do not rename them.
   No Skills option? Under Knowledge, upload the {count} files in
   "{knowledge}" instead. No upload option at all? Skip this step.
5. Switch off web search, Create images and Discourage model knowledge.
6. Select Create.

Cannot upload the files? You may be looking inside the zip without having
extracted it. On Windows, right-click the zip and choose Extract All. On a
Mac, double-click the zip. Then use the folder that appears.

Then tell the agent about your service, or attach your service context.

Built {date} from source {sha}.
"""


def run_git(*args: str) -> str:
    try:
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True,
                              text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def frontmatter(text: str) -> tuple[dict, str]:
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}, text
    fields = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        value = value.strip()
        if len(value) > 1 and value[0] == value[-1] == '"':
            value = value[1:-1]
        fields[key.strip()] = value
    return fields, text[match.end():]


def skill_files(name: str) -> list[pathlib.Path]:
    folder = SKILLS / name
    files = sorted(f for f in folder.rglob("*") if f.is_file())
    # SKILL.md first, references next, sources.md last.
    return sorted(files, key=lambda f: (f.name != "SKILL.md", f.name == "sources.md", str(f)))


def source_hash() -> str:
    """Hash what core.md summarises: the front door, and every description."""
    h = hashlib.sha256()
    h.update((SKILLS / FRONT_DOOR / "SKILL.md").read_bytes())
    for name in SKILL_ORDER:
        fields, _ = frontmatter((SKILLS / name / "SKILL.md").read_text())
        h.update(fields.get("description", "").encode())
    return h.hexdigest()[:12]


def add(z: zipfile.ZipFile, arcname: str, data: bytes | str) -> None:
    info = zipfile.ZipInfo(arcname, date_time=FIXED_TIME)
    info.external_attr = 0o644 << 16
    info.compress_type = zipfile.ZIP_DEFLATED
    z.writestr(info, data.encode() if isinstance(data, str) else data)


def write_zip(path: pathlib.Path, entries: list[tuple[str, bytes | str]]) -> None:
    with zipfile.ZipFile(path, "w") as z:
        for arcname, data in entries:
            add(z, arcname, data)


def skill_entries(name: str, prefix: str, transform=None) -> list[tuple[str, bytes | str]]:
    entries = []
    for f in skill_files(name):
        rel = f.relative_to(SKILLS / name).as_posix()
        data = f.read_bytes()
        if transform and f.suffix == ".md":
            data = transform(rel, data.decode())
        entries.append((f"{prefix}{rel}", data))
    return entries


def with_credit(rel: str, text: str) -> str:
    return text.rstrip() + "\n" + CREDIT


def knowledge_file(number: int, name: str, date: str, sha: str) -> str:
    parts = []
    for f in skill_files(name):
        rel = f.relative_to(SKILLS / name).as_posix()
        text = f.read_text()
        if rel == "SKILL.md":
            fields, body = frontmatter(text)
            header = (
                f"{NAME} knowledge file {number}: {name}\n"
                f"Use when: {fields.get('description', '')}\n"
                f"Built {date} from skills/{name}/ ({sha}).\n\n"
            )
            parts.append(header + body.strip())
        else:
            parts.append(f"File: {rel}\n\n{text.strip()}")
    return "\n\n---\n\n".join(parts) + "\n" + CREDIT


def build(check: bool) -> int:
    problems, notes = [], []
    plugin = json.loads(PLUGIN.read_text())
    version = plugin.get("version", "0.0.0")
    licence = (ROOT / "LICENSE").read_text()
    sha = source_hash()
    date = run_git("log", "-1", "--format=%cs", "--", "skills", "ports", ".claude-plugin") or "unknown"
    commit = run_git("rev-parse", "--short=12", "HEAD") or "unknown"

    reviewed = REVIEWED.read_text().strip() if REVIEWED.exists() else ""
    if reviewed != sha:
        print(
            "The front door or a skill description has changed since ports/core.md was\n"
            "last reviewed. Read the change, update core.md to match, then run:\n\n"
            "    python3 ports/build.py --accept\n",
            file=sys.stderr,
        )
        return 2

    for name in SKILL_ORDER:
        if not (SKILLS / name / "SKILL.md").exists():
            problems.append(f"{name}: no SKILL.md")
    found = sorted(p.name for p in SKILLS.iterdir() if (p / "SKILL.md").exists())
    if found != sorted(SKILL_ORDER):
        problems.append(f"skills/ holds {found}, but SKILL_ORDER lists {SKILL_ORDER}")

    instructions = (CORE.read_text()
                    .replace("{{SURFACE}}", "Microsoft 365 Copilot")
                    .replace("{{VERSION}}", version)
                    .replace("{{BUILD_DATE}}", date)
                    .replace("{{SOURCE_SHA}}", commit)
                    .replace("{{KNOWLEDGE_HOW}}", KNOWLEDGE_HOW)).rstrip() + "\n" + CREDIT
    leftover = re.findall(r"\{\{\w+\}\}", instructions)
    if leftover:
        problems.append(f"core.md: unfilled placeholders {leftover}")
    if len(instructions) > INSTRUCTIONS_CHARS:
        problems.append(f"copilot instructions: {len(instructions)} characters; the limit is {INSTRUCTIONS_CHARS}")
    elif len(instructions) > INSTRUCTIONS_CHARS * HEADROOM:
        notes.append(f"copilot instructions: {len(instructions)} of {INSTRUCTIONS_CHARS} characters")

    if len(SKILL_ORDER) > SKILL_LIMIT:
        problems.append(f"copilot: {len(SKILL_ORDER)} skills; the limit is {SKILL_LIMIT}")
    if len(SKILL_ORDER) > KNOWLEDGE_LIMIT:
        problems.append(f"copilot: {len(SKILL_ORDER)} knowledge files; the limit is {KNOWLEDGE_LIMIT}")
    for name in SKILL_ORDER:
        path = SKILLS / name / "SKILL.md"
        if not path.exists():
            continue
        fields, _ = frontmatter(path.read_text())
        if fields.get("name") != name:
            problems.append(f"{name}: frontmatter name is {fields.get('name')!r}")
        if len(fields.get("description", "")) > DESCRIPTION_CHARS:
            problems.append(f"{name}: description over {DESCRIPTION_CHARS} characters")
        size = len(with_credit("SKILL.md", path.read_text()))
        if size > SKILL_CHARS:
            problems.append(f"{name}: SKILL.md is {size} characters; the Copilot limit is {SKILL_CHARS}")
        elif size > SKILL_CHARS * HEADROOM:
            notes.append(f"{name}: SKILL.md is {size} of {SKILL_CHARS} characters")

    for note in notes:
        print(f"note: {note}")
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        return 1
    if check:
        print("All checks passed. Nothing written.")
        return 0

    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.zip"):
        old.unlink()

    # The whole plugin, as Claude reads it from this repository.
    plugin_entries = [(f"{NAME}/.claude-plugin/plugin.json", PLUGIN.read_bytes()),
                      (f"{NAME}/LICENSE", licence)]
    for name in SKILL_ORDER:
        plugin_entries += skill_entries(name, f"{NAME}/skills/{name}/")
    write_zip(OUT / f"{NAME}-plugin.zip", plugin_entries)

    # One zip per skill, with the skill folder at the root.
    for name in SKILL_ORDER:
        write_zip(OUT / f"{NAME}-{name}.zip",
                  skill_entries(name, f"{name}/") + [(f"{name}/LICENSE", licence)])

    # Copilot. No folder at the root: Extract All makes one named after the zip.
    copilot = [
        (README_FILE, README.format(version=version, repo=REPO, instructions=INSTRUCTIONS_FILE,
                                    count=len(SKILL_ORDER), skills=SKILLS_DIR,
                                    knowledge=KNOWLEDGE_DIR, date=date, sha=commit)),
        (INSTRUCTIONS_FILE, instructions),
        ("Licence.txt", licence),
    ]
    for name in SKILL_ORDER:
        inner = OUT / f".{name}.zip"
        write_zip(inner, skill_entries(name, f"{name}/", with_credit))
        copilot.append((f"{SKILLS_DIR}/{name}.zip", inner.read_bytes()))
        inner.unlink()
    for number, name in enumerate(SKILL_ORDER, 1):
        copilot.append((f"{KNOWLEDGE_DIR}/{NAME} {number} {name}.txt",
                        knowledge_file(number, name, date, commit)))
    write_zip(OUT / f"{NAME}-copilot.zip", copilot)

    for z in sorted(OUT.glob("*.zip")):
        print(f"{z.relative_to(ROOT)}  {z.stat().st_size // 1024} KB")
    print(f"Copilot instructions: {len(instructions)} of {INSTRUCTIONS_CHARS} characters")
    return 0


def main() -> int:
    args = sys.argv[1:]
    if args == ["--accept"]:
        REVIEWED.write_text(source_hash() + "\n")
        print(f"Recorded {source_hash()} in {REVIEWED.relative_to(ROOT)}.")
        return 0
    if args not in ([], ["--check"]):
        print(__doc__, file=sys.stderr)
        return 1
    return build(check=args == ["--check"])


if __name__ == "__main__":
    sys.exit(main())
