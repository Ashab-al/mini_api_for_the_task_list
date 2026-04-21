from typing import Annotated
from fastapi import APIRouter, HTTPException, Body
from schemas.api.tasks.create.request import TaskCreateRequest
from schemas.api.tasks.create.response import TaskCreateResponse

router = APIRouter()

@router.post(
    "/tasks",
    summary="Создание таска",
    response_model=TaskCreateResponse
)
async def create_task(
    request: Annotated[TaskCreateRequest, Body()]
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
    ...
