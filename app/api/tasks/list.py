from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from schemas.api.tasks.list.response import TaskListResponse
from services.tasks.list_tasks import list_tasks
from database import Task, get_database


router = APIRouter()

@router.get(
    "/tasks",
    summary="Получить все таски.",
    description="Возвращает все таски.",
    response_model=list[TaskListResponse]
)
async def list_tasks_method(
    db: Annotated[list[Task], Depends(get_database)]
):
    try:
        tasks: list[Task] = list_tasks(db)
    except ValueError as e:
        raise HTTPException(404, str(e)) from e
    except Exception as e:
        raise HTTPException(400, str(e)) from e

    return tasks
