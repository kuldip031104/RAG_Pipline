from pdf_loader import load_pdf

pages = load_pdf(r"C:\Users\KULDIP\OneDrive\Desktop\Bluepixel\RAG\MAHABHARATA_PRO\data\The Complete Mahabharata .pdf")
print("Total pages:", len(pages))
print(pages[0]["text"][:500])
