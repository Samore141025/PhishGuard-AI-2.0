from models.ml_scorer import train_model
import os

if __name__ == "__main__":
    print("Training model...")
    # Add more samples to models/ml_scorer.py if needed, or just run the existing one
    # I'll update ml_scorer.py first to have better training data.
    train_model()
    if os.path.exists('models/phishing_model.pkl'):
        print("Model trained and saved successfully.")
    else:
        print("Model training failed.")
