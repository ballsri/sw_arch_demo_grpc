from app.errors import HouseKeeperNotFoundError
from app.dto.house_keeper import HouseKeeperCreate, HouseKeeperUpdate
import app.service.house_keeper as house_keeper_service
import app.config.db as db
import grpc
from grpc_base.compiled_proto import housekeeper_pb2_grpc
from grpc_base.compiled_proto.housekeeper_pb2 import HouseKeeper


class HouseKeeperGrpc(housekeeper_pb2_grpc.HouseKeeperServiceServicer):
    def GetOneHouseKeeper(self, request, context):
        db_session = db.SessionLocal()
        try:
            housekeeper = house_keeper_service.get_by_id(db = db_session, id = request.id)
            return HouseKeeper(id = str(housekeeper.id), firstName = housekeeper.firstName, lastName = housekeeper.lastName, phone = housekeeper.phone)
        except Exception as e:
            print(e)
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            if isinstance(e, HouseKeeperNotFoundError):
                context.set_code(grpc.StatusCode.NOT_FOUND)
            return HouseKeeper()
        
    def GetAllHouseKeepers(self, request, context):
        db_session = db.SessionLocal()
        try:
            housekeepers = house_keeper_service.get_all(db=db_session)
            print("housekeepers", housekeepers)
            for housekeeper in housekeepers:
                print("housekeeper", housekeeper)
                yield HouseKeeper(id = str(housekeeper.id), firstName = housekeeper.firstName, lastName = housekeeper.lastName, phone = housekeeper.phone)
        except Exception as e:
            print(e)
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return  # No need to yield a default HouseKeeper here
        finally:
            db_session.close()  # Always close your session

        
    def CreateHouseKeeper(self, request, context):
        db_session = db.SessionLocal()
        try:
            model_house_keeper = HouseKeeperCreate(
                firstName=request.firstName,
                lastName=request.lastName,
                phone=request.phone
            )
            housekeeper = house_keeper_service.create(db = db_session, house_keeper = model_house_keeper)
            return HouseKeeper(id = housekeeper.id, firstName = housekeeper.firstName, lastName = housekeeper.lastName, phone = housekeeper.phone)
        except Exception as e:
            print(e)
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return HouseKeeper()
        
    def UpdateByIdHouseKeeper(self, request, context):
        db_session = db.SessionLocal()
        try:
            model_house_keeper = HouseKeeperUpdate(
                firstName=request.firstName,
                lastName=request.lastName,
                phone=request.phone
            )
            housekeeper = house_keeper_service.update(db = db_session, id = request.id, house_keeper = model_house_keeper)
            return HouseKeeper(id = str(housekeeper.id), firstName = housekeeper.firstName, lastName = housekeeper.lastName, phone = housekeeper.phone)
        except Exception as e:

            print(e)
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            if isinstance(e, HouseKeeperNotFoundError):
                context.set_code(grpc.StatusCode.NOT_FOUND)
            return HouseKeeper()
        
    def DeleteByIdHouseKeeper(self, request, context):
        db_session = db.SessionLocal()
        try:
            deleted_house_keeper = house_keeper_service.delete(db = db_session, id = request.id)
            return HouseKeeper(
                id = str(deleted_house_keeper.id),
                firstName = deleted_house_keeper.firstName,
                lastName = deleted_house_keeper.lastName,
                phone = deleted_house_keeper.phone
            )

        except Exception as e:
            print(e)
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            if isinstance(e, HouseKeeperNotFoundError):
                context.set_code(grpc.StatusCode.NOT_FOUND)
            return HouseKeeper()