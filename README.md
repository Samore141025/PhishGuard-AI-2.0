# PhishGuard Extension

## Overview
This is an AI-powered phishing detection system that analyzes email content and produces a phishing risk score (0-100%), a verdict (Safe/Suspicious/Malicious), and clear human-readable explanations.

## How It Works
The system combines rule-based detectors (for urgency language, threats, suspicious URLs, and sender indicators) with a lightweight machine learning model (logistic regression) to assess email risk. Scores are aggregated, and verdicts are assigned based on thresholds.

## Features
- Rule-based detection for urgency, threats, URLs, and sender indicators
- Lightweight ML model for scoring
- REST API for email analysis
- Explainable decisions

## Installation
1. Install Python 3.8+
2. Install dependencies: `pip install fastapi uvicorn pydantic scikit-learn joblib`

## Usage
1. Run the API: `uvicorn api.main:app --reload`
2. Send POST request to `http://localhost:8000/analyze-email` with JSON:
   ```json
   {
     "subject": "Urgent: Account Issue",
     "body": "Click here to verify",
     "sender": "support@bank.com",
     "urls": ["https://bank.com/verify"]
   }
   ```
   Response:
   ```json
   {
     "risk_score": 75,
     "verdict": "Malicious",
     "explanations": ["Urgent language detected", "Suspicious URL"]
   }
   ```

## Testing
Run tests: `python -m unittest tests/test_analyzer.py`

## Limitations
- ML model is trained on limited sample data; performance may improve with more data
- Rule-based detections are heuristic and may have false positives/negatives
- Does not analyze attachments or images
