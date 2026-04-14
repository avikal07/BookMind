# 📚 BookMind — AI-Powered Book Recommendation & Q&A System

A clean, production-ready Django base project for a Book Recommendation and Q&A system,
architected for seamless AI/RAG integration.

---

## Tech Stack

| Layer       | Technology                      |
|-------------|---------------------------------|
| Backend     | Django 4.2 (Python)             |
| Database    | MySQL                           |
| Frontend    | Django Templates + Bootstrap 5  |
| Env Mgmt    | python-dotenv                   |
| AI (future) | ChromaDB, sentence-transformers |

---

## Features

- 📖 Browse all books on a responsive dashboard
- ➕ Add books via a clean validated form
- 🔍 View full book details — description, reviews, rating
- 🤖 Ask AI page (placeholder, wired for RAG integration)
- 🛠 Django Admin panel for data management

---

## Project Structure

```
book_recommender/
├── manage.py
├── requirements.txt
├── README.md
├── .env.example
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── books/
    ├── __init__.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    ├── admin.py
    ├── static/books/css/
    │   └── style.css
    └── templates/books/
        ├── base.html
        ├── book_list.html
        ├── book_detail.html
        ├── add_book.html
        └── ask.html
```

---

## Setup Instructions

### Prerequisites

- Python 3.10+
- MySQL 8.0+
- pip

---

### Step 1 — Clone the repository

```bash
git clone <your-repo-url>
cd book_recommender
```

### Step 2 — Create and activate a virtual environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Configure environment variables

```bash
cp .env.example .env
```

Open `.env` and fill in your values:

```
SECRET_KEY=your-very-secret-key
DEBUG=True
DB_NAME=book_recommender_db
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```

### Step 5 — Create the MySQL database

Log in to MySQL and run:

```sql
CREATE DATABASE book_recommender_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```

### Step 6 — Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7 — (Optional) Create a superuser

```bash
python manage.py createsuperuser
```

### Step 8 — Start the development server

```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000**

---

## URL Routes

| URL            | View          | Description             |
|----------------|---------------|-------------------------|
| `/`            | book_list     | Dashboard — all books   |
| `/book/add/`   | add_book      | Add a new book          |
| `/book/<pk>/`  | book_detail   | Full book detail page   |
| `/ask/`        | ask_question  | Ask AI (placeholder)    |
| `/admin/`      | Django Admin  | Admin panel             |

---

## How to Run the Project

```bash
# Activate venv (if not already active)
source venv/bin/activate

# Start server
python manage.py runserver

# Access in browser
open http://127.0.0.1:8000
```

---

## Future Improvements (AI/RAG Integration)

| Feature               | Technology                      | Status  |
|-----------------------|---------------------------------|---------|
| Text embeddings       | sentence-transformers           | Planned |
| Vector storage        | ChromaDB                        | Planned |
| Semantic book search  | ChromaDB similarity query       | Planned |
| RAG Q&A pipeline      | LangChain / custom              | Planned |
| LLM response          | OpenAI / local LLM              | Planned |
| User authentication   | Django Auth                     | Planned |
| Reading history       | Extended User model             | Planned |

### How AI will plug in

The `ask_question` view in `books/views.py` already has a placeholder return.
Replace it with:

1. Embed the user query using `sentence-transformers`
2. Query ChromaDB for the top-k similar book chunks
3. Pass retrieved context + query to an LLM
4. Return the generated answer to the template

---

## Zip for Submission

```bash
cd ..
zip -r book_recommender.zip book_recommender/ \
  --exclude "*/venv/*" \
  --exclude "*/__pycache__/*" \
  --exclude "*/*.pyc" \
  --exclude "*/.env"
```

The zip file will appear one level above your project folder.

---

## License

MIT
