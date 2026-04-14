from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(chunks):
    embeddings = model.encode(chunks)
    return embeddings

def combine_book_text(book):
    parts = []

    if book.title:
        parts.append(book.title)

    if book.description:
        parts.append(book.description)

    if book.reviews:
        parts.append(book.reviews)

    return " ".join(parts)


def chunk_text(text, chunk_size=200):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        if chunk.strip():
            chunks.append(chunk)

    return chunks

