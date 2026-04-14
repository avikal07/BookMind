from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm, QuestionForm

from .embeddings import get_book_embeddings, find_similar_books
from .llm import generate_answer

import re


def book_to_text(book):
    return f"""
    Title: {book.title}
    Author: {book.author}
    Description: {book.description}
    Reviews: {book.reviews}
    Rating: {book.rating}
    """



def book_list(request):
    books = Book.objects.all()

    for book in books:
        print(book_to_text(book))  

    return render(request, "books/book_list.html", {"books": books})



def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html", {"book": book})


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "books/add_book.html", {"form": form})




def ask_question(request):
    answer = None
    form = QuestionForm()

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]

            books = Book.objects.all()

            # Handle empty DB
            if not books:
                answer = "⚠️ No books available. Please add some books first."
                return render(request, "books/ask.html", {"form": form, "answer": answer})

            book_texts = [book_to_text(book) for book in books]

            vectorizer, book_vectors = get_book_embeddings(book_texts)
            similarities = find_similar_books(query, vectorizer, book_vectors)

            # 🔥 Dynamic number of results
            n = 3
            match = re.search(r'\d+', query)
            if match:
                n = int(match.group())

            n = min(n, len(books))

            # Get top N
            top_indices = similarities.argsort()[-n:][::-1]
            top_books = [books[int(i)] for i in top_indices]

            # Try LLM (best book only)
            try:
                answer = generate_answer(query, top_books[0])
            except Exception as e:
                print("API ERROR:", e)

                # Fallback response
                answer = "📚 Top Recommendations:<br>"
                for i, book in enumerate(top_books, 1):
                    answer += f"{i}. {book.title} by {book.author}<br>"

    return render(request, "books/ask.html", {"form": form, "answer": answer})