from typing import Optional, List
from bson import ObjectId
from pydantic import BaseModel, Field
from db import db, generate_token
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder

router = APIRouter()
collection = 'users'


class User(BaseModel):
    firstname: str = Field(..., example='Watcharapon')
    lastname: str = Field(..., example='Weeraborirak')
    nickname: Optional[str] = Field(None, example='Kane')
    age: Optional[int] = Field(None, example=24)
    major: Optional[str] = Field(None, example='Computer Engineer')
    id_card: str = Field(
        ...,
        example=1102002743832,
        min_length=13,
        max_length=13,
    )


class ID(User):
    id: Optional[str] = Field(None, example='ID ObjectID auto generate')


class Users(BaseModel):
    __root__: List[ID]


def get_user(id_card):
    user = db.find_one(collection='users', query={'id_card': id_card})
    if not user:
        return None
    user = ID(**user)
    return user


async def check_user_duplicate(payload: User):
    user = get_user(payload.id_card)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid user duplicate'
        )
    return payload


@router.post('/', response_model=ID)
async def create_user(payload: User = Depends(check_user_duplicate)):
    Id = generate_token(engine=ObjectId())
    item_model = jsonable_encoder(payload)
    item_model['id'] = Id
    db.insert_one(collection=collection, data=item_model)
    item_store = ID(**item_model)
    return item_store


@router.get('/', response_model=ID)
async def get_users():
    users = db.find(collection=collection, query={})
    users = list(users)
    users = Users.parse_obj(users)
    return users


@router.put('/{id_card}', response_model=User)
async def update_user(payload: User, id_card: Optional[str] = None):
    item_model = jsonable_encoder(payload)
    query = {'id_card': id_card}
    values = {'$set': item_model}
    db.update_one(collection=collection, query=query, values=values)
    return payload


@router.delete('/{id_card}')
async def delete_user(id_card: Optional[str] = None):
    db.delete_one(collection=collection, query={'id_card': id_card})
    return {'detail': f'success deleted {id_card}'}
