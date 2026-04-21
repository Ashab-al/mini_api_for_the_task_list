from typing import AsyncGenerator
from models.task import Task


database: list[Task] = []
"""
In-memory база данных задач.

Description:
    Хранит список задач в виде объектов модели Task (Pydantic).
    Используется как временное хранилище в памяти приложения.

Structure:
    list[Task]: список объектов Task
"""

async def get_database() -> AsyncGenerator[list[Task], None]:
    """
    Dependency для получения in-memory хранилища задач.

    Используется в FastAPI через Depends для доступа к временному
    списку задач, хранящемуся в памяти приложения.

    Yields:
        list[Task]: Список объектов Task, представляющих текущее хранилище задач.
    """
    yield database
