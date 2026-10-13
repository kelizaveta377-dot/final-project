"""Учебная заготовка: этот файл заполняем вместе на занятии."""

from fastapi import FastAPI, HTTPException 
import os

from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="Book Catalog Service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": "1.0.0"}

books_db = [
    {"id": 1, "title": "Мастер и Маргарита", "author": "Михаил Булгаков"},
    {"id": 2, "title": "Война и мир", "author": "Лев Толстой"},
]

@app.get("/books")
def get_books():
    print("[LOG] Запрошен список всех книг")
    return {"books": books_db}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    print(f"[LOG] Запрошена книга с ID {book_id}")

    for book in books_db:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=404, detail=f"Книга с id {book_id} не найдена.")

@app.get("/books/author/")
def search_by_author(author: str):
    print(f"[LOG] Поиск книг автора: {author}")
    result = [book for book in books_db if author.lower() in book["author"].lower()]
    return {"author": author, "books": result}

@app.get("/info")
def info():
    app_name = os.getenv("APP_NAME", "Default Book Service")
    author = os.getenv("APP_AUTHOR", "Не указан")
    version = os.getenv("APP_VERSION", "1.0.0")

    return {
        "service": app_name,
        "version": version,
        "author": author,
    }

