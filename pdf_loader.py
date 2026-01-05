import re
import pdfplumber

def clean_page_text(text):
    text = re.sub(r"Canto\s+\d+[:\-]?\s*[A-Za-z\- ]+(Continued)?", " ", text, flags=re.I)
    text = re.sub(r"\b[A-Za-z\- ]+ Parva\b", " ", text, flags=re.I)
    text = re.sub(r"\b[A-Za-z\- ]+ Parva Continued\b", " ", text, flags=re.I)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def load_pdf(path):
    pages = []
    with pdfplumber.open(path) as pdf:
        for i, p in enumerate(pdf.pages):
            text = p.extract_text()
            if not text: 
                continue
            text = clean_page_text(text.replace("\n"," "))
            if len(text.split()) < 120:
                continue
            pages.append({"page":i+1,"text":text})
    return pages
