from typing import List
from fastapi import APIRouter, Depends
from app.config.db import get_db
from app.dto.house_keeper import HouseKeeper,HouseKeeperCreate,HouseKeeperUpdate
import app.service.house_keeper as house_keeper_service
from app.repo.house_keeper import HouseKeeperRepo as house_keeper_repo
from sqlalchemy.orm import Session

from app.utils import map_db_model_to_dict

router = APIRouter(prefix="/house-keepers", tags=["house-keeper"])


@router.get("/", response_model=List[HouseKeeper], response_model_exclude_none=True)
def get_all(db: Session = Depends(get_db)):
    return house_keeper_service.get_all(db)

@router.get("/{id}", response_model=HouseKeeper, response_model_exclude_none=True)
def get_by_id(id: str, db: Session = Depends(get_db)):
    return house_keeper_service.get_by_id(db, id)

@router.post("/", response_model=HouseKeeper, response_model_exclude_none=True)
def create(house_keeper: HouseKeeperCreate, db: Session = Depends(get_db)):
    return house_keeper_service.create(db, house_keeper)

@router.put("/{id}", response_model=HouseKeeper, response_model_exclude_none=True)
def update(id: str, house_keeper: HouseKeeperUpdate, db: Session = Depends(get_db)):
    updated_house_keeper = house_keeper_service.update(db, id, house_keeper)
    return HouseKeeper(**map_db_model_to_dict(updated_house_keeper))
    
@router.delete("/{id}", response_model=HouseKeeper, response_model_exclude_none=True)
def delete(id: str, db: Session = Depends(get_db)):
    deleted_house_keeper = house_keeper_service.delete(db, id)
    return deleted_house_keeper
    
