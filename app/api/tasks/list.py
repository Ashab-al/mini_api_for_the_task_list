from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from schemas.api.tasks.list.response import TaskListResponse
from services.tasks.find_all_tasks import find_all_tasks
from database import Task, get_database


router = APIRouter()

@router.get(
    "/tasks",
    summary="Получить все таски.",
    description="Возвращает все таски.",
    response_model=list[TaskListResponse]
)
async def list_task(
    db: Annotated[list[Task], Depends(get_database)]
):
    try:
        tasks = await find_all_tasks(db)
    except Exception as e:
        raise HTTPException(400, str(e)) from e

    return tasks
