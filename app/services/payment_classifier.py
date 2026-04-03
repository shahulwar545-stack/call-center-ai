def classify_payment(text: str) -> str:
    text = text.lower()

    if "emi" in text:
        return "EMI"
    elif "full payment" in text:
        return "Full Payment"
    elif "partial" in text:
        return "Partial Payment"
    elif "down payment" in text:
        return "Down Payment"
    else:
        return "Unknown"