from typing import Annotated

from fastapi import APIRouter, Path, Depends, HTTPException
from schemas.api.tasks.detail.response import TaskDetailResponse
from database import Task, get_database
from services.tasks.detail_task_by_id import detail_task_by_id

router = APIRouter()

@router.get(
    "/tasks/{id}",
    summary="Получить таск.",
    description="Возвращает таск по id.",
    response_model=TaskDetailResponse
)
async def detail_task(
    id: Annotated[int, Path(..., ge=0, description="Идентификатор таска")],
    db: Annotated[list[Task], Depends(get_database)]
):
    try:
        task: Task = detail_task_by_id(id, db)
    except ValueError as e:
        raise HTTPException(404, str(e)) from e
    except Exception as e:
        raise HTTPException(400, str(e)) from e

    return task
