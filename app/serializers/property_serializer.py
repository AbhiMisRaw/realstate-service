from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

from app.models import StatusEnum, UnitEnum


class PropertyBase(BaseModel):
    title: str = Field(min_length=8, max_length=200)
    description: Optional[str] = Field(default=None, max_length=200)
    address: str
    city: str = Field(max_length=70)
    country: str = Field(max_length=50)
    pincode: str = Field(max_length=20)
    status: StatusEnum = Field(default=StatusEnum.ACTIVE)
    price: float
    unit: UnitEnum = Field(default=UnitEnum.INR)


class PropertyCreate(PropertyBase):
    pass


class PropertyUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    price: Optional[float]
    city: Optional[str] = Field(min_length=4, max_length=70)
    country: Optional[str] = Field(min_length=5, max_length=50)
    pincode: Optional[str] = Field(min_length=5, max_length=20)
    status: Optional[StatusEnum]
    unit: Optional[UnitEnum]



class PropertyResponse(PropertyBase):
    id: int
    title: str 
    description: Optional[str]
    address: str
    status: StatusEnum
    city: str
    owned_by: int

    class Config:
        from_attributes = True
