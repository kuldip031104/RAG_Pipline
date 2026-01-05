from retrieval import retrieve
from reranker import rerank

def answer(llm, question, store, index):
    chunks = retrieve(question, store, index)
    chunks = rerank(question, chunks)

    if not chunks:
        return "Information not available in document."

    context = "\n".join([c["text"][:1200] for c in chunks])

    prompt = f"""
Use ONLY this text.
Answer in 1–2 sentences.

Text:
{context}

Question: {question}
Answer:
"""
    return llm(prompt).strip()
