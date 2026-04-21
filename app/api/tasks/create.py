from typing import Annotated
from fastapi import APIRouter, HTTPException, Body, Depends
from schemas.api.tasks.create.request import TaskCreateRequest
from schemas.api.tasks.create.response import TaskCreateResponse
from database import Task, get_database
from services.tasks.create_task import create_task


router = APIRouter()

@router.post(
    "/tasks",
    summary="Создание таска",
    response_model=TaskCreateResponse
)
async def create_task_method(
    request: Annotated[TaskCreateRequest, Body()],
    db: Annotated[list[Task], Depends(get_database)]
):
    """
    Создаёт новый таск на основе переданных данных.

    Args:
        request (TaskCreateRequest): Объект запроса с данными для создания таска,
            валидированный по схеме TaskCreateRequest.

    Returns:
        TaskCreateResponse: Объект ответа, содержащий информацию о созданном таске,
            соответствующий схеме TaskCreateResponse.

    Raises:
        HTTPException: Возникает в случае ошибки при обработке запроса,
            например, при невалидных данных или внутренней ошибке сервера.
    """
    try:
        task = create_task(request, db)
    except Exception as e:
        raise HTTPException(400, str(e)) from e

    return task