"""Учебная заготовка: этот файл заполняем вместе на занятии."""

from fastapi import FastAPI, HTTPException
import os

app = FastAPI(title="Book Catalog Service")


@app.get("/")
def root():
    return {"message": "Сервис работает"}


@app.get("/health")
def health():
    return {"status": "ok"}


# ВРЕМЕННАЯ БАЗА ДАННЫХ 
books_db = [
    {"id": 1, "title": "Мастер и Маргарита", "author": "Михаил Булгаков"},
    {"id": 2, "title": "Война и мир", "author": "Лев Толстой"},
]

# ПОЛЕЗНЫЕ МАРШРУТЫ 

# 1. Получить список всех книг
@app.get("/books")
def get_books():
    print("[LOG] Запрошен список всех книг")
    return {"books": books_db}

# 2. Получить книгу по ID
@app.get("/books/{book_id}")
def get_book(book_id: int):
    print(f"[LOG] Запрошена книга с ID: {book_id}")
    for book in books_db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")

# 3. Поиск по автору
@app.get("/books/author/")
def search_by_author(author: str):
    print(f"[LOG] Поиск книг автора: {author}")
    result = [book for book in books_db if author.lower() in book["author"].lower()]
    return {"author": author, "books": result}


@app.get("/info")
def info():
    name = os.getenv("APP_NAME", "Default Service")
    author = os.getenv("APP_AUTHOR", "Unknown")
    version = os.getenv("APP_VERSION", "1.0.0")
    return {"service": name, "author": author, "version": version}
