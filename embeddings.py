import faiss
from sentence_transformers import SentenceTransformer
from chunking import chunk_for_summary

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def build_indexes(pages):
    chunks = chunk_for_summary(pages)
    texts = [c["text"] for c in chunks]
    embeddings = embed_model.encode(texts, normalize_embeddings=True)

    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)

    return chunks, index
