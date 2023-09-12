from pydantic import BaseModel
import uuid
class HouseKeeper(BaseModel):
    id: uuid.UUID
    firstName: str
    lastName: str
    phone: str

class HouseKeeperCreate(BaseModel):
    firstName: str
    lastName: str
    phone: str

class HouseKeeperUpdate(BaseModel):
    firstName: str
    lastName: str
    phone: str