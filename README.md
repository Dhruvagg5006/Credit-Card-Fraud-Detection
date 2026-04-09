# Credit-Card-Fraud-Detection-

📌 Project Overview
This project implements a machine learning-based fraud detection system for credit card transactions. Using the publicly available Kaggle Credit Card Fraud Detection dataset, the system identifies potentially fraudulent transactions with high accuracy. The project includes data preprocessing, exploratory data analysis, model training (Logistic Regression, Random Forest, Decision Tree, and XGBoost), and a complete web application for real-time fraud prediction.

📊 Dataset
Source: Kaggle Credit Card Fraud Detection Dataset

Dataset Statistics:

Total Transactions: 284,807

Fraudulent Transactions: 492 (0.17%)

Legitimate Transactions: 284,315 (99.83%)

Features: 31 columns (Time, V1-V28, Amount, Class)

Features Description:
Feature	Description
Time	Seconds elapsed between this transaction and the first transaction
V1 - V28	Principal components obtained with PCA (anonymized for privacy)
Amount	Transaction amount
Class	Target variable (1 = Fraud, 0 = Legitimate)
🏗️ System Architecture
text
<img width="354" height="407" alt="image" src="https://github.com/user-attachments/assets/7ca16d0a-e998-4691-acdc-87daff15abd3" />

┌─────────────────────────────────────────────────────────────────────────────┐
│                           CREDIT CARD FRAUD DETECTION SYSTEM                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                 │
│  │   Data Load  │───▶│   EDA &      │───▶│  Data Split  │                 │
│  │   (CSV)      │    │   Cleaning   │    │  (Train/Test)│                 │
│  └──────────────┘    └──────────────┘    └──────────────┘                 │
│         │                   │                   │                         │
│         ▼                   ▼                   ▼                         │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                 │
│  │ Feature      │    │ Correlation  │    │  Standard    │                 │
│  │ Analysis     │    │  Heatmap     │    │  Scaling     │                 │
│  └──────────────┘    └──────────────┘    └──────────────┘                 │
│                                                   │                         │
│                                                   ▼                         │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │                        MODEL TRAINING                              │    │
│  ├────────────┬────────────┬────────────┬────────────────────────────┤    │
│  │ Logistic   │  Random    │  Decision  │         XGBoost            │    │
│  │ Regression │  Forest    │    Tree    │     (Selected Best)        │    │
│  └────────────┴────────────┴────────────┴────────────────────────────┘    │
│                                                   │                         │
│                                                   ▼                         │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                 │
│  │  Model       │    │  FastAPI     │    │  Frontend    │                 │
│  │  Export      │───▶│  Backend     │───▶│  (HTML/CSS/  │                 │
│  │  (.pkl)      │    │  Service     │    │   JS)        │                 │
│  └──────────────┘    └──────────────┘    └──────────────┘                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘


🔄 Data Flow Diagram
text
┌──────────────────────────────────────────────────────────────────────────────┐
│                           DATA FLOW DIAGRAM                                  │
└──────────────────────────────────────────────────────────────────────────────┘

   INPUT                         PROCESSING                        OUTPUT
═══════════════════════════════════════════════════════════════════════════════

┌─────────────┐         ┌─────────────────┐
│  Raw CSV    │────────▶│  Data Loading   │
│  (284,807   │         │  (pandas)       │
│  records)   │         └────────┬────────┘
└─────────────┘                  │
                                 ▼
                        ┌─────────────────┐
                        │  Exploratory    │
                        │  Data Analysis  │
                        │  - Missing vals │
                        │  - Class dist   │
                        │  - Correlation  │
                        └────────┬────────┘
                                 │
                                 ▼
                        ┌─────────────────┐
                        │  Feature Scaling│
                        │  (StandardScaler│
                        └────────┬────────┘
                                 │
                    ┌────────────┼────────────┐
                    ▼            ▼            ▼
            ┌───────────┐  ┌───────────┐  ┌───────────┐
            │  Training │  │  Testing  │  │  API      │
            │  Set (80%)│  │  Set (20%)│  │  Request  │
            └─────┬─────┘  └─────┬─────┘  └─────┬─────┘
                  │              │              │
                  ▼              ▼              ▼
            ┌─────────────────────────────────────────┐
            │           Model Training                │
            │  ┌─────────────────────────────────┐    │
            │  │  XGBoost (Best Performance)     │    │
            │  │  - n_estimators: 200            │    │
            │  │  - max_depth: 6                 │    │
            │  │  - learning_rate: 0.1           │    │
            │  │  - scale_pos_weight: 577.29     │    │
            │  └─────────────────────────────────┘    │
            └─────────────────┬───────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  Model Export   │
                    │  (joblib .pkl)  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  FastAPI Load   │
                    │  Model & Serve  │
                    └────────┬────────┘
                             │
                             ▼
┌─────────────┐      ┌─────────────────┐       ┌─────────────┐
│  User Input │─────▶│  POST /predict  │─────▶│  JSON      |
│  (Features) │      │  Endpoint       │       │  Response  |
└─────────────┘      └─────────────────┘       │  - fraud   |
                                               │  - prob    │
                                               └────────────┘
🧠 Model Performance Comparison
Model	Accuracy	Precision	Recall	F1-Score	MCC
Logistic Regression	0.9991	0.8462	0.5612	0.6748	0.6887
Random Forest	0.9995	0.9737	0.7551	0.8506	0.8573
Decision Tree	0.9995	0.9737	0.7551	0.8506	0.8573
XGBoost	0.9994	0.8495	0.8061	0.8272	0.8272
Why XGBoost was chosen as the final model:
Highest Recall (80.61%) - Better at catching actual fraud cases

Handles Imbalanced Data - Built-in scale_pos_weight parameter

Regularization - Prevents overfitting on minority class

Feature Importance - Provides interpretability

Speed - Efficient training and inference

📈 Evaluation Metrics Explained
Metric	Description	Formula
Accuracy	Overall correctness	(TP + TN) / (TP + TN + FP + FN)
Precision	Accuracy of positive predictions	TP / (TP + FP)
Recall	Ability to find all positives	TP / (TP + FN)
F1-Score	Harmonic mean of precision & recall	2 * (Precision * Recall) / (Precision + Recall)
MCC	Balanced measure for imbalanced data	(TP×TN - FP×FN) / √((TP+FP)(TP+FN)(TN+FP)(TN+FN))
Where: TP = True Positive, TN = True Negative, FP = False Positive, FN = False Negative

💻 Technology Stack
Backend
FastAPI - High-performance web framework

Python 3.9+ - Core programming language

XGBoost - Gradient boosting framework

scikit-learn - ML utilities and preprocessing

pandas/numpy - Data manipulation

joblib - Model serialization

Frontend
HTML5/CSS3 - Structure and styling

JavaScript - Client-side interactivity

Lucide Icons - Icon library

Development Tools
Jupyter Notebook - Exploratory analysis

Uvicorn - ASGI server

Git/GitHub - Version control

🚀 Installation & Setup
Prerequisites
bash
Python 3.9 or higher
pip package manager
Step 1: Clone the Repository
bash
git clone https://github.com/yourusername/credit-card-fraud-detection.git
cd credit-card-fraud-detection
Step 2: Install Dependencies
bash
pip install -r requirements.txt
Step 3: Download Dataset
Download the dataset from Kaggle and place creditcard.csv in the project root.

Step 4: Train the Model (Optional)
Run the Jupyter notebook Code.ipynb to train models and generate xgboost_fraud_model.pkl.

Step 5: Start the API Server
bash
uvicorn main:app --reload
Server runs at: http://127.0.0.1:8000

Step 6: Launch Frontend
Open frontend.html in a web browser or serve it using:

bash
python -m http.server 8080
📡 API Endpoints
POST /predict
Predicts whether a transaction is fraudulent.

Request Body:

json
{
    "features": [406.0, -2.3122, 1.9519, -1.6098, 3.9979, ...]
}
Response:

json
{
    "fraud": 1,
    "probability": "0.87"
}



📁 Project Structure
text
credit-card-fraud-detection/
│
├── Code.ipynb                 # Jupyter notebook with full analysis & training
├── main.py                    # FastAPI backend server
├── frontend.html              # Web interface
├── xgboost_fraud_model.pkl    # Trained XGBoost model
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
└── assets/                    # (Optional) Images for README
    ├── architecture.png
    └── confusion_matrix.png



    
🖥️ Usage
Via Web Interface
Open frontend.html in your browser

Enter transaction features (Time, Amount, V1-V28)

Click "RUN ANALYSIS"

View prediction result (Fraud Alert / Transaction Safe)

Via API (cURL)
bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [406.0, -2.3122, 1.9519, -1.6098, 3.9979, ...]}'
⚠️ Handling Class Imbalance
The dataset is highly imbalanced (0.17% fraud). The following techniques were applied:

scale_pos_weight parameter in XGBoost:

text
scale_pos_weight = len(y_train[y_train==0]) / len(y_train[y_train==1])
scale_pos_weight = 577.29
Precision-Recall focused metrics - F1-Score and MCC used instead of accuracy alone

Stratified train-test split - Maintains class distribution

🔍 Confusion Matrix Results (XGBoost)
text
              Predicted
              Normal  Fraud
Actual Normal   56858      5
        Fraud      38    158
True Negatives: 56,858

False Positives: 5

False Negatives: 38

True Positives: 158

🚧 Future Improvements
Add real-time transaction streaming support

Implement additional models (Neural Networks, LightGBM)

Add user authentication and transaction history

Deploy to cloud (AWS/GCP/Azure)

Add SMS/Email alerts for fraud detection

Implement SHAP values for model interpretability

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit changes (git commit -m 'Add amazing feature')

Push to branch (git push origin feature/amazing-feature)

Open a Pull Request

📝 License
This project is open-source and available under the MIT License.

📧 Contact
For questions or suggestions, please open an issue on GitHub.

🙏 Acknowledgments
Kaggle for providing the dataset

ULB Machine Learning Group for data collection

XGBoost developers for the excellent library

FastAPI community for the great framework

⭐ Star this repository if you found it useful!

