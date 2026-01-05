from pdf_loader import load_pdf
from embeddings import build_faiss
from llm import load_llm
from rag_pipeline import answer

def main():
    print("Loading PDF...")
    pages = load_pdf("data/mahabharata.pdf")

    print("Building index...")
    store, index = build_faiss(pages)

    print("Loading LLM...")
    llm = load_llm("model")

    print("READY ✅\n")

    while True:
        q = input("Ask: ")
        print(answer(llm, q, store, index), "\n")

if __name__ == "__main__":
    main()
