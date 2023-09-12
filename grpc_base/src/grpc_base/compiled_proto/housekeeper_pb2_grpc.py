# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import housekeeper_pb2 as housekeeper__pb2


class HouseKeeperServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllHouseKeepers = channel.unary_stream(
                '/housekeeper.HouseKeeperService/GetAllHouseKeepers',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=housekeeper__pb2.HouseKeeper.FromString,
                )
        self.GetOneHouseKeeper = channel.unary_unary(
                '/housekeeper.HouseKeeperService/GetOneHouseKeeper',
                request_serializer=housekeeper__pb2.IdRequest.SerializeToString,
                response_deserializer=housekeeper__pb2.HouseKeeper.FromString,
                )
        self.CreateHouseKeeper = channel.unary_unary(
                '/housekeeper.HouseKeeperService/CreateHouseKeeper',
                request_serializer=housekeeper__pb2.HouseKeeperCreate.SerializeToString,
                response_deserializer=housekeeper__pb2.HouseKeeper.FromString,
                )
        self.UpdateByIdHouseKeeper = channel.unary_unary(
                '/housekeeper.HouseKeeperService/UpdateByIdHouseKeeper',
                request_serializer=housekeeper__pb2.HouseKeeperUpdate.SerializeToString,
                response_deserializer=housekeeper__pb2.HouseKeeper.FromString,
                )
        self.DeleteByIdHouseKeeper = channel.unary_unary(
                '/housekeeper.HouseKeeperService/DeleteByIdHouseKeeper',
                request_serializer=housekeeper__pb2.IdRequest.SerializeToString,
                response_deserializer=housekeeper__pb2.HouseKeeper.FromString,
                )


class HouseKeeperServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllHouseKeepers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOneHouseKeeper(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateHouseKeeper(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateByIdHouseKeeper(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteByIdHouseKeeper(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HouseKeeperServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllHouseKeepers': grpc.unary_stream_rpc_method_handler(
                    servicer.GetAllHouseKeepers,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=housekeeper__pb2.HouseKeeper.SerializeToString,
            ),
            'GetOneHouseKeeper': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOneHouseKeeper,
                    request_deserializer=housekeeper__pb2.IdRequest.FromString,
                    response_serializer=housekeeper__pb2.HouseKeeper.SerializeToString,
            ),
            'CreateHouseKeeper': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateHouseKeeper,
                    request_deserializer=housekeeper__pb2.HouseKeeperCreate.FromString,
                    response_serializer=housekeeper__pb2.HouseKeeper.SerializeToString,
            ),
            'UpdateByIdHouseKeeper': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateByIdHouseKeeper,
                    request_deserializer=housekeeper__pb2.HouseKeeperUpdate.FromString,
                    response_serializer=housekeeper__pb2.HouseKeeper.SerializeToString,
            ),
            'DeleteByIdHouseKeeper': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteByIdHouseKeeper,
                    request_deserializer=housekeeper__pb2.IdRequest.FromString,
                    response_serializer=housekeeper__pb2.HouseKeeper.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'housekeeper.HouseKeeperService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HouseKeeperService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllHouseKeepers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/housekeeper.HouseKeeperService/GetAllHouseKeepers',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            housekeeper__pb2.HouseKeeper.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOneHouseKeeper(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/housekeeper.HouseKeeperService/GetOneHouseKeeper',
            housekeeper__pb2.IdRequest.SerializeToString,
            housekeeper__pb2.HouseKeeper.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateHouseKeeper(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/housekeeper.HouseKeeperService/CreateHouseKeeper',
            housekeeper__pb2.HouseKeeperCreate.SerializeToString,
            housekeeper__pb2.HouseKeeper.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateByIdHouseKeeper(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/housekeeper.HouseKeeperService/UpdateByIdHouseKeeper',
            housekeeper__pb2.HouseKeeperUpdate.SerializeToString,
            housekeeper__pb2.HouseKeeper.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteByIdHouseKeeper(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/housekeeper.HouseKeeperService/DeleteByIdHouseKeeper',
            housekeeper__pb2.IdRequest.SerializeToString,
            housekeeper__pb2.HouseKeeper.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
