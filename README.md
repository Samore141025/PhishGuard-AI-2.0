# PhishGuard Extension 🛡️

## Overview
This is an AI-powered phishing detection system that analyzes email content and produces a phishing risk score (0-100%), a verdict (Safe/Suspicious/Malicious), and clear human-readable explanations.

## How It Works
The system combines rule-based detectors (for urgency language, threats, suspicious URLs, and sender indicators) with a lightweight machine learning model (logistic regression) to assess email risk. Scores are aggregated, and verdicts are assigned based on thresholds.

## Features
- **AI-Powered**: Uses a logistic regression model for intelligent risk scoring.
- **Rule-Based**: Heuristic detectors for common phishing indicators.
- **Explainable**: Provides clear reasons why an email is flagged.
- **Simple API**: REST interface for easy integration.

## Installation
1. Install Python 3.8+
2. Install dependencies: `pip install -r requirements.txt`

## Usage
1. **Run the API server**:
   ```bash
   uvicorn api.main:app --reload --port 8000
   ```
2. **Access the Frontend**:
   Navigate to `http://localhost:8000` in your web browser.

3. **API Endpoint**:
   Send a POST request to `http://localhost:8000/analyze-email` with JSON:
   ```json
   {
     "subject": "Urgent Check",
     "body": "Your account is at risk. Click here: http://malicious-site.com",
     "sender": "no-reply@unknown.com",
     "urls": ["http://malicious-site.com"]
   }
   ```

## Cloudflare Tunnel
To expose your local environment for testing or remote access:
```bash
cloudflared tunnel --url http://localhost:8000
```
Note: Ensure your uvicorn server is running on the same port (default 8000).

## Testing
Run unit tests: `python -m unittest tests/test_analyzer.py`

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Limitations
- ML model trained on sample data; performance depends on data quality.
- Heuristic-based detections may have false positives.
- Does not analyze attachments or images.
