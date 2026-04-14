from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_book_embeddings(book_texts):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(book_texts)
    return vectorizer, vectors


def find_similar_books(query, vectorizer, book_vectors):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, book_vectors)
    return similarities[0]