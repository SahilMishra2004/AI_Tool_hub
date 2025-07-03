from transformers import T5Tokenizer, T5ForConditionalGeneration
import os

def humanize_text(text, model_path="Humanize"):
    if not os.path.isdir(model_path):
        return "Error: Humanize model not found at path: " + model_path

    tokenizer = T5Tokenizer.from_pretrained(model_path)
    model = T5ForConditionalGeneration.from_pretrained(model_path)

    input_ids = tokenizer.encode("humanize: " + text, return_tensors="pt", max_length=64, truncation=True)
    output_ids = model.generate(input_ids, max_length=64, num_beams=4, early_stopping=True)

    return tokenizer.decode(output_ids[0], skip_special_tokens=True)
