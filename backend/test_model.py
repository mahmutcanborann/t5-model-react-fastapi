from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("model", local_files_only=True)
model = AutoModelForSeq2SeqLM.from_pretrained("model", local_files_only=True)

print("Model ve tokenizer başarıyla yüklendi.")
