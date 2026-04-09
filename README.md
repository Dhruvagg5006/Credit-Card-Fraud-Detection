A complete end-to-end machine learning pipeline designed to detect fraudulent credit card transactions in real-time. This project features a robust XGBoost model to handle extreme data imbalance and a FastAPI backend for seamless deployment.

📋 Table of Contents
Project Overview

Dataset Information

System Architecture

Model Performance

Installation & Setup

Project Structure

🎯 Project Overview
Financial fraud costs billions annually. This system leverages advanced analytics to identify suspicious patterns. By utilizing an XGBoost classifier, the model focuses on Recall to ensure as many fraud cases as possible are captured without overwhelming the system with false positives.

Key Features:

Real-time API: POST endpoints for instant transaction scoring.

Modern UI: An interactive HTML frontend to test transactions manually.

Imbalance Handling: Optimized using scale_pos_weight and stratified sampling.

📊 Dataset Information
The dataset is sourced from Kaggle.

Anonymized Features: Features V1-V28 are PCA-transformed components for privacy.

Class Imbalance: Only 0.17% of transactions are fraudulent (492 out of 284,807).

Preprocessing: Applied standard scaling to the Time and Amount features.

🏗️ System Architecture
Code snippet
graph TD
    A[User Input / frontend.html] -->|JSON POST| B[FastAPI Backend / main.py]
    B -->|Preprocess Data| C[XGBoost Model / .pkl]
    C -->|Prediction| B
    B -->|JSON Response| A
🔄 Data Flow
Raw Input: Transaction data is fed through the frontend or API.

Standardization: Features are normalized to match the training distribution.

Inference: The pre-trained XGBoost model calculates the fraud probability.

Output: The system returns a binary classification (Fraud/Safe) and a confidence score.

🧠 Model Performance
Given the high imbalance, accuracy is not our primary metric. We focus on the Confusion Matrix and F1-Score.

Metric	Score
Accuracy	99.94%
Recall (Fraud)	81.0%
Precision (Fraud)	85.0%
F1-Score	0.83
📁 Project Structure
File	Description
Code.ipynb	Comprehensive Notebook for EDA and Model Training.
main.py	FastAPI application serving the inference logic.
frontend.html	Client-side interface for user interaction.
xgboost_fraud_model.pkl	Serialized XGBoost model for production use.
requirements.txt	List of dependencies (XGBoost, FastAPI, etc.).
🚀 Installation & Setup
Clone the repository:

Bash
git clone https://github.com/your-username/credit-card-fraud.git
cd credit-card-fraud
Install requirements:

Bash
pip install -r requirements.txt
Launch the backend server:

Bash
uvicorn main:app --reload
Open the frontend:
Simply open frontend.html in your preferred web browser to begin testing.

🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License
Distributed under the MIT License. See LICENSE for more information.
