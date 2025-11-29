import os
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils.db import get_db
from app.service import get_user_by_email
from app.constants import JWT_SECRET_KEY, ALGORITHM

# Reusable security scheme
token_auth_scheme = HTTPBearer()


async def get_current_user_from_token(
    credentials: HTTPAuthorizationCredentials = Depends(token_auth_scheme),
    db: AsyncSession = Depends(get_db)
):
    token = credentials.credentials.split(" ")[1]

    # Decode the JWT token
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        email: str = payload.get("email")

        if email is None:
            print("No payload")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token",
            )
    except JWTError:
        print("Any error")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    # Load user from DB
    user = await get_user_by_email(email, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user



from fastapi import Query

class Pagination:
    def __init__(self, page: int, limit: int):
        self.page = page
        self.limit = limit
        self.offset = (page - 1) * limit


async def pagination_params(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100)
):
    return Pagination(page, limit)
