try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    import joblib
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

import os
from utils.email_schema import EmailInput

MODEL_PATH = 'models/phishing_model.pkl'
VECTORIZER_PATH = 'models/vectorizer.pkl'

def extract_features(email: EmailInput):
    text = email.subject + " " + email.body
    url_features = len(email.urls)  # number of URLs as a simple feature
    return text, url_features

def load_model():
    if not SKLEARN_AVAILABLE:
        return None, None
    if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)
        return model, vectorizer
    else:
        # Dummy model if not trained
        return None, None

def get_ml_score(email: EmailInput) -> float:
    model, vectorizer = load_model()
    if model is None:
        return 0.0  # No model, return 0
    text, url_count = extract_features(email)
    text_vector = vectorizer.transform([text])
    # For simplicity, ignore url_count in prediction, or add it
    prob = model.predict_proba(text_vector)[0][1]  # probability of phishing
    return prob * 100  # score out of 100

# To train the model (call this separately)
def train_model():
    if not SKLEARN_AVAILABLE:
        print("Scikit-learn not available, cannot train model.")
        return
    # Sample data - in real scenario, load from data/
    texts = [
        "Urgent: Your account is suspended", 
        "Hello, how are you?", 
        "Verify your login now",
        "Weekly newsletter update",
        "Security Alert: Unauthorized login attempt",
        "Hi, let's catch up for coffee",
        "Action Required: Update your payment method",
        "Your package has been delivered",
        "Final Warning: Account closure in 24 hours",
        "Meeting invitation for tomorrow",
        "Payment Processed: Invoice #12345",
        "Click here to claim your prize",
        "Lunch menu for the cafeteria",
        "Password Reset Request",
        "New message from your bank"
    ]
    labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1]  # 1 for phishing, 0 for safe
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    model = LogisticRegression()
    model.fit(X, labels)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)
