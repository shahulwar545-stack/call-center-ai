def detect_rejection(text: str) -> str:
    text = text.lower()

    if "financial problem" in text or "no money" in text:
        return "Financial issue"
    elif "not interested" in text:
        return "Not interested"
    elif "call later" in text or "busy now" in text:
        return "Call later"
    else:
        return "None"