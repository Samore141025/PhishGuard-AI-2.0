import unittest
from utils.email_schema import EmailInput
from utils.analyzer import analyze_email

class TestAnalyzer(unittest.TestCase):
    
    def test_legitimate_email(self):
        email = EmailInput(
            subject="Hello",
            body="How are you?",
            sender="friend@example.com",
            urls=[]
        )
        result = analyze_email(email)
        self.assertEqual(result["verdict"], "Safe")
        self.assertGreaterEqual(result["risk_score"], 0)
    
    def test_borderline_email(self):
        email = EmailInput(
            subject="Urgent: Check your account",
            body="Please verify",
            sender="support@bank.com",
            urls=["https://bank.com/verify"]
        )
        result = analyze_email(email)
        self.assertIn(result["verdict"], ["Safe", "Suspicious"])
    
    def test_clear_phishing_email(self):
        email = EmailInput(
            subject="Account Suspended Immediately",
            body="Click here to login",
            sender="noreply@random.com",
            urls=["https://suspicious-login-random-string.com"]
        )
        result = analyze_email(email)
        self.assertEqual(result["verdict"], "Malicious")
        self.assertGreater(result["risk_score"], 70)

if __name__ == '__main__':
    unittest.main()
