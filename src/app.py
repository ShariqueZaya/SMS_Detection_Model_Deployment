from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, template_folder="../templates")

API_URL = "http://127.0.0.1:5000/predict"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(silent=True, force=False)

    if not message or "message" not in message:
        return jsonify({"error": "Please provide an SMS message."}), 400

    message = message["message"]

    try:
        response = requests.post(
            API_URL,
            json={"message": message},
            timeout=10
        )

        response.raise_for_status()

        result = response.json()
        return jsonify({"prediction": result["prediction"]})

    except requests.exceptions.RequestException as e:
        print("API Error:", e)
        return jsonify({"error": "Unable to connect to the API."}), 502


if __name__ == "__main__":
    app.run(port=5001, debug=True)