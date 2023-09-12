from typing import List
from fastapi import APIRouter
from app.dto.house_keeper import HouseKeeper,HouseKeeperCreate
import app.service.house_keeper as house_keeper_service
from sqlalchemy.orm import Session

from app.utils import map_db_model_to_dict

router = APIRouter(prefix="/house-keepers", tags=["house-keeper"])


@router.get("/", response_model=List[HouseKeeper], response_model_exclude_none=True)
def get_all():
    return house_keeper_service.get_all()

@router.get("/{id}", response_model=HouseKeeper, response_model_exclude_none=True)
def get_by_id(id: str):
    return house_keeper_service.get_by_id( id)

@router.post("/", response_model=HouseKeeper, response_model_exclude_none=True)
def create(house_keeper: HouseKeeperCreate):
    return house_keeper_service.create( house_keeper)

@router.put("/", response_model=HouseKeeper, response_model_exclude_none=True)
def update( house_keeper: HouseKeeper):
    updated_house_keeper = house_keeper_service.update( house_keeper)
    return HouseKeeper(**map_db_model_to_dict(updated_house_keeper))
    
@router.delete("/{id}", response_model=HouseKeeper, response_model_exclude_none=True)
def delete(id: str):
    deleted_house_keeper = house_keeper_service.delete( id)
    return deleted_house_keeper
    
