from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class UserLoginModel(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)

class UserRegistrationModel(UserLoginModel):
    full_name: str = Field(min_length=5)
    age: int
    confirm_password: str = Field(min_length=6)

class UserInfoModel():
    full_name: str
    email: EmailStr
    created_at: datetime
    