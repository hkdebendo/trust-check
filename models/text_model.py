from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "GroNLP/hateBERT"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def detect_abusive(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    outputs = model(**inputs)
    logits = outputs.logits
    probs = torch.softmax(logits, dim=-1).squeeze().tolist()

    label_non_offensive = probs[0]
    label_offensive = probs[1]

    decision = "OFFENSIF" if label_offensive > label_non_offensive else "NORMAL"

    return {
        "Texte": text,
        "Score Non-Offensif": round(label_non_offensive, 4),
        "Score Offensif": round(label_offensive, 4),
        "Verdict": decision
    }
