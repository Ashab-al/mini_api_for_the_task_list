from fastapi import APIRouter
from schemas.api.tasks.list.response import TaskListResponse


router = APIRouter()

@router.get(
    "/tasks",
    summary="Получить все таски.",
    description="Возвращает все таски.",
    response_model=list[TaskListResponse]
)
async def list_task():
    ...
