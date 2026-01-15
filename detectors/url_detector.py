import re
from utils.email_schema import EmailInput

def detect_suspicious_urls(email: EmailInput) -> dict:
    suspicious_keywords = ["login", "verify", "secure", "account", "password", "bank", "update", "confirm", "signin", "auth"]
    score = 0
    reasons = []
    for url in email.urls:
        if len(url) > 80:  # Lowered from 100
            score += 15
            reasons.append("URL length too long")
        if any(keyword in url.lower() for keyword in suspicious_keywords):
            score += 15  # Increased from 10
            reasons.append("Suspicious keyword in URL")
        # Simple entropy check: count unique chars / len
        unique_chars = len(set(url))
        entropy = unique_chars / len(url) if len(url) > 0 else 0
        if entropy > 0.5:  # Lowered from 0.7
            score += 20
            reasons.append("High entropy URL")
    if score > 0:
        return {"score": min(score, 60), "reason": "; ".join(reasons)}
    return {"score": 0, "reason": "No suspicious URLs found"}
