from fastapi import APIRouter, Path
from schemas.api.tasks.detail.response import TaskDetailResponse

router = APIRouter()

@router.get(
    "/tasks/{id}",
    summary="Получить таск.",
    description="Возвращает таск по id.",
    response_model=TaskDetailResponse
)
async def detail_task(
    id: int = Path(..., ge=0, description="Идентификатор таска")
):
    ...
