import React, { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question }),
      });

      if (!response.ok) {
        throw new Error("Sunucudan geçerli bir yanıt alınamadı");
      }

      const data = await response.json();
      console.log("✅ Model Cevabı:", data);
      setAnswer(data.answer);
    } catch (error) {
      console.error("🚨 Hata:", error);
      setAnswer("Sunucudan cevap alınamadı.");
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif", maxWidth: "600px", margin: "0 auto" }}>
      <h2>T5 Modeliyle Soru-Cevap</h2>
      <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
        <input
          type="text"
          placeholder="Bir soru yazın..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          style={{
            padding: "10px",
            width: "70%",
            fontSize: "16px",
            border: "1px solid #ccc",
            borderRadius: "4px",
            marginRight: "10px",
          }}
        />
        <button
          type="submit"
          style={{
            padding: "10px 20px",
            fontSize: "16px",
            backgroundColor: "#007bff",
            color: "#fff",
            border: "none",
            borderRadius: "4px",
            cursor: "pointer",
          }}
        >
          Gönder
        </button>
      </form>

      <div style={{ backgroundColor: "#f8f9fa", padding: "10px", borderRadius: "4px" }}>
        <h3>Cevap:</h3>
        <p style={{ fontWeight: "bold" }}>{answer}</p>
      </div>
    </div>
  );
}

export default App;
