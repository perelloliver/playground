import torch
import logging
from transformers import pipeline
from models import RequestInput, RequestOutput

class ClassificationClient:
    def __init__(self, model_name:str):
        self.pipeline = pipeline(model = model_name)

    def predict(self, text: RequestInput) -> RequestOutput:
        logging.info(f"Input text: {text.input}")
        response = self.pipeline(text)

        return RequestOutput(
            label=response[0]['label'],
            score=response[0]['score'],
            input=text.input
        )