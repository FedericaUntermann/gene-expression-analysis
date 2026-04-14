from fastapi import FastAPI
import pickle
import json

app = FastAPI()

# Cargar modelo
with open("results/model.pkl", "rb") as f:
    model = pickle.load(f)

# Cargar features
with open("results/features.json", "r") as f:
    features = json.load(f)


@app.get("/")
def home():
    return {"message": "Gene Expression API is running"}


@app.post("/predict")
def predict(data: dict):
    input_data = [data.get(feature, 0) for feature in features]

    prediction = model.predict([input_data])[0]

    proba = model.predict_proba([input_data])[0]
    confidence = max(proba)

    label_map = {
        "HPNE": "normal",
        "PANC1": "tumor"
    }

    return {
        "prediction": label_map.get(prediction, prediction),
        "confidence": float(confidence)
    }
