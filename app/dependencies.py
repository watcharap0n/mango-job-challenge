from fastapi import Header, HTTPException, status
from typing import Optional


async def sy_token_header(sy_token: Optional[str] = Header(None)):
    if not sy_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='not unauthorized!'
        )
    if sy_token != 'watcharapon':
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='not invalid header!'
        )
