def get_verdict(score: float) -> str:
    if score <= 30:
        return "Safe"
    elif score <= 70:
        return "Suspicious"
    else:
        return "Malicious"
