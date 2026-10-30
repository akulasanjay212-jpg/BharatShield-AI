from detector import detect_private_info

def redact_text(text):
    findings = detect_private_info(text)

    # Replace matches from right to left
    findings.sort(key=lambda item: item["start"], reverse=True)

    for item in findings:
        replacement = f"[REDACTED: {item['type']}]"

        text = (
            text[:item["start"]]
            + replacement
            + text[item["end"]:]
        )

    return text