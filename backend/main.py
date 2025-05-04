from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import T5Predictor
from download_model import download_model

download_model()

app = FastAPI()

# Frontend'den gelen istekleri kabul etmesi için CORS ayarı:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # sadece React URL'sini yazmak istersen: ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

predictor = T5Predictor("model/model")

class Soru(BaseModel):
    question: str

@app.post("/predict")
def cevapla(soru: Soru):
    print(f"Gelen soru: {soru.question}")
    cevap = predictor.predict(soru.question)
    print(f"Oluşturulan cevap: {cevap}")
    return {"answer": cevap}

