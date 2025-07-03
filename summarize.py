from transformers import T5Tokenizer, T5ForConditionalGeneration
import os

def summarize_text(text, model_path="my_t5_summary_model"):
    if not os.path.isdir(model_path):
        return "Error: Model not found at path: " + model_path

    tokenizer = T5Tokenizer.from_pretrained(model_path)
    model = T5ForConditionalGeneration.from_pretrained(model_path)

    input_ids = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(input_ids, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)

    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return output
