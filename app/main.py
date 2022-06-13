from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get('/')
async def index():
    return JSONResponse(status_code=status.HTTP_200_OK, content={'page': 'first page'})

