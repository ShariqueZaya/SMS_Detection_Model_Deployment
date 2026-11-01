# Import required libraries
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

# Create Flask application
app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return jsonify({
        "message": "SMS Spam Detector API is running",
        "status": "success"
    })

# Load the trained model and TF-IDF vectorizer
model = joblib.load("notebooks/spam_model.pkl")
tfidf = joblib.load("notebooks/tfidf_vectorizer.pkl")


# Create API endpoint
@app.route("/predict", methods=["POST"])
def predict():

    # Get message from the request
    data = request.get_json()

    # Check if message is provided
    if not data or "message" not in data:
        return jsonify({"error": "Please provide an SMS message"}), 400

    message = data["message"]

    # Convert message into numerical features
    message_tfidf = tfidf.transform([message])

    # Predict the message
    prediction = model.predict(message_tfidf)[0]

    # Convert prediction into readable output
    if prediction == 1:
        result = "Spam"
    else:
        result = "Not Spam"

    # Return prediction as JSON
    return jsonify({
        "message": message,
        "prediction": result
    })


# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)