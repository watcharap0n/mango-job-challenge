from fastapi import FastAPI
from routers import users

app = FastAPI()

app.include_router(
    users.router,
    prefix='/users',
    tags=['Users'],
    responses={418: {'description': "I'm teapot"}},
)

