from fastapi import FastAPI
import logging
from .clients import classification
from .models import RequestInput, RequestOutput

app = FastAPI()


@app.post("/predict")

async def predict(text: str) -> RequestOutput:
    input = RequestInput(input=text)

    response = classification.predict(input)
    logging.info(f"Prediction: {response.label} with score: {response.score} for input: {response.input}")
    return response

