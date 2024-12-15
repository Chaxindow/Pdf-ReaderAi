# pdf_reader.py
import fitz  # PyMuPDF kütüphanesi

def read_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()  # Sayfa metnini al
    return text

def get_first_500_words(pdf_text):
    words = pdf_text.split()  # Metni kelimelere ayır
    return ' '.join(words[:500])  # İlk 500 kelimeyi al ve birleştir
