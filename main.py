from langchain_ollama import OllamaLLM
from pdf_reader import read_pdf, get_first_500_words  


pdf_text = read_pdf("fikralar-sayfalar.pdf")  
first_500_words = get_first_500_words(pdf_text)

# Ollama modelini başlat
model = OllamaLLM(model="llama3.1")

# print(pdf_text)

while True:
    question = input("Soru (Çıkmak için 'exit' yazın): ")

    if question.lower() == 'exit':
        print("Çıkılıyor...")
        break

    input_text = f"Context:Atılan pdf dosyasına uygun olarak soruya yanıt verin  {pdf_text} Soru: {question}"
    result = model.invoke(input=input_text)

    # Sonucu yazdır
    print(f"Cevap: {result}")


# .\chatbot\Scripts\activate          run llma3.1