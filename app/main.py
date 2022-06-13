"""
uvicorn main:app --port {$port} --reload
pattern MVC
main.py
"""

from fastapi import FastAPI
from crud import student

app = FastAPI()

app.include_router(
    student.router,
    prefix='/student',
    tags=['Student'],
)


@app.get('/')
async def index():
    return {'index': 'hello'}
