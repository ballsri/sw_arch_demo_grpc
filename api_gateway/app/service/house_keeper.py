
from app.dto.house_keeper import HouseKeeperCreate, HouseKeeper as HouseKeeperDto 
from app.errors import HouseKeeperNotFoundError
import grpc_base.compiled_proto.housekeeper_pb2 as housekeeper_pb2
import grpc_base.compiled_proto.housekeeper_pb2_grpc as housekeeper_pb2_grpc
import grpc
import google.protobuf.empty_pb2 as empty_pb2

def get_all():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = housekeeper_pb2_grpc.HouseKeeperServiceStub(channel)
        try:
            # google.protobuf.Empty
            responses = stub.GetAllHouseKeepers(empty_pb2.Empty())
            housekeepers = []
            for response in responses:
                print("Received HouseKeeper:", response)
                housekeeper_dto = HouseKeeperDto(
                    id=response.id,
                    firstName=response.firstName,
                    lastName=response.lastName,
                    phone=response.phone
                )
                housekeepers.append(housekeeper_dto)
        except grpc.RpcError as e:
            raise ValueError(str(e))
    return housekeepers


def get_by_id( id: str):
    # house_keeper = house_keeper_repo(db).get_by_id(id)
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = housekeeper_pb2_grpc.HouseKeeperServiceStub(channel)
        try:
            response = stub.GetOneHouseKeeper(housekeeper_pb2.IdRequest(id=id))
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise HouseKeeperNotFoundError()
            raise ValueError(str(e))
        print("grpc response", response)
    return HouseKeeperDto(
        id=response.id,
        firstName=response.firstName,
        lastName=response.lastName,
        phone=response.phone
    )

def create( house_keeper: HouseKeeperCreate):

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = housekeeper_pb2_grpc.HouseKeeperServiceStub(channel)
        try:
            response = stub.CreateHouseKeeper(
                housekeeper_pb2.HouseKeeperCreate(
                                                    firstName=house_keeper.firstName,
                                                    lastName=house_keeper.lastName,
                                                    phone=house_keeper.phone
                                                ))
        except grpc.RpcError as e:
            raise ValueError(str(e))
        print("grpc response", response)
    return HouseKeeperDto(
        id=response.id,
        firstName=response.firstName,
        lastName=response.lastName,
        phone=response.phone
    )

def update( house_keeper: HouseKeeperDto):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = housekeeper_pb2_grpc.HouseKeeperServiceStub(channel)
        try:
            response = stub.UpdateByIdHouseKeeper(
                housekeeper_pb2.HouseKeeperUpdate(
                    id=str(house_keeper.id),
                    firstName=house_keeper.firstName,
                    lastName=house_keeper.lastName,
                    phone=house_keeper.phone
                    )
                )
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise HouseKeeperNotFoundError()
            raise ValueError(str(e))
        print("grpc response", response)
    return HouseKeeperDto(
        id=response.id,
        firstName=response.firstName,
        lastName=response.lastName,
        phone=response.phone
    )

def delete( id: str):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = housekeeper_pb2_grpc.HouseKeeperServiceStub(channel)
        try:
            response = stub.DeleteByIdHouseKeeper(housekeeper_pb2.IdRequest(id=id))
            if response is None:
                raise HouseKeeperNotFoundError()
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise HouseKeeperNotFoundError()
            raise ValueError(str(e))
        print("grpc response", response)
    return HouseKeeperDto(
        id=response.id,
        firstName=response.firstName,
        lastName=response.lastName,
        phone=response.phone
    )