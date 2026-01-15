import re
from utils.email_schema import EmailInput

def detect_threat(email: EmailInput) -> dict:
    threat_keywords = [
        "account suspended", "delivery failed", "payment issue", "security alert", 
        "unauthorized access", "verify your account", "compromised", "frozen", 
        "re-verify", "security breach", "locked out"
    ]
    text = email.subject + " " + email.body
    if any(re.search(r'\b' + re.escape(keyword) + r'\b', text, re.IGNORECASE) for keyword in threat_keywords):
        return {"score": 30, "reason": "Threat language detected"}
    return {"score": 0, "reason": "No threat language found"}
