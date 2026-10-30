import re

PATTERNS = {
    "Phone Number": r"(?<!\d)(?:\+91[\s-]?)?[6-9]\d{9}(?!\d)",
    "Email": r"\b[\w.-]+@[\w.-]+\.\w{2,}\b",
    "Aadhaar-like Number": r"(?<!\d)\d{4}\s?\d{4}\s?\d{4}(?!\d)",
    "PAN-like Number": r"\b[A-Z]{5}\d{4}[A-Z]\b"
}

def detect_private_info(text):
    findings = []

    for label, pattern in PATTERNS.items():
        matches = re.finditer(pattern, text)

        for match in matches:
            findings.append({
                "type": label,
                "value": match.group(),
                "start": match.start(),
                "end": match.end()
            })

    return findings