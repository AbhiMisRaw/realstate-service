from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models import User
from app.redis import RedisWrapper
from app.utils.util import (
    get_password_hash, 
    verify_password, 
    create_access_token,
)


async def handle_login_user(payload, db):
    query = select(User).where(User.email == payload.email)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify password
    if not verify_password(payload.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid credentials"
        )

    # Payload for token
    token_data = {"sub": str(user.id), "email": user.email}
    user_info = {
        "id": user.id,
        "full_name": user.full_name,
        "email": user.email
    }

    # Generate JWT
    access_token = create_access_token(data=token_data)
    print("Saving to cache")
    await RedisWrapper.save_user(email=user.email, user_info=user_info)
    print("saved to db")
    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer",
        "user": user_info
    }


async def handle_user_registration(payload, db):
    # Check if user already exists
    query = select(User).where(User.email == payload.email)
    result = await db.execute(query)
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists with this email"
        )

    hashed_pass = get_password_hash(payload.password)
    new_user = User(
        full_name=payload.full_name,
        email=payload.email,
        password=hashed_pass,
        age=payload.age
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user


async def get_user_by_email(email:str, db: Session):

    user = await RedisWrapper.get_user(email)
    if not user:
        query = select(User).where(User.email == email)
        result = await db.execute(query)
        user = result.scalar_one_or_none()
        user_info = {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email
        }
        await RedisWrapper.save_user(user.email, user_info)
        
    if user:
        return user
    return None