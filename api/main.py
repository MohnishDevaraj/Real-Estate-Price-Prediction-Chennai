import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# -------------------------------
# Load model and feature columns
# -------------------------------
with open("Models/gradient_boosting_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("Models/col_feature_columns.txt", "r") as f:
    feature_columns = [line.strip() for line in f.readlines()]

# ----------------------
# FastAPI app
# ----------------------

app = FastAPI(
    title="Chennai House Price Predictor",
    description="Predict house prices using Gradient Boosting model",
    version="1.0",
    # swagger_ui_parameters={"useLocalFiles": True}
)

# -----------------------
# Input Schema
# -----------------------
class HouseInput(BaseModel):
    data : dict

# -----------------------
# Health check
# -----------------------
@app.get("/")
def home():
    return {"status" : "API is running"}

# -----------------------
# Prediction endpoint
# -----------------------
@app.post("/predict")
def predict_price(input_data : HouseInput):
    # convert input to dataframe
    input_df = pd.DataFrame([input_data.data])

    # Ensure correct feature order
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    # Predict
    prediction = model.predict(input_df)[0]

    return {
        "predicted_price" : round(float(prediction), 2)
    }