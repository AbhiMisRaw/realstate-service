from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import Property
from app.serializers import (
    PropertyCreate, PropertyUpdate, PropertyResponse
)


async def create_property(payload: PropertyCreate, user_id: int, db: AsyncSession):
    property_obj = Property(
        **(payload.model_dump()),
        owned_by=user_id
    )
    db.add(property_obj)
    await db.commit()
    await db.refresh(property_obj)
    return property_obj


async def get_property_by_id(property_id: int, db: AsyncSession):
    result = await db.execute(
        select(Property).where(Property.id == property_id)
    )
    return result.scalar_one_or_none()


async def get_all_properties(pagination, db: AsyncSession):
    query = select(Property).offset(pagination.offset).limit(pagination.limit)
    result = await db.execute(query)
    return result.scalars().all()


async def update_property(property_id: int, payload: PropertyUpdate, db: AsyncSession):
    property_obj = await get_property_by_id(property_id, db)
    if not property_obj:
        return None

    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(property_obj, key, value)

    await db.commit()
    await db.refresh(property_obj)
    return property_obj


async def delete_property(property_id: int, db: AsyncSession):
    property_obj = await get_property_by_id(property_id, db)
    if not property_obj:
        return None

    await db.delete(property_obj)
    await db.commit()
    return True
