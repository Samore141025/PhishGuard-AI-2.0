import re
from utils.email_schema import EmailInput

def detect_urgency(email: EmailInput) -> dict:
    urgency_keywords = ["urgent", "immediately", "today", "asap", "deadline", "now", "expiring", "action required", "within 24 hours"]
    text = email.subject + " " + email.body
    if any(re.search(r'\b' + re.escape(keyword) + r'\b', text, re.IGNORECASE) for keyword in urgency_keywords):
        return {"score": 25, "reason": "Urgent language detected"}
    return {"score": 0, "reason": "No urgency language found"}
