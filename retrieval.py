from embeddings import embed_model

def retrieve(question, store, index, k=6):
    qv = embed_model.encode([question], normalize_embeddings=True)
    _, ids = index.search(qv, k)
    return [store[i] for i in ids[0] if i < len(store)]
