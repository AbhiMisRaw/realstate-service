from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer

from app.serializers import UserRegistrationModel, UserLoginModel
from app.models.user import User
from app.utils.db import get_db
from app.redis import get_redis
from app.utils.dependency import get_current_user_from_token
from app.service.user_service import (
    handle_login_user,
    handle_user_registration
)

router = APIRouter(prefix="/auth", tags=["Auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


@router.post("/register")
async def register_user(payload: UserRegistrationModel, db: AsyncSession = Depends(get_db)):
    return await handle_user_registration(payload, db)


@router.post("/login")
async def login_user(payload: UserLoginModel, db: AsyncSession = Depends(get_db)):
    return await handle_login_user(payload, db)


@router.get("/me")
async def current_user(user : User = Depends(get_current_user_from_token)):
    print(user)
    return {
        "id": user.id,
        "email": user.email,
        "name": user.full_name
    }

