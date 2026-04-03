def check_sop(text: str) -> dict:
    text = text.lower()

    return {
        "greeting": any(x in text for x in ["hello", "hi", "vanakkam"]),
        "introduction": any(x in text for x in ["my name is", "i am calling from"]),
        "payment_discussion": any(x in text for x in ["payment", "emi", "amount"])
    }