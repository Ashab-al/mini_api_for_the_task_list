from fastapi import APIRouter
from api.tasks.create import router as create_router
from api.tasks.detail import router as detail_router
from api.tasks.list import router as list_router

router = APIRouter()

router.include_router(create_router)
router.include_router(detail_router)
router.include_router(list_router)
