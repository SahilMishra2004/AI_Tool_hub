from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import torch
import os

def detect_ai_text(text, model_path="AI_Detector"):
    if not os.path.isdir(model_path):
        return "Error: Model not found at path: " + model_path

    tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)
    model = DistilBertForSequenceClassification.from_pretrained(model_path)

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    outputs = model(**inputs)
    logits = outputs.logits
    predicted = torch.argmax(logits, dim=1).item()

    return "AI-generated" if predicted == 1 else "Human-written"
