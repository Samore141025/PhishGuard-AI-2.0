import requests
import json

url = "http://127.0.0.1:8000/analyze-email"
payload = {
    "sender": "support@bank-verify.com",
    "subject": "Urgent: Your account is suspended",
    "body": "Your account has been suspended due to unauthorized access. Please verify your login now at http://bank-verify.com/login-secure-auth-update-confirm-signin-password-bank-update-confirm. Click here to claim your prize.",
    "urls": ["http://bank-verify.com/login-secure-auth-update-confirm-signin-password-bank-update-confirm"]
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    print("Success!")
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Failed with status code: {response.status_code}")
    print(response.text)
