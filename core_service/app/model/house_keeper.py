from app.config.db import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, UUID
import app.utils as utils

class HouseKeeper(Base):
    __tablename__ = "housekeeper"
    id = Column(UUID, primary_key=True, index=True, default= utils.generate_string_uuid)
    firstName = Column(String)
    lastName = Column(String)
    phone = Column(String)
