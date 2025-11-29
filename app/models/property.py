from enum import Enum
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
    Float,
    Enum as SqlEnum,
    DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.utils.db import Base


class StatusEnum(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    SOLD = "Sold"
    INPROGRESS = "Inprogress"


class UnitEnum(str, Enum):
    INR = "INR"
    USD = "USD"
    SGP = "SGP"

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    address = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)
    pincode = Column(String(20), nullable=False)
    price = Column(Float, nullable=False)
    unit = Column(SqlEnum(UnitEnum), nullable=False)
    status = Column(SqlEnum(StatusEnum))
    owned_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    owner = relationship("User", back_populates="properties")