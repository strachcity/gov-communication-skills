"""Check every text message baseline fits in one text, with long but realistic values.

Why this exists: hand-counted text messages kept going over 160 characters
once real values were filled in. This fills each baseline with stress values
and counts it the way GOV.UK Notify's text message pricing page describes.

Run from the repository root:

    python3 evals/text-message-lengths.py

It reads every ```sms block in the pattern files. It uses only the Python
standard library.
"""

import pathlib
import re
import sys

PATTERNS = pathlib.Path("skills/case-communication-patterns/references/patterns")

# Long but realistic values. Unknown placeholders get DEFAULT, and are listed.
STRESS = {
    "service name": "Apply for a temporary street trading licence",
    "case": "licence application",
    "what we received": "licence application",
    "what's due": "street trading licence",
    "what we've issued": "street trading licence",
    "due wording": "expires on",
    "action": "renew your licence",
    "action short": "Renew it",
    "next step": "make a decision",
    "timescale": "30 September 2026",
    "what we sent": "a letter",
    "short description": "proof of your current address",
    "outcome sentence": "Your licence application has not been approved",
    "next step, in a few words": "We'll post your licence",
    "if it does not arrive, in a few words": "call 0300 123 4567",
    "how to change it": "call 0300 123 4567",
    "how to recognise it": "a council photo ID card",
    "how long": "3 minutes",
    "number": "0300 123 4567",
    "opening times": "Monday to Friday, 9am to 5pm",
    "tracking url": "https://www.gov.uk/check-temporary-street-trading-licence",
    "upload url": "https://www.gov.uk/send-temporary-street-trading-evidence",
    "survey url": "https://www.gov.uk/done/temporary-street-trading-licence",
    "how to do it": "https://www.gov.uk/renew-temporary-street-trading-licence",
    "reference": "STL-2026-0012345",
    "date and time": "Wednesday 30 September 2026 between 10am and 12pm",
    "place": "Riverside House, 12 Station Road, Newtown NT1 1AA",
    "time of next attempt": "3:30pm",
}
DATE = "30 September 2026"
DEFAULT = "x" * 25

# From Notify's text message pricing page. Interpretation: the basic set below
# follows the GSM 03.38 alphabet, which the page's examples match.
BASIC = set(
    "@£$¥èéùìòÇ\nØøÅåΔ_ΦΓΛΩΠΨΣΘΞÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>?"
    "¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà"
)
DOUBLE = set("[]{}^\\|~€")  # standard, but count as 2 characters each
UNCERTAIN = set("‘’“”–—")  # Notify lists quotation marks and dashes as standard, but not which ones

STANDARD_LIMITS = [160, 306, 459, 612]
NON_STANDARD_LIMITS = [70, 134, 201, 268]


def fill(text, unknown):
    def square(m):
        key = m.group(1).lower()
        if key in STRESS:
            return STRESS[key]
        unknown.add(m.group(0))
        return DEFAULT

    def double(m):
        key = m.group(1).lower()
        if key in STRESS:
            return STRESS[key]
        if "date" in key or "deadline" in key or "arrive by" in key:
            return DATE
        unknown.add(m.group(0))
        return DEFAULT

    text = re.sub(r"\(\(([^)]+)\)\)", double, text)
    text = re.sub(r"\[([^\]]+)\]", square, text)
    return text


def count(text):
    non_standard = any(c not in BASIC and c not in DOUBLE and c not in UNCERTAIN for c in text)
    length = sum(2 if c in DOUBLE else 1 for c in text)
    limits = NON_STANDARD_LIMITS if non_standard else STANDARD_LIMITS
    texts = next((i + 1 for i, limit in enumerate(limits) if length <= limit), len(limits) + 1)
    uncertain = any(c in UNCERTAIN for c in text)
    return length, texts, non_standard, uncertain


def main():
    rows, unknown, failures = [], set(), 0
    for path in sorted(PATTERNS.glob("*.md")):
        source = path.read_text()
        for n, block in enumerate(re.findall(r"```sms\n(.*?)```", source, re.S), 1):
            template = block.strip()
            for prefixed in (True, False):
                if not prefixed and not template.startswith("[Service name]: "):
                    continue
                body = template if prefixed else template[len("[Service name]: "):]
                length, texts, non_standard, uncertain = count(fill(body, unknown))
                notes = []
                if non_standard:
                    notes.append("non-standard character, limit 70")
                if uncertain:
                    notes.append("curly quote or long dash")
                label = "with service name" if prefixed and template.startswith("[Service name]") else (
                    "without service name" if not prefixed else "")
                if texts > 1 and not (prefixed and template.startswith("[Service name]")):
                    failures += 1
                    notes.append("OVER")
                elif texts > 1:
                    notes.append("over with the prefix: leave it out if the sender ID names the service")
                rows.append((path.stem, n, label, length, texts, "; ".join(notes)))

    print("| Pattern | Text | Version | Characters | Texts | Notes |")
    print("|---|---|---|---|---|---|")
    for row in rows:
        print("| %s | %d | %s | %d | %d | %s |" % row)
    if unknown:
        print("\nPlaceholders with no stress value, counted as %d characters: %s" % (len(DEFAULT), ", ".join(sorted(unknown))))
    print("\n%d text versions checked. %d over 1 text without the service name prefix." % (len(rows), failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
