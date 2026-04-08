from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
app = FastAPI()

model = joblib.load("xgboost_fraud_model.pkl")

# ✅ Proper input schema
class InputData(BaseModel):
    features: list[float]   # IMPORTANT

@app.post("/predict")
def predict(data: InputData):
    arr = np.array(data.features).reshape(1, -1)
    prediction = model.predict(arr)[0]
    probability=model.predict_proba(arr)[0][1]
    print(model.predict_proba(arr))
    return {"fraud": int(prediction)
            ,"probability": f"{probability:.2f}"}