import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    name = os.getenv("MY_NAME", "Durelli")
    password = os.getenv("PASSWORD", "pass")
    return {"message": f" Hello World {name} your pass is {password} "}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}