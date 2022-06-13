from bson import ObjectId
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel, Field
from db import PyObjectId, db
from fastapi.encoders import jsonable_encoder


class Student(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    firstname: str
    lastname: str
    email: str

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "firstname": "kane",
                "lastname": "wera",
                "email": "admin@gmail.com"
            }
        }


app = FastAPI()
collection = 'students'


@app.get('/')
async def index():
    return {'index': 'hello'}


@app.post('/student/register', response_model=Student)
async def register_student(student: Student):
    item_model = jsonable_encoder(student)
    await db.insert_one(collection=collection, data=item_model)
    return student


@app.get('/student/find', response_model=List[Student])
async def get_students():
    students = await db.find(collection=collection, query={})
    students = list(students)
    return students
