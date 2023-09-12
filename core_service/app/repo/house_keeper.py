from app.repo.base import BaseRepo
from app.model.house_keeper import HouseKeeper
from app.errors import HouseKeeperNotFoundError
import uuid
class HouseKeeperRepo(BaseRepo[HouseKeeper]):
    model = HouseKeeper
    NotFoundError = HouseKeeperNotFoundError

    def get_by_id(self, id: str):
        house_keeper = self.db_session.query(self.model).filter(self.model.id == id).first()
        if house_keeper is None:
            raise self.NotFoundError
        return house_keeper