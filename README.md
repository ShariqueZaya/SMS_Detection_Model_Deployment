SMS Spam Detection Model Deployment

Project Overview

This project is an SMS Spam Detection system that uses Machine Learning and Natural Language Processing (NLP) to classify SMS messages as either Spam or Not Spam (Ham).

The project includes a trained machine learning model, a Flask REST API for predictions, a simple web interface, and Docker containerization for deployment.

Users can enter an SMS message through the web interface and receive a prediction indicating whether the message is spam or legitimate.

Project Objectives

- Build a machine learning model to detect spam SMS messages.
- Apply NLP techniques to process and classify text messages.
- Develop a Flask API for model inference.
- Create a simple web interface for user interaction.
- Containerize the application using Docker.
- Provide a reproducible deployment process.

Dataset

The project uses the SMS Spam Collection dataset.

The dataset contains SMS messages labeled into two categories:

- Ham: Legitimate messages.
- Spam: Unwanted or promotional messages.

Technologies Used

Technology| Purpose
Python| Programming language
Pandas| Data manipulation
NumPy| Numerical operations
Scikit-learn| Machine learning and text processing
TF-IDF| Text feature extraction
Flask| REST API and web application
Flask-CORS| Cross-origin request support
Joblib| Loading trained models
HTML| Frontend structure
Docker| Application containerization
Jupyter Notebook| Model development and experimentation

Machine Learning Models

The following machine learning algorithms were trained and evaluated:

1. Multinomial Naive Bayes
2. Logistic Regression

Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

Results

Model| Accuracy
Multinomial Naive Bayes| 98.26%
Logistic Regression| 96.71%

Multinomial Naive Bayes achieved approximately 98.26% accuracy on the test dataset.

The trained model and TF-IDF vectorizer are saved using Joblib and used during prediction.

Project Structure

SMS_Spam_Detection_Model_Deployment/
│
├── dataset/
│
├── notebooks/
│   ├── sms_spam_classification.ipynb
│   ├── spam_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── report/
│
├── results/
│
├── src/
│   ├── api.py
│   └── app.py
│
├── templates/
│   └── index.html
│
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
└── test_api.py

Model Deployment

The trained machine learning model is deployed using Flask.

The Flask API loads the trained model and TF-IDF vectorizer to classify incoming SMS messages.

API Endpoints

Method| Endpoint| Description
GET| "/"| Check API status
POST| "/predict"| Predict whether an SMS is Spam or Not Spam

Example API Request

{
  "message": "Congratulations! You have won a free prize"
}

Example API Response

{
  "message": "Congratulations! You have won a free prize",
  "prediction": "Spam"
}

Running the Project Locally

1. Clone the Repository

git clone <your-github-repository-url>

Navigate to the project directory:

cd SMS_Spam_Detection_Model_Deployment

2. Create a Virtual Environment

python -m venv .venv

Activate the virtual environment.

Windows:

.venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Run the Flask API

python src/api.py

The API will run at:

http://127.0.0.1:5000

5. Run the Web Application

Open another terminal and run:

python src/app.py

Open the frontend in your browser:

http://127.0.0.1:5001

Enter an SMS message to check whether it is Spam or Not Spam.

Docker Deployment

The application is containerized using Docker.

Docker allows the application to run in an isolated environment with its required dependencies.

1. Build the Docker Image

From the project root directory, run:

docker build -t sms-spam-detector .

2. Run the Docker Container

docker run -p 5000:5000 sms-spam-detector

3. Access the API

Open the following address in your browser:

http://127.0.0.1:5000

The API should return a JSON response confirming that it is running.

4. Test the Prediction Endpoint

Use the following PowerShell command:

Invoke-RestMethod -Uri http://127.0.0.1:5000/predict -Method Post -ContentType "application/json" -Body '{"message":"Congratulations! You have won a free prize"}'

The API will return the prediction in JSON format.

Testing

The API was tested using sample SMS messages.

Testing included:

- Checking API status.
- Sending SMS messages to the "/predict" endpoint.
- Verifying prediction responses.
- Running the application inside a Docker container.
- Testing predictions through the web interface.

Key Features

- Machine learning-based SMS classification.
- TF-IDF text feature extraction.
- Flask REST API.
- Web interface for message prediction.
- Docker-based deployment.
- JSON request and response support.

Future Improvements

- Deploy the API to a cloud platform.
- Improve model performance using additional datasets.
- Add more machine learning algorithms.
- Implement API input validation and error handling.
- Add automated API testing.
- Improve the frontend user experience.

Author

Md Sharique Zaya

Artificial Intelligence Intern
InternSpark