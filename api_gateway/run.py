import asyncio

import uvicorn
from envyaml import EnvYAML
from uvicorn import Config

import app.config.config as cfg
from app.app import create_app


class Server(uvicorn.Server):
    """Customized uvicorn.Server.

    Uvicorn server overrides signals and we need to include Rocketry to the signals.
    """

    def handle_exit(self, sig: int, frame) -> None:
        return super().handle_exit(sig, frame)


async def main():
    "Run scheduler and the API"

    log_config = EnvYAML("logging.yaml").export()

    server = Server(
        config=Config(
            app=create_app(cfg.SV_NAME, cfg.SV_VERSION),
            host=cfg.SV_HOST,
            port=cfg.SV_PORT,
            log_config=log_config,
            reload=False,
        )
    )

    api = asyncio.create_task(server.serve())

    await asyncio.wait([api])


if __name__ == "__main__":
    asyncio.run(main())
