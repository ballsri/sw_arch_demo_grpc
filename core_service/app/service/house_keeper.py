from sqlalchemy.orm import Session
from fastapi import Depends
from app.config.db import get_db
from app.dto.house_keeper import HouseKeeperCreate, HouseKeeperUpdate
from app.model.house_keeper import HouseKeeper
from app.repo.house_keeper import HouseKeeperRepo as house_keeper_repo
from app.errors import HouseKeeperNotFoundError


def get_all(db: Session):
    house_keepers = house_keeper_repo(db).get_all()
    return house_keepers

def get_by_id(db: Session, id: str):
    try:
        house_keeper = house_keeper_repo(db).get_by_id(id)
    except HouseKeeperNotFoundError:
        raise HouseKeeperNotFoundError
    return house_keeper

def create(db: Session, house_keeper: HouseKeeperCreate):
    model_house_keeper = HouseKeeper(
        firstName=house_keeper.firstName,
        lastName=house_keeper.lastName,
        phone=house_keeper.phone
    )
    return house_keeper_repo(db).create(model_house_keeper)

def update(db: Session, id: str, house_keeper: HouseKeeperUpdate):
    model_house_keeper = HouseKeeper(
        firstName=house_keeper.firstName,
        lastName=house_keeper.lastName,
        phone=house_keeper.phone
    )
    return house_keeper_repo(db).update(id, model_house_keeper)

def delete(db: Session, id: str):
    return house_keeper_repo(db).delete(id)