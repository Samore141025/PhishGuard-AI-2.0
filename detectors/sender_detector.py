import re
from utils.email_schema import EmailInput

def detect_generic_sender(email: EmailInput) -> dict:
    generic_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    generic_prefixes = ["support", "info", "admin", "noreply", "service"]
    sender = email.sender.lower()
    score = 0
    reasons = []
    domain = sender.split('@')[-1] if '@' in sender else ""
    if domain in generic_domains:
        score += 15
        reasons.append("Sender from generic email domain")
    prefix = sender.split('@')[0] if '@' in sender else sender
    if any(prefix.startswith(gen) for gen in generic_prefixes):
        score += 10
        reasons.append("Generic sender prefix")
    if score > 0:
        return {"score": score, "reason": "; ".join(reasons)}
    return {"score": 0, "reason": "Sender appears legitimate"}
