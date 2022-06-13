from fastapi import APIRouter
from typing import List
from pydantic import BaseModel, Field
from db import PyObjectId, db
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

router = APIRouter()
collection = 'students'


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


@router.post('/register', response_model=Student)
async def register_student(student: Student):
    item_model = jsonable_encoder(student)
    await db.insert_one(collection=collection, data=item_model)
    return student


@router.get('/find', response_model=List[Student])
async def get_students():
    students = await db.find(collection=collection, query={})
    students = list(students)
    return students
