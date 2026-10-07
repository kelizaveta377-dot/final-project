"""Шаг 1: самое маленькое приложение FastAPI."""

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Сервис работает"}

