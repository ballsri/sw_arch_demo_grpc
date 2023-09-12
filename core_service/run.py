import asyncio
import grpc
import uvicorn
from concurrent import futures
import app.config.config as cfg
from app.app import create_app
from app.controller.grpc.housekeeper import HouseKeeperGrpc
import grpc_base.compiled_proto.housekeeper_pb2_grpc as housekeeper_pb2_grpc

# Declare gRPC server as global so it can be accessed in different functions
grpc_server = None

class Server(uvicorn.Server):
    def handle_exit(self, sig: int, frame) -> None:
        return super().handle_exit(sig, frame)
    
    def shutdown(self, signal: int, sockets=None) -> None:
        # Stop gRPC server
        global grpc_server
        if grpc_server:
            grpc_server.stop(0)
        return super().shutdown(signal, sockets=sockets)


async def main():
    print("Starting main()...")
    server = Server(
        config=uvicorn.Config(
            app=create_app(cfg.SV_NAME, cfg.SV_VERSION),
            host=cfg.SV_HOST,
            port=cfg.SV_PORT,
            reload=True,
        )
    )

    print("Creating API task...")
    api = asyncio.create_task(server.serve())
    await asyncio.wait([api])

    print("Finished main()...")

def serve_grpc():
    global grpc_server

    print("Starting gRPC...")
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    housekeeper_pb2_grpc.add_HouseKeeperServiceServicer_to_server(HouseKeeperGrpc(), grpc_server)
    grpc_server.add_insecure_port('[::]:50051')
    grpc_server.start()
    print("gRPC server started at port 50051")
    grpc_server.wait_for_termination()

if __name__ == "__main__":
    import threading

    # Start gRPC server in a background thread
    t = threading.Thread(target=serve_grpc)
    t.start()

    print("Starting FastAPI server...")
    asyncio.run(main())
