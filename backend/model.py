from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class T5Predictor:
    def __init__(self, model_path = "model/model"):  # Burada local klasör "model"
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_path, local_files_only=True).to(self.device)

    def predict(self, question):
        inputs = self.tokenizer("Soruları cevapla: " + question, return_tensors="pt", truncation=True)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        outputs = self.model.generate(**inputs, max_new_tokens=64)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
