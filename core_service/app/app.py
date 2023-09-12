import json

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import app.config.config as cfg
from app.errors import HTTPExceptionWithCode
from app.config.db import init_db
from app.controller import router

# unused import statement to create the table
import app.model.house_keeper


def create_app(sv_name: str, version: str) -> FastAPI:
    app = FastAPI(
        title=sv_name,
        version=version,
        docs_url="/docs" if cfg.IS_DOCS else None,
        redoc_url="/redoc" if cfg.IS_DOCS else None,
    )

    @app.exception_handler(HTTPExceptionWithCode)
    async def exception_code_handler(_: Request, err: HTTPExceptionWithCode):
        return JSONResponse(
            status_code=err.status_code,
            content={"error_code": err.error_code, "detail": err.detail},
        )

    # @app.on_event("startup")
    # def export_openapi_json():
    #     openapi_schema = app.openapi()
    #     with open("docs/openapi.json", "w") as file:
    #         json.dump(openapi_schema, file, indent=2)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=cfg.ALLOW_ORIGINS.split(","),
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/")
    async def root():
        return "Hello World!"
    
    init_db()

    app.include_router(
        router=router,
        prefix="/api",
        tags=["api"],
    )


    return app


