"""Шаг 2: несколько адресов и параметр запроса."""

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Сервис работает"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello(name: str = "студент"):
    return {"message": f"Привет, {name}!"}

