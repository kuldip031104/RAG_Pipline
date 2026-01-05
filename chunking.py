def chunk_for_summary(pages, size=800, overlap=150):
    chunks, buffer_words, buffer_pages = [], [], []

    for p in pages:
        words = p["text"].split()
        buffer_words.extend(words)
        buffer_pages.append(p["page"])

        if len(buffer_words) >= size:
            chunks.append({
                "pages": buffer_pages.copy(),
                "text": " ".join(buffer_words[:size])
            })
            buffer_words = buffer_words[size-overlap:]
            buffer_pages = buffer_pages[-3:]

    if buffer_words:
        chunks.append({"pages": buffer_pages, "text": " ".join(buffer_words)})

    return chunks
