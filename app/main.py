from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict_url, load_model

app = FastAPI()

# Load the trained model once at startup
model = load_model()

class URLRequest(BaseModel):
    url: str

@app.post("/predict")
def predict(request: URLRequest):
    # Pass the preloaded model for prediction
    label = predict_url(request.url, model=model)
    return {"predicted_type": label}

@app.get("/")
def root():
    return {"msg": "Malicious URL detection API - POST /predict with {'url': '...'}"}
