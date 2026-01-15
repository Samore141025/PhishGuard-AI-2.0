from detectors.urgency_detector import detect_urgency
from detectors.threat_detector import detect_threat
from detectors.url_detector import detect_suspicious_urls
from detectors.sender_detector import detect_generic_sender
from models.ml_scorer import get_ml_score
from utils.verdict_logic import get_verdict
from utils.email_schema import EmailInput
from typing import List

def analyze_email(email: EmailInput) -> dict:
    urgency = detect_urgency(email)
    threat = detect_threat(email)
    urls = detect_suspicious_urls(email)
    sender = detect_generic_sender(email)
    ml_score = get_ml_score(email)
    
    rule_scores = [urgency['score'], threat['score'], urls['score'], sender['score']]
    total_rule_score = sum(rule_scores)
    
    # Improved scoring logic: Don't let a missing/low ML model tank the score
    if ml_score > total_rule_score:
        # If ML is higher, it boosts the score
        final_score = (total_rule_score * 0.6) + (ml_score * 0.4)
    else:
        # If rules are stronger, trust them more, but let ML contribute if present
        if ml_score > 0:
            final_score = (total_rule_score * 0.8) + (ml_score * 0.2)
        else:
            final_score = total_rule_score
            
    final_score = min(final_score, 100.0)
    
    verdict = get_verdict(final_score)
    
    explanations = []
    if urgency['score'] > 0:
        explanations.append(urgency['reason'])
    if threat['score'] > 0:
        explanations.append(threat['reason'])
    if urls['score'] > 0:
        explanations.append(urls['reason'])
    if sender['score'] > 0:
        explanations.append(sender['reason'])
    if ml_score > 50:  # If ML thinks it's likely phishing
        explanations.append("ML model indicates high phishing probability")
    
    return {
        "risk_score": int(final_score),
        "verdict": verdict,
        "explanations": explanations
    }
