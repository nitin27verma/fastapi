from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "FastAPI World"}


@app.get("/name/{value}")
def read_item(value: str):
    return {"Hello": value}

# uvicorn main:app --reload
# uvicorn server
# main refers to the main.py file.
# app refers to the FastAPI instance created in main.py
# --reload enables automatic reloading of the server when you make changes to your code
# http://127.0.0.1:8000/docs