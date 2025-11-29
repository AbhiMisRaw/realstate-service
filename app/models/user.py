
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.utils.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    full_name = Column(String(50), nullable=False,)
    email = Column(String(30), nullable=False, unique=True, index=True,)
    password = Column(String(255), nullable=False)
    age = Column(Integer, nullable=True)
    properties = relationship("Property", back_populates="owner")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())