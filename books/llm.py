import os
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_answer(query, book):
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