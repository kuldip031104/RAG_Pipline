📚 Mahabharata RAG – Retrieval Augmented Generation System

An end-to-end RAG (Retrieval Augmented Generation) pipeline for answering questions and generating summaries from the Mahabharata using FAISS + Sentence Transformers + LLM with strict hallucination control.

🚀 Features

PDF ingestion and intelligent cleaning

Semantic chunking for QA and Summary

Sentence-Transformer embeddings

FAISS vector search

Cross-Encoder reranking

Page-number grounded answers

Hallucination blocking

Summary generation with evidence checking

🏗 Project Structure
.
├── app.py
├── rag_pipeline.py
├── pdf_loader.py
├── chunking.py
├── embeddings.py
├── retrieval.py
├── reranker.py
├── llm.py
├── data/
├── model/
└── README.md

🔧 Installation
pip install -r requirements.txt

▶️ Run
python app.py

💬 Example
Ask: Who killed Abhimanyu?
Answer: Abhimanyu was killed by Dusasana’s son inside the Chakravyuh formation. [Page 214]

🛡 Hallucination Control

If the answer is not present in the document:

Information not available in document.


The system never uses outside knowledge.

🧠 Pipeline Flow
PDF → Clean → Chunk → Embed → FAISS Index
User Query → Embed → Retrieve → Rerank → Evidence Check → LLM Answer

👨‍💻 Author
kuldip jadav





