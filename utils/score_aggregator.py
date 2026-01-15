from detectors.urgency_detector import detect_urgency
from detectors.threat_detector import detect_threat
from detectors.url_detector import detect_suspicious_urls
from detectors.sender_detector import detect_generic_sender
from models.ml_scorer import get_ml_score
from utils.email_schema import EmailInput

def aggregate_score(email: EmailInput) -> float:
    urgency = detect_urgency(email)
    threat = detect_threat(email)
    urls = detect_suspicious_urls(email)
    sender = detect_generic_sender(email)
    ml_score = get_ml_score(email)
    
    rule_scores = [urgency['score'], threat['score'], urls['score'], sender['score']]
    total_rule_score = sum(rule_scores)
    
    # Simple average of rule scores and ML score
    final_score = (total_rule_score + ml_score) / 2
    return min(final_score, 100.0)  # cap at 100
