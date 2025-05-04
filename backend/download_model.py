import gdown
import os
import zipfile

def download_model():
    if not os.path.exists("model"):
        print("📦 Model indiriliyor...")
        url = "https://drive.google.com/uc?id=19ScqfRWVmJ6nBxTBRalqMwiAOTWWNG30"
        output = "model.zip"
        gdown.download(url, output, quiet=False)

        print("📂 Zip açılıyor...")
        with zipfile.ZipFile(output, "r") as zip_ref:
            zip_ref.extractall("model")
        os.remove(output)
        print("✅ Model başarıyla indirildi ve açıldı!")
    else:
        print("🟢 Model zaten var, indirmeye gerek yok.")
