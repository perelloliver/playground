import torch
import logging
from transformers import pipeline
from app.models import RequestInput, RequestOutput

class ClassificationClient:
    def __init__(self, model_name:str):
        self.pipeline = pipeline(model = model_name)

    def predict(self, text: RequestInput) -> RequestOutput:
        logging.info(f"CLASSIFYING MESSAGE: {text.input}")
        response = self.pipeline(text.input)

        return RequestOutput(
            label=response[0]['label'],
            score=response[0]['score'],
            input=text.input
        )