import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def generate_answer(query, book):
    api_key = os.getenv("OPENAI_API_KEY")

    # If no API key → trigger fallback
    if not api_key:
        raise Exception("No API key found")

    client = OpenAI(api_key=api_key)

    prompt = f"""
    User asked: {query}

    Recommended Book:
    Title: {book.title}
    Author: {book.author}
    Description: {book.description}

    Explain why this book is a good recommendation in a friendly way.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content