from typing import Generic, List, Optional, Type, TypeVar, Union


T = TypeVar("T")

class BaseRepo(Generic[T]):
    model: Type[T]
    NotFoundError: Type[Exception] = ValueError

    def __init__(self, db_session):
        self.db_session = db_session

    def get_all(self) -> List[T]:
        return self.db_session.query(self.model).all()
    
    def get_one(self, id: str) -> Optional[T]:
        return self.db_session.query(self.model).filter(getattr(self.model, "id") == id).first()
    
    def create(self, obj: T) -> T:
        self.db_session.add(obj)
        self.db_session.commit()
        return obj
    
    def update(self, id: str, obj: T) -> T:
        db_obj = self.db_session.query(self.model).filter(getattr(self.model, "id") == id).first()
        if db_obj is None:
            raise self.NotFoundError
        for key, value in obj.__dict__.items():
            if key != "_sa_instance_state":
                setattr(db_obj, key, value)
        self.db_session.commit()
        return db_obj
    
    def delete(self, id: str) -> T:
        db_obj = self.db_session.query(self.model).filter(getattr(self.model, "id") == id).first()
        if db_obj is None:
            raise self.NotFoundError
        self.db_session.delete(db_obj)
        self.db_session.commit()
        return db_obj

