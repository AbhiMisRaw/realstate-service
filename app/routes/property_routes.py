from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.serializers import (
    PropertyCreate, PropertyUpdate, PropertyResponse
)
from app.service.property_service import (
    create_property, get_property_by_id, get_all_properties, 
    update_property, delete_property
)

from app.utils.dependency import get_current_user_from_token, pagination_params
from app.utils.db import get_db
from app.models.user import User


router = APIRouter(prefix="/property", tags=["Property"])


# CREATE
@router.post("/", response_model=PropertyResponse)
async def create_property_api(
    payload: PropertyCreate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user_from_token)
):
    return await create_property(payload, user.id, db)


# READ BY ID
@router.get("/{property_id}", response_model=PropertyResponse)
async def get_property_by_id_api(
    property_id: int,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user_from_token)
):
    property_obj = await get_property_by_id(property_id, db)
    if not property_obj:
        raise HTTPException(status_code=404, detail="Property not found")
    return property_obj


# READ ALL (with pagination)
@router.get("/", response_model=list[PropertyResponse])
async def list_properties_api(
    pagination = Depends(pagination_params),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user_from_token)
):
    return await get_all_properties(pagination, db)


# UPDATE
@router.put("/{property_id}", response_model=PropertyResponse)
async def update_property_api(
    property_id: int,
    payload: PropertyUpdate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user_from_token)
):
    property_obj = await update_property(property_id, payload, db)
    if not property_obj:
        raise HTTPException(status_code=404, detail="Property not found")
    return property_obj


# DELETE
@router.delete("/{property_id}")
async def delete_property_api(
    property_id: int,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user_from_token)
):
    success = await delete_property(property_id, db)
    if not success:
        raise HTTPException(status_code=404, detail="Property not found")

    return {"message": "Property deleted successfully"}
