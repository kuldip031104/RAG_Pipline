from sentence_transformers import CrossEncoder
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(q,chunks,n=5):
    pairs = [[q,c["text"]] for c in chunks]
    scores = reranker.predict(pairs)
    ranked = sorted(zip(chunks,scores),key=lambda x:x[1],reverse=True)
    return [c for c,_ in ranked[:n]]
