from fastapi import APIRouter

from app.controller.v1.house_keeper import (
    router as house_keeper_router,
)


router = APIRouter(prefix="/v1")

router.include_router(house_keeper_router)
