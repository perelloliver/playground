from fastapi import FastAPI
import logging
from .clients import classification
from .models import RequestInput, RequestOutput

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.post("/predict")

async def predict(data: RequestInput) -> RequestOutput:
    response = classification.predict(data)
    logging.info(f"Prediction: {response.label} with score: {response.score} for input: {response.input}")
    return response

